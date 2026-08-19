# Las cartas

Estos CSV son **la fuente de la verdad** del juego. El reglamento describe
cómo se juegan; acá están los números exactos. Todo en UTF-8, con encabezado.

| Archivo | Cartas únicas | Total con copias |
|---|---:|---:|
| `pacientes.csv` | 26 | 26 |
| `recursos.csv` | 43 | 63 |
| `acciones.csv` | 20 | 30 |
| `personajes.csv` | 6 | 6 |
| `sumarios.csv` | 1 | 6 |
| | | **131** |

La columna **`copias`** dice cuántas veces se imprime cada fila.

---

## Columnas

### `pacientes.csv`

| Columna | Qué es |
|---|---|
| `gravedad` | `I`, `II`, `III` o `ROJO` |
| `vida` | Fichas ❤️ iniciales. Baja 1 en cada **Fin de Guardia** propio, incluido el día que ingresa. |
| `img` `far` `per` `mon` | Recursos que exige de cada tipo |
| `sistema` | `RESP`, `CARD`, `NEURO`, `METAB` o `QUIR`. Habilita la sinergia |
| `total_recursos` | Suma de los cuatro anteriores (**redundante a propósito**: el simulador la verifica y falla si no cuadra) |
| `puntos_alta` / `puntos_fallece` | Puntuación |

### `recursos.csv`

| Columna | Qué es |
|---|---|
| `tipo` | `IMAGEN`, `FARMACOS`, `PERSONAL`, `MONITOREO` o `COMODIN` |
| `sistema` | Vacío, o `RESP`/`CARD`/`NEURO`/`METAB`/`QUIR`. Si coincide con el sistema del paciente, **cuenta doble**. 21 de 63 |
| `comodin` | `si` = cuenta como 1 recurso del tipo que elijas. 3 de 63 |
| `restriccion` | `PERSONAL` (exige un 🧑‍⚕️ ya puesto) o `TURNO` (consume tu turno de recursos) |
| `complicacion` | `si` = lleva el símbolo ⚠️. Al robarla, resuelves la complicación impresa en la propia carta. **17 de 63** |
| `comp_nombre` | Nombre clínico de la complicación (*Neumonía Asociada a VM*) |
| `comp_objetivo` | 🎯 a quién le toca: `MAS_GRAVE` · `MEJOR` · `MAS_TRATADO` · `ESTABLE` · `ELIGES` · `MANO` |
| `comp_vida` | ❤️ que pierde el objetivo (0 o negativo) |
| `comp_pide` | Tipo de recurso cuyo requisito sube en 1 |
| `comp_descarta` | Tipo de recurso que el objetivo pierde |
| `comp_texto` | El texto que se imprime en la carta |
| `texto` | Efecto propio del recurso (opcional, hoy vacío en las 43) |

> Las cuatro columnas `comp_objetivo`/`comp_vida`/`comp_pide`/`comp_descarta`
> **las lee el simulador**: cambiarlas cambia el balance medido. `comp_nombre`
> y `comp_texto` son solo para la carta.

Algunas cartas aparecen en dos filas con el mismo nombre: es la misma carta,
pero una tirada lleva ⚠️ y la otra no.

### `acciones.csv`

`tipo` es `ATAQUE`, `APOYO`, `CAOS`, `RESPUESTA` o `EXTREMA` (la Pelada, única). Solo importa para dos
reglas: la variante *Turno de Noche* prohíbe los `ATAQUE`, y las `RESPUESTA`
se pueden jugar fuera de turno.

### El Banco de pruebas

Debajo del tablero de constantes hay un **simulador que corre en el navegador**,
sobre las cartas que tienes en pantalla — incluidas las ediciones que aún no
has guardado. Eliges jugadores, camas, robo, rondas y cuántas partidas, aprietas
**Simular**, y te devuelve las cinco métricas con semáforo:

| | |
|---|---|
| Tasa de salvamento | objetivo 55–70% |
| Altas por jugador | 2–3 |
| Fallecidos por jugador | 1–2 |
| Guardias limpias | 5–15% |
| Gravedad III salvada | 40–50% |

Si tocaste algo, corre **dos veces** —tus cartas y las originales— y muestra el
delta: *"tu cambio bajó el salvamento de 61% a 54%"*. Con 1.000 partidas el
ruido es de ±1–2 puntos, suficiente para decidir.

> **Es una segunda copia del mismo motor.** La verdad sigue siendo
> `tools/simular.py`; el Banco es su port a JavaScript, verificado contra él en
> cinco configuraciones. **Si alguna vez se toca el motor, hay que tocarlo en
> los dos lados** — están en `tools/simular.py` y en el bloque *Banco de
> pruebas* de `tools/generar_taller.py`. El número que va al reglamento sale
> siempre del Python.

---

## Print & play

```bash
python3 tools/generar_pnp.py                    # los 5 mazos → pnp.html
python3 tools/generar_pnp.py --solo pacientes   # un mazo suelto
```

Salen cartas de **63×88 mm** (tamaño estándar, entra en fundas de Magic),
9 por hoja A4. Cada carta reserva un marco punteado para la
ilustración.

Al imprimir: **A4, márgenes mínimos, y activa "gráficos de fondo"** o las
bandas de color no salen.

---

## Meterle tus ilustraciones

Tres caminos, de menos a más trabajo:

1. **Rápido:** imprime el PnP y pega/dibuja encima. Sirve perfecto para
   playtestear.
2. **Intermedio:** edita `.arte` en el CSS de `tools/generar_pnp.py` para que
   cargue un `<img>` desde una carpeta `arte/` nombrada por `id`
   (`arte/P01.png`, `arte/A03.png`…).
3. **Producción:** estos CSV se importan tal cual en
   [nanDECK](https://www.nandeck.com/), [Component Studio] o
   [CardSetter]. Ahí es donde conviene maquetar la versión final.

---

## Si cambias algo

```bash
python3 tools/simular.py --partidas 3000
```

Objetivos que hay que mantener (detalle en `docs/DISENO.md` §4):

- Salvamento **55–70%**
- **2–3 altas** por jugador
- Guardias limpias **5–15%**
- Gravedad III salvable **40–50%** (a 4 jugadores baja a ~33%: ver `docs/DISENO.md` §4)

Además: mantén los **recursos específicos repartidos entre los cinco
sistemas** en proporción a cuántos pacientes hay de cada uno. Si un sistema
tiene 7 pacientes y solo 2 recursos específicos, esos pacientes nunca ven
sinergia y la mecánica se siente muerta para ellos.

La demanda agregada de los pacientes y la composición del mazo de recursos
están acopladas a propósito. Si añades pacientes que piden muchos 💊, hay que
subir los 💊 del mazo o el juego se desbalancea sin que se note.
