#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Mete la grabación de ambiente de la UCI con el nombre que le toca.

    python3 tools/ingresar_sonido.py ~/bajadas/icu-ambience.mp3

Copia el archivo a sonido/ambiente.<ext> (borrando cualquier ambiente
anterior de otra extensión), avisa si pesa de más, y recuerda el paso
siguiente. Qué grabación sirve y de dónde sacarla: sonido/LEEME.md.
"""
import os, shutil, sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXTS = (".mp3", ".ogg", ".m4a", ".wav")
TOPE_KB = 1200


def main():
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    origen = sys.argv[1]
    ext = os.path.splitext(origen)[1].lower()
    if ext not in EXTS:
        raise SystemExit(f"Extensión {ext} no reconocida; sirven {EXTS}")
    carpeta = os.path.join(RAIZ, "sonido")
    os.makedirs(carpeta, exist_ok=True)
    for e in EXTS:                      # un solo ambiente a la vez
        viejo = os.path.join(carpeta, "ambiente" + e)
        if os.path.isfile(viejo):
            os.remove(viejo)
    destino = os.path.join(carpeta, "ambiente" + ext)
    shutil.copyfile(origen, destino)
    kb = os.path.getsize(destino) // 1024
    aviso = ("  ⚠ pesa más de lo aconsejado: bájalo a MP3 mono 96-128 kbps"
             if kb > TOPE_KB else "")
    print(f"✔ sonido/ambiente{ext} · {kb} KB{aviso}")
    print("  Anota la fuente y la licencia en sonido/LEEME.md,")
    print("  y reconstruye: python3 tools/generar_app.py && python3 tools/generar_app.py --pwa")


if __name__ == "__main__":
    main()
