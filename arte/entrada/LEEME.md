# La cortina de entrar a turno

Tres golpes de ~1,3 s antes de la partida: **marcas tarjeta**, **te lavas
las manos**, **entras**. Y el remate, que es con quién te toca hoy.

Mientras esta carpeta esté vacía, la app dibuja los tres con íconos de
línea que trae dentro. **En cuanto aparece un archivo con el nombre del
golpe, ese golpe pasa a ser la ilustración** — y los otros siguen siendo
íconos, así que se puede reemplazar de a uno.

| Archivo | Qué muestra |
|---|---|
| `reloj.webp` | la mano marcando la tarjeta en el reloj control |
| `lavado.webp` | las manos bajo el chorro, lavado clínico |
| `puerta.webp` | la mano entrando a la unidad |

- **Cuadrada, 1:1.** El hueco es un cuadrado de hasta 244 px de CSS, o sea
  **732 px reales** en un teléfono 3×. Con 800×800 sobra.
- **Fondo transparente** (`.webp` o `.png`). Detrás hay un degradado azul
  oscuro y la ilustración se apoya en él; un fondo blanco se vería como un
  parche.
- Sirven también `.png` y `.jpg`, en ese orden de preferencia.
- **Solo manos.** Es lo único que uno ve de sí mismo al llegar a un turno,
  y es lo que mantiene los tres golpes como una sola secuencia.

Para que entren, `python3 tools/generar_app.py` (y `--pwa`). No hay que
tocar código.
