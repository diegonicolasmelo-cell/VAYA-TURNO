# Notas de diseño — ¡Vaya Turno!

Este documento existe para una sola cosa: que dentro de seis meses sepas
**por qué** cada número es el que es, y no vuelvas a empezar de cero.

---

## 1. El corazón del juego

> **No puedes salvarlos a todos, y el juego lo sabe.**

Todo lo demás es decoración alrededor de eso. Tres camas, un ingreso de
recursos insuficiente, y un reloj que corre en las tres a la vez. La decisión
interesante no es *"¿cómo salvo a este paciente?"* sino **"¿a cuál dejo ir?"**.

Consecuencia de diseño: **cualquier cambio que permita salvar a los tres
pacientes rompe el juego.** Si un playtest sale con todo el mundo salvando
todo, el problema no es que falte dificultad — es que se perdió el tema.

Segundo pilar, el que lo hace rompeamistades:

> **El momento más vulnerable de un paciente es cuando ya está salvado.**

Por eso existe la ronda de consolidación. Un paciente ✅ Estabilizado está
quieto, visible y a un *Vacaciones* de volver a morirse. Sin esa ventana, las
cartas de ataque serían ruido; con ella, son el clímax de cada ronda.

---

## 2. Qué estaba sin resolver y cómo se cerró

| Hueco | Decisión | Por qué |
|---|---|---|
| ¿Cuándo termina la partida? | 8 rondas fijas (10 con 4 jug.) | Un final fijo permite planificar el triage. Un final variable ("cuando se acabe el mazo") vuelve el último tercio impredecible y castiga al que va invirtiendo a largo plazo. |
| ¿Se rellenan las camas? | Sí, siempre, en la Entrega de Turno | Camas vacías = descanso. En este juego no hay descanso. Además evita la estrategia degenerada de "dejo morir a todos y no admito a nadie para no perder puntos". |
| ¿Qué pasa con el paciente estabilizado? | Se detiene el reloj, alta una ronda después | Idea original tuya, y es la mejor del juego. Se conserva intacta. |
| ¿Se puede perder el ✅? | Sí, al instante, si deja de cumplir requisitos | Es lo que da filo a todos los ataques. Los recursos sobrantes hacen de colchón — eso premia sobre-tratar a un paciente valioso. |
| ¿Cuántas cartas se juegan por turno? | Recursos ilimitados, **1 sola Acción** | La simulación mostró que limitar recursos no cambia el balance (el cuello de botella es el robo), solo añade una regla. En cambio limitar Acciones sí importa: sin ese tope, una mano con 3 ataques borra a un jugador de la partida. |
| ¿Cómo entran los eventos adversos? | Símbolo ⚠️ en 17 de las 63 cartas de Recurso, **con su complicación impresa** (v0.14) | Tu idea de "robar un evento al robar recursos". Ata el castigo al motor del juego: mientras más juegas, más te expones — y desde v0.14 el problema es el que ese recurso causa de verdad. |
| ¿Mazo único o mazos separados? | Guardia y Protocolos separados. **El mazo de Eventos se eliminó en v0.14** | La complicación vive impresa en la carta ⚠️ que la causa: menos componentes, un paso menos por turno, y coherencia clínica. Ver §4c. |
| Puntuación | Altas − Fallecidos + **"No se me fue nadie" (+3)** o **"Se hizo todo" (+1)** | El +3 evita que la estrategia dominante sea "sacrificar sin culpa". El +1 (v0.15) hace visible lo que ya medía la simulación: puedes perder a los difíciles, no a los fáciles. |

---

## 3. Anatomía de los pacientes

| Gravedad | ❤️ | Recursos | Alta | Fallece | Swing | n |
|---|---:|---:|---:|---:|---:|---:|
| I — Observación | 7 | 3 | +2 | −1 | 3 | 8 |
| II — Grave | 6 | 5 | +3 | −2 | 5 | 10 |
| III — Crítico | 5 | 7 | +5 | −2 | 7 | 6 |
| ★ Código Rojo | 5 | 8 | +8 | −3 | 11 | 2 |

**La penalización por muerte crece más lento que el premio por alta.** Es
deliberado: si un Crítico costara −5 al morir, nadie lo admitiría nunca y las
cartas más interesantes del mazo serían basura. Tal como está, admitir un
Crítico es una **apuesta con valor esperado positivo si crees que puedes
salvarlo ~40% de las veces** — y la simulación dice que se salvan el 40%.
Justo en el filo. Ese es el punto.

El **Código Rojo** (2 cartas) no está balanceado para ser eficiente: está para
que alguien lo intente, lo consiga una vez, y lo cuente durante meses.

**Oferta vs. demanda de recursos.** La composición del Mazo de Guardia se
derivó de la demanda real agregada de las 26 cartas de paciente:

| Tipo | Demanda | % | En el mazo | % |
|---|---:|---:|---:|---:|
| 💊 Fármacos | 44 | 33% | 20 | 33% |
| 🩻 Imagen | 31 | 23% | 14 | 23% |
| 💉 Procedimientos | 31 | 23% | 14 | 23% |
| 🧑‍⚕️ Personal | 26 | 20% | 12 | 20% |

Desde v0.16 las cuatro plazas van **parejas** (ratio oferta/demanda 0,452–0,462,
antes 0,44–0,48). El colchón que Personal tenía por ser el único tipo que las
cartas de ataque destruyen (*Vacaciones*, *Licencia*) resultó innecesario: al
medirlo, quitarlo no movió ninguna métrica fuera de banda.

> **Si añades pacientes nuevos, vuelve a correr `tools/simular.py`.** Cambiar
> la demanda sin cambiar el mazo desbalancea el juego en silencio.

---

## 4. Cómo se calibró el robo (y por qué no toques esto a ojo)

