# Prototipo: el avatar se agranda y se gira

    cd tools/maqueta-avatar && python3 gen.py

Necesita C01.webp, C19.webp y C17.webp en esta carpeta (miniaturas del arte
de `cartas/arte-full/`).

## La decisión

Diego preguntó si la habilidad va al reverso girando la carta, o si se
consulta al seleccionarla. **Son la misma cosa**: girar una carta de 132 px
deja un reverso de 132 px con 250 caracteres, ilegible. Para leer hay que
agrandar, y una vez agrandada, girar es el gesto natural.

Pero el reverso **no puede llevar las reglas**:

· Al empezar se elige entre tres avatares. Con la habilidad al reverso hay
  que girar tres cartas para comparar, y la decisión más importante del
  inicio pasa a ser un juego de memoria.
· En papel la carta queda frente a ti toda la partida. Por el lado de la
  habilidad nunca ves el dibujo; por el dibujo, no recuerdas tu poder.

**Se resuelve al revés**: la habilidad al FRENTE (maquetación B) y al
reverso la ilustración completa a sangre, sin una palabra, con el lustre
encima. Es la opción C, pero como premio en vez de como problema.

## Una trampa que valía para las tres maquetas

El artefacto arma su propio `<head>` y **no trae `meta viewport`**. Sin él
el teléfono maqueta a 980 px y todo sale diminuto — la carta de 260 px se
veía de 100. La app ya lo resolvía inyectándolo por JS
(`tools/app-plantilla.html`); las maquetas no, y hubo que ponerles el mismo
parche.
