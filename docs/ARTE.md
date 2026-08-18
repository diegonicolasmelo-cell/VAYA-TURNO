# Motor de Ilustraciones · ¡VAYA TURNO! v2

> **v2 (2026-08-18):** el estilo canónico ya no es una propuesta — **existe**.
> Se recuperaron del Drive del autor 39 ilustraciones finales + ~180 escenas
> en un estilo consistente (ver §2). Las utilizables ya viven en `arte/raw/`
> mapeadas a IDs de carta. Este documento quedó actualizado a ese estilo;
> la propuesta anterior (pen-and-ink + acuarela) queda descartada.

## Visión General

124 ilustraciones (26 pacientes + 43 recursos + 28 eventos + 6 personajes + 20 acciones + 1 sumario) con **coherencia visual y temática**. Cada ilustración refuerza la narrativa del juego: hospital real, tensión médica, humor amargo, recursos concretos.

**Objetivos:**
- Paleta de colores consistente heredada del Taller de Guardia
- Estilo visual único: sketch médico moderno (líneas claras, colores satinados, fondo blanco)
- Planos fijos por tipo de carta (busto, objeto, cuerpo entero, gesto)
- Herramientas de reproducibilidad: bloque de estilo literal, hojas de contacto, normalización batch

---

## 1. Paleta de Colores

Heredada del Taller de Guardia (CSS `--color-sistema`):

### Sistemas Clínicos (5 colores)

| Sistema | Dark | Light | Uso |
|---------|------|-------|-----|
| RESPIRATORIO 🫁 | `#3d7ea6` | `#5b9dc4` | Pacientes/recursos Resp, texto badges |
| CARDIOLOGÍA ❤️ | `#b03d29` | `#e0705a` | Pacientes/recursos Card, texto crítico |
| NEUROLOGÍA 🧠 | `#7a5ba6` | `#a184c9` | Pacientes/recursos Neuro, texto aviso |
| METABOLISMO 🔬 | `#2f8f6b` | `#5cb583` | Pacientes/recursos Metab, texto ok |
| QUIRÓFANO 🏥 | `#8a6a2f` | `#c19a4e` | Pacientes/recursos Quir, texto neutro |

### Estados de Balance

| Estado | Dark | Light | Significado |
|--------|------|-------|------------|
| ✅ OK | `#2f8f6b` | `#5cb583` | Balance saludable, sinergia presente |
| ⚠️ ALERTA | `#b8801a` | `#dda43c` | Disparidad detectada, requiere ajuste |
| ❌ MAL | `#b03d29` | `#e0705a` | Desequilibrio crítico, rotura probable |

**En ilustraciones:** Usa los colores `Light` como referencia (son los que ven los usuarios en pantalla clara). Los colores deben ser reconocibles en ambos modos, pero la saturación prioriza pantalla clara.

---

## 2. El Estilo Canónico ("Retro de Guardia") y su Bloque Literal

Definido por las 39 ilustraciones finales del autor (en `arte/raw/` y
`arte/raw/extra/`). Sus rasgos, en orden de importancia:

1. **Línea:** contorno negro/marrón oscuro **grueso y de ancho uniforme**
   (ligne claire de cartoon moderno). Nada de boceto ni línea temblorosa.
2. **Color:** planos con **cel shading mínimo** (1–2 tonos de sombra). Sin
   degradados, sin acuarela.
3. **La firma: cada imagen vive en UNA familia de color.** Fondo monocromo
   ambiental y personaje compartiendo la misma temperatura (el DIOSTOR es
   teal con aureola dorada; la Oxigenoterapia es toda verde). Es lo que hace
   que 220 imágenes se vean "de la misma caja".
4. **Proporciones:** cabezones (3–4 cabezas), expresiones exageradas: ceños,
   ojeras dibujadas, sonrisas de ansiedad. La comedia está en la cara.
5. **Ambiente:** UCI reconocible — monitores con curvas, portasueros,
   letreros ambientales ("ICU", "OXÍGENO", "NURSE STATION"). Sin texto de
   juego dentro del dibujo.