> **Actualización v0.12 — el reloj se movió al final del turno.** Las fases
> pasaron de seis a cuatro y recuperaron los nombres del hospital: **Entrega de
> Turno · El Pasillo · Pase de Visita · Fin de Guardia**. El cambio de fondo no
> es el nombre sino *dónde cae el deterioro*: antes abría el turno, ahora lo
> cierra, porque **cada Fin de Guardia es un día que pasa**. Consecuencia
> mecánica: un paciente en 1 ❤️ ya no muere antes de que puedas tocarlo — te da
> tiempo de intentarlo, y si falla, la muerte es resultado de tu turno.
>
> Eso regala medio turno de gracia a todo el mundo. Sin compensar, el
> salvamento subía a **70%** y las guardias sin fallecidos a **18,5%** (fuera de
> objetivo por arriba). Se pagó con dos ajustes chicos, elegidos por barrido:
>
> | Variante (3 jug., 3.000 partidas) | Salv. | Altas | Muertes | Limpias | GIII | ROJO |
> |---|---:|---:|---:|---:|---:|---:|
> | v0.11 · deterioro al inicio | 65% | 2,68 | 1,47 | 12,0% | 47% | 54% |
> | deterioro al final, sin tocar nada | 70% | 2,90 | 1,24 | 18,5% | 58% | 61% |
> | + sin día de gracia, ROJO ❤️4 | 59% | 2,64 | 1,82 | 6,7% | 41% | **38%** |
> | **v0.12 · sin gracia + ROJO ❤️5** | **61%** | **2,66** | **1,68** | **8,2%** | **40%** | **64%** |
>
> - **Se quitó el día de gracia del recién ingresado.** Con el deterioro al
>   final, esa gracia ya venía incluida por construcción; mantenerla la
>   duplicaba. Y temáticamente es más honesto: si ingresó hoy, hoy pasó un día.
> - **El Código Rojo subió de ❤️4 a ❤️5.** Es el único número de la tabla de
>   gravedades que cambió, y era obligatorio: sin él, ROJO se desploma al 38%.
>   Pide 8 recursos; con 4 días no alcanza aunque juegues perfecto.
>
> Se descartaron por el camino: bajar el robo a 3 (sobrecorrige a 54%), acortar
> a 7 rondas (limpias al 27,7%), y bajar 1 ❤️ a las gravedades I–III (aplana el
> gradiente: III y ROJO quedaban tan salvables como II).
>
> **Efecto secundario, honesto:** con 4 jugadores (2 camas, robo 3) la Gravedad
> III cae al 33%, dos puntos bajo el objetivo. Es el costo de una mesa con
> menos camas y menos robo, y **no se maquilló**: en esa configuración un
> Crítico es una apuesta que casi nunca conviene. Si en el playtest molesta, la
> perilla es pasar a 3 camas — pero entonces el Mazo de Pacientes se agota y el
> 29% de las camas termina vacío. Ese es el trade-off real y hay que verlo en
> mesa.

> **Actualización v0.11 — la sinergia.** Del Excel histórico se rescató la
> mejor mecánica que faltaba: los pacientes tienen **sistema clínico** y 24 de
> los 63 recursos son **específicos** de un sistema. El recurso correcto en el
> paciente correcto **cuenta doble**. Esto arregla un defecto real de v0.10
> que no se había señalado: dentro de cada tipo, todas las cartas eran
> mecánicamente idénticas — un TAC y una ecografía eran la misma carta con
> otro chiste.
>
> La sinergia sube el salvamento ~3 puntos y se paga subiendo los ⚠️ de 12 a
> 17. Se añadieron además **3 comodines**: bajan de 4,3% a ~2% la proporción
> de jugadores que terminan sin ninguna alta — el anti-brick pedido por el
> autor. Resultado v0.11 con robo 4: **65% de salvamento, 2,7 altas, 1,5
> fallecidos, 11,7% de guardias sin fallecidos.** Gravedad III sube a 47% (era 41%):
> los críticos ahora son apuestas más razonables porque su recurso específico
> los rescata más rápido.
>
> **Sobre el reparto por sistema — corregido.** Aquí se anotó que los
> recursos específicos debían emparejarse con los pacientes de cada sistema
> (hoy: CARD 5/5, RESP 4/4, NEURO 3/5, METAB 4/5, QUIR 5/7). Con el plan de
> expansiones por sistema (ver `EXPANSIONES.md`), **emparejarlos sería un
> error**: la caja base debe cubrir los cinco de forma pareja pero *fina*,
> para que ningún sistema quede agotado antes de su propio módulo. El único
> ajuste que quedaba era bajar RESP de 7 a 4, hecho en v0.12: la Ventilación
> Mecánica pasó a genérica, porque el ventilador también es del politrauma y
> del séptico. Sinergia total: 21 de 63.

> **Actualización v0.10:** tras integrar el material histórico (ver
> `SINTESIS.md`), las Acciones salieron del Mazo de Guardia hacia un mazo
> propio (Protocolos, accesible por Canje) y las muertes dejan Sumario.
> Con el mazo purificado a 60 recursos, **el robo bajó de 5 a 4** (de 4 a 3
> con cuatro jugadores): 65% de salvamento, 2,5 altas, 14% de guardias
> limpias, y el Sumario cuesta ~1 punto por partida sin espiral de muerte.
> Las tablas siguientes documentan la calibración v0.9 original (mazo único);
> el método es el mismo.

La primera versión (robar 3) producía una masacre: **31% de salvamento y
puntaje medio de −1,3**. Todos los jugadores terminaban en negativo. Es un
juego temáticamente correcto y emocionalmente insoportable.

Barrido de parámetros con `tools/simular.py` (3 jugadores, 3 camas):

| Variante | Salv. | Altas | Muertes | Pts | Limpias | GIII |
|---|---:|---:|---:|---:|---:|---:|
| robo 3 | 32% | 0,87 | 1,89 | −1,3 | 6% | 9% |
| robo 4 | 46% | 1,38 | 1,61 | +1,2 | 9% | 21% |
| **robo 5** | **60%** | **2,0** | **1,34** | **+4,1** | **15%** | **34%** |
| robo 4 + vida +1 | 62% | 1,45 | 0,88 | +4,1 | 37% | 31% |
| robo 4 + vida +2 | 84% | 1,50 | 0,28 | +6,8 | 75% | 74% |
| robo 4 + requisitos −1 | 54% | 1,60 | 1,35 | +3,2 | 17% | 27% |

