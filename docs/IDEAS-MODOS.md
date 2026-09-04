# Otros modos de juego — el catálogo razonado

**v0.65.** La plataforma ya tiene cuatro maneras de jugar: contra la IA,
Dúo en un teléfono, Solo a dos manos, y desde hoy **La Guardia del Día**
(el reto diario con la baraja sembrada por la fecha, ver `PENDIENTES.md`
§5k). Este documento junta los modos que se conversaron y los que salen
solos del material que ya existe, **ordenados por lo que cuestan contra lo
que rinden** — para que cuando toque elegir el próximo, la decisión ya
esté a medio tomar.

La regla de la casa aplica aquí más que nunca: antes de construir un modo,
medirlo. Si un modo cambia reglas (no solo el reparto), primero pasa por
`tools/simular_v030.py`.

---

## Los que se pagan solos (poco código, mucho juego)

### 1. La racha del parte diario 🔥 — ✅ hecha (v0.65)

No era un modo nuevo: era terminar el que acaba de nacer. Firmar en
fechas seguidas sube la racha (🔥N en la portada, «🔥 N guardias
seguidas» en el texto compartido); un día sin jugar la corta. Es la
mecánica que hace volver mañana — Wordle no es un buen juego de palabras,
es una buena racha.

- **Queda de ella:** el historial de partes y la fila de emojis por ronda
  en el texto, estilo Wordle.

### 2. El Turno Eterno (guardia infinita) ♾️

Supervivencia: no hay 8 rondas — la guardia sigue mientras no se te muera
nadie (o hasta la tercera cruz, a decidir). Los pacientes entran cada vez
más graves: a partir de la ronda 9, todos llegan con una ⚠ puesta; a
partir de la 13, con dos. El marcador es **cuántas rondas aguantaste**.

- **Cuesta:** quitar el tope de rondas en un modo, una curva de dificultad
  (basura inicial creciente ya existe como mecánica: `basura[]` en la
  cama), y un récord en localStorage.
- **Rinde:** el modo de «una más y me acuesto». Y es el único que produce
  un número simple que crece — perfecto para compartir.
- **Ojo:** el mazo de pacientes es finito (26). Cuando se acaba, se
  rebaraja con los dados de alta — temáticamente «volvieron a caer».

### 3. El Brote 🦠 (guardia temática)

Una guardia normal pero el mazo de pacientes viene cargado hacia un
sistema: la semana respiratoria (brote de virus sincicial — cosa que en
Chile no hay que explicarle a nadie), la semana quirúrgica, la neuro. Los
recursos de ese sistema escasean o abundan, a elegir.

- **Cuesta:** un filtro/refuerzo al armar `mazoP` y `mazoG` por etiqueta
  de sistema, que ya existe en los CSV. Una pantalla de elegir brote.
- **Rinde:** rejugabilidad barata y muy temática. Combina con el diario
  (el brote del día).
- **Medir antes:** el simulador con mazo sesgado — un brote respiratorio
  con pocos ventiladores puede ser injugable, no difícil.

---

## Los medianos (una tarde larga, y hay que medir)

### 4. El Modo Director 🎬 (draft de la unidad)

Antes de la ronda 1, cada jugador **arma su unidad**: se revelan 5
pacientes y eliges 2 (el rival igual), y la mano inicial se draftea — 4
cartas, eliges 1 y pasas el resto. El azar del reparto se convierte en
decisiones, que es lo que pide el jugador que ya domina el juego base.

- **Cuesta:** dos pantallas de selección (la de admisión ya casi sirve) y
  el pase de manos. Con IA: heurística de qué draftea el rival.
- **Rinde:** profundidad para veteranos. Es EL modo torneo.
- **Medir antes:** que elegir pacientes fáciles no sea siempre mejor — el
  puntaje por gravedad ya lo compensa (G·III da más), pero hay que ver los
  números.

### 5. Contrarreloj ⏱️

