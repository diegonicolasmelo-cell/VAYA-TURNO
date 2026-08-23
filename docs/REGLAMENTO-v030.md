# ¡VAYA TURNO! — Reglamento v0.30 (rama experimental)

> **Qué es esto.** El rediseño de agosto 2026: sabotaje con recursos ⚠️,
> Pizarra de Turno, admisión obligatoria y complicación unificada "donde se
> ubica". Usa los mazos de `cartas/v030/` (recursos, acciones y logros
> propios; pacientes, personajes y sumarios se comparten con la base).
>
> **La v0.21 (`REGLAMENTO.md`) sigue siendo la versión estable e imprimible.**
> Esta rama existe para probarse en mesa. Suelo medido con
> `tools/simular_v030.py`: salvamento 64% · 2,9 altas · 1,6 fallecidos ·
> Gravedad III 41% — en banda, salvo "No se me fue nadie" (2,6%), que en un
> mundo con sabotaje se vuelve casi mítico. Ver §9.

Juego para **2–4 jugadores** · **30–45 min** · **14+**.

---

## 1. La idea en 30 segundos

Cada jugador dirige una UCI de **3 camas**. Los pacientes llegan solos, se
deterioran solos, y los recursos nunca alcanzan. Lo nuevo de esta rama: los
recursos con ⚠️ son **de doble filo** — sobre tu paciente son tratamiento
(con su complicación incluida), sobre un paciente rival son **sabotaje**.
La misma carta, dos usos. Tú decides qué eres esta noche.

---

## 2. Componentes

| Componente | Cant. | Nota |
|---|---:|---|
| Cartas de **Paciente** | 26 | Las mismas de la base (Gravedad III: 6 ❤️ · pide 8 · +6/−2) |
| Cartas de **Recurso** | 67 (44 diseños) | `cartas/v030/recursos.csv` · **22 llevan ⚠️** |
| Cartas de **Protocolo** (Acciones) | 31 (21 diseños) | Con **coste impreso 1–3**. Se compran en la Pizarra |
| Cartas de **Personaje** | 22 | Las de la base (adaptaciones en §8) |
| Cartas de **Logro** | 3 | *¡Durante Mi Guardia No!* · *Se Hizo Todo* · *Auditoría del Ministerio* |
| **Sumario Administrativo** | 6 | Ahora vive **boca arriba en tu zona**, no en la mano |

Fichas: ❤️ vida · ✅ estabilizado · ✝️ cruces · 1 moneda · marcador de ronda.

## 3. Preparación

1. Cada jugador recibe **2 avatares, elige 1** y devuelve el otro.
2. Baraja el Mazo de Pacientes. Cada jugador **recibe 2 pacientes al azar**
   — la tercera cama parte vacía. Da vuelta la primera carta del mazo:
   es el **Informe de Gestión de Camas** y queda boca arriba toda la partida.
3. Baraja el **Mazo de Guardia** (67 recursos) y el **Mazo de Protocolos**.
   Revela las **3 primeras cartas de Protocolos**: esa fila es la
   **Pizarra de Turno**.
4. Pon al centro las 3 cartas de **Logro** y los 6 **Sumarios**.
5. Cada jugador roba **4 cartas**. Empieza quien haya hecho el turno de
   noche más reciente.

**Ajuste por jugadores:** 2–3 jug: 3 camas · roba 4 · 8 rondas. 4 jug:
2 camas · roba 3 · 10 rondas.

---

## 4. El turno — cuatro fases

### 4.1 Entrega de Turno

**a) Altas.** Todo paciente tuyo con ✅ **desde antes de este turno** se va
de alta… **salvo que tenga basura clínica encima** (§6.3): nadie se va con
papeleo pendiente. Guarda la carta en tu pila de puntos; sus recursos van
al descarte.

**b) Admisión — OBLIGATORIA.** Por cada cama vacía **debes** admitir:
revela 2 pacientes (el Informe boca arriba es uno de ellos), elige 1, el
otro va al fondo. Da vuelta el nuevo Informe.

**c) Robo.** Roba **4 cartas** del Mazo de Guardia (3 en partidas de 4).
Robar una ⚠️ no hace nada: es munición o tratamiento, según dónde la pongas.