**Por qué ganó "robo 5" y no las otras:**

- **Subir la vida** arregla la tasa de salvamento pero destruye la tensión:
  con vida +1, el 37% de las guardias terminan sin ningún fallecido. El bonus
  sin fallecidos deja de ser una hazaña y pasa a ser el default.
- **Bajar los requisitos** aplana las gravedades: los Graves y los Críticos
  empiezan a parecerse entre sí y la decisión de triage pierde textura.
- **Subir el robo** arregla el problema sin tocar la identidad de ninguna
  carta. El reloj sigue siendo igual de despiadado; simplemente tienes más
  con qué pelear.

**Configuración final validada — v0.12** (3.000 partidas por config):

| Jugadores | Camas | Robo | Rondas | Salv. | Altas | Muertes | Limpias | GIII |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 2 | 3 | 4 | 8 | 62% | 2,71 | 1,64 | 8,2% | 42% |
| 3 | 3 | 4 | 8 | 61% | 2,66 | 1,68 | 8,2% | 40% |
| 4 | 2 | 3 | 10 | 57% | 2,22 | 1,69 | 9,2% | 33% |

*(La tabla de arriba, con robo 5, documenta la calibración v0.9 sobre el mazo
único. Se conserva porque el método es el mismo y el barrido sigue siendo
válido como razonamiento.)*

Objetivos de diseño que había que cumplir simultáneamente:

- Salvamento **55–70%** → salvas la mayoría, pierdes a alguien siempre.
- **2–3 altas** por jugador → la partida se siente productiva.
- Cierres con "No se me fue nadie" **5–15%** → es una hazaña, no un plan.
- Gravedad III salvable **40–50%** → vale la pena intentarlo, no siempre sale.

La configuración de 4 jugadores queda con un **16% de guardias sin fallecidos**, un
punto por encima del objetivo. Se deja así: bajar el robo a 3 la devolvería al
rango pero hundiría el salvamento al 45%. Es la config menos afinada de las
tres, y la que más conviene revisar tras el playtest.

### Limitaciones honestas del simulador

Lee esto antes de confiar demasiado en los números de arriba:

- **No modela cartas de Acción**: la IA las descarta como cartas muertas
  (29% del mazo). En la mesa real, *Interconsulta*, *Cumpleaños del Residente*
  y *Doblo Turno* dan recursos, así que **el salvamento real será algo mayor
  que 60%**. Los ataques empujan en la dirección contraria. Se cancelan
  parcialmente, pero no sabemos en qué proporción hasta jugarlo.
- **No modela personajes.** Las seis habilidades están sin validar
  numéricamente. Son la principal fuente de sorpresa en el primer playtest.
- **No modela interacción entre jugadores** en absoluto: cada UCI se simula
  aislada. El "kingmaking" y las alianzas contra el líder son invisibles aquí.
- La IA de triage es codiciosa y buena, pero no óptima. Un jugador experto
  probablemente supere estos números; un jugador nuevo, no.

**En resumen: el suelo del balance está validado. El techo, no.** Por eso el
plan de playtest de `PLAYTEST.md` mide exactamente esas tres cosas.

> **Nota v0.14 — las complicaciones ya no se estiman: se miden.** Al pasar
> del mazo Centinela (evento aleatorio) a la complicación impresa en cada ⚠️,
> el simulador dejó de necesitar la abstracción 33/33/34 y aplica **las 17
> complicaciones exactas** con su 🎯 objetivo. Ver §4c.
>
> **Nota v0.13 — el 🎯 Objetivo acercó el juego a su simulación.** El simulador
> nunca dejó que el jugador eligiera víctima: los eventos de daño siempre
> pegaban al paciente **más avanzado** (`aplicar_evento`, línea 171). O sea que
> el 61% de salvamento se midió asumiendo objetivo adversario. Con la regla
> vieja ("elige el jugador afectado") la mesa real habría sido **más fácil que
> la simulación**, porque cualquiera mandaba el golpe al paciente ya perdido.
> El 🎯 Objetivo no endurece el juego respecto a los números publicados: lo
> pone de acuerdo con ellos.

---

## 4d. El bonus "Se hizo todo": por qué el "Fallece −1" engañaba (v0.15)

El autor preguntó lo obvio: si un Gravedad I solo resta 1 punto al morir,
**¿cuál es el incentivo para salvarlo?** Se midió poniendo en la mesa a un
jugador negligente contra dos normales (3.000 partidas):

| Estrategia del jugador 0 | Sus puntos | Rivales | Ventaja |
|---|---:|---:|---:|
| Normal | 7,51 | 7,17 | +0,34 |
| Nunca trata a los Gravedad I | 6,10 | 7,30 | **−1,20** |
| Los aparca y los trata al final | 6,99 | 7,30 | −0,31 |

**El incentivo ya existía** (−1,20) pero era invisible: la carta dice −1 y el
costo real ronda los 4 puntos entre el Sumario, la cama muerta media ronda y —
sobre todo— el bonus quemado (los cierres sin fallecidos del negligente caen del
10,8% al 1,6%). Eso no es un problema de balance: **es un problema de
legibilidad.** Un juego debe enseñar sus incentivos en la carta, no en la
derrota.

Se probaron dos arreglos:

| Arreglo | Ventaja negligente | Ventaja aparcar | Veredicto |
|---|---:|---:|---|
| Escala de Sumarios (2 al leve, 0 al ROJO) | −1,20 | — | **Descartado**: efecto cero. El +2 del leve y el 0 del ROJO se cancelan, y el Sumario es una palanca más débil de lo que sugería el caso de la Gestora (§4b). Una regla más a cambio de nada. |
| **"Se hizo todo" (+1)** | **−1,37** | **−0,47** | **Adoptado.** |

