# La arquitectura de la carta y cómo debe venir el arte

Medido sobre la app de verdad a 390×844 (no estimado): se metió una rejilla
de 10×10 celdas en cada hueco de ilustración y se leyó qué franja del
original sobrevive. Todo lo de abajo sale de esa medición.

## Lo primero, porque es lo que más cambia

El arte de hoy viene en **1536×2752 — vertical 9:16**. Los huecos de la app
son **horizontales**. Por eso los personajes salen pegados a la cámara: no
es el CSS, es la forma del archivo. Toda la tanda nueva va en **4:3
horizontal**.

- **Formato:** 4:3 horizontal · **1600×1200 px** (mínimo 1200×900).
- **Archivo:** PNG o JPG de origen; el generador lo pasa a WebP y calcula
  solo el tinte del borde.
- El hueco más grande de la app es la carta en zoom: 342×274 CSS px, que a
  3× de densidad son 1026×822 reales. 1600×1200 deja margen de sobra y no
  pesa de más una vez convertido.

## Qué se ve de la imagen en cada vista

Con un original 4:3, esto es exactamente lo que entra en pantalla:

| Vista | Hueco | Aspecto | Se ve de ancho | Se ve de alto |
|---|---|---|---|---|
| Cama del tablero | 93×79 | 1,18 | 5,7 % – 94,3 % | todo |
| Carta en la mano | 108×72 | 1,50 | todo | 2,9 % – 91,8 % |
| Carta en zoom | 342×274 | 1,25 | 3,1 % – 96,9 % | todo |
| Retrato del avatar (círculo) | 82×82 | 1,00 | 12,5 % – 87,5 % | todo |

## La zona segura

Cruzando las cuatro filas:

- **Recursos, acciones y pacientes:** deja libre un **6 % por cada costado**
  y un **3 % arriba / 8 % abajo**. Todo lo que importe, dentro de ese marco.
- **Avatares y personajes:** el recorte circular es más duro. La cara y la
  cabeza tienen que caber en el **75 % central del ancho** (del 12,5 % al
  87,5 %) y el centro de la cara alrededor del **35 % desde arriba**, que es
  donde apunta el encuadre del círculo.

## El degradado: el tercio de abajo se disuelve

La ilustración no se corta con una línea: **se funde en el papel de la
carta**. El degradado ocupa el 26 % de abajo en el zoom, el 30 % en la cama
y el 34 % en la mano. Traducido al original:

- **De un 60 % de alto para abajo, la imagen empieza a lavarse.**
- **El último 8 % se pierde entero.**

Regla práctica: **cara, manos y silueta en los dos tercios de arriba.** Lo
de abajo es suelo, camilla, sombra, mesa — cosas que pueden desaparecer sin
que se note. Es lo mismo que hace una carta impresa cuando el arte entra a
sangre por arriba y muere bajo el textbox.

## El marco blanco

La carta lleva un **filete blanco fino** alrededor del arte, proporcional al
ancho de cada vista (≈2,8 %): 3 px en la mano y en la cama, 7 px en el zoom.
El arte **no sangra al filo de la carta, sangra al filete**. Para el arte
esto no cambia nada —el recorte ya está contado en la tabla— pero sí importa
saberlo: la ilustración nunca toca el borde exterior, así que un detalle
pegado al canto siempre queda escondido bajo el marco.

## Encuadre y estilo

- **Plano medio.** Ni primer plano ni cuerpo entero: de la cintura para
  arriba, con aire alrededor. Un primerísimo plano en 4:3 se ve peor que en
  9:16, porque ahora entra más escena y la cara queda enorme.
- **Personaje centrado horizontalmente.** Los recortes laterales son
  simétricos en todas las vistas menos el círculo del avatar, que también es
  simétrico. Nada descentrado sobrevive igual en las cuatro.
- **Fondo que aguante el degradado.** Como el tercio de abajo se funde en
  blanco, conviene que ahí haya tono medio o claro; un negro plano abajo
  hace una banda sucia al fundirse.
- **Tinte del sistema.** El generador saca de la propia imagen la mediana de
  su borde y la usa de fondo del hueco, para cuando la imagen no lo llena.
  Si el borde de la ilustración es del color de su sistema (respiratorio,
  cardíaco, neuro, metabólico, quirúrgico), el hueco y la carta combinan
  solos.

## Checklist antes de dar una imagen por buena

1. ¿Es 4:3 horizontal, 1600×1200?
2. ¿La cara está en los dos tercios de arriba?
3. ¿Cabe todo lo importante dejando 6 % de margen a los lados?
4. Si es avatar: ¿la cabeza está dentro del 75 % central del ancho?
5. ¿El tercio de abajo puede desaparecer sin que la carta pierda sentido?
