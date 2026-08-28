# Prompts del tablero — el ambiente de la unidad

Dos bandas que hoy están vectorizadas en `tools/generar_ambiente_app.py` y
que hay que llevar a ilustración de verdad, en el estilo de la casa. Cada
prompt es **completo y autónomo**: lleva dentro el estilo, la vista, la
paleta y —lo más importante— **las posiciones exactas**, para que el dibujo
caiga donde ya cae el vector y no haya que rehacer el CSS.

## Antes de generar, cuatro reglas que valen para las dos

1. **Vista cenital pura.** Todo el tablero se lee desde arriba, en planta.
   Es lo más difícil de conseguir de un generador: hay que insistir. Nada de
   horizonte, nada de punto de fuga, nada de paredes en perspectiva.
2. **Se usa espejada.** La misma imagen se gira 180° para el lado del rival,
   así que **no puede llevar texto, ni flechas, ni nada que se lea al
   revés**.
3. **Dibuja a fuerza completa, que la app la lava.** Encima van cartas: el
   ambiente tiene que quedar tenue. Eso no se pide al generador —sale mal—,
   lo hace el pipeline mezclando hacia el papel, igual que
   `generar_sala_app.py` con la sala. Genera con color y contraste normales.
4. **Sangre por los cuatro lados.** Las bandas tocan el filo de la pantalla:
   el mostrador se corta abajo y el suelo se corta a los costados.

---

## A · El mesón de enfermería

Va en los dos bordes exteriores del tablero: abajo es el tuyo —el retrato
del avatar se apoya en el centro de su curva— y arriba el del rival,
girado. Franja de **390 × 84 px CSS**; pide **3:1 (1560 × 520)** y compón el
mostrador en los **dos tercios de abajo**, que el tercio de arriba es piso
que se recorta.

```
Modern flat-vector cartoon illustration in the style of a contemporary
animated TV series. Clean digital finish: smooth flat color fills with soft
two-step cel shading. No visible brush texture, no grain, no photorealism,
no gradients beyond the gentle cel shading.

LINE: medium-weight outline in desaturated dark brown or deep teal, never
pure black; even and confident. Interior detail lines noticeably thinner
than the silhouette.

VIEW — THIS IS THE HARD PART, READ IT TWICE: strict orthographic TOP-DOWN
view, as if a camera bolted to the ceiling were looking straight down at the
floor. A floor plan that happens to be drawn, like the map of a board game.
There is NO horizon, NO vanishing point, NO wall seen from the side, NO
perspective depth. Every single object is seen from directly above: you see
the tops of things, never their fronts.

SCENE: the counter of a hospital nursing station, seen from straight above.
A long curved reception desk runs across the whole width of the frame and
continues past the left and right edges. Its back edge is a gentle convex
curve with generous rounded corners; the desk surface fills everything below
that curve and is cut off by the bottom edge of the frame. A narrow raised
ledge runs along the back edge of the desk. The desktop is made of panels
with visible seams between them.

WHAT SITS ON THE DESK, from left to right, seen from above:
- at 7-16% of the width: a flat computer monitor on its stand (you see the
  top of the screen and the oval base) with a keyboard just below it, closer
  to the bottom edge;
- at 22-24%: a coffee mug, a plain circle with the handle sticking out to
  the right;
- at 26-30%: a cup of pens, a small circle with two pens poking out;
- at 38-45%, sitting on the raised back ledge: three small round call-light
  indicators in a row;
- at 67-79%: three manila folders stacked in a loose fan, each offset a
  little from the one below;
- at 84-93%: a desk telephone with a coiled cord curling off to the right.

KEEP THE MIDDLE CLEAR: from 36% to 64% of the width the desktop must be
completely empty — no objects, no props, nothing. A character portrait sits
there in the game and would cover anything drawn in that band.

NO PEOPLE, no hands, no chairs, no plants. No text of any kind: no signs, no
labels, no numbers on the monitor, no writing on the folders. The monitor
screen is blank.

COLOR: one single cool hospital palette, everything in the same family —
pale blue-grey floor (#dfe7ea), desk in a slightly warmer greyed teal, props
picked out in muted teal (#4a8a96) and soft warm grey. One tiny accent of
muted terracotta is allowed on a single object. Low overall contrast, calm
and clean. Full-bleed, never white paper.

FORMAT: ultra-wide horizontal banner, aspect ratio 3:1 (1560 x 520 px). The
desk occupies the bottom two thirds; the top third is plain empty floor.
```