6. **Acabado:** grano sutil de impresión retro, bordes limpios, full-bleed
   (el fondo llena la carta — **nunca blanco**). Formato 2:3 vertical.

### Bloque literal (copia-pega en cada prompt)

```
[VAYA TURNO HOUSE STYLE — copiar tal cual]

Modern retro cartoon illustration, thick uniform dark-brown outlines (ligne claire),
flat colors with minimal 1-2 tone cel shading, subtle vintage print grain.
Exaggerated comic characters: big heads (3-4 heads tall), expressive tired faces,
drawn under-eye circles, anxious hospital humor. Setting: recognizable ICU interior
with patient monitors, IV poles and ambient signage ("ICU", "OXIGENO").
CRITICAL: the whole image lives in ONE monochromatic color family — background and
subject share the same color temperature (use the ambient color specified below).
Full-bleed background, never white. No game text, no labels except small ambient signs.
No photorealism, no watercolor, no gradients. Aspect ratio 2:3 portrait.
AMBIENT COLOR FAMILY: {color según el sistema clínico — ver tabla}
```

### Familia de color ambiental por sistema

La paleta del Taller, aplicada como monocromo ambiental:

| Sistema / uso | Familia ambiental | Ancla hex |
|---|---|---|
| 🫁 RESP | Teal / azul hospital | `#5b9dc4` |
| 🫀 CARD | Naranja quemado / rojo ladrillo | `#e0705a` |
| 🧠 NEURO | Púrpura / lavanda oscura | `#a184c9` |
| 🧪 METAB | Verde oliva | `#5cb583` |
| 🔪 QUIR | Ámbar / mostaza | `#c19a4e` |
| Genéricos y avatares | Teal hospital neutro | `#4a8a96` |
| Eventos Centinela | La familia de su categoría, **más oscura** (drama) | — |
| Acciones | Libre según la emoción (ataque=rojizo, apoyo=cálido, caos=nocturno) | — |

### Anclas de imagen (para Gemini / Whisk / image-to-image)

Antes de generar nada nuevo, carga 2–3 de estas como referencia:
- `arte/raw/C01-diostor.jpg` (personaje + teal + aureola)
- `arte/raw/R29-carro-de-paro.jpg` (escena dinámica + objeto)
- `arte/raw/extra/oxigenoterapia-soporte-vital.jpg` (objeto solo, monocromo)

---

## 3. Planos Fijos por Tipo de Carta

Cada categoría tiene un encuadre estándar. Esto acelera generación y asegura que el usuario vea lo que espera al abrir la mano.

### 3.1 Pacientes (26 ilustraciones)

**Plano:** Busto frontal, del pecho a la cabeza, sin cuerpo completo.  
**Luz:** Iluminación frontal suave (no dramática, no de lado).  
**Accesorios:** Máscara de oxígeno, tubo endotraqueal, monitor a fondo (detrás), línea IV visible si es grave.

**Por gravedad:**
- **I (leve):** Paciente despierto, algo cansado, máscara simple o sin accesorios. Edad 30–50.
- **II (moderado):** Sedado, tubo o máscara Venturi, monitor de fondo. Edad mixta 40–70.
- **III (grave):** Intubado, sedado profundo, con línea arterial visible, monitor conspicuo. Edad 60+.
- **ROJO (crítico):** Ventilado, infusión activa, expresión extrema (pánico, inconsciencia). Edad variable.

**Consejo:** En watercolor, la profundidad viene de transparencias y grises, no de enfoque. Mantén todos los elementos nítidos.

### 3.2 Recursos (43 ilustraciones)

**Plano:** Objeto aislado, 3/4 view o frontal (lo que deje ver el artefacto mejor).  
**Escala:** Objeto ocupa ~60% del canvas, blanco alrededor.  
**Luz:** 45° desde arriba-izquierda (sombra mínima debajo para levitar).

