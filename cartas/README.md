# Las cartas

Estos CSV son **la fuente de la verdad** del juego. El reglamento describe
cómo se juegan; acá están los números exactos. Todo en UTF-8, con encabezado.

| Archivo | Cartas únicas | Total con copias |
|---|---:|---:|
| `pacientes.csv` | 26 | 26 |
| `recursos.csv` | 34 | 60 |
| `acciones.csv` | 13 | 25 |
| `eventos.csv` | 18 | 18 |
| `personajes.csv` | 6 | 6 |
| `sumarios.csv` | 1 | 6 |
| | | **141** |

La columna **`copias`** dice cuántas veces se imprime cada fila.

---

## Columnas

### `pacientes.csv`

| Columna | Qué es |
|---|---|
| `gravedad` | `I`, `II`, `III` o `ROJO` |
| `vida` | Fichas ❤️ iniciales. Baja 1 por turno propio. |
| `img` `far` `per` `mon` | Recursos que exige de cada tipo |
| `total_recursos` | Suma de los cuatro anteriores (**redundante a propósito**: el simulador la verifica y falla si no cuadra) |
| `puntos_alta` / `puntos_fallece` | Puntuación |

### `recursos.csv`

| Columna | Qué es |
|---|---|
| `tipo` | `IMAGEN`, `FARMACOS`, `PERSONAL`, `MONITOREO` |
| `etiqueta` | Subtipo al que pueden apuntar cartas o habilidades (ej. `ANTIBIOTICO`, `ENFERMERIA`). Vacío = sin subtipo. |
| `complicacion` | `si` = lleva el símbolo ⚠️. Al robarla, robas un Evento Adverso. **12 de las 60.** |

Algunas cartas aparecen en dos filas con el mismo nombre: es la misma carta,
pero una tirada lleva ⚠️ y la otra no.

### `acciones.csv`

`tipo` es `ATAQUE`, `APOYO`, `CAOS`, `RESPUESTA` o `EXTREMA` (la Pelada, única). Solo importa para dos
reglas: la variante *Turno de Noche* prohíbe los `ATAQUE`, y las `RESPUESTA`
se pueden jugar fuera de turno.

### `eventos.csv`

`categoria` es `RESPIRATORIO`, `INFECCIOSO` o `GENERAL`. Hoy es informativa;
queda reservada para inmunidades de futuros avatares o expansiones.

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
- Gravedad III salvable **~40%**

La demanda agregada de los pacientes y la composición del mazo de recursos
están acopladas a propósito. Si añades pacientes que piden muchos 💊, hay que
subir los 💊 del mazo o el juego se desbalancea sin que se note.
