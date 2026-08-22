# ¡VAYA TURNO! — Reglamento v0.21 (playtest)

> Juego de cartas para **2–4 médicos** · **30–45 min** · a partir de 14 años
> (y de una tolerancia razonable al humor de pasillo)

---

## 1. La idea en 30 segundos

Cada jugador dirige una **UCI de 3 camas**. Los pacientes llegan solos, se
deterioran solos y **no esperan**. Para salvarlos necesitas cuatro cosas que
nunca hay al mismo tiempo: **imágenes, fármacos, personal y monitoreo**.

No vas a poder salvarlos a todos. Ese no es un defecto del juego: **eso es
triage**. Elige a quién salvas, deja morir al resto con dignidad, y —
mientras tanto — mándale al colega de al lado a su enfermera de vacaciones
justo antes de que dé un alta.

Gana quien tenga **más puntos** al terminar la guardia.

---

## 2. Componentes

| Componente | Cant. | Nota |
|---|---:|---|
| Cartas de **Personaje** | 6 | Un médico por jugador |
| Cartas de **Paciente** | 26 | Gravedad I, II, III y Código Rojo |
| Cartas de **Recurso** | 65 | El **Mazo de Guardia**: 🩻 Imagen · 💊 Fármacos · 🧑‍⚕️ Personal · 💉 Procedimientos · 🃏 Comodín |
| Cartas de **Protocolo** (Acciones) | 30 | Mazo aparte. Se compran con el **Canje** |
| Cartas de **Sumario Administrativo** | 6 | La maldición. Llega sola, cuesta salir |
| Fichas de **Vida** (❤️) | ~60 | Cubos, monedas o un dial por cama |
| Fichas de **Estabilizado** (✅) | 12 | 3 por jugador |
| Fichas de **Cruz** (✝️) | 20 | Marcan las Altas Celestiales |
| **Moneda** | 1 | Para la Pelada. Cualquier moneda sirve |
| **Marcador de Ronda** | 1 | Pista de 10 rondas |

> Con los CSV de `cartas/` y `tools/generar_pnp.py` tienes un print-and-play
> listo para imprimir. Ver `cartas/README.md`.

---

## 3. Preparación

1. Cada jugador elige un **Personaje** y lo pone frente a sí. Deja espacio
   para **3 camas** debajo.
2. Baraja el **Mazo de Pacientes**. Cada jugador **admite 3 pacientes**
   (ver §5.1, *Entrega de Turno*) y les pone las fichas ❤️ que indique la carta.
   Terminado el reparto, **da vuelta la primera carta del mazo**: es el
   *Informe de Gestión de Camas* y se queda boca arriba toda la partida.
3. Baraja el **Mazo de Guardia** (los 65 Recursos, con sus 18 ⚠️ adentro).
   Baraja aparte el **Mazo de Protocolos** (las 30 Acciones).
4. Cada jugador roba **4 cartas** de mano inicial.
5. Empieza quien haya hecho el turno de noche más reciente. Si nadie lo
   admite, quien tenga las manos más frías.

**Ajuste por número de jugadores:**

| Jugadores | Camas c/u | Robo por turno | Rondas | Nota |
|---|---:|---:|---:|---|
| 2 | 3 | 4 | 8 | Los ataques duelen el doble. Es a propósito. |
| 3 | 3 | 4 | 8 | **Configuración recomendada** |
| 4 | 2 | **3** | 10 | Menos camas y menos robo: los turnos vuelan |

> Estos números están simulados, no improvisados. Con ellos un jugador
> competente salva ~67% de sus pacientes: unas **3,0 altas y 1,5
> fallecidos** por guardia, salva al **40% de los Gravedad III** y cierra
> "Se hizo todo" una de cada cuatro veces. Si tu mesa se aleja mucho de
> eso, revisa `docs/DISENO.md` §4 antes de cambiar nada.

---

## 4. Los pacientes

Cada carta de paciente tiene:

```
┌─────────────────────────────┐
│  SHOCK SÉPTICO       ❤️ 6   │   ← Vida inicial
│  Gravedad III   🫀 CARDÍACO │   ← Sistema (ver §4.1)
│  ─────────────────────────  │
│  Requiere:                  │
│   🩻 ×1   💊 ×4             │   ← Lo que necesita para estabilizarse
│   💉 ×2   🧑‍⚕️ ×1             │
│  ─────────────────────────  │
│  Alta: +6      Fallece: −2  │
│  "La hora dorada empezó     │
│   hace cuatro horas."       │
└─────────────────────────────┘
```

| Gravedad | ❤️ | Recursos | Alta | Fallece |
|---|---:|---:|---:|---:|
| **I — Observación** | 7 | 3 | **+2** | −1 |
| **II — Grave** | 6 | 5 | **+3** | −2 |
| **III — Crítico** | 6 | 8 | **+6** | −2 |
| **★ Código Rojo** | 5 | 8 | **+8** | −3 |

