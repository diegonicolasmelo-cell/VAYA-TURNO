#!/usr/bin/env python3
"""Brief completo para otra IA — docs/BRIEF-IA.md

Un solo archivo autocontenido: qué es el juego, cómo se juega, el tempo, la
especificación física de la carta, la dirección de arte con su bloque de
estilo literal, y las 113 cartas una por una con su encargo de ilustración.

Se genera desde los CSV, así que nunca se desincroniza del juego.

    python3 tools/generar_brief.py
"""

import csv
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SALIDA = os.path.join(RAIZ, "docs", "BRIEF-IA.md")

SIM = {"IMAGEN": "🩻", "FARMACOS": "💊", "PERSONAL": "🧑‍⚕️",
       "PROCEDIMIENTOS": "💉", "COMODIN": "🃏"}
NOMBRE_TIPO = {"IMAGEN": "Imagen", "FARMACOS": "Fármacos", "PERSONAL": "Personal",
               "PROCEDIMIENTOS": "Procedimientos", "COMODIN": "Comodín"}

# Familia de color ambiental por sistema clínico (docs/ARTE.md §2)
AMBIENTE = {
    "RESP":  "teal / azul hospital · #5b9dc4",
    "CARD":  "naranja quemado / rojo ladrillo · #e0705a",
    "NEURO": "púrpura / lavanda oscura · #a184c9",
    "METAB": "verde oliva · #5cb583",
    "QUIR":  "ámbar / mostaza · #c19a4e",
    "":      "teal hospital neutro · #4a8a96",
}
SIS_NOMBRE = {"RESP": "🫁 Respiratorio", "CARD": "🫀 Cardiológico",
              "NEURO": "🧠 Neurológico", "METAB": "🧪 Metabólico",
              "QUIR": "🔪 Quirúrgico", "": "—"}

GRAVEDAD_VISUAL = {
    "I":    "despierto, sentado, molesto o dramático; a lo más una naricera. 30–50 años",
    "II":   "sedado, máscara Venturi o tubo, monitor detrás. 40–70 años",
    "III":  "intubado, sedación profunda, línea arterial, monitor protagonista. 60+",
    "ROJO": "ventilado, varias infusiones corriendo, la escena más extrema del mazo",
}

OBJETIVO = {"ESTE": "este paciente", "MEJOR": "el que mejor va",
            "ESTABLE": "el estabilizado ✅", "ELIGES": "tú eliges",
            "MANO": "tu mano"}

EMOCION_ACCION = {
    "ATAQUE":    "conflicto: dos manos peleando por lo mismo, rivalidad de pasillo",
    "APOYO":     "cooperación: manos que entregan, alguien que llega a ayudar",
    "CAOS":      "desorden: objetos en el aire, todo pasando a la vez",
    "RESPUESTA": "defensa: escudo, freno, el gesto de detener algo en el aire",
    "EXTREMA":   "sacrificio o superstición: el gesto más grande del mazo",
}


def leer(n):
    with open(os.path.join(RAIZ, "cartas", n), encoding="utf-8") as f:
        return list(csv.DictReader(f))


def amb(sistema):
    return AMBIENTE.get(sistema, AMBIENTE[""])


# ─────────────────────────────────────────────────────────── prosa fija ────

