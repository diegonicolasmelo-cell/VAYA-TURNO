# Plan de expansiones — ¡Vaya Turno!

Una expansión por sistema clínico. Cada una convierte tu UCI en una unidad
especializada: recibes más de un tipo de paciente y menos del resto.

> Nada de esto se produce antes del primer playtest de la caja base. Está
> escrito para que la base **reserve espacio** a cada módulo, no para
> fabricarlo ya.

---

## 1. El modelo: reemplazar, no engordar

**El mazo nunca crece.** Una expansión sustituye cartas de la caja base en el
mismo eje: pacientes por pacientes, recursos específicos por recursos
específicos, eventos por eventos.

**Por qué así y no acumulando:**

- El balance está calibrado sobre proporciones (63 recursos, 26 pacientes,
  17 ⚠️, 21 específicos). Si el mazo engorda, hay que recalibrar el robo en
  cada expansión y las partidas se alargan.
- Temáticamente es lo que pasa de verdad: cuando abren la unidad de
  neurocríticos, no te llegan *más* pacientes — te llegan **otros**.
- Es más barato de producir: una expansión de ~26 cartas, no de 60.

### Regla de montaje

Ejemplo con el **Módulo Neurocrítico**. Las demás son idénticas cambiando el
sistema:

| Paso | Qué haces | Resultado |
|---|---|---|
| 1 | Retira **12 pacientes no-🧠** del mazo base y mete los 12 🧠 de la expansión | 26 pacientes · 12 neuro (46%) |
| 2 | Retira **6 recursos específicos de otros sistemas** y mete los 6 🧠 | 63 recursos · 21 específicos · neuro pasa de 3 a 9 |
| 3 | Retira **6 Eventos Centinela `GENERAL`** y mete los 6 🧠 | 28 eventos · 9 neuro |
| 4 | Añade el avatar y las 2 acciones | Estos sí suman: son pocos y no mueven la economía |

Las cifras salen de conservar las proporciones ya calibradas. **El robo, las
rondas y la puntuación no cambian.** El balance se mantiene por construcción,
y `tools/simular.py` puede verificarlo antes de imprimir.

---

## 2. Qué trae una expansión

| Componente | Cant. | Nota |
|---|---:|---|
| **Pacientes** del sistema | 12 | Repartidos en las cuatro gravedades, como en la base |
| **Recursos específicos** del sistema | 6 | Con su chip de sinergia |
| **Eventos Centinela** propios | 6 | Las complicaciones típicas de esa unidad |
| **Avatar** temático | 1 | El especialista de esa área |
| **Acciones** | 2 | La burocracia particular de ese servicio |
| | **27** | Una cajita, no una caja |

---

## 3. Los cinco módulos previstos

| Módulo | Avatar probable | Complicaciones propias |
|---|---|---|
| 🧠 **Neurocrítico** | El Neurocirujano que opera a las 4 AM | Vasoespasmo, hipertensión intracraneal, muerte encefálica, status refractario |
| 🫁 **Respiratorio** | El Broncopulmonar | Fístula broncopleural, weaning fallido, traqueostomía tardía, SDRA refractario |
| 🫀 **Cardiovascular** | El Cardiólogo intervencionista | Shock cardiogénico, arritmia maligna, taponamiento, ECMO |
| 🔪 **Quirúrgico** | El Cirujano que "ya terminó su parte" | Dehiscencia, abdomen abierto, sangrado postoperatorio, íleo prolongado |
| 🧪 **Metabólico** | El Nefrólogo o el Endocrinólogo | Diálisis urgente, crisis tiroidea, hiperkalemia, síndrome de realimentación |

---

## 4. Lo que la caja base debe reservarse

Esta es la consecuencia práctica del plan, y **corrige un diagnóstico
anterior**: en `DISENO.md` §4 el reparto desigual de recursos específicos
está anotado como defecto a emparejar. Con expansiones por sistema, **no lo
es del todo**. La regla correcta es distinta:

> La caja base debe cubrir los cinco sistemas de forma **pareja pero fina**.
> Ningún sistema debe quedar agotado antes de su propio módulo.

