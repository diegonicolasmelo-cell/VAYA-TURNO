#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""La pantalla de inicio, vectorizada: el auxiliar trapeando la unidad.

Es la escena A de docs/PROMPTS-PORTADA.md —la calma antes del turno—
llevada al mismo lenguaje vectorial del tablero. El auxiliar va al centro,
grande, de espaldas en tres cuartos, con su carro amarillo, el cono de piso
mojado y las tres salas con las camas hechas al fondo. La acción vive en el
55 % de arriba; el 45 % de abajo es piso limpio recién trapeado, que es
donde caen el logo y el menú.

    python3 tools/generar_portada_vector.py

Escribe arte/portada/dibujo.svg (la app lo prefiere al video cuando existe:
borrarlo devuelve el clip) y docs/portada-vector.svg para mandarlo a editar.
Después hay que regenerar la app y la PWA.
"""
import os

L = "#4a3a2e"        # el delineado café de la casa
W, H = 390, 844
# La escena entera baja BAJA px. Arriba hay sitio de sobra —el pasillo se ve
# vacío— y el logotipo se topaba con las salas de vidrio: bajando el dibujo
# las letras quedan solas contra el cielo raso y no tapan nada.
#
# 66 es lo que deja el menú de tres fichas: con los cuatro botones altos de
# antes el dibujo no podía bajar de 40 sin que le cortaran los pies al
# auxiliar. Aquí el logotipo queda solo contra el cielo raso.
BAJA = 66

def svg():
    p = []
    a = p.append

    # ── fondo: cielo raso, muro y piso ────────────────────────────────
    # va FUERA del grupo que baja, y estirado hacia arriba, para que el
    # corrimiento no deje una franja hueca sobre el cielo raso
    fondo = (f'<rect y="{-BAJA}" width="{W}" height="{252+BAJA*2}" fill="#d7e1e5"/>'
             f'<rect y="{-BAJA}" width="{W}" height="{96+BAJA*2}" fill="#e9eff1"/>'
             f'<rect y="{252+BAJA}" width="{W}" height="{H-252}" fill="#e4ecef"/>')
    # El cielo raso queda LIMPIO: ahí se apoya el logotipo y cualquier cosa
    # que se dibuje se le cruza por las letras. Las luminarias se quedan solo
    # como charco de luz en el piso, más abajo.
    a(f'<path d="M0 96 L{W} 96" stroke="{L}" stroke-width="2" opacity=".5"/>')
    # el reloj se muda del techo al muro, junto al letrero: siete y diez
    a(f'<circle cx="132" cy="109" r="9" fill="#fbfdfd" stroke="{L}" stroke-width="2"/>')
    a(f'<path d="M132 109 L132 103 M132 109 L137 110" stroke="{L}" stroke-width="1.8" '
      f'stroke-linecap="round"/>')

    # el letrero de la unidad
    a(f'<rect x="163" y="100" width="64" height="18" rx="4" fill="#4a8a96" '
      f'stroke="{L}" stroke-width="2"/>')
    a('<text x="195" y="113.5" text-anchor="middle" font-family="Arial,sans-serif" '
      'font-size="11" font-weight="bold" fill="#f2f7f8" letter-spacing="3">UCI</text>')

    # ── las tres salas de vidrio, con las camas hechas ────────────────
    for x0 in (16, 142, 268):
        a(f'<rect x="{x0}" y="122" width="106" height="130" rx="5" fill="#ecf4f5" '
          f'stroke="#4a8a96" stroke-width="3"/>')
        a(f'<path d="M{x0+53} 122 L{x0+53} 252" stroke="#4a8a96" stroke-width="1.6" opacity=".7"/>')
        # el monitor apagado en el muro
        a(f'<rect x="{x0+12}" y="138" width="26" height="17" rx="2.5" fill="#37464e" '
          f'stroke="{L}" stroke-width="1.6"/>')
        # la cama hecha, de lado: base, colchón, almohada, frazada tirante
        a(f'<rect x="{x0+16}" y="214" width="74" height="10" rx="3" fill="#b9c7cc" '
          f'stroke="{L}" stroke-width="1.6"/>')
        a(f'<rect x="{x0+13}" y="196" width="80" height="20" rx="6" fill="#fbfdfd" '
          f'stroke="{L}" stroke-width="1.8"/>')
        a(f'<rect x="{x0+16}" y="192" width="20" height="12" rx="5" fill="#fefefe" '
          f'stroke="{L}" stroke-width="1.6"/>')
        a(f'<path d="M{x0+42} 196 L{x0+42} 216 M{x0+42} 202 L{x0+93} 202" '
          f'stroke="#a7c8ce" stroke-width="3.4" opacity=".9"/>')
        # patas y ruedas
        a(f'<circle cx="{x0+22}" cy="228" r="3.4" fill="#8fa2ab" stroke="{L}" stroke-width="1.4"/>')
        a(f'<circle cx="{x0+84}" cy="228" r="3.4" fill="#8fa2ab" stroke="{L}" stroke-width="1.4"/>')
        # el atril de suero, quieto
        a(f'<path d="M{x0+96} 156 L{x0+96} 224" stroke="{L}" stroke-width="1.8"/>')
        a(f'<path d="M{x0+90} 158 L{x0+102} 158" stroke="{L}" stroke-width="1.8"/>')
        # el reflejo del vidrio
        a(f'<path d="M{x0+14} 240 L{x0+52} 128 M{x0+30} 246 L{x0+68} 134" '
          f'stroke="#ffffff" stroke-width="7" opacity=".28" stroke-linecap="round"/>')
    a(f'<path d="M0 252 L{W} 252" stroke="{L}" stroke-width="2.4" opacity=".6"/>')

    # ── el piso en fuga, muy suave ────────────────────────────────────
    for k in (-4, -3, -2, 2, 3, 4):
        a(f'<path d="M{195 + k*42} 252 L{195 + k*104} {H}" stroke="#8fb0b8" '
          f'stroke-width="1.1" opacity=".16"/>')
    for y, op in ((300, .16), (368, .15), (452, .13), (566, .11), (708, .09)):
        a(f'<path d="M0 {y} L{W} {y}" stroke="#8fb0b8" stroke-width="1.1" opacity="{op}"/>')
    # el reflejo de las luces en el piso limpio
    for x in (78, 252):
        a(f'<ellipse cx="{x+30}" cy="560" rx="26" ry="130" fill="#ffffff" opacity=".14"/>')

    # ── el brillo del trapeado y la huella húmeda ─────────────────────
    a('<ellipse cx="224" cy="456" rx="92" ry="27" fill="#ffffff" opacity=".4"/>')
    a(f'<path d="M150 478 Q240 502 292 458" stroke="#ffffff" stroke-width="7" '
      f'opacity=".5" fill="none" stroke-linecap="round"/>')
    a(f'<path d="M140 502 Q232 530 306 472" stroke="#cfe4e8" stroke-width="5" '
      f'opacity=".55" fill="none" stroke-linecap="round"/>')

    # ── el cono de piso mojado ────────────────────────────────────────
    a(f'<ellipse cx="76" cy="466" rx="26" ry="7" fill="#c7d4d9" opacity=".7"/>')
    a(f'<path d="M76 398 L98 462 L54 462 Z" fill="#f0b429" stroke="{L}" stroke-width="2.4" '
      f'stroke-linejoin="round"/>')
    a(f'<path d="M64 434 L88 434 L84 420 L68 420 Z" fill="#fbfdfd" stroke="{L}" stroke-width="1.6"/>')
    a(f'<rect x="48" y="458" width="56" height="8" rx="3" fill="#f0b429" stroke="{L}" stroke-width="2"/>')

    # ── el carro amarillo, con la radio sonando ───────────────────────
    a(f'<ellipse cx="322" cy="474" rx="46" ry="8" fill="#c7d4d9" opacity=".7"/>')
    a(f'<rect x="282" y="392" width="82" height="72" rx="8" fill="#e8b73c" '
      f'stroke="{L}" stroke-width="2.6"/>')
    a(f'<path d="M282 420 L364 420" stroke="{L}" stroke-width="1.6" opacity=".55"/>')
    # los dos baldes hundidos en la tapa
    a(f'<ellipse cx="305" cy="392" rx="17" ry="7" fill="#4a8a96" stroke="{L}" stroke-width="2.2"/>')
    a(f'<ellipse cx="305" cy="390" rx="12" ry="4.4" fill="#71a7b1"/>')
    a(f'<ellipse cx="341" cy="392" rx="14" ry="6" fill="#9fb0b8" stroke="{L}" stroke-width="2.2"/>')
    # la manilla, el rociador colgado y las ruedas
    a(f'<path d="M366 392 Q378 392 378 404 L378 448" stroke="{L}" stroke-width="3" fill="none"/>')
    a(f'<rect x="270" y="404" width="11" height="17" rx="3" fill="#4a8a96" stroke="{L}" stroke-width="1.8"/>')
    a(f'<path d="M273 404 L272 398 L279 398" stroke="{L}" stroke-width="1.6" fill="none"/>')
    a(f'<circle cx="296" cy="468" r="7" fill="#37464e" stroke="{L}" stroke-width="1.8"/>')
    a(f'<circle cx="350" cy="468" r="7" fill="#37464e" stroke="{L}" stroke-width="1.8"/>')
    # la radio, encima, con su antena y sus notas
    a(f'<rect x="316" y="374" width="26" height="16" rx="3" fill="#37464e" stroke="{L}" stroke-width="2"/>')
    a(f'<circle cx="323" cy="382" r="3.4" fill="#9fb0b8"/>')
    a(f'<path d="M338 374 L346 360" stroke="{L}" stroke-width="1.8"/>')
    a('<text x="352" y="360" font-family="Arial,sans-serif" font-size="15" fill="#4a8a96">♪</text>')
    a('<text x="362" y="344" font-family="Arial,sans-serif" font-size="12" fill="#4a8a96" opacity=".8">♪</text>')

    # ── el auxiliar, de espaldas en tres cuartos ──────────────────────
    # El auxiliar sube 54 px DENTRO de la escena, que a su vez baja 40: neto
    # queda 14 px más arriba que antes. Es lo que hace falta para que el
    # dibujo pueda bajar —y despejar el logotipo— sin que el menú, que
    # arranca en y=470, le corte la cabeza del trapero. Queda de pie delante
    # de las salas, que es donde va: él está en el pasillo.
    a('<g transform="translate(0,-34)">')
    a('<ellipse cx="152" cy="472" rx="42" ry="9" fill="#b9c9cf" opacity=".8"/>')
    # las piernas en zancada corta, con los zuecos
    a(f'<path d="M138 400 L132 452 Q131 460 138 460 L148 460 L150 402 Z" '
      f'fill="#6f8a3f" stroke="{L}" stroke-width="2.4" stroke-linejoin="round"/>')
    a(f'<path d="M158 400 L164 450 Q165 458 172 458 L182 458 L176 398 Z" '
      f'fill="#7d9648" stroke="{L}" stroke-width="2.4" stroke-linejoin="round"/>')
    a(f'<path d="M130 460 Q128 470 137 470 L152 470 Q157 470 155 461 Z" '
      f'fill="#e8edf0" stroke="{L}" stroke-width="2.2"/>')
    a(f'<path d="M164 458 Q162 468 171 468 L186 468 Q191 468 188 459 Z" '
      f'fill="#e8edf0" stroke="{L}" stroke-width="2.2"/>')
    # el torso lima, apenas girado hacia el trapero
    a(f'<path d="M126 322 Q124 300 140 292 L172 290 Q190 296 190 318 '
      f'L184 404 Q158 412 132 404 Z" fill="#a9c25d" stroke="{L}" stroke-width="2.6" '
      f'stroke-linejoin="round"/>')
    a(f'<path d="M168 294 Q186 300 186 320 L182 402 Q172 406 162 406 Z" '
      f'fill="#93ad4c" opacity=".8"/>')
    a(f'<path d="M128 356 Q158 364 186 356" stroke="{L}" stroke-width="1.4" opacity=".4" fill="none"/>')
    # el brazo izquierdo cae al agarre bajo; el derecho cruza al agarre alto
    a(f'<path d="M128 316 Q116 344 138 366 Q146 372 152 366 L160 356 Q150 344 146 326 Z" '
      f'fill="#a9c25d" stroke="{L}" stroke-width="2.4" stroke-linejoin="round"/>')
    a(f'<path d="M184 312 Q200 322 202 340 L196 352 Q184 348 176 338 Z" '
      f'fill="#93ad4c" stroke="{L}" stroke-width="2.4" stroke-linejoin="round"/>')
    # las manos al palo
    a(f'<circle cx="157" cy="362" r="7.5" fill="#e8b48c" stroke="{L}" stroke-width="2.2"/>')
    a(f'<circle cx="200" cy="348" r="7.5" fill="#e8b48c" stroke="{L}" stroke-width="2.2"/>')
    # la cabeza de espaldas: nuca, moño y el audífono puesto
    a(f'<path d="M138 268 Q138 246 158 246 Q178 246 178 268 Q178 288 158 290 '
      f'Q138 288 138 268 Z" fill="#4c3b2a" stroke="{L}" stroke-width="2.6"/>')
    a(f'<circle cx="162" cy="244" r="10" fill="#4c3b2a" stroke="{L}" stroke-width="2.4"/>')
    a(f'<path d="M176 272 Q180 276 178 282 Q172 284 170 278 Z" fill="#e8b48c" '
      f'stroke="{L}" stroke-width="1.8"/>')
    # el audífono de orejera: de espaldas se ven la diadema cruzando la
    # coronilla y las dos copas, una a cada lado de la cabeza
    a(f'<path d="M134 272 Q136 236 158 234 Q180 236 182 272" fill="none" '
      f'stroke="#37464e" stroke-width="6" stroke-linecap="round"/>')
    a(f'<path d="M134 272 Q136 236 158 234 Q180 236 182 272" fill="none" '
      f'stroke="{L}" stroke-width="8.4" stroke-linecap="round" opacity=".3"/>')
    a(f'<path d="M137 240 Q158 232 179 240" stroke="#5c6f78" stroke-width="3" '
      f'fill="none" stroke-linecap="round"/>')
    for cx in (133, 183):
        a(f'<rect x="{cx-9}" y="262" width="18" height="24" rx="8" fill="#4a5b64" '
          f'stroke="{L}" stroke-width="2.4"/>')
        a(f'<rect x="{cx-5}" y="267" width="10" height="14" rx="5" fill="#6f838d"/>')
    # el cable que baja al bolsillo
    a(f'<path d="M133 286 Q128 306 136 322" stroke="#37464e" stroke-width="2.2" fill="none"/>')
    # el cuello de la tunica
    a(f'<path d="M144 292 Q158 298 172 291" stroke="{L}" stroke-width="1.8" fill="none" opacity=".6"/>')

    # ── el trapero ────────────────────────────────────────────────────
    # el palo llega hasta y=460 y no más: por debajo empieza el menú
    a(f'<path d="M150 340 L232 458" stroke="#b58a4e" stroke-width="6" stroke-linecap="round"/>')
    a(f'<path d="M150 340 L232 458" stroke="{L}" stroke-width="8.5" stroke-linecap="round" opacity=".28"/>')
    a(f'<path d="M212 454 Q232 442 252 454 Q262 462 254 470 Q232 482 210 470 '
      f'Q202 462 212 454 Z" fill="#f2f5f6" stroke="{L}" stroke-width="2.4"/>')
    for dx in (-12, -4, 4, 12):
        a(f'<path d="M{232+dx} 468 Q{233+dx} 476 {230+dx} 480" stroke="#d5dee2" '
          f'stroke-width="3" fill="none" stroke-linecap="round"/>')
    a('</g>')

    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
            f'width="{W}" height="{H}" preserveAspectRatio="xMidYMid slice">'
            + fondo + f'<g transform="translate(0,{BAJA})">' + "".join(p) + '</g></svg>')


RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
s = svg()
for destino in (os.path.join(RAIZ, "arte", "portada", "dibujo.svg"),
                os.path.join(RAIZ, "docs", "portada-vector.svg")):
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    open(destino, "w", encoding="utf-8").write(s)
print(f"✔ portada vectorizada · {len(s)//1024} KB · arte/portada/dibujo.svg + docs/portada-vector.svg")
print("  la app la prefiere al video; borrar dibujo.svg devuelve el clip")
print("  ahora: generar_app.py y generar_app.py --pwa")