**Subcategorías:**
- **Fármacos (15):** Jeringa llena, ampolla, bolsa IV, tubo vial, etc. Realismo estético (no caricatura).
- **Imagen (7):** Máquina (ecografía, TAC, RX), pantalla lateral mostrando escaneo (abstrato, ondas).
- **Monitoreo (10):** Monitor (pantalla con ondas vitales), línea de presión, cable, ventilador.
- **Personal (8):** Estetoscopio, insignia enfermera, carrito, instrumento quirúrgico, kit de cuidado.
- **Comodín (3):** Símbolo ambiguo (cofre, maletín, insignia genérica).

**Textura:** Materiales reconocibles (metal pulido, plástico traslúcido, caucho) sin fotodetalle.

### 3.3 Acciones (20 ilustraciones)

**Plano:** Escena mínima con 1–2 figuras o elemento dinámico.  
**Emoción:** Refleja el efecto (ATAQUE = conflicto, APOYO = cooperación, CAOS = desorden).  
**Luz:** Dramática pero legible (contraste alto).

**Ejemplos:**
- **ATAQUE:** Dos manos compitiendo por un recurso, expresiones de rivalidad.
- **APOYO:** Manos cooperando, gesto de entrega o ayuda.
- **CAOS:** Objetos en movimiento, nube de confusión abstracta, líneas de energía.
- **RESPUESTA:** Escudo o barrera, reacción defensiva.
- **EXTREMA:** Figura con gesto de sacrificio o determinación extrema.

**Nota:** Las Acciones no tienen sinergia por sistema, así que puedes usar rango cromático más amplio (naranja, verde neón, púrpura) para diferenciarse de pacientes/recursos.

### 3.4 Eventos (28 ilustraciones)

**Plano:** Busto o semicuerpo con gesto adverso (pánico, cansancio, concentración extrema).  
**Contexto:** Mano con papeles, reloj de pared, gotero, máquina beeping.  
**Emoción:** Negativa o tensa (no neutra).

**Por categoría clínica:**
- **RESP:** Disnea, cianosis leve (piel ligeramente azul), tubo desconectado.
- **CARD:** Ritmo arrítmico en monitor, suor, mano en pecho.
- **NEURO:** Confusión, convulsión estilizada, ojos en blanco.
- **METAB:** Hipoglucemia (temblor), orina oscura (recipiente), glucómetro.
- **INFEC:** Fiebre (termómetro), escalofríos (líneas de movimiento), sudoración.
- **GENERAL:** Fatiga del equipo, papeleo abrumador, reloj en rojo.

**Textura:** Similar a pacientes, pero con líneas de energía o movimiento para señalar caos.

### 3.5 Personajes (6 ilustraciones)

**Plano:** Cuerpo entero (pies a cabeza), pose característica.  
**Uniforme:** Bata médica, ropa de civil con pequeños indicadores (badge, reloj, bolígrafo en bolsillo).  
**Accesorios:** Estétoscopio, gafas, café en mano (humanidad).

**Arquetipos en ¡VAYA TURNO!:**
- **Diostor:** Edad ~50, confianza absoluta, mano levantada como enseñando.
- **Médico Fantasma:** Etéreo, transparencia estilizada, uniforme antiguo.
- **Doctor Amor:** Accesible, sonrisa genuina, gesto acogedor.
- **Director:** Formal, mano en cadera o brazos cruzados, autoridad.
- **Gestora:** Administrativa, clipboard, postura organizada.
- **Esotérico:** Misterioso, símbolo o luz extraña, uniforme vago.

**Escala:** Cuerpo completo ocupa ~70% del canvas.

### 3.6 Sumarios (1 ilustración)

**Plano:** Documento ondulado, sellos, firma, quizás mano firmando.  
**Emoción:** Burocracia abrumadora, amenaza silenciosa.  
**Escala:** Documento ocupa 50%, con sombra que lo agiganta.

---

## 4. Orden de Trabajo Recomendado

**Fase 1: Imágenes Difíciles (Ancla + Hojas de Contacto)**

Toma 6 avatares + 26 pacientes = 32 ilustraciones "maestras" que fijan el estilo. Genera en tandas:

1. **6 Avatares** (Tanda 1, ~30 min)
   - Genera uno por uno con el bloque de estilo
   - Ajusta saturación si es necesario en herramienta local (ej: Photoshop, GIMP)
   - Guarda como `arte/personaje-<nombre>.png`

