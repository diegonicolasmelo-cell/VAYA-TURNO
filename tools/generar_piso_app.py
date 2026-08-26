#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""El piso del playmat, llevado al fondo de la app.

    python3 tools/generar_piso_app.py

Reescribe el data-URI dentro de tools/app-plantilla.html, así
que después hay que regenerar la app y la PWA.

Mismo barril que el mat físico, pero: (a) solo la rejilla, sin zonas;
(b) en el celeste-gris de la app, no en el celeste del papel, para que no
compita con las cartas; (c) cada línea como UNA curva cuadrática en vez de
una polilínea de 40 puntos — la distorsión de barril es casi una parábola,
así que una Bézier la calca y el archivo cabe en un data-URI.
"""
import os
import re
import urllib.parse

W, H = 400.0, 860.0      # el viewport del teléfono, en vertical
K = 0.22
CX, CY = W / 2, H * 0.45
PASO = 34.0

def barril(x, y):
    nx, ny = (x - CX) / (W / 2), (y - CY) / (H / 2)
    f = 1 + K * (nx * nx + ny * ny)
    return CX + nx * f * (W / 2), CY + ny * f * (H / 2)

def bezier(p0, pm, p1):
    """Control point que hace pasar la cuadrática por el punto medio real."""
    cx = 2 * pm[0] - (p0[0] + p1[0]) / 2
    cy = 2 * pm[1] - (p0[1] + p1[1]) / 2
    return f"M{p0[0]:.1f} {p0[1]:.1f}Q{cx:.1f} {cy:.1f} {p1[0]:.1f} {p1[1]:.1f}"

d = []
x = -PASO
while x <= W + PASO:
    d.append(bezier(barril(x, -60), barril(x, H / 2), barril(x, H + 60)))
    x += PASO
y = -PASO
while y <= H + PASO:
    d.append(bezier(barril(-60, y), barril(W / 2, y), barril(W + 60, y)))
    y += PASO

# width/height explícitos: sin ellos el navegador le inventa un tamaño
# natural de 70x150 y la rejilla queda deformada al escalarla.
svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.0f} {H:.0f}" '
       f'width="{W:.0f}" height="{H:.0f}" '
       f'preserveAspectRatio="xMidYMid slice">'
       f'<g fill="none" stroke="#6e97a8" stroke-width="1.1" opacity="0.40">'
       + "".join(f'<path d="{p}"/>' for p in d) +
       '</g></svg>')

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
open(os.path.join(RAIZ, "docs", "piso-app.svg"), "w").write(svg)
uri = "data:image/svg+xml," + urllib.parse.quote(svg, safe="")

plantilla = os.path.join(RAIZ, "tools", "app-plantilla.html")
html = open(plantilla, encoding="utf-8").read()
patron = r'background:url\("data:image/svg\+xml,[^"]*"\) center/cover'
if not re.search(patron, html):
    raise SystemExit("No encontré el piso en app-plantilla.html — ¿cambió el CSS de .app?")
# ojo: comparar nuevo==html NO sirve como comprobación — si el piso ya está
# al día la sustitución devuelve el mismo texto, que es un caso legítimo
nuevo = re.sub(patron, lambda m: 'background:url("' + uri + '") center/cover',
               html, count=1)
if nuevo != html:
    open(plantilla, "w", encoding="utf-8").write(nuevo)
print(f"✔ piso de la app · {len(d)} líneas · data-URI {len(uri)} bytes")
print("  plantilla parcheada — ahora: generar_app.py y generar_app.py --pwa")
