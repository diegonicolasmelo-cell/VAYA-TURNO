#!/usr/bin/env python3
"""App jugable de ¡VAYA TURNO! v0.30 — dos formatos desde la misma plantilla

Inyecta los mazos de `cartas/v030/` (y los pacientes/personajes de
`cartas/`) dentro de `tools/app-plantilla.html`. El formato final del juego
es FÍSICO: esto existe para probar reglas donde no se puedan llevar las
cartas.

    python3 tools/generar_app.py          → docs/app.html
    python3 tools/generar_app.py --pwa    → docs/juego/  (app instalable)

**docs/app.html** es el archivo suelto que se publica como artefacto: todo
va adentro, incluido el arte en base64, porque ahí no se pueden pedir
archivos externos. Tope duro de 16 MB.

**docs/juego/** es la app instalable (PWA) que se sirve por GitHub Pages:
el arte sale a archivos aparte y el service worker los cachea uno a uno,
así el HTML queda liviano, el navegador solo re-descarga lo que cambió y
no hay tope de peso. Trae además manifest e íconos para que el teléfono la
instale con su propio ícono, a pantalla completa y sin internet.

Esa carpeta se versiona a propósito (Pages sirve archivos, no scripts);
por eso es la única salida generada que NO está en .gitignore.
"""

import base64
import csv
import hashlib
import io
import json
import os
import shutil
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLANTILLA = os.path.join(RAIZ, "tools", "app-plantilla.html")
SALIDA = os.path.join(RAIZ, "docs", "app.html")
SALIDA_PWA = os.path.join(RAIZ, "docs", "juego")
NOMBRE = "¡Vaya Turno!"
LEMA = ("Guardia virtual de ¡Vaya Turno!: el juego de cartas de triage en "
        "UCI, contra la máquina o entre dos en el mismo teléfono.")
TEMA = "#0a5860"      # el teal del ícono; pinta la barra de estado
FONDO = "#dfe7ea"
TIPOS = ("IMAGEN", "FARMACOS", "PERSONAL", "PROCEDIMIENTOS")
COL = {"IMAGEN": "img", "FARMACOS": "far", "PERSONAL": "per",
       "PROCEDIMIENTOS": "proc"}


def leer(*partes):
    with open(os.path.join(RAIZ, *partes), encoding="utf-8") as f:
        return list(csv.DictReader(f))


