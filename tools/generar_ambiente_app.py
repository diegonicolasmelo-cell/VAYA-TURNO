#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""El ambiente de la UCI, vectorizado, para el campo de la maqueta B.

El tablero se lee en planta, desde arriba: es lo que ya hacía la camilla
dibujada en la cama vacía. Sobre esa misma idea van dos piezas:

  · el MESÓN de enfermería en los dos bordes exteriores — el de abajo es
    donde se apoya tu avatar, el de arriba es el del rival, espejado. Es
    un mostrador curvo: el retrato queda dentro de su curva, como quien
    está de pie en el control.
  · el SUELO de la unidad en las franjas de aire, anclado a las camas:
    contra la fila de camas va la barra de gases del cabecero y el riel
    de la cortina, y hacia el mesón queda el piso con lo que uno se
    encuentra en un pasillo de UCI — camilla parada, portasueros, carro
    de ropa, dispensador de alcohol.

Todo en línea finísima y muy tenue, con la misma advertencia que el piso:
detrás van CARTAS. Es ambiente, no ilustración. Si compite, sobra.

    python3 tools/generar_ambiente_app.py

Reescribe los data-URI dentro de tools/app-plantilla.html, así que
después hay que regenerar la app y la PWA.
"""
import base64
import io as _io
import os
import re
import urllib.parse

from PIL import Image

W_MES, H_MES = 390, 84       # la franja del mesón, en px CSS
W_SUE, H_SUE = 390, 168      # la franja de aire (flexible; se recorta)
W_CAM, H_CAM = 390, 132      # la franja de las tres camas
# los tres huecos de cama: .centro deja 24 px por lado y la rejilla 6 de
# separación, así que en un teléfono de 390 cada columna cae en estos centros
CENTROS = (79, 195, 311)
ANCHO_BOX = 110

TRAZO = "#5f8496"            # el gris-celeste de la sala, no el de la tinta


def g(cuerpo, op=".42", grosor="1.1", relleno="none"):
    return (f'<g fill="{relleno}" stroke="{TRAZO}" stroke-width="{grosor}" '
            f'stroke-linecap="round" stroke-linejoin="round" '
            f'opacity="{op}">{cuerpo}</g>')


# ── el mesón de enfermería ────────────────────────────────────────────
def meson():
    """En planta: un mostrador curvo pegado al borde de abajo. El avatar
    cae en el centro de su curva, así que ahí no va nada."""
    p = []
    # el mostrador: una banda de esquinas muy redondeadas que se sale por
    # los lados y por abajo — el borde de la pantalla es su filo
    p.append(f'<path d="M-40 {H_MES} L-40 46 Q-40 26 -10 26 '
             f'L{W_MES+10} 26 Q{W_MES+40} 26 {W_MES+40} 46 L{W_MES+40} {H_MES} Z"/>')
    # la repisa alta del mostrador (la que da al pasillo) y su filo
    p.append(f'<path d="M-40 38 L{W_MES+40} 38"/>')
    p.append(f'<path d="M-40 43 L{W_MES+40} 43" stroke-dasharray="2 5"/>')
    # el canto de las tablas del mostrador
    for x in (72, 168, 240, 318):
        p.append(f'<path d="M{x} 46 L{x} {H_MES}"/>')
    tapa = g("".join(p), op=".30")

    o = []
    # monitor y teclado del control, a la izquierda
    o.append('<rect x="26" y="50" width="34" height="21" rx="2.5"/>')
    o.append('<path d="M34 71 L52 71"/><path d="M43 71 L43 76"/>')
    o.append('<rect x="22" y="76" width="42" height="7" rx="2"/>')
    # taza y bolígrafos
    o.append('<circle cx="88" cy="60" r="6"/><path d="M94 60 q5 0 5 4"/>')
    o.append('<rect x="104" y="52" width="11" height="13" rx="2"/>')
    o.append('<path d="M107 52 L106 45"/><path d="M111 52 L112 44"/>')
    # carpetas apiladas, a la derecha
    o.append('<rect x="262" y="54" width="38" height="12" rx="1.5"/>')
    o.append('<rect x="266" y="60" width="38" height="12" rx="1.5"/>')
    o.append('<rect x="270" y="66" width="38" height="12" rx="1.5"/>')
    # teléfono del control
    o.append('<rect x="326" y="52" width="26" height="18" rx="3"/>')
    o.append('<path d="M330 56 L348 56"/><path d="M330 61 L344 61"/>')
    o.append('<path d="M356 50 q8 2 8 12 q0 10 -8 12"/>')
    # timbre de llamada de pacientes: tres luces
    for i, x in enumerate((150, 162, 174)):
        o.append(f'<circle cx="{x}" cy="34" r="2.6"/>')
    cosas = g("".join(o), op=".38")
    return tapa + cosas


# ── el suelo de la unidad ─────────────────────────────────────────────
def suelo():
    """En planta, con las camas ARRIBA: el cabecero y el riel de cortina
    pegados a ellas, y hacia abajo el piso del pasillo."""
    # el piso no se dibuja aquí: el fondo de .app ya trae la rejilla de
    # barril, y dos rejillas superpuestas eran ruido y no ambiente
    piso = ""

    c = []
    # la barra de gases del cabecero, pegada a la fila de camas
    c.append(f'<rect x="8" y="3" width="{W_SUE-16}" height="9" rx="2.5"/>')
    for x in range(26, W_SUE - 20, 34):
        c.append(f'<circle cx="{x}" cy="7.5" r="2.2"/>')
    # el riel de la cortina y sus pliegues
    c.append(f'<path d="M0 17 L{W_SUE} 17" stroke-dasharray="9 6"/>')
    cab = g("".join(c), op=".34")

    o = []
    # camilla parada contra la pared, a la izquierda
    o.append('<rect x="14" y="46" width="30" height="74" rx="7"/>')
    o.append('<path d="M14 62 L44 62"/><path d="M14 104 L44 104"/>')
    for cx, cy in ((17, 52), (41, 52), (17, 114), (41, 114)):
        o.append(f'<circle cx="{cx}" cy="{cy}" r="3.2"/>')
    # portasueros: la base de cinco patas, vista desde arriba
    o.append('<circle cx="352" cy="58" r="4"/>')
    for a in (0, 72, 144, 216, 288):
        import math
        dx, dy = 13 * math.cos(math.radians(a)), 13 * math.sin(math.radians(a))
        o.append(f'<path d="M352 58 l{dx:.1f} {dy:.1f}"/>')
    # carro de ropa
    o.append('<rect x="330" y="92" width="46" height="30" rx="4"/>')
    o.append('<path d="M330 102 L376 102"/><path d="M353 102 L353 122"/>')
    # dispensador de alcohol en la pared, junto al cabecero
    o.append('<rect x="292" y="24" width="14" height="10" rx="2"/>')
    o.append('<path d="M299 34 L299 39"/>')
    # contenedor de cortopunzantes
    o.append('<rect x="60" y="26" width="16" height="12" rx="2"/>')
    o.append('<path d="M64 26 L64 22 L72 22 L72 26"/>')
    cosas = g("".join(o), op=".30")
    return piso + cab + cosas


# ── las tres plazas ───────────────────────────────────────────────────
def camas():
    """En planta, con la cabecera hacia AFUERA (hacia el mesón): las dos
    unidades se miran de pies a través de la Pizarra. Casi siempre va
    tapada por las cartas; lo que se ve de verdad es la plaza vacía, que
    tiene que leerse como una cama hecha esperando paciente."""
    o = []
    for cx in CENTROS:
        # el colchón
        o.append(f'<rect x="{cx-38}" y="14" width="76" height="104" rx="9"/>')
        # las dos costuras de la sábana
        o.append(f'<path d="M{cx-38} 52 L{cx+38} 52"/>')
        o.append(f'<path d="M{cx-38} 70 L{cx+38} 70"/>')
        # la almohada, en la cabecera: abajo, hacia el mesón
        o.append(f'<rect x="{cx-28}" y="94" width="56" height="20" rx="7"/>')
        # las barandas
        o.append(f'<path d="M{cx-42} 44 L{cx-42} 88"/>')
        o.append(f'<path d="M{cx+42} 44 L{cx+42} 88"/>')
        # las cuatro ruedas
        for dx in (-31, 31):
            for cy in (22, 110):
                o.append(f'<circle cx="{cx+dx}" cy="{cy}" r="3.4"/>')
    return g("".join(o), op=".26")


def envolver(cuerpo, w, h, girado=False):
    giro = (f'<g transform="translate(0,{h}) scale(1,-1)">{cuerpo}</g>'
            if girado else cuerpo)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
            f'width="{w}" height="{h}" preserveAspectRatio="xMidYMax slice">'
            f'{giro}</svg>')


def uri(svg):
    return "data:image/svg+xml," + urllib.parse.quote(svg, safe="")


# ══ las ilustraciones, cuando existen ═════════════════════════════════
# El vector de arriba es la maqueta: dice dónde va cada cosa. Si en
# cartas/tablero/ hay una ilustración de esa banda, manda la ilustración y
# el vector queda de respaldo.
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TABLERO = os.path.join(RAIZ, "cartas", "tablero")

PAPEL = (223, 231, 234)   # --mesa: el papel del tablero
# Cuánto se mezcla hacia el papel del tablero. OJO: la sala fotográfica usa
# 0,45 porque venía de una foto con todo su contraste. Estas ilustraciones
# NO: se pidieron ya en el tono del tablero —su piso mide (216,231,234) y el
# papel es (223,231,234)— así que con 0,62 quedaban al 38 % de su contraste
# y el tablero entero se veía tapado por una capa blanca. Con 0,20 se apagan
# lo justo para que las cartas manden y el dibujo siga estando.
LAVADO = 0.20
ANCHO = 1000              # el tablero no pasa de 600 CSS px; sobra para retina

# Cada banda: archivo, recorte en el original y proporción de destino.
# Los recortes salen de medir la imagen, no de mirarla:
#  · el mesón se corta 48 px arriba (una pizca de piso sobre la curva del
#    mostrador) y 434 abajo — el teclado queda cortado por el filo, que es
#    justo lo que hace un mostrador que se sale de la pantalla;
#  · el suelo pierde el marco de pared (15 px arriba, 19 a los lados) para
#    que la barra del cabecero quede a ras de la fila de camas;
#  · las camas se RECOMPONEN: el generador venía con las tres en 16/50/83 %
#    y las columnas de la app caen en 20,3/50/79,7 %, así que se recorta una
#    plaza y se pega tres veces en su sitio.
BANDAS = {
    "meson": dict(archivo="meson.png", caja=(0, 48, 1792, 434), destino=390/84),
    "suelo": dict(archivo="suelo.png", caja=(62, 44, 1522, 664), destino=390/168),
    "camas": dict(archivo="camas.png", caja=None, destino=390/132),
}
CENTROS_PC = (0.203, 0.5, 0.797)   # los centros de las tres columnas


def lavar(im):
    """Mezcla hacia el papel del tablero. Detrás van CARTAS: si el ambiente
    compite con ellas deja de ser tablero y pasa a ser ruido."""
    fondo = Image.new("RGB", im.size, PAPEL)
    return Image.blend(im.convert("RGB"), fondo, LAVADO)


def alinear(im):
    """RETIRADO del camino normal, y conviene saber por qué antes de volver
    a usarlo. Nació para cuadrar el piso de las tres bandas entre sí, cuando
    el lavado era de 0,62 y las diferencias de tono se notaban. Con el
    lavado en 0,20 sobra: los tres pisos ya venían casi idénticos —(215,230,
    237), (217,232,235) y (216,231,234)— y el desplazamiento de +7 en el
    rojo que hacía falta para clavar el papel teñía TODO el dibujo de rosa.
    Un desplazamiento plano por canal es demasiado brusco para una imagen de
    tan poco contraste."""
    import numpy as np
    a = np.asarray(im).astype(int)
    piso = a[4, 4]
    a = np.clip(a + (np.array(PAPEL) - piso), 0, 255).astype("uint8")
    return Image.fromarray(a)


def recomponer_camas(im):
    """Recorta la plaza del centro y la pega en los tres centros de columna,
    sobre un lienzo del color de fondo de la propia imagen."""
    W, H = im.size
    alto = H
    ancho = round(alto * BANDAS["camas"]["destino"])
    fondo = im.getpixel((4, 4))
    lienzo = Image.new("RGB", (ancho, alto), fondo)
    # la plaza del centro, con aire de sobra para no cortarle la sombra
    media = im.crop((W//2 - 160, 0, W//2 + 160, H))
    for pc in CENTROS_PC:
        lienzo.paste(media, (round(ancho*pc) - media.width//2, 0))
    return lienzo


def encajar(im, destino):
    """Recorta al centro hasta dar exactamente con la proporción de la banda,
    para poder pintarla con 100% 100% sin deformar nada."""
    W, H = im.size
    if W/H > destino:
        w = round(H*destino); x = (W-w)//2
        im = im.crop((x, 0, x+w, H))
    else:
        h = round(W/destino); y = (H-h)//2
        im = im.crop((0, y, W, y+h))
    return im


def a_uri(im):
    if im.width > ANCHO:
        im = im.resize((ANCHO, round(im.height*ANCHO/im.width)), Image.LANCZOS)
    buf = _io.BytesIO()
    im.save(buf, "WEBP", quality=82, method=6)
    return "data:image/webp;base64," + base64.b64encode(buf.getvalue()).decode()


def ilustracion(nombre):
    cfg = BANDAS[nombre]
    ruta = os.path.join(TABLERO, cfg["archivo"])
    if not os.path.isfile(ruta):
        return None
    im = Image.open(ruta).convert("RGB")
    im = recomponer_camas(im) if nombre == "camas" else im.crop(cfg["caja"])
    im = lavar(encajar(im, cfg["destino"]))
    return im


piezas = {
    "meson-mio":    envolver(meson(), W_MES, H_MES),
    "meson-suyo":   envolver(meson(), W_MES, H_MES, girado=True),
    "suelo-mio":    envolver(suelo(), W_SUE, H_SUE),
    "suelo-suyo":   envolver(suelo(), W_SUE, H_SUE, girado=True),
    "camas-mio":    envolver(camas(), W_CAM, H_CAM),
    "camas-suyo":   envolver(camas(), W_CAM, H_CAM, girado=True),
}

# la ilustración pisa al vector, banda por banda
fuente = {}
for nombre in BANDAS:
    im = ilustracion(nombre)
    if im is None:
        fuente[nombre] = "vector"
        continue
    fuente[nombre] = f"dibujo {im.width}x{im.height}"
    piezas[f"{nombre}-mio"] = a_uri(im)
    piezas[f"{nombre}-suyo"] = a_uri(im.rotate(180))

def envolver_uri(v):
    return v if v.startswith("data:") else uri(v)

bloque = "\n".join(f'  --{k}:url("{envolver_uri(v)}");' for k, v in piezas.items())
nuevo_css = ":root{\n" + bloque + "\n}"

plantilla = os.path.join(RAIZ, "tools", "app-plantilla.html")
html = open(plantilla, encoding="utf-8").read()
MARCA_A = "/*__AMBIENTE_INICIO__*/"
MARCA_B = "/*__AMBIENTE_FIN__*/"
if MARCA_A not in html:
    raise SystemExit("Faltan las marcas del ambiente en app-plantilla.html")
patron = re.escape(MARCA_A) + r".*?" + re.escape(MARCA_B)
html2 = re.sub(patron, MARCA_A + "\n" + nuevo_css + "\n" + MARCA_B, html,
               count=1, flags=re.S)
if html2 != html:
    open(plantilla, "w", encoding="utf-8").write(html2)
os.makedirs(os.path.join(RAIZ, "docs"), exist_ok=True)
for k, v in piezas.items():
    if not v.startswith("data:"):
        open(os.path.join(RAIZ, "docs", f"amb-{k}.svg"), "w").write(v)
print("✔ ambiente de la UCI · " +
      " · ".join(f"{k}: {f}" for k, f in fuente.items()))
print("  peso · " + " · ".join(
    f"{k} {len(envolver_uri(v))//1024} KB" for k, v in piezas.items()))
print("  plantilla parcheada — ahora: generar_app.py y generar_app.py --pwa")