CABEZA = """# ¡VAYA TURNO! — Brief completo para IA

> **Este archivo es autocontenido.** Contiene todo lo necesario para entender
> el juego y producir sus ilustraciones sin acceso al repositorio: el
> concepto, las reglas completas, el tempo, la especificación física de la
> carta, la dirección de arte con su bloque de estilo literal, y las 113
> cartas una por una con su encargo de imagen.
>
> Generado desde los datos del juego (`cartas/*.csv`) — versión de reglas
> **v0.21**. Si algo aquí contradice a un documento suelto más viejo, manda
> este archivo.

---

## 0. Instrucciones para el modelo que lea esto

Eres el director de arte de un juego de cartas de mesa en español (Chile).
Tu trabajo es producir **ilustraciones**, no texto de juego ni reglas nuevas.

1. **Lee la §4 antes de dibujar nada.** El estilo ya existe: hay 42
   ilustraciones terminadas que definen la casa (§4.5). No propongas un
   estilo nuevo.
2. **Copia el bloque de estilo de §4.1 literalmente en cada prompt**, y
   agrégale la *familia de color* que la carta indica en §5.
3. **Una carta = una imagen.** Nombra el archivo con el id de la carta:
   `P19.png`, `R31.png`, `A07.png`, `C05.png`, `S01.png`.
4. **Nunca escribas texto del juego dentro del dibujo.** El nombre, los
   números y las reglas los pone la maqueta. Solo se permiten letreros
   ambientales cortos y creíbles dentro de la escena ("UCI", "OXÍGENO",
   "PABELLÓN").
5. **El humor está en la cara y en la situación, nunca en la crueldad.**
   Ver §1.3: hay una línea que no se cruza.
6. Si una carta te parece imposible de ilustrar, dilo y propón una
   alternativa — no la inventes en otro estilo.

---

## 1. El juego

### 1.1 Qué es

**¡VAYA TURNO!** es un juego de cartas competitivo sobre **triage en una
Unidad de Cuidados Intensivos**. Cada jugador dirige una UCI de **3 camas**.
Los pacientes llegan solos y se deterioran solos; los recursos llegan
mezclados y nunca alcanzan. El juego consiste en **elegir a quién salvas**.

- **2 a 4 jugadores** · **30–45 minutos** · **14+**
- Lo escribe un trabajador de la salud chileno. El material clínico es real:
  las complicaciones son las complicaciones que esos procedimientos causan de
  verdad, y los chistes son los del pasillo.
- **No vas a salvarlos a todos.** Eso no es un defecto del juego: es la tesis.

### 1.2 El tono — esto es lo más importante para el arte

Humor **negro, cansado y cariñoso**. No es una parodia del hospital: es el
hospital contado por alguien que lleva doce horas ahí y que quiere a su
equipo. El registro exacto:

- **Cansancio antes que drama.** Ojeras dibujadas, café frío, el pelo
  aplastado por el gorro. La tensión es de turno largo, no de serie de TV.
- **Burocracia como monstruo.** El Sumario Administrativo da más miedo que la
  muerte, y ese chiste es central.
- **Los pacientes tienen dignidad.** Son ridículos por lo que *dicen* y por
  cómo llegaron, no por estar enfermos.
- **El equipo es el héroe silencioso.** Enfermera, TENS, kinesiólogo: se
  dibujan competentes, aunque estén agotados.

### 1.3 La línea que no se cruza

- Nada de sangre gráfica, vísceras, heridas abiertas ni sufrimiento explícito.
- Nada que se burle del paciente por su cuerpo, su peso, su pobreza o su
  origen.
- Nada de muerte representada con realismo. **La muerte en este juego es "el
  Alta Celestial"**, y se dibuja con humor suave (nubes, una cruz de fichas),
  nunca con un cadáver.
- Nada de logos, marcas de medicamentos reales ni nombres de hospitales
  reales.
"""

