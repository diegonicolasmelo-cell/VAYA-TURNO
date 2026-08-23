# ¡VAYA TURNO! — Reglamento v0.32 (rama experimental)

> **Qué es esto.** El rediseño de agosto 2026: sabotaje con recursos ⚠️,
> Pizarra de Turno, admisión obligatoria y complicación unificada "donde se
> ubica". Usa los mazos de `cartas/v030/` (recursos, acciones y logros
> propios; pacientes, personajes y sumarios se comparten con la base) — la
> carpeta conserva el nombre `v030` porque **el mazo no cambió** en v0.31.
>
> **v0.32: la ronda 1 se juega con 2 pacientes.** La tercera cama se admite
> recién en la ronda 2 — la unidad empieza a media carga y se llena sola.
> Medido: neutro (salvamento 67% igual; GIII 43→45%, ROJO 80→73%).
>
> **v0.31: se eliminó la fase de El Pasillo.** El turno son ahora **tres
> fases**: Entrega de Turno, Pase de Visita y Fin de Guardia. La Pizarra
> quedó en el centro de la mesa, siempre a la vista, y se compra durante el
> Pase de Visita. Ninguna medición cambia: el simulador nunca modeló la
> compra de Protocolos, así que el suelo de balance es el mismo.
>
> **La v0.21 (`REGLAMENTO.md`) sigue siendo la versión estable e imprimible.**
> Esta rama existe para probarse en mesa. Suelo medido tras el paso de
> balance con `tools/simular_v030.py`: salvamento 67% · 3,0 altas · 1,5
> fallecidos · Gravedad III 43% · ROJO 80% — todo en banda. "No se me fue
> nadie" queda en 3,2%: con sabotaje, la guardia limpia es milagro (§9).

Juego para **2–4 jugadores** · **30–45 min** · **14+**.

---

## 1. La idea en 30 segundos

Cada jugador dirige una UCI de **3 camas**. Los pacientes llegan solos, se
deterioran solos, y los recursos nunca alcanzan. Lo nuevo de esta rama: los
recursos con ⚠️ son **de doble filo** — sobre tu paciente son tratamiento
(con su complicación incluida), sobre un paciente rival son **sabotaje**.
La misma carta, dos usos. Tú decides qué eres esta noche.

---

## 2. Componentes

| Componente | Cant. | Nota |
|---|---:|---|
| Cartas de **Paciente** | 26 | Las mismas de la base (Gravedad III: 6 ❤️ · pide 8 · +6/−2) |
| Cartas de **Recurso** | 67 (44 diseños) | `cartas/v030/recursos.csv` · **22 llevan ⚠️** |
| Cartas de **Protocolo** (Acciones) | 32 (22 diseños) | Con **coste impreso 1–3**. Se compran en la Pizarra |
| Cartas de **Personaje** | 22 | Las de la base (adaptaciones en §8) |
| Cartas de **Logro** | 3 | *¡Durante Mi Guardia No!* · *Se Hizo Todo* · *Auditoría del Ministerio* |
| **Sumario Administrativo** | 6 | Ahora vive **boca arriba en tu zona**, no en la mano |

Fichas: ❤️ vida · ✅ estabilizado · ✝️ cruces · 1 moneda · marcador de ronda.

## 3. Preparación

1. Cada jugador recibe **3 avatares, elige 1** y devuelve los otros dos
   a la reserva (v0.32: eran 2 — más elección al costo de una pizca más de
   setup; el simulador no modela avatares, así que el balance no se mueve).
2. Baraja el Mazo de Pacientes. Cada jugador **recibe 2 pacientes al azar**
   — la tercera cama parte vacía y **se queda vacía toda la ronda 1**. Da
   vuelta la primera carta del mazo: es el **Informe de Gestión de Camas** y
   queda boca arriba toda la partida.
3. Baraja el **Mazo de Guardia** (67 recursos) y el **Mazo de Protocolos**.
   Revela las **3 primeras cartas de Protocolos**: esa fila es la
   **Pizarra de Turno**.
4. Pon al centro las 3 cartas de **Logro** y los 6 **Sumarios**.
5. Cada jugador roba **4 cartas**. Empieza quien haya hecho el turno de
   noche más reciente.

**Ajuste por jugadores:** 2–3 jug: 3 camas · roba 4 · 8 rondas. 4 jug:
2 camas · roba 3 · 10 rondas.

---

## 4. El turno — tres fases

### 4.1 Entrega de Turno

**a) Altas.** Todo paciente tuyo con ✅ **desde antes de este turno** se va
de alta… **salvo que tenga basura clínica encima** (§6.3): nadie se va con
papeleo pendiente. Guarda la carta en tu pila de puntos; sus recursos van
al descarte.

**b) Admisión — OBLIGATORIA, desde la ronda 2.** Por cada cama vacía
**debes** admitir: revela 2 pacientes (el Informe boca arriba es uno de
ellos), elige 1, el otro va al fondo. Da vuelta el nuevo Informe.

