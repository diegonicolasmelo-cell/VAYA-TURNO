# La economía de ¡VAYA TURNO! — cómo se tasa una carta

> El "maná" de este juego existe desde siempre; este documento solo lo pone
> por escrito. Toda carta nueva —paciente, recurso, Acción, habilidad— se
> tasa con estas reglas ANTES de medirla en el simulador. La medición
> confirma; la fórmula diseña.

---

## 1. La moneda base

En Hearthstone la moneda es el maná; en Pokémon, las energías. Acá la moneda
es **la colocación**: el derecho a poner 1 recurso sobre un paciente. Con
robo 4 y tope 3, tienes **3 colocaciones por turno y 24 por guardia**. Todo
lo demás se convierte a esa moneda:

| Cosa | Vale | De dónde sale |
|---|---|---|
| 1 recurso colocado donde se pide | **1 colocación** | por definición |
| 1 recurso con sinergia en su sistema | **2 colocaciones** | cuenta doble |
| 1 carta en mano | **≈ ½ punto** | medido: cada carta extra rinde +0,5 pts (§4h de DISENO) |
| 1 punto de puntaje | **≈ 2 cartas** | inverso de lo anterior |
| 1 Sumario | ≈ 1 punto | −1 de mano + 2 cartas para cerrarlo |
| 1 cama vacía por noche | **1 punto exacto** | regla v0.20 |

**La regla de oro que salió de medir 22 avatares:** en esta economía no hay
"robo modesto". Una carta aleatoria tapa hueco la mitad de las veces; una
carta buscada lo tapa siempre — **un tutor vale dos cartas**. Por eso
cualquier efecto repetible de "roba 1" está prohibido en cartas y sólo puede
existir 1×PARTIDA o con gatillo que controle el rival.

---

## 2. Cómo se tasa un PACIENTE

La fórmula está impresa en los 26 y es exacta:

```
    alta + |fallece|  =  recursos que pide
```

| Gravedad | vida | pide | alta | fallece | swing total |
|---|---:|---:|---:|---:|---:|
| I | 7 | 3 | +2 | −1 | 3 = 3 ✓ |
| II | 6 | 5 | +3 | −2 | 5 = 5 ✓ |
| III | **6** | **8** | **+6** | −2 | 8 = 8 ✓ |
| ROJO | 5 | 8 | +8 | −3 | **11 > 8** |

**Léela como el precio de la energía en Pokémon:** el que pega 130 pide 3
energías. Acá, cada punto de swing (lo que ganas por salvarlo más lo que
evitas por no perderlo) cuesta exactamente 1 recurso. El jugador nunca
compra puntos baratos: compra riesgo.

La **vida** es el plazo del crédito, no el precio: 7 ❤️ = "tienes 7 rondas
para pagar", 5 ❤️ = "tienes 5". Por eso el GIII es difícil sin ser caro: mismo
precio por punto, menos plazo.

> **La fórmula se ganó el sueldo en v0.21.** Al unificar las complicaciones a
> "−1 ❤️" el Gravedad III se hundió de 41% a 37% de salvamento: quitar vida es
> un **impuesto regresivo**, y él es quien menos plazo tenía y más cartas
> recibe. Darle 6 ❤️ a secas lo disparó a 52% —el plazo iba gratis—; darle
> 6 ❤️ **pagando un requisito más** (y por tanto un alta de +6, que es lo que
> la fórmula obliga) lo dejó en 40–44%, dentro de banda. El precio no se
> adivina cuando ya está escrito.

**El ROJO es la única carta con prima (11 de swing por 8 de precio)** — un
sobrepago deliberado del 37% por aceptar el peor plazo del juego con el
requisito más ancho. Es la carta aspiracional: se tasa para que intentarlo
sea correcto una vez por guardia, no siempre.

**Para crear un paciente nuevo:** elige gravedad → copia vida y total de la
tabla → reparte el total entre los 4 tipos (ancho = más fácil, concentrado =
más difícil, sin tocar el precio) → alta y fallece salen solos de la fórmula.
Si quieres una prima tipo ROJO, decláralo y mídelo.

---

## 3. Cómo se tasa un RECURSO

Un recurso vale 1. Los modificadores:

| Modificador | Ajuste | Compensación en el mazo |
|---|---|---|
| Sinergia (cuenta ×2 en su sistema) | vale hasta 2 | menos copias (1–2 por diseño) |
| ⚠️ Complicación | **impuesto fijo al colocar** | desde v0.21 **siempre −1 ❤️** al paciente que señala su 🎯. Un impuesto conocido y constante: por eso se puede tasar |
| 🛡️ PREVIENE | +valor condicional | solo en Personal, solo 1 complicación con nombre, prospectivo |
| Comodín | flexibilidad total, nunca dobla | 3 copias en todo el mazo |
| Restricción (TAC exige 🧑‍⚕️) | descuento | permite más copias |

