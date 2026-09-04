# Pendientes de desarrollo — ¡VAYA TURNO! v0.21

La lista viva de lo que falta, carta por carta y mecánica por mecánica.
Se trabaja de arriba hacia abajo: lo de arriba bloquea el playtest, lo de
abajo puede esperar años sin que pase nada.

**Convención de estado:**
- ⬜ pendiente · 🔶 definido pero sin validar en mesa · ✅ cerrado

---


## 0. LA DECISIÓN GRANDE: ¿v0.21 o v0.30?

Existen dos juegos en el repo y **el playtest debe elegir**:

- **v0.21 (estable):** solitario paralelo con sabotaje ocasional vía
  Acciones. `REGLAMENTO.md`, `cartas/`, `tools/simular.py`, taller y PDF.
- **v0.31 (elegida por el autor, balanceada):** la rama del sabotaje —
  **tres fases por turno**, sin El Pasillo —
  ⚠️ de doble filo, Pizarra, admisión obligatoria, piso universal ("colocar
  nunca mata"), Sumario que muerde la mano. `REGLAMENTO-v030.md`,
  `cartas/v030/`, `tools/simular_v030.py`, PnP con `--variante v030`.
  Suelo medido en `DISENO.md` §4k: salv 67% · GIII 43% · todo en banda.

**Para probar la v0.30 sin cartas** está `docs/app.html` (se genera con
`python3 tools/generar_app.py`): árbitro digital en un solo archivo, contra
la IA o entre dos en un teléfono. Lleva el reloj, los ✅, la ventana de alta,
las ⚠️, las 🛡️, la basura y los Sumarios; las Acciones se juegan solas desde
la Pizarra; las habilidades de avatar se aplican a mano y quedan en la
bitácora, que se copia al portapapeles para pegarla acá. Para quien juega
por primera vez está **La Residencia** en la portada (§5d): diez casos
clínicos armados a mano, uno por mecánica, y al final la partida entera
con el coach de 10 pasos que era la antigua "Primera guardia".

**El holograma de la carta grande** (referencia: Pokémon TCG Pocket): al
ver una carta en grande se inclina en 3D siguiendo el dedo, con una luz
que la recorre y resorte al soltar; en Android además responde al
giroscopio sin tocarla (iPhone exige permiso con gesto, ahí es solo al
dedo). Las cartas con sistema (×2) y los comodines llevan la banda
iridiscente arcoíris — jerarquía de rareza visual. Sin assets nuevos:
puro CSS/JS, y cuando llegue el arte los reflejos caen encima solos.

⬜ **Cartas que cambian de imagen según lo que se les coloca** (idea del
autor, agosto 2026): el paciente parte sin intubar y al recibir
Ventilación Mecánica su ilustración cambia a intubado; lo mismo con
Pleurostomía y otros procedimientos icónicos. **Medido antes de decidir**
(2.000 partidas, 2 jugadores): los recursos icónicos SÍ aterrizan seguido
— VM **2,52 por partida** (1,26 por jugador), CVC 2,52, Noradrenalina
2,29, Enfermera de UCI 2,11, Línea Arterial 1,76, Kinesiólogo 1,70,
Pabellón 1,36, Cirujano 0,86, Pleurostomía 0,54; el Personal completo
suma 8,12 por partida. O sea: el efecto se vería ~1,3 veces por guardia
por jugador, no es un adorno que nadie alcanza a ver.

Lo técnico está resuelto: la app ya guarda en `cama.puestos` las cartas
completas, así que reaccionar a un id concreto es trivial. **El costo son
imágenes, no código.**

🔴 **El riesgo clínico está medido y es real**: la VM cae sobre pacientes
de **Gravedad I el 12% de las veces** (el juego reparte recursos por
tipo, no por indicación). Dibujar intubada a la Crisis de Pánico en Box 4
sería enseñar al revés. Si se hace, el cambio de imagen debe exigir
**Gravedad II o mayor**; en Gravedad I el recurso se coloca igual pero la
ilustración no cambia.

Tres fases posibles, de menor a mayor costo de arte:
- **Fase 0 — insignias de equipo (0 imágenes)**: la cama muestra qué
  lleva puesto (tubo, catéter, línea, drogas) con los iconos que ya
  existen. Todo el valor educativo de "qué le puse a este paciente", sin
  arte nuevo.
- **Fase 1 — retrato de alta (26 imágenes)**: el paciente recuperado para
  la ceremonia de egreso. Es el estado que más se ve (~3 altas por
  guardia) y el más satisfactorio.
- **Fase 2 — retrato intervenido (18 imágenes)**: la idea original, solo
  para Gravedad II+.

Las capas transparentes (dibujar el tubo aparte y superponerlo) serían lo
barato en teoría —el encuadre de pacientes ya está estandarizado en
BRIEF-IA §5.1— pero la generación con IA no registra con precisión
suficiente: un tubo flotando cerca de la boca se ve peor que no tenerlo.

**Estado: en pausa por decisión del autor** (agosto 2026) mientras se
genera el arte base. Nada implementado; los números quedan aquí para
retomarla.

**La sala ilustrada está en los dos tableros.** El playmat físico
(`docs/playmat.svg`, 440×438 mm) usa la sala entera de
`cartas/tablero/sala-uci.jpg` como fondo y le monta encima las zonas
vectoriales: slots de 63×88 mm, marcador de vida y contadores. En el
juego digital, `tools/generar_sala_app.py` recorta de esa misma
ilustración la banda de las tres camas y la pone detrás de cada unidad —
la tuya y la del rival girada 180°, como si estuviera al otro lado de la
mesa. La franja se estira un 12% desde el centro para que las camas
dibujadas (20%, 51% y 81% de la ilustración) caigan bajo las columnas de
cartas (17%, 50% y 83%): cada carta se apoya sobre su cama, y una cama
vacía se ve como una cama vacía de verdad. La imagen va lavada al 45%
hacia el blanco porque detrás van cartas: si compite con ellas deja de
ser tablero y pasa a ser ruido.

**La Pizarra es una pizarra magnética de verdad** (v0.51): marco cromado
con bandas claras y oscuras, superficie blanca satinada, protectores de
esquina de plástico negro —triangulares y periféricos: cortan el canto en
diagonal y la pizarra termina en ellos— y un
reflejo que la recorre cada 6,5 s. La tira del tablero y el cajón abierto
llevan el mismo marco: al desplegarla no cambias de objeto, la miras de
cerca. Cuatro cosas que costó acertar y conviene no volver a romper: el
marco NO puede hacerse con `border-image` (`slice:1` toma un píxel por
lado y cada borde sale de un color liso — hay que usar dos capas,
`padding-box` para la superficie y `border-box` para el metal); el
reflejo NO puede ser un `::before` (con `z-index:-1` queda tras el fondo
opaco y con `0` tapa el texto — va como capa del `background`, que se
pinta sobre la superficie y bajo las letras); y el reflejo NO puede ser
blanco, porque sobre una pizarra blanca el blanco no se ve: lo que se lee
son sus filos, una sombra fría delante y un filo espectral detrás. Y la
cuarta: la tira del tablero NO puede llevar `overflow:hidden`, porque
`overflow` recorta al *padding-box* y los protectores de esquina viven en
el área del borde (`inset:-6px`) — se los comía enteros y la tira quedaba
sin tapitas mientras el cajón sí las mostraba. El aviso de "hay algo
comprable" tampoco puede ser un aro duro de 2 px: sobre el cromado se lee
como un segundo marco turquesa encima del metal, así que es un resplandor
difuso.

**El campo v0.55** es la reestructura grande (adaptada de Battlegrounds,
con la ropa de la unidad — el mockup vive en el artifact del campo):

· **La cama con arte es una ficha**: ilustración, marco del color de la
  gravedad, corazones, los requerimientos aplanados a fichas de color y el
  «faltan» grande. El nombre y el desglose viven en el zoom (tocar la
  cama). Sin arte queda la carta clásica, transitorio.
· **El rival es una ficha consultable** con badge ✅ alta ×N / ⚠ cerca;
  tocarla abre su unidad en un cajón vivo donde también se sabotea.
· **El zócalo**: retrato al centro con el ANILLO de indicaciones (tres
  segmentos que se apagan al colocar; volarIndic aterriza ahí), el poder
  ⚡ al hombro (late disponible, hoja con Usar/Ver carta), Sumarios al
  otro lado.
· **Fin de Guardia** es el botón redondo de la esquina opuesta. OJO: .pie
  es pointer-events:none y cada hijo tocable lo reactiva — sin
  pointer-events:auto el botón se dibuja pero no se toca.
· **Urgencias/Guardia en rieles** a los bordes (.app.partida les hace
  sitio con padding); al centro queda solo «Próximo: …».
· **La mano es un selector**: miniaturas al filo con scroll nativo; tocar
  abre la carta grande (‹ › y «Jugar esta»), luego tocas la cama. La
  cuadrícula queda SOLO para descartes. El plegado murió (UI.manoOculta
  es bandera inerte para no romper guardias guardadas).
· **El ARRASTRE se retiró**: el flujo es tocar carta → Jugar esta → tocar
  cama. Código muerto por purgar en una pasada propia: arrastre/tomarCarta,
  ponRanura/abanicoVivo/hojear*, manoAbanico/cambiarModoMano, CSS de
  .ranura/.abanico/.mano-cerrada/.btn-plegar/.indic-caja, y el driver
  gesto.py del scratchpad quedó obsoleto.
· **Emotes**: tocar tu retrato abre 4 burbujas (3 de la casa + la frase de
  tu avatar); burbuja viva 2,6 s; la IA contesta con la frase del suyo el
  65% de las veces; anti-spam 3,5 s.
· Una trampa que costó: la clase «ficha» ya existía (fichitas de la tira
  del avatar, display:flex) y bautizar igual el modo de la cama la
  colapsaba a 35 px — por eso el modo se llama `pficha`.

**El campo B convive con el A** (v0.56). No reemplaza nada: se elige en
el Panel de guardia y se recuerda en `localStorage` (`vt-maqueta`), la
partida guardada es la misma y se puede volver a **A** en cualquier
momento. Todo el CSS cuelga de `body[data-maq="b"]`, así que la maqueta A
no cambia ni un píxel. Qué hace B:

· **La Pizarra parte la pantalla en dos mitades iguales** (`flex:1 1 0`
  en las dos zonas, así que miden lo mismo pase lo que pase). Arriba su
  unidad, abajo la tuya, y cada mitad es el espejo de la otra: repisa /
  zócalo en los bordes exteriores y las camas contra la Pizarra.
· **Sus camas son la misma pieza y el mismo tamaño que las tuyas**, sólo
  que espejadas (`flex-direction:column-reverse`): corazones y
  requerimientos quedan del lado de la Pizarra, mirando a los tuyos. Con
  eso `chipRival`/`modalRival` dejan de hacer falta en B — la unidad del
  rival ya está en pantalla.
· **La cama baja de perfil**: la ventana de arte pasa de 1:1 a 4:3. No es
  un sacrificio: por la medición de más abajo, 1:1 muestra el 89 % de la
  escena y 4:3 el 100 %. Más baja *y* con más ilustración.
· **La repisa del rival** es el espejo del zócalo: retrato con su anillo
  de indicaciones, su pasiva, el badge ✅/⚠ y su mano como dorsos.
· **La mano vuelve a abrirse**: mazo compacto al filo → se despliega en
  abanico sobre TU zócalo (nunca sobre las camas) con las cartas a 106 px,
  que es donde se leen. Tocarla la elige y cierra el abanico (respaldo, 2
  toques); mantenerla presionada abre la carta grande; **arrastrarla la
  juega**, hacia abajo tratas y hacia arriba saboteas.
· **El arrastre no estaba muerto, estaba durmiendo**: el código de
  `arrastre`/`tomarCarta`/`moverCarta`/`soltarCarta` seguía entero desde
  v0.55 sin llamadas. B lo vuelve a enganchar sin tocarlo, y como
  `vistaCama` ya resolvía el destino rival (`puedeSabotear` + `__soltar`),
  el sabotaje por arrastre salió gratis. **Corrección al punto de arriba:
  ese bloque ya no es código muerto por purgar.**
· Dos trampas del arrastre en B: el velo del abanico declara
  `pointer-events:auto` para poder cerrarse al tocarlo, y hay que
  apagarlo explícitamente con `body.arrastrando` o se come el
  `elementFromPoint` y la cama nunca recibe la carta. Y
  `transform-origin:50% 130%` en las ranuras del abanico empuja las
  cartas de los extremos fuera de la pantalla al escalarlas (`s<1` las
  aleja del origen): con origen al centro el arco es predecible.

**El campo B, segunda pasada** (v0.57), con las tres cosas que salieron de
probarlo:

· **La mano se navega.** El hojeo de v0.55 seguía escrito pero apuntaba a
  `.mano.abanico`; B lo enganchó al arrastre y no al hojeo, así que
  cualquier dirección arrancaba un arrastre y con seis cartas apiladas la
  mano era ilegible. Ahora `abanicoVivo`/`hojearMover`/`abanicoVivoSnap`
  sirven a las dos maquetas (`contAbanico()` resuelve cuál) y la geometría
  de B es continua (`ponRanB`), igual que la de A. Vale la regla vieja: de
  lado navegas, hacia arriba juegas, y el empate favorece navegar.
· **Las mitades son espejo exacto**, no sólo del mismo alto. Antes medían
  igual (342 y 340) pero por dentro no: repisa 56 vs zócalo 92, aire 130 vs
  65, camas 136 vs 158. Ahora las dos mitades llevan la MISMA estructura
  —rótulo · camas · aire · repisa— y la de arriba va en `column-reverse`;
  con la repisa y el zócalo en 84 y la fila de camas en 118 fijos, el aire
  sale igual por construcción. Medido: 84/84, 172/172, 118/118.
· **En B toda cama es ficha**, tenga arte o no: sin ilustración va el ícono
  del sistema sobre un tinte de reserva (`TINSIS`). Sin eso la fila no puede
  tener alto fijo, porque la carta clásica crece con su contenido.
· **Se van la barra de estado y la franja de guía**: 86 px, el 10 % de la
  pantalla, y rompían la simetría por definición (había franja arriba y
  ninguna abajo). La ronda y la fase se mudan al reloj, el ☰ al lado de la
  Pizarra, y el aviso pasa a ser una pastilla que sale sólo con la carta en
  el aire.
· **El reloj control de asistencia ES el Fin de Guardia** (idea del autor):
  fichas la salida. Se lleva la ronda encima —que es lo que marca un reloj
  de turno— y saca el botón de la esquina donde convivía con el mazo, que
  era donde más fácil se tocaba sin querer. Mismo cromado que la Pizarra.
  La banda entera queda en 59 px, menos que los 77 de la Pizarra sola.
· **La carta lleva filete blanco**, proporcional al ancho de cada vista
  (≈2,8 %): el arte ya no sangra al filo, sangra al filete.

· **Los tirones al hojear eran las variables CSS.** `ponRanB` escribía
  `--x/--y/--a/--s/--z` en cada ranura por fotograma, y cambiar una custom
  property invalida el estilo de **todo el subárbol** del elemento: ocho
  cartas enteras recalculadas 60 veces por segundo. Ahora escribe el
  `transform` inline directo (con `translate3d`, que lo manda al
  compositor), toca `zIndex` y las clases `foco`/`lejos` sólo cuando
  cambian de valor, y mientras dura el gesto el arco lleva `will-change` y
  sombras baratas. Medido con la CPU a ¼ de velocidad, que es lo que se
  parece a un teléfono: el p90 del fotograma baja de **33,4 a 16,8 ms** y
  los fotogramas lentos de **32/102 a 3/90**. Cambiar de carta con un toque
  tampoco redibuja ya la app entera: recoloca con `abanicoVivoSnap`.
· **El parpadeo doble al detenerte** eran dos bichos distintos, medidos
  contando eventos `animationstart` en las ranuras. Uno: la animación de
  entrada colgaba de `.ran-b` a secas, así que al soltar el hojeo se
  relanzaba dos veces —una al quitar `.vivo`, que devolvía el
  `animation-name`, y otra al redibujar—. Ahora cuelga de `.abre`, que solo
  se pone al abrir la mano y se quita en el `animationend`: con keyframes
  implícitos (solo hay `from`), dejar la clase puesta hace que cambiar el
  transform por debajo reconstruya el modelo y Chrome relance la animación.
  Dos: **el temporizador de la lupa se disparaba después de hojear** — la
  pulsación larga son 480 ms y un deslizamiento tranquilo dura más, así que
  al soltar se abría sola la carta grande; la guardia miraba `hojeo.movio`,
  que para entonces `hojearFin` ya había puesto en false. Ahora el
  temporizador se cancela en cuanto hay movimiento. Medido: de 16 relanzos
  al soltar a 0, y la pulsación larga quieta sigue abriendo el zoom.
· **La mano se queda abierta después de jugar.** Plegarla obligaba a
  reabrirla para la segunda colocación del turno, que son tres por ronda.
  Ahora sólo la cierra tocar fuera: el velo pasó de cubrir el 34 % de abajo
  a cubrir la pantalla entera (`position:fixed;inset:0`, con el degradado
  sólo en la franja de abajo), y las camas suben a `z-index:44` para
  quedarse por encima y seguir recibiendo el toque. El velo tuvo que salir
  de `.pie`: `.pie` es un contexto de apilamiento (fixed + z-index), así
  que nada dentro de él puede quedar por debajo de las camas.
· **El arco del abanico va centrado en la pantalla, no en el foco.** Se
  centraba en la carta enfocada, así que con el foco en un extremo la mano
  entera se corría hacia un lado y las últimas cartas se salían (medido:
  hasta `right: 460` en una pantalla de 390). Como la mano nunca pasa de
  ocho y entera cabe, ahora el arco es fijo y lo que se mueve es el
  levante: la del foco sube y crece en su sitio, las vecinas se apartan.
· **Ajustes de talla en B** (a pedido del autor): la ranura de camas sube
  de 118 a 132 px y los puntos de requerimiento de 7,5 a 9,5 —son lo que
  más se mira de la cama y a 7,5 se contaban mal—; el retrato propio pasa
  de 82 a 94 px y se despega 10 px del filo, y el del rival crece a 54 con
  la repisa igual de separada de su borde, para que las dos sigan siendo la
  misma pieza vista al revés. La ranura crece en las dos mitades a la vez,
  así que el aire se reparte solo (158/158) y el espejo sigue cuadrando.
· **La forma del arco no depende del foco.** Al agrandar las cartas salió
  el mismo error dos veces: la caída y el giro se calculaban desde la
  distancia al foco, así que con el foco en un extremo la última carta
  bajaba 42 px y se salía por abajo (antes ya había pasado en horizontal).
  Ahora la posición, la caída y el giro salen del sitio de la carta en la
  mano —arco fijo— y el foco solo levanta, agranda y abre hueco.
· **Los Protocolos guardados** llevaban el rótulo escondido: la regla que
  ocultaba la línea de datos de la zona (`.zona.cerca .jugador-linea`) se
  llevaba por delante el «Tus Protocolos», que usa la misma clase, y la
  rejilla quedaba pegada al filo de la última cama. Con el rótulo de vuelta
  hay 12 px de aire, y la tarjeta se aprieta (texto a dos líneas, bloque a
  94 px con scroll) porque entera se metía debajo del avatar.
· **El reloj control, corregido:** la pantalla lleva SOLO la ronda sobre el
  negro y el lector de huella salió de ella a su propio rebaje en la chapa
  —biselado con sombras interiores— porque en el aparato de verdad el
  lector no es parte del visor. La huella se enciende en turquesa cuando
  puedes fichar y queda gris cuando no.
· **El ambiente de la UCI, vectorizado** (`tools/generar_ambiente_app.py`,
  cuatro data-URI SVG de ~2 KB entre las marcas `__AMBIENTE_*__`). El
  tablero se lee **en planta**, que es lo que ya hacía la camilla de la
  cama vacía: **mesón de enfermería** en los dos bordes exteriores —un
  mostrador curvo con monitor, teclado, taza, carpetas y teléfono; el
  retrato queda dentro de su curva, como quien está de pie en el control—
  y el **suelo de la unidad** en las franjas de aire, con la barra de gases
  del cabecero y el riel de la cortina pegados a la fila de camas y, hacia
  el mesón, camilla parada, portasueros, carro de ropa y dispensador.
  Dos decisiones que costaron una pasada: el suelo **no** lleva baldosas
  —el fondo de `.app` ya trae su rejilla de barril y dos rejillas
  superpuestas eran ruido— y en B se retira la sala fotográfica de detrás
  de la fila de camas (`--sala-mia`), porque mezclar foto lavada con línea
  vectorial se notaba. Ojo con la especificidad al retirarla:
  `.zona.cerca .tres` son tres clases y `body[data-maq="b"] .tres` solo
  gana con `.zona` de por medio. En su lugar va la tercera banda: **las tres
  plazas**, con la cabecera hacia afuera —las dos unidades se miran de pies
  a través de la Pizarra— y dibujadas para que la plaza VACÍA se lea como
  una cama hecha esperando paciente, que es lo único que se ve cuando la
  carta no está.
· **Los prompts para llevarlo a ilustración** están en
  `docs/PROMPTS-TABLERO.md`: tres, uno por banda, con las posiciones en
  porcentaje leídas del propio generador para que el dibujo caiga donde ya
  cae el vector. Una generación por banda: la del rival es la misma girada.
· **Y las ilustraciones ya están puestas** (`cartas/tablero/{meson,camas,
  suelo}.png`). `generar_ambiente_app.py` las prefiere al vector cuando
  existen, banda por banda, y hace cuatro cosas con cada una: recorta a la
  proporción exacta de su franja —así se pinta con `100% 100%` sin
  deformar—, lava un 62 % hacia el papel (más que la sala, porque estas
  llevan cartas encima todo el rato), **alinea el piso** y sale a WebP.
  Tres cosas que hubo que arreglar y conviene no repetir:
  · **el generador de imágenes puso las camas en 16/50/83 %** y las columnas
    de la app caen en 20,3/50/79,7. En vez de pedirlo otra vez, el script
    recorta la plaza del centro y la pega tres veces en su sitio.
  · **las tres ilustraciones traían tonos de fondo distintos** y, una debajo
    de otra, se leían como tres paneles y no como una sala. `alinear()`
    muestrea la esquina —que en las tres es piso— y desplaza la imagen
    entera hasta que ese piso es exactamente `--mesa`. El contraste interno
    no se toca.
  · el suelo venía con **marco de pared** por los cuatro lados; se recorta,
    porque una pared entre las camas y el piso no tiene dónde ir.
  Los rótulos llevan halo de papel: el dibujo pasa por detrás y el texto
  tiene que ganar caiga donde caiga del mostrador.
· **El alta y el Sumario ahora se ven.** La moneda dorada ya encontraba su
  ancla solo en la maqueta A (buscaba `.zona.lejos .marca.al`, que en B no
  existe): ahora el número de altas del rótulo de cada unidad lleva
  `.marca.al` y el selector cubre las dos maquetas más el chip del rival.
  El golpe pasó de un `scale(1.12)` de medio segundo a un `popAlta` que
  crece al doble con destello dorado — ojo, hay que declarar
  `display:inline-block`, que un `transform` sobre un elemento inline se
  descarta en silencio. Y el **alta celestial ya no sube el contador de
  Sumarios en silencio al otro extremo**: el 📋 vuela desde la ceremonia
  hasta tu contador y lo golpea, que es lo que hace ver de dónde salió el
  castigo.
· **Pendiente relacionado:** el generador limita el arte a **520 px de
  ancho** (`generar_app.py`), medida heredada de cuando el arte era 9:16.
  El hueco más grande —la carta en zoom— pide 342 CSS px, que a 3× son
  1026: con 520 se ve blando. Lo correcto cuando llegue la tanda nueva son
  **dos tamaños**: uno chico (≈380 px) para la mano y las camas, y uno
  grande (≈900) sólo para el zoom. Subir el único tamaño a 900 a secas
  encarece el peso de la app y el coste de decodificar ocho cartas en el
  abanico — que es justo lo que acabamos de arreglar.

**Cómo debe venir el arte** está medido y escrito en `docs/ARTE-CARTA.md`.
El titular: el arte de hoy es **9:16 vertical** y los huecos son
horizontales — por eso los personajes salen pegados a la cámara. La tanda
nueva va en **4:3, 1600×1200**, con la cara en los dos tercios de arriba
(el tercio de abajo se funde en el papel de la carta) y, en los avatares, la
cabeza dentro del 75 % central del ancho, que es lo que deja pasar el
recorte circular del retrato.

**La carta va en maquetación B** desde v0.54: el arte entra a sangre por
arriba y se **disuelve** en la ficha —no se corta, que una línea dura
partiría la carta en dos—, y el nombre y los datos viven sobre papel. Está
en las tres vistas: la cama, la mano y la carta grande. Detrás del arte va
el **tinte de la propia ilustración**, la mediana de su borde, que calcula
`generar_app.py` al cargarla; sirve para que los costados no se vean
cuando la imagen no llena el hueco.

Los **requerimientos son fichas redondas del color de su tipo**, no
casilleros. Es la gramática del coste de energía de Pokémon —fichas,
nombre, número— y se lee sin leer: cuentas los puntos de color de un
vistazo. Es el cambio que más se nota a 132 px.

**El avatar se agranda y se gira.** La habilidad va al FRENTE: al empezar
se elige entre tres avatares, y con la habilidad al reverso habría que
girar tres cartas para comparar, además de que en papel la carta queda a la
vista toda la partida. Al reverso va la ilustración completa sin una
palabra, con el lustre — full art como premio y no como problema. Se abre
tocando el nombre en la tira; la ⓘ sigue siendo el vistazo rápido.

**Cuánto de la escena se ve.** El hueco del arte es más ancho que alto, y
con arte 9:16 solo entra la mitad del alto de la ilustración: por eso los
personajes salen pegados a la cámara. Medido: 9:16 → 50 %, 3:4 → 67 %,
1:1 → 89 %, 4:3 → 100 %. **El arreglo no es CSS, es la forma del archivo**;
hay que generar en 1:1. Mientras tanto, las cartas con regla llevan la
imagen metida al 78 % del ancho (`aire`), que sube el 50 % a un 64 %.

Falta reescribir los 115 prompts con la forma 1:1, plano medio y el tinte
fijado al color del sistema.

**La pantalla de inicio también está dibujada** (v0.58). La escena A de
`PROMPTS-PORTADA.md` —la calma antes del turno— vectorizada en
`tools/generar_portada_vector.py`: el auxiliar de aseo trapeando de
espaldas, con su audífono de orejera, el carro amarillo con la radio
sonando, el cono de piso mojado y las tres salas de vidrio con las camas
hechas. Sale a `arte/portada/dibujo.svg` (la app lo prefiere al clip; se
borra el archivo y vuelve el video, el código sigue entero) y a
`docs/portada-vector.svg` para mandarlo a editar.

Para que la escena y el menú convivan, el inicio pasó a ser una **columna
de alto completo**: logotipo arriba, un `aire-inicio` flexible en medio
—que es donde se luce el dibujo— y el menú apoyado en el filo de abajo.
Antes el menú arrancaba a `8vh` fijos y en pantalla corta le caía encima al
auxiliar. Se fueron el subtítulo «Guardia virtual · reglas», la nota de las
tres fases y las Acciones, y el pie del «árbitro digital» —ninguno le habla
a quien va a jugar—, y el velo dejó de borrar el piso (llegaba a 0,97 de
blanco): los botones son vidrio esmerilado sobre el suelo recién trapeado.

**Y el menú son tres pastillas** (el autor eligió la variante B del
mockup: bajas, con el nombre completo y la pista a la derecha, en vez de las
fichas cuadradas). Las modalidades son tres, no cuatro: la
Primera guardia **no es una modalidad**, es la partida contra la IA con el
coach encendido —en el código, la misma llamada con una bandera de más—.
Así que baja a una **casilla** bajo las pastillas: la marcas y «Contra la IA»
arranca con la guía; quien ya jugó no vuelve a leerla nunca. Con el menú
compacto la escena pudo bajar 66 px enteros y el logotipo quedó solo contra
el cielo raso, que además se despejó: las luminarias se fueron y el reloj se
mudó del techo al muro, junto al letrero de UCI.

**La pantalla de inicio tiene fondo vivo** (v0.52): el clip del auxiliar
de aseo trapeando el pasillo, en bucle y con la unidad sonando. Sale de
`arte/portada/` y se rehace con `tools/generar_portada_video.py clip.mp4`,
que le pega su propio reverso —el clip de Flow no cierra el ciclo y en
`loop` se veía el corte—, le sintetiza la banda de sonido y saca el cuadro
fijo de respaldo. Cinco cosas aprendidas montándolo:

· El `<video>` NO puede vivir dentro de `#app`: `render()` hace
  `innerHTML = ""` y el video volvería a empezar en cada repintado. Va
  fuera, y `pintarPortada()` lo deja quieto si ya está puesto.
· Un `<video>` NO puede colgar de un `data:` URI — el navegador no lo
  puede pedir por tramos y se queda en 0x0. En el artefacto hay que pasar
  el data-URI por `fetch` → `blob:` antes de dárselo.
· `position:fixed` crea contexto de apilado en Chrome, así que el botón de
  sonido no podía subir sobre `.app` desde dentro de `#portada`: se
  dibujaba pero era intocable. Cuelga de `<body>`.
· El navegador no deja arrancar con sonido sin que alguien toque algo. El
  video parte mudo por obligación y el audio es un botón, que recuerda la
  elección.
· Al empezar la partida NO basta con vaciar `#portada`: el contenedor es
  fijo y opaco, y `.app` no está posicionada, así que el piso de la unidad
  y las camas se pintan por DEBAJO y quedaban tapadas por el cuadro fijo
  del pasillo. Hay que esconderlo entero (`hidden`) y limpiar también el
  `background-image` en línea.
· El Chromium de Playwright NO trae H.264 ni AAC (`canPlayType` → "NO", y
  el video da `error 4`). Para probar la integración hay que armar una
  copia en VP9/Opus; el mp4 está bien, el que no puede es el navegador de
  pruebas.

**El logotipo** manda en la portada desde v0.53: reemplaza al título
tipográfico, aunque el `<h1>` se queda (el nombre sigue siendo el
encabezado para quien no ve la imagen). El maestro sin recortar está en
`arte/portada/logo-crudo.webp` y `tools/recortar_logo.py` lo deja sobre
transparencia. Dos cosas de ese recorte que no son obvias: el fondo NO se
quita con un «todo lo blanco a transparente», porque el logo tiene brillos
blancos DENTRO de las letras y ese método los perfora — se rellena desde
los bordes; y además hay que sacar los bolsones de blanco ENCERRADOS entre
el tubo del monitor y las letras, que no tocan ningún borde y quedaban
como manchas flotando sobre el video (se separan por área: un brillo
pintado es un trazo fino, un hueco de fondo es una mancha ancha).

Nada de GIF: medido, el mismo bucle en GIF a 360 px y 12 fps pesa 15 MB
contra 2 MB del mp4 a 720 px, 24 fps y con sonido.

**El sello de la caché cuenta también los íconos** por su contenido, no
por su nombre. Están en el núcleo del service worker, así que cambiar el
dibujo sin mover el sello dejaba a los teléfonos ya instalados con el
ícono viejo para siempre — no hay nada que los invalide. Comprobado: el
sello se mueve al cambiar el dibujo y vuelve al mismo valor al revertirlo.

**La app instalable (PWA)** sale de la misma plantilla con
`python3 tools/generar_app.py --pwa` → `docs/juego/`. Se instala en el
teléfono con su ícono, abre a pantalla completa y **funciona sin
internet** (service worker + tipografías alojadas en casa; nada le pide
nada a Google). Es el paso previo a las tiendas: el mismo código se
envuelve después con Capacitor.

> ⚠️ `docs/juego/` es la única salida generada que **sí se versiona**:
> GitHub Pages sirve archivos, no ejecuta scripts. Después de tocar la
> plantilla o los CSV hay que **recompilar y comprometer** esa carpeta, o
> la app publicada se queda atrás. Los dos formatos van juntos:
> `generar_app.py` (artefacto) y `generar_app.py --pwa` (app).

**Para publicarla** (una sola vez, en GitHub → Settings → Pages): fuente
*Deploy from a branch*, rama `claude/medical-card-game-o9synq` (o `main`
cuando se fusione), carpeta **`/docs`**. Queda en
`https://diegonicolasmelo-cell.github.io/VAYA-TURNO/` (portada) y
`.../VAYA-TURNO/juego/` (el juego). Ojo: **la instalación exige HTTPS** —
Pages lo da; abrir el archivo local no basta.

**Batería de jugabilidad (agosto 2026, 4.000 partidas 2j + 3.000 partidas
3j, IA de referencia):** el flujo está sano — las 3 indicaciones se usan
completas el 100% de los turnos y la "mano seca" (querer jugar y no poder)
es 0,1%: no existen los turnos muertos. El circuito de sabotaje funciona
como tempo puro: 1,4 ataques por guardia y 1,3 limpiezas — casi todo golpe
se paga con una des-escalada. Sumarios: 81% se cierran. Tres cosas para
vigilar en mesa: (1) **el descarte del cierre muerde el 58% de los turnos**
(era 69% con mano 5, y en la v0.21 un 17%) — robas 4 y colocas 3, así que
seguido botas 1; es una decisión de calidad de mano, pero también un paso
más por turno; (2) **nadie muere antes de la ronda 4** y el pico de muertes es la ronda 7 —
el arco dramático es de guardia real (la noche se pone fea tarde), pero las
3 primeras rondas son sin consecuencias; (3) el mazo se rebaraja exactamente
1 vez por partida, a la mitad — la densidad de ⚠️ se mantiene pareja.

**El descarte del 69% ya se atacó — límite de mano 6** (v0.33, DISENO §4l).
Robo 3 colapsaba el juego (salv 57%, el mazo nunca rebaraja) y quedó
descartado; **robo 4 · mano 6** baja el descarte a 58% y mejora todo lo
demás medio punto, idéntico a 2 y 3 jugadores. ✅ Aplicado en
REGLAMENTO-v030 §4.3, la app y `simular_v030.py`. 🔶 En mesa: confirmar que
sostener 6 cartas no estorba físicamente y que la mano guardada se usa para
planificar (juntar el cierre de Sumario, esperar la ⚠️) y no para acaparar.

**Las Acciones ya se ejecutan en la app** (v0.35, DISENO §4m): las 22
tienen efecto real con selección de objetivo, verificadas una por una.
Estado de las brechas:
- ✅ **La IA ya compra y juega Protocolos** (v0.36, DISENO §4n). Medido:
  el juego se endurece pero queda en banda (salv 68→64%, GIII 47→42%),
  usarla paga +1,24 netos con 55% de victorias, y **el descarte cae del
  58% al 20%** — la Pizarra es el otro destino del excedente. Comprar de
  más es un error medible: la IA exige 2 cartas de sobra antes de comprar.
- 🔶 **Cuatro Acciones que la IA nunca juega**: A07 ¡Liceeeencia! y A12
  Protocolo Institucional (fuera del modelo del simulador), A10 Rotación
  de Internos y A22 Alta Anticipada (condiciones muy estrechas). Mirar en
  mesa si A10 y A22 piden demasiado.
- 🔶 **Las RESPUESTA (A11, A16) son anulación, no interrupción**: revierten
  la última complicación de la ronda sobre un paciente tuyo. Equivalente en
  efecto, pero se juegan en tu turno y no "fuera de turno". Ver si en mesa
  la diferencia se nota.

⬜ **Valor propio de los recursos — medido, decisión pendiente** (DISENO
§4o). Que el TAC valga 2 a cualquiera es un +6pp de salvamento que **la
escasez no alcanza a pagar** (partir copias recupera solo 2pp): el cuello
son las indicaciones, no las cartas. Lo que sí lo paga es exigir 🧑‍⚕️
Personal ya puesto en esa cama (66%, en banda, y clínicamente cierto).
Si se adopta: cartas simples con etiqueta de sistema, cartas complejas con
valor 2 fijo y requisito de Personal, **sin acumular ambas**, y el
requisito solo sobre las **10 no-Personal** (Cirujano y Kinesiólogo se
autobloquearían). Medido: el Personal **no escasea**, se vuelve una llave
— añadir copias casi no alivia porque la traba es de secuencia, no de
oferta. Vigilar en mesa la sensación de "tengo el TAC y no puedo jugarlo"
(1,85 bloqueos por turno).

✅ **¿Sacar los pacientes NEURO? Medido: no hace falta** (agosto 2026).
La sospecha del autor era correcta en los datos —NEURO pide 8💊 vs 5🩻 y es
el único sistema con CERO fármacos de sinergia (el Anticonvulsivante se fue
en la cirugía v1.0 y nadie ocupó el hueco)— pero no se traduce en
desbalance: NEURO salva al 68%, el promedio exacto del juego (METAB 73 ·
CARD 72 · NEURO 68 · QUIR 66 · RESP 59). La etiqueta ×2 es acelerador, no
requisito. Se dejó tal cual. 🔶 Dos cosas para la mesa: si NEURO se siente
plano (nunca ×2 en fármacos), el arreglo barato es re-etiquetar UNA carta
—Sedoanalgesia calza clínicamente con el Status— antes que sacar pacientes;
y vigilar RESP (59%), que carga hacia lo grave.

✅ **Tier list de avatares medido Y rebalanceado** (DISENO §4p y §4q).
La brecha de 6 puntos (−0,92…+5,03) quedó en **1,1 (+0,08…+1,22)**: los
22 avatares aportan y ninguno domina. Doctrina pedida por el autor
(Hearthstone: toda habilidad paga tempo · Battlegrounds: girar números,
no identidades · Pokémon: cada avatar un momento único), 3 iteraciones
medidas a 3.000 partidas por giro. 9 textos nuevos en personajes.csv:
Subespecialista y Doctor Amor ahora 1×PARTIDA, Esotérico 2×PARTIDA,
Diostor descarta 2, Enfermera vela UNA cama, Residente dobla al 3º de
tipos distintos, Fantasma solo paga la ronda 1, Intensivista cubre ROJO,
Buena Muñeca mira 3 y elige. 🔶 Para la mesa: la franja C (+0,08…+0,16)
sigue siendo correcta pero olvidable — es problema de sabor, no de
números, y la Buena Muñeca (+0,12) está subestimada por la heurística
del simulador.

✅ **Acciones medidas contra la banda de avatares** (DISENO §4r). La
sospecha del autor era correcta: A01 Vacaciones (+2,21) y A04
Interconsulta (+2,13) superaban al mejor avatar (+1,22), y A17 Quiebre
de Stock (+8,66) era un **bug del simulador** (el "próximo turno" duraba
toda la guardia — arreglado en ambos simuladores). Nerfs con la doctrina
§4q: A01 devuelve el 🧑‍⚕️ a la mano rival y baja a 1 copia (+0,70); A04
rescata a la mano, no coloca gratis (+0,67). El mazo de Protocolos queda
en **31 cartas** y la ventaja de usar la Pizarra baja de +1,24 a +0,31.
🔶 Para la mesa: las Acciones de coste 3 (A02, A15, A21) la IA nunca las
compra — vigilar si en mesa se pudren en la Pizarra; A07 y A12 no están
modeladas en el simulador.

⬜ **El mazo tiene ~12 cartas de holgura**: de 67 a 55 no cambia nada medible
a 2 ni a 3 jugadores. A 50 se nota en las rebarajas. El simulador no mide
la variedad que siente un humano — decidir en mesa.

**A22 Alta Anticipada** (agosto 2026): agregada al mazo de Protocolos,
coste 2, única, con la pena "el alta apurada vale 2 puntos menos" — sin
la pena era un botón de +1,2 pts que todos guardan a la última ronda
(medición completa en DISENO §4l). 🔶 vigilar en mesa si la pena se
entiende y si el momento de usarla se siente como decisión.

Qué mirar en mesa antes de decidir: (1) ¿el sabotaje se siente táctico o
sólo malicioso? (2) ¿la Pizarra hace que El Pasillo por fin se juegue?
(3) ¿"No se me fue nadie" al 2,6% se siente épico o imposible? (4) ¿la
basura girada 180° se lee bien físicamente? (5) ¿la admisión obligatoria
se extraña como decisión?

---

## 1. Cartas con efecto definido pero SIN VALIDAR (el simulador no las modela)

El simulador (`tools/simular.py`) valida la economía base: pacientes,
recursos, deterioro, Sumarios. **No modela ninguna de estas cartas.** Su
efecto está escrito y es jugable, pero nadie sabe todavía si está balanceado.
Solo el playtest lo dirá.

### 1.1 Las 20 Acciones (mazo de Protocolos) — todas 🔶

Prioridad de observación en mesa, de más a menos peligrosa:

| Prioridad | Carta | Qué vigilar |
|---|---|---|
| 🔴 1 | **A02 Cumpleaños del Residente** (×2) | Roba 1 recurso EN JUEGO a *cada* rival. En mesa de 4 son 3 recursos gratis: puede romper un ✅ ajeno por lado. Candidata a nerf (→ "a UN rival"). |
| 🔴 2 | **A10 Rotación de Internos** (×1) | Intercambio de mano completo. El swing más grande del juego. ¿Se siente injusto o glorioso? |
| 🔴 3 | **A13 Anda Rondando la Pelada** (×1) | Única. Mata un paciente ✅ con 2 caras de moneda. Es EL momento del juego — pero ¿aparece lo suficiente estando en un mazo de 30 al que se llega por Canje? |
| 🟡 4 | **A05 Doblo Turno** (×1) | +3 cartas ahora, −2 después. Con ⚠️ adentro puede encadenar 2–3 complicaciones de golpe. |
| 🟡 5 | **A17 Quiebre de Stock** (×1) | Bloquea un tipo de recurso un turno. Contra un jugador que necesita justo eso para estabilizar, es un ❤️ de daño indirecto. |
| 🟡 6 | **A18 Recorte Presupuestario** (×1) | −2 robo un turno. En 4 jugadores (robo 3) deja al rival con 1 carta: ¿demasiado duro? |
| 🟢 7 | A01 Vacaciones, A07 ¡Liceeeencia!, A08 Llaman de Urgencias, A09 Auditoría, A20 Hay Que Repetirlo | Ataques de intensidad media. Vigilar solo la frecuencia. |
| 🟢 8 | A03 Reunión Clínica, A04 Interconsulta, A14 Ojo Clínico, A15 Receta en Blanco, A19 Capacitación | Apoyos. Vigilar que el Canje (pagar 2 por 1) se sienta justo. |
| 🟢 9 | A11 ¿Y Si Vamos por un Cafecito?, A16 Simulación Clínica | Respuestas 🛡️. Vigilar si 4 copias entre 30 son suficientes para que la defensa exista. |
| 🟢 10 | A06 Se Cayó el Sistema, A12 Protocolo Institucional | Caos y copia. Ver ambigüedades en §3. |

### 1.1a La "Se hizo todo" (regla nueva, v0.15) — 🔶

+1 punto si tus únicos ✝️ fueron Gravedad III o Código Rojo (`REGLAMENTO.md`
§9). Medida: sube el disuasivo contra aparcar a los leves un 52% y salta en el
27,8% de las guardias (`DISENO.md` §4d).

**Qué vigilar en mesa:**
- ¿Se persigue o se ignora? Si nadie la menciona al contar puntos, el +1 es
  demasiado poco y habría que subirlo a +2.
- ¿Genera la conversación correcta? Lo que buscamos es el *"se me fue, pero se
  hizo todo"* — si en cambio genera discusión sobre si tal muerte "contaba",
  el corte III/ROJO está mal puesto y hay que incluir a los Gravedad II.
- ¿Confunde tenerla junto a la Limpia? No se suman: o una u otra.

### 1.1b El Trueque de Pasillo (regla nueva, v0.13) — 🔶

Incorporado como alternativa al Canje dentro del Negocio único del Pasillo
(`REGLAMENTO.md` §5.2): das 2 recursos de tu mano a un rival → te entrega 1
del tipo que pidas (él elige cuál; puede negarse).

**Qué vigilar en mesa:**
- ¿Dos jugadores se alimentan mutuamente contra el tercero? (2+1 cartas por
  ronda fluyendo entre los mismos dos). Nerf preparado: *"no puedes trocar
  con el mismo jugador dos rondas seguidas"*.
- ¿Canibaliza al Canje o conviven? Lo sano es ~1 Trueque por cada 2–3 Canjes.
- En 2 jugadores debería casi no usarse (darle 2 cartas a tu único rival
  rara vez conviene) — confirmar que efectivamente se autorregula.

### 1.2 Las habilidades de Personaje — 10 ✅ medidas · 11 🔶 de mesa · 1 al alza

> **v0.19: plantilla completa de 22 avatares** (`DISENO.md` §4h), con reparto
> 2-elige-1 y vocabulario de alcance (*este paciente* / *tu unidad*). Diez
> habilidades están medidas y en banda (+0,3 a +1,0); once usan piezas que el
> simulador no modela y se calibran en playtest. El autor las modificará tras
> el playtest — están diseñadas para sobrevivir a ese recorte, no para eludirlo.

Lo que queda por vigilar en mesa:

| Personaje | Riesgo |
|---|---|
| **El Multiuso** | ✅ medido pero **caliente (+1,09)**. Si domina: el comodín inicial empieza en juego, no en mano. |
| **El Diostor** | 🔶 Con v0.17 eligió momento: ahora decide CUÁNDO coloca la ⚠️ que endosa. Probablemente subió de poder. |
| **El Médico Fantasma** | 🔶 ¿Netea a favor? (A.F. Kay en Battlegrounds era fuerte: el pago tardío vale más que el tempo temprano). |
| **El Médico Esotérico** | 🔶 v0.19 le puso costo fijo (descarta 1 siempre). ¿Sigue siendo el más jugado? |
| **La de Abastecimiento** | 🔶 Canje a 1 recurso = economía doble. La candidata a rota de las once de mesa. |
| **El Carroñero de Pasillo** | 🔶 Roba de la mano rival: el único que castiga a un jugador ya golpeado. ¿Se siente miserable? |
| **La Gestora de Camas** | ✅ v0.13 (+0,7). Sin cambios. |

### 1.3 Las 18 complicaciones ⚠️ — ✅ medidas, 🔶 sin mesa

> **v0.21: las dieciocho hacen lo mismo — el 🎯 pierde 1 ❤️** (`DISENO.md`
> §4j). Se acabó el 27% de complicaciones nulas; queda **1,0%**, que son las
> protecciones 🛡️ funcionando. Lo nuevo a vigilar en mesa:
> - **¿Se sienten repetidas?** La apuesta es que no: el nombre, el dibujo y
>   el 🎯 llevan la variedad, como en Pokémon todos los ataques son daño. Si
>   en mesa se sienten intercambiables, la apuesta falló y hay que devolver
>   variedad — pero por el lado de los Protocolos, no de las ⚠️.
> - **¿El Gravedad III re-tasado (6 ❤️ · pide 8 · +6) se siente alcanzable?**
>   Mide 40% de salvamento, el piso de la banda.
> - Los textos quedaron **más cortos**: una línea de efecto y el chiste.
>   Comprobar que ahora sí se leen rápido.

> **v0.17: se disparan al COLOCAR la carta, no al robarla** (`DISENO.md` §4f).
> Lo nuevo a vigilar: (a) la línea *cobarde* — el que evita jugar ⚠️ egresa
> menos pero protege su bonus de cierre; (b) si un humano cronometra sus ⚠️
> para que el 🎯 falle, el 43% de Gravedad III medido se queda corto;
> (c) si el Trueque muere porque nadie quiere recibir cartas malditas.

> **v0.14: se eliminó el Mazo de Eventos Centinela.** Cada ⚠️ trae impresa la
> complicación que ese recurso causa de verdad (`REGLAMENTO.md` §7). El
> simulador ya no las estima con una abstracción: **aplica las 18 exactas**,
> así que por primera vez el número de balance incluye los eventos de verdad.
> Calibración completa en `DISENO.md` §4c.
>
> Lo que queda por ver en mesa:
> - ¿Se lee rápido? Las ⚠️ son ahora las cartas más cargadas del juego
>   (nombre + tipo + chip + 🎯 + párrafo). Si frenan el robo, hay que acortar
>   los textos.
> - ¿Se echa de menos el teatro de voltear una carta del mazo maldito?
> - Diez de dieciocho apuntan al que iba bien y cuatro (🎯 ESTE) al que
>   acabas de tratar. ¿Se siente cruel-divertido o cruel-injusto? Las ESTE
>   son autoinfligidas y predecibles: ¿le quitan sorpresa al mazo, o la
>   anticipación ("sé lo que me puede pasar si conecto esto") compensa?
> - Con 🎯 ESTE, el jugador decide en qué paciente estalla la complicación
>   eligiendo dónde coloca la carta. ¿Aparece el "paciente pararrayos"
>   (uno ya perdido que recibe todos los ⚠️)? El costo real es que el
>   recurso queda gastado en él — medir en mesa si alcanza como freno.
> - 🎯 EL MÁS TRATADO quedó **sin cartas** (la NAVM pasó a ESTE). El
>   vocabulario sigue implementado en ambos simuladores por si una carta
>   futura lo usa; si en v1.0 sigue huérfano, quitarlo del REGLAMENTO.
> - Las 4 huérfanas (*Corte de Suministro*, *Paro*, *Hemorragia Masiva*,
>   *Cambio de Turno Caótico*) esperan en `cartas/retirados/`: son candidatas
>   a Acciones de CAOS si el mazo de Protocolos pide más caos.

## 2. Mecánicas RESERVADAS sin efecto todavía (efecto pendiente literal)

Espacio dejado a propósito en las cartas, hoy sin regla que lo use:

| # | Qué | Dónde vive | Para qué está reservado |
|---|---|---|---|
| ⬜ 1 | **Chip de sistema en los recursos ⚠️** como categoría de su complicación | `recursos.csv` | Inmunidades de avatares futuros (el Broncopulmonar ignora las complicaciones de recursos 🫁…). Al eliminarse el mazo Centinela en v0.14, la categoría clínica del evento desapareció; su sustituto natural es el sistema del recurso que la causa. |
| ⬜ 2 | **Chip de sistema en pacientes** más allá de la sinergia | `pacientes.csv` | Las expansiones por sistema (`EXPANSIONES.md` §1). |
| ⬜ 3 | **Columna `set`** en los CSV | No existe todavía | Filtrar base vs. expansión en Taller, PnP y simulador. `EXPANSIONES.md` §5. |
| ⬜ 4 | **Frecuencias de avatar** como sistema (1×turno / 1×ronda / 1×partida / pasiva) | `personajes.csv` | Hoy cada avatar la usa; falta decidir si las expansiones respetan el mismo menú de frecuencias. |

---

## 2b. Hallazgos del inventario de mecánicas (v0.20 · `MECANICAS.md`)

| # | Hallazgo | Medición |
|---|---|---|
| ✅ 1 | ~~El 27,3% de las ⚠️ no hace nada~~ — **cerrado en v0.21**: las 18 unificadas a −1 ❤️, teatro residual **1,0%**. Costó re-tasar el Gravedad III (`DISENO.md` §4j). | 4.000 → 5.000 partidas |
| 🚨 2 | **El Trueque nunca se ha usado.** El simulador no lo modela y en dos partidas físicas el autor saltó El Pasillo completo. | mesa |
| 🔶 3 | **Las protecciones 🛡️ previenen ~6% de su complicación** (1,0% del total; eran 1,2% en v0.20). Piso, porque la IA no secuencia — pero siguen siendo 3 cartas para 3 de 18: se puede jugar una partida sin verlas actuar. | 4.000 partidas |
| 🔶 4 | **El Sumario dura 1,00 rondas y se paga el 100% de las veces.** No es maldición, es factura: su efecto real es "descarta 2 cartas". Cuesta 4 reglas y un tipo de carta. | 10.731 sumarios |
| ✅ 5 | ~~No hay mecánica de información~~ — **v0.21: Informe de Gestión de Camas** (el próximo paciente boca arriba). Medido: no cambia el resultado con una IA de política fija; su valor es humano, por confirmar en mesa. | 5.000 partidas |

---

## 3. Ambigüedades de reglas por cerrar (candidatas a la FAQ §5.5)

Decisiones que la mesa va a preguntar y el reglamento aún no responde:

| # | Pregunta | Propuesta por defecto (a validar) |
|---|---|---|
| ⬜ 1 | **A12 Protocolo Institucional** — ¿puede copiar la Pelada (A13, ÚNICA)? ¿Y una 🛡️? | No a ambas: solo copia Acciones de tipo ATAQUE/APOYO/CAOS. Escribirlo en la carta. |
| ⬜ 2 | **A17 Quiebre de Stock** — ¿bloquea un 🃏 Comodín declarado como ese tipo? | Sí: el comodín *se convierte* en el tipo al jugarse, y ese tipo está bloqueado. |
| ⬜ 3 | **TAC de Urgencia** ya jugado — si el paciente pierde su único 🧑‍⚕️ (Vacaciones, Doctor Amor), ¿el TAC se queda? | Se queda: la restricción se paga al jugarlo, no es un estado. Confirmar y añadir a §5.5. |
| ⬜ 4 | **Doblo Turno** en 4 jugadores (robo 3): ¿robas 3+3=6 y luego 1? | El texto dice "3 adicionales / robas solo 2": en robo 3 sería 6 ahora, 1 después. Confirmar que la mano de 5 lo soporta. |
| ⬜ 5 | Una complicación 🎯 **EL ✅ ESTABILIZADO** sobre un paciente que iba a salir de alta este turno | El alta ocurre en tu Entrega, antes de que nadie más robe: solo puede pegarte entre medio. Confirmar timing en mesa. |
| ⬜ 6 | **Modo Pelada Letal** + A16 Simulación Clínica: ¿puedes anular la victoria instantánea? | Sí: la Pelada es una Acción y ¿Cafecito? (A11) la anula. Anotarlo en Variantes. |

---

## 4. Ideas rescatadas ESTACIONADAS (no tocar hasta después del playtest)

| # | Idea | Origen | Dónde quedó documentada |
|---|---|---|---|
| ⬜ 1 | **Novatos y Veteranos** (seniority en Personal: el Kine Vieja Escuela inmune a Vacaciones/Licencias; copias según experiencia) | `CARTAAAS.xlsx` | `EXPANSIONES.md` §6 — Módulo Experiencia |
| ⬜ 2 | **La Enfermera Influencer** y el resto del personal con nombre | Material Gemini / Excel | `SINTESIS.md` — expansión *"Personal con Apellido"* |
| ⬜ 3 | **Interconsulta forzada** (transferir un paciente problemático al tablero rival) | Material Gemini | Sin documentar como carta. Candidata a Acción de expansión: es el ataque más temático que existe. |
| ⬜ 4 | **Rareza en 4 niveles** para todo el mazo | Material Gemini / Excel | Descartada para la base (el balance usa copias exactas, no rareza). Podría volver solo como lenguaje de expansiones. |
| ⬜ 5 | **Eliminación de jugador** por acumular decesos | Material Gemini | Descartada en v0.12 (nadie queda fuera mirando 40 min). Rescatable como variante dura tipo "Modo Cruel". |
| ⬜ 6 | **Tablero doble capa con hendiduras** para dados/fichas | Material Gemini | Decisión de producción, no de reglas. Para la versión deluxe, si algún día existe. |
| ✅ 8 | **Personal protector (pasivas de prevención)** — IMPLEMENTADO en v0.20 (`REGLAMENTO.md` §7.3): TENS→NAVM (30° y aseo de cavidades), Enfermera→Bacteriemia (manejo estéril), Kine→Delirium (movilización precoz, la E del bundle ABCDEF) — reasignados en v0.20.1 por precisión clínica; prospectivas, en las copias sin ⚠️. En simulación previenen 1,1% de complicaciones (piso: la IA no secuencia). Vigilar en mesa si el jugador siente que la secuencia protector-primero vale la pena. Resto de la fila, histórico: — el recurso 🧑‍⚕️ protege al paciente donde está de UNA complicación con nombre: Kinesiólogo / *movilización precoz* → previene la debilidad adquirida en UCI; TENS / *posicionamiento y aseo de cavidades* → previene la NAVM; Enfermera / *omnipresencia* → previene la autoextubación. Unas cartas dañan, otras blindan: cada rol se reconoce en lo que hace bien. | Idea del autor (2026-08-20) | **Regla de tiempo ya decidida (2026-08-21): la prevención es solo prospectiva.** El protector debe estar sobre el paciente ANTES de que la complicación se resuelva; entonces "no ocurre" (misma jurisprudencia del §7: no se sustituye ni se busca otro objetivo). Jugarlo después no revierte nada — la complicación ya resuelta es historia, coherente con el disparo instantáneo de v0.17. Contrajuego emergente: robar al protector (*Vacaciones*) pasa a ser desmantelar un blindaje. Falta definir el resto — depende de qué complicaciones existan tras el playtest. Encaja en la columna `texto` de `recursos.csv` (§5b) y gana sentido con 🎯 ESTE PACIENTE: proteger ANTES de instalar el ⚠️ es una secuencia clínica real (§4g de `DISENO.md`). |
| ⬜ 9 | **La Virgen Negra de Fátima** — la estampita que alarga la vida del paciente. Idea del autor (2026-08-29): en el hospital chileno la estampita pegada al velador es folclore de verdad, y el chiste es que en un juego de recursos clínicos la carta que evita la muerte no sea un fármaco. Forma candidata: **Protocolo de tipo RESPUESTA**, se juega sobre un paciente propio y **la primera vez que llegaría a 0 ❤️ se queda en 1** en lugar de morir; se descarta al usarse. Una copia, o dos como mucho: es un indulto, no una estrategia. | Idea del autor (2026-08-29) | Sin documentar como carta todavía. **Antes de escribirla hay que decidir dos cosas:** si el indulto también aplica a la muerte por basura clínica —la regla nueva de la v0.57— y si consume indicación. Y **no entra al balance validado**: `simular.py` no modela Acciones, así que una carta que evita muertes toca justo la métrica que el simulador sí mide (61 % de salvamento, 8 % de guardias limpias). Habría que medirla en mesa antes de darla por buena. |
| ❌ 7 | **Rescatar del descarte como regla libre** | Propuesta del autor (2026-08-18) | **Evaluada por simulación y descartada como regla base.** 2.000 partidas por variante (3 jug., config estándar): rescate 1:1 sube el salvamento de 61%→65% y **duplica las Guardias Limpias (8%→14%)** — mata la hazaña; rescate 2:1 resulta una trampa (la IA que lo usa siempre cae a 46% de salvamento: pagar 2 por 1 desangra la mano). El acceso al descarte queda como **efecto de carta** (*A04 Interconsulta* ya lo hace) y candidato a 1–2 cartas más en expansiones. La variante 1:1 podría rescatarse como "modo suave" para mesas nuevas. |

---

## 5. Arte — 18 de 124 colocadas, estilo canónico definido 🔶

Las imágenes aparecieron: estaban en el **Drive del autor** (carpeta "cartas
vaya turno", 452 archivos). Las 39 finales + mejores escenas ya viven en
`arte/` mapeadas a IDs (ver `arte/README.md`), y el estilo canónico "Retro de
Guardia" quedó documentado en `ARTE.md` §2 con su bloque de prompt.

- ✅ Estilo canónico definido + anclas de imagen elegidas
- ✅ 18 cartas con ilustración en `arte/raw/` (4 avatares, 11 recursos, 1 evento, 2 acciones)
- ⬜ C02 Médico Fantasma y C04 Director (generar con anclas)
- ⬜ 26 pacientes · ⬜ 32 recursos restantes · ⬜ 27 eventos · ⬜ 18 acciones · ⬜ 1 sumario
- ⬜ Curar las ~180 escenas del Drive (candidatas a eventos/acciones ya dibujadas)
- ⬜ Normalizar lote y enganchar `generar_pnp.py --arte`

---

## 5c. El arte que entra por Drive (v0.58) 🔶

La carpeta **«Vaya turno Claude»** del Drive del autor es ahora el buzón del
arte. Diego deja ahí los archivos con el nombre del personaje o de la carta
—«Enfermera de noche.jpg»— y `tools/ingresar_arte.py` los mete al juego con
el nombre que la app necesita, que es el **id**.

El guion hace dos copias: el original tal cual en `cartas/arte-full/<ID>.jpg`
y la versión de juego en `cartas/arte/<ID>.jpg`, recortada al **4:3 exacto y
1600×1200**. Con `--alto` se corre la ventana del recorte cuando la fuente
no es 4:3 y hay que salvar la cabeza del personaje.

**Primera tanda: 17 imágenes.** Dieciséis vinieron 2400×1792 —que es 4:3 con
0,45 % de sobra, o sea diez píxeles de ancho de recorte y nada más— y una,
«Becado», llegó todavía en la vertical vieja 1536×2752: conserva el 42 % con
`--alto 0.20`, alcanza para la cabeza y los libros, pero conviene rehacerla.

Ids colocados: **C03 C05 C07 C09 C11 C13 C17 C19 C21 C22 · A01 A11 A14 ·
R20 R26 R30 R32.** Con la herencia por nombre (abajo) quedan 29 cartas
ilustradas de 124.

### Dos cosas que este lote dejó abiertas

- **Dos mapeos son míos, no de Diego.** «Bodega» (mujer con tabla en una
  bodega de insumos) la puse en **C09 La de Abastecimiento**, cuya habilidad
  se llama literalmente BODEGA LLENA; la otra candidata era R43 Stock de
  Sala. Y «El que guarda siempre tiene» (enfermera con el casillero surtido
  mientras el resto corre) la puse en **C21 El Precavido**; la otra
  candidata era otra vez R43. Si alguna está cambiada, es mover un archivo.
- **El retrato redondo del mesón queda chico.** Estas ilustraciones son
  escenas anchas, no retratos, y el círculo de 94 px se queda con la escena
  entera: la cara de La Jefa de Unidad se lee, pero es diminuta. O el arte
  de los personajes viene más cerrado, o el mesón deja de recortar en
  círculo y muestra la escena. No es un error, es una decisión pendiente.

### Herencia por nombre (arreglado de paso)

`generar_app.py` ya no pide el archivo dos veces para una carta repetida.
R32 y R33 son las dos «Gases Arteriales» —la misma carta, dos copias en el
mazo— y antes había que dejar el mismo jpg con los dos nombres, pesándolo
dos veces en el artefacto. Ahora, si una copia tiene arte, sus gemelas del
mismo nombre lo heredan. Cubrió R21, R27, R31, R33 y R51 sin tocar nada.

---

## 5d. La Residencia · el tutorial por casos (v0.59) ✅

El coach de la «Primera guardia» se monta encima de una partida de verdad,
y una partida de verdad no enseña lo que quieres cuando quieres: puede que
en ocho rondas no te toque nunca una ⚠ que sirva para sabotear, o que el
único paciente a punto de cerrar sea del rival. Los diez pasos del coach
terminaban explicando la interfaz y no las mecánicas.

**La Residencia** es lo otro: diez unidades armadas a mano para que UNA
mecánica ocurra, ahora, y se vea ocurrir. Dos o tres jugadas cada una.

| # | Caso | Lo que enseña |
|---|---|---|
| 1 | Dar de alta | requisitos, sinergia ×2, cuándo se paga el alta |
| 2 | La complicación que conviene | la ⚠ que cierra la cama, colocar nunca mata, el ✅ congela |
| 3 | El escudo que previene | el 🛡️ de los recursos, y que el orden de dos cartas es una jugada |
| 4 | La carta que anula la ⚠ | las RESPUESTA y su ventana (la última ⚠ del turno, sobre lo tuyo) |
| 5 | Comprar en la Pizarra | pagar con cartas, guardar y jugar un Protocolo (Alta Anticipada) |
| 6 | Sabotear: el alta que no llega | la basura clínica retiene el alta y descongela el reloj |
| 7 | Sabotear: el alta celestial | el mismo golpe en 1 ❤️: mata en el cierre, y abre Sumario |
| 8 | Des-escalar | la respuesta, y lo que cuesta: una indicación por basura |
| 9 | El Sumario y el límite de mano | 📋 encoge la mano, cerrarlo cuesta 2, y el cierre te obliga a botar |
| 10 | El poder de tu personaje | dónde vive el ⚡, las tres frecuencias, y qué resuelve la app |

La casilla «Primera guardia» de la portada se fue adentro, como séptima
entrada: ahí se entiende que es el último escalón y no una cuarta
modalidad compitiendo con las tres monedas.

### Cómo está hecho

Un caso es **datos**, no código: `montar(mío, rival)` arma las camas, la
mano y la Pizarra; `pasos[]` dice qué se explica y qué hay que hacer.
Añadir un caso son treinta líneas en `CASOS` y nada más.

Tres decisiones que conviene no deshacer:

- **Las metas se leen de `G` y de `UI`, nunca del DOM.** Un `querySelector`
  se rompe en cuanto alguien renombra una clase, y entonces el paso no
  avanza nunca y el caso queda muerto sin que nadie se entere.
- **`guardar()` se salta los casos enteros.** Un caso es un banco de
  pruebas: si se guardara, pisaría la guardia de verdad que el jugador
  tenga a medias. Verificado en la prueba: la partida guardada sobrevive.
- **El rival no improvisa.** `casoRival()` cierra su guardia y devuelve el
  turno. La IA de verdad compraría en la Pizarra y te sabotearía de vuelta,
  y el guion no sobreviviría dos turnos.

### Lo que queda abierto

- **La mano abierta tapa el tablero.** Se resolvió con `cierra:true` en los
  pasos que necesitan verlo, pero el problema es general y no solo de los
  casos: cuando te quedas sin indicaciones, la mano sigue desplegada y su
  velo se come los toques. Candidato a recogerse sola.
- **No hay condición de fracaso.** Si el jugador se va por otro camino y
  deja el caso irresoluble, la burbuja sigue pidiendo lo mismo. Hay
  «reiniciar» a mano, y con casos de dos jugadas alcanza; con casos más
  largos habría que declarar `falla()`.
- **El Canje no tiene caso porque no está en la app.** Es la única de las
  mecánicas de la mesa que el árbitro digital no implementa —`grep canje`
  solo encuentra `canjeAvatar`, que es otra cosa (el préstamo de avatar de
  ¡Liceeeencia!)—. Un tutorial de algo que no ocurre sería enseñar una
  mentira. O se implementa, o se dice en el reglamento que es de mesa.
- **El caso 10 documenta una deuda en vez de enseñar una mecánica.** Las
  22 habilidades de avatar siguen siendo texto: el ⚡ marca el poder como
  gastado y el efecto lo aplica el jugador, igual que en la mesa. Está
  dicho desde el principio (cabecera de este documento) y es deliberado,
  pero un jugador nuevo lo lee como que la app está rota. El caso lo dice
  con todas las letras. La salida definitiva es hacer con los avatares lo
  que la v0.35 hizo con las 22 Acciones: darles un `ACC`-equivalente y que
  el árbitro las resuelva.
- **Dos ayudas que se solapan.** El coach clásico y los casos enseñan cosas
  distintas hoy, pero si los casos llegan a cubrir la interfaz, el coach
  sobra y son 60 líneas menos.

### Y una trampa que volvió a morder

`.sello` y `.num` ya existían —la etiqueta de la cama y el contador de los
requisitos— y las reutilicé sin mirar: el 🩺 del cierre salió dentro de una
píldora con borde y en mayúsculas. Es la tercera vez en el proyecto
(`.moneda` fue la primera). **Antes de inventar una clase, `grep`.**

---

## 5e. La contraindicación ⛔ (v0.60) ✅

Salió de mirar *Critical Care: The Game* (Swamy y Chan, 2020→) y darse
cuenta de que lo interesante no era su mecánica sino un hueco en la
nuestra, que el autor formuló así: **«pide 2 tto, pero no dice cuál»**.

Un paciente pedía cantidades por categoría y cualquier carta de esa
categoría servía. La decisión clínica se agotaba en el tipo. Ahora nueve
pacientes traen impreso **un recurso de un tipo que sí piden y que en
ellos está prohibido**:

| Paciente | ⛔ | Por qué |
|---|---|---|
| P12 Hemorragia Digestiva Alta | Anticoagulación | pide 2💊 y ese 💊 lo desangra |
| P11 ACV en Ventana | Anticoagulación | no antes del TAC |
| P13 Insuficiencia Cardíaca Desc. | Cristaloides | sobrecarga de volumen |
| P21 SDRA | Cristaloides | estrategia restrictiva |
| P16 EPOC Exacerbado | Sedoanalgesia | deprime el respiratorio |
| P18 Delirium del Adulto Mayor | Sedoanalgesia | lo empeora |
| P17 Intoxicación Mixta | Sedoanalgesia | encima de lo que ya tomó |
| P10 Cetoacidosis Diabética | Corticoides | le sube la glicemia |
| P07 El Que Googleó Sus Síntomas | TAC de Urgencia | cada imagen le encuentra algo |

**La condición de diseño es que el recurso sea de un tipo que el paciente
pide.** Si no, la regla es invisible: la carta ya no se podía jugar ahí por
tipo, y nadie se entera de que existe una contraindicación.
`tools/ingresar_arte.py` no valida esto, pero el script que llenó la
columna sí lo comprobó carta por carta, y conviene repetir la comprobación
si se añaden más.

### Medido

4.000 partidas, antes y después: **3,08 → 3,07 altas por jugador · 68 % →
68 % de salvamento · 8,9 → 8,8 puntos**. No mueve el balance.

Eso es a la vez la buena y la mala noticia, y hay que decirlo entero: **si
al bot no le cuesta nada, es porque el bot nunca alarga la mano hacia el
fármaco equivocado.** Con 4 cartas robadas y 3 indicaciones casi siempre
hay otra jugada. El valor de la regla es dramático y didáctico —el humano
sí comete el error, y la carta se lo dice— no económico. No se vendió como
ajuste de equilibrio y no debe usarse como tal.

### Lo que sí cambió sin buscarlo

La copia **⚠️** de un recurso contraindicado deja de "servirle" a ese
paciente. Así que si un rival te tira la Anticoagulación ⚠️ sobre la
hemorragia, ya no cuenta como tratamiento: cae como **basura clínica**. El
sabotaje no se amplió (sigue exigiendo carta ⚠️), pero ganó nueve objetivos
donde antes ayudaba al enemigo.

### Descartado en la misma sesión

- **El paciente que llega sucio** (con basura clínica puesta desde la
  admisión, como las fichas de daño de Critical Care). Medido con 5 de 26:
  altas 3,08 → **2,90**, salvamento 68 % → 65 % (bien, se despega del
  techo) pero «no se me fue nadie» 2,6 % → **1,8 %**, y esa métrica ya
  estaba por debajo de su objetivo de 5-15 %. Es viable, pero **hay que
  pagarlo**: +1 punto de alta a esos cinco, o un requisito menos. Sin
  compensar, empeora justo el número peor calibrado.
- **La economía de horas** (terapias que cuestan 3/6/9/12 h del turno, como
  en Critical Care). Elegante y descartada: mete aritmética en cada turno,
  que es exactamente de lo que murió la Era 2 (§SINTESIS 1).
- **Reglas propias por paciente.** Eso es la Era 1, muerta porque «cada
  carta necesitaba conocimiento médico para jugarse». La contraindicación
  es la versión sana del mismo impulso: **un símbolo, sin regla que leer**.

### De paso: el simulador jugaba otro juego

`simular_v030.py` tenía el Fin de Guardia de antes de la v0.58 —`si no está
estable, −1 ❤️`— sin la regla de que la basura clínica descongela el ✅.
Alineado y re-medido: **números idénticos**, porque el bot des-escala
siempre en cuanto le estorba. O sea que la regla no cambió el juego óptimo,
solo cerró un exploit que el juego óptimo no usaba. La calibración sigue
siendo válida, y ahora el simulador y la app juegan lo mismo.

---

## 5f. El comodín con casa propia (v0.60) ✅

El comodín valía 1 en cualquier cosa y **la app elegía el hueco por ti**:
`colocar()` lo mandaba solo al tipo con el agujero más grande, que muchas
veces es el peor sitio —justo el que ibas a llenar con la carta de sistema
que vale doble—. Dos cambios, y el comodín pasa de trámite a decisión:

1. **Ahora pregunta.** Si hay más de un hueco posible, se abre la hoja de
   elección con los cuatro tipos, cuánto le falta de cada uno y cuánto
   cubre la carta. Con un solo hueco no molesta. La IA sigue eligiendo
   sola: `elegirUno` se queda con la primera opción, y la lista viene
   ordenada con la casa propia delante.
2. **Tiene casa propia.** El **Stock de Sala** vale 2 puesto como 💊 y 1 en
   cualquier otro sitio; el **Médico General de Turno**, 2 como 🧑‍⚕️.

### La columna que reemplazó a un id cableado

`aporte()` tenía escrito a mano `if(carta.cirujano && … === "PERSONAL")`, y
`cirujano` era literalmente `r["id"] == "R54"` en tres archivos distintos.
Ahora es una columna, **`doble_en`**, y el Cirujano de Turno es un caso más
de la regla general. No queda ni un rastro del id en el código.

**El tope sigue siendo 2 y las fuentes no se suman.** Hay dos caminos al
×2 —sinergia de sistema y casa propia— y una carta que cumpla los dos sigue
valiendo 2. La gracia del juego es que el recurso correcto valga el doble,
no que existan cartas de cuatro.

### Medido

| variante | altas | salvamento | puntaje | «no se me fue nadie» |
|---|---|---|---|---|
| antes (comodín = 1 en todo) | 3,07 | 68 % | 8,8 | 2,5 % |
| **casa propia** (lo que se hizo) | 3,04 | 67 % | 8,6 | **3,0 %** |
| + un comodín por tipo, sin ⚠ | 3,16 | **69 %** | 9,3 | 3,2 % |
| + un comodín por tipo, con ⚠ | 3,15 | 68 % | 9,0 | 2,4 % |

La casa propia sale gratis y **sube la única métrica que estaba bajo
objetivo** (partidas limpias, 2,5 → 3,0 %, objetivo 5-15 %).

### Los dos comodines que faltan, si se quieren

La idea del autor era **uno por tipo**. Faltan el de 🩻 y el de 💉, y están
medidos arriba pero **no están en el mazo**: dos naipes más de pura
flexibilidad empujan el salvamento a 69 %, al filo del techo de la banda.
Se probaron con complicación ⚠ y vuelve a 68 %, pero entonces las partidas
limpias caen a 2,4 %. Las filas exactas que se midieron, por si se agregan:

```
R55,Rayos Portátil,COMODIN,🃏,,si,IMAGEN,,no,…,1,
    "Sube a la cama, dispara y se va. Nadie sabe quién la maneja."
R56,Carro de Procedimientos,COMODIN,🃏,,si,PROCEDIMIENTOS,,no,…,1,
    "Tiene de todo. Ordenado por nadie."
```

Decisión pendiente, y es de contenido: son dos ilustraciones más y un
salvamento en el filo.

---

## 5g. El soporte vital ⏸ (v0.61) ✅

El autor propuso que una carta valiera 2 según el estado del paciente —la
Ventilación Mecánica ×2 sobre alguien en ≤2 ❤️—. Se midió y se descartó a
favor de una versión distinta de la misma intuición.

**Por qué no el ×2.** Medido: aplicándoselo a las catorce cartas de
procedimientos y con umbral ≤3 ❤️, el salvamento solo sube de 67 % a 69 %.
El bono llega tarde: una unidad extra sobre alguien en 2 ❤️ casi nunca
alcanza a cerrar el requisito antes de que se acabe el reloj. Y tenía dos
costos que no salen en la tabla: diluye el ×2 —la firma del juego es *el
recurso correcto en el paciente correcto cuenta doble*, y una tercera
fuente lo vuelve común— y premia justo **no** hacer triage, que es la tesis
del juego. Débil y contra la tesis es la peor combinación: tienta a la
jugada mala sin pagarla.

**Lo que se hizo.** La carta compra **tiempo**, no requisitos: aguanta
**un** Fin de Guardia y se gasta. No toca la economía del ×2, y estrena un
verbo que no existía — hasta ahora **lo único que paraba el reloj era el
✅**, y el ✅ no se puede arrancar.

Se construyó primero permanente y el autor la corrigió a un turno con el
argumento correcto: *«un ventilado igual puede fallecer, lo sostiene un
turno»*. Los números le dieron la razón — permanente dejaba el salvamento
en 69 %, pegado al techo de la banda.

| | altas | ✝️/jug | salvamento | limpias | grado III |
|---|---|---|---|---|---|
| antes | 3,04 | 1,47 | 67 % | 3,0 % | 47 % |
| VM ×2 con ≤2 ❤️ | 3,07 | 1,46 | 68 % | 2,9 % | — |
| todos los 💉 ×2 con ≤3 ❤️ | 3,15 | 1,41 | 69 % | 3,5 % | — |
| VM para el reloj, permanente | 3,07 | 1,38 | 69 % | 3,6 % | 50 % |
| **VM aguanta 1 turno** (lo que quedó) | 3,07 | **1,42** | 68 % | **3,4 %** | 48 % |

Con **dos cartas** hace más que el ×2 con catorce.

### Detalles que costaron

- **`alFilo()` también había que tocarlo.** Es el que enciende el aura roja
  de «se muere esta noche», y sin la excepción quedaba encendida sobre el
  único paciente que no se muere.
- **`extraDeterioro` se consume siempre**, esté o no conectado. Si se
  quedaba dentro del `if`, un turno de *Llaman de Urgencias* se guardaba
  para el siguiente por haber estado en ventilador.
- **La insignia no cabía en la ficha.** Se puso primero como sello en la
  fila de sellos y **se recortaba sin avisar**: la cama tiene alto fijo y
  con ocho símbolos de recurso ya no queda sitio. Terminó junto al corazón,
  como **⏸ EN VM**, reemplazando al `congelada` del ✅ cuando hay las dos —
  porque el ventilador dice además que hay una carta que el rival puede
  arrancar. Regla general para la ficha de cama: **si la información es
  importante, no va en una fila que pueda quedar fuera del alto fijo.**

### Lo que queda por revisar (el autor lo pidió explícitamente)

- **Dura un turno**, y el aguante vive en la cama (`soporteVivo`) y no en
  la carta: la carta se queda puesta como 💉 aunque el aguante se haya
  consumido, colocar otra Ventilación Mecánica recarga, y que te la quiten
  desconecta. Solo se consume cuando de verdad salva.
- **Corta también la sangría de la basura clínica**, así que es la mejor
  defensa contra el sabotaje del §6.3. No estaba buscado.
- **El bot no sabe planear mantenerlo puesto** ni desconectárselo al rival,
  así que el número medido es un piso: en manos humanas debería rendir más.
- **Solo la Ventilación Mecánica.** El Catéter Venoso Central era el otro
  candidato y quedó fuera.

---

## 5h. Las habilidades del personal 🧑‍⚕️ (v0.62) ✅

El §5b de abajo decía que la columna `texto` de los recursos estaba vacía
en las 43 cartas y recomendaba llenar «5-8 como mucho». **Estaba
desactualizado**: al ir a mirar había ya **seis** recursos con texto, y las
seis eran 🧑‍⚕️. Nadie lo escribió como doctrina, pero el mazo ya estaba
construido así. Ahora está dicho:

> **Los recursos no hacen nada; las personas sí.**

Es la regla que justifica la excepción. Un recurso con texto es una carta
que hay que leer *cada vez* que alguien la juega, y los recursos son la
carta más frecuente del juego. Restringir el texto a las 🧑‍⚕️ acota el
coste de mesa a una familia que el jugador puede tener en la cabeza.

### Los cinco verbos

| | Verbo | Qué hace | Cartas |
|---|---|---|---|
| 🛡️ | PREVIENE | anula una ⚠ con nombre mientras esté puesto | R34, R35, R39 |
| ×2 | VALE DOBLE | cuenta 2 en su tipo | R54 |
| 🔎 | BUSCA | descarta 2 y saca 1 recurso del Mazo de Guardia | **R38 (nuevo)** |
| ↔ | MUEVE | reubica 1 recurso entre tus camas, gratis | **R53** |
| 🔁 | RECUPERA | rescata 1 Protocolo del descarte | **R37** |

Los tres últimos se disparan **al colocar la carta sobre un paciente
tuyo**, como tratamiento —nunca como sabotaje ni como basura— y **no
gastan indicación aparte**: la indicación es la de colocar.

**MUEVE y RECUPERA ya estaban escritas en el CSV desde antes y la app no
las ejecutaba**, igual que las 22 habilidades de avatar (§5d, caso 10).
Ahora corren.

### Medido

4.000 partidas: **3,07 → 3,06 altas · 68 % → 68 % de salvamento · 8,9 →
8,9 puntos**, y las partidas sin ningún ✝️ suben de 3,4 % a 3,7 %.

La búsqueda sale gratis y la razón es la buena: *descarta 2 para sacar 1*
es **negativo en cartas**. Pagas dos por una y el coste compra exactamente
la precisión. Es una mejora de **calidad**, no de poder — cambias cantidad
por certeza, que es lo que uno quiere de una habilidad.

Aviso de honestidad sobre ese número: el simulador **solo modela 🔎
BUSCA**. Mover un recurso y reciclar un Protocolo son jugadas de tempo que
este bot no sabe valorar, y fingirlas habría medido ruido.

### Lo que pidió el autor para más adelante

**El Kinesiólogo Respiratorio busca y arma la Ventilación Mecánica.** Su
argumento, textual: *«es muy propio de nuestro quehacer; vamos a intubar a
alguien y el kine busca y arma el VM»*. Yo objeté que el kine y el
ventilador son el mismo territorio clínico — **la objeción era mala**: que
sean el mismo territorio es justamente el motivo. Queda pendiente por dos
razones que sí son razones:

1. El Kine ya tiene 🛡️ (previene el Delirium), así que sería **la segunda
   habilidad en la misma carta** — el primer caso del mazo.
2. Crea un motor respiratorio fuerte: Kine (sinergia RESP, ×2 en
   pacientes respiratorios) + VM (⏸ soporte vital). Hay que medirlo antes,
   no después.

---

## 5i. Entrar a turno · la cortina de arranque (v0.63) ✅

**Ocho segundos** entre tocar la moneda y elegir personaje. Tres golpes de
mano y nada más:

| | Golpe | Rótulo | Dura |
|---|---|---|---|
| 1 | mano marcando la tarjeta en el reloj control | *Marcando tarjeta.* | 2,5 s |
| 2 | mano en el pulsador de la puerta | *Adentro.* | 2,3 s |
| 3 | manos bajo el chorro | *Veinte segundos. Cuéntalos.* | 3,2 s |

**El lavado va al final**, corregido por el autor y con razón clínica: la
higiene es en el punto de atención. Se marca tarjeta, se entra a la unidad,
y recién ahí uno se lava las manos antes de tocar al primer paciente.

**No hay cuarto golpe.** Hubo uno —el retrato de «hoy te toca con»— y se
sacó: la pantalla que viene ya está llena de caras, así que poner una antes
era decir dos veces lo mismo, y encima presentaba a un personaje que
todavía no estaba repartido.

**No esconde ninguna carga.** La partida se arma en un milisegundo; esto es
una cortina de ficción. Por eso **se salta tocando la pantalla** y por eso
**no lleva barra de progreso** —una barra falsa sería mentirle al jugador—:
lleva tres puntos, que dicen cuánto falta sin fingir que miden algo. Con
`prefers-reduced-motion` no aparece.

### El hueco para la ilustración

Los tres golpes son **íconos de línea provisionales**, dibujados en el
mismo trazo que el resto de la app. `arte/entrada/{reloj,lavado,puerta}.webp`
los reemplaza **de a uno**: el golpe que tenga archivo usa la imagen, el
que no, sigue con su ícono. Cuadrado 1:1, fondo transparente, 800×800
basta. Está documentado en `arte/entrada/LEEME.md` y verificado metiendo
una imagen de prueba: el marco pasó de `svg svg svg` a `svg IMG svg`.

### Dos cosas que costaron

- **El tercer golpe se dibujó dos veces.** El primero era un guante y no se
  leía —sin dedos separados podía ser un calcetín—. El segundo era la mano
  empujando la hoja de la puerta, y salió peor: giré la mano con
  `rotate(-90)` cuando lo que manda los dedos a la derecha es `rotate(90)`,
  y encima la puerta se la comía. Terminó siendo el pulsador, que además es
  lo que uno toca de verdad para entrar a una UCI, y que **reusa la
  composición del primer golpe** —objeto arriba, mano vertical abajo—, que
  es la que ya se sabía que funcionaba.
- **Un ícono hay que mirarlo, no describirlo.** Los tres se juzgaron
  capturando los cuatro cuadros y mirándolos; los dos primeros pasaron a la
  primera y el tercero no, y eso no se sabe leyendo el `path`.

---

## 5j. Personajes con movimiento (v0.64) 🔶

### Lo que ya se hizo, gratis y sin salir de la app

- **La carta del frente respira.** Paneo lentísimo de 11 s sobre la
  ilustración del personaje enfocado en la rueda de selección: escala
  1,015 → 1,075 con un desplazamiento de dos puntos. Va **sobre la imagen y
  nunca sobre la carta**, porque el `transform` de la carta lo reescribe
  `pintarRueda` en cada arrastre y las dos se pelearían.
- **Solo el del frente.** Si se movieran las tres, la pantalla temblaría
  entera y ninguna diría «esta es». La clase `.foco` la pone `pintarRueda`.
- **El retrato redondo del mesón ya se movía** desde antes: `av-respira`,
  escala 1 → 1,02 cada 5,2 s, y está en `LATIDOS` para que el re-render no
  la reinicie. Medido: 1,1 % de píxeles en 1,3 s. Es sutil a propósito — a
  94 px cualquier cosa más grande se lee como tembleque.

Medido en el navegador: la carta enfocada cambia **21,6 % de píxeles en
2,4 s**, la vecina con arte tiene `animation-name: none`.

### Animación de verdad (Google Flow u otro): el análisis

Un personaje que parpadea o mueve la bata **no se puede hacer con CSS**:
hace falta un clip por avatar. Lo que decide si vale la pena es el **peso**,
no la herramienta.

- **El artefacto de un archivo tiene tope duro de 16 MB** y va en ~6,2 MB.
  22 avatares × un bucle de 2 s a 720×540 VP9 ≈ 180 KB cada uno = **~4 MB**.
  Cabe, pero se come casi toda la holgura que queda para las 115
  ilustraciones de carta que todavía faltan.
- **La PWA no tiene tope**: los archivos van sueltos y el service worker los
  cachea uno a uno. Ahí sí caben sin discusión.
- **El círculo de 94 px no lo vale.** Un parpadeo a ese tamaño mide dos
  píxeles. Serían 22 clips para animar una miniatura que nadie puede ver: el
  CSS que ya está es la respuesta correcta ahí.
- **Donde sí vale** es la pantalla de selección (244 px, y es el momento en
  que uno está mirando una cara) y, si acaso, el zoom de la carta.

**Receta si se generan:** un clip por avatar, **2-3 s en bucle perfecto**
—que termine donde empieza—, sutil (respiración, un parpadeo, la tela, el
fondo vivo) y **sin movimiento de cámara**, que de eso ya se encarga el CSS.
**4:3 a 800×600**, mismo encuadre que el arte fijo para que el cambio no se
note. **WebM/VP9, sin audio, ≤150 KB.** Nombre = id de la carta
(`C03.webm`).

**Ojo con el formato:** el navegador de pruebas de este entorno **no tiene
H.264**, solo VP9/Opus. Un MP4 lo reproduce cualquier teléfono, pero yo no
podría verificarlo aquí. Mejor WebM, o MP4 y lo transcodifico.

**Pendiente de decisión:** montar el hueco `cartas/arte-vivo/<ID>.webm` con
el mismo patrón que `arte/entrada/` —si el clip existe, la carta de
selección lo reproduce; si no, imagen fija con el paneo— y decidir si los
clips entran también al artefacto o solo a la PWA.

---

## 5k. La Guardia del Día 🗓️ (v0.65) ✅

El reto diario: una partida contra la IA cuya baraja **la siembra la
fecha**. Todo el que juegue el 4 de septiembre recibe los mismos pacientes
de partida, la misma mano, la misma pizarra y la misma terna de avatares;
lo único distinto es cómo la juega. Entra por su propia ficha en la
portada, bajo La Residencia.

Cómo está hecho:

- Todo el azar del juego pasa por `AZAR` (por defecto `Math.random`).
  `nuevaPartida(modo, nombres, tuto, dia)` con `dia` = `"2026-09-04"`
  siembra un mulberry32 con el hash de la fecha **solo durante el reparto
  inicial** (los cuatro barajados); después `AZAR` vuelve a ser
  `Math.random`, así que el rebarajeo del descarte y la moneda de la
  Pelada siguen siendo azar de verdad — para entonces las partidas ya
  divergieron y no afecta la equidad del arranque.
- **El parte del día se firma una sola vez**: el primer resultado de cada
  fecha queda en `localStorage['vt-dia']` y no se pisa aunque repitas
  (la baraja es la misma: repetir con lo aprendido sería trampa). La
  portada muestra el parte firmado; la pantalla final gana el botón
  **«Compartir el parte del día»** (navigator.share o portapapeles):

      ¡VAYA TURNO! · Guardia del 04-09-2026
      🛏️ 2 altas · ✝️ 0 · 9 pts
      🏆 Le gané a Dr. Silicio (2)
      https://diegonicolasmelo-cell.github.io/VAYA-TURNO/juego/

- Verificado con Playwright (`dia.py`): dos arranques de la misma fecha
  dan huella idéntica (pacientes, manos, pizarra, terna), el modo normal
  difiere y no lleva `G.dia`, el parte no se pisa, y el soak de 5 partidas
  sigue 5/5 limpio.

**Queda para después** (anotado también en `IDEAS-MODOS.md`): la racha
(cuántos días seguidos firmaste), un historial de partes, y que el texto
compartido lleve una fila de emojis por ronda al estilo Wordle.

---

## 5b. Texto de efecto en los Recursos 🔶 (columna abierta, sin usar)

`recursos.csv` tiene desde v0.13 una columna **`texto`**, vacía en las 43
cartas. El Taller la deja editar y el PnP la imprime si tiene contenido.

**Antes de llenarla, conviene saber esto:** hoy los recursos **no tienen
texto** a propósito — son puro ícono, y todo lo que hacen se lee de sus
símbolos (tipo, chip de sistema, ⚑ restricción, ⚠️ complicación). Eso es lo
que permite jugar 5 recursos en un turno sin frenar la mesa. Cada recurso con
texto es una carta más que leer **cada vez que alguien la juega**, y son la
carta más frecuente del juego (63 de 159).

Recomendación: **texto solo en unas pocas** (5–8 como mucho, las más
memorables), no en las 43. Y ninguna que cambie la economía sin volver a
correr `simular.py` — el simulador no lee esta columna, así que cualquier
efecto que toque vida, requisitos o robo queda **fuera del balance validado**.

---

## 6. Herramientas ⬜

- ⬜ Columna `set` en CSVs + filtro en Taller/PnP/simulador (`EXPANSIONES.md` §5).
- ⬜ `generar_pnp.py --arte`: cargar ilustraciones desde `arte/final/` cuando existan.
- ⬜ Modelar Acciones en el simulador (opcional, grande: hoy el suelo del balance no las necesita, pero cerraría §1.1 sin mesa).

---

## El orden sugerido

1. **Playtest** (3 sesiones, `PLAYTEST.md`) — desbloquea todo el §1.
2. Cerrar las 6 ambigüedades del §3 con la carta en la mano (30 min de mesa).
3. Generar los 6 avatares de arte (fija el estilo del resto).
4. El resto del arte, por tandas.
5. Recién ahí: mirar el §4.

---

## 7. Deuda de la app · v0.57 (la tanda de los ocho arreglos)

### Podar la maqueta A ⬜

`maqueta()` devuelve `"b"` siempre desde la v0.57 —el autor se quedó con el
campo partido— pero las ramas `if(esB())` siguen todas en pie, y con ellas
las funciones que solo servían a A: `chipRival()`, `modalRival()`,
`barraEstado()`, la franja de guía, la tira `.selector`, el abanico viejo
de `.ranura`, y unas 200 líneas de CSS bajo selectores sin
`body[data-maq="b"]`. Podarlo es mecánico y grande a la vez; se dejó fuera
de esta tanda para no mezclar un borrado masivo con ocho arreglos que sí
había que revisar uno por uno. **Antes de podar:** las pruebas de
`scratchpad/app/etapa1.py` y `etapa3.py` afirman sobre `.rival-chip` y
`.selector`, así que hay que reescribirlas o borrarlas en el mismo commit.

### Dos tamaños de arte ⬜

El hueco más grande es el zoom: 342 px de CSS, o sea **1026 px reales** en
un teléfono 3×. El generador guarda a 800 px (subió de 520 en la v0.57,
gratis, porque el arte 4:3 ya no desperdicia píxeles en el recorte). Subir
a 1024 pondría las 115 cartas en ≈ 7 MB y el artefacto de un archivo tiene
tope de 16 MB contando tablero, portada y clip. La salida limpia es
guardar **dos tamaños** —≈420 px para mano y camas, ≈1024 px solo para el
zoom— y que `verCartaGrande`/`verPacienteGrande` pidan el suyo. No cambia
nada de lo que hay que dibujar: los dos salen del mismo original de 1600.

### Trampas nuevas encontradas en esta tanda

- **Las animaciones infinitas se relanzan en cada render.** `#app` se
  reconstruye entero, así que toda `animation: … infinite` que viva adentro
  vuelve al fotograma 0. Medido: 235 relanzamientos por partida y un salto
  de 0,0102 de escala en el retrato —media amplitud— en cada uno. Se
  arregla con `animation-delay` negativo igual a `performance.now() % dur`,
  repuesto en cada render (`continuarAnimaciones()`, lista `LATIDOS`).
  Cualquier animación infinita nueva dentro de `#app` hay que apuntarla ahí.
- **Colisión de clases: `.moneda`.** El menú de inicio estrenó una
  `.moneda` para el ícono, y ya existía `.moneda` —la del alta, que es
  `position:fixed`—. El botón salió con el ícono flotando sobre el texto y
  no se veía en el CSS: había que mirar el `getComputedStyle`. Antes de
  estrenar una clase, `grep`.
- **`z-index` negativo no sirve de fondo.** `.final-fondo` con `z-index:-2`
  quedaba TAPADO por el papel del tablero: los hijos con z negativo se
  pintan antes que los fondos de los bloques del documento. Fondo en 0,
  contenido en 1, y `isolation:isolate` en el contenedor.
- **`getBoundingClientRect` de un elemento rotado miente.** Devuelve la caja
  alineada a los ejes de la caja rotada, así que una carta del abanico con
  `rotate(3.5deg)` mide 115×95 cuando en realidad es 90×67,5. Para medir
  proporciones dentro del abanico, `getComputedStyle().width/height`.
- **La opacidad no es distancia.** Las cartas lejanas del abanico estaban a
  `opacity:.55` y el papel dejaba pasar el texto de las de atrás: la mano
  entera se veía como una nube de letras —lo que el autor llamó «la mano
  invisible»—. La lejanía se da con `filter:saturate()`, que no vuelve
  translúcido el papel.

### El clip de portada ✅ y lo que queda

`arte/portada/portada.mp4` es el clip nuevo (2,29 MB, ida y vuelta, 16 s).
Entra **por ancho y anclado arriba**, no a sangre: el clip es 9:16 y el
teléfono 9:19,5, así que llenar la pantalla se comía el 18 % de cada
costado. Debajo del clip sobran ~150 px que rellena el papel de la mesa, y
ahí caen los tres cuadrados del menú. `dibujo.svg` pasa a ser el respaldo
de última hora, debajo del cuadro fijo.

- ⬜ Las tres salas del fondo se animan dentro del clip, no en CSS: si
  alguna vez hay que retocar una (el ritmo de las compresiones, por
  ejemplo) hay que volver a Flow, no al código.

### El sello de la caché contaba los nombres, no los bytes ✅ (v0.57)

`generar_app.py --pwa` calculaba la versión del service worker con el HTML,
el manifiesto, la huella de los **íconos** y la **lista de nombres** del
resto. O sea: reemplazar `portada/portada.mp4` por otro clip con el mismo
nombre **no movía el sello**, y los teléfonos ya instalados se quedaban con
el video viejo para siempre — que es exactamente el bicho que el comentario
del código decía haber arreglado, pero solo para los íconos. Ahora la
huella se calcula sobre el contenido de **todo** lo que entra a la caché:
íconos, tipografías, arte y portada. Comprobado: cambiar un byte de
`salida.webp` mueve el sello de `89b5b1cf7bbb` a `b1d31d2f02a7`, y
restaurarlo lo devuelve.

Regla para el futuro: **cualquier archivo nuevo que se sume a la caché
tiene que entrar en `cacheados`**, o volvemos al mismo agujero.

### La Entrega de Turno ✅ (v0.58)

La primera fase del juego ya se llamaba así y era la única que nunca
ocurría en pantalla: elegías personaje y de golpe había dos pacientes en
sus camas. Ahora la colega que sale te pasa la unidad, cama por cama.

Dos formas, y la diferencia es cuántas veces la has visto —bandera
`vt-entrega-vista` en localStorage—:

- **La ceremonia**, la primera guardia de todas y siempre con el coach:
  apertura con el reloj, un golpe por cama con la carta grande, la cama
  vacía («por ahora») y el cierre. «Saltar» desde el primer toque.
- **La hoja**, de ahí en adelante: una pantalla, dos toques, y tocar una
  cama abre la ficha de siempre.

**No toca ninguna regla.** No se elige paciente, no cambia el reparto: el
61 % de salvamento y el 8 % de guardias limpias siguen valiendo.

Dos columnas nuevas en `pacientes.csv`, editables desde el Taller:

- **`edad`** — llena con edades plausibles para las 26, deducidas de la
  propia carta (la Caída del Baño tiene 78, el Politraumatizado que iba a
  120 sin cinturón tiene 22). Son un marcador de trabajo: cámbialas.
- **`entrega`** — ⬜ **vacía a propósito, la escribe el autor.** Es la
  línea con que la colega te pasa el paciente, y es distinta de `frase`:
  la frase es el chiste de la carta, la entrega es alguien contándote el
  caso. Mientras esté vacía se usa la `frase`, así que la pantalla
  funciona hoy y mejora sola cuando se llene.

### Las dos pantallas que esperan tienen reloj ✅ (v0.58)

La admisión y la Entrega no se quedan esperando para siempre: **a los 10 s
siguen solas**. La admisión entra con el paciente marcado —o con el
primero, si no marcaste ninguno—, lo deja anotado en la bitácora y arranca
el turno; la Entrega pasa al golpe siguiente, así que si dejas el teléfono
la ceremonia se cuenta sola y el juego empieza igual.

Dos decisiones que no pidió el autor pero que el reloj obliga a tomar:

- **Va con barra a la vista**, en el filo de abajo. Una cuenta atrás
  invisible que actúa por su cuenta es una trampa, no una comodidad.
- **Marcar un paciente reinicia los 10 s** (`reiniciarRelojCapa`). Sin
  eso, marcar en el segundo nueve te dejaba uno para confirmar.

No lo llevan ni la elección de personaje ni la cortina del hotseat: las
dos piden una decisión que no se puede poner por defecto sin robársela al
jugador.

### Y la capa de pantallas pendientes ya no parpadea ✅ (v0.58)

`pintarCapa()` vaciaba y rehacía `#capa` en **cada** render, y con ella
volvían a arrancar las animaciones de entrada: el velo aparece, la hoja
sube, las opciones entran en cascada. En la admisión eso se veía como un
parpadeo cada vez que tocabas un paciente —tocar guarda la elección y
llama a `render`, o sea que la pantalla entera volvía a nacer para cambiar
una clase—. Es el mismo bicho que la rueda de avatares ya tenía parcheado
a mano en 2026-08; ahora la regla es de todas.

`clavePendiente(p)` firma el estado y la capa se monta **una vez por
estado**; mientras la clave no cambie, `refrescarPendiente()` retoca lo
que haga falta (hoy solo la selección de la admisión). La clave incluye el
golpe de la Entrega, que sí quiere volver a entrar en cada paso.

Medido: seis toques sobre las opciones de la admisión pasan de **24
animaciones relanzadas a 0**, y la ceremonia sigue animando **una vez por
golpe** aunque le fuerces dos renders en medio.

Si mañana una pantalla pendiente gana estado interno, hay que sumarla a
`refrescarPendiente()` — si no, se queda congelada en su primer dibujo.

Trampa encontrada: `.pips`, `.gr` y `.uni` estaban scopeados a
`.cama.pficha`, así que los símbolos de recurso salían como `<i>` sin
tamaño en cualquier pantalla nueva. Si aparece otra vista que los use,
hay que darles estilo propio o subir esas reglas.

### La basura clínica ya muerde ✅ (v0.57)

Dos cosas, una de interfaz y una de reglas.

**No se podía des-escalar porque el botón no estaba en pantalla.** La
ficha de la cama tiene alto fijo —las dos mitades del campo miden igual— y
`cama-btn` se añadía DESPUÉS del contenido: caía 17 px por fuera y la cama
recorta con `overflow:hidden`. Medido: cama en 474–606, botón en 623–649.
Y no era solo «Des-escalar»: «Tratar», «Sabotear» y «🛡️ protegido»
llevaban invisibles desde que la ficha tiene alto fijo. Ahora la banda es
absoluta **sobre la ilustración** —no sobre el pie, donde están los
símbolos de recurso, que es justo lo que hay que leer para decidir— y no
ocupa alto, así que el espejo sigue cuadrando. La des-escalada está además
en la ficha del paciente, que es donde hay sitio para decir lo que cuesta.

**Y el ✅ ya no protege con basura encima.** Antes un paciente
estabilizado con basura era inmune para siempre: no moría porque el ✅
congela el reloj, y no se iba de alta porque la basura la retiene. Dejar
la basura salía gratis. Ahora la basura descongela: pierde 1 ❤️ al cierre
de cada turno hasta que la saques. **Esto NO está en el balance validado**
—`simular.py` no modela Acciones ni basura—, así que es candidato número
uno a revisar en la primera mesa: si el sabotaje con ⚠️ resulta demasiado
letal, la palanca es hacer que muerda solo al paciente ✅ y no al que ya
se estaba deteriorando.

### El aura de la cama ✅ (v0.57)

Verde fija en el que se va de alta en tu próxima Entrega (`estable` y sin
basura), roja latiendo en el que no llega vivo al cierre del turno
(`vida − deterioro ≤ 0`). Va en un `::after` con sombra **interior**: la
ficha recorta, así que una sombra por fuera no se vería, y así tampoco
pelea con el borde de gravedad ni con el aro del escudo, que son
box-shadow del propio elemento.

El aura roja late, y late dentro de `#app`: entra en `LATIDOS`. Pero es un
pseudo-elemento y a un `::after` no se le escribe el estilo desde JS, así
que el retardo se le pasa por variable (`--fase`) — de ahí el tercer campo
de la lista.

### El audio de la portada ✅ (v0.57)

El clip trae su propia música y es la que se queda. `sonido_portada.py`
—que sintetizaba monitores, alarmas y las pasadas del trapero— deja de
usarse; el módulo se queda en el repo por si vuelve a llegar un clip mudo.

**La imagen va y vuelve; el audio no.** El autor quiso el vaivén de vuelta
—cierra el ciclo sin corte y a un tipo trapeando le calza—, pero la música
son 125 pulsos por minuto y al revés se nota a la primera. Así que el video
es ida y vuelta y el audio se construye aparte: el original repetido hacia
adelante hasta cubrir el ciclo, con 0,45 s de disolvencia en cada empalme y
otra que envuelve el final sobre el principio. Comprobado midiendo el pulso
por mitades: 125 en las dos.

**El crescendo se queda.** El clip sube de volumen de principio a fin y en
bucle eso se oye como un vaivén. Se probó nivelarlo —`aplanar()` divide por
el RMS corrido con ventana de 1,6 s, mucho más larga que un compás para no
tocar el pulso, con la ganancia acotada— y funciona: la desviación de nivel
a lo largo del ciclo baja del 32 % al 10 % sin recorte. **Pero el autor
prefirió su música tal cual**, así que queda `APLANAR = False`. La función
sigue ahí y se enciende con esa línea.

Tres trampas encontradas en el camino, por si vuelve el tema:

- **`xfade` no sirve para cerrar un bucle sobre sí mismo.** Exige que su
  primera entrada dure más que `offset+duration`, y la cola mide justo la
  disolvencia. Sale con `overlay` y un `fade=alpha=1` sobre la cabeza.
- **`acrossfade` devuelve cero muestras** con entradas de esa largura, y el
  error que da es `Could not open encoder before EOF`, que no apunta a
  nada. Y el `aformat` de entrada no sobra: sin él el `concat` de audio no
  arranca. Por las dos cosas el montaje del audio se hace en numpy, donde
  se ve lo que pasa y se puede medir.
- **El nivel por segundo engaña.** Esta música son ráfagas de 0,17 con
  huecos de 0,03 entre medio: un RMS por segundo da 0,10 planito y esconde
  el patrón. Para juzgar una costura hay que mirar la envolvente a 50 ms.