Los recursos se colocan **encima de la carta del paciente**, en abanico, y
se quedan ahí. No son gastables: **son su tratamiento**.

> **La tabla no es arbitraria: es la fórmula.** En los cuatro casos
> `alta + |fallece| = recursos que pide`. Cada punto de swing cuesta
> exactamente un recurso, y la **vida es el plazo, no el precio**: el
> Gravedad III no es caro, es *urgente*. La única excepción deliberada es el
> Código Rojo, que paga 11 de swing por 8 de precio — una prima del 37% por
> aceptar el peor plazo del juego. Todo esto está en `docs/ECONOMIA.md`.

### El sistema del paciente

Cada paciente pertenece a un **sistema clínico**, marcado con un chip de color:

🫁 **Respiratorio** · 🫀 **Cardíaco** · 🧠 **Neurológico** · 🧪 **Metabólico** · 🔪 **Quirúrgico**

Eso importa por una sola regla, la de §4.1.

### 4.1 Recursos específicos: la sinergia

21 de las 65 cartas del Mazo de Guardia llevan también un chip de sistema.

> **Un recurso específico jugado sobre un paciente de su mismo sistema
> cuenta como DOS recursos de su tipo, en vez de uno.**

Un *Broncodilatador* 🫁 sobre una Neumonía cuenta como 💊×2. Sobre un Shock
Séptico cuenta como 💊×1, y sirve igual — solo que sin el premio.

No hay sumas ni valores: sigues contando íconos, algunos valen por dos.

> La decisión que esto abre es la buena: **¿quemo el broncodilatador en el
> cardíaco que se me está yendo ahora, o lo guardo por si llega un
> respiratorio?**

### 4.2 Comodines

Tres cartas del mazo son 🃏 **Comodín** (*Médico General de Turno*, *Stock de
Sala*). Cuentan como **1 recurso del tipo que tú elijas** al colocarlas.
Nunca cuentan doble. Son escasas a propósito: existen para que nadie se quede
con la mano muerta, no para resolverte la partida.

### 4.3 Recursos con restricción

Dos cartas cuestan algo más que una jugada:

| Carta | Restricción |
|---|---|
| **TAC de Urgencia** | Solo puedes jugarlo sobre un paciente que ya tenga al menos 1 🧑‍⚕️. Alguien tiene que bajarlo. |
| **Resonancia con Cupo** | Al jugarla, **termina tu Pase de Visita**: no colocas más recursos ni cierras Sumarios este turno. Cuesta tiempo, no recursos. |

---

## 5. El turno

Un turno son **cuatro fases**, en este orden. Una **ronda** son los turnos de
todos los jugadores, y **cada Fin de Guardia es un día que pasa**.

```
 ENTREGA DE TURNO  →  EL PASILLO  →  PASE DE VISITA  →  FIN DE GUARDIA
   recibes             negocias         tratas            pasa el día
```

### 5.1 Entrega de Turno

Llegas, te cuentan cómo está la unidad y agarras el carro.

**a) Altas.** Da de alta a **todo paciente que ya llevara la ficha ✅ antes de
que empezara este turno**. Sobrevivió la ronda de consolidación: ponlo en tu
**pila de altas** y anota sus puntos. Sus recursos van al descarte y la cama
queda vacía.

En corto: **estabilizas en un turno, das de alta en el siguiente.** Entre medio
pasan los turnos de todos los demás, y ahí es donde te lo pueden arruinar.

> **Por qué existe esta espera:** completar los recursos no es ganar todavía.
> Hay una ronda entera en la que tu paciente estabilizado está a la vista de
> todos, sin perder vida pero perfectamente saboteable. Ahí es donde se rompen
> las amistades.

**b) Admisión (opcional desde v0.20).** Por cada **cama vacía puedes** revelar
las **2 primeras cartas** del Mazo de Pacientes, **elegir 1** y poner la otra
**al fondo del mazo** — o **dejar la cama vacía**. Decides cama por cama.
Coloca las fichas ❤️ que indique la carta.

> **Informe de Gestión de Camas (v0.21).** La **primera carta del Mazo de
> Pacientes está siempre boca arriba**, junto al mazo, desde la preparación.
> Es una de las dos que revelarías. Así decides si admites **sabiendo al menos
> la mitad de lo que te va a tocar**, igual que en un hospital de verdad: la
> lista de espera de urgencias no es secreta. Cuando alguien admite, se
> resuelve la elección y se **da vuelta la nueva primera carta**.
>
> No cuesta cartas ni reglas nuevas, y convierte «¿admito?» en una decisión
> informada en vez de una apuesta.