El nuevo bonus sube el disuasivo contra *aparcar* un **52%** — que era el punto
débil real, casi empatado —, salta en el **27,8%** de las guardias (suficiente
para perseguirla, no tanto para ser automática) y solo infla el puntaje medio
de 7,28 a 7,56.

> **Y de paso puso nombre a algo que el juego no decía:** el Gravedad I no vale
> por sus 2 puntos, vale por **lo rápido que libera la cama**. Tres recursos,
> alta, y vuelves a revelar dos pacientes. Sus 7 ❤️ no son permiso para
> ignorarlo: son el margen para elegir *cuándo* lo cierras.

**Efecto sobre la Gestora:** su Derivación quema **los dos bonus de cierre**,
no solo el de +3. Verificado: su ventaja pasa de +0,66 a **+0,63** — sigue en
banda.

---

## 4c. Las 17 complicaciones: cómo se calibraron (v0.14)

Al mover la complicación del mazo Centinela a la propia carta ⚠️, el balance
hubo que rehacerlo — y el primer intento salió mal de una forma instructiva.

| Intento | Salvamento | Limpias | Gravedad III |
|---|---:|---:|---:|
| v0.13 de referencia (mazo Centinela) | 61% | 8,2% | **40%** |
| 1º · 13 de 17 subían un requisito | 59% | 3,9% | **28%** |
| 2º · se cambiaron 5 a "descarta 1 recurso" | 63% | 5,9% | 31% |
| 3º · se abrió la puntería fuera del grave | 64% | 7,0% | 33% |
| **Final · 10 de 17 apuntan al que va bien** | **66%** | **10,5%** | **43%** |

**Tres lecciones que valen para cualquier complicación futura:**

1. **"+1 requisito" es el efecto más duro que existe, y lo es de forma
   desigual.** Al Gravedad I le sube la meta de 3 a 4; al III, de 7 a 8. Pero
   el III además tiene 5 ❤️ y no 7, así que no le alcanza el reloj para
   reponerlo. Trece cartas subiendo requisitos hundieron al III al 28%.
   La mezcla sana resultó **5 quitan ❤️ · 8 suben requisito · 6 descartan un
   recurso** — descartar es el efecto suave: repones la carta, no cambias la meta.
2. **`MAS_TRATADO` y `TÚ ELIGES` convergen los dos sobre el paciente grave.**
   El primero golpea donde invertiste; con el segundo, un jugador razonable
   descarga el daño en el que ya dio por perdido. Juntos hacían que el III
   absorbiera todo. Hoy solo **una** carta usa `MAS_TRATADO` (la Ventilación
   Mecánica, donde es clínicamente ineludible) y **dos** usan `ELIGES`.
3. **El criterio de balance no es el salvamento medio: es el valor esperado
   comparado.** Con el III al 33%, ir por un grave rendía +0,30 puntos contra
   +1,56 de un leve — cinco veces peor, y la decisión central del juego se
   volvía obvia. Con el reparto final: **III +1,04 vs I +1,33.** Sigue siendo
   más seguro el leve, pero el grave paga.

> **Consecuencia de diseño, no solo de números:** diez de las diecisiete
> complicaciones terminaron apuntando a *EL QUE MEJOR VA* o a *EL ✅
> ESTABILIZADO*. No fue una decisión estética — fue lo único que mantenía
> vivo al Gravedad III. Pero al llegar ahí, resultó ser también la frase que
> mejor describe el juego: lo que se complica no es lo que ya estaba perdido.

---

## 4b. La Gestora de Camas: la primera habilidad medida (v0.13)

Un avatar sí se puede medir, aunque el simulador no los modele de fábrica: se
le da la habilidad **a un solo jugador** y se compara su puntaje contra el de
sus dos rivales **en la misma mesa**. Lo hicimos con la Gestora porque su
Derivación era la sospechosa más obvia. 3.000 partidas por variante, 3
jugadores, configuración estándar.

| Variante | Ventaja sobre sus rivales | Guardias Limpias |
|---|---:|---:|
| Sin Gestora (control) | −0,18 | 8% |
| 1×turno, gratis (v0.12) | **+2,66** | **31%** |
| 1×partida, gratis | +2,12 | 25% |
| 1×turno + deja Sumario | +1,77 | 30% |
| 1×partida + deja Sumario | +1,18 | 24% |
| 1×turno + Sumario + rompe Limpia | +1,06 | 6,7% |
| **1×partida + Sumario + rompe Limpia (v0.13)** | **+0,66** | **6,3%** |
| 1×partida + Sumario + Limpia + −1 pt | −0,04 | 6,3% |

**Lo que enseñó la medición, y vale para cualquier habilidad futura:**

1. **Bajar la frecuencia casi no sirve.** De 1×turno a 1×partida solo se
   pierden 0,5 de los 2,7 puntos de ventaja, porque la oportunidad de derivar
   es rara por naturaleza: incluso sin límite, una IA razonable solo encuentra
   a quién derivar **0,9 veces por partida**. Si una habilidad se dispara poco,
   limitar cuántas veces puedes usarla no la arregla — hay que tocar el efecto.
2. **El daño real no estaba en los puntos, estaba en el bonus de cierre.** La
   Derivación gratis convertía una hazaña del 8% en un trámite del 31%. Toda
   habilidad que esquive fallecidos tiene que pagar ese bonus, o desfigura la
   estadística que le da sentido.
3. **El coste de tempo no es coste.** Probamos dejar la cama vacía hasta la
   siguiente Entrega de Turno (como una muerte): la ventaja no bajó, subió a
   +2,70. Perder una cama con un paciente condenado encima es un alivio, no un
   castigo. Cuidado con "compensar" con tempo en este juego.
4. **El Sumario sí muerde** (−0,9 en 1×turno): cuesta 2 recursos y −1 de mano,
   y eso se siente en la economía.