REGLAS = """
---

## 2. Las reglas, completas y comprimidas

Un artista no necesita jugar, pero sí necesita saber **qué hace cada carta y
por qué importa**, porque eso es lo que la imagen tiene que comunicar en un
segundo.

### 2.1 Componentes

| Componente | Cant. | Qué es |
|---|---:|---|
| **Pacientes** | 26 | Llegan solos. Cada uno pide recursos y tiene vida ❤️ |
| **Recursos** (Mazo de Guardia) | 65 (44 diseños) | 🩻 Imagen · 💊 Fármacos · 🧑‍⚕️ Personal · 💉 Procedimientos · 🃏 Comodín |
| **Protocolos** (Acciones) | 30 (20 diseños) | Mazo aparte. Se compran, no se roban |
| **Personajes** (avatares) | 22 | Uno por jugador, con una habilidad propia |
| **Sumario Administrativo** | 6 (1 diseño) | La maldición. Llega cuando se te muere alguien |

Fichas: ❤️ vida · ✅ estabilizado · ✝️ Alta Celestial · 1 moneda · marcador de
ronda.

### 2.2 El objetivo

Al final de **8 rondas** gana quien tenga más puntos:

```
  + puntos de cada paciente dado de ALTA
  − penalización de cada ✝️ (paciente fallecido)
  − 1 punto por cada cama que dejaste vacía en cada noche
  + 3 si terminas SIN NINGÚN ✝️            "No se me fue nadie"
  + 1 si tus únicos ✝️ fueron los más graves  "Se hizo todo"
```

Los dos bonus no se suman: o lo uno, o lo otro.

### 2.3 Los pacientes: la tabla de precios

| Gravedad | ❤️ | Recursos que pide | Alta | Fallece |
|---|---:|---:|---:|---:|
| **I — Observación** | 7 | 3 | +2 | −1 |
| **II — Grave** | 6 | 5 | +3 | −2 |
| **III — Crítico** | 6 | 8 | +6 | −2 |
| **★ Código Rojo** | 5 | 8 | +8 | −3 |

La regla escondida: `alta + |fallece| = recursos que pide`. Cada punto cuesta
exactamente un recurso. **La vida no es el precio, es el plazo**: 7 ❤️ = siete
rondas para pagar. Por eso el crítico no es caro, es *urgente*.

### 2.4 El turno: cuatro fases (este es el tempo)

Una **ronda** son los turnos de todos. Cada Fin de Guardia **es un día que
pasa**. La partida dura 8 rondas: una guardia completa.

**1 · ENTREGA DE TURNO** — *llegas y te cuentan cómo está la unidad*
- Da de alta a todo paciente que ya tenía ✅ **desde antes de este turno**.
- **Puedes** admitir en cada cama vacía: revelas 2 pacientes, eliges 1. La
  primera carta de la fila de urgencias está siempre **boca arriba** (el
  *Informe de Gestión de Camas*), así decides sabiendo la mitad.
- Robas 4 cartas del Mazo de Guardia.

**2 · EL PASILLO** — *negocias*
- Un solo negocio por turno: **Canje** (botas 2 recursos → robas 2 Protocolos
  y te quedas 1) o **Trueque** con un rival.
- Puedes jugar como máximo **1 Acción**.

**3 · PASE DE VISITA** — *tratas*
- Colocas **hasta 3 recursos** sobre tus pacientes. Los recursos se quedan
  encima de la carta, en abanico: **son su tratamiento, no se gastan**.
- Un recurso de un sistema clínico jugado sobre un paciente del mismo sistema
  **cuenta doble**.
- Paciente con todo lo que pide → ficha **✅**: deja de deteriorarse.

**4 · FIN DE GUARDIA** — *pasa el día*
- Todo paciente sin ✅ **pierde 1 ❤️**.
- A 0 ❤️ recibe el **Alta Celestial**: ✝️, puntos negativos y un Sumario.
- Descartas hasta quedar con 5 cartas.

> **La ventana de sabotaje**, que es el corazón social del juego:
> **estabilizas en un turno y das de alta en el siguiente.** Entre medio pasa
> el turno de todos los demás, y tu paciente terminado está a la vista de
> todos.

### 2.5 Las Complicaciones ⚠️

18 de las 65 cartas de recurso llevan el sello **⚠️** y traen impresa **la
complicación que ese recurso causa de verdad**: el ventilador trae la neumonía
asociada a ventilación mecánica, el catéter la bacteriemia, el antibiótico la
resistencia.

- **Se disparan al COLOCAR la carta**, no al robarla. Tenerla en la mano no
  hace nada: es una decisión de riesgo-beneficio.
- **Todas hacen lo mismo: el paciente señalado pierde 1 ❤️.** Lo que cambia es
  a quién señalan (el 🎯 Objetivo) y cómo se llaman.
- Once de las dieciocho apuntan **al que iba bien** o al que ya tenía su ✅, y
  cuatro **al paciente que acabas de tratar**. Eso es deliberado: lo que se
  complica en una UCI es lo que parecía resuelto, o lo que tú mismo tocaste.

**Las Protecciones 🛡️:** tres cartas de Personal previenen una complicación
con nombre, *si ya estaban puestas antes*. El TENS con la cabecera a 30°
previene la neumonía; la enfermera con manejo estéril previene la bacteriemia;
el kinesiólogo con movilización precoz previene el delirium. Son bundles
reales de UCI, y esa es la mejor parte del juego.

### 2.6 Qué significa "fuerte" en este juego

Para que las imágenes acompañen la potencia de cada carta:

- La moneda real es **la colocación**: tienes 3 por turno, 24 por guardia.
- **1 carta en mano ≈ medio punto.** Un tutor (buscar la carta exacta) vale
  dos cartas.
- Una **Acción** cuesta un Canje ≈ 2 colocaciones ≈ 1 punto de swing. Son
  cartas de momento, no de poder bruto.
- Una **habilidad de avatar** sana vale entre **+0,3 y +1,0 puntos** de
  ventaja. Ninguna gana la partida sola.
"""


