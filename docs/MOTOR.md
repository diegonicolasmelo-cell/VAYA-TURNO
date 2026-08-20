# El motor TURNO — el juego sin el tema

*Nombre de trabajo.* Este documento describe **qué es el motor de ¡Vaya Turno!
cuando le quitas la UCI**, para poder reutilizarlo en otras profesiones sin
volver a diseñar desde cero — y, de paso, para saber qué es esencial y qué es
decorado en el juego que ya tenemos.

---

## 1. Las cinco piezas

Un juego corre sobre el motor TURNO si tiene estas cinco. Ni una más.

### 1.1 El reloj
Cada caso que tienes en mesa lleva un contador que **baja solo, cada turno**.
Si llega a cero lo pierdes, y perderlo cuesta puntos. Nunca tienes suficiente
para atender a todos: **la decisión central del juego no es cómo salvar un
caso, sino a cuál renunciar.**

> *Lo que cambia con el tema:* qué significa que el contador llegue a cero.
> En la UCI, el paciente muere. En otras profesiones casi nunca es la muerte
> — ver §3, que es la parte que hay que resolver en cada adaptación.

### 1.2 Cuatro monedas, no una
El caso no pide "8 puntos de tratamiento". Pide **cantidades por categoría**:
2 de esto, 3 de aquello, 1 de lo otro. Y las categorías son **cuatro**, ni
tres ni cinco.

Cuatro es el número por una razón concreta: con tres, la mano casi siempre
sirve y no hay escasez; con cinco, casi nunca sirve y el juego se atasca.
Cuatro deja la mano útil a medias, que es donde vive la decisión.

Las cuatro plazas, en abstracto:

| Plaza | Qué es | En la UCI |
|---|---|---|
| **SABER** | Reducir incertidumbre: ver qué tiene | 🩻 Imagen |
| **ACTUAR** | Intervenir directo sobre el cuerpo | 💊 Fármacos |
| **ACOMPAÑAR** | Tiempo humano cualificado | 🧑‍⚕️ Personal |
| **INTERVENIR** | Acto técnico que deja algo puesto | 💉 Procedimientos |

**No hay valores numéricos.** Se cuentan íconos, no se suman puntos. Esa es la
diferencia entre este motor y la versión anterior del juego, y es lo que lo
mantiene ágil en mesa.

**Sinergia:** algunos recursos llevan la marca de un subtipo del caso y
**cuentan doble** sobre un caso de ese subtipo. Eso convierte la mano en una
decisión de oportunidad: gastarlo ahora en el caso equivocado, o guardarlo.

### 1.3 La ventana de consolidación
Completar los requisitos **no cierra el caso**. Hay que aguantar una ronda más
con todo puesto. Durante esa ronda el caso está quieto, visible y vulnerable.

Esta es la pieza que hace que el juego sea rompeamistades: sin ella, los
ataques serían ruido; con ella, hay un momento exacto en el que duelen.

> *Lo que cambia con el tema:* cómo se llama la espera. En la UCI es la
> consolidación antes del alta. En odontología, **el control a los seis meses**.
> En rehabilitación, **el alta funcional que hay que demostrar**.

### 1.4 El veneno
Un mazo aparte de cartas de Acción, al que **solo se llega gastando recursos**
(el Canje: descartas 2, robas 1). Sirven sobre todo para estorbar al rival.

Que sean caras y de un mazo distinto es deliberado: obliga a elegir entre
tratar a tus casos o fastidiar a los ajenos.

> *Lo que cambia:* la burocracia y las miserias propias de esa profesión.
> Toda profesión tiene las suyas, y son el mejor material de humor que hay.

### 1.5 La maldición
Perder un caso no solo resta puntos: **deja papeleo** que se queda en tu mano
estorbando hasta que pagas por cerrarlo.

Convierte la derrota en fricción continua en vez de un número al final. Y es
donde el juego dice su verdad más incómoda: lo que más duele de perder a
alguien es el formulario.

---

## 2. Los dos parámetros que se recalibran

Todo lo demás es contenido. Estos dos son los que hay que volver a calcular
en cada tema, y para eso existe `tools/simular.py`:

1. **El robo por turno.** Es la perilla maestra. En ¡Vaya Turno! pasar de 3 a
   5 movió el salvamento del 32% al 65%. Cualquier otro ajuste es fino
   comparado con este.
2. **La composición del mazo.** Se deriva de la demanda agregada de los casos:
   si el 34% de lo que piden los casos es de la categoría ACTUAR, el 34% del
   mazo debe serlo.

Objetivos de diseño que un tema sano debe cumplir:

- Casos resueltos: **55–70%** (salvas la mayoría, siempre pierdes a alguien)
- **2–3 cierres** por jugador y partida
- Partida perfecta: **5–15%** de las veces — una hazaña, no un plan
- Los casos más difíciles: **40–50%** de éxito

---

## 3. El problema que aparece en cada adaptación

**Fuera de la UCI, el reloj deja de ser la muerte.** Y si lo copias tal cual,
el juego pierde su tensión y queda como una lista de tareas.

La buena noticia es que casi siempre hay un reloj mejor, y suele ser **más
verdadero** que el de la UCI porque es el que de verdad angustia a esa
profesión:

| Tema | El contador es… | A cero… |
|---|---|---|
| **UCI** | la vida | Alta Celestial |
| **Odontología** | la paciencia y el bolsillo | abandona el tratamiento |
| **Rehabilitación** | la adherencia | deja de venir |
| **Nutrición** | la motivación | vuelve a lo de antes |
| **Fonoaudiología** | la ventana de plasticidad | se cronifica |

Fíjate en el patrón: en la UCI el enemigo es la biología; en el resto es
**que la persona se va**. Eso no es un problema del motor, es el hallazgo:
en la mayoría de las profesiones de la salud el fracaso no es la muerte,
es el abandono. Un juego que ponga eso en el centro dice algo cierto.

---

## 4. Mapeos esbozados

### 4.1 Rehabilitación musculoesquelética
*Casos:* fractura de fémur, rotura del manguito rotador, lumbago crónico,
esguince del que "ya está bien", hombro congelado, postoperado de LCA.

**El reloj: la adherencia.** Cada turno sin avanzar, el paciente pierde
motivación. A cero, deja de venir — y el tratamiento a medias deja peor
funcionalidad que no haber empezado.

> **Nota sobre las cinco categorías.** Enumeraste analgesia, terapia manual,
> fisioterapia, apoyo psicológico y el tratante, y te diste cuenta de que eran
> cinco para cuatro plazas. La salida no es descartar una: **lo psicológico no
> es una categoría, es el reloj**. La adherencia *es* el contador. Con eso
> quedan cuatro limpias:

| Plaza | Categoría | Ejemplos |
|---|---|---|
| SABER | 🔍 **Evaluación** | Goniometría, test funcional, eco musculoesquelética, RM |
| ACTUAR | 💊 **Analgesia** | AINE, infiltración, crioterapia, punción seca |
| ACOMPAÑAR | 🙌 **Terapia** | Terapia manual, ejercicio supervisado, el kine, el equipo |
| INTERVENIR | ⚙️ **Agentes y órtesis** | Ultrasonido, onda corta, TENS, férula, bastón |

*Subtipos para la sinergia:* hombro, rodilla, columna, cadera, mano.

*Eventos adversos:* **quemadura por agente físico**, **caída de la camilla**,
brote de dolor, recidiva, el que hizo crossfit el fin de semana, el que
googleó que el ejercicio le va a romper el disco, alta del seguro.

*Avatares:* el Kine FIT, el Sacavueltas, el de la máquina milagrosa, el
Senior que trata todo con manos, el que manda 40 ejercicios por WhatsApp.

### 4.2 Odontología
**El reloj: la paciencia y el presupuesto.** A cero, se cambia de consulta.

SABER = radiografía y sondaje · ACTUAR = procedimiento (obturación,
endodoncia, exodoncia) · ACOMPAÑAR = sillón, higienista, tiempo de box ·
INTERVENIR = prótesis, ortodoncia, férula.

*Subtipos:* caries, periodoncia, endodoncia, ortodoncia, cirugía.
*Consolidación:* el control a los seis meses.

### 4.3 Nutrición
**El reloj: la motivación.** A cero, vuelve a lo de antes.

SABER = antropometría y exámenes · ACTUAR = plan alimentario ·
ACOMPAÑAR = consulta y seguimiento · INTERVENIR = suplementación y soporte enteral.

Es el tema más difícil de los cuatro: el fracaso es lento y poco dramático.
Necesitaría un reloj más largo y probablemente una partida más corta.

### 4.4 Fonoaudiología
**El reloj: la ventana.** A cero, se cronifica.

SABER = evaluación deglución/voz/lenguaje · ACTUAR = maniobras y ejercicios ·
ACOMPAÑAR = sesión y familia entrenada · INTERVENIR = espesantes, adaptaciones,
comunicación aumentativa.

---

## 5. Arquitectura de producto sugerida

**Producto principal: la UCI. No lo diluyas a "hospital".** Tres razones:

1. La UCI es donde el motor funciona **sin traducción**: el reloj es literal.
   Es el mejor escaparate de lo que el motor sabe hacer.
2. Lo específico vende mejor que lo genérico. "Diriges una UCI" es una premisa;
   "trabajas en un hospital" es un escenario.
3. Y la razón práctica: si el producto base se llama *Hospital*, **te comiste
   el paraguas**. ¿Qué le queda entonces a las expansiones y a los demás
   títulos? Manteniendo la UCI acotada, todo lo demás cabe encima.

```
              motor TURNO
                   │
   ┌───────────────┼────────────────┬─────────────┐
   │               │                │             │
¡VAYA TURNO!   (título 2)       (título 3)    (título 4)
   UCI         Rehabilitación   Odontología   Nutrición
   │
   ├── Módulo Neurocrítico
   ├── Módulo Respiratorio
   ├── Módulo Cardiovascular
   ├── Módulo Quirúrgico
   └── Módulo Metabólico
```

Cada título es **su propia caja**, no una expansión: cambia el reloj, cambian
las cuatro categorías y cambia el público. Comparten motor, no componentes.

> **El orden importa.** Nada de esto se toca hasta que ¡Vaya Turno! esté
> jugado en una mesa de verdad. Un motor que nadie ha probado no es un motor:
> es una hipótesis con cinco temas encima.