El Pase de Visita con reloj: 45 segundos por turno (o un presupuesto total
de 5 minutos por guardia, estilo ajedrez rápido). Se te acaba el tiempo,
se acaba el turno — las indicaciones no usadas se pierden.

- **Cuesta:** un temporizador visible, pausas limpias (las hojas modales
  tendrían que congelarlo) y decidir qué pasa con las pendientes.
- **Rinde:** tensión de arcade. En un juego que ya es de gestión de pánico
  temático, le calza.
- **Riesgo:** pelea con la accesibilidad y con el juego pensado — es el
  modo que más gente va a apagar. Que sea opcional siempre.

### 6. Hotseat de 3 y 4 jugadores 👥

El motor ya reparte `nombres.map(...)` y `otros()` es una lista — el
código casi no supone 2 jugadores. Lo que sí supone 2 es **la pantalla**
(zona cerca/lejos) y el balance (sumarios libres, tamaño del mazo, el
sabotaje se reparte distinto entre 3).

- **Cuesta:** layout para N rivales (la vista B con chips ya apunta ahí),
  y una pasada seria de balance en el simulador con 3-4 IAs.
- **Rinde:** el juego de mesa en persona es de 2-4; la app debería
  alcanzarlo algún día. Pero es el mediano más caro.

---

## Los grandes (proyectos con nombre propio)

### 7. El Modo Docente 🎓 (casos propios)

La Residencia con casos escritos por profesores: el Taller
(`generar_taller.py`) gana una pestaña donde un docente arma un escenario
—estos pacientes, esta mano, esta meta— y lo exporta como un enlace o un
JSON que otro teléfono importa. El motor de casos (`montarCaso`, metas
sobre G) ya es datos más que código; lo que falta es el editor y el
formato de intercambio.

- **Rinde:** es la puerta a que el juego viva en escuelas de medicina y
  enfermería — que es de donde viene y donde más se le quiere. Único modo
  que crea contenido sin tocar el repositorio.

### 8. Cooperativo: los dos contra la unidad 🤝

Dos jugadores, una sola unidad de 6 camas, la «IA» es la guardia misma:
cada ronda la unidad tira complicaciones (una carta de evento por ronda —
brote, corte de luz, fuga de un paciente). Se gana si la unidad termina la
noche con más altas que cruces.

- **Cuesta:** un mazo de eventos nuevo (diseño, no solo código) y
  rebalancear todo — el sabotaje, que es media economía del juego, aquí no
  existe.
- **Rinde:** el modo para parejas que no quieren competir. Es
  temáticamente el más honesto: en la UCI real el rival nunca es el otro
  turno… bueno, casi nunca.

### 9. El torneo del parte 🏆

La Guardia del Día compartida de verdad: una tabla del día entre amigos.
Sin servidor propio, dos caminos honestos — el texto compartido ya sirve
de tabla manual en el grupo de WhatsApp (gratis, ya funciona), o la base
de datos del artefacto para una tabla real entre quienes usan el enlace de
Claude.

- **Cuesta:** decidir dónde viven los puntajes. Todo lo demás ya existe.
- **Rinde:** convierte el diario en liga. Pero el juego debe ganarse esa
  liga primero — esperar a que el diario tenga jugadores.

---

## El orden que este documento recomienda

1. **La racha** (§1) — termina el modo que acaba de nacer, cuesta nada.
2. **El Turno Eterno** (§2) — el mejor cociente juego/código del catálogo.
3. **El Brote** (§3) — barato, temático, y ensaya el filtro de mazos que
   el Director (§4) necesitará después.
4. Después del playtest físico: **Director** o **Docente**, según si el
   juego tira más a torneo o a sala de clases.

Lo que NO recomienda: empezar por el cooperativo o el hotseat de 4. Son
los más caros y los dos piden rebalancear la economía completa antes de
saber si alguien los va a jugar.