> **En la ronda 1 no se admite.** La guardia empieza con los 2 pacientes que
> te tocaron y una cama libre: el primer turno es para ordenarte, no para
> apagar tres incendios a la vez. La tercera cama se llena en la ronda 2.

**c) Robo.** Roba **4 cartas** del Mazo de Guardia (3 en partidas de 4).
Robar una ⚠️ no hace nada: es munición o tratamiento, según dónde la pongas.

### 4.2 Pase de Visita — 3 colocaciones y la Pizarra

Tienes **3 colocaciones** y un menú. Cada línea cuesta 1 colocación:

| Opción | Qué haces |
|---|---|
| **Tratar** | Coloca un recurso de tu mano sobre un paciente **tuyo**. Si trae ⚠️, resuélvela (§6.1) |
| **Sabotear** | Coloca un recurso **⚠️** sobre un paciente **rival** (§6.2) |
| **Des-escalar** | Retira 1 **basura clínica** de un paciente tuyo y descártala |

**Cerrar un Sumario NO gasta colocación:** en cualquier momento de tu Pase
de Visita, descarta **2 cartas** de tu mano y cierra 1 Sumario (nunca el
mismo turno en que llegó). *Se midió con colocación: nadie cerraba ninguno
(0%). Sin ella, se cierra el 94%.*

**La Pizarra de Turno tampoco gasta colocación.** Está en el centro de la
mesa, siempre a la vista: tres Protocolos boca arriba con su coste impreso.
Una vez por turno puedes **tomar uno pagando su coste en cartas de tu mano**
(1, 2 o 3) y repones la Pizarra de inmediato. Puedes jugarlo ahí mismo o
guardarlo para otro turno; en todo caso, **máximo 1 Acción jugada por
turno** (las RESPUESTA 🛡️ se juegan fuera de turno y no cuentan).

- **Limpieza de Pizarra:** si no tomas nada, puedes descartar los 3
  Protocolos y revelar 3 nuevos. Gasta tu compra del turno.

> El Canje y el Trueque de la v0.21 no existen en esta rama: la Pizarra los
> reemplaza. Y desde v0.31 tampoco existe la fase de El Pasillo — comprar
> es una decisión más del Pase de Visita, que es cuando de verdad miras la
> Pizarra.

La sinergia sigue igual: recurso con sistema sobre paciente del mismo
sistema **cuenta doble**. Paciente completo (y sin bloqueo) → ficha **✅**:
deja de deteriorarse. La regla de la ventana no cambia: **estabilizas en un
turno, das de alta al siguiente.**

### 4.3 Fin de Guardia

1. Todo paciente tuyo **sin ✅ pierde 1 ❤️**.
2. A 0 ❤️: **Alta Celestial** — ✝️, penalización, y toma un **Sumario**
   del centro, boca arriba en tu zona.
3. Descarta hasta quedar con **5 cartas, menos 1 por cada Sumario abierto**
   que tengas en tu zona.

---

## 5. El Sumario Administrativo (v0.30)

Vive **boca arriba en tu zona** — todos ven cuántos debes — y **muerde
mientras esté abierto: cada Sumario reduce tu límite de mano en 1**.
Cerrarlo cuesta **2 cartas** en tu Pase de Visita (no gasta colocación),
nunca el mismo turno en que llegó.

> **La Auditoría del Ministerio es una VARIANTE opcional** (la carta lo
> dice). Medida: le pega al que ya iba perdiendo el 86–90% de las veces y
> ensancha la brecha final de 5,4 a 7,1 puntos — es sal en la herida.
> Actívenla solo si su mesa disfruta ese tipo de maldad.

---

## 6. Las Complicaciones ⚠️ — una regla, dos filos

**Toda ⚠️ hace lo mismo: el paciente DONDE SE UBICA la carta pierde 1 ❤️,
al colocarla.** No hay 🎯 impreso: la víctima la decide la colocación. El
nombre y el dibujo son la sazón; la regla es una sola.

### 6.1 Sobre tu propio paciente

El recurso cuenta para su receta **y** el paciente pierde 1 ❤️. La pregunta
de siempre: *¿lo necesito lo suficiente como para aceptar lo que trae?*

> **COLOCAR NUNCA MATA.** Ninguna ⚠️ puede quitar el último ❤️ — ni la
> tuya. Si el −1 lo dejaría en 0, queda en 1. **El que mata es el reloj**
> (el deterioro del Fin de Guardia), no la carta. Esto habilita la jugada
> heroica: un paciente en 1 ❤️ puede recibir todo lo que haga falta
> mientras corres contra la noche. Medido: al experto no le cambia nada;
> al jugador nuevo le devuelve 6 puntos de salvamento.

### 6.2 Sobre un paciente rival (sabotaje)

- La complicación se resuelve: **pierde 1 ❤️** (con el piso de siempre:
  colocar nunca mata).
- **Si el tipo de la carta es algo que ese paciente pide, cuenta para su
  receta** — le regalaste tratamiento a cambio del golpe. Por eso el
  sabotaje fino se hace con tipos que **no** pide.
- Máximo **1 sabotaje por paciente rival por ronda**.

### 6.3 La basura clínica

