# ¡VAYA TURNO! — Reglamento v0.15 (playtest)

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
| Cartas de **Recurso** | 63 | El **Mazo de Guardia**: 🩻 Imagen · 💊 Fármacos · 🧑‍⚕️ Personal · 💉 Procedimientos · 🃏 Comodín |
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
3. Baraja el **Mazo de Guardia** (los 63 Recursos, con sus 18 ⚠️ adentro).
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
> competente salva ~66% de sus pacientes: unas **2,8 altas y 1,4
> fallecidos** por guardia, salva al **43% de los Gravedad III** y cierra
> "Se hizo todo" una de cada cuatro veces. Si tu mesa se aleja mucho de
> eso, revisa `docs/DISENO.md` §4 antes de cambiar nada.

---

## 4. Los pacientes

Cada carta de paciente tiene:

```
┌─────────────────────────────┐
│  SHOCK SÉPTICO       ❤️ 5   │   ← Vida inicial
│  Gravedad III   🫀 CARDÍACO │   ← Sistema (ver §4.1)
│  ─────────────────────────  │
│  Requiere:                  │
│   🩻 ×1   💊 ×3             │   ← Lo que necesita para estabilizarse
│   💉 ×2   🧑‍⚕️ ×1             │
│  ─────────────────────────  │
│  Alta: +5      Fallece: −2  │
│  "La hora dorada empezó     │
│   hace cuatro horas."       │
└─────────────────────────────┘
```

| Gravedad | ❤️ | Recursos | Alta | Fallece |
|---|---:|---:|---:|---:|
| **I — Observación** | 7 | 3 | **+2** | −1 |
| **II — Grave** | 6 | 5 | **+3** | −2 |
| **III — Crítico** | 5 | 7 | **+5** | −2 |
| **★ Código Rojo** | 5 | 8 | **+8** | −3 |

Los recursos se colocan **encima de la carta del paciente**, en abanico, y
se quedan ahí. No son gastables: **son su tratamiento**.

### El sistema del paciente

Cada paciente pertenece a un **sistema clínico**, marcado con un chip de color:

🫁 **Respiratorio** · 🫀 **Cardíaco** · 🧠 **Neurológico** · 🧪 **Metabólico** · 🔪 **Quirúrgico**

Eso importa por una sola regla, la de §4.1.

### 4.1 Recursos específicos: la sinergia

21 de las 63 cartas del Mazo de Guardia llevan también un chip de sistema.

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

**b) Admisión.** Por cada **cama vacía**, revela las **2 primeras cartas** del
Mazo de Pacientes, **elige 1** y pon la otra **al fondo del mazo**. Coloca las
fichas ❤️ que indique la carta.

> No puedes dejar camas vacías. Nunca ha habido una cama vacía en una UCI y no
> la va a haber en este juego.

**c) Robo.** Roba **4 cartas** del Mazo de Guardia (**3** en partidas de 4
jugadores).

Si robas una carta con el símbolo **⚠️ Complicación**: quédate la carta (es un
recurso normal), pero **resuelve de inmediato la complicación impresa en ella**
(ver §7). Después sigue robando hasta completar tu robo.

> Sí. La carta que te salva te trae el problema. Bienvenido.

El ⚠️ dispara **cada vez que la carta llega a tu mano desde el Mazo de
Guardia**, sea en esta fase o por una Acción (*Doblo Turno*, *Receta en
Blanco*). No dispara si la carta viene del descarte o de la mano de otro.

Si el Mazo de Guardia se agota, baraja el descarte y forma uno nuevo.

### 5.2 El Pasillo

Antes de la visita, en el pasillo, se arregla lo que no se puede decir en la
reunión. Aquí pasan las dos cosas turbias del juego:

