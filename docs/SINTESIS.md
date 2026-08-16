# Síntesis del material histórico — y qué se hizo con cada cosa

Enviaste: el PDF original (*"Juego de Mesa UCI: Salvando Vidas"*), el DOCX con
el barrido de 40 cartas, y seis conversaciones con distintos asistentes. Este
documento ordena ese material, dice **qué entendí**, **qué quedó integrado**,
**qué quedó estacionado y por qué**, y **qué decisiones siguen abiertas**.
El §4-bis cubre el Excel `CARTAS.xlsx`, integrado en v0.11.

> El Notion (`app.notion.com/p/CARTAS-...`) está bloqueado desde este entorno.
> Expórtalo como CSV (⋯ → Export → Markdown & CSV) y lo integro directo a
> `cartas/`.

---

## 1. Lo que entendí: tu juego pasó por tres eras

Trabajaste dos años sin plan, pero no trabajaste en círculos: cada era
**simplificó** a la anterior. Eso es exactamente la dirección correcta.

### Era 1 — "Salvando Vidas" (el PDF)
Simulación clínica seria con humor incidental. Pacientes con contador de
**supervivencia** (ej. 10), tratamientos que suman (+3 el Prono), requisitos
de personal específico (1 enfermero + 1 TENS + 1 kine), consecuencias
diferidas (el Prono lesiona la piel a los 2 turnos), contramedidas exactas
(la Convulsión se anula con benzodiacepinas). Puntos: +5 egreso, −3 muerte,
−10 te elimina.

**Diagnóstico:** esta era es injugable y tú ya lo sabías — lo dijiste
textual: *"era inviable compatibilizar lo clínico con el juego en sí"*. Cada
carta necesitaba conocimiento médico para jugarse. Pero de aquí sobreviven
las mejores ideas de sabor: el Prono, la autoextubación, el paciente
chagásico, la evidencia como chiste.

### Era 2 — "Estabilidad" (las conversaciones con Gemini)
Pacientes con **meta numérica** (10/15/20), recursos con **valor** (+1/+2/+3),
suma ≥ meta → egresa. Puntos de Acción (3 PA), moneda para cartas inestables,
staff con valores de estabilidad (Vieja Escuela 5, Especialista Arrogante 6),
prestigio (salvados − fallecidos, primero en +3 gana).

**Diagnóstico:** más jugable, pero el sistema de sumas tiene dos problemas
conocidos en diseño: (a) contabilidad constante — cada turno todos suman
columnas de números — y (b) los recursos se vuelven intercambiables: si todo
es "+2", da igual qué le pongas al paciente, y la decisión clínica
desaparece. La Era 3 lo resolvió mejor.

### Era 3 — "Categorías" (tu descripción de memoria, la del primer día)
La que me dictaste al empezar: **cuatro categorías de recursos** (🩻 imagen,
💊 fármacos, 🧑‍⚕️ personal, 📈 monitoreo), el paciente pide *cantidades por
categoría*, contador de vida que baja por turno, estabilización + **una ronda
de consolidación** antes del alta.