5. **Banda sana para una habilidad: +0,3 a +1,0 puntos.** Por debajo es un
   adorno; por encima elige al ganador en un juego cuyo puntaje medio es 6,3.
   El −1 punto extra la dejaba en −0,04: convertía la habilidad en una trampa.

> Reproducirlo: el parche del simulador está en el histórico de la sesión; la
> forma de medir (un jugador con la habilidad contra dos sin ella, misma mesa,
> misma semilla) es lo que hay que repetir para las otras cinco.

---

### 4e. Soporte Vital → 💉 Procedimientos (v0.16)

**El problema real no era de balance, era de nombre.** La categoría se llamaba
`MONITOREO` en el código, "Soporte Vital" en las cartas, "SOSTENER" en este
documento y "monitoreo" en el README. Cuatro nombres para una plaza es el
síntoma de una plaza sin concepto.

Al auditar su contenido apareció el motivo: **11 de sus 14 copias ya eran
procedimientos invasivos** (línea arterial, catéter venoso central, ventilación
mecánica, gases arteriales). Solo *Monitor Multiparámetro* era monitoreo de
verdad. No se creó una categoría nueva: se le puso el nombre correcto a una que
llevaba dos años mal rotulada.

**Por qué esta y no Imagen** (la otra candidata):

| | Reemplazar Soporte Vital | Reemplazar Imagen |
|---|---|---|
| Contenido reciclable | 11 de 14 copias | 0 de 14 |
| Ilustraciones perdidas | 0 (VM y Carro de Paro sobreviven) | 3 terminadas |
| Sinergia perdida | 0 (Gases Arteriales sigue siendo punción) | CARD y NEURO pierden una fuente |
| Verbo perdido | "SOSTENER", que nunca fue un verbo del jugador | SABER — el único diagnóstico |

**Lo medido.** El renombrado puro es **idénticamente neutro**: 3.000 partidas
con la misma semilla sobre una copia renombrada devolvieron los mismos números
hasta el último dígito. Lo que sí movía el balance era el cambio de contenido,
porque las cartas que entran llevan sinergia y la que sale no la tenía.

| | antes | después | banda |
|---|---:|---:|---|
| Salvamento | 66% | 66% | 55–70% |
| Altas por jugador | 2,82 | 2,83 | 2–3 |
| Gravedad III salvada | 43% | 43% | 40–50% |
| "No se me fue nadie" | 10,5% | 10,3% | 5–15% |

**Los cambios de contenido.** Sale *Monitor Multiparámetro* (2 copias, sin
sinergia). Entran *Pleurostomía* (RESP, ⚠️ **Fuga Aérea Persistente**, −1 ❤️,
🎯 ESTABLE) y *Punción Lumbar* (NEURO). *Carro de Paro* pasa a llamarse
*Reanimación* — el acto, no el mueble; conserva su ilustración porque el arte
se resuelve por ID. El mazo sigue en 63 copias.

**El equilibrio de requisitos.** Dos puntos movidos, ambos con lógica clínica:
*El Que Googleó Sus Síntomas* cambia 1 🩻 por 1 🧑‍⚕️ (necesita que alguien le
hable, no un segundo TAC) y *Pielonefritis Complicada* cambia 1 💊 por 1 💉
(una pielonefritis obstructiva se drena). La demanda total no cambia, así que
`total_recursos` y `puntos_alta` siguen válidos.

Lecciones:

1. **Una categoría que nadie sabe nombrar es una categoría sin concepto.** La
   deriva terminológica no era descuido: era el diagnóstico.
2. **Renombrar es gratis; recomponer no.** Separar las dos operaciones y medir
   solo la segunda ahorró una recalibración entera.
3. **Emparejar los ratios costó dos puntos de requisito.** El colchón de
   Personal (3 puntos, justificado en su día por las cartas de ataque) resultó
   ser folklore: al quitarlo, ninguna métrica se movió de banda.

---

### 4f. La ⚠️ se dispara al jugar, no al robar (v0.17)

**El motivo decisivo no fue de diseño, fue de integridad.** Robar una carta es
un acto privado: si la complicación se dispara al robar, cualquiera puede
callarse y nadie se entera hasta varios turnos después, si es que se entera.
Colocar una carta es un acto público, boca arriba. La regla pasa a hacerse
cumplir sola. Ese argumento pesa más que la ficción (un ventilador que nunca
conectaste no puede dar NAVM) y más que la información (dejas de anunciar lo
que llevas en la mano).

**Lo medido, antes de calibrar** — 5.000 partidas, semilla 42:

| Modelo | Puntaje | Altas | Gravedad III | "No se me fue nadie" |
|---|---:|---:|---:|---:|
| Al robar (v0.16) | 7,4 | 2,82 | 43% | 10,2% |
| Al jugar · IA normal | 7,0 | 2,69 | 39% | 11,9% |
| Al jugar · IA que las evita | 7,0 | 2,68 | 39% | 12,1% |
| Al jugar · IA que **nunca** las juega | 6,2 | 2,42 | 35% | 13,7% |
| *Al robar · nunca las juega (control)* | *2,8* | *1,89* | *24%* | *3,5%* |

**Disparar al jugar endurece el juego.** Es contraintuitivo y es el hallazgo
central: al robar, la complicación estalla en la Entrega de Turno, con el
tablero flaco y muchos pacientes sin recursos encima — y falla sola (te pide
descartar un 💊 que no está, busca al ✅ y no hay). Al jugar, estalla en el
Pase de Visita, con el tablero en su punto más poblado y más avanzado. Máxima
superficie.

**Los dos riesgos que parecían obvios no existen:**

1. **Acaparar no funciona** — el límite de mano de 5 lo impide. La IA evasiva
   rinde 2,68 altas contra 2,69 de la ingenua: ruido.
2. **No se vuelven cartas muertas** — negarse a jugarlas cuesta 0,8 puntos.
   Necesitas el recurso más de lo que te molesta la complicación, que es
   exactamente la decisión que la regla quiere provocar.

