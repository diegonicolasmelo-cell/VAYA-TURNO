# Inventario de mecánicas — ¡VAYA TURNO! v0.21

> Todas las frecuencias vienen de **4.000 partidas simuladas** (2 jugadores,
> 64.000 turnos-jugador, 186.160 indicaciones). Una mecánica que casi no
> dispara cuesta reglamento y no paga.

---

## 1. El reencuadre: no cuentes mecánicas, cuenta decisiones

El juego tiene **20 mecánicas** pero eso no es la métrica correcta. Lo que
carga al jugador no es cuántas reglas existen, sino **cuántas decisiones tiene
que tomar por turno** y **cuántas reglas tiene que recordar que NO están
pasando**.

| Familia | Cuántas | Carga por turno |
|---|---:|---|
| **Automáticas** (el motor las resuelve solo) | 4 | cero |
| **Decisión cada turno** | 5 | **la carga real** |
| **Decisión ocasional** (llega con la carta) | 5 | baja, la carta lo recuerda |
| **Fase opcional** (puedes saltarla) | 3 | baja |
| **Subsistemas** | 3 | media |

Cinco decisiones por turno es **sano**. Battlegrounds tiene más. El problema
de ¡Vaya Turno! no es el número: es que **tres mecánicas disparan tan poco, o
tan en falso, que el jugador paga su reglamento sin recibir el juego**.

---

## 2. Las automáticas — 4, todas sanas

| Mecánica | Qué hace | Frecuencia | Veredicto |
|---|---|---:|---|
| **Deterioro** | −1 ❤️ por ronda a todo no-✅ | siempre | ✅ **Es el reloj. Es la tesis.** No tocar |
| **Estabilización ✅** | completar requisitos detiene el reloj | 0,35/turno | ✅ la única forma de comprar tiempo |
| **Alta** | ✅ de la ronda anterior → puntos | 0,35/turno | ✅ la ventana de consolidación crea el sabotaje |
| **Muerte ✝️** | 0 ❤️ → penalización | 0,17/turno | ✅ |

**Ventaja:** cero carga cognitiva, generan toda la tensión.
**Desventaja:** ninguna medida. Son el suelo del juego.

---

## 3. Decisión cada turno — 5, todas sanas tras v0.20

| Mecánica | Frecuencia | Veredicto |
|---|---:|---|
| **Colocar recursos** | 2,91/turno | ✅ el verbo central |
| **Tope de 3** | choca el **93,5%** de los turnos | ✅ **la mejor regla de v0.20**: convierte "descargar la mano" en "elegir" |
| **Elegir a quién** | cada indicación | ✅ el corazón del triage |
| **Descarte por límite de mano** | muerde el **16,6%** de los turnos | ✅ frecuencia correcta: duele sin ser rutina |
| **Admisión opcional** | 0,18 camas vacías/turno | ✅ nueva en v0.20, ya se usa |

---

## 4. Decisión ocasional — 5, con dos problemas graves

| Mecánica | Frecuencia | Veredicto |
|---|---:|---|
| **⚠️ Complicaciones** | 0,78/turno · **1,0% no hace nada** | ✅ **arreglada en v0.21**: las 18 quitan 1 ❤️ |
| **🛡️ Protecciones** | ~6% de su complicación · 1,0% del total | 🔶 mejor, pero sigue siendo rara de ver |
| **Sinergia ×2** | 12,8% de las indicaciones | ✅ 1 de cada 8 — frecuencia ideal |
| **Comodín 🃏** | 4,9% (3 cartas) | 🔶 marginal pero barato |
| **Restricción ⚑** | 4,6% (2 cartas) | 🔶 marginal pero barato |

### 4.1 El problema grande, resuelto en v0.21

**Hasta v0.20, una de cada cuatro ⚠️ era teatro**: dabas vuelta la carta,
leías el nombre, buscabas la víctima según su 🎯… y no pasaba nada. El 27,3%,
y no repartido al azar — fallaban **las seis que descartaban un recurso**
(entre 74% y 86% cada una) y **ninguna** de las que quitaban ❤️ o subían un
requisito. El motivo era estructural: para descartar un 💊 del paciente
señalado, ese paciente tenía que *tener* un 💊 puesto, y con 3 indicaciones
por turno repartidas entre tres camas casi nunca lo tenía.

**v0.21 lo cierra unificando el efecto: las dieciocho quitan 1 ❤️ al paciente
que señala su 🎯.** Una regla, dieciocho nombres. El teatro bajó a **1,0%**, y
ese 1% es un 🛡️ previniendo — el único "no pasa nada" que el jugador quiere
ver. La medición completa, y por qué hubo que re-tasar el Gravedad III para
pagarlo, está en `DISENO.md` §4j.

### 4.2 El problema chico: las protecciones se ven poco

v0.21 las mejoró de rebote —ya nada más borra al protector de la cama— y
pasaron de 1,2% a ~6% de su propia complicación: la Bacteriemia se previene el
8,5% de las veces, la NAVM el 6,3%, el Delirium el 3,2%. Aun así son 3 cartas
cubriendo 3 complicaciones de 18, y parte del número es artefacto (la IA no
planifica la secuencia protector→procedimiento y un humano sí).
**Todavía se puede jugar una partida entera sin ver una protección funcionar.**

