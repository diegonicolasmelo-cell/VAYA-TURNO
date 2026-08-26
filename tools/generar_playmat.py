#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""El playmat de ¡VAYA TURNO!: tu UCI vista desde un dron.

Una unidad de 3 camas mirada desde arriba. La sala la dibuja la
ilustración (`cartas/tablero/sala-uci.jpg`); este archivo pone encima lo
que la ilustración no puede poner con precisión: los slots de carta a
63×88 mm exactos, el marcador de vida, los contadores y los rótulos.

Dos capas, y cada una hace lo suyo — la IA no acierta un rectángulo al
milímetro, y el vector no dibuja una sala con gracia.

Si la ilustración no está, dibuja un piso sintético de baldosas con la
misma distorsión de barril, para no quedarse sin mat.

    python3 tools/generar_playmat.py   → docs/playmat.svg

Unidades: 1 unidad SVG = 1 mm.
"""
import base64
import math
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONDO = os.path.join(RAIZ, "cartas", "tablero", "sala-uci.jpg")
SALIDA = os.path.join(RAIZ, "docs", "playmat.svg")

# ── el mat sale medido DESDE la ilustración ─────────────────────────
# La sala es 4:3 y sus camas ocupan el 14,3% del ancho. Para que una
# carta de 63 mm caiga justo sobre la cama, el mat tiene que medir
# 63 / 0,143 = 440 mm de ancho. Todo lo demás se deduce de ahí.
W = 440.0
H_SALA = W * 3 / 4                # 330 mm: la ilustración, en su 4:3 natural
BANDA = 108.0                     # tu puesto, en el borde cercano de la mesa
H = H_SALA + BANDA                # 425 mm

# El puesto NO cabe dentro de la sala: el piso dibujado termina antes y las
# zonas quedaban pisando el muro del fondo. Así que el mat se extiende con
# una banda limpia abajo — que además es como funciona un playmat real: la
# sala allá, tu mesa de trabajo acá.

CW, CH = 63.0, 88.0               # la carta de póker

# posiciones medidas sobre la ilustración, en fracciones de H_SALA
CAMAS_X = (0.202, 0.511, 0.808)   # centro de cada cama
CAMA_Y0, CAMA_Y1 = 0.209, 0.591   # cabecera y pies de cama
VIDA_Y = 0.655                    # los corazones, en el suelo bajo la cama
EST_Y = H_SALA + 4.0              # tu puesto, ya en la banda

K = 0.22                          # barril del piso sintético (sin ilustración)
CX_B, CY_B = W / 2, H_SALA * 0.46

# ── paleta: celestes y blancos limpios ──────────────────────────────
PISO, PISO_2 = "#eef7fa", "#e2f0f6"
REJILLA, MURO, MURO_LIN = "#cfe6ee", "#d8ebf2", "#a9cede"
CELESTE, HONDO, TINTA = "#4aa3c7", "#1f6b8c", "#16323d"
BLANCO, VIDA = "#ffffff", "#c0492f"


def texto(x, y, txt, size=4.4, color=HONDO, peso=600, anchor="start",
          fam="Archivo Narrow", track=0.18, op=1.0, halo=True):
    """Rótulo. Sobre una ilustración el texto necesita halo para leerse."""
    comun = (f'x="{x:.1f}" y="{y:.1f}" font-family="{fam}, sans-serif" '
             f'font-size="{size}" font-weight="{peso}" '
             f'letter-spacing="{track}" text-anchor="{anchor}"')
    s = ""
    if halo:
        s += (f'<text {comun} fill="none" stroke="{BLANCO}" stroke-width="2.4" '
              f'stroke-linejoin="round" opacity="{0.85 * op:.2f}">{txt}</text>')
    s += f'<text {comun} fill="{color}" opacity="{op}">{txt}</text>'
    return s


def piso_sintetico():
    """Plan B: baldosas curvadas por barril, si no hay ilustración."""
    def barril(x, y):
        nx, ny = (x - CX_B) / (W / 2), (y - CY_B) / (H / 2)
        f = 1 + K * (nx * nx + ny * ny)
        return CX_B + nx * f * (W / 2), CY_B + ny * f * (H / 2)

    def curva(pts):
        return "M " + " L ".join(f"{x:.1f} {y:.1f}" for x, y in pts)

    s = [f'<rect x="0" y="0" width="{W:.0f}" height="{H_SALA:.0f}" fill="url(#suelo)"/>',
         f'<g fill="none" stroke="{REJILLA}" stroke-width="0.65">']
    for i in range(-2, 22):
        s.append('<path d="%s"/>' % curva(
            [barril(i * 26.0, -40 + 400 * k / 30) for k in range(31)]))
    for j in range(-1, 16):
        s.append('<path d="%s"/>' % curva(
            [barril(-60 + 560 * k / 40, j * 26.0) for k in range(41)]))
    s.append('</g>')
    borde = [barril(-60 + 560 * k / 40, H_SALA * 0.17) for k in range(41)]
    d = f"M -60 -40 L {W + 60:.0f} -40 L {W + 60:.0f} {borde[-1][1]:.1f}"
    for p in reversed(borde):
        d += f" L {p[0]:.1f} {p[1]:.1f}"
    s.append(f'<path d="{d} Z" fill="{MURO}"/>')
    s.append(f'<path d="{curva(borde)}" fill="none" stroke="{MURO_LIN}" '
             f'stroke-width="1.1"/>')
    return "\n".join(s)


def fondo_ilustrado():
    """La sala, incrustada en base64 y estirada a todo el mat."""
    if not os.path.isfile(FONDO):
        return None
    datos = base64.b64encode(open(FONDO, "rb").read()).decode()
    return (f'<image x="0" y="0" width="{W:.0f}" height="{H_SALA:.0f}" '
            f'preserveAspectRatio="xMidYMid slice" '
            f'href="data:image/jpeg;base64,{datos}"/>')


def construir():
    s = []
    a = s.append
    ilustrada = fondo_ilustrado()

    a(f'<svg xmlns="http://www.w3.org/2000/svg" '
      f'xmlns:xlink="http://www.w3.org/1999/xlink" '
      f'viewBox="0 0 {W:.0f} {H:.0f}" width="{W:.0f}mm" height="{H:.0f}mm" '
      f'role="img" aria-label="Playmat: unidad de cuidados intensivos de '
      f'tres camas vista desde arriba, con las zonas de juego marcadas">')

    a('<defs>')
    if not ilustrada:
        a(f'<radialGradient id="suelo" cx="50%" cy="42%" r="78%">'
          f'<stop offset="0%" stop-color="{BLANCO}"/>'
          f'<stop offset="55%" stop-color="{PISO}"/>'
          f'<stop offset="100%" stop-color="{PISO_2}"/></radialGradient>')
    a(f'<clipPath id="mat"><rect x="0" y="0" width="{W:.0f}" '
      f'height="{H:.0f}" rx="7"/></clipPath>')
    a('</defs>')

    a('<g clip-path="url(#mat)">')
    a(f'<rect x="0" y="0" width="{W:.0f}" height="{H:.0f}" fill="{PISO}"/>')
    a(ilustrada or piso_sintetico())
    # la banda de tu puesto: mismo piso, sin muebles
    a(f'<rect x="0" y="{H_SALA:.0f}" width="{W:.0f}" height="{BANDA:.0f}" '
      f'fill="{PISO_2}"/>')
    for k in range(1, 5):
        a(f'<path d="M 0 {H_SALA + k * 22:.0f} H {W:.0f}" stroke="{REJILLA}" '
          f'stroke-width="0.65" fill="none"/>')
    for k in range(1, 18):
        a(f'<path d="M {k * 26:.0f} {H_SALA:.0f} V {H:.0f}" '
          f'stroke="{REJILLA}" stroke-width="0.65" fill="none"/>')
    a(f'<path d="M 0 {H_SALA:.0f} H {W:.0f}" stroke="{MURO_LIN}" '
      f'stroke-width="1.6" fill="none" opacity="0.9"/>')
    a('</g>')

    # ── las tres bahías ─────────────────────────────────────────────
    slot_y = (CAMA_Y0 + (CAMA_Y1 - CAMA_Y0) / 2) * H_SALA - CH / 2  # centrada en la cama
    for i, fx in enumerate(CAMAS_X):
        cx = fx * W
        sx = cx - CW / 2
        # el slot: recto y a escala real, es donde se apoya la carta
        a(f'<rect x="{sx:.1f}" y="{slot_y:.1f}" width="{CW:.0f}" '
          f'height="{CH:.0f}" rx="3.5" fill="{BLANCO}" fill-opacity="0.30" '
          f'stroke="{HONDO}" stroke-width="1.3" stroke-dasharray="5.5 3.6"/>')
        a(texto(cx, slot_y + CH / 2 + 1.8, "PACIENTE", 5.2, HONDO, 700,
                "middle", track=1.6, op=0.5))
        a(texto(cx - CW / 2 - 4, slot_y + 13, str(i + 1), 17, HONDO, 700,
                "end", fam="Petrona, Georgia, serif", track=0, op=0.55))
        # la vida, en el suelo bajo la cama
        vy = VIDA_Y * H_SALA
        a(texto(cx - 36, vy + 1.6, "VIDA", 3.6, VIDA, 700, "start",
                track=0.9, op=0.95))
        for k in range(7):
            hx = cx - 17 + k * 9.6
            a(f'<path d="M {hx:.1f} {vy - 2.6:.1f} '
              f'c -1.8 -2.1 -4.3 -0.5 -4.3 1.5 c 0 2.1 2.6 3.6 4.3 4.9 '
              f'c 1.7 -1.3 4.3 -2.8 4.3 -4.9 c 0 -2.0 -2.5 -3.6 -4.3 -1.5 Z" '
              f'fill="{BLANCO}" fill-opacity="0.62" stroke="{VIDA}" '
              f'stroke-width="0.85" opacity="0.75"/>')

    # ── tu puesto, en el suelo despejado de abajo ───────────────────
    ey = EST_Y
    # avatar
    ax = W * 0.045
    a(f'<rect x="{ax:.1f}" y="{ey:.1f}" width="{CW:.0f}" height="{CH:.0f}" '
      f'rx="3.5" fill="{BLANCO}" fill-opacity="0.30" stroke="{HONDO}" '
      f'stroke-width="1.3" stroke-dasharray="5.5 3.6"/>')
    a(texto(ax + CW / 2, ey + CH / 2 + 1.8, "TU AVATAR", 5.2, HONDO, 700,
            "middle", track=1.5, op=0.5))

    # las tres indicaciones: la moneda del turno
    ix = W * 0.235
    a(texto(ix, ey + 9, "INDICACIONES DEL TURNO", 4.2, HONDO, 700, "start",
            track=1.1))
    for k in range(3):
        a(f'<circle cx="{ix + 12 + k * 28:.1f}" cy="{ey + 30:.1f}" r="11" '
          f'fill="{BLANCO}" fill-opacity="0.55" stroke="{CELESTE}" '
          f'stroke-width="1.6"/>')
    a(texto(ix, ey + 52, "Tratar &#183; Sabotear &#183; Des-escalar", 3.5,
            HONDO, 600, "start", track=0.3, op=0.85))
    a(texto(ix, ey + 60, "una ficha por indicación gastada", 3.5, HONDO, 500,
            "start", track=0.2, op=0.7))

    # sumarios
    sx2 = W * 0.485
    a(f'<rect x="{sx2:.1f}" y="{ey:.1f}" width="70" height="{CH:.0f}" rx="4" '
      f'fill="{BLANCO}" fill-opacity="0.22" stroke="{HONDO}" '
      f'stroke-width="1" stroke-dasharray="3.5 3" opacity="0.85"/>')
    a(texto(sx2 + 35, ey + 11, "SUMARIOS", 4.4, HONDO, 700, "middle", track=1.2))
    a(texto(sx2 + 35, ey + 19, "boca arriba", 3.4, HONDO, 500, "middle",
            track=0.3, op=0.75))
    a(texto(sx2 + 35, ey + 62, "cada uno te quita", 3.4, HONDO, 500, "middle",
            track=0.2, op=0.75))
    a(texto(sx2 + 35, ey + 69, "1 carta de mano", 3.4, HONDO, 700, "middle",
            track=0.2, op=0.85))
    a(texto(sx2 + 35, ey + 80, "cerrar: 2 cartas", 3.4, CELESTE, 700, "middle",
            track=0.2))

    # protocolos: caen justo sobre el mesón de enfermería de la ilustración
    px = W * 0.66
    a(f'<rect x="{px:.1f}" y="{ey:.1f}" width="{W * 0.29:.0f}" '
      f'height="{CH:.0f}" rx="4" fill="{BLANCO}" fill-opacity="0.22" '
      f'stroke="{CELESTE}" stroke-width="1" stroke-dasharray="3.5 3"/>')
    a(texto(px + W * 0.145, ey + 11, "TUS PROTOCOLOS", 4.4, HONDO, 700,
            "middle", track=1.2))
    a(texto(px + W * 0.145, ey + 19, "comprados en la Pizarra", 3.4, HONDO,
            500, "middle", track=0.3, op=0.75))
    for k in range(3):
        a(f'<rect x="{px + 12 + k * 34:.1f}" y="{ey + 26:.1f}" width="28" '
          f'height="40" rx="2.6" fill="{BLANCO}" fill-opacity="0.30" '
          f'stroke="{CELESTE}" stroke-width="0.9"/>')
    a(texto(px + W * 0.145, ey + 79, "máx. 1 compra y 1 jugada por turno", 3.4,
            HONDO, 500, "middle", track=0.2, op=0.75))

    # rótulo al borde inferior
    a(texto(W / 2, H - 6.5, "&#161;VAYA TURNO! &#183; TU UNIDAD &#183; 3 CAMAS",
            4.2, HONDO, 500, "middle", fam="IBM Plex Mono, monospace",
            track=2.4, op=0.55))

    a(f'<rect x="0.7" y="0.7" width="{W - 1.4:.1f}" height="{H - 1.4:.1f}" '
      f'rx="7" fill="none" stroke="{MURO_LIN}" stroke-width="1.4"/>')
    a('</svg>')
    return "\n".join(s), ilustrada is not None


if __name__ == "__main__":
    svg, con_arte = construir()
    os.makedirs(os.path.dirname(SALIDA), exist_ok=True)
    open(SALIDA, "w", encoding="utf-8").write(svg)
    print(f"✔ {SALIDA} — {W:.0f}×{H:.0f} mm · {len(svg) // 1024} KB")
    print("  fondo:", "sala ilustrada incrustada" if con_arte
          else "piso sintético (falta cartas/tablero/sala-uci.jpg)")
    print("  slots de carta: 63×88 mm · pide 3 mm de sangrado a la imprenta")
