# ¡VAYA TURNO! — Brief completo para IA

> **Este archivo es autocontenido.** Contiene todo lo necesario para entender
> el juego y producir sus ilustraciones sin acceso al repositorio: el
> concepto, las reglas completas, el tempo, la especificación física de la
> carta, la dirección de arte con su bloque de estilo literal, y las 113
> cartas una por una con su encargo de imagen.
>
> Generado desde los datos del juego (`cartas/*.csv`) — versión de reglas
> **v0.21**. Si algo aquí contradice a un documento suelto más viejo, manda
> este archivo.

---

## 0. Instrucciones para el modelo que lea esto

Eres el director de arte de un juego de cartas de mesa en español (Chile).
Tu trabajo es producir **ilustraciones**, no texto de juego ni reglas nuevas.

1. **Lee la §4 antes de dibujar nada.** El estilo ya existe: hay 42
   ilustraciones terminadas que definen la casa (§4.5). No propongas un
   estilo nuevo.
2. **Copia el bloque de estilo de §4.1 literalmente en cada prompt**, y
   agrégale la *familia de color* que la carta indica en §5.
3. **Una carta = una imagen.** Nombra el archivo con el id de la carta:
   `P19.png`, `R31.png`, `A07.png`, `C05.png`, `S01.png`.
4. **Nunca escribas texto del juego dentro del dibujo.** El nombre, los
   números y las reglas los pone la maqueta. Solo se permiten letreros
   ambientales cortos y creíbles dentro de la escena ("UCI", "OXÍGENO",
   "PABELLÓN").
5. **El humor está en la cara y en la situación, nunca en la crueldad.**
   Ver §1.3: hay una línea que no se cruza.
6. Si una carta te parece imposible de ilustrar, dilo y propón una
   alternativa — no la inventes en otro estilo.

---

## 1. El juego

### 1.1 Qué es

**¡VAYA TURNO!** es un juego de cartas competitivo sobre **triage en una
Unidad de Cuidados Intensivos**. Cada jugador dirige una UCI de **3 camas**.
Los pacientes llegan solos y se deterioran solos; los recursos llegan
mezclados y nunca alcanzan. El juego consiste en **elegir a quién salvas**.

- **2 a 4 jugadores** · **30–45 minutos** · **14+**
- Lo escribe un trabajador de la salud chileno. El material clínico es real:
  las complicaciones son las complicaciones que esos procedimientos causan de
  verdad, y los chistes son los del pasillo.
- **No vas a salvarlos a todos.** Eso no es un defecto del juego: es la tesis.

### 1.2 El tono — esto es lo más importante para el arte

Humor **negro, cansado y cariñoso**. No es una parodia del hospital: es el
hospital contado por alguien que lleva doce horas ahí y que quiere a su
equipo. El registro exacto:

- **Cansancio antes que drama.** Ojeras dibujadas, café frío, el pelo
  aplastado por el gorro. La tensión es de turno largo, no de serie de TV.
- **Burocracia como monstruo.** El Sumario Administrativo da más miedo que la
  muerte, y ese chiste es central.
- **Los pacientes tienen dignidad.** Son ridículos por lo que *dicen* y por
  cómo llegaron, no por estar enfermos.
- **El equipo es el héroe silencioso.** Enfermera, TENS, kinesiólogo: se
  dibujan competentes, aunque estén agotados.

### 1.3 La línea que no se cruza

- Nada de sangre gráfica, vísceras, heridas abiertas ni sufrimiento explícito.
- Nada que se burle del paciente por su cuerpo, su peso, su pobreza o su
  origen.
- Nada de muerte representada con realismo. **La muerte en este juego es "el
  Alta Celestial"**, y se dibuja con humor suave (nubes, una cruz de fichas),
  nunca con un cadáver.
- Nada de logos, marcas de medicamentos reales ni nombres de hospitales
  reales.

---

## 2. Las reglas, completas y comprimidas

Un artista no necesita jugar, pero sí necesita saber **qué hace cada carta y
por qué importa**, porque eso es lo que la imagen tiene que comunicar en un
segundo.

### 2.1 Componentes

| Componente | Cant. | Qué es |
|---|---:|---|
| **Pacientes** | 26 | Llegan solos. Cada uno pide recursos y tiene vida ❤️ |
| **Recursos** (Mazo de Guardia) | 65 (44 diseños) | 🩻 Imagen · 💊 Fármacos · 🧑‍⚕️ Personal · 💉 Procedimientos · 🃏 Comodín |
| **Protocolos** (Acciones) | 30 (20 diseños) | Mazo aparte. Se compran, no se roban |
| **Personajes** (avatares) | 22 | Uno por jugador, con una habilidad propia |
| **Sumario Administrativo** | 6 (1 diseño) | La maldición. Llega cuando se te muere alguien |

Fichas: ❤️ vida · ✅ estabilizado · ✝️ Alta Celestial · 1 moneda · marcador de
ronda.

### 2.2 El objetivo

Al final de **8 rondas** gana quien tenga más puntos:

```
  + puntos de cada paciente dado de ALTA
  − penalización de cada ✝️ (paciente fallecido)
  − 1 punto por cada cama que dejaste vacía en cada noche
  + 3 si terminas SIN NINGÚN ✝️            "No se me fue nadie"
  + 1 si tus únicos ✝️ fueron los más graves  "Se hizo todo"
```

Los dos bonus no se suman: o lo uno, o lo otro.

### 2.3 Los pacientes: la tabla de precios

| Gravedad | ❤️ | Recursos que pide | Alta | Fallece |
|---|---:|---:|---:|---:|
| **I — Observación** | 7 | 3 | +2 | −1 |
| **II — Grave** | 6 | 5 | +3 | −2 |
| **III — Crítico** | 6 | 8 | +6 | −2 |
| **★ Código Rojo** | 5 | 8 | +8 | −3 |

La regla escondida: `alta + |fallece| = recursos que pide`. Cada punto cuesta
exactamente un recurso. **La vida no es el precio, es el plazo**: 7 ❤️ = siete
rondas para pagar. Por eso el crítico no es caro, es *urgente*.

### 2.4 El turno: cuatro fases (este es el tempo)

Una **ronda** son los turnos de todos. Cada Fin de Guardia **es un día que
pasa**. La partida dura 8 rondas: una guardia completa.

**1 · ENTREGA DE TURNO** — *llegas y te cuentan cómo está la unidad*
- Da de alta a todo paciente que ya tenía ✅ **desde antes de este turno**.
- **Puedes** admitir en cada cama vacía: revelas 2 pacientes, eliges 1. La
  primera carta de la fila de urgencias está siempre **boca arriba** (el
  *Informe de Gestión de Camas*), así decides sabiendo la mitad.