> **Pero la cama vacía se cobra:** en cada Fin de Guardia, **cada cama vacía
> te resta 1 punto** (§5.4). Hay doce esperando en urgencias y todo el
> hospital sabe que tienes una cama libre. Rechazar un ingreso es una decisión
> clínica legítima — negarse a trabajar, no. La medición está en
> `DISENO.md` §4i: el que nunca admite termina con puntaje negativo.

**c) Robo.** Roba **4 cartas** del Mazo de Guardia (**3** en partidas de 4
jugadores).

Robar una carta **⚠️ Complicación no hace nada**: entra a tu mano como un
recurso más. Su complicación se resuelve **al colocarla** sobre un paciente
(§7). Nadie más tiene por qué saber lo que llevas en la mano.

Si el Mazo de Guardia se agota, baraja el descarte y forma uno nuevo.

### 5.2 El Pasillo

Antes de la visita, en el pasillo, se arregla lo que no se puede decir en la
reunión. Aquí pasan las dos cosas turbias del juego:

- **El Negocio** (máx. 1 por turno). La ventanilla del pasillo tiene un solo
  cupo, y eliges con quién tratas:
  - **Canje** (con el mazo): descarta **2 recursos** de tu mano, **roba 2
    cartas del Mazo de Protocolos, quédate 1** y pon la otra bajo el mazo.
    Así se consiguen las Acciones: cambiando lo que te sobra por un favor.
    Pagas con azar acotado: no sabes qué
    Protocolo te va a tocar.
  - **Trueque** (con un colega): ofrece **2 recursos de tu mano** a un rival y
    pide **un tipo** de recurso (🩻, 💊, 🧑‍⚕️ o 💉). Si acepta, te entrega
    **1 carta de ese tipo de su mano** — él elige cuál, tú no ves su mano — y
    se queda tus 2. Puede negarse, y si nadie acepta no pierdes nada: aún
    puedes hacer el Canje. Pagas con política: le acabas de regalar ventaja
    a un rival, y toda la mesa lo vio.
  - **El Negocio no es una Acción**: puedes negociar aunque no puedas jugar
    Acciones (*Se Cayó el Sistema*), y negociar no gasta tu Acción del turno.
- **Acciones:** juega **como máximo 1 por turno** — puede ser la que acabas de
  canjear. Cuestan 0: ya pagaste al conseguirla. Resuelve su texto y descártala.

> El límite de 1 es de veneno, no de trabajo clínico. Podrás tratar a tus
> pacientes todo lo que te dé la mano en la fase siguiente; arruinarle el turno
> al colega, una vez.

> *En el pasillo nadie regala nada. Pero todo tiene precio.* El Trueque es a
> propósito un mal negocio en cartas (das 2, recibes 1) y un buen negocio en
> precisión: recibes exactamente el tipo que te falta, hoy. La pregunta de la
> mesa no es "¿me conviene?" — es "**¿a quién estoy engordando?**".

**Por qué el pasillo va antes de la visita:** porque lo que consigas acá —una
*Receta en Blanco*, un recurso que le quitaste a un rival, tres cartas de
*Doblo Turno*— lo puedes usar **este mismo turno** en el Pase de Visita. Y
porque el Canje te obliga a decidir qué te sobra **antes** de haber tratado a
nadie, que es la decisión difícil.

### 5.3 Pase de Visita

La reunión. Cama por cama, se indica el tratamiento.

- **Recursos:** coloca **hasta 3 por turno** (v0.20), **encima de tus**
  pacientes, en abanico. No son gastables: son su tratamiento. El día no da
  para más: elegir cuáles 3 —y quién espera a mañana— es el trabajo.
- **Cerrar Sumarios:** descarta 2 recursos por cada Sumario que quieras cerrar.

En cuanto un paciente tiene **todos** los recursos que pide (da igual si le
sobran de un tipo), colócale una ficha **✅ Estabilizado**. Deja de perder vida
de inmediato, incluso a mitad de fase.

> **Importante:** si un paciente ✅ pierde un recurso por cualquier motivo y
> deja de cumplir sus requisitos, **pierde la ficha ✅ al instante** y vuelve a
> deteriorarse en el siguiente Fin de Guardia. Los recursos sobrantes sirven de
> colchón.

### 5.4 Fin de Guardia

**Pasa un día.** Esta es la fase que hace que el juego sea un juego.

**a) Deterioro.** Cada paciente en tu UCI que **no** esté ✅ Estabilizado pierde
**1 ❤️**. Sin excepciones: el que ingresó hoy también vio pasar el día.

**b) Alta Celestial.** Si un paciente llega a **0 ❤️**, se le cursó el alta
hacia el piso que está sobre las nubes. Descarta la carta y todos sus recursos,
pon una ✝️ frente a ti y anota su penalización.

**La cama queda vacía hasta tu próxima Entrega de Turno.** Pasa una ronda
entera con un hueco en tu unidad: perder un paciente no solo cuesta puntos,
cuesta también el turno de trabajo que esa cama no te va a dar.

