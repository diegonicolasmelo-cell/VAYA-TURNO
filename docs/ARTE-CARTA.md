# La arquitectura de la carta y cómo debe venir el arte

**v0.57 — la ventana enmarcada.** Hasta ahora la ilustración entraba a
sangre y se disolvía en el papel de la carta: el tercio de abajo se perdía
y había que dibujar contra un degradado. Se acabó. Ahora el arte vive en
una **ventana con marco, y se ve entera**.

Todo lo de abajo está medido sobre la app de verdad a 390×844, metiendo una
rejilla de 10×10 celdas en **todas** las ranuras a la vez y comprobando que
el filete rojo del borde de la rejilla sobrevive en las cuatro esquinas. No
hay nada estimado.

---

## La regla, en una línea

> **Una sola imagen por carta, 4:3 horizontal, 1600×1200 px.
> Se ve completa en todas las vistas rectangulares. No se recorta nada.**

Eso es todo lo que hay que saber para dibujar. El resto de este documento
es el detalle, y solo hace falta para los dos casos con recorte redondo y
para saber qué esquinas quedan bajo una insignia.

---

## Formato del archivo

- **Proporción:** 4:3 horizontal, exacta. No 3:2, no 16:9, no vertical.
- **Tamaño:** **1600×1200 px**. Mínimo aceptable 1200×900.
- **Archivo:** PNG o JPG. El generador lo convierte a WebP, lo baja a
  800 px de ancho y calcula solo el tinte de su borde.
- Los originales grandes viven en `cartas/arte-full/`; los que entran al
  juego, en `cartas/arte/<ID>.jpg` — el nombre es el id de la carta
  (`P02`, `R07`, `A19`, `C17`…).
- **No hace falta acertar el tamaño al píxel.** El generador de imágenes
  entrega 2400×1792, que es 4:3 con 0,45 % de sobra;
  `tools/ingresar_arte.py` recorta esos diez píxeles de ancho, guarda el
  original y deja la copia de juego en 1600×1200. Lo que importa es la
  proporción horizontal, no el número exacto.
- **Una carta repetida no necesita su propio archivo.** R32 y R33 son las
  dos «Gases Arteriales»: con `R32.jpg` basta, la gemela hereda por nombre.

### Por qué 4:3 y no lo de antes

El arte actual viene en **1536×2752 — vertical 9:16**, y las ranuras son
horizontales: dos tercios de cada archivo se tiraban en el recorte. Con
4:3 no se tira nada, y eso paga solo una subida de calidad. Medido sobre
las diez ilustraciones que hay:

| fuente | tope de ancho | peso por carta | 115 cartas |
|---|---|---|---|
| 9:16 (hoy) | 520 px | 42,5 KB | ≈ 4,8 MB |
| **4:3 (nuevo)** | **800 px** | **46,1 KB** | **≈ 5,2 MB** |

Mismo peso, **54 % más de resolución visible**. El tope del generador ya
subió a 800 px por eso.

---

## Qué se ve en cada vista

Con un original 4:3 se ve **el 100 %** en todas las ranuras rectangulares.
Las medidas son píxeles CSS en un teléfono de 390 de ancho; multiplica por
la densidad de pantalla (×3 en un teléfono bueno) para saber la resolución
real que se le pide al archivo.

| Vista | Ranura CSS | En pantalla a 3× | Se ve |
|---|---|---|---|
| Carta en la mano (abanico) | 90 × 67,5 | 270 × 202 | **todo** |
| Cama del tablero (ficha) | 93 × 70 | 279 × 210 | **todo** |
| Protocolo guardado | 144 × 108 | 432 × 324 | **todo** |
| Elegir personaje (pantalla completa) | 244 × 183 | 732 × 549 | **todo** |
| Carta de avatar (la que gira) | 252 × 189 | 756 × 567 | **todo** |
| **Carta o paciente en zoom** | **342 × 256,5** | **1026 × 770** | **todo** |
| Retrato del mesón (círculo) | 94 × 94 | 282 × 282 | recorte, ver abajo |
| Miniatura de lo puesto (círculo) | 22 × 22 | 66 × 66 | recorte, ver abajo |

**La ranura que manda es el zoom: 1026 px reales de ancho.** Por eso el
original quiere 1600 y el generador guarda 800.

---

## Los dos recortes redondos

Son los únicos sitios donde se pierde imagen, y los dos recortan igual:
**el cuadrado central**, y de ese cuadrado, el círculo inscrito.

- Se conserva el **75 % central del ancho** (del 12,5 % al 87,5 %) y **todo
  el alto**.
- De ese cuadrado, el círculo se come las esquinas.

Traducido a lo que hay que dibujar: **la cabeza y la cara dentro del 75 %
central del ancho, y el centro de la cara alrededor del 45 % desde
arriba.** Un personaje descentrado sobrevive en la carta y se decapita en
el círculo.