### 4.2 El Pasillo — la Pizarra de Turno

Puedes **comprar 1 Protocolo** de la Pizarra pagando su **coste impreso**:
descarta esa cantidad de cartas de tu mano (1, 2 o 3). Repón la Pizarra de
inmediato. Puedes jugar la Acción ahora o guardarla.

- Máximo **1 compra** y **1 Acción jugada** por turno (las RESPUESTA 🛡️ se
  juegan fuera de turno y no cuentan).
- **Limpieza de Pizarra:** si no compras nada, puedes descartar las 3 cartas
  de la Pizarra y revelar 3 nuevas. Gasta tu compra del turno.

> El Canje y el Trueque de la v0.21 no existen en esta rama: la Pizarra los
> reemplaza.

### 4.3 Pase de Visita — 3 colocaciones

Tienes **3 colocaciones** y un menú. Cada línea cuesta 1 colocación:

| Opción | Qué haces |
|---|---|
| **Tratar** | Coloca un recurso de tu mano sobre un paciente **tuyo**. Si trae ⚠️, resuélvela (§6.1) |
| **Sabotear** | Coloca un recurso **⚠️** sobre un paciente **rival** (§6.2) |
| **Des-escalar** | Retira 1 **basura clínica** de un paciente tuyo y descártala |
| **Cerrar Sumario** | Además de la colocación, descarta **2 cartas** de tu mano |

La sinergia sigue igual: recurso con sistema sobre paciente del mismo
sistema **cuenta doble**. Paciente completo (y sin bloqueo) → ficha **✅**:
deja de deteriorarse. La regla de la ventana no cambia: **estabilizas en un
turno, das de alta al siguiente.**

### 4.4 Fin de Guardia

1. Todo paciente tuyo **sin ✅ pierde 1 ❤️**.
2. A 0 ❤️: **Alta Celestial** — ✝️, penalización, y toma un **Sumario**
   del centro, boca arriba en tu zona.
3. Descarta hasta quedar con **5 cartas**. (El Sumario ya no reduce tu
   mano: ahora es papeleo sobre la mesa, a la vista de todos.)

---

## 5. El Sumario Administrativo (v0.30)

Vive **boca arriba en tu zona** — todos ven cuántos debes. Cerrar uno
cuesta **1 colocación + 2 cartas** en tu Pase de Visita, nunca el mismo
turno en que llegó. Al final de la partida, el jugador con **más Sumarios
abiertos** recibe la **Auditoría del Ministerio: −3 puntos** (empate: nadie
la recibe).

---

## 6. Las Complicaciones ⚠️ — una regla, dos filos

**Toda ⚠️ hace lo mismo: el paciente DONDE SE UBICA la carta pierde 1 ❤️,
al colocarla.** No hay 🎯 impreso: la víctima la decide la colocación. El
nombre y el dibujo son la sazón; la regla es una sola.

### 6.1 Sobre tu propio paciente

El recurso cuenta para su receta **y** el paciente pierde 1 ❤️ (una ⚠️
propia **sí puede matarlo** — ese riesgo es tuyo). La pregunta de siempre:
*¿lo necesito lo suficiente como para aceptar lo que trae?*

### 6.2 Sobre un paciente rival (sabotaje)

- La complicación se resuelve: **pierde 1 ❤️**, pero un recurso rival
  **nunca quita el último ❤️** (si lo dejaría en 0, queda en 1).
- **Si el tipo de la carta es algo que ese paciente pide, cuenta para su
  receta** — le regalaste tratamiento a cambio del golpe. Por eso el
  sabotaje fino se hace con tipos que **no** pide.
- Máximo **1 sabotaje por paciente rival por ronda**.

### 6.3 La basura clínica

Un recurso rival que el paciente **no pide** se queda sobre él **girado
180°**: es *basura clínica*. No cuenta para nada, pero **el paciente no
puede irse de alta mientras tenga basura encima** — se estabiliza igual
(el ✅ detiene el reloj), pero el alta espera el papeleo. Se limpia con la
**Des-escalada** (1 colocación por carta).

### 6.4 Las Protecciones 🛡️ PREVIENE