---

## B · El suelo de la unidad

Va en las franjas de aire entre las camas y el mesón. La fila de camas queda
**arriba** de esta imagen: contra ella van el cabecero y la cortina. Franja
de **390 × 168 px CSS**; pide **7:3 (1568 × 672)**.

```
Modern flat-vector cartoon illustration in the style of a contemporary
animated TV series. Clean digital finish: smooth flat color fills with soft
two-step cel shading. No visible brush texture, no grain, no photorealism.

LINE: medium-weight outline in desaturated dark brown or deep teal, never
pure black; even and confident. Interior detail lines noticeably thinner
than the silhouette.

VIEW — THIS IS THE HARD PART, READ IT TWICE: strict orthographic TOP-DOWN
view, as if a camera bolted to the ceiling were looking straight down at the
floor. A floor plan that happens to be drawn, like the map of a board game.
There is NO horizon, NO vanishing point, NO wall seen from the side, NO
perspective depth. Every single object is seen from directly above.

SCENE: the empty floor of a hospital intensive-care unit between the beds
and the nursing station, seen from straight above. Polished pale floor with
a very faint tile pattern, a few soft scuff marks and the ghost of a
reflection.

WHAT IS IN THE FRAME, by position:
- ACROSS THE VERY TOP EDGE, running the full width: the headwall service
  rail — a long rounded bar with evenly spaced round gas outlets along it,
  the strip that sits behind every ICU bed. Just below it, a ceiling curtain
  track: a long thin dashed line spanning the width, with two or three
  bunched curtain folds gathered at its ends.
- LEFT SIDE, from 4% to 12% of the width and from 27% to 71% of the height:
  a spare gurney parked lengthwise against the wall, seen from above — a
  rounded rectangle mattress with two cross seams and four caster wheels at
  its corners.
- LEFT, at 15-20% of the width and 15-23% of the height: a small sharps
  container mounted low, a boxy shape with a lid.
- RIGHT, at 75-79% of the width and 14-20% of the height: a wall-mounted
  alcohol gel dispenser with its little nozzle pointing down.
- RIGHT, at 88-93% of the width and 30-40% of the height: an IV pole seen
  from directly above — a small hub circle with five thin legs radiating out
  like a star, each ending in a caster.
- RIGHT, from 85% to 97% of the width and 54% to 73% of the height: a linen
  trolley, a rounded rectangle with a lid seam across it and a divider.

KEEP THE MIDDLE CLEAR: the central 55% of the width, from 20% of the height
downward, must be plain empty floor. Cards are played over that area.

NO PEOPLE, no beds with patients, no monitors, no text of any kind — no
signs, no floor markings with letters, no numbers.

COLOR: the same single cool hospital palette as the nursing-station banner —
pale blue-grey floor (#dfe7ea), equipment in muted teal (#4a8a96) and soft
warm grey, everything in one family. Low overall contrast, calm and clean.
Full-bleed, never white paper.

FORMAT: wide horizontal banner, aspect ratio 7:3 (1568 x 672 px).
```

---

## Cuando lleguen

Van a `cartas/tablero/` como `meson.png` y `suelo.png`. El paso siguiente es
un lavado hacia el papel del tablero (la sala usa 0,45 de mezcla con blanco)
y meterlas por las mismas variables CSS que hoy llenan los SVG:
`--meson-mio`, `--meson-suyo`, `--suelo-mio`, `--suelo-suyo`. Las versiones
"suyo" son la misma imagen girada 180°, así que sale una sola generación por
banda.
