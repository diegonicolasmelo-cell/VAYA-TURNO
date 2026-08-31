#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Mete una imagen suelta al juego con el nombre que le toca.

    python3 tools/ingresar_arte.py C13 ~/bajadas/becado.jpg
    python3 tools/ingresar_arte.py --lote lote.tsv

El arte llega de fuera —de Drive, del generador, de donde sea— con el
nombre que le puso quien lo dibujó («Enfermera de noche.jpg»), y la app lo
busca por el id de la carta (`C07.jpg`). Este guion hace las dos cosas que
median entre una y otra:

· GUARDA EL ORIGINAL en `cartas/arte-full/<ID>.jpg`, tal como vino. Es el
  respaldo: si mañana cambia el encuadre o el tope de tamaño, se rehace
  desde ahí y no hay que volver a pedir el archivo.

· DEJA EN `cartas/arte/<ID>.jpg` la versión que entra al juego: **4:3
  exacto, 1600×1200**. El recorte es centrado y del lado que sobra, así que
  una imagen que ya viene casi 4:3 pierde un filo de píxeles y nada más.
  Nunca deforma: antes estirar un 0,5 % que dejar la proporción torcida.

Cuando la fuente viene muy lejos del 4:3 —una vertical 9:16 de las viejas—
el recorte se lleva más de medio archivo, así que avisa. Con `--alto` se
corre la ventana del recorte hacia arriba o hacia abajo (0 = pegada
arriba, 0.5 = centrada, 1 = pegada abajo) para salvar la cabeza del
personaje, que es lo primero que se pierde.

El formato de `--lote` es un id, un tabulador y una ruta por línea; una
tercera columna opcional es el `--alto` de esa imagen.
"""
import os, sys
from PIL import Image

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ANCHO, ALTO = 1600, 1200
CALIDAD = 88
PROP = ANCHO / ALTO


def ingresar(ident, origen, alto=0.5):
    ident = ident.upper()
    im = Image.open(origen).convert("RGB")
    w, h = im.size
    prop = w / h

    full = os.path.join(RAIZ, "cartas", "arte-full", ident + ".jpg")
    os.makedirs(os.path.dirname(full), exist_ok=True)
    im.save(full, "JPEG", quality=94, subsampling=0)

    if prop > PROP:                       # sobra ancho: recorte lateral
        nw = round(h * PROP)
        x = (w - nw) // 2
        caja = (x, 0, x + nw, h)
    else:                                 # sobra alto: recorte de arriba/abajo
        nh = round(w / PROP)
        y = round((h - nh) * alto)
        caja = (0, y, w, y + nh)

    guardado = (caja[2] - caja[0]) * (caja[3] - caja[1]) / (w * h)
    fuera = im.crop(caja).resize((ANCHO, ALTO), Image.LANCZOS)
    destino = os.path.join(RAIZ, "cartas", "arte", ident + ".jpg")
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    fuera.save(destino, "JPEG", quality=CALIDAD, subsampling=0)

    aviso = "  ⚠ se recorta más de un tercio" if guardado < 0.67 else ""
    print(f"  {ident}  {w}×{h} ({prop:.3f}) → 1600×1200 · "
          f"conserva {guardado*100:.0f} %"
          f" · {os.path.getsize(destino)/1024:.0f} KB{aviso}")
    return guardado


def main():
    if len(sys.argv) >= 3 and sys.argv[1] == "--lote":
        n = 0
        for linea in open(sys.argv[2], encoding="utf-8"):
            linea = linea.rstrip("\n")
            if not linea.strip() or linea.startswith("#"):
                continue
            partes = linea.split("\t")
            ident, origen = partes[0].strip(), partes[1].strip()
            alto = float(partes[2]) if len(partes) > 2 and partes[2].strip() else 0.5
            ingresar(ident, origen, alto)
            n += 1
        print(f"✔ {n} imágenes")
    elif len(sys.argv) >= 3:
        alto = float(sys.argv[3]) if len(sys.argv) > 3 else 0.5
        ingresar(sys.argv[1], sys.argv[2], alto)
    else:
        raise SystemExit(__doc__)


if __name__ == "__main__":
    main()