- Robas 4 cartas del Mazo de Guardia.

**2 · EL PASILLO** — *negocias*
- Un solo negocio por turno: **Canje** (botas 2 recursos → robas 2 Protocolos
  y te quedas 1) o **Trueque** con un rival.
- Puedes jugar como máximo **1 Acción**.

**3 · PASE DE VISITA** — *tratas*
- Colocas **hasta 3 recursos** sobre tus pacientes. Los recursos se quedan
  encima de la carta, en abanico: **son su tratamiento, no se gastan**.
- Un recurso de un sistema clínico jugado sobre un paciente del mismo sistema
  **cuenta doble**.
- Paciente con todo lo que pide → ficha **✅**: deja de deteriorarse.

**4 · FIN DE GUARDIA** — *pasa el día*
- Todo paciente sin ✅ **pierde 1 ❤️**.
- A 0 ❤️ recibe el **Alta Celestial**: ✝️, puntos negativos y un Sumario.
- Descartas hasta quedar con 5 cartas.

> **La ventana de sabotaje**, que es el corazón social del juego:
> **estabilizas en un turno y das de alta en el siguiente.** Entre medio pasa
> el turno de todos los demás, y tu paciente terminado está a la vista de
> todos.

### 2.5 Las Complicaciones ⚠️

18 de las 65 cartas de recurso llevan el sello **⚠️** y traen impresa **la
complicación que ese recurso causa de verdad**: el ventilador trae la neumonía
asociada a ventilación mecánica, el catéter la bacteriemia, el antibiótico la
resistencia.

- **Se disparan al COLOCAR la carta**, no al robarla. Tenerla en la mano no
  hace nada: es una decisión de riesgo-beneficio.
- **Todas hacen lo mismo: el paciente señalado pierde 1 ❤️.** Lo que cambia es
  a quién señalan (el 🎯 Objetivo) y cómo se llaman.
- Once de las dieciocho apuntan **al que iba bien** o al que ya tenía su ✅, y
  cuatro **al paciente que acabas de tratar**. Eso es deliberado: lo que se
  complica en una UCI es lo que parecía resuelto, o lo que tú mismo tocaste.

**Las Protecciones 🛡️:** tres cartas de Personal previenen una complicación
con nombre, *si ya estaban puestas antes*. El TENS con la cabecera a 30°
previene la neumonía; la enfermera con manejo estéril previene la bacteriemia;
el kinesiólogo con movilización precoz previene el delirium. Son bundles
reales de UCI, y esa es la mejor parte del juego.

### 2.6 Qué significa "fuerte" en este juego

Para que las imágenes acompañen la potencia de cada carta:

- La moneda real es **la indicación**: tienes 3 por turno, 24 por guardia.
- **1 carta en mano ≈ medio punto.** Un tutor (buscar la carta exacta) vale
  dos cartas.
- Una **Acción** cuesta un Canje ≈ 2 indicaciones ≈ 1 punto de swing. Son
  cartas de momento, no de poder bruto.
- Una **habilidad de avatar** sana vale entre **+0,3 y +1,0 puntos** de
  ventaja. Ninguna gana la partida sola.

---

## 3. Especificación física de la carta

- **Formato: 63 × 88 mm** (el estándar de Magic / Mitos y Leyendas / poker).
  Se imprime 9 por hoja Carta y se corta con guillotina.
- La maqueta reserva una **ventana de ilustración de 55,7 mm de ancho**. La
  altura cambia según cuánto texto lleva la carta:

| Tipo de carta | Ventana (ancho × alto) |
|---|---|
| Paciente Gravedad I / II | 55,7 × 32,2 / 28,3 mm |
| Paciente Gravedad III / Código Rojo | 55,7 × 35,5 mm |
| Recurso 🩻 Imagen · 💉 Procedimientos | 55,7 × 61,5 mm |
| Recurso 💊 Fármacos | 55,7 × 57,6 mm |
| Recurso 🧑‍⚕️ Personal | 55,7 × 46,9 mm |
| Recurso 🃏 Comodín | 55,7 × 54,5 mm |
| Acción (según tipo) | 55,7 × 29,6 – 45,2 mm |
| Personaje | 55,7 × 31,8 mm |
| Sumario | 55,7 × 29,6 mm |

> **Cómo resolver esa contradicción, que es la instrucción más importante de
> esta sección.** Las 39 ilustraciones que ya existen son **2:3 vertical a
> sangre completa**, y así hay que seguir generándolas para que todo se vea
> de la misma caja. Pero la ventana más angosta (28,3 mm sobre 55,7 mm de
> ancho) equivale a **la banda central del 34% de la altura** de esa imagen.
>
> Entonces: **genera 2:3 vertical, pero compón para que la cara, el gesto y
> el objeto que identifica la carta vivan en el tercio central**. Lo de
> arriba y lo de abajo es ambiente sacrificable. Una imagen que pone la cara
> arriba se pierde al recortarla.

- **A sangre completa: el fondo llena el rectángulo, nunca blanco.**
- Resolución de entrega: mínimo **1024 × 1536 px** (2:3). PNG.
- Se imprime en casa, muchas veces **en escala de grises**. Comprueba que la
  imagen se lea sin color: necesita contraste de valor, no solo de tono.

---

## 4. Dirección de arte

### 4.1 El estilo canónico — "Retro de Guardia"

Definido por 42 ilustraciones que ya existen y están terminadas. Sus rasgos,
en orden de importancia:

1. **Línea:** contorno café oscuro **grueso y de ancho uniforme** (ligne
   claire de cartoon moderno). Nada de boceto, nada de línea temblorosa.
2. **Color:** planos, con **cel shading mínimo** de 1–2 tonos. Sin degradados,
   sin acuarela.
3. **La firma de la casa: cada imagen vive en UNA familia de color.** Fondo
   monocromo ambiental y personaje compartiendo la misma temperatura. Es lo
   único que hace que 113 imágenes se vean de la misma caja.
4. **Proporciones:** cabezones (3–4 cabezas), expresiones exageradas, ojeras
   dibujadas. **La comedia está en la cara.**
5. **Ambiente:** UCI reconocible — monitores con curvas, portasueros,
   letreros cortos.
6. **Acabado:** grano sutil de impresión retro, a sangre completa, 2:3.

**Bloque literal — cópialo tal cual en cada prompt:**