Esto vale para **cualquier** Alta Celestial, la cause el reloj, un Evento
una complicación ⚠️ o la Pelada: siempre ✝️, siempre Sumario.

**Y llega el papeleo:** toma una carta de **Sumario Administrativo**. Queda en
tu mano, no se puede jugar ni descartar, y **reduce tu límite de mano en 1**.
Para cerrarlo: en tu Pase de Visita, descarta 2 recursos — o consigue que el
Director del Hospital haga desaparecer el expediente.

> Lo peor de perder un paciente no es perder los puntos. Es el formulario.

**b2) La cama vacía se cobra.** Por **cada cama vacía** en tu unidad al cerrar
este Fin de Guardia, **anota −1 punto** (no aplica en la última ronda: la
guardia ya terminó). Da igual por qué está vacía — duelo, estrategia o pereza:
el servicio factura igual.

**c) Descarte.** Quédate con un máximo de **5 cartas** en mano (**menos 1 por
cada Sumario abierto**). Pasa el turno.

> **La última ronda.** Lo último que pasa en la partida es un Fin de Guardia:
> tus pacientes no-✅ pierden su ❤️ igual, y los que estén en 1 ❤️ se mueren
> con el juego ya terminado. Por eso **estabilizar en la ronda final sigue
> valiendo la pena aunque no alcances a dar el alta**: no ganas los puntos,
> pero te ahorras la ✝️ y el Sumario no llega a tiempo de estorbarte. Es la
> decisión más contraintuitiva del juego y la que separa a las mesas.

> **Por qué el deterioro va al final y no al principio.** Porque el reloj es el
> día, no tu llegada: si el paciente se te va, se te va **después** de que
> hiciste todo lo que podías hacer hoy. Un paciente en 1 ❤️ es un paciente al
> que **alcanzas a intentar salvar** — y si no lo logras, la muerte es
> consecuencia de tu turno, no algo que pasó mientras dormías. Cuesta caro: es
> medio turno de gracia para todo el mundo, y por eso el Código Rojo tiene
> ❤️5 y el recién ingresado ya no tiene día de cortesía.

### 5.5 Lo que se pregunta en la mesa

| Situación | Respuesta |
|---|---|
| ¿Se agotó el **Mazo de Pacientes**? | No se admite a nadie más. Las camas vacías quedan vacías y la guardia termina **al final de la ronda en curso**. |
| ¿Se agotaron los **Sumarios** (son 6)? | No tomas ninguno. Tuviste suerte: la impresora estaba mala. |
| ¿Puedo dejar una cama vacía a propósito? | No en la Entrega de Turno: si hay cama y hay mazo, admites. Sí durante el resto de la ronda, cuando el hueco lo dejó una muerte. |
| ¿Puedo cerrar un Sumario el mismo turno que lo recibo? | No. Llega en tu Fin de Guardia; lo pagas en tu próximo Pase de Visita. |
| ¿Un paciente ✅ puede recibir más recursos? | Sí, y conviene: los sobrantes son el colchón que aguanta un ataque. |
| ¿Puedo mover un recurso de un paciente a otro? | Solo si una carta lo dice (*Reunión Clínica*). Por defecto, lo puesto queda puesto. |
| ¿Los pacientes que quedan en cama al final puntúan? | No. Ni bien ni mal. Quedan para la próxima guardia. |
| ¿Y si un efecto sube los requisitos de un paciente ya ✅? | Pierde el ✅ al instante si deja de cumplirlos, y vuelve a deteriorarse en tu siguiente Fin de Guardia. |
| ¿El 🎯 Objetivo de una complicación puede señalar a un paciente ✅? | Sí, y suele ser lo peor que te pasa: si el golpe le quita vida o recursos, puede perder la ficha. Solo *EL ESTABILIZADO* lo busca a propósito. |
| ¿Cómo cuento "el más tratado"? | **Cartas de recurso encima**, no íconos. Un recurso específico que cuenta doble sigue siendo **una** carta. |

---

## 6. Fuera de turno

Solo dos cosas se pueden hacer cuando no es tu turno:

1. **Jugar una carta marcada 🛡️ RESPUESTA** (ej.: *¿Y Si Vamos por un Cafecito?*).
   No cuenta como tu Acción del turno.
2. **Usar una habilidad de Personaje que diga explícitamente que se puede.**

Las cartas 🛡️ se resuelven **antes** que la carta que están respondiendo, y
pueden encadenarse (una 🛡️ puede anular otra 🛡️).

**Regla de oro de las discusiones:** si la mesa no se pone de acuerdo en cómo
se resuelve algo, la interpretación que **más perjudique al jugador que va
ganando** es la correcta. Ha funcionado en comités clínicos durante décadas.

---

## 7. Las Complicaciones ⚠️