def tinte(im):
    """El color de fondo de una ilustración: la mediana de su borde.

    Sirve para rellenar los costados cuando la imagen no llena el hueco,
    y con arte monocromo —que es lo que tiene este juego— el relleno no se
    nota. Se mide del borde y no de la imagen entera porque el borde ES el
    fondo: el personaje vive al centro."""
    ch = im.convert("RGB").resize((40, 40))
    px = list(ch.im)          # getdata() está deprecado en Pillow 14
    borde = ([px[i] for i in range(40)] + [px[40 * 39 + i] for i in range(40)] +
             [px[f * 40] for f in range(40)] + [px[f * 40 + 39] for f in range(40)])
    med = [sorted(c[k] for c in borde)[len(borde) // 2] for k in range(3)]
    return "#%02x%02x%02x" % tuple(med)


def cargar_arte(destino=None):
    """cartas/arte/<id>.(png|jpg|webp) → la referencia que usará la carta.

    Se recomprime a WebP ~500 px siempre. Con `destino`, cada imagen se
    escribe como archivo y la carta recibe una ruta relativa (`arte/C01.webp`):
    es el modo PWA, donde el service worker cachea cada archivo por separado.
    Sin `destino`, vuelve como data-URI incrustado (modo artefacto)."""
    carpeta = os.path.join(RAIZ, "cartas", "arte")
    arte, tintes = {}, {}
    if destino:
        # una imagen retirada de cartas/arte/ no puede quedar de zombi
        shutil.rmtree(destino, ignore_errors=True)
        os.makedirs(destino, exist_ok=True)
    if not os.path.isdir(carpeta):
        return arte, tintes
    try:
        from PIL import Image
    except ImportError:
        Image = None
    for nombre in sorted(os.listdir(carpeta)):
        raiz, ext = os.path.splitext(nombre)
        if ext.lower() not in (".png", ".jpg", ".jpeg", ".webp"):
            continue
        ruta = os.path.join(carpeta, nombre)
        datos_img = open(ruta, "rb").read()
        mime = "image/webp"
        if Image is not None:
            im = Image.open(io.BytesIO(datos_img)).convert("RGB")
            tintes[raiz.upper()] = tinte(im)
            # 800 px de ancho: el hueco más grande del juego es el zoom
            # (342 px de CSS → 1026 px reales en un teléfono 3×), así que
            # 520 se veía blando. Con el arte en 4:3 subir a 800 sale
            # gratis: la fuente 9:16 de antes gastaba dos tercios de sus
            # píxeles en la parte que el recorte tiraba, y a 800 el 4:3
            # pesa lo mismo (46 KB por carta contra 42) mostrando un 54 %
            # más de resolución. Medido sobre las diez ilustraciones que
            # hay: 115 cartas ≈ 5,2 MB, igual que hoy.
            if im.width > 800:
                im = im.resize((800, round(im.height * 800 / im.width)))
            buf = io.BytesIO()
            im.save(buf, "WEBP", quality=80)
            if buf.tell() < len(datos_img):
                datos_img = buf.getvalue()
            else:
                mime = {".png": "image/png", ".webp": "image/webp"}.get(
                    ext.lower(), "image/jpeg")
        else:
            mime = {".png": "image/png", ".webp": "image/webp"}.get(
                ext.lower(), "image/jpeg")
        if destino:
            # el nombre del archivo es el id: la ruta queda predecible
            ext_s = {"image/webp": ".webp", "image/png": ".png"}.get(mime, ".jpg")
            archivo = raiz.upper() + ext_s
            with open(os.path.join(destino, archivo), "wb") as f:
                f.write(datos_img)
            arte[raiz.upper()] = "arte/" + archivo
        else:
            arte[raiz.upper()] = ("data:" + mime + ";base64,"
                                  + base64.b64encode(datos_img).decode())
    return arte, tintes


def cargar_portada(destino=None):
    """arte/portada/portada.(mp4|jpg) → el fondo vivo de la pantalla de inicio.

    Mismo trato que el arte de cartas: data-URI en el artefacto, archivo
    aparte en la PWA. El video pesa ~2 MB, así que en la PWA importa que
    sea un archivo propio y no parte del HTML: el service worker lo cachea
    solo, y una corrección de reglas no obliga a bajarlo de nuevo."""
    carpeta = os.path.join(RAIZ, "arte", "portada")
    out = {"video": "", "cuadro": "", "dibujo": "", "logo": "", "salida": ""}
    for clave, nombre, mime in (("video", "portada.mp4", "video/mp4"),
                                ("cuadro", "portada.jpg", "image/jpeg"),
                                ("dibujo", "dibujo.svg", "image/svg+xml"),
                                ("logo", "logo.webp", "image/webp"),
                                # el pasillo de salida: fondo del marcador
                                # final, cuando se cuentan los puntos
                                ("salida", "salida.webp", "image/webp")):
        ruta = os.path.join(carpeta, nombre)
        if not os.path.isfile(ruta):
            continue
        crudo = open(ruta, "rb").read()
        if destino:
            os.makedirs(destino, exist_ok=True)
            with open(os.path.join(destino, nombre), "wb") as f:
                f.write(crudo)
            out[clave] = "portada/" + nombre
        else:
            out[clave] = ("data:" + mime + ";base64,"
                          + base64.b64encode(crudo).decode())
    return out


def datos(destino_arte=None):
    pacientes = []
    for p in leer("cartas", "pacientes.csv"):
        pide = {t: int(p[COL[t]]) for t in TIPOS}
        pacientes.append({
            "id": p["id"], "nombre": p["nombre"], "gravedad": p["gravedad"],
            # v0.58 · la Entrega de Turno: la edad y la línea con que la
            # colega que sale te pasa el paciente. Las dos pueden venir
            # vacías — la pantalla se apaña con lo que haya.
            "edad": (p.get("edad") or "").strip(),
            "entrega": (p.get("entrega") or "").strip(),
            # v0.60 · la contraindicación: el recurso que este paciente
            # aceptaría por tipo y que, en él, está prohibido. Es el que
            # convierte «pide 2 💊» en una decisión clínica: dice cuál NO.
            "contra": (p.get("contra") or "").strip(),
            "sistema": p["sistema"], "vida": int(p["vida"]), "pide": pide,
            "total": sum(pide.values()),
            "alta": int(p["puntos_alta"]), "fallece": int(p["puntos_fallece"]),
            "frase": p["frase"], "copias": int(p.get("copias") or 1),
        })

    recursos = []
    for r in leer("cartas", "v030", "recursos.csv"):
        recursos.append({
            "id": r["id"], "nombre": r["nombre"], "tipo": r["tipo"],
            "sistema": r["sistema"], "comodin": r["comodin"] == "si",
            "restriccion": r["restriccion"], "previene": r["previene"],
            "texto": r["texto"], "frase": r["frase"],
            "warn": r["complicacion"] == "si",
            "compNombre": r["comp_nombre"], "compTexto": r["comp_texto"],
            # v0.60 · el tipo en el que esta carta vale por DOS. Antes era
            # un id cableado (R54, el Cirujano); ahora es una columna, y con
            # ella los comodines dejan de valer 1 en todo: cada uno tiene su
            # casa —el Stock de Sala ×2 en 💊, el Médico General ×2 en 🧑‍⚕️—
            # y fuera de ella sigue siendo un relleno de 1.
            "dobleEn": (r.get("doble_en") or "").strip(),
            # v0.61 · el soporte vital no cura: para el reloj. Mientras
            # esta carta siga puesta, el paciente no se deteriora al Fin
            # de Guardia. Es el segundo modo de congelar el reloj —el
            # primero es el ✅— y el único que se puede desconectar.
            "soporte": (r.get("soporte") or "").strip() == "si",
            "turno24": r["comp_nombre"] == "El Turno Veinticuatro",
            "copias": int(r["copias"]),
        })

    acciones = [{
        "id": a["id"], "nombre": a["nombre"], "tipo": a["tipo"],
        "coste": int(a["coste"]), "texto": a["texto"], "frase": a["frase"],
        "copias": int(a["copias"]),
    } for a in leer("cartas", "v030", "acciones.csv")]

    personajes = [{
        "id": c["id"], "nombre": c["nombre"], "frecuencia": c["frecuencia"],
        "habilidad": c["habilidad"], "frase": c["frase"],
    } for c in leer("cartas", "personajes.csv")]

    arte, tintes = cargar_arte(destino_arte)
    for lista in (pacientes, recursos, acciones, personajes):
        for c in lista:
            if c.get("id") and c["id"].upper() in arte:
                c["arte"] = arte[c["id"].upper()]
                if c["id"].upper() in tintes:
                    c["tinte"] = tintes[c["id"].upper()]
        # Hay cartas repetidas con ids distintos: R32 y R33 son las dos
        # «Gases Arteriales», y son la misma carta dos veces en el mazo. No
        # tiene sentido pedir el archivo dos veces ni pesarlo dos veces en el
        # artefacto: si una copia tiene arte, sus gemelas lo heredan. La
        # herencia es por nombre y dentro de la misma lista, que es donde el
        # nombre identifica de verdad a la carta.
        porta = {c["nombre"]: c for c in lista if c.get("arte")}
        for c in lista:
            gemela = porta.get(c.get("nombre"))
            if gemela is not None and not c.get("arte"):
                c["arte"] = gemela["arte"]
                if gemela.get("tinte"):
                    c["tinte"] = gemela["tinte"]
    if arte:
        usados = {c["id"].upper() for l in (pacientes, recursos, acciones,
                  personajes) for c in l if c.get("arte")}
        sueltos = set(arte) - usados
        print(f"  arte: {len(usados)} cartas ilustradas" +
              (f" · sin dueño: {', '.join(sorted(sueltos))}" if sueltos else ""))
    return {"pacientes": pacientes, "recursos": recursos,
            "acciones": acciones, "personajes": personajes}


def armar(d, pwa=False, css_local=None, portada=None):
    """Mete los datos en la plantilla. En modo PWA además la envuelve en un
    documento completo: la plantilla es un fragmento (el artefacto le pone
    la cabecera), pero un archivo servido por Pages necesita la suya."""
    with open(PLANTILLA, encoding="utf-8") as f:
        plantilla = f.read()
    marca = "/*__DATOS__*/{}"
    if marca not in plantilla:
        raise SystemExit("La plantilla no tiene el marcador /*__DATOS__*/{}")
    html = plantilla.replace(marca, json.dumps(d, ensure_ascii=False,
                                               separators=(",", ":")))
    for clave, hueco in (("video", '/*__PORTADA_VIDEO__*/""'),
                         ("cuadro", '/*__PORTADA_CUADRO__*/""'),
                         ("dibujo", '/*__PORTADA_DIBUJO__*/""'),
                         ("logo", '/*__PORTADA_LOGO__*/""'),
                         ("salida", '/*__PORTADA_SALIDA__*/""')):
        if hueco not in html:
            raise SystemExit("La plantilla no tiene el marcador " + hueco)
        html = html.replace(hueco, json.dumps((portada or {}).get(clave, "")), 1)
    if not pwa:
        return html
    html = html.replace("/*__PWA__*/false", "/*__PWA__*/true", 1)
    if css_local:
        # la app instalada no le pide las letras a Google: las trae consigo
        google = [l for l in html.split("\n")
                  if "fonts.googleapis.com" in l or "fonts.gstatic.com" in l]
        for l in google:
            html = html.replace(l + "\n", "", 1)
        html = html.replace("<title>", '<link rel="stylesheet" href="'
                            + css_local + '">\n<title>', 1)
    corte = '<div class="app" id="app">'
    if corte not in html:
        raise SystemExit("La plantilla ya no empieza el cuerpo con " + corte)
    cabeza, cuerpo = html.split(corte, 1)
    cuerpo = corte + cuerpo
    return f"""<!doctype html>
<html lang="es-CL">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="{LEMA}">
<meta name="theme-color" content="{TEMA}">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" href="iconos/icono-192.png" sizes="192x192">
<link rel="apple-touch-icon" href="iconos/apple-touch-icon.png">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="{NOMBRE}">
{cabeza}</head>
<body>
{cuerpo}
</body>
</html>
"""


def manifiesto():
    return json.dumps({
        # sin "id": por defecto es start_url, que ya identifica la app y no
        # se rompe si mañana cambia la carpeta donde se publica
        "name": NOMBRE + " — Guardia Virtual",
        "short_name": NOMBRE,
        "description": LEMA,
        "lang": "es-CL",
        "dir": "ltr",
        "categories": ["games"],
        "start_url": ".",
        "scope": ".",
        "display": "standalone",
        "orientation": "portrait",
        "background_color": FONDO,
        "theme_color": TEMA,
        "icons": [
            {"src": "iconos/icono-192.png", "sizes": "192x192",
             "type": "image/png", "purpose": "any"},
            {"src": "iconos/icono-512.png", "sizes": "512x512",
             "type": "image/png", "purpose": "any"},
            {"src": "iconos/icono-maskable-512.png", "sizes": "512x512",
             "type": "image/png", "purpose": "maskable"},
        ],
    }, ensure_ascii=False, indent=2) + "\n"


def worker(version, arte_urls, tipos):
    """El service worker: es lo que hace que la app abra sin internet.

    El HTML va por RED PRIMERO (así una versión nueva llega al recargar y
    nadie queda pegado en una vieja) con la caché de respaldo; el resto
    —arte, íconos, tipografías— por CACHÉ PRIMERO, que no cambia y es lo
    que más pesa. El arte se precarga sin bloquear: si una imagen falla,
    la instalación igual termina."""
    nucleo = ["./", "index.html", "manifest.webmanifest",
              "iconos/icono-192.png", "iconos/icono-512.png",
              "iconos/icono-maskable-512.png", "iconos/apple-touch-icon.png"]
    nucleo += sorted(tipos)      # las letras son parte de la identidad: van al núcleo
    return f"""/* ¡Vaya Turno! — service worker generado por tools/generar_app.py.
   No editar a mano: se rehace con `python3 tools/generar_app.py --pwa`. */
const VERSION = "{version}";
const NUCLEO = {json.dumps(nucleo)};
const ARTE = {json.dumps(sorted(arte_urls))};

self.addEventListener("install", ev => {{
  ev.waitUntil((async () => {{
    const c = await caches.open(VERSION);
    await c.addAll(NUCLEO);                                  // sin esto no hay app
    await Promise.allSettled(ARTE.map(u => c.add(u)));       // el arte, si se puede
    self.skipWaiting();
  }})());
}});

self.addEventListener("activate", ev => {{
  ev.waitUntil((async () => {{
    const viejas = (await caches.keys()).filter(k => k !== VERSION);
    await Promise.all(viejas.map(k => caches.delete(k)));
    await self.clients.claim();
  }})());
}});

self.addEventListener("fetch", ev => {{
  const req = ev.request;
  if(req.method !== "GET") return;
  if(req.mode === "navigate"){{
    ev.respondWith((async () => {{
      try {{
        const r = await fetch(req);
        const c = await caches.open(VERSION);
        c.put("index.html", r.clone());
        return r;
      }} catch(e) {{
        return (await caches.match("index.html")) || Response.error();
      }}
    }})());
    return;
  }}
  ev.respondWith((async () => {{
    const hit = await caches.match(req, {{ignoreVary: true}});
    if(hit) return hit;
    try {{
      const r = await fetch(req);
      if(r && (r.ok || r.type === "opaque")){{
        const c = await caches.open(VERSION);
        c.put(req, r.clone());
      }}
      return r;
    }} catch(e) {{
      return Response.error();
    }}
  }})());
}});
"""


def construir_pwa():
    import iconos_pwa
    import tipografias_pwa
    os.makedirs(SALIDA_PWA, exist_ok=True)
    d = datos(destino_arte=os.path.join(SALIDA_PWA, "arte"))
    tipos = tipografias_pwa.preparar(os.path.join(SALIDA_PWA, "tipos"))
    portada = cargar_portada(destino=os.path.join(SALIDA_PWA, "portada"))
    html = armar(d, pwa=True, css_local="tipos/tipos.css" if tipos else None,
                 portada=portada)
    man = manifiesto()
    iconos_pwa.generar(os.path.join(SALIDA_PWA, "iconos"))

    urls = sorted({c["arte"] for l in d.values() for c in l if c.get("arte")})
    # el fondo de la portada va con el arte: caché primero, y si falla la
    # descarga la app igual instala y la portada queda en el cuadro fijo
    urls += [u for u in portada.values() if u]
    # La versión de la caché sale del CONTENIDO de todo lo que se cachea.
    # Antes solo los íconos contaban por su contenido y el resto por su
    # nombre, y eso dejaba un agujero real: reemplazar portada.mp4 por otro
    # clip con el mismo nombre no movía el sello, así que los teléfonos ya
    # instalados se quedaban con el video viejo para siempre. Ahora se
    # calcula la huella de cada archivo que entra a la caché —íconos,
    # tipografías, arte y portada—: si cambia un byte, cambia el sello y el
    # `activate` del worker borra la caché anterior.
    def huella(rel):
        ruta = os.path.join(SALIDA_PWA, rel)
        if not os.path.isfile(ruta):
            return rel                      # no está: cuenta por su nombre
        with open(ruta, "rb") as f:
            return hashlib.sha256(f.read()).hexdigest()

    cacheados = sorted(set(urls) | set(tipos or []) | {
        "iconos/" + n for n in os.listdir(os.path.join(SALIDA_PWA, "iconos"))})
    huellas = "".join(r + huella(r) for r in cacheados)
    sello = hashlib.sha256((html + man + huellas).encode()).hexdigest()[:12]

    with open(os.path.join(SALIDA_PWA, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    with open(os.path.join(SALIDA_PWA, "manifest.webmanifest"), "w",
              encoding="utf-8") as f:
        f.write(man)
    with open(os.path.join(SALIDA_PWA, "sw.js"), "w", encoding="utf-8") as f:
        f.write(worker("vt-" + sello, urls, tipos or []))
    # Pages no sirve carpetas que empiecen con _, pero sí respeta esto:
    with open(os.path.join(SALIDA_PWA, ".nojekyll"), "w") as f:
        f.write("")

    peso = sum(os.path.getsize(os.path.join(r, n))
               for r, _, ns in os.walk(SALIDA_PWA) for n in ns)
    print(f"✔ App instalable → {SALIDA_PWA}/ ({peso // 1024} KB en total)")
    print(f"  index.html {len(html) // 1024} KB · {len(urls)} archivos de arte · "
          f"{len(tipos or [])} archivos de tipografía · caché {sello}")
    return d


def main():
    pwa = "--pwa" in sys.argv[1:]
    if pwa:
        d = construir_pwa()
    else:
        d = datos()
        html = armar(d, portada=cargar_portada())
        os.makedirs(os.path.dirname(SALIDA), exist_ok=True)
        with open(SALIDA, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"✔ App v0.30 → {SALIDA} ({len(html) // 1024} KB)")

    rec = sum(r["copias"] for r in d["recursos"])
    acc = sum(a["copias"] for a in d["acciones"])
    print(f"  {len(d['pacientes'])} pacientes · {rec} recursos · {acc} "
          f"protocolos · {len(d['personajes'])} avatares")


if __name__ == "__main__":
    sys.path.insert(0, os.path.join(RAIZ, "tools"))
    main()
