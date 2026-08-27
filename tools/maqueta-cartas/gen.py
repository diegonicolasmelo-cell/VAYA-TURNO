#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from datos import *
from cartas import JUEGOS, cuarteto
from estilo import CSS

AQUI = os.path.dirname(os.path.abspath(__file__))

def mini(op):
    p, r, a, v = JUEGOS[op]
    return (p("P11", "center 24%") + r("R07", "center 42%") +
            a("A01", "center 30%") + v("C19", "center 20%"))

def opcion(letra, nom, resumen, cuerpo, si, no):
    return f'''<div class="op">
<h3><span class="letra">{letra}</span> {nom}</h3>
<p class="resumen">{resumen}</p>
{cuerpo}
<div class="mazo">{cuarteto(letra.lower())}</div>
<p class="rotulo">Y a 132 px, que es como se ve en la cama del tablero</p>
<div class="mini">{mini(letra.lower())}</div>
<div class="balance">
 <div class="si"><h5>A favor</h5><ul>{''.join(f'<li>{x}</li>' for x in si)}</ul></div>
 <div class="no"><h5>En contra</h5><ul>{''.join(f'<li>{x}</li>' for x in no)}</ul></div>
</div></div>'''

CUERPO = f'''
<div class="env">
<p class="eyebrow">Tres maquetaciones · mismo arte, mismos datos</p>
<h1>Cómo repartir la carta</h1>
<p class="bajada">Las tres llevan el avatar con el texto al frente y están
pensadas para el juego digital primero. Cada una reparte el mismo contenido
de otra manera. Míralas en el teléfono: es donde se juega.</p>

<section>
<p class="eyebrow">Lo que preguntaste primero</p>
<h2>Qué tienen que ver las cartas Pokémon</h2>
<p>Más de lo que parece, pero no por donde crees. La carta Pokémon clásica
<strong>no es full art</strong>: la ilustración va en una ventana enmarcada
que ocupa como el 45&nbsp;% de la carta, con el nombre y los PS arriba y la
caja de ataques abajo. Lo que tú describes —imagen en los dos tercios de
arriba— es más bien el formato de <em>Lorcana</em> o de las cartas
<em>full&nbsp;art</em> de Pokémon, que son la excepción cara del sobre.</p>

<p>Pero hay una cosa de Pokémon que <strong>sí deberíamos copiar tal cual</strong>,
y es la que resuelve nuestro problema más difícil:</p>

<div class="tabla-env"><table>
<thead><tr><th>Pokémon</th><th>¡Vaya Turno!</th><th>¿Se traduce?</th></tr></thead>
<tbody>
<tr><td>PS del Pokémon</td><td>❤️ Vida del paciente</td><td class="si">Directo</td></tr>
<tr><td>Símbolo de tipo (🔥💧⚡)</td><td>Sistema (Resp / Card / Neuro / Metab / Quir)</td><td class="si">Directo</td></tr>
<tr><td><strong>Coste de energía del ataque</strong></td>
    <td><strong>Requerimientos del paciente</strong></td>
    <td class="si">Directo — y es lo importante</td></tr>
<tr><td>Caja de ataques</td><td>Las filas de requerimiento</td><td class="si">Directo</td></tr>
<tr><td>Debilidad / resistencia / retirada</td><td>Alta y fallece</td><td>Parecido</td></tr>
<tr><td>Ventana de arte enmarcada</td><td>—</td><td class="no">Aquí nos separamos</td></tr>
</tbody></table></div>

<div class="nota bien">
<h4>Lo que hay que robarle a Pokémon</h4>
<p>El <strong>coste de energía</strong>. Una línea de ataque Pokémon es
«tres fichas de color, el nombre, y el número a la derecha», y se lee sin
leer: cuentas las fichas de un vistazo. Nuestros requerimientos son
exactamente eso —dos de Fármacos, uno de Personal— y hasta ahora los
dibujábamos como casilleros vacíos.</p>
<p>En las tres opciones de abajo los cambié a <strong>fichas redondas del
color del tipo</strong>. Es el cambio que más se nota a 132&nbsp;px, y no
depende de cuál maquetación elijas.</p>
</div>
</section>

<section>
<p class="eyebrow">Las tres</p>
<h2>Opciones</h2>
<p>En las tres se ve la misma carta: ACV en Ventana, Cristaloides, El Que
Guarda Siempre Tiene y El Diostor — a propósito el avatar más largo del
mazo, 250 caracteres, para que veas el peor caso y no el bonito.</p>

{opcion("A", "Ventana", 
  "El marco clásico. La ilustración vive en una ventana enmarcada y nunca "
  "hay texto encima de ella. Es la solución de Pokémon, Magic y casi todo "
  "juego con reglas largas.",
  "",
  ["El texto va siempre sobre papel: se lee perfecto, siempre, en cualquier carta.",
   "El arte nunca compite con la tipografía — la ilustración se ve limpia.",
   "El panel crece hacia abajo sin romper nada: aguanta los 309 caracteres de La Gestora de Camas.",
   "Es la más fácil de imprimir y la más barata de leer en la mesa."],
  ["No es full art. La ilustración baja a un 40&nbsp;% de la carta.",
   "Se ve más “juego de mesa clásico” y menos videojuego.",
   "Con arte 9:16 el recorte a ventana 4:3 es brutal: se pierde más de la mitad."])}

{opcion("B", "Dos tercios",
  "Lo que pediste. El arte entra a sangre por arriba y baja hasta un 64&nbsp;%, "
  "donde se disuelve —no se corta— en un panel sólido. El nombre y las reglas "
  "viven en el panel.",
  "",
  ["El arte manda: dos tercios de la carta, a sangre, sin marco que lo encierre.",
   "El texto sigue sobre papel sólido: se lee tan bien como en la opción A.",
   "El borde del arte se disuelve en el panel, así que no hay una línea dura cruzando la carta.",
   "La altura del arte puede variar por tipo — el recurso llega al 72&nbsp;%, el avatar baja al 52&nbsp;%."],
  ["El panel tiene un presupuesto fijo: si el texto no cabe, hay que acortar la regla.",
   "Con 250 caracteres el avatar baja el arte al 52&nbsp;%, y ahí ya no son dos tercios.",
   "La línea horizontal se repite en las 115 cartas: el mazo se ve más uniforme, para bien y para mal."])}

{opcion("C", "Sangre",
  "Full art de verdad. La ilustración ocupa la carta entera y el texto flota "
  "encima en un panel esmerilado que solo crece lo que necesita.",
  "",
  ["Cristaloides queda 100&nbsp;% ilustración: no tiene reglas, así que no hay panel. Es la carta más bonita de las tres opciones.",
   "El panel se encoge cuando el texto es corto — el mazo respira distinto carta a carta.",
   "Es la que más se parece a un juego digital moderno.",
   "El arte se ve entero, incluidos los bordes."],
  ["El texto sobre imagen siempre se lee un punto peor, por mucho velo que le pongas.",
   "El Diostor a 132&nbsp;px queda tapado casi entero por su propio panel — míralo arriba.",
   "El tamaño del panel cambia carta a carta: el mazo se ve menos ordenado.",
   "En papel, el esmerilado no existe: hay que reemplazarlo por un panel opaco y pierde la gracia."])}
</section>

<section>
<p class="eyebrow">Mi recomendación</p>
<h2>B para el juego, y una cosa más</h2>
<p><strong>La B es la respuesta</strong>, y no solo porque sea la que pediste.
Es la única que te da el arte grande <em>y</em> el texto sobre papel. La C se
ve mejor en las cartas sin reglas y peor en todas las demás, y en el juego
las cartas con reglas son la mayoría. La A es la más segura pero renuncia a
lo que quieres.</p>

<div class="nota">
<h4>La cosa más</h4>
<p>En el juego digital <strong>la carta chica y la carta abierta no tienen
por qué llevar la misma maquetación</strong>, y hoy ya no la llevan. La carta
en la cama solo necesita nombre, gravedad, sistema, vida y requerimientos
—nunca el texto de reglas, porque la tocas y se abre—. Así que:</p>
<p>· <strong>Carta abierta y papel:</strong> opción B, arte a dos tercios.<br>
· <strong>Carta en la cama:</strong> la misma B con el panel reducido a
requerimientos, sin frase ni reglas. Es la que se ve arriba a 132&nbsp;px y
funciona.</p>
</div>

<ul class="lista">
<li><strong>Proporción:</strong> sigue siendo 3:4 para generar. Con la B el
recorte duele menos, porque el tercio de abajo del arte se disuelve igual.</li>
<li><strong>El encuadre de los prompts cambia:</strong> hoy pide la cara en la
mitad superior por la tira de 44&nbsp;px. Con la B hay que pedirla en el
<strong>tercio central</strong>, para que no la coma ni el borde de arriba ni
la disolvencia de abajo.</li>
<li><strong>Los avatares con más de 200 caracteres van a apretar</strong> en
cualquiera de las tres. Vale la pena revisar los cuatro o cinco más largos y
ver si se pueden decir más corto — es trabajo de reglamento, no de diseño.</li>
</ul>
</section>
</div>
'''

PAG = f'''<title>Cómo repartir la carta</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Petrona:ital,wght@0,400;0,700;1,400&family=Archivo+Narrow:wght@400;600;700&family=IBM+Plex+Mono:wght@400;600;700&display=swap">
<style>{CSS}</style>
{CUERPO}
'''
sal = os.path.join(AQUI, "opciones-carta.html")
open(sal, "w", encoding="utf-8").write(PAG)
print(f"✔ {sal} ({os.path.getsize(sal)/1024:.0f} KB)")