Estado actual (recursos específicos / pacientes por sistema):

| Sistema | Rec. | Pac. | Lectura |
|---|---:|---:|---|
| 🫁 RESP | 4 | 4 | Ajustado en v0.12: la Ventilación Mecánica pasó a genérica (sirve al politrauma y al séptico igual) |
| 🫀 CARD | 5 | 5 | Bien |
| 🔪 QUIR | 5 | 7 | Bien |
| 🧪 METAB | 4 | 5 | Bien |
| 🧠 NEURO | 3 | 5 | Justo, pero deja buen margen al módulo |

Respiratorio era el único desajustado, y por una razón distinta a la que
creíamos: no porque desbalanceara la partida, sino porque **se comía el
contenido de su propia expansión**. Corregido en v0.12 sin borrar ninguna
carta: la **Ventilación Mecánica** (3 copias) perdió su chip 🫁 y quedó
genérica — clínicamente es lo correcto, el ventilador también es del
politrauma, del neurocrítico y del séptico. Con eso el módulo respiratorio
conserva para sí la VMNI, el weaning, la traqueostomía y el prono.

---

## 5. Andamiaje técnico pendiente

Para que esto funcione sin dolor, falta añadir a las herramientas (**no está
hecho todavía**):

- Una columna `set` en los CSV (`base`, `exp-neuro`, `exp-resp`…).
- Que el Taller y el print-and-play filtren por set.
- Que el simulador acepte `--set base` o `--set base+exp-neuro` y verifique
  que un módulo entra sin romper los objetivos de balance.

Son cambios de herramienta, no de cartas: ninguna carta cambia al hacerlo.

---

## 6. Idea rescatada: Novatos y Veteranos (Módulo Experiencia)

Rescatada del Excel histórico (`CARTAAAS.xlsx`), **estacionada a propósito**
para después del playtest de la base.

**La idea original:** el personal existía en dos versiones — *De Turno*
(novato: más copias, sin gracia) y *Vieja Escuela* (veterano: menos copias,
con protección). El ejemplo canónico: **el Kinesiólogo senior era inmune a
Vacaciones y Licencias**. La seniority definía el número de copias y daba
características compartidas por todos los veteranos.

**Por qué no entra en la caja base:**

- Duplica el inventario de 🧑‍⚕️ Personal (cada carta × 2 versiones) y el mazo
  no puede crecer (§1).
- Una inmunidad pasiva apaga cartas de ataque completas (*Vacaciones*,
  *¡Liceeeencia!*) en un mazo donde los ataques ya son escasos: 2 copias de
  cada una en 30 Protocolos.
- Añade una capa de rareza que el balance actual no usa ni necesita.

**Cómo entraría sin romper nada (cuando toque):**

| Regla del módulo | Detalle |
|---|---|
| Reemplazo 1:1 | 4–6 cartas de Personal de la base salen; entran sus pares novato/veterano. El mazo sigue en 63. |
| Veterano | 1 copia, chip ⭐. **Inmune a Acciones que remuevan Personal** (Vacaciones, ¡Liceeeencia!, Seducción de Pasillo). |
| Novato | 2–3 copias, sin protección — y candidato natural a ⚠️ (el interno entusiasta *genera* eventos). |
| Verificación | `tools/simular.py` con la columna `set` (§5) confirma que el reemplazo no mueve el salvamento del rango 55–70%. |

La versión mínima que conserva el alma de la idea: **un solo par por
profesión** (Kine de Turno / Kine Vieja Escuela), no un sistema de rareza
transversal. Si el playtest pide más textura en el Personal, este es el
primer módulo transversal a producir — funciona con cualquier expansión de
sistema porque no toca pacientes ni eventos.

---

## 7. Más allá de la UCI

La idea de llevar el motor a otras profesiones (odontología, rehabilitación,
nutrición, fonoaudiología) **no son expansiones**: son títulos distintos que
comparten motor y no comparten componentes.

Están documentados aparte, en **[`MOTOR.md`](MOTOR.md)** — incluido el
problema que aparece en todas: fuera de la UCI el reloj deja de ser la muerte
y pasa a ser el abandono.