La ⚠️ y el recurso se anulan aproximadamente (+1 colocación por −1 ❤️ de
complicación): por eso la carta ⚠️ es una **decisión** y no basura ni premio.

**La regla de v0.21 que ordenó todo esto: el azar impuesto debe ser
confiable; el azar elegido puede ser variado.** Una ⚠️ no la eliges —viene
pegada a un recurso que necesitas—, así que tiene que significar algo el 100%
de las veces: de ahí que las dieciocho hagan lo mismo y la variedad viva en el
nombre, el dibujo y el 🎯. Un Protocolo sí lo eliges y lo pagas con un Canje:
ahí la variedad es el producto, y son 30 efectos distintos a propósito.

---

## 4. Cómo se tasa una ACCIÓN

Una Acción cuesta, vía Canje: **2 recursos + el cupo del Negocio + el azar de
2-elige-1**. En moneda: ≈ 2 colocaciones. Entonces:

> **Una Acción debe producir un swing de ~2 colocaciones (≈ 1 punto), con
> varianza permitida hacia ambos lados.**

Ejemplos ya impresos, tasados con esa vara:

| Acción | Swing | Veredicto |
|---|---|---|
| *Vacaciones* (descarta 1 🧑‍⚕️ rival) | −1 rival ≈ +1 tuyo... más romper un ✅ | justa: brilla con timing |
| *Reunión Clínica* (mueve 3 recursos tuyos) | 0 en cartas, hasta +3 en eficiencia | justa: paga en habilidad |
| *Doblo Turno* (roba 3, luego −2) | +1 carta neta + tempo | justa |
| *Receta en Blanco* (busca 1 recurso) | tutor = 2 cartas | **justa SOLO porque cuesta un Canje**; jamás gratis |
| *Anda Rondando la Pelada* | enorme, 50% de perder la mano | prima de varianza tipo ROJO |

**Para crear una Acción nueva:** estima su swing en colocaciones. 2 = precio
justo. 3+ = necesita costo extra (descarte, moneda, condición). 1 = agrégale
cadencia ("y roba 1 Protocolo") o hazla RESPUESTA.

---

## 5. Cómo se tasa una HABILIDAD de avatar

Medido en `DISENO.md` §4h con el método §4b. La banda: **+0,3 a +1,0 puntos**
de ventaja sobre rivales en la misma mesa.

Conversiones útiles (todas medidas):

- 1×PARTIDA "salva una vida" ≈ +0,3
- 1×PARTIDA con descarte de 2 ≈ +0,7
- Pasiva de filtro (calidad sin cantidad) ≈ +0,5
- +1 carta seca al inicio ≈ +1,1 (el techo)
- **Robo repetible = +1,8 a +8,5 = prohibido**

---

## 6. Las tres restricciones que no se negocian

1. **El reloj no se compra.** Ninguna carta puede dar ❤️ ni detener el
   deterioro fuera del ✅ (la única excepción tasada: la Enfermera de Noche,
   1×PARTIDA, pagando 2 cartas). El día pasa para todos: es la tesis.
2. **El robo repetible está prohibido** (§1). En cartas, recursos y avatares.
3. **La oferta sigue a la demanda.** Los cuatro tipos mantienen ratio
   oferta/demanda 0,45 ± 0,01. Si agregas pacientes, recalcula el mazo
   (`DISENO.md`, tabla de oferta vs demanda) — el desbalance silencioso entre
   tipos es el error que no se ve en mesa hasta la partida 20.

---

*Cambios v0.21 tasados con estas reglas: la ⚠️ unificada a −1 ❤️ (impuesto
fijo, medido en `DISENO.md` §4j), el Gravedad III re-tasado con la fórmula de
§2, y +2 copias de recurso (Hemoderivados 💊, Reanimación 💉) para sostener la
tercera restricción cuando la demanda subió de 132 a 138 — el mazo de Guardia
pasó de 63 a 65 cartas.*

*Cambios v0.20 tasados con estas reglas: tope 3 (define la moneda), admisión
opcional a −1/noche (pone precio a la cama, mata la tortuga: −2,6 vs 6,0
medido), Canje 2-elige-1 (reduce el azar sin tocar el precio), protecciones 🛡️
(valor condicional, gratis porque exigen secuencia correcta).*