Igual que en la base, y ahora también son **defensa antisabotaje**: si el
protector ya estaba sobre el paciente, la complicación nombrada no ocurre
— ni la tuya ni la que te tire un rival. Enfermera de UCI ⇒ *Bacteriemia
por Catéter* · Técnico en Enfermería ⇒ *Neumonía Asociada a VM* ·
Kinesiólogo Respiratorio ⇒ *Delirium en UCI*. La prevención es prospectiva
y viaja con la carta.

### 6.5 Los dobles filos con texto 🛡️ propio

Cuatro cartas de Personal traen, además de su ⚠️, un beneficio que **solo
funciona sobre tus pacientes**:

| Carta | ⚠️ (donde se ubica) | 🛡️ (solo sobre lo tuyo) |
|---|---|---|
| **Cirujano de Turno** | Oblito Quirúrgico: −1 ❤️ | Cuenta como **2 recursos 🧑‍⚕️** en cualquier paciente |
| **Pabellón** | Pabellón Suspendido: −1 ❤️ | Mueve gratis 1 recurso entre tus pacientes |
| **Becado de Medicina** | Aún Estoy Aprendiendo: −1 ❤️ | Busca 1 Protocolo en el descarte de Protocolos y tómalo |
| **Personal de Turno Extra** | El Turno Veinticuatro: −1 ❤️ **y el jefe de esa unidad descarta 1 carta** | — (nació para el sabotaje) |

---

## 7. Fin de la partida y puntuación

Tras la **ronda 8**:

```
  + puntos de cada paciente en tu pila de ALTAS
  − penalización de cada ✝️
  − 1 por cada cama vacía al final (solo pasa si se agotó Urgencias)
  − 3 la Auditoría del Ministerio (el que tenga MÁS Sumarios abiertos)
  + 3 ¡Durante Mi Guardia No!  (ningún ✝️)
  + 1 Se Hizo Todo             (tus únicos ✝️ fueron III o ROJO)
```

Los dos logros positivos no se acumulan. Desempates: menos ✝️, luego más
altas de III/ROJO.

---

## 8. Los avatares en esta rama

Los 22 personajes se usan igual. Tres habilidades nombran mecánicas que
esta rama reemplazó — léelas así:

| Avatar | Decía | En v0.30 se lee |
|---|---|---|
| **La de Abastecimiento** (C09) | tus Canjes cuestan 1 recurso en vez de 2 | tus compras en la Pizarra cuestan **1 carta menos** (mínimo 1) |
| **La Enfermera de IAAS** (C12) | cada 3 ⚠️ resueltas en tu unidad, roba 1 Protocolo | igual, pero cuentan las ⚠️ resueltas **sobre tus pacientes** (propias o sabotaje recibido) — toma gratis la carta más barata de la Pizarra |
| **El Diostor** (C01) | pásale la complicación al de la derecha | al **tratar** con una ⚠️ propia, puedes resolver su −1 ❤️ sobre un paciente del jugador de tu derecha (piso 1 ❤️) |

---

## 9. Lo que la simulación ya dijo de esta rama

- **Atacar paga sin dominar:** +0,89 puntos netos el jugador que sabotea
  contra uno que no (medido con ~1,4 sabotajes por guardia). Está en la
  banda sana de una habilidad — el sabotaje es una herramienta, no la
  estrategia obligatoria.
- **El precio de la interacción:** el salvamento baja de 70% (nadie ataca)
  a 64% (todos atacan). Las muertes extra no vienen del golpe directo — el
  piso de 1 ❤️ lo impide — sino del **tempo**: cada −1 y cada limpieza
  atrasan un ✅ y el deterioro remata.
- **"No se me fue nadie" queda casi mítico (2,6%).** En un mundo donde te
  sabotean, la guardia limpia ya no es una hazaña: es un milagro. Si la
  mesa lo confirma, candidatos: dejarlo como logro-leyenda, o cambiarlo por
  "termina con 1 ✝️ o menos: +2". **Decidir en playtest, no antes.**
- La IA de referencia **prefiere la copia limpia y no remata a su propio
  paciente** con una ⚠️ (no la coloca sobre camas a 1 ❤️). Sin ese juicio,
  el juego mide 61% de salvamento — jugar bien la carta sucia es parte del
  oficio de esta rama.