2. **26 Pacientes en 3 Hojas de Contacto** (Tandas 2–4, ~2 horas)
   - Agrupa por gravedad: 9×I, 8×II, 6×III, 3×ROJO
   - Usa **hojas de contacto** (contact sheet prompt):
     ```
     Generate a contact sheet with 9 medical patient portraits in pen-and-ink style,
     all different ages/ethnicities, mild respiratory patients, centered, 1:1 ratio each.
     [Bloque de estilo COPIABLE].
     Label each with patient name below.
     ```
   - Recorta cada portada en imagen individual: `arte/paciente-<id>.png`
   - Exporta la hoja completa como `arte/contactsheet-I.png` (reference)

3. **Imagen Ancla** (Tanda 5, ~15 min)
   - Genera **una UCI completa** con 3 camas ocupadas (composición maestra)
   - Usa como referencia visual para mantener profundidad de espacios en batches posteriores
   - Guarda como `arte/uci-master.png` (no es carta, es referencia)

**Fase 2: Imágenes Fáciles (Batch Rápido)**

Con avatares y pacientes listos, genera recursos/eventos en tandas por tipo:

4. **Recursos por tipo** (Tandas 6–10, ~3 horas)
   - Fármacos (15): 3 tandas de 5
   - Imagen (7): 2 tandas
   - Monitoreo (10): 2 tandas
   - Personal (8): 2 tandas
   - Comodín (3): 1 tanda

5. **Eventos por categoría clínica** (Tandas 11–15, ~2 horas)
   - RESP (5), CARD (5), NEURO (5), METAB (5), INFEC (5), GENERAL (3)

6. **Acciones** (Tandas 16–17, ~1 hora)
   - 20 acciones en 2 tandas de 10

7. **Sumario** (Tanda 18, ~5 min)
   - 1 ilustración única

**Tiempo total estimado:** 8–10 horas de generación (incluida revisión y ajuste).

---

## 5. Herramientas: Flow (Google Whisk), ChatGPT, Alternativas

### 5.1 Google Whisk / Flow

**Ventajas:**
- Image-to-image: toma una ilustración maestra y varía personajes/objetos manteniendo estilo
- Rápido, sin cola de espera
- Integración con Google Suite

**Workflow recomendado:**
1. Genera 2–3 "maestros" manuales (paciente grave + paciente leve + recurso) con ChatGPT
2. Carga en Whisk como base
3. Usa **"Replace this face/object"** para generar variaciones rápidas
4. Mantén el bloque de estilo en contexto para prompts

### 5.2 ChatGPT (DALL-E 3)

**Ventajas:**
- Mejor comprensión de prompts complejos
- Generación de "hojas de contacto" (múltiples objetos en grid)
- Iteración rápida sin herramienta separada

**Workflow recomendado:**
1. Usa prompts detallados con el bloque de estilo embebido
2. Pide "9 imágenes en grid" para contactsheets
3. Descarga PNG, recorta con herramienta local
4. Itera en variaciones (edad, postura, accesorios)

### 5.3 Stable Diffusion (ComfyUI, WebUI, API)

**Ventajas:**
- Control local, sin límites de API
- ControlNet para mantener pose/composición
- Batch processing integrado

**Workflow recomendado:**
1. Crea workflow `pacientes.json` con seed fijo, prompt dinámico
2. Ejecuta batch con variaciones automáticas
3. Normaliza output con script Python incluido

---

## 6. Validación & Normalización

### 6.1 Checklist Antes de Finalizar

Para cada ilustración:

- [ ] **Paleta:** Colores principales reconocibles, saturación consistente con otras (no demasiado brillante ni apagada)
- [ ] **Resolución:** 512×512 mín., preferentemente 1024×1024 o superior
- [ ] **Formato:** PNG con fondo transparente O PNG con fondo blanco sólido (consistente)
- [ ] **Composición:** Encaja en plano esperado (busto, objeto, cuerpo, etc.)
- [ ] **Legibilidad:** Sin texto superpuesto, contornos nítidos, líneas no borrosas

