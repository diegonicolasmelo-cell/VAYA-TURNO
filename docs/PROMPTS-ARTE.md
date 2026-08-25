# Los prompts del arte, carta por carta

Un prompt **completo y autosuficiente** por carta, listo para pegar en Nano
Banana (Google Flow) tal cual — no hay que armar nada. Cada uno trae el
estilo de la casa ("Retro de Guardia", BRIEF-IA §4.1), el encuadre de su
tipo de carta, su familia de color y la escena personalizada.

**Cómo usarlo:**

1. Copia el bloque de la carta y pégalo entero en el generador.
2. Si Flow acepta imagen de referencia, acompáñalo con una ilustración de
   `arte/raw/` ("match this style") — `C01-diostor.jpg` es el ancla.
3. Guarda el resultado con el **id como nombre de archivo** (`C09.png`,
   `P14.jpg`, `R30.webp`) y mándalo: la app lo integra sola.
4. Pide **2:3 vertical, mínimo 1024×1536**.

La inspiración compositiva es de ilustración de juego de mesa: una
silueta protagonista, UNA acción legible, el sujeto en el tercio central
— la carta se lee a tamaño de pulgar sobre la mesa. Las claves están
dentro de cada prompt; no lo recortes.

**El orden sugerido:** los 22 personajes primero (fijan las caras del
juego), después los 26 pacientes, después recursos, y al final Acciones
y el Sumario.

---

## 1. Personajes — los avatares (22)