def seccion_fisica():
    return """
---

## 3. Especificación física de la carta

- **Formato: 63 × 88 mm** (el estándar de Magic / Mitos y Leyendas / poker).
  Se imprime 9 por hoja Carta y se corta con guillotina.
- La maqueta reserva una **ventana de ilustración de 55,7 mm de ancho**. La
  altura cambia según cuánto texto lleva la carta:

| Tipo de carta | Ventana (ancho × alto) |
|---|---|
| Paciente Gravedad I / II | 55,7 × 32,2 / 28,3 mm |
| Paciente Gravedad III / Código Rojo | 55,7 × 35,5 mm |
| Recurso 🩻 Imagen · 💉 Procedimientos | 55,7 × 61,5 mm |
| Recurso 💊 Fármacos | 55,7 × 57,6 mm |
| Recurso 🧑‍⚕️ Personal | 55,7 × 46,9 mm |
| Recurso 🃏 Comodín | 55,7 × 54,5 mm |
| Acción (según tipo) | 55,7 × 29,6 – 45,2 mm |
| Personaje | 55,7 × 31,8 mm |
| Sumario | 55,7 × 29,6 mm |

> **Cómo resolver esa contradicción, que es la instrucción más importante de
> esta sección.** Las 39 ilustraciones que ya existen son **2:3 vertical a
> sangre completa**, y así hay que seguir generándolas para que todo se vea
> de la misma caja. Pero la ventana más angosta (28,3 mm sobre 55,7 mm de
> ancho) equivale a **la banda central del 34% de la altura** de esa imagen.
>
> Entonces: **genera 2:3 vertical, pero compón para que la cara, el gesto y
> el objeto que identifica la carta vivan en el tercio central**. Lo de
> arriba y lo de abajo es ambiente sacrificable. Una imagen que pone la cara
> arriba se pierde al recortarla.

- **A sangre completa: el fondo llena el rectángulo, nunca blanco.**
- Resolución de entrega: mínimo **1024 × 1536 px** (2:3). PNG.
- Se imprime en casa, muchas veces **en escala de grises**. Comprueba que la
  imagen se lea sin color: necesita contraste de valor, no solo de tono.
"""