Sí aparece una línea **cobarde**: el que se niega sube su "No se me fue nadie"
de 10,2% a 13,7% y salva 84% de los Gravedad I. No domina (6,2 contra 7,0),
pero existe. A vigilar en mesa.

**Calibración.** Gravedad III cayó a 39%, bajo la banda 40–50%. Se corrigió con
**un solo campo**: *Taquicardia Ventricular* (Noradrenalina ⚠️) pasa de 🎯 EL
MÁS GRAVE a 🎯 EL QUE MEJOR VA. Clínicamente es incluso mejor — la arritmia
aparece cuando estás bajando la noradrenalina al que iba saliendo. Con 8.000
partidas: salvamento 66% · altas 2,71 · **Gravedad III 43%** · "No se me fue
nadie" 13,7% · puntaje 7,4. Las cinco métricas en banda.

Se descartaron alternativas que daban 45% de Gravedad III porque empujaban
"No se me fue nadie" a 15,5%, fuera de banda: la guardia limpia tiene que
seguir siendo una hazaña.

**Lo que el simulador no puede responder.** La IA juega la ⚠️ cuando es la
mejor carta. Un humano la **cronometraría**: se guarda la de 🎯 ESTABILIZADO
hasta no tener ningún ✅ en mesa y la complicación se pierde en el aire. Al
controlar el *cuándo*, el jugador controla el estado de tablero que la carta
va a leer, y eso erosiona el 🎯 (§7). El 43% es un **piso**, no una
predicción. Solo la mesa lo resuelve.

Lecciones:

1. **Una regla que depende de un acto privado no es una regla, es un pacto de
   honor.** Antes de discutir si un disparo es temático, pregúntate si es
   auditable.
2. **Mover un efecto "más tarde" no lo suaviza: lo concentra donde hay más
   blanco.** La intuición decía más fácil; la medición dijo lo contrario.
3. **El límite de mano ya era la defensa contra el acaparamiento.** No hizo
   falta regla nueva: la restricción que ya existía cubría el hueco.

---

### 4g. 🎯 ESTE PACIENTE: la complicación del procedimiento (v0.18)

El disparo al colocar (§4f) desbloqueó un objetivo que antes era imposible de
escribir: **ESTE PACIENTE** — el que está debajo de la carta que acabas de
poner. Es el objetivo más realista de los siete: la NAVM le da al que
ventilaste, no a otro.

**El criterio de reparto es causal, no estético.** ESTE se reservó para las
complicaciones *del procedimiento* (le pasan al que lo recibió); los errores
*de sistema* siguen disparando lejos, porque así funcionan de verdad:

| Carta ⚠️ | 🎯 nuevo | Por qué |
|---|---|---|
| Ventilación Mecánica → NAVM | **ESTE** | La neumonía es del intubado |
| Catéter Venoso Central → Bacteriemia | **ESTE** | El catéter infectado es el suyo |
| Pleurostomía → Fuga Aérea | **ESTE** | El tubo que burbujea es el suyo |
| TAC de Urgencia → Nefropatía | **ESTE** | El contraste se lo llevó él |
| Anticoagulación → Sangrado | MAS_GRAVE → **MEJOR** | Compensación (ver abajo), y clínicamente mejor: sangra el que iba saliendo |
| Errores de medicación, Turno 24, Pabellón… | sin cambio | Un error de sistema no elige al paciente que lo motivó |

**Lo medido.** Una a una, las cuatro conversiones caben en banda. Juntas no:
Gravedad III cae de 43% a **39%**, porque los graves son quienes consumen los
recursos 💉 — ESTE concentra en ellos el golpe que MEJOR repartía hacia los
sanos. La compensación exacta resultó ser *Sangrado* → MEJOR: devuelve hacia
los sanos parte de la presión que ESTE les quitó.

Configuración final, 8.000 partidas × 3 semillas (42/7/99):
**Gravedad III 41/41/41%** · salvamento 66–67% · altas 2,73 · "No se me fue
nadie" 13,8–14,2% · puntaje 7,4. Las cinco métricas en banda. Paridad
Python↔JS verificada.

**Dos vigilancias nuevas para la mesa** (anotadas en `PENDIENTES.md`):

1. Gravedad III quedó en 41% — borde inferior de la banda, aunque el §4f ya
   argumentó que el número simulado es un piso (el humano cronometra mejor
   que la IA).
2. "No se me fue nadie" quedó en ~14% — borde superior. Si el playtest lo
   empuja sobre 15%, la palanca barata es devolver *Falso Positivo* o
   *Pabellón Suspendido* a un efecto con −1 ❤️.

**El costo de diseño asumido:** las ESTE son autoinfligidas y predecibles —
menos crueles que el resto del mazo. Se aceptó porque compran la mejor
enseñanza del juego: *sabes exactamente qué riesgo instalas cuando conectas
el ventilador*. La sorpresa vive en las otras catorce.

**Vocabulario:** 🎯 EL MÁS TRATADO quedó sin cartas (la NAVM era su única
usuaria). Sigue implementado en ambos simuladores como vocabulario reservado.

Lecciones:

1. **Un objetivo nuevo no se reparte por sabor: se reparte por mecanismo
   causal.** "¿La complicación es del procedimiento o del sistema?" respondió
   sola qué cartas convertir, y la regla se explica en una frase.
2. **Concentrar daño donde van los recursos es regresivo.** Los graves
   consumen más 💉 → ESTE los castiga más. Todo objetivo ligado al flujo de
   recursos hereda la distribución de ese flujo.
3. **La compensación más limpia vive en la misma moneda que el daño.** El
   déficit lo creó mover presión fuera de los sanos; lo cerró devolver una
   carta (Sangrado) hacia los sanos — no tocar vidas, copias ni requisitos.

---

### 4h. La plantilla de 22 avatares (v0.19)

Se aplicó la plantilla completa inspirada en los arquetipos de héroe de
*Hearthstone Battlegrounds*, con dos reglas de armadura: **reparto 2-elige-1**
(el draft chico absorbe desbalance residual) y **vocabulario de alcance**
explícito en cada texto (*este paciente* / *tu unidad*).

