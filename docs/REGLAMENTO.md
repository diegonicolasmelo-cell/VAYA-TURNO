# ¡VAYA TURNO! — Reglamento v0.11 (playtest)

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
| Cartas de **Recurso** | 63 | El **Mazo de Guardia**: 🩻 Imagen · 💊 Fármacos · 🧑‍⚕️ Personal · 📈 Soporte Vital · 🃏 Comodín |
| Cartas de **Protocolo** (Acciones) | 45 | Mazo aparte. Se compran con el **Canje** |
| Cartas de **Evento Centinela** | 28 | Mazo aparte. Solo se roba cuando algo lo obliga |
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
   (ver §5.3, *Admisión*) y les pone las fichas ❤️ que indique la carta.
3. Baraja el **Mazo de Guardia** (los 63 Recursos, con sus ⚠️ adentro).
   Baraja aparte el **Mazo de Protocolos** (las 45 Acciones).
4. Deja el **Mazo de Eventos Centinela** aparte, boca abajo. **Nunca se roba
   por voluntad propia.**
5. Cada jugador roba **4 cartas** de mano inicial.
6. Empieza quien haya hecho el turno de noche más reciente. Si nadie lo
   admite, quien tenga las manos más frías.

**Ajuste por número de jugadores:**

| Jugadores | Camas c/u | Robo por turno | Rondas | Nota |
|---|---:|---:|---:|---|
| 2 | 3 | 4 | 8 | Los ataques duelen el doble. Es a propósito. |
| 3 | 3 | 4 | 8 | **Configuración recomendada** |
| 4 | 2 | **3** | 10 | Menos camas y menos robo: los turnos vuelan |

> Estos números están simulados, no improvisados. Con ellos un jugador
> competente salva ~65% de sus pacientes: unas **2,7 altas y 1,5
> fallecidos** por guardia. Si tu mesa se aleja mucho de eso, revisa
> `docs/DISENO.md` §4 antes de cambiar nada.

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
│   📈 ×2   🧑‍⚕️ ×1             │
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
| **★ Código Rojo** | 4 | 8 | **+8** | −3 |

Los recursos se colocan **encima de la carta del paciente**, en abanico, y
se quedan ahí. No son gastables: **son su tratamiento**.

### El sistema del paciente

Cada paciente pertenece a un **sistema clínico**, marcado con un chip de color:

🫁 **Respiratorio** · 🫀 **Cardíaco** · 🧠 **Neurológico** · 🧪 **Metabólico** · 🔪 **Quirúrgico**

Eso importa por una sola regla, la de §4.1.

### 4.1 Recursos específicos: la sinergia

24 de las 63 cartas del Mazo de Guardia llevan también un chip de sistema.

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
| **Resonancia con Cupo** | Al jugarla, **no puedes jugar más recursos este turno**. Cuesta tiempo, no recursos. |

---

## 5. El turno

Un turno tiene seis fases, en este orden. Una **ronda** son los turnos de
todos los jugadores.

### 5.1 Deterioro

Cada paciente en tu UCI que **no** esté ✅ Estabilizado pierde **1 ❤️**.

Si un paciente llega a **0 ❤️** → recibe el **Alta Celestial**. Se le cursó
el alta hacia el piso que está sobre las nubes: descarta la carta y todos sus
recursos, pon una ✝️ frente a ti y anota su penalización. La cama queda vacía.

**Y llega el papeleo:** toma una carta de **Sumario Administrativo**. Queda en
tu mano, no se puede jugar ni descartar, y **reduce tu límite de mano en 1**.
Para cerrar el caso: en tu fase de Acción, descarta 2 recursos de tu mano —
o consigue que el Director del Hospital haga desaparecer el expediente.

> Lo peor de perder un paciente no es perder los puntos. Es el formulario.

### 5.2 Alta

¿Tienes un paciente que ya estaba ✅ Estabilizado **desde antes de tu turno
anterior**? Ha sobrevivido la ronda de consolidación: **dale de alta**.

Toma la carta, ponla en tu **pila de altas** y anota sus puntos. Sus
recursos van al descarte. La cama queda vacía.