**Diagnóstico:** esta es la versión buena y es la que está construida y
simulada. Reemplaza la suma de valores por *matching* de categorías: cero
aritmética, la decisión sigue siendo clínica ("¿a quién le doy el único
monitoreo?"), y compatible con tu decisión de aplanar los medicamentos a
"fármacos". **El motor actual es la Era 3. No se retrocede.**

---

## 2. Lo que las conversaciones SÍ aportan — integrado en v0.10

Estas cinco cosas de las eras anteriores son mejores que lo que yo había
puesto de relleno, y ya están dentro:

### a) Los 6 avatares (reemplazan a mis placeholders)
Tus personajes con tus mecánicas, adaptados solo en vocabulario al motor v0.10:

| Avatar | Frecuencia | Habilidad (esencia tuya) |
|---|---|---|
| **El Diostor** | 1×ronda | Desvía el Evento Centinela de un ⚠️ al jugador de tu derecha |
| **El Médico Fantasma** | pasiva | Rondas 1–3 roba 1 menos; desde la 4, roba 1 extra siempre |
| **Doctor Amor** | 1×partida | Roba un 🧑‍⚕️ Personal de un paciente rival |
| **El Director del Hospital** | 1×partida | Anula un Sumario, de quien sea (favor cobrable) |
| **La Gestora de Camas** | 1×turno | Devuelve un paciente al fondo del mazo y admite otro; no cuenta como muerte |
| **El Médico Esotérico** | 1×turno | Revela la 1ª carta del Mazo de Guardia: recurso → gratis a un paciente; ⚠️ → el evento explota + descartas 1 |

*Adaptación del Esotérico:* tu versión duplicaba el valor del recurso, pero
en v0.10 los recursos no tienen valor numérico — el equivalente es que el
recurso entra **gratis** (no gasta carta de tu mano). Mismo riesgo/premio,
misma gracia.

### b) Alta Celestial + Sumario Administrativo
Tu eufemismo y tu carta de maldición, tal como los definiste: morir se llama
**Alta Celestial**, y deja un **Sumario** en tu mano (límite de mano −1, no
jugable, no descartable). Elegí una vía de escape concreta porque en las
conversaciones quedaron 3 opciones sin decidir: **cerrar el caso cuesta 2
recursos** — la misma moneda del Canje, para que el juego tenga una sola
economía. El Director lo anula gratis, como querías. *(Simulado: cuesta ~1
punto por partida y no genera espiral de muerte. Ver §4.)*

### c) Mazos separados + el Canje
Tu decisión de los "split decks", literal:
- **Mazo de Guardia** (63 recursos, con los ⚠️ mezclados — el miedo a robar
  que querías conservar).
- **Mazo de Protocolos** (45 acciones). Se accede solo por **Canje**: descarta
  2 recursos → roba 1 acción, máximo 1 canje por turno, acciones cuestan 0.

Esto convierte las cartas repetidas en oportunidad (tu argumento) y de paso
resolvió un defecto de mi v0.9 que no te había señalado: con las acciones
mezcladas en el mazo, el 29% de tus robos eran cartas que quizás no querías.
Ahora robas puro recurso y *eliges* cuándo convertir sobras en veneno.

### d) Anda Rondando la Pelada
Carta **única** en el mazo de Protocolos. Jugable solo si un rival tiene
**2+ ✝️** (tu "Espiral de la Muerte" — mismo umbral, misma función). Dos
monedas: dos caras → un paciente de ese rival recibe el Alta Celestial;
cualquier otra cosa → descartas toda tu mano.

*Adaptación deliberada:* tu versión original era **victoria instantánea**.
La bajé a "mata un paciente" en el modo base porque en un juego de puntos
por triage, un botón de victoria por moneda invalida las 7 rondas anteriores.
**Pero tu versión existe como variante oficial** ("Modo Pelada Letal",
Reglamento §11) — si en la mesa la versión suave no da miedo, activas la
letal y listo. Esto es una decisión tuya que revertí parcialmente: si la
quieres letal en el modo base, se cambia en un minuto.

### e) La moneda
Entra al juego por la puerta que le corresponde: la Pelada (y la variante
letal). No la generalicé a "cartas inestables" (el Becado, el Kine
Sacavueltas) — ver §3.

---

## 3. Lo que quedó estacionado — y el porqué de cada uno

Nada de esto está "rechazado". Está en la banca, con su razón:

| Idea | Por qué está en la banca |
|---|---|
| **Sistema de estabilidad numérica** (metas 10-20, recursos +1/+2/+3) | Es la Era 2. El matching por categorías hace el mismo trabajo sin aritmética. Volver atrás significaría rebalancear todo desde cero. |
| **Puntos de Acción (3 PA)** | La simulación mostró que limitar jugadas no cambia el balance (el cuello de botella es el robo) — un límite que no muerde es una regla que sobra. El "1 Acción/turno" cumple la función anti-abuso. |
| **Moneda en cartas de staff** (Becado, Sacavueltas, Esotérico-staff) | En v0.10 el personal son recursos anónimos apilables, no cartas con identidad en mesa. Meterles moneda individual = frenar el juego en cada colocación. El RNG vive concentrado en el avatar Esotérico y la Pelada, donde es un momento, no un trámite. **Si el playtest pide más caos, la banca está llena.** |
| **Staff con habilidades** (Vieja Escuela inamovible, TENS con sinergia, Especialista solitario) | Ídem: exige que el personal sean cartas únicas. Es la expansión natural #1 — "Personal con Nombre" — cuando el core esté probado. |
| **Dados como vitalidad** (tablero con monitor para d6) | El contador de vida ya lo hace con fichas. El d6 en el monitor es una idea de *producción* (y es muy buena) — no cambia reglas, cambia componentes. Va en el tablero final. |
| **Eliminación por −10 puntos** | Eliminar jugadores en un juego de 40 minutos deja gente mirando el techo. La presión de los ✝️ ya existe vía Sumarios + Pelada. |
| **"Primero en +3 gana"** | Final por carrera hace que el que arranca bien gane siempre; el final por rondas fijas permite remontadas y planificar el triage. |
| **Modo cooperativo / campaña / roles por equipo** | Post-playtest. Está esbozado en Reglamento §11 (Modo Brote). |
| **Tablero de doble capa + cartas deslizadas bajo el paciente** | La mejor idea de producción de todo el material (el "riel" que conecta el tubo al paciente es oro). No afecta reglas. Cuando el juego esté probado, esa dirección de arte ("Guardia Nocturna Eterna") es la que financiaría en imprenta. |
| **Arquitectura web app** (React/Node/Socket.io) | Correcta en general, pero es el paso 10 y estás en el 3. El informe de Gemini sobrevive; los CSV de `cartas/` ya son la base de datos que esa app consumiría. |

---

## 4. La matemática v0.10 (re-simulada tras integrar tus decisiones)

Separar los mazos cambió la economía entera: al sacar las 24 acciones del
mazo, cada robo es 100% recurso, así que **el robo bajó de 5 a 4** (y de 4 a
3 con cuatro jugadores). Validado sobre 2.000–3.000 partidas por configuración:

| Config | Salvamento | Altas | Fallecidos | Pts | Limpias |
|---|---:|---:|---:|---:|---:|
| 2 jug · 3 camas · robo 4 · 8 rondas | 65% | 2,6 | 1,4 | 6,3 | 14% |
| **3 jug · 3 camas · robo 4 · 8 rondas** | **65%** | **2,5** | **1,4** | **6,1** | **14%** |
| 4 jug · 2 camas · robo 3 · 10 rondas | 62% | 2,1 | 1,3 | 4,6 | 16% |

El **Sumario cuesta ~1 punto por partida** (6,1 con sumario vs 6,9 sin él) y
la tasa de guardias limpias no se mueve → castiga sin crear espiral de
muerte. Es exactamente el "entorpece un poco" que pediste.

Con robo 5 y mazos separados el juego se regalaba (77% salvamento, 24%
limpias): por eso el número bajó. **Si tocas la composición de mazos, corre
`python3 tools/simular.py` antes de imprimir nada.**

Lo que la simulación sigue sin ver: los 6 avatares y las 25 acciones. El
suelo está validado; el techo se mide en la mesa (plan en `PLAYTEST.md`).

---

## 4-bis. El Excel `CARTAS.xlsx` (integrado en v0.11)

126 filas, de las cuales **74 sin efecto escrito** — un inventario de nombres
más que un set de cartas. Pero los ~52 con efecto traían cuatro cosas que el
juego no tenía:

| Rescatado | Qué era en el Excel | Cómo quedó en v0.11 |
|---|---|---|
| **Sistemas + sinergia** | Pacientes con subtipo (Respiratorio, Cardíaco…) y recursos con *"+1 si se aplica en ASMA/EPOC"* | Los 26 pacientes tienen sistema; 24 recursos son específicos y **cuentan doble** en su sistema. Sin aritmética: se cuentan íconos, algunos valen por dos |
| **Restricciones como costo** | RNM *"en este turno solo puedes jugar esta carta"*; TAC *"solo con 3 personal en juego"* | Resonancia consume tu turno de recursos; TAC exige 1 🧑‍⚕️ sobre el paciente. Lo mejor diseñado del archivo |
| **Comodines** | *Médico General* y *Dios-tor* como recurso comodín | 3 comodines (*Médico General de Turno*, *Stock de Sala*). Anti-brick validado |
| **Vocabulario** | "Evento Centinela", "¿Y si vamos por un cafecito?", Liceeeencia!, Estás Despedido | Adoptados: el mazo se llama ahora **Eventos Centinela** |

También se escribieron efectos para **13 eventos centinela** que en el Excel
eran solo títulos (VILI, Neumotórax a tensión, Bacteriemia, Resistencia
antibiótica, Sobresedación, Bradicardia extrema, TV, Falla renal…) y para
**9 acciones nuevas** (Ojo Clínico, Receta en Blanco, Quiebre de Stock,
Recorte Presupuestario, Paro de Funcionarios, Convivencia de Servicio,
Muestra Hemolizada, Capacitación, Simulación Clínica).

**Lo que quedó fuera del Excel:** el sistema de valores 1–5 (es la Era 2);
ocho antibióticos mecánicamente idénticos; cinco kinesiólogos casi iguales
(sobreviven como nombres y arte, no como cartas distintas); once "Médico"
genéricos; y el *reloj de eventos* (*"reduce en 1 los turnos para que ocurra
un evento"*), que duplicaría la contabilidad que el ⚠️ ya resuelve.

**Los ~20 efectos de personal** del Excel asumen que el personal son cartas
con identidad en mesa, y en v0.11 siguen siendo recursos anónimos. Los mejores
se convirtieron en cartas de **Protocolo** (Ojo Clínico ← Kine Geek; Receta en
Blanco ← Enfermera Especialista). El resto espera la expansión *"Personal con
Nombre"*.

---

## 5. Decisiones que siguen siendo tuyas

1. **¿Pelada letal o Pelada suave en el modo base?** Hoy: suave en base,
   letal como variante. Un minuto de cambio si lo quieres al revés.
2. **El Notion.** Sin el CSV no sé qué cartas de esa tabla no están cubiertas
   por las 174 actuales. Expórtalo y hago el diff.
5. **El reparto de sistemas.** Los 26 pacientes se asignaron por criterio
   clínico (Shock Séptico → cardíaco, Pancreatitis → quirúrgico, Delirium →
   neuro). Revísalo: es tu juego y tu criterio manda. Está en la columna
   `sistema` de `cartas/pacientes.csv`.
3. **Avatares asimétricos.** Amor y el Director juegan 1 vez por partida;
   Fantasma y Esotérico, todos los turnos. Puede estar bien (Exploding
   Kittens vive de eso) o puede sentirse plano. Si el playtest lo confirma,
   la corrección es darles una pasiva menor (sugerencias en `DISENO.md` §5).
4. **"Vaya Turno" con o sin ¡!** — está escrito de las dos formas en tu
   material. Hoy los archivos dicen "¡Vaya Turno!".

---

## 6. Mi feedback honesto, en cinco líneas

1. **El juego ya está diseñado.** Lo que tenías no era un juego a medio
   hacer: eran tres juegos superpuestos. La Era 3 es la buena; las otras dos
   son canteras de contenido, no de reglas.
2. Tus tres mejores ideas de mecánica son la **ronda de consolidación**, el
   **⚠️ dentro del mazo de recursos** y el **Canje**. Las tres están en el core.
3. Tu mejor idea de tono es el **Sumario**: convierte la muerte en burocracia,
   que es el chiste más verdadero de todo el juego.
4. El riesgo #1 del proyecto ya no es diseño ni matemática: es que lleves
   **dos años sin ponerlo en una mesa**. Todo lo que queda por decidir se
   decide jugando. `pnp.html` tiene 141 cartas listas para imprimir hoy.
5. La app web, el tablero troquelado y el arte final son premios por terminar
   el playtest — no requisitos para empezarlo.
