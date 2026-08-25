#!/usr/bin/env python3
"""Las tipografías, alojadas en casa — solo para la app instalable.

El artefacto tiene que pedirlas a Google (su CSP solo deja pasar
fonts.googleapis/gstatic), pero una app que se instala en el teléfono no
puede depender de un tercero: si el hospital no tiene señal, la portada
saldría en Georgia. Así que en modo --pwa las descargamos una vez, se
guardan junto al juego y quedan versionadas.

Del CSS de Google solo se conservan los subconjuntos **latin y latin-ext**:
el resto (cirílico, griego, vietnamita) son 20 archivos que este juego no
va a usar nunca.

Si los archivos ya están, no se vuelven a bajar: compilar no necesita red.
Con `--refrescar` se fuerza la descarga de nuevo.
"""

import os
import re
import sys
import urllib.request

CSS_URL = ("https://fonts.googleapis.com/css2"
           "?family=Archivo+Narrow:wght@500;600;700"
           "&family=IBM+Plex+Mono:wght@400;500;600"
           "&family=Petrona:ital,wght@0,500;0,700;1,500&display=swap")
# sin un User-Agent de navegador, Google devuelve TTF en vez de woff2
UA = ("Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/120.0.0.0 Mobile Safari/537.36")
SUBCONJUNTOS = ("latin", "latin-ext")


def _bajar(url, cabeceras=None):
    pet = urllib.request.Request(url, headers=cabeceras or {"User-Agent": UA})
    with urllib.request.urlopen(pet, timeout=30) as r:
        return r.read()


def preparar(destino, refrescar=False):
    """Deja `destino/tipos.css` + los .woff2 y devuelve la lista de rutas
    relativas (para el precache del service worker), o None si no se pudo."""
    css_local = os.path.join(destino, "tipos.css")
    if os.path.isfile(css_local) and not refrescar:
        return _listar(destino)

    try:
        css = _bajar(CSS_URL).decode("utf-8")
    except Exception as e:                      # sin red: que siga con Google
        print(f"  tipografías: no se pudieron bajar ({e}); quedan en Google")
        return None

    os.makedirs(destino, exist_ok=True)
    # el CSS viene como  /* latin */\n@font-face{...}  — se parte por comentario
    piezas = re.split(r"/\*\s*([\w-]+)\s*\*/", css)
    salida, archivos = [], []
    for i in range(1, len(piezas) - 1, 2):
        subconjunto, bloque = piezas[i], piezas[i + 1]
        if subconjunto not in SUBCONJUNTOS:
            continue
        m = re.search(r"url\((https://[^)]+\.woff2)\)", bloque)
        if not m:
            continue
        url = m.group(1)
        familia = re.search(r"font-family:\s*'([^']+)'", bloque).group(1)
        peso = re.search(r"font-weight:\s*(\d+)", bloque).group(1)
        cursiva = "italic" in bloque.split("font-style:")[1][:12]
        nombre = (familia.replace(" ", "") + "-" + peso +
                  ("i" if cursiva else "") + "-" + subconjunto + ".woff2")
        ruta = os.path.join(destino, nombre)
        if not os.path.isfile(ruta) or refrescar:
            try:
                with open(ruta, "wb") as f:
                    f.write(_bajar(url, {"User-Agent": UA}))
            except Exception as e:
                print(f"  tipografías: falló {nombre} ({e})")
                return None
        archivos.append(nombre)
        salida.append("@font-face {" + bloque.replace(url, nombre).strip() + "}")

    if not salida:
        return None
    cabecera = ("/* Tipografías del juego, alojadas junto a la app para que\n"
                "   funcione sin internet. Generado por tools/tipografias_pwa.py:\n"
                "   no editar a mano. Subconjuntos: " + ", ".join(SUBCONJUNTOS) +
                ". */\n")
    with open(css_local, "w", encoding="utf-8") as f:
        f.write(cabecera + "\n".join(salida) + "\n")
    print(f"  tipografías: {len(archivos)} archivos alojados en casa")
    return _listar(destino)


def _listar(destino):
    base = os.path.basename(destino)
    return [f"{base}/{n}" for n in sorted(os.listdir(destino))
            if n.endswith((".woff2", ".css"))]


if __name__ == "__main__":
    raiz = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(preparar(os.path.join(raiz, "docs", "juego", "tipos"),
                   refrescar="--refrescar" in sys.argv))
