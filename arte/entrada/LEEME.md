# La cortina de entrar a turno

**Ocho segundos** entre tocar la moneda y elegir personaje. Tres golpes, y
los tres son manos:

| # | Golpe | Archivo | Dura |
|---|---|---|---|
| 1 | la mano marca la tarjeta en el reloj control | `reloj.webp` | 2,5 s |
| 2 | la mano entra a la unidad | `puerta.webp` | 2,3 s |
| 3 | las manos bajo el chorro | `lavado.webp` | 3,2 s |

El lavado va **al final** a propósito: la higiene es en el punto de
atención. Se marca tarjeta, se entra a la unidad, y recién ahí uno se lava
las manos antes de tocar al primer paciente.

No hay un cuarto golpe: la cortina entrega directo a la elección de
personaje, que ya es una pantalla llena de caras.

## Cómo se reemplazan

Mientras esta carpeta esté vacía, la app dibuja los tres con íconos de
línea que trae dentro. **En cuanto aparece un archivo con el nombre del
golpe, ese golpe pasa a ser la ilustración** — y los otros siguen siendo
íconos, así que se puede reemplazar de a uno.

- **Cuadrada, 1:1.** El hueco es un cuadrado de hasta 244 px de CSS, o sea
  **732 px reales** en un teléfono 3×. Con 800×800 sobra.
- **Fondo transparente** (`.webp` o `.png`). Detrás hay un degradado azul
  oscuro y la ilustración se apoya en él; un fondo blanco se vería como un
  parche.
- Sirven también `.png` y `.jpg`, en ese orden de preferencia.
- **Solo manos.** Es lo único que uno ve de sí mismo al llegar a un turno,
  y es lo que mantiene los tres golpes como una sola secuencia.

Para que entren: `python3 tools/generar_app.py` (y `--pwa`). No hay que
tocar código.