def seccion_arte():
    return """
---

## 4. Dirección de arte

### 4.1 El estilo canónico — "Retro de Guardia"

Definido por 42 ilustraciones que ya existen y están terminadas. Sus rasgos,
en orden de importancia:

1. **Línea:** contorno café oscuro **grueso y de ancho uniforme** (ligne
   claire de cartoon moderno). Nada de boceto, nada de línea temblorosa.
2. **Color:** planos, con **cel shading mínimo** de 1–2 tonos. Sin degradados,
   sin acuarela.
3. **La firma de la casa: cada imagen vive en UNA familia de color.** Fondo
   monocromo ambiental y personaje compartiendo la misma temperatura. Es lo
   único que hace que 113 imágenes se vean de la misma caja.
4. **Proporciones:** cabezones (3–4 cabezas), expresiones exageradas, ojeras
   dibujadas. **La comedia está en la cara.**
5. **Ambiente:** UCI reconocible — monitores con curvas, portasueros,
   letreros cortos.
6. **Acabado:** grano sutil de impresión retro, a sangre completa, 2:3.

**Bloque literal — cópialo tal cual en cada prompt:**

```text
[VAYA TURNO HOUSE STYLE]
Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire),
flat colors with minimal 1-2 tone cel shading, subtle vintage print grain.
Exaggerated comic characters: big heads (3-4 heads tall), expressive tired faces,
drawn under-eye circles, anxious hospital humor. Setting: recognizable ICU interior
with patient monitors, IV poles and ambient signage ("ICU", "OXIGENO").
CRITICAL: the whole image lives in ONE monochromatic color family - background and
subject share the same color temperature (see AMBIENT COLOR FAMILY below).
Full-bleed background, never white. No game text, no labels except small ambient signs.
No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
Compose so the face and the identifying object sit in the CENTRAL THIRD of the frame.
AMBIENT COLOR FAMILY: <la que indique la carta en §5>
```

### 4.2 La familia de color, por sistema clínico

| Sistema | Familia ambiental | Ancla |
|---|---|---|
| 🫁 Respiratorio | teal / azul hospital | `#5b9dc4` |
| 🫀 Cardiológico | naranja quemado / rojo ladrillo | `#e0705a` |
| 🧠 Neurológico | púrpura / lavanda oscura | `#a184c9` |
| 🧪 Metabólico | verde oliva | `#5cb583` |
| 🔪 Quirúrgico | ámbar / mostaza | `#c19a4e` |
| Sin sistema (genéricos y avatares) | teal hospital neutro | `#4a8a96` |
| Acciones | libre según la emoción: ataque rojizo, apoyo cálido, caos nocturno | — |

> El sistema clínico es un dato **de juego**: solo 21 de los 65 recursos lo
> llevan, porque sirve para la regla de sinergia. Cuando una carta no lo trae,
> la familia por defecto es el teal neutro — pero si el objeto pertenece
> obviamente a un sistema (un ventilador es respiratorio, aunque su carta no
> lleve chip), puedes inclinarte a esa familia. Lo que no se negocia es que la
> imagen viva en **una sola** familia.

### 4.3 El plano, por tipo de carta

| Tipo | Encuadre | Nota |
|---|---|---|
| **Paciente** | busto frontal, del pecho a la cabeza | luz frontal suave; el monitor va detrás |
| **Recurso** | el objeto casi aislado, 3/4 o frontal, ocupando ~60% | fondo monocromo ambiental, no blanco |
| **Recurso 🧑‍⚕️ Personal** | busto o medio cuerpo de la persona en su gesto de trabajo | son gente, no objetos |
| **Acción** | escena mínima, 1–2 figuras o un elemento en movimiento | la emoción manda sobre el detalle |
| **Personaje** | cuerpo entero, pose característica, ocupando ~70% | es un retrato de arquetipo |
| **Sumario** | un documento con timbres, agigantado por su sombra | burocracia como amenaza |

### 4.4 Las parejas: el mismo objeto, limpio y complicado

Quince recursos existen **dos veces**: una versión limpia y una versión ⚠️ con
complicación. **Deben compartir el objeto y el encuadre**, y diferenciarse
solo en lo que está pasando:

> *Ventilación Mecánica* limpia: el ventilador funcionando, curva estable,
> nadie mirando. *Ventilación Mecánica ⚠️ (Neumonía Asociada a VM)*: el mismo
> ventilador, mismo ángulo, pero lleva ocho días ahí — secreciones en el
> tubo, alguien con cara de "otra vez".

Esa repetición con variación es el mejor recurso narrativo del mazo. Las
quince parejas están marcadas en §5.2.

### 4.5 Las anclas visuales — mándalas junto con este archivo

Existen **18 ilustraciones ya mapeadas a cartas** (`arte/raw/`) y **24 escenas
más** en el mismo estilo (`arte/raw/extra/`), más 2 referencias de maqueta en
`arte/referencias/`. Para una IA de imagen, **una referencia visual vale más que
tres párrafos de descripción**: manda 2 o 3 de estas junto con este archivo y
pídele que las use como referencia de estilo (image-to-image o "match this
style").

Las tres que mejor cubren el rango:

| Archivo | Qué ancla |
|---|---|
| `arte/raw/C01-diostor.jpg` | personaje, teal, aureola — el arquetipo cómico |
| `arte/raw/R29-carro-de-paro.jpg` | escena con objeto y movimiento |
| `arte/raw/R34-enfermera-de-uci.jpg` | el equipo: competente y cansado a la vez |

Y dos que sirven de contexto, no de estilo:
`arte/referencias/plantilla-carta.jpg` (cómo se arma la carta) y
`arte/referencias/tablero-uci.jpg`.

> Ojo con una: `arte/raw/A20-muestra-hemolizada.jpg` está mal mapeada. A20 es
> la Acción *Hay Que Repetirlo*; *Muestra Hemolizada* es la complicación del
> recurso **R33**. Renómbrala antes de usarla como referencia de esa carta.

### 4.6 Entrega

- Un archivo por carta, nombrado con su id: `P01.png` … `R45.png` …
  `A01.png` … `C01.png` … `S01.png`.
- PNG, 2:3, mínimo 1024 × 1536.
- Si generas hojas de contacto para iterar, entrégalas aparte y recortadas al
  final.
- **Orden sugerido:** primero los 22 personajes (fijan el estilo de las
  caras), después los 26 pacientes (son los que más se miran en mesa),
  después los recursos, y al final Acciones y Sumario.
"""