**No hay mazo de eventos.** Cada carta marcada con ⚠️ **trae su propia
complicación impresa**, y es siempre la complicación que ese recurso causa de
verdad: la Ventilación Mecánica trae la neumonía asociada a ventilación
mecánica, el catéter trae la bacteriemia, el antibiótico trae la resistencia.

> **Toda complicación hace lo mismo: el paciente señalado pierde 1 ❤️.**
> Una sola regla para las dieciocho (v0.21). Lo que cambia de una a otra es
> **a quién le pega** —su 🎯 Objetivo— y cómo se llama. La única excepción la
> dice su propia carta: *La Gaveta Vacía*, que no es una complicación clínica
> sino de bodega, y te hace descartar de la mano.

> **La complicación se dispara al COLOCAR la carta sobre un paciente**, no al
> robarla. Robarla no hace nada: es un recurso más en tu mano. En el momento
> en que la pones sobre una cama, el recurso surte efecto **y** resuelves su
> complicación de inmediato, en ese orden.

Son **18 cartas de las 65** del Mazo de Guardia: una de cada cuatro que robas.

**Por qué al jugarla y no al robarla.** Por tres motivos, en orden de peso:

1. **Es auditable.** Robar es un acto privado: si la complicación se disparara
   al robar, bastaría con callarse. Colocar una carta es un acto público, boca
   arriba, delante de todos. La regla se hace cumplir sola.
2. **Es verdad.** Un ventilador que nunca conectaste no puede dar una neumonía
   asociada a ventilación mecánica.
3. **Es una decisión.** Deja de ser un impuesto y pasa a ser la pregunta que se
   hace de verdad en una UCI: *¿lo necesito lo suficiente como para aceptar lo
   que trae?* A veces sí — tienes otro 🧑‍⚕️ en la mano y puedes pagar el
   requisito extra. A veces conviene esperar la carta limpia.

**Dos precisiones que van a salir en la mesa:**

- **Descartar una ⚠️ no dispara nada.** Si la botas en el cierre de turno, si
  te la roban de la mano o si la entregas en un Trueque, la complicación no
  ocurre. Solo cuenta colocarla sobre un paciente.
- **Si vuelve del descarte, vuelve a disparar.** Una carta ⚠️ rescatada con
  *Interconsulta* (A04) resuelve su complicación otra vez al colocarla. No hay
  cartas ⚠️ "ya gastadas": el riesgo viaja con la carta, siempre.

> **En el Trueque, ojo.** El rival elige qué carta te entrega y tú no ves su
> mano (§5.2). Si le pides un 💉 y tiene la pleurostomía con fuga aérea,
> adivina cuál te va a pasar.

### 7.1 A quién le pasa: el 🎯 Objetivo

**La carta elige a la víctima, no tú.** Cada complicación lleva un 🎯 Objetivo
que dice a cuál de tus pacientes le toca:

| 🎯 Objetivo | A quién señala |
|---|---|
| **ESTE PACIENTE** | El paciente sobre el que **acabas de colocar la carta**. La complicación es del procedimiento mismo: le pasa a quien se lo hiciste |
| **EL QUE MEJOR VA** | El que tenga **más ❤️** en este momento |
| **EL ESTABILIZADO ✅** | Tu paciente con ficha ✅. Si no tienes ninguno, va **al que mejor va** |
| **TÚ ELIGES** | Eliges tú. Son solo dos: la muestra perdida y la línea que hubo que retirar no discriminan |
| **TU MANO** | No toca ninguna cama: descartas una carta de tu mano. Solo el *Stock de Sala* |

**En caso de empate, eliges tú entre los empatados.** Es la única decisión que
te queda, y a veces es la que importa.

> **Por qué la carta decide.** Si eligieras libremente, mandarías siempre el
> daño al paciente que ya diste por perdido y ninguna complicación dolería.
> Y fíjate hacia dónde apuntan: **once de las dieciocho buscan al que iba
> bien** o al que ya tenía su ✅, y **cuatro más golpean exactamente al
> paciente que acabas de tratar**. Eso no es casualidad — es la tesis del
> juego. Lo que se complica en una UCI no es lo que ya estaba perdido: es lo
> que parecía resuelto, o lo que tú mismo acabas de tocar.
>
> Las cuatro de 🎯 ESTE PACIENTE son las de causalidad directa: la NAVM le da
> al que ventilaste, la bacteriemia al del catéter, la fuga aérea al de la
> pleurostomía, la nefropatía al que pasó por el TAC. Los errores de sistema
> — el fármaco equivocado, el turno de 24 horas, el pabellón caído — siguen
> golpeando lejos, porque así funcionan: el error de medicación no elige al
> paciente que lo motivó.

Si **no tienes ningún paciente en cama**, no pasa nada. Y si el objetivo está
**protegido** por un 🛡️ que nombra esa complicación (§7.3), tampoco: no se
sustituye por otro efecto ni se busca otro objetivo.