> **Por qué existe esta espera:** completar los recursos no es ganar todavía.
> Hay una ronda entera en la que tu paciente estabilizado está a la vista de
> todos, sin vida perdiendo pero perfectamente sabotéable. Ahí es donde se
> rompen las amistades.

### 5.3 Admisión

Por cada **cama vacía**, revela las **2 primeras cartas** del Mazo de
Pacientes, **elige 1** para admitir y pon la otra **al fondo del mazo**.

Coloca las fichas ❤️ que indique la carta. Los pacientes recién admitidos
**no pierden vida este turno** (su primer deterioro es en tu próximo turno).

> No puedes dejar camas vacías. Nunca ha habido una cama vacía en una UCI y
> no la va a haber en este juego.

### 5.4 Guardia (robo)

Roba **4 cartas** del Mazo de Guardia (**3** en partidas de 4 jugadores).

**Si robas una carta con el símbolo ⚠️ Complicación:** quédate la carta
(es un recurso normal), pero **inmediatamente** roba 1 carta del Mazo de
Eventos Centinela y resuélvela. Sigue robando hasta completar tu robo.

> Sí. La carta que te salva te trae el problema. Bienvenido.

Si el Mazo de Guardia se agota, baraja el descarte y forma uno nuevo.

### 5.5 Acción

- **Recursos:** juega **todos los que quieras**. Colócalos sobre **tus**
  pacientes.
- **El Canje** (máx. 1 por turno): descarta **2 recursos** de tu mano y roba
  **1 carta del Mazo de Protocolos**. Así se consiguen las Acciones: cambiando
  lo que te sobra por un favor.
- **Acciones:** juega **como máximo 1 por turno**. Cuestan 0 — ya pagaste al
  conseguirla. Resuelve su texto y descártala.
- **Cerrar Sumarios:** descarta 2 recursos por cada Sumario que quieras cerrar.

> El límite de Acciones es de veneno, no de trabajo clínico. Puedes tratar a
> tus pacientes todo lo que te dé la mano; arruinarle el turno al colega,
> una vez.

En cuanto un paciente tiene **todos** los recursos que pide (da igual si le
sobran de un tipo), colócale una ficha **✅ Estabilizado**. Deja de perder
vida de inmediato, incluso a mitad de turno.

> **Importante:** si un paciente ✅ pierde un recurso por cualquier motivo y
> deja de cumplir sus requisitos, **pierde la ficha ✅ al instante** y vuelve
> a deteriorarse en tu siguiente fase de Deterioro. Los recursos sobrantes
> sirven de colchón.

### 5.6 Cierre

Descarta hasta quedarte con un máximo de **5 cartas** en mano (**menos 1 por
cada Sumario abierto** que tengas). Pasa el turno.

---

## 6. Fuera de turno

Solo dos cosas se pueden hacer cuando no es tu turno:

1. **Jugar una carta marcada 🛡️ RESPUESTA** (ej.: *Café de Enfermería*).
   No cuenta como tu Acción del turno.
2. **Usar una habilidad de Personaje que diga explícitamente que se puede.**

Las cartas 🛡️ se resuelven **antes** que la carta que están respondiendo, y
pueden encadenarse (una 🛡️ puede anular otra 🛡️).

**Regla de oro de las discusiones:** si la mesa no se pone de acuerdo en cómo
se resuelve algo, la interpretación que **más perjudique al jugador que va
ganando** es la correcta. Ha funcionado en comités clínicos durante décadas.

---

## 7. Eventos Centinela

El Mazo de Eventos Centinela se roba **únicamente** cuando algo te obliga:
un ⚠️ al robar, o una carta de Acción que te lo imponga.

Se resuelve de inmediato y se descarta. Si el evento afecta a "un paciente"
sin especificar cuál y no dice quién elige, **elige el jugador afectado**.

Si un evento no puede aplicarse (ej.: pide descartar un Fármaco y el paciente
no tiene ninguno), **no pasa nada**. No se sustituye por otro efecto.

Los eventos llevan categoría (`RESPIRATORIO`, `INFECCIOSO`, `GENERAL`). Hoy
es solo sabor; queda reservada para inmunidades de futuros avatares.

---

## 8. Los personajes