Cuerpo entero, pose característica, ~70% del cuadro. **El escenario rota
con cada personaje** — no todos viven en la UCI: la de Abastecimiento
está en su bodega, el Dirigente afuera del hospital. El añadido extra de
cada uno trae la micro-acción para el **retrato vivo** (pide las
variantes como image-to-image sobre la imagen final: *"same exact image,
eyes closed"* y *"same exact image, <micro-acción>"*).

### C01 · El Diostor

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
CHARACTER PORTRAIT: full body, signature pose, filling about 70% of the frame. This is an archetype portrait — draw the personality, not the uniform.
AMBIENT COLOR FAMILY: neutral hospital teal (#4a8a96) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: hospital corridor as his personal catwalk: smug senior attending, immaculate flowing coat, arms open in a blameless shrug, a faint saint-like halo; a junior trails behind carrying his paperwork.
```

- **Descripción:** 1×RONDA — Cuando colocas una carta ⚠️, puedes descartar 2 cartas de tu mano para pasarle su complicación al jugador de tu derecha: la resuelve él sobre sus pacientes, como si la hubiera jugado. El recurso se queda igual sobre tu paciente.
- **Frase de la carta:** «¿Yo, equivocarme? Imposible. Debe ser un error del laboratorio.»
- **Añadido extra:** Retrato vivo: variante 1 «same exact image, eyes closed»; variante 2 «same exact image, se ajusta la solapa y se mira en el reflejo del vidrio» (tradúcela al inglés al pedirla). Manda las 3 como C01.png, C01-b.png y C01-c.png.

### C02 · El Médico Fantasma

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
CHARACTER PORTRAIT: full body, signature pose, filling about 70% of the frame. This is an archetype portrait — draw the personality, not the uniform.
AMBIENT COLOR FAMILY: nocturnal dark hospital teal (#2e5a63) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: the night door of the on-call residence: a half-translucent doctor with coffee slipping backwards out of frame, ghostly motion trail, his pager glowing and ringing unanswered on the desk.
```

- **Descripción:** PASIVA — En la ronda 1 robas 1 carta menos (el fantasma aún no llega). Desde la ronda 4 en adelante, robas 1 carta adicional cada turno por el resto de la guardia.
- **Frase de la carta:** «Aló... sí, voy bajando. (Se da media vuelta en la residencia.)»
- **Añadido extra:** Retrato vivo: variante 1 «same exact image, eyes closed»; variante 2 «same exact image, mira el celular, se da media vuelta y se desvanece un poco más» (tradúcela al inglés al pedirla). Manda las 3 como C02.png, C02-b.png y C02-c.png.

### C03 · Doctor Amor

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
CHARACTER PORTRAIT: full body, signature pose, filling about 70% of the frame. This is an archetype portrait — draw the personality, not the uniform.
AMBIENT COLOR FAMILY: neutral hospital teal (#4a8a96) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: ward corridor at golden lamp light: telenovela-handsome doctor leaning on an IV pole like a lamppost, winking, a rose in the coat pocket, tiny sparkles; the ECG behind draws a heart.
```

- **Descripción:** 1×PARTIDA — SEDUCCIÓN DE PASILLO — Roba un recurso 🧑‍⚕️ Personal colocado sobre un paciente rival y añádelo a tu mano. Colocarlo después cuesta su indicación, como cualquier carta.
- **Frase de la carta:** «Tus ojos brillan más que este laringoscopio. ¿Un café de máquina?»
- **Añadido extra:** Retrato vivo: variante 1 «same exact image, eyes closed»; variante 2 «same exact image, guiña un ojo y aparece la rosa» (tradúcela al inglés al pedirla). Manda las 3 como C03.png, C03-b.png y C03-c.png.

### C04 · El Director del Hospital

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
CHARACTER PORTRAIT: full body, signature pose, filling about 70% of the frame. This is an archetype portrait — draw the personality, not the uniform.
AMBIENT COLOR FAMILY: neutral hospital teal (#4a8a96) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: top-floor office overlooking the hospital through glass: suited director with hospital badge, phone at the ear, one hand feeding a report into a shredder, political smile, golf trophy on the shelf.
```

- **Descripción:** 1×PARTIDA · PASIVA — PERDONAZO ADMINISTRATIVO (1×PARTIDA) — Anula y descarta un Sumario Administrativo, tuyo o de cualquier otro jugador. Puedes cobrar el favor. BUROCRACIA AMIGA (PASIVA) — Cerrar tus Sumarios te cuesta 1 carta en vez de 2.
- **Frase de la carta:** «Haré unas llamadas para que esto no aparezca en los indicadores de calidad.»
- **Añadido extra:** Retrato vivo: variante 1 «same exact image, eyes closed»; variante 2 «same exact image, saca un papel del bolsillo, lo mira y lo guarda» (tradúcela al inglés al pedirla). Manda las 3 como C04.png, C04-b.png y C04-c.png.

### C05 · La Gestora de Camas

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
CHARACTER PORTRAIT: full body, signature pose, filling about 70% of the frame. This is an archetype portrait — draw the personality, not the uniform.
AMBIENT COLOR FAMILY: neutral hospital teal (#4a8a96) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: the bed-management whiteboard as a war room: sharp woman with radio in hand moving bed magnets like chess pieces; behind her, a stretcher waits with a suitcase on it.
```

- **Descripción:** 1×PARTIDA — DERIVACIÓN — Devuelve un paciente tuyo al fondo del Mazo de Pacientes (sus recursos se descartan) y admite uno nuevo de inmediato. No cuenta como fallecido: no pones ✝️ ni restas sus puntos. Pero el papeleo es el mismo: toma un Sumario Administrativo, y esta guardia ya no puede cobrar ningún bonus de cierre.
- **Frase de la carta:** «No hay cama en UCI. Se va a Intermedio... o a pasillo.»
- **Añadido extra:** Retrato vivo: variante 1 «same exact image, eyes closed»; variante 2 «same exact image, mueve un imán de cama de una columna a otra» (tradúcela al inglés al pedirla). Manda las 3 como C05.png, C05-b.png y C05-c.png.

### C06 · El Médico Esotérico

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
CHARACTER PORTRAIT: full body, signature pose, filling about 70% of the frame. This is an archetype portrait — draw the personality, not the uniform.
AMBIENT COLOR FAMILY: nocturnal dark hospital teal (#2e5a63) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: a dim on-call room turned ritual den: doctor with amulets and crystals over the scrubs, sage smoke curling, lab results spread like tarot cards around a candle.
```

- **Descripción:** 2×PARTIDA — CONFÍA EN EL UNIVERSO — Descarta 1 carta de tu mano como ofrenda, luego revela la primera carta del Mazo de Guardia. Si es un recurso sin ⚠️: colócalo gratis sobre un paciente tuyo. Si trae ⚠️: colócalo gratis igual y resuelve su complicación.
- **Frase de la carta:** «Tus chakras están bloqueando la vía venosa. Cuarzo rosa y sahumerio, stat.»
- **Añadido extra:** Retrato vivo: variante 1 «same exact image, eyes closed»; variante 2 «same exact image, sopla el humo del sahumerio hacia la cámara» (tradúcela al inglés al pedirla). Manda las 3 como C06.png, C06-b.png y C06-c.png.

### C07 · La Enfermera de Noche

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
CHARACTER PORTRAIT: full body, signature pose, filling about 70% of the frame. This is an archetype portrait — draw the personality, not the uniform.
AMBIENT COLOR FAMILY: nocturnal dark hospital teal (#2e5a63) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: the dark ward under one pool of lamplight: serene night nurse sitting guard with a thermos, finger to her lips in a shh; the alarm bells behind her wrapped in gauze.
```

- **Descripción:** 1×PARTIDA — TURNO TRANQUILO — Descarta 3 cartas de tu mano y elige 1 paciente de tu unidad: en este Fin de Guardia, ese paciente no pierde ❤️.
- **Frase de la carta:** «Duerman tranquilos. Yo me quedo con las alarmas.»
- **Añadido extra:** Retrato vivo: variante 1 «same exact image, eyes closed»; variante 2 «same exact image, se lleva el dedo a los labios (shh)» (tradúcela al inglés al pedirla). Manda las 3 como C07.png, C07-b.png y C07-c.png.

### C08 · El Jefe de Servicio

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
CHARACTER PORTRAIT: full body, signature pose, filling about 70% of the frame. This is an archetype portrait — draw the personality, not the uniform.
AMBIENT COLOR FAMILY: neutral hospital teal (#4a8a96) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: hospital corridor photo-op: gray-haired chief posing with a thumbs up for a framed picture, camera flash frozen; behind him the exhausted team does the actual work.
```

- **Descripción:** 1×PARTIDA — FOTO PARA LA MEMORIA — Cuando das tu primera alta ✅ de la guardia, roba 1 carta.
- **Frase de la carta:** «Excelente trabajo, equipo. Lo presento yo en la reunión.»
- **Añadido extra:** Retrato vivo: variante 1 «same exact image, eyes closed»; variante 2 «same exact image, pose de foto y flash» (tradúcela al inglés al pedirla). Manda las 3 como C08.png, C08-b.png y C08-c.png.

### C09 · La de Abastecimiento

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
CHARACTER PORTRAIT: full body, signature pose, filling about 70% of the frame. This is an archetype portrait — draw the personality, not the uniform.
AMBIENT COLOR FAMILY: neutral hospital teal (#4a8a96) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: the supply warehouse aisle: supply queen among tall shelves of labeled boxes, walkie-talkie on her belt, SAFETY BOOTS, hi-vis vest over the uniform, checking inventory on a clipboard with a pen chained to it, one finger counting boxes.
```

- **Descripción:** PASIVA — BODEGA LLENA — Tus Canjes cuestan 1 recurso en vez de 2.
- **Frase de la carta:** «Firma acá, acá y acá. Y me devuelves el lápiz.»
- **Añadido extra:** Retrato vivo: variante 1 «same exact image, eyes closed»; variante 2 «same exact image, marca una casilla del inventario con el lápiz encadenado» (tradúcela al inglés al pedirla). Manda las 3 como C09.png, C09-b.png y C09-c.png.

### C10 · El Dirigente Gremial

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
CHARACTER PORTRAIT: full body, signature pose, filling about 70% of the frame. This is an archetype portrait — draw the personality, not the uniform.
AMBIENT COLOR FAMILY: neutral hospital teal (#4a8a96) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: OUTSIDE the hospital entrance in open daylight: union leader with sash and megaphone, fist raised high, a stack of petitions under the arm, a protest banner strung between two poles behind, coworkers with little flags.
```

- **Descripción:** PASIVA — ASAMBLEA EXTRAORDINARIA — Cada vez que una Acción de ATAQUE rival te elige a ti o a un paciente de tu unidad, roba 1 carta.
- **Frase de la carta:** «Compañeros, esto no se va a quedar así.»
- **Añadido extra:** Retrato vivo: variante 1 «same exact image, eyes closed»; variante 2 «same exact image, alza el megáfono y el puño un poco más» (tradúcela al inglés al pedirla). Manda las 3 como C10.png, C10-b.png y C10-c.png.

### C11 · El Subespecialista

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
CHARACTER PORTRAIT: full body, signature pose, filling about 70% of the frame. This is an archetype portrait — draw the personality, not the uniform.
AMBIENT COLOR FAMILY: neutral hospital teal (#4a8a96) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: a quiet consult office with a diploma wall: elegant subspecialist examining one single ECG strip through a magnifying glass, unhurried, one eyebrow raised; a four-day-old interconsult form waits in the inbox tray.
```

- **Descripción:** 1×PARTIDA — SUGIERO EVALUAR — Gasta 1 indicación y deja 1 recurso de tu mano boca abajo sobre esta carta. Al inicio de tu próximo Pase de Visita colócalo gratis sobre un paciente tuyo y cuenta doble (si no doblaba ya).
- **Frase de la carta:** «Respondió al cuarto día. Pero qué respuesta.»
- **Añadido extra:** Retrato vivo: variante 1 «same exact image, eyes closed»; variante 2 «same exact image, baja la lupa y asiente, lento» (tradúcela al inglés al pedirla). Manda las 3 como C11.png, C11-b.png y C11-c.png.

### C12 · La Enfermera de IAAS

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
CHARACTER PORTRAIT: full body, signature pose, filling about 70% of the frame. This is an archetype portrait — draw the personality, not the uniform.
AMBIENT COLOR FAMILY: neutral hospital teal (#4a8a96) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: a corridor checkpoint: infection-control nurse in impeccable PPE holding a giant folded spreadsheet printout cascading to the floor, pointing at a hand-hygiene poster; an alcohol-gel spray holstered like a sheriff.
```

- **Descripción:** PASIVA — VIGILANCIA EPIDEMIOLÓGICA — Cada 3 complicaciones ⚠️ que se resuelvan en tu unidad, roba 1 Protocolo gratis.
- **Frase de la carta:** «No es magia. Es una planilla Excel con 14 pestañas.»
- **Añadido extra:** Retrato vivo: variante 1 «same exact image, eyes closed»; variante 2 «same exact image, rocía alcohol gel al aire» (tradúcela al inglés al pedirla). Manda las 3 como C12.png, C12-b.png y C12-c.png.

### C13 · El Residente Aplicado

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
CHARACTER PORTRAIT: full body, signature pose, filling about 70% of the frame. This is an archetype portrait — draw the personality, not the uniform.
AMBIENT COLOR FAMILY: neutral hospital teal (#4a8a96) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: the on-call study desk at dawn: young resident with heroic dark circles, a tower of highlighted textbooks, three coffee cups, pens lined in the pocket, eager overachiever smile.
```

- **Descripción:** PASIVA — PACIENTE EMBLEMA — Si en un mismo turno colocas 3 recursos de tipos distintos sobre un mismo paciente, el 3º cuenta doble (si no doblaba ya).
- **Frase de la carta:** «Me lo estudié anoche. Entero. Dos veces.»
- **Añadido extra:** Retrato vivo: variante 1 «same exact image, eyes closed»; variante 2 «same exact image, pasa una página y subraya» (tradúcela al inglés al pedirla). Manda las 3 como C13.png, C13-b.png y C13-c.png.

### C14 · El Reanimador

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
CHARACTER PORTRAIT: full body, signature pose, filling about 70% of the frame. This is an archetype portrait — draw the personality, not the uniform.
AMBIENT COLOR FAMILY: neutral hospital teal (#4a8a96) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: bedside mid-code, lit from below by the monitor: intense doctor with defibrillator paddles raised and charging, absolute NOT TODAY determination; a nurse hands adrenaline from the side.
```

- **Descripción:** 1×PARTIDA — MASAJE Y ADRENALINA — Cuando un paciente tuyo fuera a fallecer, no muere: queda con 1 ❤️ y pierde todos sus recursos colocados.
- **Frase de la carta:** «No se me va. Hoy no. Carguen a 200.»
- **Añadido extra:** Retrato vivo: variante 1 «same exact image, eyes closed»; variante 2 «same exact image, frota las paletas entre sí» (tradúcela al inglés al pedirla). Manda las 3 como C14.png, C14-b.png y C14-c.png.

### C15 · El Dador de Altas

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
CHARACTER PORTRAIT: full body, signature pose, filling about 70% of the frame. This is an archetype portrait — draw the personality, not the uniform.
AMBIENT COLOR FAMILY: neutral hospital teal (#4a8a96) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: the ward exit door: doctor stamping discharge papers in a motion blur of triple stamps, a half-dressed patient already being wheeled out; behind, the empty bed is being remade at speed.
```

- **Descripción:** 1×PARTIDA — ALTA ADMINISTRATIVA — Descarta 2 cartas de tu mano: un paciente tuyo al que le falte exactamente 1 recurso completa sus requisitos (queda ✅ y consolida normal).
- **Frase de la carta:** «Se va hoy. La cama la necesito para las tres.»
- **Añadido extra:** Retrato vivo: variante 1 «same exact image, eyes closed»; variante 2 «same exact image, timbra un papel más» (tradúcela al inglés al pedirla). Manda las 3 como C15.png, C15-b.png y C15-c.png.

### C16 · El Radiólogo de Guardia

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
CHARACTER PORTRAIT: full body, signature pose, filling about 70% of the frame. This is an archetype portrait — draw the personality, not the uniform.
AMBIENT COLOR FAMILY: nocturnal dark hospital teal (#2e5a63) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: the dark reading room lit only by lightbox glow: radiologist holding a film up close, intrigued squint, dictaphone in the other hand; a leaning tower of unread studies beside.
```

- **Descripción:** PASIVA — OJO ENTRENADO — Tus recursos 🩻 Imagen con sistema cuentan doble en cualquier paciente tuyo, no solo en los de su sistema.
- **Frase de la carta:** «Interesante. Muy interesante. ¿Qué me dijiste que buscábamos?»
- **Añadido extra:** Retrato vivo: variante 1 «same exact image, eyes closed»; variante 2 «same exact image, gira la placa 90 grados y entrecierra los ojos» (tradúcela al inglés al pedirla). Manda las 3 como C16.png, C16-b.png y C16-c.png.

### C17 · El Multiuso

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
CHARACTER PORTRAIT: full body, signature pose, filling about 70% of the frame. This is an archetype portrait — draw the personality, not the uniform.
AMBIENT COLOR FAMILY: neutral hospital teal (#4a8a96) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: mid-corridor, mid-everything: handyman-orderly with a utility belt mixing wrench, BP cuff, plunger and cables, a monitor under one arm and a mop in the other hand, unbothered.
```

- **Descripción:** PASIVA — EL QUE HACE DE TODO — Empiezas la guardia con 1 Comodín 🃏 adicional en la mano. Tus comodines no pueden ser robados ni descartados por rivales.
- **Frase de la carta:** «Yo cableo el monitor, destapo el baño y de paso tomo la presión.»
- **Añadido extra:** Retrato vivo: variante 1 «same exact image, eyes closed»; variante 2 «same exact image, cambia de herramienta sin mirar» (tradúcela al inglés al pedirla). Manda las 3 como C17.png, C17-b.png y C17-c.png.

### C18 · La de la Buena Muñeca

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
CHARACTER PORTRAIT: full body, signature pose, filling about 70% of the frame. This is an archetype portrait — draw the personality, not the uniform.
AMBIENT COLOR FAMILY: neutral hospital teal (#4a8a96) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: bedside, first try: confident nurse flexing her wrist with a tiny halo on it, syringe with one perfect drop, the patient's arm relieved; a caught butterfly needle drawn like a medal.
```

- **Descripción:** PASIVA — AL PRIMER INTENTO — Al final de tu Entrega de Turno, puedes devolver 1 carta de tu mano al fondo del Mazo de Guardia: mira las 3 primeras cartas del mazo, quédate con 1 y devuelve el resto al fondo.
- **Frase de la carta:** «Vena difícil no existe. Existe poca fe.»
- **Añadido extra:** Retrato vivo: variante 1 «same exact image, eyes closed»; variante 2 «same exact image, gira la muñeca, elegante» (tradúcela al inglés al pedirla). Manda las 3 como C18.png, C18-b.png y C18-c.png.

### C19 · El Intensivista

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
CHARACTER PORTRAIT: full body, signature pose, filling about 70% of the frame. This is an archetype portrait — draw the personality, not the uniform.
AMBIENT COLOR FAMILY: neutral hospital teal (#4a8a96) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: the eye of the storm: dead-calm intensivist sipping coffee while every monitor around flashes and alarms; his face says this is a normal Tuesday.
```

- **Descripción:** PASIVA — A MÍ NO ME ASUSTA — Tus pacientes de Gravedad III y Código ROJO entran a tu unidad con +1 ❤️.
- **Frase de la carta:** «Grave lo veo yo. Esto es un martes normal.»
- **Añadido extra:** Retrato vivo: variante 1 «same exact image, eyes closed»; variante 2 «same exact image, sorbe el café, imperturbable» (tradúcela al inglés al pedirla). Manda las 3 como C19.png, C19-b.png y C19-c.png.

### C20 · El Carroñero de Pasillo

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
CHARACTER PORTRAIT: full body, signature pose, filling about 70% of the frame. This is an archetype portrait — draw the personality, not the uniform.
AMBIENT COLOR FAMILY: nocturnal dark hospital teal (#2e5a63) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: a night corridor corner: lanky figure peeking around the wall, sneaky grin, wheeling an IV pole loaded like a shopping cart with borrowed equipment, eyes locked on an unattended monitor.
```

- **Descripción:** PASIVA — JUSTO PASABA POR AHÍ — Cada vez que un rival pone un ✝️, roba 1 carta al azar de su mano.
- **Frase de la carta:** «Lamento tu pérdida. ¿Vas a ocupar ese monitor?»
- **Añadido extra:** Retrato vivo: variante 1 «same exact image, eyes closed»; variante 2 «same exact image, se asoma y se esconde tras la esquina» (tradúcela al inglés al pedirla). Manda las 3 como C20.png, C20-b.png y C20-c.png.

### C21 · El Precavido

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
CHARACTER PORTRAIT: full body, signature pose, filling about 70% of the frame. This is an archetype portrait — draw the personality, not the uniform.
AMBIENT COLOR FAMILY: neutral hospital teal (#4a8a96) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: the supply-room doorway: doctor opening his coat like a street vendor to reveal contingency folders, spare batteries, masks and a tiny umbrella; behind, a wall calendar with March circled in red and a told-you-so face.
```

- **Descripción:** 1×PARTIDA — POR SI ACASO — Busca en el Mazo de Protocolos una carta RESPUESTA 🛡️, muéstrala y tómala gratis. Baraja el mazo.
- **Frase de la carta:** «Yo esto lo vi venir en marzo. Está en mi correo.»
- **Añadido extra:** Retrato vivo: variante 1 «same exact image, eyes closed»; variante 2 «same exact image, abre y cierra el abrigo» (tradúcela al inglés al pedirla). Manda las 3 como C21.png, C21-b.png y C21-c.png.

### C22 · La Jefa de Unidad

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
CHARACTER PORTRAIT: full body, signature pose, filling about 70% of the frame. This is an archetype portrait — draw the personality, not the uniform.
AMBIENT COLOR FAMILY: neutral hospital teal (#4a8a96) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: the nurses station as a fortress: formidable head nurse, arms crossed, reading glasses on a chain, looking over them straight at the viewer; her staff sheltered behind her and a metrics board of all-green checkmarks.
```

- **Descripción:** PASIVA — CUMPLIMIENTO DE METAS — Los recursos 🧑‍⚕️ de tu unidad no pueden ser descartados por cartas de rivales.
- **Frase de la carta:** «Mi gente no se toca. Las estadísticas tampoco.»
- **Añadido extra:** Retrato vivo: variante 1 «same exact image, eyes closed»; variante 2 «same exact image, baja los lentes y te mira por encima» (tradúcela al inglés al pedirla). Manda las 3 como C22.png, C22-b.png y C22-c.png.

---

## 2. Pacientes (26)

Busto frontal, del pecho a la cabeza, luz suave; el monitor y el
portasueros van detrás, simplificados. El estado clínico lo marca la
gravedad (ya viene descrito dentro de cada prompt). La frase de la carta
es el chiste — y el prompt ya la convirtió en escena.

### P01 · Dolor Torácico Atípico

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
PATIENT PORTRAIT: frontal bust from chest to head, soft frontal light, ICU monitor and IV pole simplified behind.
AMBIENT COLOR FAMILY: burnt orange / brick red (#e0705a) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: middle-aged man clutching his chest with theatrical agony while side-eyeing the hospital bill on his tray table; one eyebrow says the pain moved when the price appeared. Clinical state: awake and sitting up, dramatic or annoyed, at most a nasal cannula, 30-50 years old.
```

- **Descripción:** Gravedad I · 🫀 Cardiológico · ❤️7 · pide 🩻1 💊1 💉1 · alta +2 / fallece -1
- **Frase de la carta:** «Le duele cuando respira, cuando camina y cuando le hablan de la cuenta.»
- **Añadido extra:** El más liviano del mazo: la comedia manda, cero cables.

### P02 · El del Frasco Completo

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
PATIENT PORTRAIT: frontal bust from chest to head, soft frontal light, ICU monitor and IV pole simplified behind.
AMBIENT COLOR FAMILY: olive green (#5cb583) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: patient sitting up with an innocent guilty smile, holding an empty pill bottle upside down; a lone cotton ball missing from the cotton jar beside him. Clinical state: awake and sitting up, dramatic or annoyed, at most a nasal cannula, 30-50 years old.
```

- **Descripción:** Gravedad I · 🧪 Metabólico · ❤️7 · pide 💊2 🧑‍⚕️1 · alta +2 / fallece -1
- **Frase de la carta:** «Se lo tomó todo. Incluido el algodón.»
- **Añadido extra:** El más liviano del mazo: la comedia manda, cero cables.

### P03 · Abandono de Tratamiento

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
PATIENT PORTRAIT: frontal bust from chest to head, soft frontal light, ICU monitor and IV pole simplified behind.
AMBIENT COLOR FAMILY: burnt orange / brick red (#e0705a) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: relaxed man shrugging with total confidence, a dusty unopened pill box with cobwebs on his nightstand, calendar behind showing eight months crossed out. Clinical state: awake and sitting up, dramatic or annoyed, at most a nasal cannula, 30-50 years old.
```

- **Descripción:** Gravedad I · 🫀 Cardiológico · ❤️7 · pide 💊2 💉1 · alta +2 / fallece -1
- **Frase de la carta:** «Se sentía bien, así que dejó las pastillas. Hace ocho meses.»
- **Añadido extra:** El más liviano del mazo: la comedia manda, cero cables.

### P04 · La Caída del Baño

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
PATIENT PORTRAIT: frontal bust from chest to head, soft frontal light, ICU monitor and IV pole simplified behind.
AMBIENT COLOR FAMILY: amber / mustard (#c19a4e) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: bruised patient with an arm sling insisting with a straight face, while the whole scene behind him (wet floor sign, rubber duck) contradicts his story. Clinical state: awake and sitting up, dramatic or annoyed, at most a nasal cannula, 30-50 years old.
```

- **Descripción:** Gravedad I · 🔪 Quirúrgico · ❤️7 · pide 🩻2 🧑‍⚕️1 · alta +2 / fallece -1
- **Frase de la carta:** «'Me resbalé', dice. Nadie en la sala le cree.»
- **Añadido extra:** El más liviano del mazo: la comedia manda, cero cables.

### P05 · Crisis de Pánico en Box 4

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
PATIENT PORTRAIT: frontal bust from chest to head, soft frontal light, ICU monitor and IV pole simplified behind.
AMBIENT COLOR FAMILY: dark lavender purple (#a184c9) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: hyperventilating woman gripping the bed rails with catastrophic eyes, monitor behind showing a perfectly normal rhythm; a wall calendar with every Tuesday circled. Clinical state: awake and sitting up, dramatic or annoyed, at most a nasal cannula, 30-50 years old.
```

- **Descripción:** Gravedad I · 🧠 Neurológico · ❤️7 · pide 💊1 🧑‍⚕️2 · alta +2 / fallece -1
- **Frase de la carta:** «Se está muriendo. Todos los martes.»
- **Añadido extra:** El más liviano del mazo: la comedia manda, cero cables.

### P06 · Deshidratado de Verano

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
PATIENT PORTRAIT: frontal bust from chest to head, soft frontal light, ICU monitor and IV pole simplified behind.
AMBIENT COLOR FAMILY: olive green (#5cb583) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: sunburnt young man with cracked lips holding up four fingers proudly, empty beer cans arranged like a trophy on the tray, IV line already running. Clinical state: awake and sitting up, dramatic or annoyed, at most a nasal cannula, 30-50 years old.
```

- **Descripción:** Gravedad I · 🧪 Metabólico · ❤️7 · pide 💊1 🧑‍⚕️1 💉1 · alta +2 / fallece -1
- **Frase de la carta:** «Insiste en que cuatro cervezas cuentan como líquido.»
- **Añadido extra:** El más liviano del mazo: la comedia manda, cero cables.

### P07 · El Que Googleó Sus Síntomas

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
PATIENT PORTRAIT: frontal bust from chest to head, soft frontal light, ICU monitor and IV pole simplified behind.
AMBIENT COLOR FAMILY: dark lavender purple (#a184c9) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: smug patient in bed holding out a thick printed stack titled with a diagnosis, treatment plan bookmarked, the doctor's clipboard hanging defeated at the bedside. Clinical state: awake and sitting up, dramatic or annoyed, at most a nasal cannula, 30-50 years old.
```

- **Descripción:** Gravedad I · 🧠 Neurológico · ❤️7 · pide 🩻1 💊1 🧑‍⚕️1 · alta +2 / fallece -1
- **Frase de la carta:** «Trae impreso el diagnóstico. Y el tratamiento. Y el pronóstico.»
- **Añadido extra:** El más liviano del mazo: la comedia manda, cero cables.

### P08 · Postoperado Que No Debería Estar Aquí

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
PATIENT PORTRAIT: frontal bust from chest to head, soft frontal light, ICU monitor and IV pole simplified behind.
AMBIENT COLOR FAMILY: amber / mustard (#c19a4e) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: post-op patient camped in the bed with personal slippers, a plant and three days of newspapers; surgical drain still attached, roots almost growing. Clinical state: awake and sitting up, dramatic or annoyed, at most a nasal cannula, 30-50 years old.
```

- **Descripción:** Gravedad I · 🔪 Quirúrgico · ❤️7 · pide 🩻1 🧑‍⚕️1 💉1 · alta +2 / fallece -1
- **Frase de la carta:** «El cirujano dijo 'obsérvenlo un rato'. Van tres días.»
- **Añadido extra:** El más liviano del mazo: la comedia manda, cero cables.

### P09 · Neumonía Adquirida en la Comunidad

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
PATIENT PORTRAIT: frontal bust from chest to head, soft frontal light, ICU monitor and IV pole simplified behind.
AMBIENT COLOR FAMILY: hospital teal-blue (#5b9dc4) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: gray-faced man mid-cough with a Venturi mask lifted to talk, one month of crumpled tissue packets on the blanket, dark rings of a sleepless month. Clinical state: drowsy, Venturi mask or oxygen, monitor visible behind, 40-70 years old.
```

- **Descripción:** Gravedad II · 🫁 Respiratorio · ❤️6 · pide 🩻1 💊2 🧑‍⚕️1 💉1 · alta +3 / fallece -2
- **Frase de la carta:** «Lleva un mes tosiendo. Vino hoy porque no lo dejaba dormir.»
- **Añadido extra:** Punto medio: enfermo de verdad, humor intacto.

### P10 · Cetoacidosis Diabética

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
PATIENT PORTRAIT: frontal bust from chest to head, soft frontal light, ICU monitor and IV pole simplified behind.
AMBIENT COLOR FAMILY: olive green (#5cb583) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: young woman breathing deep and fast (Kussmaul), empty insulin pen on the nightstand, calendar showing Thursday to Sunday crossed out, sweet fruity breath drawn as tiny wavy lines. Clinical state: drowsy, Venturi mask or oxygen, monitor visible behind, 40-70 years old.
```

- **Descripción:** Gravedad II · 🧪 Metabólico · ❤️6 · pide 💊2 🧑‍⚕️1 💉2 · alta +3 / fallece -2
- **Frase de la carta:** «Se le acabó la insulina el jueves. Hoy es domingo.»
- **Añadido extra:** Punto medio: enfermo de verdad, humor intacto.

### P11 · ACV en Ventana

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
PATIENT PORTRAIT: frontal bust from chest to head, soft frontal light, ICU monitor and IV pole simplified behind.
AMBIENT COLOR FAMILY: dark lavender purple (#a184c9) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: elderly patient with one side of the face drooping, a wall clock behind with a giant question mark on it, family silhouettes shrugging at the door. Clinical state: drowsy, Venturi mask or oxygen, monitor visible behind, 40-70 years old.
```

- **Descripción:** Gravedad II · 🧠 Neurológico · ❤️6 · pide 🩻2 💊1 🧑‍⚕️1 💉1 · alta +3 / fallece -2
- **Frase de la carta:** «Nadie sabe a qué hora empezó. Nadie.»
- **Añadido extra:** Punto medio: enfermo de verdad, humor intacto.

### P12 · Hemorragia Digestiva Alta

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
PATIENT PORTRAIT: frontal bust from chest to head, soft frontal light, ICU monitor and IV pole simplified behind.
AMBIENT COLOR FAMILY: amber / mustard (#c19a4e) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: pale patient with a knowing look away from the doctor, six little tally marks scratched on the bed rail, a basin discreetly at hand. Clinical state: drowsy, Venturi mask or oxygen, monitor visible behind, 40-70 years old.
```

- **Descripción:** Gravedad II · 🔪 Quirúrgico · ❤️6 · pide 🩻1 💊2 💉2 · alta +3 / fallece -2
- **Frase de la carta:** «Dice que es la primera vez. Es la sexta.»
- **Añadido extra:** Punto medio: enfermo de verdad, humor intacto.

### P13 · Insuficiencia Cardíaca Descompensada

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
PATIENT PORTRAIT: frontal bust from chest to head, soft frontal light, ICU monitor and IV pole simplified behind.
AMBIENT COLOR FAMILY: burnt orange / brick red (#e0705a) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: grandfather with swollen ankles propped up, oxygen on, surrounded by the loving evidence: a thermos of cazuela, soup cup, juice box and a dessert plate on the tray. Clinical state: drowsy, Venturi mask or oxygen, monitor visible behind, 40-70 years old.
```

- **Descripción:** Gravedad II · 🫀 Cardiológico · ❤️6 · pide 🩻1 💊2 🧑‍⚕️1 💉1 · alta +3 / fallece -2
- **Frase de la carta:** «Comió cazuela. Y sopa. Y jugo. Y postre.»
- **Añadido extra:** Punto medio: enfermo de verdad, humor intacto.

### P14 · Pielonefritis Complicada

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
PATIENT PORTRAIT: frontal bust from chest to head, soft frontal light, ICU monitor and IV pole simplified behind.
AMBIENT COLOR FAMILY: olive green (#5cb583) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: exhausted woman in work uniform still holding her lanyard, fever flush on the cheeks, an IV starting; her phone buzzing with work messages on the tray. Clinical state: drowsy, Venturi mask or oxygen, monitor visible behind, 40-70 years old.
```

- **Descripción:** Gravedad II · 🧪 Metabólico · ❤️6 · pide 🩻1 💊2 🧑‍⚕️1 💉1 · alta +3 / fallece -2
- **Frase de la carta:** «Aguantó dos semanas por no faltar al trabajo.»
- **Añadido extra:** Punto medio: enfermo de verdad, humor intacto.

### P15 · Abdomen Agudo Sin Diagnóstico

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
PATIENT PORTRAIT: frontal bust from chest to head, soft frontal light, ICU monitor and IV pole simplified behind.
AMBIENT COLOR FAMILY: amber / mustard (#c19a4e) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: patient with hands on the belly, in a tug-of-war of pointing arrows: a surgical cap silhouette points left, a stethoscope silhouette points right; he belongs to no one. Clinical state: drowsy, Venturi mask or oxygen, monitor visible behind, 40-70 years old.
```

- **Descripción:** Gravedad II · 🔪 Quirúrgico · ❤️6 · pide 🩻3 💊1 🧑‍⚕️1 · alta +3 / fallece -2
- **Frase de la carta:** «Cirugía dice que es de medicina. Medicina dice que es de cirugía.»
- **Añadido extra:** Punto medio: enfermo de verdad, humor intacto.

### P16 · EPOC Exacerbado

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
PATIENT PORTRAIT: frontal bust from chest to head, soft frontal light, ICU monitor and IV pole simplified behind.
AMBIENT COLOR FAMILY: hospital teal-blue (#5b9dc4) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: wiry old man with a Venturi mask, his oxygen tank on one side of the bed and his cigarette pack peeking from the robe pocket on the other; both drawn as loyal pets. Clinical state: drowsy, Venturi mask or oxygen, monitor visible behind, 40-70 years old.
```

- **Descripción:** Gravedad II · 🫁 Respiratorio · ❤️6 · pide 🩻1 💊2 💉2 · alta +3 / fallece -2
- **Frase de la carta:** «Trae su balón de oxígeno. Y su cajetilla.»
- **Añadido extra:** Punto medio: enfermo de verdad, humor intacto.

### P17 · Intoxicación Mixta

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
PATIENT PORTRAIT: frontal bust from chest to head, soft frontal light, ICU monitor and IV pole simplified behind.
AMBIENT COLOR FAMILY: olive green (#5cb583) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: young man with spiral eyes and a chalkboard of question marks behind, toxicology chart on the wall with everything circled; he shrugs too. Clinical state: drowsy, Venturi mask or oxygen, monitor visible behind, 40-70 years old.
```

- **Descripción:** Gravedad II · 🧪 Metabólico · ❤️6 · pide 💊3 🧑‍⚕️1 💉1 · alta +3 / fallece -2
- **Frase de la carta:** «Nadie sabe qué tomó. Él tampoco.»
- **Añadido extra:** Punto medio: enfermo de verdad, humor intacto.

### P18 · Delirium del Adulto Mayor

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
PATIENT PORTRAIT: frontal bust from chest to head, soft frontal light, ICU monitor and IV pole simplified behind.
AMBIENT COLOR FAMILY: dark lavender purple (#a184c9) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: sweet grandmother asleep like an angel in daylight... with a tiny inset moon showing her conducting an invisible orchestra with the IV pole as baton at night. Clinical state: drowsy, Venturi mask or oxygen, monitor visible behind, 40-70 years old.
```

- **Descripción:** Gravedad II · 🧠 Neurológico · ❤️6 · pide 🩻1 💊1 🧑‍⚕️3 · alta +3 / fallece -2
- **Frase de la carta:** «De día duerme. De noche dirige una orquesta.»
- **Añadido extra:** Punto medio: enfermo de verdad, humor intacto.

### P19 · Shock Séptico

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
PATIENT PORTRAIT: frontal bust from chest to head, soft frontal light, ICU monitor and IV pole simplified behind.
AMBIENT COLOR FAMILY: burnt orange / brick red (#e0705a) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: gravely ill patient, flushed and sweaty, four infusion pumps stacked like a totem beside the bed, a melted golden hourglass on the monitor shelf. Clinical state: intubated, deep sedation, arterial line, the monitor is a protagonist, over 60.
```

- **Descripción:** Gravedad III · 🫀 Cardiológico · ❤️6 · pide 🩻1 💊4 🧑‍⚕️1 💉2 · alta +6 / fallece -2
- **Frase de la carta:** «La hora dorada empezó hace cuatro horas.»
- **Añadido extra:** Aquí el monitor es co-protagonista; el humor se vuelve negro.

### P20 · Politraumatizado

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
PATIENT PORTRAIT: frontal bust from chest to head, soft frontal light, ICU monitor and IV pole simplified behind.
AMBIENT COLOR FAMILY: amber / mustard (#c19a4e) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: young man in cervical collar and full fixation, monitor busy; a tiny speedometer at 120 and an unbuckled seatbelt drawn as ghost icons above. Clinical state: intubated, deep sedation, arterial line, the monitor is a protagonist, over 60.
```

- **Descripción:** Gravedad III · 🔪 Quirúrgico · ❤️6 · pide 🩻3 💊1 🧑‍⚕️1 💉3 · alta +6 / fallece -2
- **Frase de la carta:** «Iba a 120. Sin cinturón. 'Por acá nunca hay control'.»
- **Añadido extra:** Aquí el monitor es co-protagonista; el humor se vuelve negro.

### P21 · Síndrome de Distrés Respiratorio

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
PATIENT PORTRAIT: frontal bust from chest to head, soft frontal light, ICU monitor and IV pole simplified behind.
AMBIENT COLOR FAMILY: hospital teal-blue (#5b9dc4) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: serene intubated patient, almost peaceful, while the chest X-ray on the lightbox behind is a storm of frosted glass; the calm and the storm in one frame. Clinical state: intubated, deep sedation, arterial line, the monitor is a protagonist, over 60.
```

- **Descripción:** Gravedad III · 🫁 Respiratorio · ❤️6 · pide 🩻2 💊2 🧑‍⚕️2 💉2 · alta +6 / fallece -2
- **Frase de la carta:** «Los pulmones parecen vidrio esmerilado. Él parece tranquilo.»
- **Añadido extra:** Aquí el monitor es co-protagonista; el humor se vuelve negro.

### P22 · Status Epiléptico

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
PATIENT PORTRAIT: frontal bust from chest to head, soft frontal light, ICU monitor and IV pole simplified behind.
AMBIENT COLOR FAMILY: dark lavender purple (#a184c9) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: intubated patient with EEG leads, four empty syringes lined up on the cart like spent shells, a tiny lightning bolt still crossing the monitor trace. Clinical state: intubated, deep sedation, arterial line, the monitor is a protagonist, over 60.
```

- **Descripción:** Gravedad III · 🧠 Neurológico · ❤️6 · pide 🩻1 💊4 🧑‍⚕️1 💉2 · alta +6 / fallece -2
- **Frase de la carta:** «Cuarta dosis. Sigue convulsionando.»
- **Añadido extra:** Aquí el monitor es co-protagonista; el humor se vuelve negro.

### P23 · Pancreatitis Grave

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
PATIENT PORTRAIT: frontal bust from chest to head, soft frontal light, ICU monitor and IV pole simplified behind.
AMBIENT COLOR FAMILY: amber / mustard (#c19a4e) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: big man intubated with a distended belly, dreaming (thought bubble) of a single innocent asado skewer with a halo; enzyme numbers towering on the monitor. Clinical state: intubated, deep sedation, arterial line, the monitor is a protagonist, over 60.
```

- **Descripción:** Gravedad III · 🔪 Quirúrgico · ❤️6 · pide 🩻3 💊2 🧑‍⚕️2 💉1 · alta +6 / fallece -2
- **Frase de la carta:** «Fue un asado. Uno solo, insiste.»
- **Añadido extra:** Aquí el monitor es co-protagonista; el humor se vuelve negro.

### P24 · Tromboembolismo Pulmonar Masivo

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
PATIENT PORTRAIT: frontal bust from chest to head, soft frontal light, ICU monitor and IV pole simplified behind.
AMBIENT COLOR FAMILY: hospital teal-blue (#5b9dc4) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: patient on high-flow oxygen gripping the bed, a suitcase with flight stickers still at the bedside, boarding pass on the floor; one leg drawn swollen. Clinical state: intubated, deep sedation, arterial line, the monitor is a protagonist, over 60.
```

- **Descripción:** Gravedad III · 🫁 Respiratorio · ❤️6 · pide 🩻2 💊2 💉4 · alta +6 / fallece -2
- **Frase de la carta:** «Volvió de un vuelo de catorce horas y del baño no salió caminando.»
- **Añadido extra:** Aquí el monitor es co-protagonista; el humor se vuelve negro.

### P25 · Falla Multiorgánica

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
PATIENT PORTRAIT: frontal bust from chest to head, soft frontal light, ICU monitor and IV pole simplified behind.
AMBIENT COLOR FAMILY: burnt orange / brick red (#e0705a) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: the most tangled bed of the deck: ventilator, pumps, lines and drains all at once, each labeled organ waving a tiny white flag in alphabetical order. Clinical state: ventilated, several infusion pumps running, the most extreme scene in the deck.
```

- **Descripción:** Gravedad ROJO · 🫀 Cardiológico · ❤️5 · pide 🩻2 💊3 🧑‍⚕️1 💉2 · alta +8 / fallece -3
- **Frase de la carta:** «Todo mal. Y en orden alfabético.»
- **Añadido extra:** La escena más extrema del mazo — que asuste un poco.

### P26 · Trasplante en Lista Cero

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
PATIENT PORTRAIT: frontal bust from chest to head, soft frontal light, ICU monitor and IV pole simplified behind.
AMBIENT COLOR FAMILY: amber / mustard (#c19a4e) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: patient ready and packed on the stretcher, IV pole as flag mast; through the window a tiny plane circles and the OR doors behind have a CLOSED sign. Clinical state: ventilated, several infusion pumps running, the most extreme scene in the deck.
```

- **Descripción:** Gravedad ROJO · 🔪 Quirúrgico · ❤️5 · pide 🩻2 💊2 🧑‍⚕️2 💉2 · alta +8 / fallece -3
- **Frase de la carta:** «Hay órgano. Hay avión. No hay pabellón.»
- **Añadido extra:** La escena más extrema del mazo — que asuste un poco.

---

## 3. Recursos — el Mazo de Guardia (44 diseños)

El objeto casi aislado, 3/4 o frontal, ~60% del cuadro, sobre fondo
monocromo ambiental (nunca blanco). **Los 🧑‍⚕️ Personal son personas**:
busto o medio cuerpo en su gesto de trabajo. Las parejas (misma carta
limpia y con ⚠️) comparten objeto y encuadre: genera primero la limpia y
pide la complicada como variación de la misma imagen.

### R01 · Antibiótico de Amplio Espectro

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
OBJECT CARD: the object nearly isolated, 3/4 or frontal view, filling about 60% of the frame, on an ambient monochrome hospital background, never white.
AMBIENT COLOR FAMILY: neutral hospital teal (#4a8a96) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: a proud wide-spectrum antibiotic IV bag hanging center stage with a superhero glow, covering the whole scene with its shadow like a protective cape.
```

- **Descripción:** 💊 Fármacos · 2 copia(s)
- **Frase de la carta:** «Cubre todo. Especialmente nuestra falta de diagnóstico.»
- **Añadido extra:** Pareja con R02 — esta es la versión LIMPIA: mismo objeto, mismo encuadre; cambia solo lo que sale mal.

### R02 · Antibiótico de Amplio Espectro

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
OBJECT CARD: the object nearly isolated, 3/4 or frontal view, filling about 60% of the frame, on an ambient monochrome hospital background, never white.
AMBIENT COLOR FAMILY: neutral hospital teal (#4a8a96) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: the same wide-spectrum IV bag, but a tiny army of smug bacteria wearing helmets and carrying microscopic shields marches across the tubing unharmed.
```

- **Descripción:** 💊 Fármacos · ⚠️ Resistencia Antibiótica · 1 copia(s)
- **Frase de la carta:** «Cubre todo. Especialmente nuestra falta de diagnóstico.»
- **Añadido extra:** Pareja con R01 — esta es la versión COMPLICADA: mismo objeto, mismo encuadre; cambia solo lo que sale mal.

### R46 · Sedoanalgesia

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
OBJECT CARD: the object nearly isolated, 3/4 or frontal view, filling about 60% of the frame, on an ambient monochrome hospital background, never white.
AMBIENT COLOR FAMILY: amber / mustard (#c19a4e) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: a sedation syringe pump purring softly, zzz bubbles floating up, a serene sleeping patient silhouette in the background; the whole ward exhales.
```

- **Descripción:** 💊 Fármacos · 🔪 Quirúrgico ×2 · 2 copia(s)
- **Frase de la carta:** «Duerme él. Duerme la unidad. No duermes tú. '¿Del uno al diez?' 'Quince.'»
- **Añadido extra:** Pareja con R47 — esta es la versión LIMPIA: mismo objeto, mismo encuadre; cambia solo lo que sale mal. Lleva chip de sistema: en la app esta carta luce la banda iridiscente al verla en grande.

### R47 · Sedoanalgesia

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
OBJECT CARD: the object nearly isolated, 3/4 or frontal view, filling about 60% of the frame, on an ambient monochrome hospital background, never white.
AMBIENT COLOR FAMILY: amber / mustard (#c19a4e) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: the same syringe pump at night, the zzz bubbles turning into ?! sparks, the patient silhouette behind wide-eyed conducting an invisible orchestra.
```

- **Descripción:** 💊 Fármacos · 🔪 Quirúrgico ×2 · ⚠️ Delirium en UCI · 1 copia(s)
- **Frase de la carta:** «Duerme él. Duerme la unidad. No duermes tú. '¿Del uno al diez?' 'Quince.'»
- **Añadido extra:** Pareja con R46 — esta es la versión COMPLICADA: mismo objeto, mismo encuadre; cambia solo lo que sale mal. Lleva chip de sistema: en la app esta carta luce la banda iridiscente al verla en grande.

### R05 · Anticoagulación

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
OBJECT CARD: the object nearly isolated, 3/4 or frontal view, filling about 60% of the frame, on an ambient monochrome hospital background, never white.
AMBIENT COLOR FAMILY: neutral hospital teal (#4a8a96) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: an anticoagulation vial balanced dead-center on a tiny seesaw, one side a blood drop, the other a clot; both watching each other with suspicion.
```

- **Descripción:** 💊 Fármacos · 1 copia(s)
- **Frase de la carta:** «Si sangra fue mucho. Si coagula fue poco. Nunca fue justo.»
- **Añadido extra:** Pareja con R06 — esta es la versión LIMPIA: mismo objeto, mismo encuadre; cambia solo lo que sale mal.

### R06 · Anticoagulación

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
OBJECT CARD: the object nearly isolated, 3/4 or frontal view, filling about 60% of the frame, on an ambient monochrome hospital background, never white.
AMBIENT COLOR FAMILY: neutral hospital teal (#4a8a96) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: the same vial and seesaw, tipped hard: the blood-drop side flooding, tiny red drips escaping the frame; the balance was never fair.
```

- **Descripción:** 💊 Fármacos · ⚠️ Sangrado · 1 copia(s)
- **Frase de la carta:** «Si sangra fue mucho. Si coagula fue poco. Nunca fue justo.»
- **Añadido extra:** Pareja con R05 — esta es la versión COMPLICADA: mismo objeto, mismo encuadre; cambia solo lo que sale mal.

### R07 · Hemoderivados

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
OBJECT CARD: the object nearly isolated, 3/4 or frontal view, filling about 60% of the frame, on an ambient monochrome hospital background, never white.
AMBIENT COLOR FAMILY: neutral hospital teal (#4a8a96) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: a blood bag arriving in a cooler with a heroic entrance, dramatic light, its paper tag missing — just a torn string where the form should be.
```

- **Descripción:** 💊 Fármacos · 2 copia(s)
- **Frase de la carta:** «Llegaron. Sin la ficha, pero llegaron.»
- **Añadido extra:** Carta única, sin pareja.

### R08 · Noradrenalina

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
OBJECT CARD: the object nearly isolated, 3/4 or frontal view, filling about 60% of the frame, on an ambient monochrome hospital background, never white.
AMBIENT COLOR FAMILY: burnt orange / brick red (#e0705a) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: a noradrenaline syringe pump with a pressure gauge climbing, the needle rising like a thermometer in summer; steady hands hold the frame.
```

- **Descripción:** 💊 Fármacos · 🫀 Cardiológico ×2 · 2 copia(s)
- **Frase de la carta:** «La presión sube. La del paciente y la tuya.»
- **Añadido extra:** Pareja con R09 — esta es la versión LIMPIA: mismo objeto, mismo encuadre; cambia solo lo que sale mal. Lleva chip de sistema: en la app esta carta luce la banda iridiscente al verla en grande.

### R09 · Noradrenalina

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
OBJECT CARD: the object nearly isolated, 3/4 or frontal view, filling about 60% of the frame, on an ambient monochrome hospital background, never white.
AMBIENT COLOR FAMILY: burnt orange / brick red (#e0705a) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: the same pump, gauge needle buried in red, the ECG trace behind gone jagged like a mountain range; everything vibrates slightly.
```

- **Descripción:** 💊 Fármacos · 🫀 Cardiológico ×2 · ⚠️ Taquicardia Ventricular · 1 copia(s)
- **Frase de la carta:** «La presión sube. La del paciente y la tuya.»
- **Añadido extra:** Pareja con R08 — esta es la versión COMPLICADA: mismo objeto, mismo encuadre; cambia solo lo que sale mal. Lleva chip de sistema: en la app esta carta luce la banda iridiscente al verla en grande.

### R10 · Broncodilatador en Nebulización

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
OBJECT CARD: the object nearly isolated, 3/4 or frontal view, filling about 60% of the frame, on an ambient monochrome hospital background, never white.
AMBIENT COLOR FAMILY: hospital teal-blue (#5b9dc4) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: a nebulizer mask puffing majestic clouds of vapor that fill the top of the frame like a spa; a tiny rubber duck silhouette in the mist.
```

- **Descripción:** 💊 Fármacos · 🫁 Respiratorio ×2 · 2 copia(s)
- **Frase de la carta:** «Sale más vapor que del baño turco. Algo tiene que estar llegando.»
- **Añadido extra:** Lleva chip de sistema: en la app esta carta luce la banda iridiscente al verla en grande.

### R13 · Insulina en Bomba

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
OBJECT CARD: the object nearly isolated, 3/4 or frontal view, filling about 60% of the frame, on an ambient monochrome hospital background, never white.
AMBIENT COLOR FAMILY: olive green (#5cb583) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: an insulin pump beside a glucometer, both flanked by a clock face marked every two hours; a stack of used test strips like a tiny card deck.
```

- **Descripción:** 💊 Fármacos · 🧪 Metabólico ×2 · 2 copia(s)
- **Frase de la carta:** «Cada dos horas un hemoglucotest. Cada dos horas.»
- **Añadido extra:** Lleva chip de sistema: en la app esta carta luce la banda iridiscente al verla en grande.

### R48 · Corticoides

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
OBJECT CARD: the object nearly isolated, 3/4 or frontal view, filling about 60% of the frame, on an ambient monochrome hospital background, never white.
AMBIENT COLOR FAMILY: neutral hospital teal (#4a8a96) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: a corticosteroid vial radiating a mighty power aura, flexing its glow; everything around it stands a little straighter.
```

- **Descripción:** 💊 Fármacos · 1 copia(s)
- **Frase de la carta:** «Sirven para todo. Suben el azúcar, el ánimo y la presión.»
- **Añadido extra:** Pareja con R49 — esta es la versión LIMPIA: mismo objeto, mismo encuadre; cambia solo lo que sale mal.

### R49 · Corticoides

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
OBJECT CARD: the object nearly isolated, 3/4 or frontal view, filling about 60% of the frame, on an ambient monochrome hospital background, never white.
AMBIENT COLOR FAMILY: neutral hospital teal (#4a8a96) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: the same vial, but a pyramid of sugar cubes has piled up behind it and the glucometer beside shows a screaming high number with sweat drops.
```

- **Descripción:** 💊 Fármacos · ⚠️ Hiperglicemia · 1 copia(s)
- **Frase de la carta:** «Sirven para todo. Suben el azúcar, el ánimo y la presión.»
- **Añadido extra:** Pareja con R48 — esta es la versión COMPLICADA: mismo objeto, mismo encuadre; cambia solo lo que sale mal.

### R50 · Cristaloides

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
OBJECT CARD: the object nearly isolated, 3/4 or frontal view, filling about 60% of the frame, on an ambient monochrome hospital background, never white.
AMBIENT COLOR FAMILY: neutral hospital teal (#4a8a96) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: a crystal-clear saline bag glinting like a jewel, one perfect drop mid-fall, calm and generous.
```

- **Descripción:** 💊 Fármacos · 1 copia(s)
- **Frase de la carta:** «Agua con sal. La primera respuesta a casi todo.»
- **Añadido extra:** Pareja con R51 — esta es la versión LIMPIA: mismo objeto, mismo encuadre; cambia solo lo que sale mal.

### R51 · Cristaloides

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
OBJECT CARD: the object nearly isolated, 3/4 or frontal view, filling about 60% of the frame, on an ambient monochrome hospital background, never white.
AMBIENT COLOR FAMILY: neutral hospital teal (#4a8a96) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: the same saline bag overflowing, a puddle spreading below, tiny sandbags stacked around the IV pole like flood defense.
```

- **Descripción:** 💊 Fármacos · ⚠️ Sobrecarga de Volumen · 1 copia(s)
- **Frase de la carta:** «Agua con sal. La primera respuesta a casi todo.»
- **Añadido extra:** Pareja con R50 — esta es la versión COMPLICADA: mismo objeto, mismo encuadre; cambia solo lo que sale mal.

### R16 · Radiografía de Tórax

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
OBJECT CARD: the object nearly isolated, 3/4 or frontal view, filling about 60% of the frame, on an ambient monochrome hospital background, never white.
AMBIENT COLOR FAMILY: neutral hospital teal (#4a8a96) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: a chest X-ray film held up to the light — slightly rotated, slightly crooked, clipped anyway; the lightbox hums with routine dignity.
```

- **Descripción:** 🩻 Imagen · 3 copia(s)
- **Frase de la carta:** «Rotada, penetrada y en espiración. Se informa igual.»
- **Añadido extra:** Pareja con R17 — esta es la versión LIMPIA: mismo objeto, mismo encuadre; cambia solo lo que sale mal.

### R17 · Radiografía de Tórax

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
OBJECT CARD: the object nearly isolated, 3/4 or frontal view, filling about 60% of the frame, on an ambient monochrome hospital background, never white.
AMBIENT COLOR FAMILY: neutral hospital teal (#4a8a96) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: the same film with one tiny circled shadow in a corner, three question marks orbiting it; nobody asked for this discovery.
```

- **Descripción:** 🩻 Imagen · ⚠️ Hallazgo Incidental · 1 copia(s)
- **Frase de la carta:** «Rotada, penetrada y en espiración. Se informa igual.»
- **Añadido extra:** Pareja con R16 — esta es la versión COMPLICADA: mismo objeto, mismo encuadre; cambia solo lo que sale mal.

### R18 · Ecografía a Pie de Cama

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
OBJECT CARD: the object nearly isolated, 3/4 or frontal view, filling about 60% of the frame, on an ambient monochrome hospital background, never white.
AMBIENT COLOR FAMILY: neutral hospital teal (#4a8a96) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: a bedside ultrasound machine with a proud gray blob on screen, the probe raised like a sword; conviction without certainty.
```

- **Descripción:** 🩻 Imagen · 3 copia(s)
- **Frase de la carta:** «Veo algo. No sé qué es, pero lo veo.»
- **Añadido extra:** Pareja con R19 — esta es la versión LIMPIA: mismo objeto, mismo encuadre; cambia solo lo que sale mal.

### R19 · Ecografía a Pie de Cama

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
OBJECT CARD: the object nearly isolated, 3/4 or frontal view, filling about 60% of the frame, on an ambient monochrome hospital background, never white.
AMBIENT COLOR FAMILY: neutral hospital teal (#4a8a96) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: the same ultrasound, the blob on screen now suspiciously shaped like a fish, the probe scratching its own cable in doubt.
```

- **Descripción:** 🩻 Imagen · ⚠️ Falso Positivo · 1 copia(s)
- **Frase de la carta:** «Veo algo. No sé qué es, pero lo veo.»
- **Añadido extra:** Pareja con R18 — esta es la versión COMPLICADA: mismo objeto, mismo encuadre; cambia solo lo que sale mal.

### R20 · TAC de Urgencia

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
OBJECT CARD: the object nearly isolated, 3/4 or frontal view, filling about 60% of the frame, on an ambient monochrome hospital background, never white.
AMBIENT COLOR FAMILY: neutral hospital teal (#4a8a96) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: a CT scanner donut glowing at the end of a corridor while a stretcher rolls toward it at full speed, motion lines and a flying chart.
```

- **Descripción:** 🩻 Imagen · 2 copia(s)
- **Frase de la carta:** «El traslado es más peligroso que la enfermedad. Vamos igual.»
- **Añadido extra:** Pareja con R21 — esta es la versión LIMPIA: mismo objeto, mismo encuadre; cambia solo lo que sale mal.

### R21 · TAC de Urgencia

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
OBJECT CARD: the object nearly isolated, 3/4 or frontal view, filling about 60% of the frame, on an ambient monochrome hospital background, never white.
AMBIENT COLOR FAMILY: neutral hospital teal (#4a8a96) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: the same corridor mid-disaster: stretcher drifting a corner, IV pole tipping, papers airborne — the scanner still glowing patiently far away.
```

- **Descripción:** 🩻 Imagen · ⚠️ Incidente en el Traslado · 1 copia(s)
- **Frase de la carta:** «El traslado es más peligroso que la enfermedad. Vamos igual.»
- **Añadido extra:** Pareja con R20 — esta es la versión COMPLICADA: mismo objeto, mismo encuadre; cambia solo lo que sale mal.

### R22 · Angio-TAC

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
OBJECT CARD: the object nearly isolated, 3/4 or frontal view, filling about 60% of the frame, on an ambient monochrome hospital background, never white.
AMBIENT COLOR FAMILY: burnt orange / brick red (#e0705a) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: an angio-CT console showing vessels lit up like a golden subway map, the contrast injector standing by like a rocket booster.
```

- **Descripción:** 🩻 Imagen · 🫀 Cardiológico ×2 · 2 copia(s)
- **Frase de la carta:** «Contraste, creatinina, y una fe enorme.»
- **Añadido extra:** Pareja con R52 — esta es la versión LIMPIA: mismo objeto, mismo encuadre; cambia solo lo que sale mal. Lleva chip de sistema: en la app esta carta luce la banda iridiscente al verla en grande.

### R52 · Angio-TAC

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
OBJECT CARD: the object nearly isolated, 3/4 or frontal view, filling about 60% of the frame, on an ambient monochrome hospital background, never white.
AMBIENT COLOR FAMILY: burnt orange / brick red (#e0705a) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: the same console, but the contrast bottle drips its last drop and a kidney-shaped warning light blinks on the corner of the screen.
```

- **Descripción:** 🩻 Imagen · 🫀 Cardiológico ×2 · ⚠️ Nefropatía por Contraste · 1 copia(s)
- **Frase de la carta:** «Contraste, creatinina, y una fe enorme.»
- **Añadido extra:** Pareja con R22 — esta es la versión COMPLICADA: mismo objeto, mismo encuadre; cambia solo lo que sale mal. Lleva chip de sistema: en la app esta carta luce la banda iridiscente al verla en grande.

### R23 · Resonancia con Cupo

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
OBJECT CARD: the object nearly isolated, 3/4 or frontal view, filling about 60% of the frame, on an ambient monochrome hospital background, never white.
AMBIENT COLOR FAMILY: dark lavender purple (#a184c9) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: an MRI machine glowing like a mythical portal behind a velvet rope, a take-a-number ticket dispenser beside it showing 87.
```

- **Descripción:** 🩻 Imagen · 🧠 Neurológico ×2 · 1 copia(s)
- **Frase de la carta:** «Existe. La han visto. Hay testigos.»
- **Añadido extra:** Lleva chip de sistema: en la app esta carta luce la banda iridiscente al verla en grande.

### R24 · Línea Arterial

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
OBJECT CARD: the object nearly isolated, 3/4 or frontal view, filling about 60% of the frame, on an ambient monochrome hospital background, never white.
AMBIENT COLOR FAMILY: neutral hospital teal (#4a8a96) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: an arterial line finally in place on a wrist, drawn triumphant; behind, a tray discreetly hides four bent needles under a cloth.
```

- **Descripción:** 💉 Procedimientos · 2 copia(s)
- **Frase de la carta:** «Al quinto intento salió. Nadie mencionará los cuatro anteriores.»
- **Añadido extra:** Pareja con R25 — esta es la versión LIMPIA: mismo objeto, mismo encuadre; cambia solo lo que sale mal.

### R25 · Línea Arterial

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
OBJECT CARD: the object nearly isolated, 3/4 or frontal view, filling about 60% of the frame, on an ambient monochrome hospital background, never white.
AMBIENT COLOR FAMILY: neutral hospital teal (#4a8a96) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: the same wrist, the fingertips drawn faintly blue-violet, a tiny alarm bell above; the line itself whistles innocently.
```

- **Descripción:** 💉 Procedimientos · ⚠️ Isquemia Distal · 1 copia(s)
- **Frase de la carta:** «Al quinto intento salió. Nadie mencionará los cuatro anteriores.»
- **Añadido extra:** Pareja con R24 — esta es la versión COMPLICADA: mismo objeto, mismo encuadre; cambia solo lo que sale mal.

### R26 · Catéter Venoso Central

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
OBJECT CARD: the object nearly isolated, 3/4 or frontal view, filling about 60% of the frame, on an ambient monochrome hospital background, never white.
AMBIENT COLOR FAMILY: neutral hospital teal (#4a8a96) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: a central line kit laid out on a sterile field like surgical jewelry, ultrasound at the ready, an audience of small silhouettes at the door.
```

- **Descripción:** 💉 Procedimientos · 3 copia(s)
- **Frase de la carta:** «Ecoguiado, estéril y con público.»
- **Añadido extra:** Pareja con R27 — esta es la versión LIMPIA: mismo objeto, mismo encuadre; cambia solo lo que sale mal.

### R27 · Catéter Venoso Central

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
OBJECT CARD: the object nearly isolated, 3/4 or frontal view, filling about 60% of the frame, on an ambient monochrome hospital background, never white.
AMBIENT COLOR FAMILY: neutral hospital teal (#4a8a96) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: the same kit, but a conga line of tiny green germs with party hats climbs up the catheter; the sterile field pretends not to see.
```

- **Descripción:** 💉 Procedimientos · ⚠️ Bacteriemia por Catéter · 1 copia(s)
- **Frase de la carta:** «Ecoguiado, estéril y con público.»
- **Añadido extra:** Pareja con R26 — esta es la versión COMPLICADA: mismo objeto, mismo encuadre; cambia solo lo que sale mal.

### R30 · Ventilación Mecánica

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
OBJECT CARD: the object nearly isolated, 3/4 or frontal view, filling about 60% of the frame, on an ambient monochrome hospital background, never white.
AMBIENT COLOR FAMILY: neutral hospital teal (#4a8a96) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: a mechanical ventilator with its knobs and screen, connected by tubing drawn as a tug-of-war rope to a small pair of stubborn lungs.
```

- **Descripción:** 💉 Procedimientos · 3 copia(s)
- **Frase de la carta:** «Modo controlado. El paciente y el ventilador aún negocian.»
- **Añadido extra:** Pareja con R31 — esta es la versión LIMPIA: mismo objeto, mismo encuadre; cambia solo lo que sale mal.

### R31 · Ventilación Mecánica

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
OBJECT CARD: the object nearly isolated, 3/4 or frontal view, filling about 60% of the frame, on an ambient monochrome hospital background, never white.
AMBIENT COLOR FAMILY: neutral hospital teal (#4a8a96) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: the same ventilator, tiny germs surfing down the tubing on droplets, the lungs bracing; the machine keeps its dignity.
```

- **Descripción:** 💉 Procedimientos · ⚠️ Neumonía Asociada a VM · 1 copia(s)
- **Frase de la carta:** «Modo controlado. El paciente y el ventilador aún negocian.»
- **Añadido extra:** Pareja con R30 — esta es la versión COMPLICADA: mismo objeto, mismo encuadre; cambia solo lo que sale mal.

### R32 · Gases Arteriales

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
OBJECT CARD: the object nearly isolated, 3/4 or frontal view, filling about 60% of the frame, on an ambient monochrome hospital background, never white.
AMBIENT COLOR FAMILY: olive green (#5cb583) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: an arterial blood gas syringe resting on crushed ice like a delicacy, a pH strip beside reading catastrophic; someone must now say something smart.
```

- **Descripción:** 💉 Procedimientos · 🧪 Metabólico ×2 · 1 copia(s)
- **Frase de la carta:** «pH 7.09. Alguien diga algo inteligente.»
- **Añadido extra:** Pareja con R33 — esta es la versión LIMPIA: mismo objeto, mismo encuadre; cambia solo lo que sale mal. Lleva chip de sistema: en la app esta carta luce la banda iridiscente al verla en grande.

### R33 · Gases Arteriales

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
OBJECT CARD: the object nearly isolated, 3/4 or frontal view, filling about 60% of the frame, on an ambient monochrome hospital background, never white.
AMBIENT COLOR FAMILY: olive green (#5cb583) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: the same syringe shaken like a cocktail — foam, pink froth and a tiny paper umbrella planted on top; the lab will not be amused.
```

- **Descripción:** 💉 Procedimientos · 🧪 Metabólico ×2 · ⚠️ Muestra Hemolizada · 1 copia(s)
- **Frase de la carta:** «pH 7.09. Alguien diga algo inteligente.»
- **Añadido extra:** Pareja con R32 — esta es la versión COMPLICADA: mismo objeto, mismo encuadre; cambia solo lo que sale mal. Lleva chip de sistema: en la app esta carta luce la banda iridiscente al verla en grande.

### R44 · Pleurostomía

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
OBJECT CARD: the object nearly isolated, 3/4 or frontal view, filling about 60% of the frame, on an ambient monochrome hospital background, never white.
AMBIENT COLOR FAMILY: hospital teal-blue (#5b9dc4) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: a chest tube kit with chalk marks counting rib spaces on a diagram, the water-seal chamber bubbling politely in a corner.
```

- **Descripción:** 💉 Procedimientos · 🫁 Respiratorio ×2 · ⚠️ Fuga Aérea Persistente · 1 copia(s)
- **Frase de la carta:** «Entre la cuarta y la quinta costilla. Por el borde superior. Por favor.»
- **Añadido extra:** Sin gemela limpia: la complicación vive en la misma imagen. Lleva chip de sistema: en la app esta carta luce la banda iridiscente al verla en grande.

### R45 · Punción Lumbar

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
OBJECT CARD: the object nearly isolated, 3/4 or frontal view, filling about 60% of the frame, on an ambient monochrome hospital background, never white.
AMBIENT COLOR FAMILY: dark lavender purple (#a184c9) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: a lumbar puncture needle poised over the curved back of a patient curled like a shrimp, a dotted target line between two vertebrae.
```

- **Descripción:** 💉 Procedimientos · 🧠 Neurológico ×2 · 1 copia(s)
- **Frase de la carta:** «Quédese quietito. Va a sentir un pinchazo... y una cefalea de tres días.»
- **Añadido extra:** Lleva chip de sistema: en la app esta carta luce la banda iridiscente al verla en grande.

### R34 · Enfermera de UCI

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
STAFF PORTRAIT: bust or half body of the person in their working gesture, tired but competent, ICU ambience behind.
AMBIENT COLOR FAMILY: neutral hospital teal (#4a8a96) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: veteran ICU nurse, bust, taping a line with perfect technique while giving the viewer the polite look of someone who already knows the answer.
```

- **Descripción:** 🧑‍⚕️ Personal · 🛡️ previene Bacteriemia por Catéter · 3 copia(s)
- **Frase de la carta:** «Sabe más que tú. Te lo dirá con mucha educación.»
- **Añadido extra:** Carta única, sin pareja.

### R35 · Técnico en Enfermería

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
STAFF PORTRAIT: bust or half body of the person in their working gesture, tired but competent, ICU ambience behind.
AMBIENT COLOR FAMILY: neutral hospital teal (#4a8a96) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: ICU technician carrying half the unit in one arm — supply stack, monitor cable, and the dignity of the whole shift — without dropping anything.
```

- **Descripción:** 🧑‍⚕️ Personal · 🛡️ previene Neumonía Asociada a VM · 2 copia(s)
- **Frase de la carta:** «Sostiene la unidad entera. Y la camilla. Y al interno.»
- **Añadido extra:** Carta única, sin pareja.

### R36 · Personal de Turno Extra

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
STAFF PORTRAIT: bust or half body of the person in their working gesture, tired but competent, ICU ambience behind.
AMBIENT COLOR FAMILY: neutral hospital teal (#4a8a96) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: the same technician on hour twenty-four: two coffee mugs, cap slightly crooked, one eye twitching, still standing, still carrying everything.
```

- **Descripción:** 🧑‍⚕️ Personal · ⚠️ El Turno Veinticuatro · 1 copia(s)
- **Frase de la carta:** «Aceptó el turno 24. Nadie le preguntó cómo venía del anterior.»
- **Añadido extra:** Sin gemela limpia: la complicación vive en la misma imagen.

### R37 · Becado de Medicina

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
STAFF PORTRAIT: bust or half body of the person in their working gesture, tired but competent, ICU ambience behind.
AMBIENT COLOR FAMILY: neutral hospital teal (#4a8a96) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: young medical fellow with an open manual, enthusiastic sparkle, pockets bursting with pocket guides; a heart full of theory and hands full of hope.
```

- **Descripción:** 🧑‍⚕️ Personal · ⚠️ Aún Estoy Aprendiendo · 1 copia(s)
- **Frase de la carta:** «Quiere aprender. Hoy. Ahora. Contigo.»
- **Añadido extra:** Sin gemela limpia: la complicación vive en la misma imagen.

### R38 · Gestor de Camas

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
STAFF PORTRAIT: bust or half body of the person in their working gesture, tired but competent, ICU ambience behind.
AMBIENT COLOR FAMILY: neutral hospital teal (#4a8a96) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: bed manager holding a clipboard where the beds are drawn as Tetris pieces that don't fit; he brings no beds, only questions about beds.
```

- **Descripción:** 🧑‍⚕️ Personal · ⚠️ Presión de Camas · 1 copia(s)
- **Frase de la carta:** «No trae camas. Trae preguntas sobre las camas.»
- **Añadido extra:** Sin gemela limpia: la complicación vive en la misma imagen.

### R39 · Kinesiólogo Respiratorio

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
STAFF PORTRAIT: bust or half body of the person in their working gesture, tired but competent, ICU ambience behind.
AMBIENT COLOR FAMILY: hospital teal-blue (#5b9dc4) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: respiratory physiotherapist mid chest-percussion, already half out of the door in motion blur; came, aspirated, mobilized, vanished.
```

- **Descripción:** 🧑‍⚕️ Personal · 🫁 Respiratorio ×2 · 🛡️ previene Delirium en UCI · 2 copia(s)
- **Frase de la carta:** «Vino, aspiró, movilizó y se fue. Nadie sabe a dónde.»
- **Añadido extra:** Lleva chip de sistema: en la app esta carta luce la banda iridiscente al verla en grande.

### R53 · Pabellón

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
STAFF PORTRAIT: bust or half body of the person in their working gesture, tired but competent, ICU ambience behind.
AMBIENT COLOR FAMILY: amber / mustard (#c19a4e) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: gleaming operating room double doors opening with rays of light — and one dotted silhouette where the anesthesiologist should be standing.
```

- **Descripción:** 🧑‍⚕️ Personal · 🔪 Quirúrgico ×2 · ⚠️ Pabellón Suspendido · 2 copia(s)
- **Frase de la carta:** «Hay pabellón. Hay equipo. Falta el anestesista.»
- **Añadido extra:** Sin gemela limpia: la complicación vive en la misma imagen. Lleva chip de sistema: en la app esta carta luce la banda iridiscente al verla en grande.

### R54 · Cirujano de Turno

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
STAFF PORTRAIT: bust or half body of the person in their working gesture, tired but competent, ICU ambience behind.
AMBIENT COLOR FAMILY: neutral hospital teal (#4a8a96) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: scrubbed surgeon counting instruments with theatrical confidence; on the count tray, one gauze slot conspicuously empty and glowing.
```

- **Descripción:** 🧑‍⚕️ Personal · ⚠️ Oblito Quirúrgico · 1 copia(s)
- **Frase de la carta:** «Yo opero. El postoperatorio es problema de ustedes.»
- **Añadido extra:** Sin gemela limpia: la complicación vive en la misma imagen.

### R42 · Médico General de Turno

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
STAFF PORTRAIT: bust or half body of the person in their working gesture, tired but competent, ICU ambience behind.
AMBIENT COLOR FAMILY: neutral hospital teal (#4a8a96) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: the general practitioner on duty, bust, holding a swiss-army stethoscope with a tool for everything; the one who is always there.
```

- **Descripción:** 🃏 Comodín · vale por cualquier tipo · 2 copia(s)
- **Frase de la carta:** «No es su especialidad, pero es el que está. Siempre es el que está.»
- **Añadido extra:** Carta única, sin pareja.

### R43 · Stock de Sala

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
OBJECT CARD: the object nearly isolated, 3/4 or frontal view, filling about 60% of the frame, on an ambient monochrome hospital background, never white.
AMBIENT COLOR FAMILY: neutral hospital teal (#4a8a96) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: an open ward drawer with the survivors: odd gloves, one saline flush, a bandage roll and a tiny tumbleweed of gauze rolling past.
```

- **Descripción:** 🃏 Comodín · vale por cualquier tipo · ⚠️ La Gaveta Vacía · 1 copia(s)
- **Frase de la carta:** «Lo que quedó en la gaveta. Sirve para algo. Para algo sirve.»
- **Añadido extra:** Sin gemela limpia: la complicación vive en la misma imagen.

---

## 4. Protocolos — las Acciones (22 diseños)

Escena mínima: una o dos figuras o un elemento en movimiento; la emoción
manda sobre el detalle. Aquí la paleta se suelta por tipo — ataque
rojizo, apoyo cálido, caos nocturno, respuesta serena, extrema oscura —
y ya viene puesta en cada prompt.

### A01 · Vacaciones

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
ACTION SCENE: minimal scene, one or two figures or a single element in motion; the emotion leads over the detail.
AMBIENT COLOR FAMILY: brick red / rust conflict palette (#b5533c) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: a nurse silhouette walking off toward the exit with a suitcase and a sun hat, leaving a glowing dotted outline at the bedside; an HR stamp floats above, freshly inked.
```

- **Descripción:** ATAQUE · coste 2 · Elige un recurso 🧑‍⚕️ Personal colocado sobre un paciente rival: vuelve a la mano de su dueño.
- **Frase de la carta:** «Quince días hábiles. Aprobados por RR.HH. justo hoy.»
- **Añadido extra:** Conflicto de pasillo: que se note quién pierde.

### A02 · Cumpleaños del Residente

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
ACTION SCENE: minimal scene, one or two figures or a single element in motion; the emotion leads over the detail.
AMBIENT COLOR FAMILY: brick red / rust conflict palette (#b5533c) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: a circle of rival staff reluctantly handing supplies to one beaming resident holding a birthday cake; every gift has a tiny invisible debt attached.
```

- **Descripción:** ATAQUE · coste 3 · Cada rival elige uno de sus recursos en juego y te lo entrega. Colócalos sobre tus pacientes.
- **Frase de la carta:** «Trajo torta para todos. Ahora todos le deben algo.»
- **Añadido extra:** Conflicto de pasillo: que se note quién pierde.

### A03 · Reunión Clínica

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
ACTION SCENE: minimal scene, one or two figures or a single element in motion; the emotion leads over the detail.
AMBIENT COLOR FAMILY: warm amber / honey palette (#c98d3e) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: a long meeting table with a wall clock at the two-hour mark, resources sliding across the table like poker chips toward their new beds.
```

- **Descripción:** APOYO · coste 2 · Redistribuye libremente hasta 3 recursos entre TUS pacientes.
- **Frase de la carta:** «Dos horas para decidir lo que ya sabías al minuto cuatro.»
- **Añadido extra:** Cooperación: manos que entregan, alivio visible.

### A04 · Interconsulta

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
ACTION SCENE: minimal scene, one or two figures or a single element in motion; the emotion leads over the detail.
AMBIENT COLOR FAMILY: warm amber / honey palette (#c98d3e) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: a hand rescuing one shining card from a trash bin of crumpled papers, a note attached reading like a polite suggestion; the find goes to the pocket, not the bed.
```

- **Descripción:** APOYO · coste 2 · Busca en la pila de descartes 1 carta de Recurso y ponla en tu mano.
- **Frase de la carta:** «Respondió al cuarto día: 'sugiero evaluar'.»
- **Añadido extra:** Cooperación: manos que entregan, alivio visible.

### A05 · Doblo Turno

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
ACTION SCENE: minimal scene, one or two figures or a single element in motion; the emotion leads over the detail.
AMBIENT COLOR FAMILY: warm amber / honey palette (#c98d3e) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: one doctor with two ID badges, three coffees and an armful of extra cards, while a ghost version of tomorrow-him slumps in the corner.
```

- **Descripción:** APOYO · coste 1 · Roba 3 cartas adicionales. En tu próximo turno robas solo 2.
- **Frase de la carta:** «Me quedo. Total, ya estoy acá.»
- **Añadido extra:** Cooperación: manos que entregan, alivio visible.

### A06 · Se Cayó el Sistema

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
ACTION SCENE: minimal scene, one or two figures or a single element in motion; the emotion leads over the detail.
AMBIENT COLOR FAMILY: night slate-blue palette (#4a5a78) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: a dead computer screen at the nurses station with a yellowed sticky note, staff frozen mid-click around it; a cable drawn like a crime scene.
```

- **Descripción:** CAOS · coste 1 · Durante la próxima ronda completa, ningún jugador puede jugar cartas de Acción.
- **Frase de la carta:** «Estamos trabajando en ello. Lleva tres años el cartel.»
- **Añadido extra:** Todo pasando a la vez; el desorden es el chiste.

### A07 · ¡Liceeeencia!

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
ACTION SCENE: minimal scene, one or two figures or a single element in motion; the emotion leads over the detail.
AMBIENT COLOR FAMILY: brick red / rust conflict palette (#b5533c) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: two white coats swapping mid-air between two horrified doctors, name tags trading places; a medical leave form flutters down like a feather.
```

- **Descripción:** ATAQUE · coste 2 · Intercambia tu carta de avatar con la de un rival hasta el final de tu próximo turno. Las habilidades 1×PARTIDA ya gastadas siguen gastadas.
- **Frase de la carta:** «Estrés laboral. Alguien tiene que cubrir el puesto. Ese alguien eres tú.»
- **Añadido extra:** Conflicto de pasillo: que se note quién pierde.

### A08 · Llaman de Urgencias

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
ACTION SCENE: minimal scene, one or two figures or a single element in motion; the emotion leads over the detail.
AMBIENT COLOR FAMILY: brick red / rust conflict palette (#b5533c) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: a red wall phone ringing itself off the hook, twelve tally marks scratched beside it, the corridor lights flickering to attention.
```

- **Descripción:** ATAQUE · coste 1 · Un rival elige uno de sus pacientes. Ese paciente pierde 1 ❤️ adicional en su próximo Fin de Guardia.
- **Frase de la carta:** «Urgencias tiene doce esperando. Doce.»
- **Añadido extra:** Conflicto de pasillo: que se note quién pierde.

### A09 · Auditoría

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
ACTION SCENE: minimal scene, one or two figures or a single element in motion; the emotion leads over the detail.
AMBIENT COLOR FAMILY: brick red / rust conflict palette (#b5533c) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: an auditor with a clipboard leaning uncomfortably close over someone's fanned hand of cards, smiling the smile of someone who is definitely fiscalizing.
```

- **Descripción:** ATAQUE · coste 2 · Mira la mano de un rival y descarta 1 carta de ella.
- **Frase de la carta:** «Vengo a acompañar el proceso, no a fiscalizar. (Miente.)»
- **Añadido extra:** Conflicto de pasillo: que se note quién pierde.

### A10 · Rotación de Internos

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
ACTION SCENE: minimal scene, one or two figures or a single element in motion; the emotion leads over the detail.
AMBIENT COLOR FAMILY: night slate-blue palette (#4a5a78) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: two full hands of cards crossing mid-air in a small tornado between two desks, name stickers flying loose; nobody knows who rotates where.
```

- **Descripción:** CAOS · coste 1 · Intercambia tu mano completa con la de un rival a tu elección.
- **Frase de la carta:** «Nadie sabe quién rota a dónde. Ellos tampoco.»
- **Añadido extra:** Todo pasando a la vez; el desorden es el chiste.

### A11 · ¿Y Si Vamos por un Cafecito?

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
ACTION SCENE: minimal scene, one or two figures or a single element in motion; the emotion leads over the detail.
AMBIENT COLOR FAMILY: calm hospital teal (#4a8a96) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: two steaming coffee cups on a tray raised like a shield, an incoming complication bolt bouncing off the steam; somewhere, a kettle did its duty.
```

- **Descripción:** RESPUESTA · coste 2 · 🛡️ RESPUESTA — Juega fuera de turno. Anula una carta de Acción o una complicación ⚠️ que se acabe de resolver.
- **Frase de la carta:** «Nadie sabe quién lo hizo ni cuándo. Está listo y está caliente.»
- **Añadido extra:** El gesto de DETENER algo en el aire.

### A12 · Protocolo Institucional

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
ACTION SCENE: minimal scene, one or two figures or a single element in motion; the emotion leads over the detail.
AMBIENT COLOR FAMILY: warm amber / honey palette (#c98d3e) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: a dusty institutional binder glowing on a shelf as it photocopies the last played card by itself, the copy sliding out still warm.
```

- **Descripción:** APOYO · coste 1 · Copia el efecto de la última carta de Acción jugada en la partida, como si la jugaras tú.
- **Frase de la carta:** «Está en la intranet. En un PDF. En una carpeta. En algún lado.»
- **Añadido extra:** Cooperación: manos que entregan, alivio visible.

### A13 · Anda Rondando la Pelada

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
ACTION SCENE: minimal scene, one or two figures or a single element in motion; the emotion leads over the detail.
AMBIENT COLOR FAMILY: deep nocturnal purple, almost black (#3d2b52) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: the far end of a dark corridor: a hooded skeletal figure in scrubs politely asking at bed 4, two coins spinning in the air above an open palm.
```

- **Descripción:** EXTREMA · coste 1 · ÚNICA. Juégala solo si un rival tiene 2 o más ✝️. Lanza 2 monedas. Dos caras: elige un paciente de ese rival (aunque esté ✅) y dale el Alta Celestial de inmediato. Cualquier otro resultado: descarta toda tu mano.
- **Frase de la carta:** «Pasó preguntando por la cama 4. Dijo que volvía al rato.»
- **Añadido extra:** El gesto más grande del mazo: respeto y humor negro a partes iguales.

### A14 · Ojo Clínico

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
ACTION SCENE: minimal scene, one or two figures or a single element in motion; the emotion leads over the detail.
AMBIENT COLOR FAMILY: warm amber / honey palette (#c98d3e) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: a doctor with one enormous magnifying-glass eye squinting at three face-down cards on the deck, one of them sweating.
```

- **Descripción:** APOYO · coste 1 · Mira las 3 primeras cartas del Mazo de Guardia. Devuélvelas en el orden que quieras o manda 1 al fondo.
- **Frase de la carta:** «Yo a este paciente lo veo raro. No sé por qué. Lo veo raro.»
- **Añadido extra:** Cooperación: manos que entregan, alivio visible.

### A15 · Receta en Blanco

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
ACTION SCENE: minimal scene, one or two figures or a single element in motion; the emotion leads over the detail.
AMBIENT COLOR FAMILY: warm amber / honey palette (#c98d3e) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: a signed blank prescription flying through the ward like a golden ticket, staff diving after it; the signature is a lightning scribble.
```

- **Descripción:** APOYO · coste 3 · Busca en el Mazo de Guardia 1 recurso a tu elección y ponlo en tu mano. Baraja el mazo.
- **Frase de la carta:** «La firmó apurado, sin mirar. Que Dios reparta suerte.»
- **Añadido extra:** Cooperación: manos que entregan, alivio visible.

### A16 · Simulación Clínica

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
ACTION SCENE: minimal scene, one or two figures or a single element in motion; the emotion leads over the detail.
AMBIENT COLOR FAMILY: calm hospital teal (#4a8a96) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: a CPR training dummy heroically raising a shield to block an incoming complication bolt aimed at the bed behind it; it has seen worse.
```

- **Descripción:** RESPUESTA · coste 2 · 🛡️ RESPUESTA — Juega fuera de turno. Anula una complicación ⚠️ antes de que se resuelva: el recurso se queda puesto sobre el paciente y no pasa nada más.
- **Frase de la carta:** «Lo practicamos con el muñeco. El muñeco no se movía tanto.»
- **Añadido extra:** El gesto de DETENER algo en el aire.

### A17 · Quiebre de Stock

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
ACTION SCENE: minimal scene, one or two figures or a single element in motion; the emotion leads over the detail.
AMBIENT COLOR FAMILY: brick red / rust conflict palette (#b5533c) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: a pharmacy shelf empty except for a small sign promising Thursday, a spider web in the corner and one loyal box of the wrong size.
```

- **Descripción:** ATAQUE · coste 2 · En su próximo turno, tu rival no puede colocar recursos 💊 Fármacos.
- **Frase de la carta:** «Llega el jueves. Lleva tres jueves llegando.»
- **Añadido extra:** Conflicto de pasillo: que se note quién pierde.

### A18 · Recorte Presupuestario

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
ACTION SCENE: minimal scene, one or two figures or a single element in motion; the emotion leads over the detail.
AMBIENT COLOR FAMILY: brick red / rust conflict palette (#b5533c) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: a giant pair of budget scissors cutting a ribbon shaped like an IV line; below, a hand holds two indication tokens where three used to be.
```

- **Descripción:** ATAQUE · coste 2 · En su próximo turno, tu rival tiene solo 2 indicaciones en su Pase de Visita.
- **Frase de la carta:** «Hay que hacer más con menos. Otra vez menos.»
- **Añadido extra:** Conflicto de pasillo: que se note quién pierde.

### A19 · El Que Guarda Siempre Tiene

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
ACTION SCENE: minimal scene, one or two figures or a single element in motion; the emotion leads over the detail.
AMBIENT COLOR FAMILY: warm amber / honey palette (#c98d3e) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: the deep bottom drawer opening with a golden glow while a veteran nurse guards it, key on a necklace; inside, exactly what was needed.
```

- **Descripción:** APOYO · coste 1 · Elige un paciente tuyo: hasta tu próximo turno, sus recursos no pueden ser robados ni descartados, y los rivales no pueden colocarle recursos.
- **Frase de la carta:** «La gaveta del fondo. La que solo ella sabe abrir.»
- **Añadido extra:** Cooperación: manos que entregan, alivio visible.

### A20 · Hay Que Repetirlo

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
ACTION SCENE: minimal scene, one or two figures or a single element in motion; the emotion leads over the detail.
AMBIENT COLOR FAMILY: brick red / rust conflict palette (#b5533c) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: a sample tube shaken like a cocktail shaker with a tiny umbrella, next to an X-ray sliding into a bin with a REPEAT stamp mid-air.
```

- **Descripción:** ATAQUE · coste 2 · Descarta un recurso 🩻 Imagen o 💉 Procedimientos de un paciente rival.
- **Frase de la carta:** «Se tomó bien. Se rotuló bien. Se agitó como coctelera.»
- **Añadido extra:** Conflicto de pasillo: que se note quién pierde.

### A21 · Encarnizamiento Terapéutico

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
ACTION SCENE: minimal scene, one or two figures or a single element in motion; the emotion leads over the detail.
AMBIENT COLOR FAMILY: brick red / rust conflict palette (#b5533c) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: a wall of machines looming over one tiny bed, one more device being plugged in by insistent hands; new ribs gleam, nobody asked the question.
```

- **Descripción:** ATAQUE · coste 3 · Elige un paciente rival sin ✅: pierde 1 ❤️ (no puede bajar de 1 ❤️) y su dueño descarta 1 recurso ya colocado sobre él.
- **Frase de la carta:** «Tres ciclos. Costillas nuevas. Nadie preguntó si correspondía.»
- **Añadido extra:** Conflicto de pasillo: que se note quién pierde.

### A22 · Alta Anticipada

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
ACTION SCENE: minimal scene, one or two figures or a single element in motion; the emotion leads over the detail.
AMBIENT COLOR FAMILY: warm amber / honey palette (#c98d3e) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: a patient in street clothes sprinting out the ward door trailing ECG leads like streamers, discharge paper stamped mid-air, one slipper left behind.
```

- **Descripción:** APOYO · coste 2 · Elige un paciente tuyo estabilizado ✅ en este mismo turno y sin basura clínica: dale el alta de inmediato, sin esperar tu próxima Entrega. El alta apurada vale 2 puntos menos.
- **Frase de la carta:** «—¿Y el control? —En el CESFAM. —¿Cuándo? —Sí.»
- **Añadido extra:** Cooperación: manos que entregan, alivio visible.

---

## 5. El Sumario Administrativo (1)

### S01 · Sumario Administrativo

```text
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire), flat colors with minimal 1-2 tone cel shading, subtle vintage print grain. Exaggerated comic style: big heads (3-4 heads tall), expressive tired faces, drawn under-eye circles, anxious hospital humor. Board-game card art composition: one strong silhouette, one clear readable action, the subject in the central third of the frame. Full-bleed background, never white. No game text, no labels except small ambient signs. No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
OBJECT CARD: a single document as the whole threat, filling the frame with its shadow.
AMBIENT COLOR FAMILY: cold gray-teal bureaucratic palette (#5f7a80) — the whole image lives in this ONE monochromatic family; background and subject share the same color temperature.
SCENE: a manila folder bristling with red stamps and seals, grown huge, casting a long shadow over a tiny clinician's desk below; one paper clip like a padlock.
```

- **Descripción:** La sanción del juego: cada Sumario abierto muerde 1 carta del límite de mano; cerrarlo cuesta 2 cartas.
- **Frase de la carta:** «El proceso será justo, transparente y eterno.»
- **Añadido extra:** Burocracia como amenaza: el documento es el monstruo. Una sola imagen para las 6 copias.

---

*Generado con `python3 tools/generar_prompts_arte.py` sobre los CSV
vivos del repo — si una carta cambia de nombre o habilidad, regenerar.
Los prompts son autosuficientes: el estilo, el encuadre, el color y la
escena van adentro de cada bloque.*
