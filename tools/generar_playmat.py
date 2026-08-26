#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""El playmat de ¡Vaya Turno!: tu UCI vista desde un dron.

Una unidad de 3 camas mirada desde arriba con ojo de pez leve. La regla
de oro: el PISO y los MUROS se curvan, los SLOTS DE CARTA no — una carta
de 63×88 mm tiene que apoyarse plana sobre un rectángulo recto.

Unidades: 1 unidad SVG = 1 mm. El mat mide 400×352 mm.
"""
import math
import os

W, H = 400.0, 352.0          # mm
K = 0.22                     # fuerza del barril: se nota, sin ser pescado
CX, CY = W / 2, H * 0.46     # el dron no está justo al centro: mira hacia la cabecera

# ── paleta: celestes y blancos limpios ──────────────────────────────
PISO      = "#eef7fa"
PISO_2    = "#e2f0f6"
REJILLA   = "#cfe6ee"
MURO      = "#d8ebf2"
MURO_LIN  = "#a9cede"
CELESTE   = "#4aa3c7"
HONDO     = "#1f6b8c"
TINTA     = "#16323d"
BLANCO    = "#ffffff"
VIDA      = "#c0492f"        # el único color cálido: los corazones
CAMA      = "#c3dfe9"

def barril(x, y):
    """Distorsión de barril: los puntos se abomban hacia afuera del centro.
    Es lo que hace que el piso se vea como filmado con lente ancho."""
    nx = (x - CX) / (W / 2)
    ny = (y - CY) / (H / 2)
    r2 = nx * nx + ny * ny
    f = 1 + K * r2
    return CX + nx * f * (W / 2), CY + ny * f * (H / 2)

def curva(pts):
    """Polilínea suavizada por los puntos ya distorsionados."""
    d = "M %.2f %.2f" % pts[0]
    for p in pts[1:]:
        d += " L %.2f %.2f" % p
    return d

def linea_h(y, x0=-60, x1=460, n=42):
    return curva([barril(x0 + (x1 - x0) * i / n, y) for i in range(n + 1)])

def linea_v(x, y0=-40, y1=360, n=32):
    return curva([barril(x, y0 + (y1 - y0) * i / n) for i in range(n + 1)])

# ── geometría de las zonas (rectas, sin distorsión) ─────────────────
CW, CH = 63.0, 88.0                     # la carta
BAHIAS = [(18.0, 110.0), (145.0, 110.0), (272.0, 110.0)]   # x, ancho
BAHIA_Y, BAHIA_H = 58.0, 174.0
SLOT_Y = 68.0
FAN_Y, FAN_H = 182.0, 48.0              # los recursos, en abanico bajo la cama
EST_Y = 244.0                            # tu puesto

s = []
a = s.append

a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.0f} {H:.0f}" '
  f'width="{W:.0f}mm" height="{H:.0f}mm" role="img" '
  f'aria-label="Playmat de una unidad de cuidados intensivos de tres camas, '
  f'vista desde arriba">')

# ── defs ────────────────────────────────────────────────────────────
a('<defs>')
a(f'<radialGradient id="suelo" cx="50%" cy="42%" r="78%">'
  f'<stop offset="0%" stop-color="{BLANCO}"/>'
  f'<stop offset="55%" stop-color="{PISO}"/>'
  f'<stop offset="100%" stop-color="{PISO_2}"/></radialGradient>')
# la viñeta del ojo de pez: los bordes caen un pelo
a('<radialGradient id="vineta" cx="50%" cy="44%" r="72%">'
  '<stop offset="0%" stop-color="#0b3murk" stop-opacity="0"/>'
  '<stop offset="62%" stop-color="#12475c" stop-opacity="0"/>'
  '<stop offset="100%" stop-color="#12475c" stop-opacity="0.16"/></radialGradient>')
a(f'<linearGradient id="muro" x1="0" y1="0" x2="0" y2="1">'
  f'<stop offset="0%" stop-color="#c6e1ec"/>'
  f'<stop offset="100%" stop-color="{MURO}"/></linearGradient>')
a('<clipPath id="mat"><rect x="0" y="0" width="%.0f" height="%.0f" rx="7"/></clipPath>' % (W, H))
a('</defs>')

a('<g clip-path="url(#mat)">')

# ── piso ────────────────────────────────────────────────────────────
a(f'<rect x="0" y="0" width="{W:.0f}" height="{H:.0f}" fill="url(#suelo)"/>')

# rejilla de baldosas, curvada por el barril
a(f'<g fill="none" stroke="{REJILLA}" stroke-width="0.65" opacity="1">')
for i in range(-2, 21):
    a(f'<path d="{linea_v(i * 26.0)}"/>')
for j in range(-1, 15):
    a(f'<path d="{linea_h(j * 26.0)}"/>')
a('</g>')

# ── el muro de cabecera, arriba, también curvado ────────────────────
borde = [barril(x, 58.0) for x in [-60 + 520 * i / 40 for i in range(41)]]
d_muro = "M -60 -40 L 460 -40 L 460 %.2f" % borde[-1][1]
for p in reversed(borde):
    d_muro += " L %.2f %.2f" % p
d_muro += " Z"
a(f'<path d="{d_muro}" fill="url(#muro)"/>')
a(f'<path d="{curva(borde)}" fill="none" stroke="{MURO_LIN}" stroke-width="1.1"/>')

a('</g>')   # fin del clip del piso

def texto(x, y, txt, size=4.4, color=HONDO, peso=600, anchor="start",
          fam="Archivo Narrow", track=0.18, op=1.0):
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-family="{fam}, sans-serif" '
            f'font-size="{size}" font-weight="{peso}" fill="{color}" '
            f'letter-spacing="{track}" text-anchor="{anchor}" '
            f'opacity="{op}">{txt}</text>')

# ── las tres bahías ─────────────────────────────────────────────────
for i, (bx, bw) in enumerate(BAHIAS):
    n = i + 1
    cx_b = bx + bw / 2
    a('<g>')
    # cortina divisoria (salvo la primera)
    if i:
        a(f'<path d="M {bx - 8:.1f} 60 L {bx - 8:.1f} {BAHIA_Y + BAHIA_H:.0f}" '
          f'stroke="{MURO_LIN}" stroke-width="0.7" stroke-dasharray="2 2.6" '
          f'opacity="0.75" fill="none"/>')
    # cabecera de la cama: monitor y tomas de gases, sobre el muro
    mx = cx_b - 17
    a(f'<rect x="{mx:.1f}" y="17" width="34" height="21" rx="2.6" '
      f'fill="{BLANCO}" stroke="{MURO_LIN}" stroke-width="0.8"/>')
    a(f'<path d="M {mx+4:.1f} 29 h 6 l 2.5 -6 l 3 11 l 2.5 -5 h 4 l 2 3 h 6" '
      f'fill="none" stroke="{CELESTE}" stroke-width="1" '
      f'stroke-linejoin="round" stroke-linecap="round"/>')
    for k, col in enumerate((CELESTE, "#8fbfd4", "#b9d6e2")):
        a(f'<circle cx="{cx_b - 9 + k * 9:.1f}" cy="46" r="2.6" fill="{col}" '
          f'opacity="0.85"/>')
    # la cama vista desde arriba, detrás del slot
    a(f'<rect x="{cx_b - 36:.1f}" y="{SLOT_Y - 5:.1f}" width="72" '
      f'height="{CH + 14:.0f}" rx="8" fill="{CAMA}" opacity="0.5"/>')
    a(f'<rect x="{cx_b - 36:.1f}" y="{SLOT_Y - 5:.1f}" width="72" '
      f'height="{CH + 14:.0f}" rx="8" fill="none" stroke="{MURO_LIN}" '
      f'stroke-width="0.8" opacity="0.9"/>')
    # la almohada: es lo que hace legible que ESTO es una cama
    a(f'<rect x="{cx_b - 22:.1f}" y="{SLOT_Y - 2.5:.1f}" width="44" height="11" '
      f'rx="5.5" fill="{BLANCO}" opacity="0.85" stroke="{MURO_LIN}" '
      f'stroke-width="0.6"/>')
    # ruedas
    for wx in (cx_b - 30, cx_b + 30):
        for wy in (SLOT_Y + 2, SLOT_Y + CH + 4):
            a(f'<circle cx="{wx:.1f}" cy="{wy:.1f}" r="2.2" fill="{MURO_LIN}" '
              f'opacity="0.55"/>')
    # SLOT DE PACIENTE — recto, 63×88, es donde se apoya la carta
    sx = cx_b - CW / 2
    a(f'<rect x="{sx:.1f}" y="{SLOT_Y:.0f}" width="{CW:.0f}" height="{CH:.0f}" '
      f'rx="3.5" fill="{BLANCO}" fill-opacity="0.72" stroke="{CELESTE}" '
      f'stroke-width="1.1" stroke-dasharray="5 3.4"/>')
    a(texto(cx_b, SLOT_Y + CH / 2 + 1.6, "PACIENTE", 5, CELESTE, 700,
            "middle", track=1.5, op=0.5))
    # número de cama, grande, en el piso
    a(f'<text x="{bx + 5:.1f}" y="{SLOT_Y + 14:.1f}" '
      f'font-family="Petrona, Georgia, serif" font-size="17" font-weight="700" '
      f'fill="{CELESTE}" opacity="0.5">{n}</text>')
    # ── la vida del paciente, justo bajo la cama: 7 casillas ──
    a(texto(cx_b - 38, FAN_Y - 4.5, "VIDA", 3.4, VIDA, 700, "start",
            track=0.9, op=0.9))
    for k in range(7):
        hx = cx_b - 16 + k * 9.6
        a(f'<path d="M {hx:.1f} {FAN_Y - 8.8:.1f} '
          f'c -1.8 -2.1 -4.3 -0.5 -4.3 1.5 c 0 2.1 2.6 3.6 4.3 4.9 '
          f'c 1.7 -1.3 4.3 -2.8 4.3 -4.9 c 0 -2.0 -2.5 -3.6 -4.3 -1.5 Z" '
          f'fill="{BLANCO}" fill-opacity="0.55" stroke="{VIDA}" '
          f'stroke-width="0.75" opacity="0.62"/>')

    # ── lo que lleva puesto: una fila de casillas por tipo ──
    a(f'<rect x="{cx_b - 42:.1f}" y="{FAN_Y:.0f}" width="84" '
      f'height="{FAN_H:.0f}" rx="4" fill="{BLANCO}" fill-opacity="0.42" '
      f'stroke="{CELESTE}" stroke-width="0.8" stroke-dasharray="3 3" '
      f'opacity="0.75"/>')
    a(texto(cx_b, FAN_Y + 7.6, "RECURSOS COLOCADOS", 3.4, HONDO, 700,
            "middle", track=0.9, op=0.78))
    for k, nom in enumerate(("IMAGEN", "FÁRMACOS", "PERSONAL", "PROCED.")):
        ty = FAN_Y + 16.5 + k * 8.0
        a(texto(cx_b - 37, ty + 1.2, nom, 3.2, HONDO, 600, "start",
                track=0.4, op=0.72))
        for j in range(4):
            a(f'<circle cx="{cx_b - 3 + j * 9.5:.1f}" cy="{ty:.1f}" r="2.5" '
              f'fill="{BLANCO}" fill-opacity="0.7" stroke="{CELESTE}" '
              f'stroke-width="0.65" opacity="0.85"/>')
    a('</g>')

# ── franja del puesto ───────────────────────────────────────────────
a(f'<path d="M 12 {EST_Y - 8:.0f} L {W - 12:.0f} {EST_Y - 8:.0f}" '
  f'stroke="{MURO_LIN}" stroke-width="0.8" opacity="0.8"/>')

# avatar
a(f'<rect x="18" y="{EST_Y:.0f}" width="{CW:.0f}" height="{CH:.0f}" rx="3.5" '
  f'fill="{BLANCO}" fill-opacity="0.72" stroke="{HONDO}" stroke-width="1.1" '
  f'stroke-dasharray="5 3.4"/>')
a(texto(18 + CW / 2, EST_Y + CH / 2 + 1.6, "TU AVATAR", 5, HONDO, 700,
        "middle", track=1.4, op=0.55))

# las tres indicaciones: el corazón del turno
IX, IY = 100.0, EST_Y + 6
a(texto(IX, IY + 4, "INDICACIONES DEL TURNO", 4, HONDO, 700, "start", track=1.1))
for k in range(3):
    a(f'<circle cx="{IX + 11 + k * 26:.1f}" cy="{IY + 22:.1f}" r="10.5" '
      f'fill="{BLANCO}" fill-opacity="0.8" stroke="{CELESTE}" '
      f'stroke-width="1.4"/>')
    a(f'<circle cx="{IX + 11 + k * 26:.1f}" cy="{IY + 22:.1f}" r="6.2" '
      f'fill="{CELESTE}" opacity="0.16"/>')
a(texto(IX, IY + 42, "Tratar · Sabotear · Des-escalar · una ficha por gasto",
        3.4, HONDO, 500, "start", track=0.3, op=0.66))
a(texto(IX, IY + 50.5, "Cierras Sumario sin gastar indicación",
        3.4, HONDO, 500, "start", track=0.3, op=0.5))

# sumarios
SX = 200.0
a(f'<rect x="{SX:.0f}" y="{EST_Y:.0f}" width="72" height="{CH:.0f}" rx="4" '
  f'fill="none" stroke="{HONDO}" stroke-width="0.9" stroke-dasharray="3 3" '
  f'opacity="0.72"/>')
a(texto(SX + 36, EST_Y + 10, "SUMARIOS", 4.2, HONDO, 700, "middle", track=1.2))
a(texto(SX + 36, EST_Y + 17.5, "boca arriba", 3.3, HONDO, 500, "middle",
        track=0.3, op=0.62))
a(texto(SX + 36, EST_Y + 50, "cada uno te quita", 3.3, HONDO, 500, "middle",
        track=0.2, op=0.62))
a(texto(SX + 36, EST_Y + 57, "1 carta de mano", 3.3, HONDO, 600, "middle",
        track=0.2, op=0.72))
a(texto(SX + 36, EST_Y + 72, "cerrar: 2 cartas", 3.3, CELESTE, 600, "middle",
        track=0.2, op=0.9))

# protocolos comprados
PX = 286.0
a(f'<rect x="{PX:.0f}" y="{EST_Y:.0f}" width="96" height="{CH:.0f}" rx="4" '
  f'fill="none" stroke="{CELESTE}" stroke-width="0.9" stroke-dasharray="3 3" '
  f'opacity="0.8"/>')
a(texto(PX + 48, EST_Y + 10, "TUS PROTOCOLOS", 4.2, HONDO, 700, "middle",
        track=1.2))
a(texto(PX + 48, EST_Y + 17.5, "comprados en la Pizarra", 3.3, HONDO, 500,
        "middle", track=0.3, op=0.62))
for k in range(3):
    a(f'<rect x="{PX + 8 + k * 28:.1f}" y="{EST_Y + 24:.0f}" width="24" '
      f'height="34" rx="2.4" fill="{BLANCO}" fill-opacity="0.6" '
      f'stroke="{CELESTE}" stroke-width="0.7" opacity="0.8"/>')
a(texto(PX + 48, EST_Y + 70, "máx. 1 compra y 1 jugada por turno", 3.3,
        HONDO, 500, "middle", track=0.2, op=0.62))

# ── rótulo al borde inferior: arriba chocaba con el monitor de la cama 1
a(f'<text x="{W/2:.0f}" y="{H - 5:.0f}" text-anchor="middle" '
  f'font-family="IBM Plex Mono, monospace" font-size="4.2" font-weight="500" '
  f'fill="{HONDO}" letter-spacing="2.4" opacity="0.5">'
  f'&#161;VAYA TURNO! &#183; TU UNIDAD &#183; 3 CAMAS</text>')

# ── viñeta del ojo de pez, encima de todo ───────────────────────────
a(f'<rect x="0" y="0" width="{W:.0f}" height="{H:.0f}" rx="7" '
  f'fill="url(#vineta)" pointer-events="none"/>')
a(f'<rect x="0.6" y="0.6" width="{W - 1.2:.1f}" height="{H - 1.2:.1f}" rx="7" '
  f'fill="none" stroke="{MURO_LIN}" stroke-width="1.2"/>')
a('</svg>')

svg = "\n".join(s).replace('#0b3murk', '#12475c')
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SALIDA = os.path.join(RAIZ, "docs", "playmat.svg")
os.makedirs(os.path.dirname(SALIDA), exist_ok=True)
open(SALIDA, "w", encoding="utf-8").write(svg)
print(f"✔ {SALIDA} — {W:.0f}×{H:.0f} mm · {len(svg)//1024} KB")
print("  slots de carta: 63×88 mm · pide 3 mm de sangrado a la imprenta")
