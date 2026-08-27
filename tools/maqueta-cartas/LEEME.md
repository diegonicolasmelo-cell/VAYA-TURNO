# Maqueta de cartas — las tres opciones

Genera la página que compara las tres maquetaciones con el arte real y los
datos de los CSV vivos. Es una herramienta de decisión, no parte de la app.

    cd tools/maqueta-cartas && python3 gen.py

Necesita las miniaturas WebP del arte en esta carpeta (una por id de carta).
Se hacen desde `cartas/arte-full/` con un thumbnail a 760 px de ancho.

## Las tres

| | arte | texto | dónde sirve |
|---|---|---|---|
| **A · Ventana** | ventana enmarcada, 42 % del alto | siempre sobre papel | el más legible, el menos full art |
| **B · Dos tercios** | a sangre arriba, 64 % del alto, se disuelve en el panel | sobre papel | **el elegido** |
| **C · Sangre** | toda la carta | panel esmerilado flotante | el más bonito sin reglas, el peor con reglas |

En las tres, la carta chica (132 px) suelta las reglas y la frase: en la app
se toca y se abre grande, así que ahí solo van nombre, chips, vida y
requerimientos.

## Cuatro trampas de CSS que costaron

1. **`font-size:calc(var(--w)/222*1rem)` es inválido.** px dividido por un
   número da px, y px por rem no existe, así que el calc se descartaba
   entero y TODAS las cartas heredaban 16 px — la carta chica llevaba la
   letra de la grande. Lo correcto es `calc(var(--w)*.0721)`.
2. **`flex-basis` en % no resuelve** contra un alto que viene de
   `aspect-ratio`: se cae a `auto` y la zona de arte tomaba el alto entero
   de la imagen. Los altos van en `calc` sobre el ancho.
3. **`aspect-ratio` no da un alto definido** para el reparto flex de los
   hijos. El alto de la carta va explícito: `calc(var(--w)*1.3968)`.
4. **`{expr,}` dentro de un f-string es una tupla** y se imprime su `repr`,
   con comillas y `\n` escapados. Una coma de más metía texto basura en el
   HTML — y esos `\n` sueltos eran los que desbordaban las cartas.

## Cuánto de la escena se ve

El hueco del arte en la opción B es casi cuadrado (222 × 198). Medido con
`object-fit: cover`, esto es lo que entra de la ilustración según su forma:

| hueco | arte 9:16 | arte 3:4 | arte 1:1 | arte 4:3 |
|---|---|---|---|---|
| paciente y protocolo (64 %) | **50 %** | 67 % | 89 % | 100 % |
| avatar largo (52 %) | **41 %** | 55 % | 73 % | 97 % |
| carta entera (opción C) | 79 % | 100 % | 100 % | 100 % |

Por eso los personajes se ven pegados a la cámara: con 9:16 solo entra la
mitad del alto. **El arreglo no es CSS, es la forma del archivo** — para la
opción B hay que generar en 1:1.

Mientras tanto, `.zona-art.aire` mete la imagen al 78 % del ancho en vez de
llenar el hueco (se ve un 64 % en vez del 50 %) y rellena los costados con
`TINTE`, la mediana del borde de la propia ilustración. Con arte monocromo
no se nota.

## Lo que Pokémon sí aporta

El coste de energía. Una línea de ataque Pokémon es «fichas de color, el
nombre, y el número a la derecha», y se lee sin leer. Nuestros
requerimientos son exactamente eso, y estaban dibujados como casilleros
vacíos. Aquí pasan a fichas redondas del color del tipo, y a 132 px se
sueltan las palabras y quedan solo las fichas — igual que en el coste del
ataque, que no lleva ninguna.