- **El Negocio** (máx. 1 por turno). La ventanilla del pasillo tiene un solo
  cupo, y eliges con quién tratas:
  - **Canje** (con el mazo): descarta **2 recursos** de tu mano y roba
    **1 carta del Mazo de Protocolos**. Así se consiguen las Acciones:
    cambiando lo que te sobra por un favor. Pagas con azar: no sabes qué
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

- **Recursos:** juega **todos los que quieras**. Colócalos **encima de tus**
  pacientes, en abanico. No son gastables: son su tratamiento.
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

> **Al robar una carta ⚠️: te la quedas** (es un recurso normal y lo puedes
> jugar) **y resuelves su complicación de inmediato.** Después sigues robando.

Son **18 cartas de las 63** del Mazo de Guardia. Robas una cada cuatro cartas,
más o menos: una por turno.

### 7.1 A quién le pasa: el 🎯 Objetivo

**La carta elige a la víctima, no tú.** Cada complicación lleva un 🎯 Objetivo
que dice a cuál de tus pacientes le toca:

| 🎯 Objetivo | A quién señala |
|---|---|
| **EL MÁS GRAVE** | El que tenga **menos ❤️** en este momento |
| **EL QUE MEJOR VA** | El que tenga **más ❤️** en este momento |
| **EL MÁS TRATADO** | El que tenga **más recursos encima** (cuenta cartas, no íconos) |
| **EL ESTABILIZADO ✅** | Tu paciente con ficha ✅. Si no tienes ninguno, va **al que mejor va** |
| **TÚ ELIGES** | Eliges tú. Son solo dos: la muestra perdida y la línea que hubo que retirar no discriminan |
| **TU MANO** | No toca ninguna cama: descartas una carta de tu mano. Solo el *Stock de Sala* |

**En caso de empate, eliges tú entre los empatados.** Es la única decisión que
te queda, y a veces es la que importa.

> **Por qué la carta decide.** Si eligieras libremente, mandarías siempre el
> daño al paciente que ya diste por perdido y ninguna complicación dolería.
> Y fíjate hacia dónde apuntan: **once de las dieciocho buscan al que iba
> bien** o al que ya tenía su ✅. Eso no es casualidad — es la tesis del juego.
> Lo que se complica en una UCI no es lo que ya estaba perdido: es lo que
> parecía resuelto.

Si la complicación no puede aplicarse (pide descartar un 💊 y ese paciente no
tiene ninguno; o no tienes pacientes en cama), **no pasa nada**. No se
sustituye por otro efecto ni se busca otro objetivo.

### 7.2 Las dieciocho

| Carta ⚠️ | Complicación | 🎯 |
|---|---|---|
| Antibiótico de Amplio Espectro | Resistencia Antibiótica | ✅ ESTABILIZADO |
| Sedoanalgesia | Delirium en UCI | EL QUE MEJOR VA |
| Anticoagulación | Sangrado | EL MÁS GRAVE |
| Noradrenalina | Taquicardia Ventricular | EL MÁS GRAVE |
| Anticonvulsivante | Sobresedación | ✅ ESTABILIZADO |
| Analgesia Postoperatoria | Depresión Respiratoria | EL QUE MEJOR VA |
| Radiografía de Tórax | Hallazgo Incidental | ✅ ESTABILIZADO |
| Ecografía a Pie de Cama | Falso Positivo | EL QUE MEJOR VA |
| TAC de Urgencia | Nefropatía por Contraste | EL QUE MEJOR VA |
| Línea Arterial | Isquemia Distal | TÚ ELIGES |
| Catéter Venoso Central | Bacteriemia por Catéter | EL QUE MEJOR VA |
| **Ventilación Mecánica** | **Neumonía Asociada a VM** | EL MÁS TRATADO |
| Gases Arteriales | Muestra Hemolizada | TÚ ELIGES |
| Pleurostomía | Fuga Aérea Persistente | ✅ ESTABILIZADO |
| Técnico en Enfermería | El Turno Veinticuatro | EL MÁS GRAVE |
| Gestor de Camas | Presión de Camas | EL QUE MEJOR VA |
| Pabellón Disponible | Pabellón Suspendido | EL QUE MEJOR VA |
| Stock de Sala | La Gaveta Vacía | TU MANO |