Los seis avatares de la fauna hospitalaria. Cada uno tiene **una** habilidad,
con su propia frecuencia de uso. Los de "1×PARTIDA" giran la carta 90° al
usarla.

| Personaje | Frecuencia | Habilidad |
|---|---|---|
| **El Diostor** | 1× por ronda | Cuando robas una carta ⚠️, puedes pasarle el Evento Centinela al jugador de tu derecha: lo roba y lo resuelve él como si fuera suyo. *"¿Yo, equivocarme? Debe ser un error del laboratorio."* |
| **El Médico Fantasma** | Pasiva | En las rondas 1–3 robas 1 carta **menos**. Desde la ronda 4, robas 1 carta **adicional** cada turno por el resto de la guardia. |
| **Doctor Amor** | 1× por partida | **Seducción de Pasillo:** roba un recurso 🧑‍⚕️ Personal colocado sobre un paciente rival y colócalo sobre un paciente tuyo. |
| **El Director del Hospital** | 1× por partida | **Perdonazo Administrativo:** anula y descarta un Sumario, tuyo o de cualquier otro jugador. Puedes cobrar el favor. |
| **La Gestora de Camas** | 1× por turno | **Derivación:** devuelve un paciente tuyo al fondo del Mazo de Pacientes (sus recursos se descartan) y admite uno nuevo de inmediato. No cuenta como fallecido ni deja Sumario. |
| **El Médico Esotérico** | 1× por turno | **Confía en el Universo:** revela la primera carta del Mazo de Guardia. Recurso sin ⚠️ → colócalo **gratis** sobre un paciente tuyo. Con ⚠️ → resuelve el Evento y descarta 1 carta de tu mano como penitencia kármica. |

> **Notas de balance sin validar** (se resuelven en la mesa): el Fantasma y el
> Esotérico juegan cada turno mientras Amor y el Director juegan una vez — si
> en el playtest los segundos se sienten planos, darles una pasiva menor es el
> ajuste natural. Está anotado en `docs/DISENO.md` §5.

---

## 9. Fin de la partida y puntuación

La guardia termina al **final de la ronda 8** (2 y 3 jugadores) o de la
**ronda 10** (4 jugadores) — o antes, si el Mazo de Pacientes se agota.

Los pacientes que quedan en cama **no puntúan**: ni bien ni mal. Quedan para
la próxima guardia. Ese es su problema.

**Puntuación:**

```
  + Puntos de cada paciente en tu pila de ALTAS
  − Penalización de cada ✝️ frente a ti
  + 3   si terminas la guardia SIN NINGÚN FALLECIDO  ("Guardia Limpia")
  ─────────────────────────────────────────────────
  = Tu puntaje
```

**Desempates**, en orden:
1. Menos fallecidos.
2. Más altas de Gravedad III o Código Rojo.
3. Más pacientes vivos aún en cama.
4. Quien haya llegado antes al café. Se decide discutiendo.

---

## 10. Resumen del turno (para la mesa)

```
1. DETERIORO   No-✅ pierde 1 ❤️. A 0 → Alta Celestial: ✝️ + Sumario.
2. ALTA        Los ✅ que sobrevivieron una ronda completa → alta + puntos.
3. ADMISIÓN    Por cada cama vacía: revela 2 pacientes, elige 1.
4. GUARDIA     Roba 4 cartas (3 si son 4 jug.). Cada ⚠️ → 1 Centinela ya.
5. ACCIÓN      Recursos libres (🫁🫀🧠🧪🔪 en su sistema = ×2) · Canje 2→1
               · Acción máx 1 · Completo → ✅
6. CIERRE      Descarta hasta 5 en mano (−1 por Sumario abierto).
```

---

## 11. Variantes

**Guardia Corta (25 min).** 6 rondas, todo lo demás igual. En esta variante
**no se aplica el bonus de Guardia Limpia**: con tan pocas rondas terminar sin
fallecidos deja de ser una hazaña y se vuelve lo normal.

**Modo Cooperativo (Brote).** Todos comparten una UCI de 6 camas y turnan las
fases. Se roban **2** Eventos Centinela por ronda. Ganan si logran 25 puntos
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
