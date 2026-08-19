# Plan de playtest — ¡Vaya Turno! v0.12

Llevas dos años con esto en la cabeza. Lo que falta **no es más diseño**: son
tres sesiones de mesa y un cuaderno. Este documento es ese cuaderno.

La regla más importante: **no cambies nada a mitad de una sesión.** Anota el
problema, termina la partida con las reglas como están, y decide después.

---

## Sesión 1 — ¿Funciona el motor? (3 jugadores, 2 partidas)

**Solo se prueba una cosa:** que el ciclo *entrego turno → trato → pasa el día*
se entienda y se sienta bien. Nada más.

**Modificación para esta sesión:** juega **sin el Mazo de Protocolos** (guárdalo
entero; no hay Canje ni Acciones, y el turno se queda en tres fases: Entrega de
Turno · Pase de Visita · Fin de Guardia). Sí, va a ser más aburrido. Es a
propósito: si el motor no funciona sin ataques, los ataques solo lo van a
esconder.

**Qué medir:**

| Métrica | Objetivo | Cómo |
|---|---|---|
| Duración de la partida | 25–35 min | Cronómetro |
| Duración de un turno | < 90 s | Cronometra 5 turnos sueltos |
| Altas por jugador | 2–3 (simulado: 2,7) | Hoja de registro |
| Fallecidos por jugador | 1–2 (simulado: 1,7) | Hoja de registro |
| ¿Alguien salvó un paciente en su último ❤️? | Al menos 1 por partida | Es la prueba de que mover el deterioro al Fin de Guardia sirvió |
| Nº de veces que alguien pregunta una regla | ↓ en la 2ª partida | Palito en la hoja |

**Preguntas al terminar (hazlas en voz alta, anota la primera reacción):**
1. ¿En qué momento supiste a cuál paciente ibas a dejar morir?
2. ¿Se sintió como una decisión tuya o como que el mazo decidió por ti?
3. ¿Hubo algún turno en que no tuvieras nada interesante que hacer?

**Señales de alarma:**
- Si nadie pierde ningún paciente → **baja el robo a 3**. Es la perilla, no la vida.
- Si alguien termina con 0 altas → mira si fue mala suerte de tipos de recurso.
  Si se repite, el mazo necesita más equilibrio entre tipos.
- Si los turnos pasan de 2 min → el problema casi siempre es la Admisión
  (revelar 2 y elegir), dentro de la Entrega de Turno. Prueba revelando solo 1.
- Si alguien juega recursos y *después* se acuerda de que quería atacar → el
  orden Pasillo-antes-de-Visita no está entrando. Anótalo: es el candidato
  número uno a invertirse.

---

## Sesión 2 — ¿Funciona el veneno? (3 jugadores, 2 partidas)

Ahora **con el Mazo de Protocolos completo** (30 Acciones, vía Canje) y **con personajes**.

**Qué medir:**

| Métrica | Objetivo | Señal de problema |
|---|---|---|
| Acciones jugadas por jugador/partida | 4–7 | < 3 = el tope de 1 por turno ahoga; > 9 = revisa |
| Nº de altas arruinadas por un ataque | 1–3 por partida | 0 = los ataques no muerden; > 5 = frustrante |
| ¿Se concentraron los ataques en 1 jugador? | No | Si sí, es el problema clásico de "pegarle al que va perdiendo" |
| Puntaje del ganador vs. último | Diferencia < 8 | > 12 = alguien quedó fuera de la partida temprano |

**Registro obligatorio de personajes.** Anota qué personaje usó cada quien y
su puntaje final. Después de 6+ partidas, si alguno gana más del 40% de las
veces (esperado: ~17%), está roto.

| Personaje | Partidas | Victorias | Puntaje medio |
|---|---|---|---|
| El Diostor | | | |
| El Médico Fantasma | | | |
| Doctor Amor | | | |
| El Director del Hospital | | | |
| La Gestora de Camas | | | |
| El Médico Esotérico | | | |

**Sospechas a confirmar o descartar** (de `DISENO.md` §5):
- ¿El Fantasma y el Esotérico dominan por jugar **cada turno**, mientras Amor y
  el Director juegan **una vez por partida**? Es la asimetría más sospechosa.
- La Gestora **ya se midió y se corrigió** en v0.13 (`DISENO.md` §4b): pasó de
  +2,7 a +0,7 puntos de ventaja. Lo que queda por ver en mesa no es si rompe,
  sino si **se siente bien**: con un solo uso por partida y el Sumario encima,
  ¿el momento "este es el que derivo" resulta potente o mezquino?