# ─────────────────────────────────────────────────────── bloques de cartas ──

def tabla_pacientes():
    pac = leer("pacientes.csv")
    filas = []
    for p in pac:
        pide = " ".join(f"{SIM[t]}{p[c]}" for t, c in
                        (("IMAGEN", "img"), ("FARMACOS", "far"),
                         ("PERSONAL", "per"), ("PROCEDIMIENTOS", "proc"))
                        if int(p[c]) > 0)
        filas.append(
            f'| **{p["id"]}** | {p["nombre"]} | {p["gravedad"]} · '
            f'{SIS_NOMBRE.get(p["sistema"], p["sistema"])} | ❤️{p["vida"]} · '
            f'pide {pide} | {amb(p["sistema"])} | *{p["frase"]}* |')
    cuerpo = "\n".join(filas)
    grav = "\n".join(f"- **Gravedad {k}:** {v}" for k, v in GRAVEDAD_VISUAL.items())
    return f"""
### 5.1 Pacientes ({len(pac)} cartas)

**Plano:** busto frontal, del pecho a la cabeza. Luz frontal suave. El monitor
y el portasueros van detrás, desenfocados por simplificación, no por foco.

**El estado clínico lo marca la gravedad:**

{grav}

**La frase de la carta es la dirección de escena.** Es el chiste, y casi
siempre dice exactamente qué expresión hay que dibujar. Úsala como brief.

| id | Carta | Gravedad · sistema | Ficha | Familia de color | La frase = la escena |
|---|---|---|---|---|---|
{cuerpo}
"""


def tabla_recursos():
    rec = leer("recursos.csv")
    from collections import Counter
    veces = Counter(r["nombre"] for r in rec)
    filas = []
    for r in rec:
        par = "🔁 pareja" if veces[r["nombre"]] > 1 else ""
        if r["complicacion"] == "si":
            que = (f'⚠️ **{r["comp_nombre"]}** → 🎯 {OBJETIVO.get(r["comp_objetivo"], "")} '
                   f'pierde 1 ❤️')
        elif r["previene"]:
            que = f'🛡️ previene *{r["previene"]}*'
        elif r["comodin"] == "si":
            que = "🃏 vale por cualquier tipo"
        else:
            que = "—"
        filas.append(
            f'| **{r["id"]}** | {r["nombre"]} | {SIM.get(r["tipo"], "")} '
            f'{NOMBRE_TIPO.get(r["tipo"], r["tipo"])} | {que} | {par} | '
            f'{amb(r["sistema"])} | *{r["frase"]}* |')
    cuerpo = "\n".join(filas)
    copias = sum(int(r["copias"]) for r in rec)
    return f"""
### 5.2 Recursos — el Mazo de Guardia ({len(rec)} diseños, {copias} cartas)

**Plano:** el objeto casi aislado, 3/4 o frontal, ocupando ~60% del cuadro,
sobre fondo monocromo ambiental. **Excepción: los recursos 🧑‍⚕️ Personal son
personas** — busto o medio cuerpo, en su gesto de trabajo, con la misma
dignidad cansada del resto del equipo.

Las marcadas **🔁 pareja** comparten objeto y encuadre con su gemela: una
limpia y una ⚠️ (ver §4.4).

| id | Carta | Tipo | Qué hace | Par | Familia de color | La frase = la escena |
|---|---|---|---|---|---|---|
{cuerpo}
"""


