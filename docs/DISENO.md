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
| ¿Se rellenan las camas? | Sí, siempre, al inicio de tu turno | Camas vacías = descanso. En este juego no hay descanso. Además evita la estrategia degenerada de "dejo morir a todos y no admito a nadie para no perder puntos". |
| ¿Qué pasa con el paciente estabilizado? | Se detiene el reloj, alta una ronda después | Idea original tuya, y es la mejor del juego. Se conserva intacta. |
| ¿Se puede perder el ✅? | Sí, al instante, si deja de cumplir requisitos | Es lo que da filo a todos los ataques. Los recursos sobrantes hacen de colchón — eso premia sobre-tratar a un paciente valioso. |
| ¿Cuántas cartas se juegan por turno? | Recursos ilimitados, **1 sola Acción** | La simulación mostró que limitar recursos no cambia el balance (el cuello de botella es el robo), solo añade una regla. En cambio limitar Acciones sí importa: sin ese tope, una mano con 3 ataques borra a un jugador de la partida. |
| ¿Cómo entran los eventos adversos? | Símbolo ⚠️ en 12 de las 60 cartas de Recurso | Tu idea de "robar un evento al robar recursos". Ata el castigo al motor del juego: mientras más juegas, más te expones. |
| ¿Mazo único o mazos separados? | Guardia (recursos+acciones) unido; Eventos aparte | Los eventos deben poder ser brutales sin diluir el mazo principal. Aparte, se roban solo cuando algo obliga. |
| Puntuación | Altas − Fallecidos + bonus Guardia Limpia | El bonus de +3 evita que la estrategia dominante sea siempre "sacrificar sin culpa". Con él, hay dos rutas viables: maximizar altas o proteger el expediente. |

---

## 3. Anatomía de los pacientes

| Gravedad | ❤️ | Recursos | Alta | Fallece | Swing | n |
|---|---:|---:|---:|---:|---:|---:|
| I — Observación | 7 | 3 | +2 | −1 | 3 | 8 |
| II — Grave | 6 | 5 | +3 | −2 | 5 | 10 |
| III — Crítico | 5 | 7 | +5 | −2 | 7 | 6 |
| ★ Código Rojo | 4 | 8 | +8 | −3 | 11 | 2 |

**La penalización por muerte crece más lento que el premio por alta.** Es
deliberado: si un Crítico costara −5 al morir, nadie lo admitiría nunca y las
cartas más interesantes del mazo serían basura. Tal como está, admitir un
Crítico es una **apuesta con valor esperado positivo si crees que puedes
salvarlo ~40% de las veces** — y la simulación dice que se salvan el 41%.
Justo en el filo. Ese es el punto.

El **Código Rojo** (2 cartas) no está balanceado para ser eficiente: está para
que alguien lo intente, lo consiga una vez, y lo cuente durante meses.

**Oferta vs. demanda de recursos.** La composición del Mazo de Guardia se
derivó de la demanda real agregada de las 26 cartas de paciente:

| Tipo | Demanda | % | En el mazo | % |
|---|---:|---:|---:|---:|
| 💊 Fármacos | 45 | 34% | 20 | 33% |
| 🩻 Imagen | 32 | 24% | 14 | 23% |
| 📈 Monitoreo | 30 | 23% | 13 | 22% |
| 🧑‍⚕️ Personal | 25 | 19% | 13 | 22% |

Personal está deliberadamente **sobre-representado en 3 puntos** porque es el
único tipo que las cartas de ataque destruyen (*Vacaciones*, *Licencia*). Sin
ese colchón, un solo ataque se volvía letal.

> **Si añades pacientes nuevos, vuelve a correr `tools/simular.py`.** Cambiar
> la demanda sin cambiar el mazo desbalancea el juego en silencio.

---

## 4. Cómo se calibró el robo (y por qué no toques esto a ojo)

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
> fallecidos, 11,7% de guardias limpias.** Gravedad III sube a 48% (era 41%):
> los críticos ahora son apuestas más razonables porque su recurso específico
> los rescata más rápido.
>
> **Importante:** los recursos específicos deben estar repartidos entre los
> cinco sistemas en proporción a cuántos pacientes hay de cada uno. Hoy:
> CARD 5/5, RESP 7/4, NEURO 3/5, METAB 4/5, QUIR 5/7 (recursos/pacientes).
> RESP está sobre-servido y NEURO/QUIR algo cortos — es la primera cosa a
> ajustar si el playtest muestra que unos sistemas se sienten mejores.

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
  de Guardia Limpia deja de ser una hazaña y pasa a ser el default.
- **Bajar los requisitos** aplana las gravedades: los Graves y los Críticos
  empiezan a parecerse entre sí y la decisión de triage pierde textura.
- **Subir el robo** arregla el problema sin tocar la identidad de ninguna
  carta. El reloj sigue siendo igual de despiadado; simplemente tienes más
  con qué pelear.

**Configuración final validada** (8 rondas, 2000 partidas por config):

| Jugadores | Camas | Robo | Rondas | Salv. | Altas | Muertes | Limpias |
|---|---:|---:|---:|---:|---:|---:|---:|
| 2 | 3 | 5 | 8 | 61% | 2,38 | 1,50 | 10% |
| 3 | 3 | 5 | 8 | 61% | 2,41 | 1,52 | 9,5% |
| 4 | 2 | 4 | 10 | 65% | 2,32 | 1,27 | 16% |

Objetivos de diseño que había que cumplir simultáneamente:

- Salvamento **55–70%** → salvas la mayoría, pierdes a alguien siempre.
- **2–3 altas** por jugador → la partida se siente productiva.
- Guardia Limpia **5–15%** → es una hazaña, no un plan.
- Gravedad III salvable **40–50%** → vale la pena intentarlo, no siempre sale.

La configuración de 4 jugadores queda con un **16% de guardias limpias**, un
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
   - *La Gestora* puede ciclar pacientes buscando Gravedad I fáciles; si se
     abusa, limitarla a 1 derivación cada 2 rondas.
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