Y una advertencia que salió de la primera tanda de arte 4:3: **una escena
ancha se lee estupendo en la carta y se pierde en el círculo.** La Jefa de
Unidad detrás de su mesón, con dos enfermeras al fondo y la pizarra de
turnos, es una gran ilustración; en los 94 px del retrato del mesón su cara
mide unos ocho píxeles. Si el personaje va a salir en el mesón, el plano
tiene que estar más cerrado que el de una escena.

Esto aplica a **avatares y personajes** (`C##`), que son los que salen en
el mesón. Recursos, acciones y pacientes no pasan nunca por un círculo
grande — solo por la miniatura de 22 px de «lo puesto en este paciente»,
donde no se distingue una cara de todos modos.

---

## Las esquinas que quedan tapadas

La imagen se ve entera, pero encima suyo van insignias. Nada importante
debe caer bajo ellas.

**Carta (mano, zoom, protocolo)** — el índice del naipe: el símbolo del
recurso **en diagonal**, arriba a la izquierda y abajo a la derecha, como
en una carta de baraja. Cada sello tapa **22 % × 27 %** de la imagen en la
mano (menos en el zoom, porque el sello es fijo y la imagen crece).

**Cama del tablero** — tres insignias, y la del escudo va al medio:

- **esquina interior izquierda** (la que mira a la Pizarra): la gravedad,
  `G·II` o `★ROJO`, **27 % × 21 %**.
- **esquina interior derecha:** el número de lo que falta, **10 % × 29 %**.
- **centro, solo cuando el paciente está protegido:** el escudo 🛡️,
  **32 % × 46 %**. Es transitorio y no hay que componer para él, pero por
  eso conviene que el centro exacto no lleve el único detalle que importe.

**Elegir personaje y carta de avatar:**

- **arriba a la izquierda:** la etiqueta de frecuencia (`1×PARTIDA`,
  `PASIVA`, `1×RONDA`), un **28 % × 11 %** aproximado según el largo de la
  palabra.

Regla práctica que cubre todas: **deja libres las dos esquinas de la
diagonal —arriba-izquierda y abajo-derecha— y no pongas la cara pegada a
un costado.**

---

## El marco

La ilustración ya no sangra al filo: es una **ventana** dentro de la
carta, con el papel alrededor y un filete de 1 px. El arte no toca nunca
el borde exterior de la carta.

Para quien dibuja esto es una buena noticia y hay que aprovecharla: **el
borde de la imagen se ve**. Un fondo que muere en un degradado sucio
justo en el canto ahora se nota. Cierra la escena.

---

## Encuadre y estilo

- **Plano medio.** De la cintura para arriba, con aire alrededor. En 4:3
  entra más escena que en 9:16: un primerísimo plano queda enorme.
- **Personaje centrado horizontalmente.** Todos los recortes que quedan
  son simétricos; nada descentrado sobrevive igual en las ocho vistas.
- **El fondo ya no se funde en blanco.** Antes el tercio de abajo se
  lavaba y convenía dejarlo neutro. Ya no: **abajo se ve tanto como
  arriba**, así que ahí puede ir escena de verdad — camilla, suelo,
  monitores, lo que sea.
- **Tinte del borde.** El generador saca la mediana del borde de la propia
  imagen y la usa de fondo de la ranura, por si el redondeo deja ver un
  pelo de costado. Si el borde de la ilustración es del color de su
  sistema (respiratorio, cardíaco, neuro, metabólico, quirúrgico), carta y
  ranura combinan solas.

---

## Checklist antes de dar una imagen por buena

1. ¿Es **4:3 horizontal, 1600×1200**?
2. ¿El 20 % de arriba está libre de lo imprescindible? (van las insignias)
3. ¿El personaje está centrado a lo ancho?
4. Si es **avatar o personaje** (`C##`): ¿la cabeza cabe en el **75 %
   central del ancho**, con la cara a un **45 % desde arriba**?
5. ¿La escena cierra en los cuatro bordes? Ya no hay degradado que tape.
6. ¿El nombre del archivo es el id de la carta?

---

## Pendiente conocido

El zoom pide 1026 px reales y el generador guarda 800: se ve un pelo
blando si lo buscas. Subir a 1024 pondría las 115 cartas en ≈ 7 MB, y el
artefacto de un solo archivo tiene tope de 16 MB contando el tablero, la
portada y el resto. La salida limpia es guardar **dos tamaños** —uno de
~420 px para mano y camas, otro de ~1024 px solo para el zoom— y que el
zoom cargue el suyo. Está anotado en `PENDIENTES.md`; no cambia nada de lo
que hay que dibujar, porque los dos salen del mismo original de 1600.
