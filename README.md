# ¡VAYA TURNO!

**Un juego de cartas sobre salvar pacientes, no salvarlos a todos, y
arruinarle el turno al colega de al lado.**

2–4 jugadores · 30–45 min · 134 cartas

---

Eres médico a cargo de una UCI de tres camas. Los pacientes llegan solos, se
deterioran solos y no esperan. Para salvarlos necesitas cuatro cosas que nunca
hay al mismo tiempo: **🩻 imágenes, 💊 fármacos, 🧑‍⚕️ personal y 📈 monitoreo**.

No vas a poder salvarlos a todos. Eso no es un defecto del juego: **eso es
triage.** Elige a quién salvas, deja ir al resto, y — mientras tanto — manda a
la enfermera del rival de vacaciones justo antes de que dé un alta.

Cada paciente pertenece a un **sistema** (🫁 🫀 🧠 🧪 🔪), y el recurso correcto
en el paciente correcto **cuenta doble**. Ahí está la decisión que duele:
¿quemas el broncodilatador en el cardíaco que se te está yendo ahora, o lo
guardas por si llega un respiratorio?

---

## Estado del proyecto

**v0.12 — listo para playtest.** Reglas cerradas, 159 cartas escritas, economía
simulada y calibrada, y todo el material histórico del autor integrado:
avatares, Sumario, Canje, la Pelada, y la **sinergia por sistema clínico**
rescatada del Excel antiguo (ver `docs/SINTESIS.md`). Falta jugarlo con gente.

En v0.12 el turno pasó de seis fases a cuatro y recuperó los nombres del
hospital — **Entrega de Turno · El Pasillo · Pase de Visita · Fin de Guardia** —
y con ellos el cambio que importa: **el deterioro ocurre al cerrar el turno, no
al abrirlo.** Cada Fin de Guardia es un día que pasa. Un paciente en 1 ❤️ ya no
muere antes de que puedas tocarlo: alcanzas a intentarlo, y si falla, la muerte
es consecuencia de tu turno.

| | |
|---|---|
| Reglamento | ✅ completo |
| Cartas (texto y números) | ✅ 159 |
| Balance | ✅ simulado sobre 2.000 partidas por configuración |
| Print & play | ✅ generador incluido |
| Ilustraciones | ⬜ existen, falta maquetarlas |
| Playtest con humanos | ⬜ **el siguiente paso** |

---

## Empieza acá

```bash
# 1. Abre el Taller de Guardia: ver las cartas, sus constantes y editarlas
python3 tools/generar_taller.py && open taller.html

# 2. Genera el print-and-play (159 cartas en A4)
python3 tools/generar_pnp.py

# 3. Abre pnp.html e imprime: A4, márgenes mínimos, con gráficos de fondo
# 4. Recorta, consigue unos cubitos para las vidas, y juega
```

Después lee **[`docs/PLAYTEST.md`](docs/PLAYTEST.md)**, que te dice exactamente
qué medir en las tres primeras sesiones.

---

## Los documentos

| Archivo | Qué es |
|---|---|
| **[docs/REGLAMENTO.md](docs/REGLAMENTO.md)** | Las reglas completas. Es lo que se lleva a la mesa. |
| **[docs/DISENO.md](docs/DISENO.md)** | Por qué cada número es el que es. Léelo antes de cambiar nada. |
| **[docs/PLAYTEST.md](docs/PLAYTEST.md)** | Plan de 3 sesiones, qué medir y hoja de registro imprimible. |
| **[docs/SINTESIS.md](docs/SINTESIS.md)** | Qué se hizo con todo el material histórico: integrado, estacionado y por qué. |
| **[docs/EXPANSIONES.md](docs/EXPANSIONES.md)** | Los cinco módulos por sistema, el modelo de reemplazo y lo que la caja base debe reservarse. |
| **[docs/MOTOR.md](docs/MOTOR.md)** | El motor TURNO sin el tema: las cinco piezas reutilizables y su mapeo a otras profesiones. |
| **[cartas/](cartas/)** | Las 159 cartas en CSV. Es la fuente de la verdad. |
| **[tools/generar_taller.py](tools/generar_taller.py)** | CSV → **Taller de Guardia**: galería de las 159 cartas, tablero de constantes del mazo y editor en vivo. |
| **[tools/generar_pnp.py](tools/generar_pnp.py)** | CSV → HTML imprimible. |
| **[tools/simular.py](tools/simular.py)** | Simulador de balance. Córrelo tras cualquier cambio de números. |

---

## El balance, en corto

La primera versión del reloj era una masacre: 31% de salvamento y todos los
jugadores en puntaje negativo. Un barrido de parámetros mostró que la perilla
correcta era el **robo por turno**, no la vida ni los requisitos (subir la vida
arreglaba la tasa pero mataba la tensión: el 37% de las partidas terminaban sin
un solo fallecido).

Configuración final, validada sobre 3.000 partidas por caso (v0.12):

| Jugadores | Camas | Robo | Rondas | Salvamento | Altas | Fallecidos | Limpias |
|---|---:|---:|---:|---:|---:|---:|---:|
| 2 | 3 | 4 | 8 | 62% | 2,7 | 1,6 | 8% |
| 3 | 3 | 4 | 8 | 61% | 2,7 | 1,7 | 8% |
| 4 | 2 | 3 | 10 | 57% | 2,2 | 1,7 | 9% |

Salvas la mayoría. Siempre pierdes a alguien. Terminar una guardia sin ningún
fallecido pasa el ~8% de las veces, y por eso vale 3 puntos.

Mover el deterioro al final del turno regalaba medio turno de gracia a todo el
mundo (el salvamento se iba al 70%). Se pagó con dos ajustes: **el recién
ingresado ya no tiene día de cortesía**, y el **Código Rojo subió de ❤️4 a ❤️5**
— sin eso se desplomaba al 38%, porque pide 8 recursos y con 4 días no alcanza.

```bash
python3 tools/simular.py --partidas 3000
```

> El simulador modela la economía base: **no** modela las cartas de Acción ni
> las habilidades de personaje. Valida el suelo del balance, no el techo. Las
> limitaciones están detalladas y sin maquillar en `docs/DISENO.md` §4.

---

## Modificar cartas

Los CSV de `cartas/` son la fuente de la verdad. Edítalos, y después:

```bash
python3 tools/simular.py --partidas 3000   # ¿sigue en 55-70% de salvamento?
python3 tools/generar_pnp.py               # regenera el imprimible
```

Si tocas `pacientes.csv` o `recursos.csv`, **corre el simulador**. La demanda
de recursos de los pacientes y la composición del mazo están acopladas: cambiar
una sin la otra desbalancea el juego en silencio.
