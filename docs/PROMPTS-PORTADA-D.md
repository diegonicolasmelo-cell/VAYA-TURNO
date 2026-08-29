# Prompt de portada · D — la versión que está en la app

Las tres escenas de `PROMPTS-PORTADA.md` eran ideas sueltas. Ésta no: es la
portada **que ya existe**, vectorizada en `tools/generar_portada_vector.py` y
en pantalla ahora mismo. El prompt de abajo la manda a dibujar en serio, con
las posiciones exactas del vector, para que la ilustración caiga donde ya cae
y no haya que mover una línea de CSS.

Es la escena A —la calma antes del turno— con lo que el autor pidió después:
el auxiliar **con audífonos de orejera, bailando**, y las tres salas del fondo
**en pleno caos**. El chiste es que él es lo único tranquilo de la pantalla.

## Las cinco reglas de esta portada

1. **Formato 9:19,5 vertical** (1080 × 2340). Es la pantalla del teléfono. Si
   el generador no lo ofrece, pide **9:16** y compón todo dentro del 88 %
   central del alto: la app la usa a sangre y recorta por arriba y por abajo.
2. **El 19 % de arriba es cielo raso vacío.** Ahí va el logotipo. Nada de
   luminarias, carteles ni tuberías: cualquier cosa que se dibuje ahí se le
   cruza por las letras.
3. **El 28 % de abajo es piso limpio y vacío.** Ahí van los tres botones.
   Suelo recién trapeado, reflejos suaves, nada más.
4. **Toda la acción vive entre el 19 % y el 72 %.** Ese es el encuadre útil.
5. **Sin texto**, salvo el letrero de la unidad, que dice `UCI` y nada más.

## El prompt

