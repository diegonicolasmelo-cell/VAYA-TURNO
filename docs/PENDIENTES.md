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
las ⚠️, las 🛡️, la basura y los Sumarios; las Acciones y las habilidades de
avatar se aplican a mano y quedan en la bitácora, que se copia al portapapeles
para pegarla acá.

**Batería de jugabilidad (agosto 2026, 4.000 partidas 2j + 3.000 partidas
3j, IA de referencia):** el flujo está sano — las 3 colocaciones se usan
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
son las colocaciones, no las cartas. Lo que sí lo paga es exigir 🧑‍⚕️
Personal ya puesto en esa cama (66%, en banda, y clínicamente cierto).
Si se adopta: cartas simples con etiqueta de sistema, cartas complejas con
valor 2 fijo y requisito de Personal, **sin acumular ambas**, y el
requisito solo sobre las **10 no-Personal** (Cirujano y Kinesiólogo se
autobloquearían). Medido: el Personal **no escasea**, se vuelve una llave
— añadir copias casi no alivia porque la traba es de secuencia, no de
oferta. Vigilar en mesa la sensación de "tengo el TAC y no puedo jugarlo"
(1,85 bloqueos por turno).

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
