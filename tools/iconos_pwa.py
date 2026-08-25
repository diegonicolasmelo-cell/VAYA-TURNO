#!/usr/bin/env python3
"""Los íconos de la app instalable — se dibujan, no se versionan a mano.

Una carta color papel, ligeramente inclinada sobre el teal del hospital,
con el ❤️ del paciente y la línea del monitor cruzando por detrás. Es lo
que se ve en la pantalla de inicio del teléfono, así que tiene que leerse
a 48 px: una carta, un corazón, nada más.

La versión `maskable` deja el 40% de margen que Android recorta al gusto
(círculo, cuadrado redondeado, gota) sin comerse el dibujo.

Se invoca solo desde generar_app.py --pwa; el dibujo es determinista, así
que regenerar no ensucia el repo.
"""

from PIL import Image, ImageDraw

TEAL = (10, 88, 96)          # fondo: el mismo verde del tablero
TEAL_2 = (17, 132, 145)      # el acento claro, para la línea del monitor
PAPEL = (255, 253, 248)
BORDE = (199, 214, 219)
CORAZON = (192, 73, 47)      # --vida


def _corazon(d, cx, cy, w, color):
    """Un corazón de dos lóbulos y punta, en coordenadas de píxel."""
    r = w / 2
    d.ellipse([cx - w / 2, cy - r * 0.62, cx + r * 0.06, cy + r * 0.38], fill=color)
    d.ellipse([cx - r * 0.06, cy - r * 0.62, cx + w / 2, cy + r * 0.38], fill=color)
    d.polygon([(cx - w / 2 + 1, cy - r * 0.10),
               (cx + w / 2 - 1, cy - r * 0.10),
               (cx, cy + r * 1.15)], fill=color)


def _carta(lado, escala):
    """La carta con su corazón, en su propia capa para poder inclinarla."""
    cw, ch = int(lado * 0.50 * escala), int(lado * 0.68 * escala)
    capa = Image.new("RGBA", (cw, ch), (0, 0, 0, 0))
    d = ImageDraw.Draw(capa)
    borde = max(2, int(lado * 0.012))
    d.rounded_rectangle([0, 0, cw - 1, ch - 1], radius=int(cw * 0.13),
                        fill=PAPEL, outline=BORDE, width=borde)
    _corazon(d, cw / 2, ch * 0.44, cw * 0.52, CORAZON)
    # la firma del reverso: tres puntos = las tres indicaciones del turno
    pr = max(2, int(cw * 0.045))
    for k in (-1, 0, 1):
        x = cw / 2 + k * cw * 0.17
        d.ellipse([x - pr, ch * 0.78 - pr, x + pr, ch * 0.78 + pr], fill=TEAL_2)
    return capa


def dibujar(lado, escala=1.0):
    """Un ícono cuadrado de `lado` px. escala<1 = margen para maskable."""
    im = Image.new("RGBA", (lado, lado), TEAL + (255,))
    d = ImageDraw.Draw(im)

    # la línea del monitor cruza el fondo, detrás de la carta
    gr = max(2, int(lado * 0.018))
    y = lado * 0.62
    p = lado * 0.5 - lado * 0.44 * escala
    ancho = lado * 0.88 * escala
    alto = lado * 0.13 * escala
    pts = [(p, y), (p + ancho * 0.06, y),
           (p + ancho * 0.10, y - alto),
           (p + ancho * 0.14, y + alto * 0.55),
           (p + ancho * 0.18, y), (p + ancho * 0.82, y),
           (p + ancho * 0.86, y - alto),
           (p + ancho * 0.90, y + alto * 0.55),
           (p + ancho * 0.94, y), (p + ancho, y)]
    d.line(pts, fill=TEAL_2, width=gr, joint="curve")

    carta = _carta(lado, escala).rotate(-9, resample=Image.BICUBIC, expand=True)
    im.alpha_composite(carta, (int((lado - carta.width) / 2),
                               int((lado - carta.height) / 2)))
    return im.convert("RGB")


def generar(carpeta):
    """Escribe el juego completo de íconos y devuelve sus nombres."""
    import os
    os.makedirs(carpeta, exist_ok=True)
    salidas = {
        "icono-192.png": dibujar(192, 1.0),
        "icono-512.png": dibujar(512, 1.0),
        "icono-maskable-512.png": dibujar(512, 0.62),   # zona segura 80%
        "apple-touch-icon.png": dibujar(180, 1.0),
    }
    for nombre, im in salidas.items():
        im.save(os.path.join(carpeta, nombre), "PNG", optimize=True)
    return sorted(salidas)


if __name__ == "__main__":
    import os
    raiz = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(generar(os.path.join(raiz, "docs", "juego", "iconos")))