def tabla_acciones():
    acc = leer("acciones.csv")
    filas = []
    for a in acc:
        filas.append(
            f'| **{a["id"]}** | {a["nombre"]} | {a["tipo"]} | {a["texto"]} | '
            f'*{a["frase"]}* |')
    cuerpo = "\n".join(filas)
    emo = "\n".join(f"- **{k}:** {v}" for k, v in EMOCION_ACCION.items())
    copias = sum(int(a["copias"]) for a in acc)
    return f"""
### 5.3 Protocolos — las Acciones ({len(acc)} diseños, {copias} cartas)

**Plano:** escena mínima, una o dos figuras o un elemento en movimiento. Aquí
la paleta se suelta: las Acciones no tienen sistema clínico, así que pueden
usar un rango más amplio para distinguirse de pacientes y recursos.

{emo}

| id | Carta | Tipo | Qué hace | La frase = la escena |
|---|---|---|---|---|
{cuerpo}
"""


def tabla_personajes():
    per = leer("personajes.csv")
    filas = []
    for c in per:
        filas.append(
            f'| **{c["id"]}** | {c["nombre"]} | {c["frecuencia"]} | '
            f'{c["habilidad"]} | *{c["frase"]}* |')
    cuerpo = "\n".join(filas)
    return f"""
### 5.4 Personajes — los avatares ({len(per)} cartas)

**Plano:** cuerpo entero, pose característica, ocupando ~70% del cuadro.
Familia de color: **teal hospital neutro `#4a8a96`**, salvo que el personaje
pida otra cosa (el Esotérico y la Enfermera de Noche admiten nocturno).

Estos son los primeros que hay que dibujar: fijan cómo se ven las caras del
juego. Cada uno es un arquetipo que cualquiera que haya trabajado en un
hospital reconoce al tiro — **la habilidad dice qué hace y la frase dice cómo
es**. Dibuja la personalidad, no el uniforme.

| id | Avatar | Frecuencia | Habilidad | La frase = la escena |
|---|---|---|---|---|
{cuerpo}
"""


def tabla_sumario():
    sm = leer("sumarios.csv")
    filas = [f'| **{s["id"]}** | {s["nombre"]} | {s["texto"]} | *{s["frase"]}* |'
             for s in sm]
    return f"""
### 5.5 El Sumario Administrativo (1 diseño, 6 cartas)

La única carta que no se juega: te llega. **Es el mejor chiste del juego** y
la carta que más miedo tiene que dar — más que la muerte, que en este juego se
llama "Alta Celestial" y se dibuja con humor suave.

| id | Carta | Qué hace | La frase = la escena |
|---|---|---|---|
{filas[0]}
"""


CIERRE = """
---

## 6. Resumen para el que va a dibujar

0. **Pide las imágenes de referencia** (§4.5) antes de empezar. Con este
   archivo solo tienes las palabras; con dos o tres anclas tienes el estilo.
1. **El estilo ya existe** (§4.1): línea gruesa uniforme, color plano, una
   sola familia de color por imagen, cabezones cansados, a sangre completa.
2. **Compón para el tercio central** (§3): la maqueta recorta.
3. **La frase de cada carta es el brief de escena.** Está en la columna
   final de todas las tablas de §5.
4. **Los pacientes tienen dignidad; el ridículo es de la situación** (§1.3).
5. **Nombra los archivos con el id de la carta.**
6. **Empieza por los 22 personajes**, que fijan las caras.

Total del encargo: **113 ilustraciones** — 26 pacientes, 44 recursos, 20
Acciones, 22 personajes, 1 Sumario.
"""


def main():
    partes = [CABEZA, REGLAS, seccion_fisica(), seccion_arte(),
              "\n---\n\n## 5. Las 113 cartas, una por una\n",
              tabla_pacientes(), tabla_recursos(), tabla_acciones(),
              tabla_personajes(), tabla_sumario(), CIERRE]
    doc = "".join(partes)
    with open(SALIDA, "w", encoding="utf-8") as f:
        f.write(doc)
    n = sum(len(leer(x)) for x in ("pacientes.csv", "recursos.csv",
                                   "acciones.csv", "personajes.csv",
                                   "sumarios.csv"))
    palabras = len(doc.split())
    print(f"✔ Brief con {n} cartas · {palabras:,} palabras · "
          f"{len(doc) // 1024} KB → {SALIDA}")


if __name__ == "__main__":
    main()