### 6.2 Script de Normalización

Ejecuta `tools/normalizar_arte.py` para batch-procesar 124 imágenes:

```bash
python3 tools/normalizar_arte.py \
  --entrada arte/raw \
  --salida arte/final \
  --paleta-dark '#3d7ea6,#b03d29,#7a5ba6,#2f8f6b,#8a6a2f' \
  --paleta-light '#5b9dc4,#e0705a,#a184c9,#5cb583,#c19a4e' \
  --resize 512 \
  --borde 0
```

**Lo que hace:**
1. Redimensiona a 512×512 (o máximo mantiene aspecto)
2. Reduce paleta a 64 colores (eliminando ruido)
3. Normaliza grano (aplicar filtro uniforme)
4. Convierte fondo inconsistente a blanco sólido
5. Ajusta contraste ligeramente para legibilidad

---

## 7. Integración con Generador de Print-and-Play

Una vez finalizadas las 124 ilustraciones en `arte/final/`:

```bash
python3 tools/generar_pnp.py \
  --cartas cartas/ \
  --arte arte/final \
  --salida pnp-ilustrado.html
```

El generador:
- Carga cada `arte/<id>.png` si existe
- Incrustra como fondo de carta
- Mantiene texto/nombre superpuesto legible (contraste automático)
- Genera booklet de 32 páginas A4, 6 cartas/página, listos para recortar

---

## 8. Referencias Artísticas

**Inspiración visual (sin copiar):**
- **Lucas Elliott:** Editorial científico moderno, líneas claras, watercolor sutil
- **Sam Kalda:** Ilustración médica rigurosa, estilo cartoon maduro
- **Medical Illustration Today:** Tonalidad profesional, claridad narrativa
- **Sketchbook de enfermería mexicana:** Humor amargo en línea, dignidad en la representación

**Paleta de referencia:**
- Herbario de medicina: muted ochres, teals, warm grays
- Uniformes de hospital moderno: azules clínicos, rojo de urgencia, grises
- Fluidos y objetos médicos: transparencias, reflejos limpios sin brillo

---

## 9. Resolución de Problemas Comunes

| Problema | Causa | Solución |
|----------|-------|----------|
| Escenario varía entre ilustraciones | Prompt demasiado abierto | Fija plano en bloque ("busto frontal", "objeto aislado") |
| Colores desaturados | Modelo satura menos que deseado | Agrega al prompt: "rich, saturated colors" + código hex explícito |
| Objetos médicos irreconocibles | Prompt vago | Especifica: "syringe with plunger visible", "ECG monitor showing waveform" |
| Texto superpuesto ilegible | No pedir blanco fondo | Siempre incluye: "white background, clean edges, no text overlay" |
| Inconsistencia entre lotes | Seed distinto | Fija seed en ComfyUI; en ChatGPT, copia exacto el prompts anterior |

---

## 10. Cronograma Propuesto

**Semana 1:** Validar herramienta (Whisk vs ChatGPT vs Stable), generar 6 avatares + imagen UCI maestra.

**Semana 2–3:** Generar 26 pacientes (hojas de contacto).

**Semana 4:** Generar recursos + eventos (~70 ilustraciones).

**Semana 5:** Acciones + Sumario, normalizar batch, integrar con PnP.

**Semana 6:** Playtest con arte finalmente, iterar si faltan ajustes tonales.

---

## Comandos Rápidos

```bash
# Ver colores del taller
grep -E '\-\-s[A-Z]+:' taller.html | head -3

# Generar 26 pacientes (pseudocódigo)
python3 tools/prompts.py --tipo pacientes --salida prompts_pacientes.txt

# Normalizar lote
python3 tools/normalizar_arte.py --entrada arte/raw --salida arte/final --resize 512

# Integrar con PnP
python3 tools/generar_pnp.py --cartas cartas/ --arte arte/final --salida pnp.html
```

---

**Última actualización:** 2026-08-16  
**Versión del juego:** v0.12  
**Estado:** Bloque de estilo y planos validados. Esperando confirmación de herramienta de generación.