> **Por qué las dieciocho hacen lo mismo.** Hasta v0.20 había tres familias
> —quitar ❤️, subir un requisito, descartar un recurso— y las seis que
> descartaban **fallaban entre el 74% y el 86% de las veces**, porque el
> paciente señalado casi nunca tenía puesto justo ese recurso. Una de cada
> cuatro ⚠️ era teatro: dabas vuelta la carta, leías el nombre, buscabas la
> víctima y no pasaba nada. Hoy **el 99% resuelve**, y el 1% que no es un 🛡️
> haciendo su trabajo. La variedad se mudó donde no puede fallar: los
> nombres, los dibujos y el 🎯.

### 7.2 Las dieciocho

**Todas quitan 1 ❤️ al paciente que señala su 🎯** (salvo la última, que va a
tu mano). Se leen de corrido:

| Carta ⚠️ | Complicación | 🎯 |
|---|---|---|
| Antibiótico de Amplio Espectro | Resistencia Antibiótica | ✅ ESTABILIZADO |
| Sedoanalgesia | Delirium en UCI | EL QUE MEJOR VA |
| Anticoagulación | Sangrado | EL QUE MEJOR VA |
| Noradrenalina | Taquicardia Ventricular | EL QUE MEJOR VA |
| Anticonvulsivante | Sobresedación | ✅ ESTABILIZADO |
| Analgesia Postoperatoria | Depresión Respiratoria | EL QUE MEJOR VA |
| Radiografía de Tórax | Hallazgo Incidental | ✅ ESTABILIZADO |
| Ecografía a Pie de Cama | Falso Positivo | EL QUE MEJOR VA |
| TAC de Urgencia | Nefropatía por Contraste | **ESTE PACIENTE** |
| Línea Arterial | Isquemia Distal | TÚ ELIGES |
| Catéter Venoso Central | Bacteriemia por Catéter | **ESTE PACIENTE** |
| **Ventilación Mecánica** | **Neumonía Asociada a VM** | **ESTE PACIENTE** |
| Gases Arteriales | Muestra Hemolizada | TÚ ELIGES |
| Pleurostomía | Fuga Aérea Persistente | **ESTE PACIENTE** |
| Técnico en Enfermería | El Turno Veinticuatro | EL QUE MEJOR VA |
| Gestor de Camas | Presión de Camas | EL QUE MEJOR VA |
| Pabellón Disponible | Pabellón Suspendido | EL QUE MEJOR VA |
| Stock de Sala | La Gaveta Vacía | TU MANO |

> Nota el contraste: el ventilador daña **al que ventilaste**, pero *El Turno
> Veinticuatro* golpea **al que iba mejor aunque hayas puesto al técnico en
> otra cama** — el error aparece justo donde nadie estaba mirando. Esa es la
> diferencia entre una complicación del procedimiento y un error de sistema.

### 7.3 Las Protecciones 🛡️ (v0.20)

Algunos recursos 🧑‍⚕️ Personal traen un texto **🛡️ PREVIENE** con el nombre de
una complicación. Mientras ese Personal **siga sobre el paciente**, la
complicación nombrada **no puede ocurrirle a ese paciente**: si una ⚠️ la
señalara, simplemente no ocurre (no se sustituye ni busca otro objetivo).

| Protector 🛡️ | Previene | El bundle |
|---|---|---|
| **Técnico en Enfermería** | Neumonía Asociada a VM | Cabecera a 30° y aseo de cavidades |
| **Enfermera de UCI** | Bacteriemia por Catéter | Manejo estéril del catéter |
| **Kinesiólogo Respiratorio** | Delirium en UCI | Movilización precoz |

> Los tres son bundles reales, y por eso las protecciones enseñan algo: quien
> juega el TENS antes de intubar está haciendo lo mismo que se hace en una UCI
> de verdad.

Tres reglas cortas:

1. **La prevención es prospectiva.** El protector debe estar colocado **antes**
   de que la complicación se resuelva. Llegar después no revierte nada: la
   complicación ya resuelta es historia. Proteger ANTES del procedimiento
   invasivo — kinesiólogo primero, ventilador después — es la secuencia
   correcta, aquí y en la vida real.
2. **La protección viaja con la carta.** Si el protector deja la cama (robado,
   descartado), la protección se va con él.
3. **El gemelo cansado no previene.** El *Técnico en Enfermería* ⚠️ (El Turno
   Veinticuatro) es el mismo cargo en otro estado: no trae 🛡️. Lee la carta.

---

## 8. Los personajes

La fauna hospitalaria completa: **22 avatares**. Cada uno tiene **una**
habilidad con su frecuencia de uso; los de 1×PARTIDA giran la carta 90° al
usarla.