**Método:** el de §4b — la habilidad se le da solo al jugador 0 y se compara
su puntaje contra el promedio de sus dos rivales, misma mesa, misma semilla,
4.000 partidas. Sesgo de asiento medido: +0,07 (la señal es limpia). Banda
sana: **+0,3 a +1,0**.

**El hallazgo que gobernó toda la calibración: el robo de cartas repetible es
la habilidad más rota del juego.** La mano es el cuello de botella de la
economía, así que cada carta extra vale ~+0,5 puntos y además compone: robar
alimenta colocar, colocar alimenta altas.

| Versión descartada | Δ medida |
|---|---:|
| Residente: cada 3 recursos colocados → roba 1 | **+8,45** |
| Buena Muñeca: roba 1 extra por turno (con filtro) | +4,99 |
| Enfermera: 1×TURNO un paciente no se deteriora | +4,84 |
| Dador: alta inmediata con ≤2 faltantes, gratis | +3,24 |
| Residente: ídem pero máx 1 robo por turno | +4,45 |
| Residente: el 3er recurso del turno cuenta doble | +2,24 |
| Jefe de Servicio: cada alta → roba 1 | +1,84 |
| Jefe: ídem, máx 2 por partida | +1,37 |
| Intensivista: +1 ❤️ a Gravedad III **y** ROJO | +1,37 |
| Residente: límite de mano 6 | **−0,11** (adorno) |

**Las versiones que quedaron impresas:**

| Avatar | Δ final |
|---|---:|
| El Intensivista (+1 ❤️ solo Gravedad III) | +0,97 |
| El Jefe de Servicio (solo la primera alta) | +0,79 |
| El Dador de Altas (falta exactamente 1, descarta 2) | +0,70 |
| La Enfermera de Noche (1×PARTIDA, descarta 2) | +0,67 |
| La de la Buena Muñeca (filtro neto cero) | +0,59 |
| El Radiólogo de Guardia | +0,48 |
| El Subespecialista (congelar paga el doblete) | +0,41 |
| El Residente Aplicado (4º recurso al mismo paciente) | +0,41 |
| El Reanimador | +0,30 |
| El Multiuso (comodín inicial intocable) | **+1,09** 🔶 |

El Multiuso queda deliberadamente caliente: es el único +1 carta seca de la
plantilla y sirve de vara — si en mesa no se siente dominante, la banda puede
relajarse; si se siente, el arreglo es que el comodín inicial empiece **en
juego** sobre un paciente (pierde la flexibilidad de mano).

**Los nueve «mesa»** (Diostor, Fantasma, Amor, Director, Esotérico,
Abastecimiento, Dirigente, IAAS, Carroñero, Precavido, Jefa de Unidad) usan
piezas que el simulador no modela — Acciones, Canje, manos rivales. Parten al
playtest con la lección del robo aplicada de antemano: sus robos son 1×PARTIDA
o con gatillo que controla el rival.

Lecciones:

1. **En una economía de mano apretada, "roba 1 carta" no es una habilidad
   menor: es la moneda más cara del juego.** Medirlo antes de imprimir ahorró
   ~seis avatares rotos.
2. **El costo correcto vive en la misma moneda que el beneficio.** El
   Subespecialista quedó en banda sin ajustes numéricos: congelar la carta un
   turno ya paga el doblete. Enfermera y Dador entraron en banda pagando
   cartas de la mano.
3. **El sesgo de asiento (+0,07) hay que medirlo una vez y restarlo siempre.**
4. **Un límite que la IA nunca toca es un adorno** (mano 6 = −0,11): antes de
   regalar "capacidad extra", verificar que el jugador de verdad choque con
   el límite.

---

### 4i. v0.20 — el turno se vuelve decisión (tope, admisión, protecciones)

**El diagnóstico que lo motivó** (partida narrada completa + 4.000 simuladas):
el 59% de los turnos no tenía ni un alta ni un ✝️, la mano cerraba en 1,07
cartas y el 0% de los turnos obligaba a elegir. El motor era coherente pero el
turno promedio no contenía decisiones. Tres reglas y un arreglo:

**1 · Tope de 3 recursos por turno.** El puntaje casi no se mueve (7,3 vs 7,6)
pero la mano pasa de 1,07 a 3,4 cartas y el 93% de los turnos deja algo que
querías bajar. Define además la moneda del juego (`ECONOMIA.md` §1).

**2 · Admisión opcional + cama vacía = −1 punto por noche.** La intuición del
autor ("el premio por admitir es más trabajo, que sea decisión") medida contra
su propio riesgo (la tortuga que no admite nunca):

| política | puntaje normal | puntaje tortuga | guardias sin ✝️ tortuga |
|---|---:|---:|---:|
| cama vacía gratis | 7,56 | 6,52 (viable) | 33% |
| cama vacía = 1 Sumario | 6,94 | 5,73 (viable) | 25% |
| **cama vacía = −1 punto** | **5,98** | **−2,62 (muerta)** | 30% pero pierde |

El Sumario era la versión más temática y NO mató a la tortuga (el tope de mano
tiene suelo). El punto seco sí. Un "Reingreso" como carta de ataque se
descartó: una sola carta decidiendo la partida.

**3 · Canje: roba 2, quédate 1.** El 50% del Mazo de Protocolos no avanza a
ningún paciente propio; a ciegas, el Canje era pagar 2 progresos por una
moneda al aire y la IA (y el autor) lo saltaban todos los turnos. 2-elige-1
baja el blanco al 25% sin tocar el precio. No medible en simulador (no juega
Acciones): a validar en mesa.

**4 · Protecciones 🛡️** (idea del autor, §7.3): Kine→NAVM, Enfermera→
Bacteriemia, Técnico→Delirium, en las copias sin ⚠️ (el gemelo cansado no
previene). Prospectivas, viajan con la carta. En simulación previenen el 1,1%
de las complicaciones — la IA no planifica la secuencia protector-antes-del-⚠️;
un humano la buscará, así que 1,1% es el piso. Sin costo de balance medible.

