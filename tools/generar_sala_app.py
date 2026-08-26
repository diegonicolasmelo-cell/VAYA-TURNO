#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""La sala ilustrada, llevada al tablero del juego digital.

El playmat físico usa la sala entera (4:3). En el teléfono el tablero es
vertical y cada unidad es una FRANJA ancha de tres camas, así que de la
ilustración se recorta solo esa banda: muro de cabecera, monitores, las
tres camas y un poco de piso.

Se generan dos versiones: la tuya y la del rival girada 180°, como si
estuviera sentado al otro lado de la mesa.

Y se aclaran a propósito. Detrás van CARTAS: si la sala compite con
ellas deja de ser tablero y pasa a ser ruido. La mezcla con blanco la
convierte en un fantasma de sí misma, que es justo lo que tiene que ser.

    python3 tools/generar_sala_app.py

Reescribe los data-URI dentro de tools/app-plantilla.html, así que
después hay que regenerar la app y la PWA.
"""
import base64
import io
import os
import re

from PIL import Image

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FUENTE = os.path.join(RAIZ, "cartas", "tablero", "sala-uci.jpg")

BANDA = (0.115, 0.665)   # de la ilustración: del muro a un poco bajo las camas
ANCHO = 1100             # px: el tablero nunca pasa de 600 CSS px, sobra para retina
BLANCO = 0.45            # cuánto se lava hacia el blanco (0 = original, 1 = papel)


def franja(girada=False):
    im = Image.open(FUENTE).convert("RGB")
    W, H = im.size
    im = im.crop((0, int(H * BANDA[0]), W, int(H * BANDA[1])))
    im = im.resize((ANCHO, round(ANCHO * im.height / im.width)), Image.LANCZOS)
    if girada:
        im = im.rotate(180)
    velo = Image.new("RGB", im.size, (255, 255, 255))
    im = Image.blend(im, velo, BLANCO)
    buf = io.BytesIO()
    im.save(buf, "WEBP", quality=80, method=6)
    return ("data:image/webp;base64," +
            base64.b64encode(buf.getvalue()).decode()), im.size, buf.tell()


def main():
    if not os.path.isfile(FUENTE):
        raise SystemExit(f"Falta la ilustración: {FUENTE}")
    mia, tam, peso1 = franja(False)
    suya, _, peso2 = franja(True)

    plantilla = os.path.join(RAIZ, "tools", "app-plantilla.html")
    html = open(plantilla, encoding="utf-8").read()
    cambios = 0
    for marca, uri in (("--sala-mia", mia), ("--sala-suya", suya)):
        patron = re.compile(re.escape(marca) + r':url\("[^"]*"\)')
        if not patron.search(html):
            raise SystemExit(f"No encontré {marca} en app-plantilla.html")
        html, n = patron.subn(lambda m: marca + ':url("' + uri + '")', html, 1)
        cambios += n
    open(plantilla, "w", encoding="utf-8").write(html)
    print(f"✔ sala del tablero · franja {tam[0]}×{tam[1]} px · "
          f"{(peso1 + peso2) // 1024} KB las dos")
    print(f"  {cambios} fondos actualizados — ahora: generar_app.py y --pwa")


if __name__ == "__main__":
    main()