**Reparto (v0.19):** con la plantilla ampliada, ya no se asigna uno al azar —
**reparte 2 avatares a cada jugador y que cada uno se quede con 1**,
devolviendo el otro a la caja. El pequeño draft absorbe las diferencias de
poder y deja que cada uno juegue con un estilo que eligió.

### 8.1 Dónde aplica cada habilidad: el alcance

Toda habilidad dice explícitamente su alcance, con dos palabras fijas:

| Alcance | Significa |
|---|---|
| **este paciente** | Solo el paciente afectado por esa condición |
| **tu unidad** | Todas tus camas (y tus recursos colocados en ellas) |

Si una habilidad resuelve algo de otros pacientes o de otros jugadores, lo
dice explícito en la carta. Nada aplica más allá de lo que su texto nombra.

### 8.2 Los veintidós

Los textos completos van en las cartas; esta tabla es el índice. La columna
**Δ** es la ventaja medida con el método de `DISENO.md` §4b (banda sana:
+0,3 a +1,0); «mesa» significa que la habilidad usa piezas que el simulador
no modela (Acciones, Canje, rivales) y se calibra en playtest.

| Personaje | Frecuencia | Habilidad (resumen) | Δ |
|---|---|---|---|
| **El Diostor** | 1×RONDA | Al colocar una ⚠️, pásale la complicación al jugador de tu derecha; el recurso se queda en tu paciente | mesa · al alza con v0.17 |
| **El Médico Fantasma** | PASIVA | Rondas 1–3 robas 1 menos; desde la 4, robas 1 más | mesa |
| **Doctor Amor** | 1×PARTIDA · PASIVA | Roba un 🧑‍⚕️ rival · tus 🧑‍⚕️ no pueden ser robados | mesa |
| **El Director del Hospital** | 1×PARTIDA · PASIVA | Anula un Sumario de cualquiera · cerrar tus Sumarios cuesta 1 carta | mesa |
| **La Gestora de Camas** | 1×PARTIDA | Deriva un paciente sin ✝️; toma un Sumario y pierdes los bonus de cierre | **+0,7** ✅ v0.13 |
| **El Médico Esotérico** | 1×TURNO | Descarta 1 carta como ofrenda y revela: sin ⚠️ entra gratis; con ⚠️ entra gratis y resuelves | mesa |
| **La Enfermera de Noche** | 1×PARTIDA | Descarta 2: un Fin de Guardia sin deterioro en tu unidad | **+0,67** ✅ |
| **El Jefe de Servicio** | 1×PARTIDA | Tu primera alta ✅ te da 1 carta | **+0,79** ✅ |
| **La de Abastecimiento** | PASIVA | Tus Canjes cuestan 1 recurso en vez de 2 | mesa |
| **El Dirigente Gremial** | PASIVA | Acción de ATAQUE contra tu unidad → robas 1 carta | mesa |
| **El Subespecialista** | 1×TURNO | Congela 1 recurso boca abajo; al próximo turno entra gratis y cuenta doble | **+0,41** ✅ |
| **La Enfermera de IAAS** | PASIVA | Cada 3 ⚠️ resueltas en tu unidad, roba 1 Protocolo gratis | mesa |
| **El Residente Aplicado** | PASIVA | El 4º recurso sobre un mismo paciente en un turno cuenta doble | **+0,41** ✅ |
| **El Reanimador** | 1×PARTIDA | Un paciente tuyo que fallecería queda en 1 ❤️ y pierde sus recursos | **+0,30** ✅ |
| **El Dador de Altas** | 1×PARTIDA | Descarta 2: un paciente al que le falte 1 recurso queda ✅ | **+0,70** ✅ |
| **El Radiólogo de Guardia** | PASIVA | Tus 🩻 con sistema cuentan doble en cualquier paciente tuyo | **+0,48** ✅ |
| **El Multiuso** | PASIVA | +1 Comodín inicial; tus comodines son intocables | **+1,09** 🔶 caliente |
| **La de la Buena Muñeca** | PASIVA | Tras robar, devuelve 1 carta al fondo y roba reemplazo | **+0,59** ✅ |
| **El Intensivista** | PASIVA | Tus Gravedad III entran con +1 ❤️ | **+0,97** ✅ |
| **El Carroñero de Pasillo** | PASIVA | Rival pone ✝️ → robas 1 carta al azar de su mano | mesa |
| **El Precavido** | 1×PARTIDA | Busca una RESPUESTA 🛡️ en el Mazo de Protocolos, gratis | mesa |
| **La Jefa de Unidad** | PASIVA | Tus 🧑‍⚕️ no pueden ser descartados por rivales | mesa |

> **Por qué estos números** (`DISENO.md` §4h): las primeras versiones de
> varios de estos avatares medían +1,4 a **+8,5** — todo lo que genere robo de
> cartas repetible se dispara, porque robar alimenta colocar y colocar altas.
> Lo que ves arriba es la versión ya calibrada de cada uno. Los «mesa» parten
> del playtest con esa lección aprendida: si roban cartas, que sea una vez o
> con gatillo rival.

