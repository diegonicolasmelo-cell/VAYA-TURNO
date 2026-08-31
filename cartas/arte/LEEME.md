# Arte de las cartas

Aquí viven las imágenes que entran al juego. `generar_app.py` las incrusta
solo, sin pedir permiso a nadie.

- **El nombre del archivo es el id de la carta**: `P01.jpg` (paciente),
  `C03.jpg` (personaje/avatar), `R12.jpg` (recurso), `A22.jpg` (Acción).
- **Formato: 4:3 horizontal, 1600×1200.** El detalle completo —qué esquinas
  tapan las insignias, dónde va la cara— está en `docs/ARTE-CARTA.md`.
- Si falta el arte de una carta, la app se ve como hasta ahora: el arte es
  opcional carta por carta.
- Una carta repetida hereda de su gemela. R32 y R33 son las dos «Gases
  Arteriales»: basta con dejar `R32.jpg` y la otra se sirve sola.

Los ids están en `cartas/pacientes.csv`, `cartas/personajes.csv` y
`cartas/v030/`.

## No copies el archivo a mano

Para meter una imagen usa el guion, que además guarda el original:

    python3 tools/ingresar_arte.py C13 ~/bajadas/becado.jpg

Deja el original tal cual en `cartas/arte-full/<ID>.jpg` y aquí la versión
recortada a 4:3 exacto. Si la fuente no es 4:3, un tercer argumento entre 0
y 1 corre la ventana del recorte (0 = pegada arriba, 0,5 = centrada) para
que no se pierda la cabeza del personaje.

En lote, con un archivo de `id`, tabulador y ruta por línea:

    python3 tools/ingresar_arte.py --lote lote.tsv

## De dónde viene

Del Drive del autor, carpeta **«Vaya turno Claude»**. Ahí se dejan los
archivos con el nombre que uno quiera —«Enfermera de noche.jpg»— y el
guion los renombra al id que les toca.