> *El Turno Veinticuatro* es la única que actúa fuera de la cama donde juegas:
> el técnico lleva un día de pie y confunde dos bombas **en el paciente más
> grave**, aunque tú hayas puesto la carta en otro.

---

## 8. Los personajes

Los seis avatares de la fauna hospitalaria. Cada uno tiene **una** habilidad,
con su propia frecuencia de uso. Los de "1×PARTIDA" giran la carta 90° al
usarla.

| Personaje | Frecuencia | Habilidad |
|---|---|---|
| **El Diostor** | 1× por ronda | Cuando robas una carta ⚠️, puedes pasarle su complicación al jugador de tu derecha: la resuelve él sobre sus pacientes, como si la hubiera robado. *"¿Yo, equivocarme? Debe ser un error del laboratorio."* |
| **El Médico Fantasma** | Pasiva | En las rondas 1–3 robas 1 carta **menos**. Desde la ronda 4, robas 1 carta **adicional** cada turno por el resto de la guardia. |
| **Doctor Amor** | 1× por partida | **Seducción de Pasillo:** roba un recurso 🧑‍⚕️ Personal colocado sobre un paciente rival y colócalo sobre un paciente tuyo. |
| **El Director del Hospital** | 1× por partida | **Perdonazo Administrativo:** anula y descarta un Sumario, tuyo o de cualquier otro jugador. Puedes cobrar el favor. |
| **La Gestora de Camas** | 1× por partida | **Derivación:** devuelve un paciente tuyo al fondo del Mazo de Pacientes (sus recursos se descartan) y admite uno nuevo de inmediato. No cuenta como fallecido: no pones ✝️ ni restas sus puntos. **Pero el papeleo es el mismo:** toma un Sumario, y tu guardia ya no puede ser Limpia. |
| **El Médico Esotérico** | 1× por turno | **Confía en el Universo:** revela la primera carta del Mazo de Guardia. Recurso sin ⚠️ → colócalo **gratis** sobre un paciente tuyo. Con ⚠️ → resuelve el Evento y descarta 1 carta de tu mano como penitencia kármica. |

> **Notas de balance sin validar** (se resuelven en la mesa): el Fantasma y el
> Esotérico juegan cada turno mientras Amor y el Director juegan una vez — si
> en el playtest los segundos se sienten planos, darles una pasiva menor es el
> ajuste natural. Está anotado en `docs/DISENO.md` §5.
>
> **La Gestora sí está medida** (v0.13): con la Derivación gratis y cada turno
> ganaba +2,7 puntos sobre sus rivales y cerraba "No se me fue nadie" el 31% de las
> veces contra el 8% de los demás. Con el Sumario, la pérdida de la Limpia y el
> límite de 1 por partida queda en **+0,7**, que es lo que debe valer una
> habilidad. Los números están en `docs/DISENO.md` §4.

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
> +5. Sus 7 ❤️ no son permiso para ignorarlo: son el margen para elegir *cuándo*
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
                      b) Cama vacía → revela 2 pacientes, elige 1
                      c) Roba 4 (3 si son 4 jug.) · cada ⚠️ → su complicación ya

2. EL PASILLO         1 Negocio: Canje (bota 2 → roba 1 Protocolo)
                        o Trueque (da 2 a un rival → te da 1 del tipo que pidas)
                      Juega máx. 1 Acción

3. PASE DE VISITA     Recursos sin límite (🫁🫀🧠🧪🔪 en su sistema = ×2)
                      Cerrar Sumario: bota 2 recursos c/u
                      Completo → ✅ Estabilizado

4. FIN DE GUARDIA     Pasa un día: todo no-✅ pierde 1 ❤️
                      A 0 ❤️ → Alta Celestial: ✝️ + Sumario
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