---

## 5. Fase opcional — 3, la zona más débil del juego

| Mecánica | Estado |
|---|---|
| **Canje** (comprar Acción) | 🔶 v0.20 lo mejoró a 2-elige-1. Antes se saltaba sin pensarlo |
| **Trueque** (con un rival) | 🚨 **nunca medido, nunca usado en playtest.** Sospechoso de estar muerto |
| **Jugar Acción** (máx. 1) | ✅ pero depende del Canje para existir |

El simulador **no juega Acciones**, así que toda esta fase es territorio de
mesa. Lo que sí sabemos: en dos partidas físicas seguidas el autor saltó El
Pasillo completo sin dudarlo.

---

## 6. Subsistemas — 3

| Mecánica | Medición | Veredicto |
|---|---|---|
| **Sumario Administrativo** | dura **1,00 rondas** de media, se cierra al turno siguiente el **100%** de las veces | 🔶 **no es una maldición, es una factura** |
| **Pasivas de personaje** | 22 avatares, 10 medidos en banda | ✅ dan identidad, 2-elige-1 absorbe el desbalance |
| **Tutores / robo rival** | dentro de Acciones | 🔶 no medible |

### 6.1 El Sumario no hace lo que dice hacer

El reglamento lo vende como maldición: ocupa la mano, reduce tu límite,
cuesta 2 recursos cerrarlo, no puedes cerrarlo el mismo turno. Cuatro reglas
y un tipo de carta físico (6 cartas).

Lo que **realmente** ocurre: llega, y al turno siguiente se paga. Siempre.
Su efecto neto es *"cuando se te muere un paciente, descarta 2 cartas"*.

---

## 7. Qué sobra

**1 · ~~La implementación de "descarta un recurso" (6 cartas)~~ — hecho en
v0.21.** Se midieron las tres salidas (unificar a −1 ❤️, efecto alternativo,
retargeting) y **las tres endurecían el juego**, porque el 27% de teatro era
el amortiguador del balance. Ganó la unificación por ser la dosis mínima. La
familia "descartar un recurso" no desapareció: **se mudó a los Protocolos**
(*Vacaciones*), que es donde el jugador la juega mirando la mesa y por eso no
puede fallar.

**2 · El Sumario como carta física.** Si su efecto real es "descarta 2
cartas", podría ser una línea del reglamento en vez de un tipo de carta con
cuatro reglas propias. **Contra:** es el mejor chiste del juego, y el Director
del Hospital y la Gestora dependen de él. Decisión de sabor, no de mecánica.

**3 · Nada más.** Comodín y Restricción disparan poco (4,9% y 4,6%) pero
cuestan una línea cada uno y dan textura. No pagan reglamento caro.

---

## 8. Qué falta

**Mi recomendación es que no falta ninguna mecánica.** El juego tiene 20 y las
que tiene no están rindiendo. Agregar una más antes de arreglar las ⚠️ nulas
es construir sobre un piso flojo.

Dicho eso, hay **un hueco conceptual** real: no existe ninguna mecánica de
**información**. En un juego de triage, saber qué viene debería importar, y
hoy el futuro es opaco salvo por una carta (*Ojo Clínico*). Candidatas
baratas, para después del playtest:

- La **Urgencia visible**: el próximo paciente del mazo boca arriba, siempre.
  Cero cartas nuevas, cero reglas nuevas, y convierte "¿admito?" en una
  decisión informada.
- **Ronda de mañana**: al Fin de Guardia, mira la primera carta del Mazo de
  Guardia. Una línea.

El otro hueco es **interacción real entre jugadores**: el Trueque es el único
canal cooperativo y está probablemente muerto. Pero eso se arregla probándolo,
no agregando otro.

---

## 9. Dónde atacar, en orden

| # | Qué | Por qué | Estado |
|---|---|---|---|
| ~~1~~ | Arreglar las ⚠️ que no hacían nada | 27% de la mecánica más activa era teatro | ✅ **v0.21**: las 18 quitan 1 ❤️ (1,0% residual) |
| **1** | **Probar El Pasillo en mesa** | fase entera sin validar; se saltó 2 partidas seguidas | ⏳ **lo único que ya no se puede medir aquí** |
| ~~3~~ | A17 Quiebre de Stock | la carta más débil tras el tope de 3 | ✅ **v0.21**: fijada a 💊 Fármacos |
| ~~4~~ | Urgencia visible | cierra el hueco de información sin agregar cartas | ✅ **v0.21**: *Informe de Gestión de Camas* |
| **2** | Sumario: ¿carta o línea? | dura 1,00 rondas y se cierra el 100% de las veces | decisión de sabor, sin costo hasta decidir |
| **3** | Trueque | nunca medido, nunca usado | playtest |

Lo que **no** hay que tocar: el deterioro, la ventana de consolidación, el
tope de 3 y la sinergia. Los cuatro están midiendo sano y son el juego.
