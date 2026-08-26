#!/usr/bin/env python3
"""Los íconos de la app instalable — se dibujan, no se versionan a mano.

El emblema del logotipo: el monitor con la línea del ECG, sobre el amarillo
de las letras y con el mismo contorno azul marino. No es un recorte del
logo —ahí el monitor mide 180 px y estirarlo a 512 lo dejaba blando—, está
redibujado con los colores tomados del archivo, así que sale nítido a
cualquier tamaño.

El nombre completo NO cabe: a 48 px, que es como se ve en la pantalla de
inicio de un teléfono, cada línea del logotipo quedaría de 7 px de alto.
Un objeto se reconoce a ese tamaño; dos palabras apiladas, no.

La versión `maskable` deja el margen que Android recorta al gusto (círculo,
cuadrado redondeado, gota) sin comerse el dibujo.

Se invoca solo desde generar_app.py --pwa; el dibujo es determinista, así
que regenerar no ensucia el repo.
"""

from PIL import Image, ImageDraw

# Todos tomados del logotipo con un cuentagotas, no elegidos a ojo.
AMARILLO = (253, 230, 17)        # #fde611 — la cara de las letras
AMARILLO_2 = (245, 197, 20)      # el amarillo se oscurece hacia abajo
ORO = (200, 145, 20)             # el bisel bajo cada letra
MARINO = (17, 48, 106)           # #11306a — el contorno de todo
PANTALLA = (3, 52, 88)           # #033458 — el vidrio del monitor
ECG = (43, 230, 180)             # #2be6b4 — el trazo
CUERPO = (206, 217, 226)         # la carcasa gris del monitor
CUERPO_2 = (168, 183, 196)
TUBO = (58, 160, 224)
NARANJA = (240, 125, 24)

SS = 4                           # se dibuja en grande y se reduce: así hay
                                 # bordes suaves sin filtros ni trucos


def _emblema(d, x, y, w, gr):
    """El monitor, con su ancho `w` y grosor de contorno `gr`, centrado
    en (x, y). Todas las medidas salen de `w` para que escale entero."""
    h = w * 0.74
    izq, arr = x - w / 2, y - h / 2

    # el tubo sale por la derecha y da una vuelta — es lo que lo hace un
    # monitor de verdad y no una tele
    tv = w * 0.115
    curva = [(izq + w * 0.92, arr + h * 0.40), (izq + w * 1.20, arr + h * 0.40),
             (izq + w * 1.31, arr + h * 0.60), (izq + w * 1.28, arr + h * 0.88),
             (izq + w * 1.09, arr + h * 1.00)]
    d.line(curva, fill=MARINO, width=int(tv + gr * 2), joint="curve")
    d.line(curva, fill=TUBO, width=int(tv), joint="curve")

    # la carcasa
    r = w * 0.10
    d.rounded_rectangle([izq, arr, izq + w, arr + h], r,
                        fill=CUERPO, outline=MARINO, width=int(gr))
    d.rounded_rectangle([izq + gr, arr + h * 0.72, izq + w - gr, arr + h - gr],
                        r * 0.5, fill=CUERPO_2)

    # el vidrio
    px0, py0 = izq + w * 0.10, arr + h * 0.11
    px1, py1 = izq + w * 0.90, arr + h * 0.66
    d.rounded_rectangle([px0, py0, px1, py1], w * 0.045,
                        fill=PANTALLA, outline=MARINO, width=int(gr * 0.7))

    # el trazo: UN latido, grande. Con dos, a 48 px se empastan y quedan
    # como una mancha verde; con uno se sigue leyendo como un ECG.
    pw, ph = px1 - px0, py1 - py0
    base = py0 + ph * 0.58
    pico = ph * 0.46
    d.line([(px0 + pw * 0.07, base), (px0 + pw * 0.30, base),
            (px0 + pw * 0.40, base - pico),
            (px0 + pw * 0.50, base + pico * 0.62),
            (px0 + pw * 0.60, base), (px0 + pw * 0.93, base)],
           fill=ECG, width=max(1, int(gr * 1.15)), joint="curve")

    # los botones de abajo
    br = w * 0.043
    for i, col in enumerate((NARANJA, TUBO, TUBO)):
        bx = izq + w * (0.20 + i * 0.24)
        by = arr + h * 0.855
        d.ellipse([bx - br, by - br, bx + br, by + br],
                  fill=col, outline=MARINO, width=max(1, int(gr * 0.5)))


def dibujar(lado, escala=1.0, marco=True):
    """Un ícono cuadrado de `lado` px. escala<1 = margen para maskable."""
    L = lado * SS
    im = Image.new("RGBA", (L, L), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)

    # el campo amarillo, degradado como la cara de las letras
    for i in range(L):
        t = i / max(L - 1, 1)
        d.line([(0, i), (L, i)],
               fill=tuple(round(a + (b - a) * t)
                          for a, b in zip(AMARILLO, AMARILLO_2)) + (255,))
    if marco:
        # el mismo marco azul del logotipo, por dentro
        m = L * 0.055
        d.rounded_rectangle([m, m, L - m, L - m], L * 0.14,
                            outline=MARINO, width=int(L * 0.045))

    # el monitor va corrido a la izquierda porque el tubo sale a la derecha:
    # lo que hay que centrar es el conjunto, no la carcasa
    w = L * 0.56 * escala
    _emblema(d, L / 2 - w * 0.14, L * 0.50, w, max(SS, L * 0.018 * escala))
    return im.resize((lado, lado), Image.LANCZOS).convert("RGB")


def generar(carpeta):
    """Escribe el juego completo de íconos y devuelve sus nombres."""
    import os
    os.makedirs(carpeta, exist_ok=True)
    salidas = {
        "icono-192.png": dibujar(192),
        "icono-512.png": dibujar(512),
        "icono-maskable-512.png": dibujar(512, 0.70, marco=False),
        "apple-touch-icon.png": dibujar(180),
    }
    for nombre, im in salidas.items():
        im.save(os.path.join(carpeta, nombre), "PNG", optimize=True)
    return sorted(salidas)


if __name__ == "__main__":
    import os
    raiz = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(generar(os.path.join(raiz, "docs", "juego", "iconos")))