```text
[VAYA TURNO HOUSE STYLE]
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire),
flat colors with minimal 1-2 tone cel shading, subtle vintage print grain.
Exaggerated comic characters: big heads (3-4 heads tall), expressive tired faces,
drawn under-eye circles, anxious hospital humor. Setting: recognizable ICU interior
with patient monitors, IV poles and ambient signage ("ICU", "OXIGENO").
CRITICAL: the whole image lives in ONE monochromatic color family - background and
subject share the same color temperature (see AMBIENT COLOR FAMILY below).
Full-bleed background, never white. No game text, no labels except small ambient signs.
No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
Compose so the face and the identifying object sit in the CENTRAL THIRD of the frame.
AMBIENT COLOR FAMILY: <la que indique la carta en §5>
```

### 4.2 La familia de color, por sistema clínico

| Sistema | Familia ambiental | Ancla |
|---|---|---|
| 🫁 Respiratorio | teal / azul hospital | `#5b9dc4` |
| 🫀 Cardiológico | naranja quemado / rojo ladrillo | `#e0705a` |
| 🧠 Neurológico | púrpura / lavanda oscura | `#a184c9` |
| 🧪 Metabólico | verde oliva | `#5cb583` |
| 🔪 Quirúrgico | ámbar / mostaza | `#c19a4e` |
| Sin sistema (genéricos y avatares) | teal hospital neutro | `#4a8a96` |
| Acciones | libre según la emoción: ataque rojizo, apoyo cálido, caos nocturno | — |

> El sistema clínico es un dato **de juego**: solo 21 de los 65 recursos lo
> llevan, porque sirve para la regla de sinergia. Cuando una carta no lo trae,
> la familia por defecto es el teal neutro — pero si el objeto pertenece
> obviamente a un sistema (un ventilador es respiratorio, aunque su carta no
> lleve chip), puedes inclinarte a esa familia. Lo que no se negocia es que la
> imagen viva en **una sola** familia.

### 4.3 El plano, por tipo de carta

| Tipo | Encuadre | Nota |
|---|---|---|
| **Paciente** | busto frontal, del pecho a la cabeza | luz frontal suave; el monitor va detrás |
| **Recurso** | el objeto casi aislado, 3/4 o frontal, ocupando ~60% | fondo monocromo ambiental, no blanco |
| **Recurso 🧑‍⚕️ Personal** | busto o medio cuerpo de la persona en su gesto de trabajo | son gente, no objetos |
| **Acción** | escena mínima, 1–2 figuras o un elemento en movimiento | la emoción manda sobre el detalle |
| **Personaje** | cuerpo entero, pose característica, ocupando ~70% | es un retrato de arquetipo |
| **Sumario** | un documento con timbres, agigantado por su sombra | burocracia como amenaza |

### 4.4 Las parejas: el mismo objeto, limpio y complicado

Quince recursos existen **dos veces**: una versión limpia y una versión ⚠️ con
complicación. **Deben compartir el objeto y el encuadre**, y diferenciarse
solo en lo que está pasando:

> *Ventilación Mecánica* limpia: el ventilador funcionando, curva estable,
> nadie mirando. *Ventilación Mecánica ⚠️ (Neumonía Asociada a VM)*: el mismo
> ventilador, mismo ángulo, pero lleva ocho días ahí — secreciones en el
> tubo, alguien con cara de "otra vez".

Esa repetición con variación es el mejor recurso narrativo del mazo. Las
quince parejas están marcadas en §5.2.

### 4.5 Las anclas visuales — mándalas junto con este archivo

