#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Deja el logotipo recortado sobre transparencia, listo para ponerlo
encima del video de la portada.

    python3 tools/recortar_logo.py logo-crudo.png

Escribe arte/portada/logo.webp (y logo.png de respaldo).

El fondo NO se quita con un «todo lo blanco a transparente»: el logo tiene
brillos blancos DENTRO de las letras y un contorno claro, y ese método se
los perfora. Se rellena desde los bordes, así que solo desaparece el blanco
que rodea al dibujo por fuera.

El borde tampoco se corta a cuchillo: los píxeles del contorno vienen
mezclados con el blanco del fondo, y un recorte duro deja una orla clara
que se nota apenas lo pones sobre una imagen. En la franja de contacto el
alfa sale de cuánto blanco tenía el píxel.
"""
import os, sys
import numpy as np
from PIL import Image
from scipy.ndimage import label, binary_dilation

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DESTINO = os.path.join(RAIZ, "arte", "portada")
ANCHO = 1000          # el logo ocupa ~330 px de pantalla; a 3x sobra
UMBRAL = 236          # a partir de aquí un píxel cuenta como fondo
HUECO = 300           # mancha blanca encerrada que ya no es un brillo


def recortar(ruta):
    im = Image.open(ruta).convert("RGB")
    a = np.asarray(im).astype(np.int16)
    minimo = a.min(axis=2)                      # lo blanco tiene los 3 canales altos

    # 1. qué es fondo: blanco Y pegado al borde de la imagen… más los
    #    huecos encerrados. En este logo hay bolsones de fondo atrapados
    #    entre el tubo del monitor y las letras que no tocan ningún borde:
    #    si no se sacan, quedan como manchas blancas flotando sobre el
    #    video. Un brillo pintado a propósito es un trazo fino; un hueco de
    #    fondo es una mancha ancha, así que el área los separa bien.
    blanco = minimo >= UMBRAL
    trozos, n = label(blanco)
    bordes = set(trozos[0].tolist()) | set(trozos[-1].tolist()) \
           | set(trozos[:, 0].tolist()) | set(trozos[:, -1].tolist())
    bordes.discard(0)
    tam = np.bincount(trozos.ravel())
    huecos = {i for i in range(1, n + 1) if i not in bordes and tam[i] >= HUECO}
    fondo = np.isin(trozos, list(bordes | huecos))
    print(f"  {n} manchas blancas · {len(bordes)} tocan el borde · "
          f"{len(huecos)} huecos encerrados · "
          f"{100*fondo.mean():.1f}% de la imagen es fondo")

    # 2. alfa. En la franja donde el dibujo se mezcla con el fondo, el alfa
    #    sale de cuánto blanco traía el píxel; el resto queda opaco.
    alfa = np.where(fondo, 0.0, 1.0)
    franja = binary_dilation(fondo, iterations=2) & ~fondo
    suave = np.clip((UMBRAL - minimo) / 40.0, 0, 1)
    alfa[franja] = suave[franja]

    out = np.dstack([np.asarray(im), (alfa * 255).astype(np.uint8)])
    im2 = Image.fromarray(out, "RGBA")

    # 3. a la caja justa, y al tamaño de trabajo
    caja = im2.getchannel("A").point(lambda v: 255 if v > 6 else 0).getbbox()
    im2 = im2.crop(caja)
    print(f"  recortado a {im2.width}x{im2.height}")
    if im2.width > ANCHO:
        im2 = im2.resize((ANCHO, round(im2.height * ANCHO / im2.width)),
                         Image.LANCZOS)
    return im2


def main():
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    os.makedirs(DESTINO, exist_ok=True)
    im = recortar(sys.argv[1])
    for nombre, opts in (("logo.webp", dict(format="WEBP", quality=88, method=6)),
                         ("logo.png", dict(format="PNG", optimize=True))):
        f = os.path.join(DESTINO, nombre)
        im.save(f, **opts)
        print(f"✔ {os.path.relpath(f, RAIZ)} ({os.path.getsize(f)/1024:.0f} KB) "
              f"· {im.width}x{im.height}")


if __name__ == "__main__":
    main()