**Compensaciones de calibración:**
- *El Turno Veinticuatro*: MAS_GRAVE → MEJOR (GIII 39→41; la nota del §7 se
  reescribió: el error aparece donde nadie estaba mirando). Con esto
  **MAS_GRAVE quedó sin cartas** — segundo vocabulario reservado junto a
  MAS_TRATADO.
- Las tres ⚠️ que se auto-anulaban (detectadas por el autor en su primera
  partida física) descargan ahora OTRO tipo: Hallazgo Incidental −1 💊,
  Falso Positivo −1 🧑‍⚕️, Pabellón Suspendido −1 💉.
- También se corrigió un fósil: el §5.1c del reglamento aún decía que la ⚠️
  disparaba al robar (regla muerta en v0.17).

**Resultado final** (8.000 partidas × 3 semillas, 2 jug; paridad JS exacta):
altas 2,81 · ✝️ 1,39 · salvamento 67% · **GIII 41–42%** · "No se me fue
nadie" **8,0–8,7%** (por fin lejos del techo) · puntaje 6,3 (baja porque las
camas vacías ahora cuestan — es puntaje redistribuido, no juego perdido).

**La prueba de fuego:** la semilla 2026 —la partida narrada que bajo v0.19
terminó en **−2** encadenado a admisiones forzadas imposibles— bajo v0.20
terminó en **+8**: el jugador rechazó admitir estando sobrecargado, pagó −3
en camas vacías, y usó ese aire para completar y dar de alta al Trasplante en
Lista Cero (+8). La regla nueva convirtió la peor partida del motor en una
historia de triage.

Lecciones:

1. **"% de turnos sin alta ni ✝️" es la métrica de aburrimiento** y ninguna de
   las clásicas la veía. Medirla antes de discutir dinamismo.
2. **El castigo temático no siempre es el castigo que funciona.** El Sumario
   era más bonito; el −1 seco fue el único que mató la estrategia degenerada.
3. **Una regla de agencia se prueba contra su peor abuso, no contra su uso
   normal.** La admisión opcional era neutra en manos normales; la decisión
   la tomó la tortuga.

---

## 5. Lo que sigue abierto (en orden de riesgo)

1. **Los seis avatares están sin balancear.** (Desde v0.10 son los del
   autor: Diostor, Fantasma, Amor, Director, Gestora, Esotérico.) Sospechas:
   - *Doctor Amor* y *el Director* juegan una sola vez por partida, contra
     avatares que actúan cada turno. Si se sienten planos, pasivas menores
     sugeridas: Amor — "cuando un rival te quite o descarte un recurso,
     roba 1 carta"; Director — "una vez por turno, descarta 1 carta y roba 1".
   - *El Esotérico* tiene 80% de éxito en su revelación (48/60 cartas sin ⚠️).
     Si resulta demasiado seguro, la penitencia puede subir a 2 cartas.
   - ~~*La Gestora* puede ciclar pacientes buscando Gravedad I fáciles.~~
     **Medida y corregida en v0.13** — la sospecha era correcta pero el
     diagnóstico no: el problema no era la frecuencia. Ver §4b.
   - *El Diostor* con 2 jugadores golpea siempre al mismo rival: revisar en
     duelos.
2. **¿Es divertido perder pacientes?** El riesgo real del juego. Si en el
   playtest la gente se siente castigada en vez de desafiada, la solución no
   es subir el robo — es hacer que las muertes tengan un premio de consuelo
   (p. ej.: cada ✝️ te deja robar 1 carta extra el turno siguiente, "la cama
   quedó libre").
3. **Duración.** 8 rondas × 3 jugadores = 24 turnos. Estimado 30–40 min. Sin
   medir. Si pasa de 50 min, baja a 7 rondas antes que tocar cualquier otra
   cosa.
4. **El tope de 1 Acción por turno** puede dejar cartas de ataque muertas en
   la mano. Alternativa a probar: 2 Acciones pero solo 1 de tipo ATAQUE.
5. **Partidas a 2 jugadores**: los ataques se concentran. Simulado bien, pero
   la simulación no modela ataques. Es la configuración con más riesgo real.

---

## 6. Ideas descartadas (y por qué, para no volver a proponerlas)

- **Puntos por recursos sobrantes al final.** Incentiva acaparar en vez de
  tratar. Va contra el tema.
- ~~**Cartas de recurso "comodín" que valen cualquier tipo.**~~
  **Revertido en v0.11.** Se descartaron por "borrar la decisión", pero con
  datos el argumento no se sostiene a baja densidad: 3 comodines en 63 cartas
  bajan a la mitad los jugadores que terminan sin ninguna alta, sin mover el
  salvamento medio. Escasos no borran la decisión — evitan la mano muerta.
  Lo que sí sigue prohibido es hacerlos abundantes.
- **Poder mover recursos entre pacientes libremente.** Elimina el coste de
  equivocarse. Se conservó solo como efecto puntual y caro (*Reunión Clínica*
  y el Turno Extra de la Enfermera Coordinadora), que es donde brilla.
- **Eliminación de jugadores.** En un juego de 30 minutos nadie debería
  quedarse mirando.
- **Mazo de eventos que se roba cada ronda obligatoriamente.** Probado en
  papel: convierte el juego en una sucesión de desgracias sin agencia. Atarlo
  al símbolo ⚠️ mantiene la sensación de que *tú* provocaste el problema.

---

## 7. Expansiones plausibles (no antes de cerrar el core)

- **Más personajes**: el Cirujano ("yo opero, el postoperatorio es tuyo"), el
  Radiólogo (que informa cuando quiere), el Bioquímico, el Capellán.
- **Turno de Noche** como mazo alternativo de eventos, más duro y más raro.
- **Pacientes con historia**: cartas que se encadenan (el que reingresa tres
  veces y todos ya lo conocen por su nombre).
- **Modo Pandemia** (cooperativo): ya esbozado en el reglamento §11.