- ¿Alguien usó el Perdonazo del Director en un rival para cobrárselo después?
  Si no pasa nunca, la carta es solo un descarte de Sumario.

**Prueba específica de v0.12 — el Canje a ciegas.** El Canje ahora ocurre en El
Pasillo, *antes* de tratar. Anota: ¿alguien botó un recurso en el Canje y en el
Pase de Visita lo echó de menos? Si pasa seguido, la fase está bien puesta.
Si no pasa nunca, el Canje es gratis y hay que revisarlo.

**Pregunta clave al terminar:** *¿Alguien se rió?* Este juego tiene una premisa
humorística. Si no hay risas, el problema no está en los números — está en el
texto de las cartas, y eso se arregla escribiendo mejores chistes.

---

## Sesión 3 — Los bordes (2 y 4 jugadores)

**Con 2 jugadores:** la configuración de mayor riesgo. Todos los ataques van a
la misma persona. Mide específicamente: **¿se siente injusto o se siente un
duelo?** Si es lo primero, prueba la regla *"no puedes jugar dos cartas de
ATAQUE en turnos consecutivos"*.

**Con 4 jugadores:** 2 camas, robo **3**, 10 rondas. Mide sobre todo el **tiempo
de espera entre tus turnos** — y, específicamente, si **alguien se atreve con un
Gravedad III**. La simulación dice que en esta configuración solo se salvan el
33% (contra 40% a 3 jugadores): si en la mesa nadie los admite nunca, hay que
subir el robo a 4 y pasar a 3 camas, asumiendo que el Mazo de Pacientes se
agotará antes del final. Si supera los 4 minutos, el juego necesita algo
que hacer fuera de turno (más cartas 🛡️ RESPUESTA es la solución natural).

---

## Hoja de registro (imprímela, una por partida)

```
FECHA ________  Nº JUGADORES ____  DURACIÓN ______ min   PARTIDA Nº ____

JUGADOR      PERSONAJE          ALTAS (pts)   ✝️ (pts)   LIMPIA   TOTAL
__________   ________________   ___________   ________   ______   _____
__________   ________________   ___________   ________   ______   _____
__________   ________________   ___________   ________   ______   _____
__________   ________________   ___________   ________   ______   _____

ALTAS POR GRAVEDAD:   I ____   II ____   III ____   ROJO ____
MUERTES POR GRAVEDAD: I ____   II ____   III ____   ROJO ____

Eventos Centinela resueltos: ____   Canjes hechos: ____   Sumarios abiertos: ____
Cartas de Acción jugadas: ____   ¿Cuántas arruinaron un ✅? ____
Pacientes salvados en su último ❤️ (gracias al Fin de Guardia): ____

REGLAS QUE HUBO QUE CONSULTAR:
_________________________________________________________________
_________________________________________________________________

MOMENTO MÁS DIVERTIDO DE LA PARTIDA:
_________________________________________________________________

MOMENTO MÁS ABURRIDO / CONFUSO:
_________________________________________________________________

CARTA QUE NADIE QUISO JUGAR NUNCA: ______________________________
CARTA QUE TODOS PELEARON POR TENER: _____________________________
```

---

## Cómo decidir cambios después de cada sesión

En este orden, y **de a un cambio por vez**:

1. **¿Es un problema de reglas poco claras?** → Reescribe el texto. No toques
   números.
2. **¿Es un problema de una carta concreta?** → Arregla esa carta.
3. **¿Es un problema de ritmo general?** → Ajusta el nº de rondas.
4. **¿Es un problema de dificultad global?** → Ajusta el robo (±1). Es la
   perilla más potente del juego: robo 3→5 movió el salvamento del 32% al 60%.
   Ojo: es **muy** potente. En v0.12, bajar de 4 a 3 llevó el salvamento de 61%
   a 54% de una sola vez.
5. **¿Es un problema de identidad de las gravedades?** → Último recurso.
   Cambiar vida o requisitos obliga a recalibrar todo lo demás.

Después de cualquier cambio en `cartas/pacientes.csv` o `cartas/recursos.csv`:

```bash
python3 tools/simular.py --partidas 3000
```

y compara contra los objetivos de `docs/DISENO.md` §4.

---

## Cuándo dejar de playtestear

Cuando se cumplan las tres a la vez:

- Dos partidas seguidas sin consultar el reglamento.
- Ningún personaje gana más del 30% de las partidas en 12+ partidas.
- Alguien que no seas tú pide jugar otra vez sin que se lo propongas.

Ahí el juego está terminado. En serio. **No sigas puliéndolo después de eso** —
que es exactamente lo que lleva dos años pasando.