---

## 9. Fin de la partida y puntuación

La guardia termina cuando el **último jugador de la ronda 8** (2 y 3 jugadores)
o de la **ronda 10** (4 jugadores) termina su **Fin de Guardia** — sí, con su
deterioro incluido. También termina así la ronda en la que se agote el Mazo de
Pacientes.

Los pacientes que quedan en cama **no puntúan**: ni bien ni mal. Quedan para
la próxima guardia. Ese es su problema.

**Puntuación:**

```
  + Puntos de cada paciente en tu pila de ALTAS
  − Penalización de cada ✝️ frente a ti
  + 3   si terminas SIN NINGÚN ✝️              "No se me fue nadie"
  + 1   si tus únicos ✝️ fueron Gravedad III
        o Código Rojo                          "Se hizo todo"
  ─────────────────────────────────────────────────
  = Tu puntaje
```

Los dos bonus **no se suman**: o lo uno, o lo otro.

> **"Se hizo todo"** es el consuelo del que se arriesgó. Si se te fue un
> Crítico o un Código Rojo, nadie te va a preguntar nada: entraron muriéndose y
> **se hizo todo**. Pero basta con que se te vaya **un solo Gravedad I** para
> perderlo — de eso no se muere nadie, y en el comité te lo van a decir.
>
> Ahí está el incentivo que la carta no dice: el *Fallece −1* del leve engaña.
> Dejarlo morir te cuesta **cuatro veces eso** entre el Sumario, la cama muerta
> media ronda y los dos bonus que ya no vas a cobrar. El Gravedad I no vale por
> sus 2 puntos: **vale por lo rápido que libera la cama.** Tres recursos, alta,
> y vuelves a revelar dos pacientes — uno de los cuales puede ser un Crítico de
> +6. Sus 7 ❤️ no son permiso para ignorarlo: son el margen para elegir *cuándo*
> lo cierras.

**Desempates**, en orden:
1. Menos fallecidos.
2. Más altas de Gravedad III o Código Rojo.
3. Más pacientes vivos aún en cama.
4. Quien haya llegado antes al café. Se decide discutiendo.

---

## 10. Resumen del turno (para la mesa)

```
1. ENTREGA DE TURNO   a) ✅ de hace una ronda → ALTA + puntos
                      b) Cama vacía → PUEDES revelar 2 y admitir 1
                         (cada cama vacía: −1 punto al Fin de Guardia)
                      c) Roba 4 (3 si son 4 jug.) · robar ⚠️ no hace nada

2. EL PASILLO         1 Negocio: Canje (bota 2 → roba 2 Protocolos, elige 1)
                        o Trueque (da 2 a un rival → te da 1 del tipo que pidas)
                      Juega máx. 1 Acción

3. PASE DE VISITA     Máx. 3 recursos (en su sistema = ×2)
                      Colocar ⚠️ → resuelve su complicación AHÍ (🛡️ la previene)
                      Cerrar Sumario: bota 2 recursos c/u
                      Completo → ✅ Estabilizado

4. FIN DE GUARDIA     Pasa un día: todo no-✅ pierde 1 ❤️
                      A 0 ❤️ → Alta Celestial: ✝️ + Sumario
                      Cada cama vacía: −1 punto (salvo en la última ronda)
                      Descarta hasta 5 en mano (−1 por Sumario abierto)
```

## 11. Variantes

**Guardia Corta (25 min).** 6 rondas, todo lo demás igual. En esta variante
**no se aplican los bonus de Guardia "No se me fue nadie" ni "Se hizo todo"**: con tan pocas
rondas terminar sin fallecidos deja de ser una hazaña y se vuelve lo normal.

**Modo Cooperativo (Brote).** Todos comparten una UCI de 6 camas y turnan las
fases. Cada ⚠️ afecta a la unidad compartida. Ganan si logran 25 puntos
sin superar 5 ✝️. Las cartas de ataque se descartan del mazo.

**Modo Pelada Letal.** Tal como la parió su autor: si la *Pelada* saca dos
caras, no mata un paciente — **ganas la partida al instante**. Conviértela en
el final más dramático o más injusto de la noche. Recomendado solo para mesas
que ya se odian un poco.

**Modo Cruel.** Los recursos sobrantes no hacen de colchón: si a un paciente
✅ le quitan cualquier recurso, pierde el ✅ igual. Recomendado solo entre
personas que no vayan a compartir turno mañana.

**Turno de Noche.** No se pueden jugar cartas de Acción de tipo ATAQUE. Baja
el caos, sube el peso de la gestión clínica. Para grupos que quieren un juego
más "serio" — o que van a compartir turno de verdad mañana.
