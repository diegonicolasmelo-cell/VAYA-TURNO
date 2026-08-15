# ¡VAYA TURNO! — Reglamento v0.9 (playtest)

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
| Cartas de **Recurso** | 60 | 🩻 Imagen · 💊 Fármacos · 🧑‍⚕️ Personal · 📈 Monitoreo |
| Cartas de **Acción** | 24 | 12 diseños × 2 copias |
| Cartas de **Evento Adverso** | 18 | Mazo aparte. Solo se roba cuando algo lo obliga |
| Fichas de **Vida** (❤️) | ~60 | Cubos, monedas o un dial por cama |
| Fichas de **Estabilizado** (✅) | 12 | 3 por jugador |
| Fichas de **Cruz** (✝️) | 20 | Marcan fallecidos |
| **Marcador de Ronda** | 1 | Pista de 10 rondas |

> Con los CSV de `cartas/` y `tools/generar_pnp.py` tienes un print-and-play
> listo para imprimir. Ver `cartas/README.md`.

---

## 3. Preparación

1. Cada jugador elige un **Personaje** y lo pone frente a sí. Deja espacio
   para **3 camas** debajo.
2. Baraja el **Mazo de Pacientes**. Cada jugador **admite 3 pacientes**
   (ver §5.3, *Admisión*) y les pone las fichas ❤️ que indique la carta.
3. Baraja el **Mazo de Guardia** (Recursos + Acciones, todo junto).
4. Deja el **Mazo de Eventos Adversos** aparte, boca abajo. **Nunca se roba
   por voluntad propia.**
5. Cada jugador roba **4 cartas** de mano inicial.
6. Empieza quien haya hecho el turno de noche más reciente. Si nadie lo
   admite, quien tenga las manos más frías.

**Ajuste por número de jugadores:**

| Jugadores | Camas c/u | Robo por turno | Rondas | Nota |
|---|---:|---:|---:|---|
| 2 | 3 | 5 | 8 | Los ataques duelen el doble. Es a propósito. |
| 3 | 3 | 5 | 8 | **Configuración recomendada** |
| 4 | 2 | **4** | 10 | Menos camas y menos robo: los turnos vuelan |

> Estos números están simulados, no improvisados. Con ellos un jugador
> competente salva ~60% de sus pacientes: unas **2,4 altas y 1,5
> fallecidos** por guardia. Si tu mesa se aleja mucho de eso, revisa
> `docs/DISENO.md` §4 antes de cambiar nada.

---

## 4. Los pacientes

Cada carta de paciente tiene:

```
┌─────────────────────────────┐
│  SHOCK SÉPTICO       ❤️ 5   │   ← Vida inicial
│  Gravedad III               │
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

---

## 5. El turno

Un turno tiene seis fases, en este orden. Una **ronda** son los turnos de
todos los jugadores.

### 5.1 Deterioro

Cada paciente en tu UCI que **no** esté ✅ Estabilizado pierde **1 ❤️**.

Si un paciente llega a **0 ❤️** → **fallece**. Descarta la carta y todos sus
recursos, pon una ✝️ frente a ti y anota su penalización. La cama queda vacía.

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

Roba **5 cartas** del Mazo de Guardia (**4** en partidas de 4 jugadores).

**Si robas una carta con el símbolo ⚠️ Complicación:** quédate la carta
(es un recurso normal), pero **inmediatamente** roba 1 carta del Mazo de
Eventos Adversos y resuélvela. Sigue robando hasta completar tu robo.

> Sí. La carta que te salva te trae el problema. Bienvenido.

Si el Mazo de Guardia se agota, baraja el descarte y forma uno nuevo.

### 5.5 Acción

- **Recursos:** juega **todos los que quieras**. Colócalos sobre **tus**
  pacientes.
- **Acciones:** juega **como máximo 1 por turno**. Resuelve su texto y
  descártala.

> El límite es de veneno, no de trabajo clínico. Puedes tratar a tus
> pacientes todo lo que te dé la mano; arruinarle el turno al colega,
> una vez.

En cuanto un paciente tiene **todos** los recursos que pide (da igual si le
sobran de un tipo), colócale una ficha **✅ Estabilizado**. Deja de perder
vida de inmediato, incluso a mitad de turno.

> **Importante:** si un paciente ✅ pierde un recurso por cualquier motivo y
> deja de cumplir sus requisitos, **pierde la ficha ✅ al instante** y vuelve
> a deteriorarse en tu siguiente fase de Deterioro. Los recursos sobrantes
> sirven de colchón.

### 5.6 Cierre

Descarta hasta quedarte con un máximo de **5 cartas** en mano. Pasa el turno.

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

## 7. Eventos Adversos

El Mazo de Eventos Adversos se roba **únicamente** cuando algo te obliga:
un ⚠️ al robar, o una carta de Acción que te lo imponga.

Se resuelve de inmediato y se descarta. Si el evento afecta a "un paciente"
sin especificar cuál y no dice quién elige, **elige el jugador afectado**.

Si un evento no puede aplicarse (ej.: pide descartar un Fármaco y el paciente
no tiene ninguno), **no pasa nada**. No se sustituye por otro efecto.

Algunos personajes son **inmunes** a categorías de eventos (marcadas en la
carta como `RESPIRATORIO` o `INFECCIOSO`). Si eres inmune, el evento se
descarta sin efecto.

---

## 8. Los personajes

Cada personaje tiene una **Pasiva** (siempre activa) y un **Turno Extra**
(una sola vez por partida — gira la carta 90° al usarlo).

| Personaje | Pasiva | Turno Extra (1×/partida) |
|---|---|---|
| **La Intensivista** | En tu fase de Deterioro, elige 1 paciente: no pierde vida este turno. | **Código Azul:** devuelve a 1 ❤️ un paciente tuyo que haya fallecido en esta ronda. Recupera su carta y sus recursos del descarte. Cancela la ✝️. |
| **El Infectólogo** | Inmune a eventos `INFECCIOSO`. Una vez por turno, revela cartas del Mazo de Guardia hasta encontrar un 💊 **Antibiótico**: quédatelo y descarta el resto. | **Terapia Dirigida:** un paciente tuyo cuenta como si tuviera **todos** los 💊 que pide. |
| **La Terapeuta Respiratoria** | Inmune a eventos `RESPIRATORIO`. | **Weaning Exitoso:** durante este turno, tus 📈 cuentan como 🩻 y viceversa. |
| **El Residente de Turno** | Robas **1 carta adicional** cada turno. Tu mano máxima es **4** en vez de 5. | **Guardia de 36 Horas:** toma un turno completo extra ahora. Después, sáltate tu siguiente turno entero (tus pacientes **sí** se deterioran en él). |
| **La Enfermera Coordinadora** | Tus recursos 🧑‍⚕️ no pueden ser robados, descartados ni movidos por cartas de rivales. | **Reasignación:** mueve libremente **todos** los recursos entre tus pacientes, como quieras. |
| **El Jefe de Servicio** | Una vez por turno, descarta 1 carta y roba 2. | **No Está en el Protocolo:** anula cualquier carta de Acción o Evento Adverso, juegue quien la juegue. Se puede usar fuera de turno. |

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
1. DETERIORO   Cada paciente no-✅ pierde 1 ❤️. A 0 ❤️ → fallece.
2. ALTA        Los ✅ que sobrevivieron una ronda completa → alta + puntos.
3. ADMISIÓN    Por cada cama vacía: revela 2 pacientes, elige 1.
4. GUARDIA     Roba 5 cartas (4 si son 4 jug.). Cada ⚠️ → 1 Evento ya.
5. ACCIÓN      Recursos: los que quieras. Acciones: máx. 1.  Completo → ✅.
6. CIERRE      Descarta hasta 5 cartas en mano.
```

---

## 11. Variantes

**Guardia Corta (25 min).** 6 rondas, todo lo demás igual. En esta variante
**no se aplica el bonus de Guardia Limpia**: con tan pocas rondas terminar sin
fallecidos deja de ser una hazaña y se vuelve lo normal.

**Modo Cooperativo (Brote).** Todos comparten una UCI de 6 camas y turnan las
fases. Se roban **2** Eventos Adversos por ronda. Ganan si logran 25 puntos
sin superar 5 ✝️. Las cartas de ataque se descartan del mazo.

**Modo Cruel.** Los recursos sobrantes no hacen de colchón: si a un paciente
✅ le quitan cualquier recurso, pierde el ✅ igual. Recomendado solo entre
personas que no vayan a compartir turno mañana.

**Turno de Noche.** No se pueden jugar cartas de Acción de tipo ATAQUE. Baja
el caos, sube el peso de la gestión clínica. Para grupos que quieren un juego
más "serio" — o que van a compartir turno de verdad mañana.
