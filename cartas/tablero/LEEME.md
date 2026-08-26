# Arte del tablero

La ilustración de fondo del playmat: la unidad vista desde arriba.

- `sala-uci.jpg` — la sala de 3 camas, vista cenital con ojo de pez leve.
  El prompt que la generó está en `docs/PROMPTS-ARTE.md`, sección del
  tablero.
- La usa `tools/generar_playmat.py`, que la incrusta como fondo y dibuja
  encima las zonas de juego (slots de 63×88 mm, marcadores, contadores).
  Si el archivo no está, el generador dibuja un piso sintético.

**Si la reemplazas por otra versión**, revisa que las tres camas sigan
centradas en 20%, 51% y 81% del ancho y ocupando del 21% al 59% del alto;
si se movieron, hay que ajustar `CAMAS_X` y `CAMA_Y0/Y1` en el generador.