Un recurso rival que el paciente **no pide** se queda sobre él **girado
180°**: es *basura clínica*. No cuenta para nada, pero **el paciente no
puede irse de alta mientras tenga basura encima** — se estabiliza igual
(el ✅ detiene el reloj), pero el alta espera el papeleo. Se limpia con la
**Des-escalada** (1 colocación por carta).

### 6.4 Las Protecciones 🛡️ PREVIENE

Igual que en la base, y ahora también son **defensa antisabotaje**: si el
protector ya estaba sobre el paciente, la complicación nombrada no ocurre
— ni la tuya ni la que te tire un rival. Enfermera de UCI ⇒ *Bacteriemia
por Catéter* · Técnico en Enfermería ⇒ *Neumonía Asociada a VM* ·
Kinesiólogo Respiratorio ⇒ *Delirium en UCI*. La prevención es prospectiva
y viaja con la carta.

### 6.5 Los dobles filos con texto 🛡️ propio

Cuatro cartas de Personal traen, además de su ⚠️, un beneficio que **solo
funciona sobre tus pacientes**:

| Carta | ⚠️ (donde se ubica) | 🛡️ (solo sobre lo tuyo) |
|---|---|---|
| **Cirujano de Turno** | Oblito Quirúrgico: −1 ❤️ | Cuenta como **2 recursos 🧑‍⚕️** en cualquier paciente |
| **Pabellón** | Pabellón Suspendido: −1 ❤️ | Mueve gratis 1 recurso entre tus pacientes |
| **Becado de Medicina** | Aún Estoy Aprendiendo: −1 ❤️ | Busca 1 Protocolo en el descarte de Protocolos y tómalo |
| **Personal de Turno Extra** | El Turno Veinticuatro: −1 ❤️ **y el jefe de esa unidad descarta 1 carta** | — (nació para el sabotaje) |

---

## 7. Fin de la partida y puntuación

Tras la **ronda 8**:

```
  + puntos de cada paciente en tu pila de ALTAS
  − penalización de cada ✝️
  − 1 por cada cama vacía al final (solo pasa si se agotó Urgencias)
  + 3 ¡Durante Mi Guardia No!  (ningún ✝️)
  + 1 Se Hizo Todo             (tus únicos ✝️ fueron III o ROJO)
```

Los dos logros positivos no se acumulan. Desempates: menos ✝️, luego más
altas de III/ROJO.

---

## 8. Los avatares en esta rama

Los 22 personajes se usan igual. Tres habilidades nombran mecánicas que
esta rama reemplazó — léelas así:

| Avatar | Decía | En v0.30 se lee |
|---|---|---|
| **La de Abastecimiento** (C09) | tus Canjes cuestan 1 recurso en vez de 2 | tus compras en la Pizarra cuestan **1 carta menos** (mínimo 1) |
| **La Enfermera de IAAS** (C12) | cada 3 ⚠️ resueltas en tu unidad, roba 1 Protocolo | igual, pero cuentan las ⚠️ resueltas **sobre tus pacientes** (propias o sabotaje recibido) — toma gratis la carta más barata de la Pizarra |
| **El Diostor** (C01) | pásale la complicación al de la derecha | al **tratar** con una ⚠️ propia, puedes resolver su −1 ❤️ sobre un paciente del jugador de tu derecha (piso 1 ❤️) |

---

## 9. Lo que la simulación ya dijo de esta rama

Suelo final (4.000 partidas, 2 jugadores): **salv 67% · GIII 43% · ROJO
80% · altas 2,98 · ✝️ 1,50 · sin ✝️ 3,2%.**

- **Atacar paga sin dominar:** +0,89 puntos netos el jugador que sabotea
  contra uno que no (~1,4 sabotajes por guardia). El sabotaje es una
  herramienta, no la estrategia obligatoria.
- **El precio de la interacción es tempo, no sangre:** el piso impide
  rematar, pero cada −1 y cada limpieza atrasan un ✅ y el deterioro cobra.
- **"No se me fue nadie" queda en 3,2% bajo IA despiadada.** En mesa,
  donde nadie ataca óptimo y existe *El Que Guarda Siempre Tiene* como
  escudo, debería quedar entre 3 y 6%. Si tras el playtest se siente
  imposible, el candidato es "≤1 ✝️: +2" — pero medido, ≤1 ✝️ ocurre el
  45% de las veces: sería regalo. **Mejor milagro que regalo.**
- **El piso universal es la regla-maestra del balance:** al experto no le
  cambia un decimal; al novato le devuelve 6 puntos de salvamento y le
  quita la peor experiencia posible (matar a su propio paciente por no
  leer la letra chica). Y regala la jugada heroica del ROJO en 1 ❤️.
- **El Sumario volvió a morder la mano** porque el castigo en puntos
  fracasó dos veces: el martillo (−3 al peor) golpeaba al que ya perdía
  9 de cada 10 veces, y el cierre con colocación hacía que nadie cerrara
  nunca (0%). Con mordida + cierre de 2 cartas: **94% se cierran** — el
  Sumario vuelve a ser una factura que se paga, no una lápida.
