# Prompts de portada — pantalla de inicio

Tres escenas para la pantalla de inicio de *¡Vaya Turno!*. Comparten el
estilo de la casa (el mismo de las 115 cartas, `PROMPTS-ARTE.md`) y una
regla de encuadre propia: **la acción vive en el 55% de arriba y el 40%
de abajo queda vacío a propósito**, porque ahí van el logo y los botones
del menú.

Formato: **3:4 vertical** (o 9:16 si Flow lo ofrece — calza exacto con la
pantalla del teléfono). Nunca cuadrado, nunca horizontal.

---

## Bloque común — pégalo al principio de los tres

```
Modern flat-vector cartoon illustration in the style of a contemporary
animated TV series. Clean digital finish: smooth flat color fills with soft
two-step cel shading plus gentle airbrushed gradients. No visible brush
texture, no grain, no photorealism.
LINE: medium-weight outline in desaturated dark brown or deep teal, never
pure black; even and confident, slightly tapered at the ends. Interior
detail lines noticeably thinner than the silhouette.
CHARACTERS: adult naturalistic proportions with a slightly enlarged head
(about 5 to 6 heads tall). Large round eyes with clear white sclera and dark
irises; thick expressive eyebrows doing most of the acting; simple mouths.
Chilean public-hospital cast: varied ages, builds and skin tones. Ordinary
hospital clothing: teal or navy scrubs, white coats, lanyards.
LIGHT: soft ambient light, gentle falloff, no hard shadows, no rim light,
no lens flare.
TONE: affectionate workplace comedy — competent people, warm humour, never
cruel and never grim.
TITLE-SCREEN LAYOUT (important): portrait 3:4. All the action, the figures
and the identifying architecture sit in the UPPER 55% of the frame. The
LOWER 40% is deliberately empty and quiet — bare floor or bare asphalt,
no figures, no props, no detail — because the game's logo and menu buttons
are drawn on top of it. Keep that lower area even in tone so text stays
readable over it. Nothing important touches any edge.
AVOID: photorealism, watercolor, painterly texture, thick black comic-book
inking, chibi or super-deformed proportions, neon or rainbow palettes, real
brand logos, and readable text of any kind.
```

---

## A · La calma antes del turno  🥇 recomendada

Es la que mejor dice de qué se trata el juego: gente competente, veinte
minutos antes de que empiece todo.

```
SCENE: the corridor of a hospital intensive-care unit, twenty minutes before
the shift starts. In the foreground, seen from behind at a three-quarter
angle, a cleaning auxiliary in a lime-green work uniform and rubber clogs
slowly mops the polished floor — shoulders relaxed, one earphone in, plainly
humming along to something. A small transistor radio and a spray bottle ride
on the yellow janitor cart; a folded yellow WET FLOOR cone stands alongside.
The damp floor holds a soft mirror reflection of the ceiling lights. Behind,
the corridor opens onto three glass-walled ICU rooms: beds freshly made with
the sheets still creased flat, monitors dark, ventilators parked and idle,
one IV pole standing alone. Far down the corridor, three tiny background
figures get ready without hurry — one stocking a supply cart, one writing on
a magnetic whiteboard, one carrying two coffees. A window at the far end
lets in low early-morning light.
MOOD: peaceful, unhurried, almost tender. Nobody is tired and nobody is
worried — this is the last quiet moment of the day.
COLOR: one dominant hue of clean pale hospital celeste-teal across floor,
walls, glass and scrubs, narrow value range, low contrast. Exactly two
accents: the warm cream-gold of the morning light at the end of the
corridor, and the single yellow of the janitor cart and cone.
DEPTH: strong one-point perspective down the corridor. The foreground
auxiliary is the one clear silhouette; the rooms behind sit one step lower
in contrast. The empty polished floor in the front is the quiet lower area.
```

**Variante noche** — cambia una línea: `A window at the far end lets in low
early-morning light` → `The corridor is lit only by the low night lighting
and the blue glow of one screen at the nurses' station`, y el acento cálido
pasa a `the amber pool of the single desk lamp at the station`.

---

## B · Las puertas de la UCI

La más gráfica de las tres: las puertas enmarcan el logo casi solas. Ideal
también para abrir el tutorial.

```
SCENE: the double swing doors of an intensive-care unit, seen head-on from
the corridor outside, filling the frame like a portal. Wide institutional
doors with big round porthole windows and scuffed metal kick plates. Warm
light spills through the portholes and through the gap under the doors,
drawing two long glowing strips across the floor. Above the doors, a simple
backlit sign reading only "UCI", and a small red lamp beside it. On the wall
alongside: an alcohol-gel dispenser, a card reader, and a rack of folded
yellow isolation gowns. An empty gurney is parked against the left wall with
a blanket folded on it. Nobody in the shot, or at most one small silhouette
suggested through a porthole. The polished floor reflects the doors faintly.
MOOD: anticipation and quiet gravity — a threshold about to be crossed.
Calm and inviting, never ominous, never horror.
COLOR: one dominant hue of cool hospital teal across doors, walls and floor,
narrow value range. Exactly two accents: the warm amber leaking from the
portholes and from under the doors, and the single red of the lamp.
COMPOSITION: symmetrical and frontal, doors centred and occupying the upper
55% of the frame; the reflective empty floor in front of them is the quiet
lower area.
TEXT: the ONLY letters allowed anywhere in the image are the three
characters "UCI" on the sign. No other writing, no labels, no signage.
```

---

## C · La urgencia desde afuera

La de más energía. Funciona mejor como pantalla de carga, transición de
ronda o imagen de tienda que como fondo de menú — tiene demasiado que mirar.

```
SCENE: the ambulance ramp of a Chilean public hospital's emergency
department, seen from across the driveway at dusk. Two ambulances at the
covered entrance: one has just backed in, rear doors open and roof lights
turning, and two paramedics in high-visibility jackets roll a stretcher down
the ramp; the second is arriving from the right with its headlights on.
Under the canopy, three hospital staff in scrubs come out to receive them —
one holding the sliding door, one pulling on gloves, one already talking to
the crew. A wheelchair and a spare gurney wait to one side. Above the
entrance, a large illuminated red cross. Light rain has just stopped: the
asphalt is wet and mirrors the red and amber lights in long vertical smears.
Behind the hospital, the low silhouette of the building against a dim
evening sky.
MOOD: urgent but professional — momentum and teamwork, everyone knows their
job. Energetic, never panicked. No blood, no visible injuries; the person on
the stretcher is fully covered by a blanket.
COLOR: one dominant hue of deep nocturnal slate-blue across sky, building
and wet asphalt, narrow value range. Exactly two accents: the red of the
emergency lights and the cross, and the warm amber of the canopy lighting.
COMPOSITION: a slight low three-quarter angle so the ambulances read big.
Entrance and figures in the upper 55%; the wet empty asphalt of the driveway
in the foreground is the quiet lower area, carrying only soft reflections.
```

---

## Cómo se monta después

La imagen entra como fondo de `pantallaInicio()` en
`tools/app-plantilla.html`, a sangre completa y con un degradado al color
de papel en el tercio inferior para que el menú se lea. Si el 40% de abajo
sale con detalle igual, se recorta la banda superior y listo — es el mismo
truco que ya usan las cartas.