Existen **18 ilustraciones ya mapeadas a cartas** (`arte/raw/`) y **24 escenas
más** en el mismo estilo (`arte/raw/extra/`), más 2 referencias de maqueta en
`arte/referencias/`. Para una IA de imagen, **una referencia visual vale más que
tres párrafos de descripción**: manda 2 o 3 de estas junto con este archivo y
pídele que las use como referencia de estilo (image-to-image o "match this
style").

Las tres que mejor cubren el rango:

| Archivo | Qué ancla |
|---|---|
| `arte/raw/C01-diostor.jpg` | personaje, teal, aureola — el arquetipo cómico |
| `arte/raw/R29-carro-de-paro.jpg` | escena con objeto y movimiento |
| `arte/raw/R34-enfermera-de-uci.jpg` | el equipo: competente y cansado a la vez |

Y dos que sirven de contexto, no de estilo:
`arte/referencias/plantilla-carta.jpg` (cómo se arma la carta) y
`arte/referencias/tablero-uci.jpg`.

> Ojo con una: `arte/raw/A20-muestra-hemolizada.jpg` está mal mapeada. A20 es
> la Acción *Hay Que Repetirlo*; *Muestra Hemolizada* es la complicación del
> recurso **R33**. Renómbrala antes de usarla como referencia de esa carta.

### 4.6 Entrega

- Un archivo por carta, nombrado con su id: `P01.png` … `R45.png` …
  `A01.png` … `C01.png` … `S01.png`.
- PNG, 2:3, mínimo 1024 × 1536.
- Si generas hojas de contacto para iterar, entrégalas aparte y recortadas al
  final.
- **Orden sugerido:** primero los 22 personajes (fijan el estilo de las
  caras), después los 26 pacientes (son los que más se miran en mesa),
  después los recursos, y al final Acciones y Sumario.

---

## 5. Las 113 cartas, una por una

### 5.1 Pacientes (26 cartas)

**Plano:** busto frontal, del pecho a la cabeza. Luz frontal suave. El monitor
y el portasueros van detrás, desenfocados por simplificación, no por foco.

**El estado clínico lo marca la gravedad:**

- **Gravedad I:** despierto, sentado, molesto o dramático; a lo más una naricera. 30–50 años
- **Gravedad II:** sedado, máscara Venturi o tubo, monitor detrás. 40–70 años
- **Gravedad III:** intubado, sedación profunda, línea arterial, monitor protagonista. 60+
- **Gravedad ROJO:** ventilado, varias infusiones corriendo, la escena más extrema del mazo

**La frase de la carta es la dirección de escena.** Es el chiste, y casi
siempre dice exactamente qué expresión hay que dibujar. Úsala como brief.

| id | Carta | Gravedad · sistema | Ficha | Familia de color | La frase = la escena |
|---|---|---|---|---|---|
| **P01** | Dolor Torácico Atípico | I · 🫀 Cardiológico | ❤️7 · pide 🩻1 💊1 💉1 | naranja quemado / rojo ladrillo · #e0705a | *Le duele cuando respira, cuando camina y cuando le hablan de la cuenta.* |
| **P02** | El del Frasco Completo | I · 🧪 Metabólico | ❤️7 · pide 💊2 🧑‍⚕️1 | verde oliva · #5cb583 | *Se lo tomó todo. Incluido el algodón.* |
| **P03** | Abandono de Tratamiento | I · 🫀 Cardiológico | ❤️7 · pide 💊2 💉1 | naranja quemado / rojo ladrillo · #e0705a | *Se sentía bien, así que dejó las pastillas. Hace ocho meses.* |
| **P04** | La Caída del Baño | I · 🔪 Quirúrgico | ❤️7 · pide 🩻2 🧑‍⚕️1 | ámbar / mostaza · #c19a4e | *'Me resbalé', dice. Nadie en la sala le cree.* |
| **P05** | Crisis de Pánico en Box 4 | I · 🧠 Neurológico | ❤️7 · pide 💊1 🧑‍⚕️2 | púrpura / lavanda oscura · #a184c9 | *Se está muriendo. Todos los martes.* |
| **P06** | Deshidratado de Verano | I · 🧪 Metabólico | ❤️7 · pide 💊1 🧑‍⚕️1 💉1 | verde oliva · #5cb583 | *Insiste en que cuatro cervezas cuentan como líquido.* |
| **P07** | El Que Googleó Sus Síntomas | I · 🧠 Neurológico | ❤️7 · pide 🩻1 💊1 🧑‍⚕️1 | púrpura / lavanda oscura · #a184c9 | *Trae impreso el diagnóstico. Y el tratamiento. Y el pronóstico.* |
| **P08** | Postoperado Que No Debería Estar Aquí | I · 🔪 Quirúrgico | ❤️7 · pide 🩻1 🧑‍⚕️1 💉1 | ámbar / mostaza · #c19a4e | *El cirujano dijo 'obsérvenlo un rato'. Van tres días.* |
| **P09** | Neumonía Adquirida en la Comunidad | II · 🫁 Respiratorio | ❤️6 · pide 🩻1 💊2 🧑‍⚕️1 💉1 | teal / azul hospital · #5b9dc4 | *Lleva un mes tosiendo. Vino hoy porque no lo dejaba dormir.* |
| **P10** | Cetoacidosis Diabética | II · 🧪 Metabólico | ❤️6 · pide 💊2 🧑‍⚕️1 💉2 | verde oliva · #5cb583 | *Se le acabó la insulina el jueves. Hoy es domingo.* |
| **P11** | ACV en Ventana | II · 🧠 Neurológico | ❤️6 · pide 🩻2 💊1 🧑‍⚕️1 💉1 | púrpura / lavanda oscura · #a184c9 | *Nadie sabe a qué hora empezó. Nadie.* |
| **P12** | Hemorragia Digestiva Alta | II · 🔪 Quirúrgico | ❤️6 · pide 🩻1 💊2 💉2 | ámbar / mostaza · #c19a4e | *Dice que es la primera vez. Es la sexta.* |
| **P13** | Insuficiencia Cardíaca Descompensada | II · 🫀 Cardiológico | ❤️6 · pide 🩻1 💊2 🧑‍⚕️1 💉1 | naranja quemado / rojo ladrillo · #e0705a | *Comió cazuela. Y sopa. Y jugo. Y postre.* |
| **P14** | Pielonefritis Complicada | II · 🧪 Metabólico | ❤️6 · pide 🩻1 💊2 🧑‍⚕️1 💉1 | verde oliva · #5cb583 | *Aguantó dos semanas por no faltar al trabajo.* |
| **P15** | Abdomen Agudo Sin Diagnóstico | II · 🔪 Quirúrgico | ❤️6 · pide 🩻3 💊1 🧑‍⚕️1 | ámbar / mostaza · #c19a4e | *Cirugía dice que es de medicina. Medicina dice que es de cirugía.* |
| **P16** | EPOC Exacerbado | II · 🫁 Respiratorio | ❤️6 · pide 🩻1 💊2 💉2 | teal / azul hospital · #5b9dc4 | *Trae su balón de oxígeno. Y su cajetilla.* |
| **P17** | Intoxicación Mixta | II · 🧪 Metabólico | ❤️6 · pide 💊3 🧑‍⚕️1 💉1 | verde oliva · #5cb583 | *Nadie sabe qué tomó. Él tampoco.* |
| **P18** | Delirium del Adulto Mayor | II · 🧠 Neurológico | ❤️6 · pide 🩻1 💊1 🧑‍⚕️3 | púrpura / lavanda oscura · #a184c9 | *De día duerme. De noche dirige una orquesta.* |
| **P19** | Shock Séptico | III · 🫀 Cardiológico | ❤️6 · pide 🩻1 💊4 🧑‍⚕️1 💉2 | naranja quemado / rojo ladrillo · #e0705a | *La hora dorada empezó hace cuatro horas.* |
| **P20** | Politraumatizado | III · 🔪 Quirúrgico | ❤️6 · pide 🩻3 💊1 🧑‍⚕️1 💉3 | ámbar / mostaza · #c19a4e | *Iba a 120. Sin cinturón. 'Por acá nunca hay control'.* |
| **P21** | Síndrome de Distrés Respiratorio | III · 🫁 Respiratorio | ❤️6 · pide 🩻2 💊2 🧑‍⚕️2 💉2 | teal / azul hospital · #5b9dc4 | *Los pulmones parecen vidrio esmerilado. Él parece tranquilo.* |
| **P22** | Status Epiléptico | III · 🧠 Neurológico | ❤️6 · pide 🩻1 💊4 🧑‍⚕️1 💉2 | púrpura / lavanda oscura · #a184c9 | *Cuarta dosis. Sigue convulsionando.* |
| **P23** | Pancreatitis Grave | III · 🔪 Quirúrgico | ❤️6 · pide 🩻3 💊2 🧑‍⚕️2 💉1 | ámbar / mostaza · #c19a4e | *Fue un asado. Uno solo, insiste.* |
| **P24** | Tromboembolismo Pulmonar Masivo | III · 🫁 Respiratorio | ❤️6 · pide 🩻2 💊2 💉4 | teal / azul hospital · #5b9dc4 | *Volvió de un vuelo de catorce horas y del baño no salió caminando.* |
| **P25** | Falla Multiorgánica | ROJO · 🫀 Cardiológico | ❤️5 · pide 🩻2 💊3 🧑‍⚕️1 💉2 | naranja quemado / rojo ladrillo · #e0705a | *Todo mal. Y en orden alfabético.* |
| **P26** | Trasplante en Lista Cero | ROJO · 🔪 Quirúrgico | ❤️5 · pide 🩻2 💊2 🧑‍⚕️2 💉2 | ámbar / mostaza · #c19a4e | *Hay órgano. Hay avión. No hay pabellón.* |

### 5.2 Recursos — el Mazo de Guardia (44 diseños, 65 cartas)

**Plano:** el objeto casi aislado, 3/4 o frontal, ocupando ~60% del cuadro,
sobre fondo monocromo ambiental. **Excepción: los recursos 🧑‍⚕️ Personal son
personas** — busto o medio cuerpo, en su gesto de trabajo, con la misma
dignidad cansada del resto del equipo.

Las marcadas **🔁 pareja** comparten objeto y encuadre con su gemela: una
limpia y una ⚠️ (ver §4.4).

| id | Carta | Tipo | Qué hace | Par | Familia de color | La frase = la escena |
|---|---|---|---|---|---|---|
| **R01** | Antibiótico de Amplio Espectro | 💊 Fármacos | — | 🔁 pareja | teal hospital neutro · #4a8a96 | *Cubre todo. Especialmente nuestra falta de diagnóstico.* |
| **R02** | Antibiótico de Amplio Espectro | 💊 Fármacos | ⚠️ **Resistencia Antibiótica** → 🎯 el estabilizado ✅ pierde 1 ❤️ | 🔁 pareja | teal hospital neutro · #4a8a96 | *Cubre todo. Especialmente nuestra falta de diagnóstico.* |
| **R03** | Sedoanalgesia | 💊 Fármacos | — | 🔁 pareja | teal hospital neutro · #4a8a96 | *Duerme él. Duerme la unidad. No duermes tú.* |
| **R04** | Sedoanalgesia | 💊 Fármacos | ⚠️ **Delirium en UCI** → 🎯 el que mejor va pierde 1 ❤️ | 🔁 pareja | teal hospital neutro · #4a8a96 | *Duerme él. Duerme la unidad. No duermes tú.* |
| **R05** | Anticoagulación | 💊 Fármacos | — | 🔁 pareja | teal hospital neutro · #4a8a96 | *Si sangra fue mucho. Si coagula fue poco. Nunca fue justo.* |
| **R06** | Anticoagulación | 💊 Fármacos | ⚠️ **Sangrado** → 🎯 el que mejor va pierde 1 ❤️ | 🔁 pareja | teal hospital neutro · #4a8a96 | *Si sangra fue mucho. Si coagula fue poco. Nunca fue justo.* |
| **R07** | Hemoderivados | 💊 Fármacos | — |  | teal hospital neutro · #4a8a96 | *Llegaron. Sin la ficha, pero llegaron.* |
| **R08** | Noradrenalina | 💊 Fármacos | — | 🔁 pareja | naranja quemado / rojo ladrillo · #e0705a | *La presión sube. La del paciente y la tuya.* |
| **R09** | Noradrenalina | 💊 Fármacos | ⚠️ **Taquicardia Ventricular** → 🎯 el que mejor va pierde 1 ❤️ | 🔁 pareja | naranja quemado / rojo ladrillo · #e0705a | *La presión sube. La del paciente y la tuya.* |
| **R10** | Broncodilatador en Nebulización | 💊 Fármacos | — |  | teal / azul hospital · #5b9dc4 | *Sale más vapor que del baño turco. Algo tiene que estar llegando.* |
| **R11** | Anticonvulsivante | 💊 Fármacos | — | 🔁 pareja | púrpura / lavanda oscura · #a184c9 | *Tercera dosis de carga. Vamos bien. Creo.* |
| **R12** | Anticonvulsivante | 💊 Fármacos | ⚠️ **Sobresedación** → 🎯 el estabilizado ✅ pierde 1 ❤️ | 🔁 pareja | púrpura / lavanda oscura · #a184c9 | *Tercera dosis de carga. Vamos bien. Creo.* |
| **R13** | Insulina en Bomba | 💊 Fármacos | — |  | verde oliva · #5cb583 | *Cada dos horas un hemoglucotest. Cada dos horas.* |
| **R14** | Analgesia Postoperatoria | 💊 Fármacos | — | 🔁 pareja | ámbar / mostaza · #c19a4e | *'¿Del uno al diez?' 'Quince.' Anotado: quince.* |
| **R15** | Analgesia Postoperatoria | 💊 Fármacos | ⚠️ **Depresión Respiratoria** → 🎯 el que mejor va pierde 1 ❤️ | 🔁 pareja | ámbar / mostaza · #c19a4e | *'¿Del uno al diez?' 'Quince.' Anotado: quince.* |
| **R16** | Radiografía de Tórax | 🩻 Imagen | — | 🔁 pareja | teal hospital neutro · #4a8a96 | *Rotada, penetrada y en espiración. Se informa igual.* |
| **R17** | Radiografía de Tórax | 🩻 Imagen | ⚠️ **Hallazgo Incidental** → 🎯 el estabilizado ✅ pierde 1 ❤️ | 🔁 pareja | teal hospital neutro · #4a8a96 | *Rotada, penetrada y en espiración. Se informa igual.* |
| **R18** | Ecografía a Pie de Cama | 🩻 Imagen | — | 🔁 pareja | teal hospital neutro · #4a8a96 | *Veo algo. No sé qué es, pero lo veo.* |
| **R19** | Ecografía a Pie de Cama | 🩻 Imagen | ⚠️ **Falso Positivo** → 🎯 el que mejor va pierde 1 ❤️ | 🔁 pareja | teal hospital neutro · #4a8a96 | *Veo algo. No sé qué es, pero lo veo.* |
| **R20** | TAC de Urgencia | 🩻 Imagen | — | 🔁 pareja | teal hospital neutro · #4a8a96 | *El traslado es más peligroso que la enfermedad. Vamos igual.* |
| **R21** | TAC de Urgencia | 🩻 Imagen | ⚠️ **Nefropatía por Contraste** → 🎯 este paciente pierde 1 ❤️ | 🔁 pareja | teal hospital neutro · #4a8a96 | *El traslado es más peligroso que la enfermedad. Vamos igual.* |
| **R22** | Angio-TAC | 🩻 Imagen | — |  | naranja quemado / rojo ladrillo · #e0705a | *Contraste, creatinina, y una fe enorme.* |
| **R23** | Resonancia con Cupo | 🩻 Imagen | — |  | púrpura / lavanda oscura · #a184c9 | *Existe. La han visto. Hay testigos.* |
| **R24** | Línea Arterial | 💉 Procedimientos | — | 🔁 pareja | teal hospital neutro · #4a8a96 | *Al quinto intento salió. Nadie mencionará los cuatro anteriores.* |
| **R25** | Línea Arterial | 💉 Procedimientos | ⚠️ **Isquemia Distal** → 🎯 tú eliges pierde 1 ❤️ | 🔁 pareja | teal hospital neutro · #4a8a96 | *Al quinto intento salió. Nadie mencionará los cuatro anteriores.* |
| **R26** | Catéter Venoso Central | 💉 Procedimientos | — | 🔁 pareja | teal hospital neutro · #4a8a96 | *Ecoguiado, estéril y con público.* |
| **R27** | Catéter Venoso Central | 💉 Procedimientos | ⚠️ **Bacteriemia por Catéter** → 🎯 este paciente pierde 1 ❤️ | 🔁 pareja | teal hospital neutro · #4a8a96 | *Ecoguiado, estéril y con público.* |
| **R29** | Reanimación | 💉 Procedimientos | — |  | teal hospital neutro · #4a8a96 | *El carro se revisó el martes. Por alguien. Supuestamente.* |
| **R30** | Ventilación Mecánica | 💉 Procedimientos | — | 🔁 pareja | teal hospital neutro · #4a8a96 | *Modo controlado. El paciente y el ventilador aún negocian.* |
| **R31** | Ventilación Mecánica | 💉 Procedimientos | ⚠️ **Neumonía Asociada a VM** → 🎯 este paciente pierde 1 ❤️ | 🔁 pareja | teal hospital neutro · #4a8a96 | *Modo controlado. El paciente y el ventilador aún negocian.* |
| **R32** | Gases Arteriales | 💉 Procedimientos | — | 🔁 pareja | verde oliva · #5cb583 | *pH 7.09. Alguien diga algo inteligente.* |
| **R33** | Gases Arteriales | 💉 Procedimientos | ⚠️ **Muestra Hemolizada** → 🎯 tú eliges pierde 1 ❤️ | 🔁 pareja | verde oliva · #5cb583 | *pH 7.09. Alguien diga algo inteligente.* |
| **R44** | Pleurostomía | 💉 Procedimientos | ⚠️ **Fuga Aérea Persistente** → 🎯 este paciente pierde 1 ❤️ |  | teal / azul hospital · #5b9dc4 | *Entre la cuarta y la quinta costilla. Por el borde superior. Por favor.* |
| **R45** | Punción Lumbar | 💉 Procedimientos | — |  | púrpura / lavanda oscura · #a184c9 | *Quédese quietito. Va a sentir un pinchazo... y una cefalea de tres días.* |
| **R34** | Enfermera de UCI | 🧑‍⚕️ Personal | 🛡️ previene *Bacteriemia por Catéter* |  | teal hospital neutro · #4a8a96 | *Sabe más que tú. Te lo dirá con mucha educación.* |
| **R35** | Técnico en Enfermería | 🧑‍⚕️ Personal | 🛡️ previene *Neumonía Asociada a VM* | 🔁 pareja | teal hospital neutro · #4a8a96 | *Sostiene la unidad entera. Y la camilla. Y al interno.* |
| **R36** | Técnico en Enfermería | 🧑‍⚕️ Personal | ⚠️ **El Turno Veinticuatro** → 🎯 el que mejor va pierde 1 ❤️ | 🔁 pareja | teal hospital neutro · #4a8a96 | *Sostiene la unidad entera. Y la camilla. Y al interno.* |
| **R37** | Interno Entusiasta | 🧑‍⚕️ Personal | — |  | teal hospital neutro · #4a8a96 | *Quiere aprender. Hoy. Ahora. Contigo.* |
| **R38** | Gestor de Camas | 🧑‍⚕️ Personal | ⚠️ **Presión de Camas** → 🎯 el que mejor va pierde 1 ❤️ |  | teal hospital neutro · #4a8a96 | *No trae camas. Trae preguntas sobre las camas.* |
| **R39** | Kinesiólogo Respiratorio | 🧑‍⚕️ Personal | 🛡️ previene *Delirium en UCI* |  | teal / azul hospital · #5b9dc4 | *Vino, aspiró, movilizó y se fue. Nadie sabe a dónde.* |
| **R40** | Pabellón Disponible | 🧑‍⚕️ Personal | — | 🔁 pareja | ámbar / mostaza · #c19a4e | *Hay pabellón. Hay equipo. Falta el anestesista.* |
| **R41** | Pabellón Disponible | 🧑‍⚕️ Personal | ⚠️ **Pabellón Suspendido** → 🎯 el que mejor va pierde 1 ❤️ | 🔁 pareja | ámbar / mostaza · #c19a4e | *Hay pabellón. Hay equipo. Falta el anestesista.* |
| **R42** | Médico General de Turno | 🃏 Comodín | 🃏 vale por cualquier tipo |  | teal hospital neutro · #4a8a96 | *No es su especialidad, pero es el que está. Siempre es el que está.* |
| **R43** | Stock de Sala | 🃏 Comodín | ⚠️ **La Gaveta Vacía** → 🎯 tu mano pierde 1 ❤️ |  | teal hospital neutro · #4a8a96 | *Lo que quedó en la gaveta. Sirve para algo. Para algo sirve.* |

### 5.3 Protocolos — las Acciones (20 diseños, 30 cartas)

**Plano:** escena mínima, una o dos figuras o un elemento en movimiento. Aquí
la paleta se suelta: las Acciones no tienen sistema clínico, así que pueden
usar un rango más amplio para distinguirse de pacientes y recursos.

- **ATAQUE:** conflicto: dos manos peleando por lo mismo, rivalidad de pasillo
- **APOYO:** cooperación: manos que entregan, alguien que llega a ayudar
- **CAOS:** desorden: objetos en el aire, todo pasando a la vez
- **RESPUESTA:** defensa: escudo, freno, el gesto de detener algo en el aire
- **EXTREMA:** sacrificio o superstición: el gesto más grande del mazo

| id | Carta | Tipo | Qué hace | La frase = la escena |
|---|---|---|---|---|
| **A01** | Vacaciones | ATAQUE | Elige un recurso 🧑‍⚕️ Personal colocado sobre un paciente rival y descártalo. | *Quince días hábiles. Aprobados por RR.HH. justo hoy.* |
| **A02** | Cumpleaños del Residente | ATAQUE | Cada rival elige uno de sus recursos en juego y te lo entrega. Colócalos sobre tus pacientes. | *Trajo torta para todos. Ahora todos le deben algo.* |
| **A03** | Reunión Clínica | APOYO | Redistribuye libremente hasta 3 recursos entre TUS pacientes. | *Dos horas para decidir lo que ya sabías al minuto cuatro.* |
| **A04** | Interconsulta | APOYO | Busca en la pila de descartes 1 carta de Recurso y colócala sobre un paciente tuyo. | *Respondió al cuarto día: 'sugiero evaluar'.* |
| **A05** | Doblo Turno | APOYO | Roba 3 cartas adicionales. En tu próximo turno robas solo 2. | *Me quedo. Total, ya estoy acá.* |
| **A06** | Se Cayó el Sistema | CAOS | Durante la próxima ronda completa, ningún jugador puede jugar cartas de Acción. | *Estamos trabajando en ello. Lleva tres años el cartel.* |
| **A07** | ¡Liceeeencia! | ATAQUE | Intercambia tu carta de avatar con la de un rival hasta el final de tu próximo turno. Las habilidades 1×PARTIDA ya gastadas siguen gastadas. | *Estrés laboral. Alguien tiene que cubrir el puesto. Ese alguien eres tú.* |
| **A08** | Llaman de Urgencias | ATAQUE | Un rival elige uno de sus pacientes. Ese paciente pierde 1 ❤️ adicional en su próximo Fin de Guardia. | *Urgencias tiene doce esperando. Doce.* |
| **A09** | Auditoría | ATAQUE | Mira la mano de un rival y descarta 1 carta de ella. | *Vengo a acompañar el proceso, no a fiscalizar. (Miente.)* |
| **A10** | Rotación de Internos | CAOS | Intercambia tu mano completa con la de un rival a tu elección. | *Nadie sabe quién rota a dónde. Ellos tampoco.* |
| **A11** | ¿Y Si Vamos por un Cafecito? | RESPUESTA | 🛡️ RESPUESTA — Juega fuera de turno. Anula una carta de Acción o una complicación ⚠️ que se acabe de resolver. | *Nadie sabe quién lo hizo ni cuándo. Está listo y está caliente.* |
| **A12** | Protocolo Institucional | APOYO | Copia el efecto de la última carta de Acción jugada en la partida, como si la jugaras tú. | *Está en la intranet. En un PDF. En una carpeta. En algún lado.* |
| **A13** | Anda Rondando la Pelada | EXTREMA | ÚNICA. Juégala solo si un rival tiene 2 o más ✝️. Lanza 2 monedas. Dos caras: elige un paciente de ese rival (aunque esté ✅) y dale el Alta Celestial de inmediato. Cualquier otro resultado: descarta toda tu mano. | *Pasó preguntando por la cama 4. Dijo que volvía al rato.* |
| **A14** | Ojo Clínico | APOYO | Mira las 3 primeras cartas del Mazo de Guardia. Devuélvelas en el orden que quieras o manda 1 al fondo. | *Yo a este paciente lo veo raro. No sé por qué. Lo veo raro.* |
| **A15** | Receta en Blanco | APOYO | Busca en el Mazo de Guardia 1 recurso a tu elección y ponlo en tu mano. Baraja el mazo. | *La firmó apurado, sin mirar. Que Dios reparta suerte.* |
| **A16** | Simulación Clínica | RESPUESTA | 🛡️ RESPUESTA — Juega fuera de turno. Anula una complicación ⚠️ antes de que se resuelva: el recurso se queda puesto sobre el paciente y no pasa nada más. | *Lo practicamos con el muñeco. El muñeco no se movía tanto.* |
| **A17** | Quiebre de Stock | ATAQUE | En su próximo turno, tu rival no puede colocar recursos 💊 Fármacos. | *Llega el jueves. Lleva tres jueves llegando.* |
| **A18** | Recorte Presupuestario | ATAQUE | En su próximo turno, tu rival roba 2 cartas menos. | *Hay que hacer más con menos. Otra vez menos.* |
| **A19** | Capacitación | APOYO | Elige un paciente tuyo: hasta tu próximo turno, sus recursos no pueden ser robados ni descartados por rivales. | *Ocho horas de PowerPoint. Algo quedó.* |
| **A20** | Hay Que Repetirlo | ATAQUE | Descarta un recurso 🩻 Imagen o 💉 Procedimientos de un paciente rival. | *Se tomó bien. Se rotuló bien. Se agitó como coctelera.* |

### 5.4 Personajes — los avatares (22 cartas)

**Plano:** cuerpo entero, pose característica, ocupando ~70% del cuadro.
Familia de color: **teal hospital neutro `#4a8a96`**, salvo que el personaje
pida otra cosa (el Esotérico y la Enfermera de Noche admiten nocturno).

Estos son los primeros que hay que dibujar: fijan cómo se ven las caras del
juego. Cada uno es un arquetipo que cualquiera que haya trabajado en un
hospital reconoce al tiro — **la habilidad dice qué hace y la frase dice cómo
es**. Dibuja la personalidad, no el uniforme.

| id | Avatar | Frecuencia | Habilidad | La frase = la escena |
|---|---|---|---|---|
| **C01** | El Diostor | 1×RONDA | Cuando colocas una carta ⚠️, puedes pasarle su complicación al jugador de tu derecha: la resuelve él sobre sus pacientes, como si la hubiera jugado. El recurso se queda igual sobre tu paciente. | *¿Yo, equivocarme? Imposible. Debe ser un error del laboratorio.* |
| **C02** | El Médico Fantasma | PASIVA | En las rondas 1 a 3 robas 1 carta menos. Desde la ronda 4 en adelante, robas 1 carta adicional cada turno por el resto de la guardia. | *Aló... sí, voy bajando. (Se da media vuelta en la residencia.)* |
| **C03** | Doctor Amor | 1×PARTIDA · PASIVA | SEDUCCIÓN DE PASILLO (1×PARTIDA) — Roba un recurso 🧑‍⚕️ Personal colocado sobre un paciente rival y colócalo sobre un paciente tuyo. REPUTACIÓN (PASIVA) — Los recursos 🧑‍⚕️ de tu unidad no pueden ser robados por rivales. | *Tus ojos brillan más que este laringoscopio. ¿Un café de máquina?* |
| **C04** | El Director del Hospital | 1×PARTIDA · PASIVA | PERDONAZO ADMINISTRATIVO (1×PARTIDA) — Anula y descarta un Sumario Administrativo, tuyo o de cualquier otro jugador. Puedes cobrar el favor. BUROCRACIA AMIGA (PASIVA) — Cerrar tus Sumarios te cuesta 1 carta en vez de 2. | *Haré unas llamadas para que esto no aparezca en los indicadores de calidad.* |
| **C05** | La Gestora de Camas | 1×PARTIDA | DERIVACIÓN — Devuelve un paciente tuyo al fondo del Mazo de Pacientes (sus recursos se descartan) y admite uno nuevo de inmediato. No cuenta como fallecido: no pones ✝️ ni restas sus puntos. Pero el papeleo es el mismo: toma un Sumario Administrativo, y esta guardia ya no puede cobrar ningún bonus de cierre. | *No hay cama en UCI. Se va a Intermedio... o a pasillo.* |
| **C06** | El Médico Esotérico | 1×TURNO | CONFÍA EN EL UNIVERSO — Descarta 1 carta de tu mano como ofrenda, luego revela la primera carta del Mazo de Guardia. Si es un recurso sin ⚠️: colócalo gratis sobre un paciente tuyo. Si trae ⚠️: colócalo gratis igual y resuelve su complicación. | *Tus chakras están bloqueando la vía venosa. Cuarzo rosa y sahumerio, stat.* |
| **C07** | La Enfermera de Noche | 1×PARTIDA | TURNO TRANQUILO — Descarta 2 cartas de tu mano: en este Fin de Guardia, ningún paciente de tu unidad pierde ❤️. | *Duerman tranquilos. Yo me quedo con las alarmas.* |
| **C08** | El Jefe de Servicio | 1×PARTIDA | FOTO PARA LA MEMORIA — Cuando das tu primera alta ✅ de la guardia, roba 1 carta. | *Excelente trabajo, equipo. Lo presento yo en la reunión.* |
| **C09** | La de Abastecimiento | PASIVA | BODEGA LLENA — Tus Canjes cuestan 1 recurso en vez de 2. | *Firma acá, acá y acá. Y me devuelves el lápiz.* |
| **C10** | El Dirigente Gremial | PASIVA | ASAMBLEA EXTRAORDINARIA — Cada vez que una Acción de ATAQUE rival te elige a ti o a un paciente de tu unidad, roba 1 carta. | *Compañeros, esto no se va a quedar así.* |
| **C11** | El Subespecialista | 1×TURNO | SUGIERO EVALUAR — Deja 1 recurso de tu mano boca abajo sobre esta carta. Al inicio de tu próximo Pase de Visita colócalo gratis sobre un paciente tuyo y cuenta doble (si no doblaba ya). | *Respondió al cuarto día. Pero qué respuesta.* |
| **C12** | La Enfermera de IAAS | PASIVA | VIGILANCIA EPIDEMIOLÓGICA — Cada 3 complicaciones ⚠️ que se resuelvan en tu unidad, roba 1 Protocolo gratis. | *No es magia. Es una planilla Excel con 14 pestañas.* |
| **C13** | El Residente Aplicado | PASIVA | PACIENTE EMBLEMA — El 4º recurso que coloques sobre un mismo paciente en un mismo turno cuenta doble. | *Me lo estudié anoche. Entero. Dos veces.* |
| **C14** | El Reanimador | 1×PARTIDA | MASAJE Y ADRENALINA — Cuando un paciente tuyo fuera a fallecer, no muere: queda con 1 ❤️ y pierde todos sus recursos colocados. | *No se me va. Hoy no. Carguen a 200.* |
| **C15** | El Dador de Altas | 1×PARTIDA | ALTA ADMINISTRATIVA — Descarta 2 cartas de tu mano: un paciente tuyo al que le falte exactamente 1 recurso completa sus requisitos (queda ✅ y consolida normal). | *Se va hoy. La cama la necesito para las tres.* |
| **C16** | El Radiólogo de Guardia | PASIVA | OJO ENTRENADO — Tus recursos 🩻 Imagen con sistema cuentan doble en cualquier paciente tuyo, no solo en los de su sistema. | *Interesante. Muy interesante. ¿Qué me dijiste que buscábamos?* |
| **C17** | El Multiuso | PASIVA | EL QUE HACE DE TODO — Empiezas la guardia con 1 Comodín 🃏 adicional en la mano. Tus comodines no pueden ser robados ni descartados por rivales. | *Yo cableo el monitor, destapo el baño y de paso tomo la presión.* |
| **C18** | La de la Buena Muñeca | PASIVA | AL PRIMER INTENTO — Al final de tu Entrega de Turno, puedes devolver 1 carta de tu mano al fondo del Mazo de Guardia y robar 1 de reemplazo. | *Vena difícil no existe. Existe poca fe.* |
| **C19** | El Intensivista | PASIVA | A MÍ NO ME ASUSTA — Tus pacientes de Gravedad III entran a tu unidad con +1 ❤️. | *Grave lo veo yo. Esto es un martes normal.* |
| **C20** | El Carroñero de Pasillo | PASIVA | JUSTO PASABA POR AHÍ — Cada vez que un rival pone un ✝️, roba 1 carta al azar de su mano. | *Lamento tu pérdida. ¿Vas a ocupar ese monitor?* |
| **C21** | El Precavido | 1×PARTIDA | POR SI ACASO — Busca en el Mazo de Protocolos una carta RESPUESTA 🛡️, muéstrala y tómala gratis. Baraja el mazo. | *Yo esto lo vi venir en marzo. Está en mi correo.* |
| **C22** | La Jefa de Unidad | PASIVA | CUMPLIMIENTO DE METAS — Los recursos 🧑‍⚕️ de tu unidad no pueden ser descartados por cartas de rivales. | *Mi gente no se toca. Las estadísticas tampoco.* |

### 5.5 El Sumario Administrativo (1 diseño, 6 cartas)

La única carta que no se juega: te llega. **Es el mejor chiste del juego** y
la carta que más miedo tiene que dar — más que la muerte, que en este juego se
llama "Alta Celestial" y se dibuja con humor suave.

| id | Carta | Qué hace | La frase = la escena |
|---|---|---|---|
| **S01** | Sumario Administrativo | Recíbela cuando un paciente tuyo recibe el Alta Celestial. Queda en tu mano: no se puede jugar ni descartar y reduce tu límite de mano en 1. Para cerrarlo, descarta 2 recursos de tu mano en tu Pase de Visita — o convence al Director del Hospital. | *Todo lo que diga podrá ser usado en su contra en la auditoría de calidad.* |

---

## 6. Resumen para el que va a dibujar

0. **Pide las imágenes de referencia** (§4.5) antes de empezar. Con este
   archivo solo tienes las palabras; con dos o tres anclas tienes el estilo.
1. **El estilo ya existe** (§4.1): línea gruesa uniforme, color plano, una
   sola familia de color por imagen, cabezones cansados, a sangre completa.
2. **Compón para el tercio central** (§3): la maqueta recorta.
3. **La frase de cada carta es el brief de escena.** Está en la columna
   final de todas las tablas de §5.
4. **Los pacientes tienen dignidad; el ridículo es de la situación** (§1.3).
5. **Nombra los archivos con el id de la carta.**
6. **Empieza por los 22 personajes**, que fijan las caras.

Total del encargo: **113 ilustraciones** — 26 pacientes, 44 recursos, 20
Acciones, 22 personajes, 1 Sumario.