```
Modern flat-vector cartoon illustration in the style of a contemporary
animated TV series. Clean digital finish: smooth flat color fills with soft
two-step cel shading. No visible brush texture, no grain, no photorealism.

LINE: medium-weight outline in desaturated dark brown, never pure black;
even and confident, slightly tapered. Interior detail lines noticeably
thinner than the silhouette.

CHARACTERS: adult naturalistic proportions with a slightly enlarged head
(about 5 to 6 heads tall). Chilean public-hospital cast: varied ages, builds
and skin tones. Teal or navy scrubs and white coats for the clinical staff.

SCENE: the corridor of a hospital intensive-care unit, twenty minutes before
the shift starts, seen straight on at eye level — a flat theatre-stage view,
not a dramatic angle. Three glass-walled ICU rooms across the back wall, and
the polished corridor floor in the foreground.

THE JOKE, and it is the whole point: in the foreground a cleaning auxiliary
is mopping, calm and happy and completely oblivious, while behind the glass
all three rooms are in the middle of something. Nobody in the rooms looks at
him. He does not look at them.

COMPOSITION, by percentage of the frame height — follow this closely:
- 0 to 19%: plain empty ceiling. Absolutely nothing here. No lights, no
  signs, no pipes, no vents. Just a pale flat ceiling.
- at 19%: the line where ceiling meets the back wall. Immediately below it,
  centered, a small teal wall sign reading UCI, and a round wall clock a
  little to its left showing ten past seven.
- 22% to 38%: the three glass-walled rooms, side by side, evenly spaced, each
  one about 27% of the frame width, with teal metal frames and soft
  reflections on the glass. Their contents are listed below.
- at 38%: the floor line.
- 33% to 59%, centered horizontally: the cleaning auxiliary, seen FROM
  BEHIND at a three-quarter angle, mopping. He wears a lime-green work tunic
  and trousers with white clogs, hair tied in a small bun, and — this
  matters — big OVER-EAR HEADPHONES: a padded band arcing over the crown and
  a round cushioned cup covering each ear. His weight is on one hip and his
  shoulders are tilted: he is dancing to whatever he is listening to,
  relaxed, unhurried, mid-sway. The mop reaches down and to his right, its
  head resting in a wet sheen on the floor.
- 12% to 27% of the width, at 51% to 59% of the height: a yellow folding WET
  FLOOR cone.
- 69% to 97% of the width, at 48% to 60% of the height: a yellow janitor
  cart with two buckets sunk into its lid, a spray bottle hooked on the
  side, a push handle, and a small transistor radio sitting on top with its
  antenna up and two or three little music notes floating away from it.
- 72% to 100%: clean empty floor. Freshly mopped, faintly reflective, a soft
  damp arc where the mop has just passed. Nothing else — no furniture, no
  props, no people.

WHAT IS HAPPENING IN EACH ROOM, left to right:
- LEFT ROOM — a central line going in. Two clinicians lean over a patient
  covered by a blue sterile drape: one is working with concentration, the
  other holds out a small instrument tray. An IV pole stands beside the bed
  with a drip bag hanging. Focused and still — this is the calm one.
- MIDDLE ROOM — a resuscitation in progress. One clinician kneels or stands
  over the patient's chest with both arms locked straight, doing chest
  compressions, their whole upper body driving down. A second clinician at
  the head of the bed squeezes a grey bag-valve mask over the patient's
  face. On the wall behind them a monitor shows a jagged red trace with a
  red alarm light lit. A yellow crash cart stands open at the foot of the
  bed. This room is the loudest thing in the picture.
- RIGHT ROOM — an agitated patient. The patient is sitting halfway up in
  bed, one arm thrown out mid-swing, face contorted, bedding tangled. Two
  clinicians, one on each side, lean in holding an arm each, braced against
  the pull. A soft wrist restraint dangles unused from the bed rail.

NO TEXT anywhere except the small UCI wall sign. No speech bubbles, no
sound effects, no labels, no numbers on the monitors, no logos.

COLOR: one single cool hospital palette — pale blue-grey walls and floor
(#dfe7ea and #e4ecef), teal for the glass frames and the scrubs (#4a8a96),
the auxiliary's tunic in lime green (#a9c25d) and his cart in warm yellow
(#e8b73c), and ONE spot of muted red on the monitor alarm in the middle
room. Everything else stays in that family. Bright, clean, calm daylight —
the drama is in what people are doing, not in the lighting.

FORMAT: tall vertical, aspect ratio 9:19.5 (1080 x 2340 px).
```

## Si además la quieres animada

La animación necesita que las piezas que se mueven sean **capas aparte**: si
la portada es una sola imagen plana, el auxiliar no puede bailar. La forma
barata de conseguirlo es pedir **una segunda imagen en la misma sesión**:

```
Same corridor, same style, same palette, same camera, same everything —
but completely empty. No people at all: no cleaning auxiliary, no
clinicians, no patients. The three rooms have their beds made and empty,
their monitors dark. The janitor cart and the wet floor cone stay where
they are. The floor is clean and unmarked.
```

Con las dos imágenes se recortan las figuras de la primera y el hueco que
dejan se rellena con la segunda: quedan cinco capas —fondo, auxiliar, y un
grupo por sala— y cada una se anima por su cuenta con las mismas veinte
líneas de CSS del mockup. El recorte no es a mano: el arte es plano y de
contorno limpio, que es justo el caso que resuelve `tools/recortar_logo.py`.

Si prefieres saltarte eso, la portada estática también sirve: el movimiento
se queda en las notas musicales y el parpadeo de la alarma, que se dibujan
por encima en SVG y no dependen de la ilustración.

## Cuando llegue

Va a `arte/portada/` como `dibujo.png` (y `dibujo-vacio.png` si generas la
segunda). El generador ya prefiere el dibujo al clip de video, así que entra
sola. Las medidas de arriba salen del vector que está en pantalla, así que
debería calzar sin tocar CSS — y si algo baila un par de píxeles, se corrige
en el recorte y no en el prompt.
