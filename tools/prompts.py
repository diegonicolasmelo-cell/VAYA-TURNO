#!/usr/bin/env python3
"""
Generador de prompts para ilustraciones de ¡VAYA TURNO!

Convierte datos de CSVs en prompts listos para ChatGPT, DALL-E 3, Google Whisk o Stable Diffusion.
Agrupa por tipo y batch para acelerar generación en paralelo.

Uso:
    python3 tools/prompts.py --tipo pacientes
    python3 tools/prompts.py --tipo recursos --batch 5
    python3 tools/prompts.py --salida prompts_todos.txt
"""

import argparse
import csv
import os
import sys
from collections import defaultdict

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Bloque de estilo global (embebido en cada prompt).
# Es el estilo canónico "Retro de Guardia", definido por las 39 ilustraciones
# finales del autor (arte/raw/). Ver docs/ARTE.md §2.
ESTILO = """
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
"""

# Familia de color ambiental por sistema clínico (docs/ARTE.md §2)
AMBIENTE = {
    "RESP": "hospital teal / blue family (anchor #5b9dc4)",
    "CARD": "burnt orange / brick red family (anchor #e0705a)",
    "NEURO": "purple / dark lavender family (anchor #a184c9)",
    "METAB": "olive green family (anchor #5cb583)",
    "QUIR": "amber / mustard family (anchor #c19a4e)",
    "": "neutral hospital teal family (anchor #4a8a96)",
    None: "neutral hospital teal family (anchor #4a8a96)",
    "INFEC": "sickly olive-yellow family, darker (drama)",
    "GENERAL": "neutral hospital teal family, darker (drama)",
}

def ambiente(sistema):
    return "AMBIENT COLOR FAMILY: " + AMBIENTE.get(sistema, AMBIENTE[""])

def cargar_csv(nombre):
    """Carga CSV desde carpeta cartas/."""
    ruta = os.path.join(RAIZ, "cartas", nombre)
    with open(ruta, encoding="utf-8") as f:
        return list(csv.DictReader(f))

def gen_prompts_pacientes(datos):
    """Genera prompts para 26 pacientes en hojas de contacto por gravedad."""
    prompts = defaultdict(list)

    grupos = {"I": [], "II": [], "III": [], "ROJO": []}
    for p in datos:
        grupos[p["gravedad"]].append(p)

    for gravedad, pacientes in grupos.items():
        n = len(pacientes)
        batch = 1
        for i in range(0, n, 3):  # Grupos de 3 para hojas de contacto
            tandas = pacientes[i:i+3]
            nombres = ", ".join([f['nombre'] for f in tandas])
            ids = "-".join([f['id'] for f in tandas])

            prompt = f"""
BATCH: pacientes-{gravedad}-{batch}
IDS: {ids}
OUTPUT: contactsheet-{gravedad}-{batch}.png

Generate a contact sheet with {len(tandas)} medical patient portraits in different poses,
ages, and ethnicities. All are Gravedad {gravedad} patients ({"leve" if gravedad == "I" else "moderate" if gravedad == "II" else "grave" if gravedad == "III" else "critical"}).

Patients: {nombres}

Visual guidelines:
- Busts from chest to head, no full body
- Gravedad I: Awake, fatigued, simple oxygen mask or no accessories
- Gravedad II: Sedated, Venturi mask or intubated, monitor background
- Gravedad III: Intubated, sedated, arterial line visible, monitor prominent
- Gravedad ROJO: Ventilated, active infusion, extreme expression

Composition: Each portrait centered, 2:3 portrait each, {len(tandas)} in a row.
Each portrait uses the ambient color family of ITS clinical system:
RESP=teal #5b9dc4, CARD=burnt orange #e0705a, NEURO=purple #a184c9,
METAB=olive #5cb583, QUIR=amber #c19a4e. Full-bleed ICU room background.
Label each with patient name below.

{ESTILO}
"""
            prompts["pacientes-" + gravedad].append(prompt.strip())
            batch += 1

    return prompts

def gen_prompts_recursos(datos):
    """Genera prompts para 43 recursos en tandas por tipo."""
    prompts = defaultdict(list)
    tipos = defaultdict(list)

    for r in datos:
        tipo = r.get("tipo", "DESCONOCIDO")
        # Algunas filas tienen "COMODIN" como tipo
        if tipo not in tipos:
            tipos[tipo] = []
        tipos[tipo].append(r)

    tipo_etiqueta = {
        "FARMACOS": "Fármacos",
        "IMAGEN": "Imaging",
        "MONITOREO": "Monitoring",
        "PERSONAL": "Staff",
        "COMODIN": "Wildcard"
    }

    for tipo, recursos in tipos.items():
        batch = 1
        for i in range(0, len(recursos), 5):  # Tandas de 5
            tandas = recursos[i:i+5]
            nombres = ", ".join([r["nombre"] for r in tandas])
            ids = "-".join([r["id"] for r in tandas])

            if len(tandas) == 1:
                # Single item
                r = tandas[0]
                sistema = f"({r.get('sistema', 'GENERAL')})" if r.get("sistema") else ""
                prompt = f"""
ID: {r["id"]}
NOMBRE: {r["nombre"]}
BATCH: recurso-{tipo}-{batch}
OUTPUT: recurso-{r["id"]}.png

Medical resource: {r["nombre"]} {sistema}
Description: {r.get("frase", "Medical equipment")}
Type: {tipo_etiqueta.get(tipo, tipo)}

Visual: 3/4 view or frontal (best angle). Object is the protagonist, ~60% of canvas,
drawn with the same thick outlines and flat colors as the characters (like a retro
equipment poster — see arte/raw/extra/oxigenoterapia). Full-bleed monochrome ICU wall behind.
{ambiente(r.get("sistema"))}

{ESTILO}
"""
            else:
                # Contact sheet
                prompt = f"""
BATCH: recurso-{tipo}-{batch}
IDS: {ids}
OUTPUT: contactsheet-recurso-{tipo}-{batch}.png

Generate a contact sheet with {len(tandas)} medical resources/equipment, all {tipo}.
Items: {nombres}

Visual: Each object is the protagonist of its own panel (2:3 each), thick outlines,
flat colors, retro equipment-poster look. Full-bleed monochrome ICU wall behind each.
Each item uses the ambient family of ITS clinical system (RESP=teal, CARD=burnt orange,
NEURO=purple, METAB=olive, QUIR=amber; generic items = neutral hospital teal).

{ESTILO}
"""
            prompts["recursos-" + tipo].append(prompt.strip())
            batch += 1

    return prompts

def gen_prompts_eventos(datos):
    """Genera prompts para 28 eventos en tandas por categoría."""
    prompts = defaultdict(list)
    categorias = defaultdict(list)

    for e in datos:
        cat = e.get("categoria", "GENERAL")
        categorias[cat].append(e)

    for cat, eventos in categorias.items():
        batch = 1
        for i in range(0, len(eventos), 5):  # Tandas de 5
            tandas = eventos[i:i+5]
            nombres = ", ".join([e["nombre"] for e in tandas])
            ids = "-".join([e["id"] for e in tandas])

            if len(tandas) == 1:
                e = tandas[0]
                prompt = f"""
ID: {e["id"]}
NOMBRE: {e["nombre"]}
BATCH: evento-{cat}-{batch}
OUTPUT: evento-{e["id"]}.png

Medical event/complication: {e["nombre"]}
Clinical category: {cat}
Narrative: {e.get("frase", "Medical emergency")}

Visual: Bust or semi-body with adverse gesture (panic, exhaustion, extreme focus).
Context: Hand with papers, wall clock, drip, machine beeping.
Emotion: Negative or tense (not neutral).

Clinical details for {cat}:
- RESP: Dyspnea, mild cyanosis (slightly blue skin), disconnected tube
- CARD: Arrhythmic rhythm on monitor, sweat, hand on chest
- NEURO: Confusion, stylized seizure, eyes rolling back
- METAB: Hypoglycemia (tremor), dark urine (cup), glucometer
- INFEC: Fever (thermometer), chills (motion lines), sweating
- GENERAL: Team fatigue, overwhelming paperwork, clock in red

{ambiente(cat)} — darker and more dramatic than resource cards.

{ESTILO}
"""
            else:
                prompt = f"""
BATCH: evento-{cat}-{batch}
IDS: {ids}
OUTPUT: contactsheet-evento-{cat}-{batch}.png

Generate a contact sheet with {len(tandas)} medical events/adverse effects, all {cat}.
Events: {nombres}

Visual: Each bust or semi-body with adverse gesture, 2:3 each. Negative/tense emotion.
Minimal context (monitor, clock, drip). Full-bleed ICU background.
{ambiente(cat)} — darker and more dramatic than resource cards.

{ESTILO}
"""
            prompts["eventos-" + cat].append(prompt.strip())
            batch += 1

    return prompts

def gen_prompts_acciones(datos):
    """Genera prompts para 20 acciones en tandas por tipo."""
    prompts = defaultdict(list)
    tipos = defaultdict(list)

    for a in datos:
        tipo = a.get("tipo", "GENERAL")
        tipos[tipo].append(a)

    tipo_narrativa = {
        "ATAQUE": "conflict, rivalry, competitive tension",
        "APOYO": "cooperation, support, team helping team",
        "CAOS": "disorder, confusion, chaos, disruption",
        "RESPUESTA": "defense, shield, reactive protection",
        "EXTREMA": "sacrifice, determination, extreme stakes"
    }

    for tipo, acciones in tipos.items():
        batch = 1
        for i in range(0, len(acciones), 5):  # Tandas de 5
            tandas = acciones[i:i+5]
            nombres = ", ".join([a["nombre"] for a in tandas])
            ids = "-".join([a["id"] for a in tandas])

            if len(tandas) == 1:
                a = tandas[0]
                prompt = f"""
ID: {a["id"]}
NOMBRE: {a["nombre"]}
BATCH: accion-{tipo}-{batch}
OUTPUT: accion-{a["id"]}.png

Card effect: {a["nombre"]}
Action type: {tipo}
Narrative: {a.get("frase", "Game mechanic")}

Visual: Minimal scene with 1–2 figures or dynamic element.
Emotion: Reflects effect: {tipo_narrativa.get(tipo, "dynamic")}
Lighting: Dramatic but legible (high contrast).

Examples by type:
- ATAQUE: Two hands competing for a resource, rivalry expressions
- APOYO: Hands cooperating, gesture of handing over or helping
- CAOS: Objects in motion, abstract confusion cloud, energy lines
- RESPUESTA: Shield or barrier, defensive reaction
- EXTREMA: Figure with sacrifice or extreme determination gesture

Color: Wider chromatic range (orange, neon green, purple) to differentiate from patients/resources.

{ESTILO}
"""
            else:
                prompt = f"""
BATCH: accion-{tipo}-{batch}
IDS: {ids}
OUTPUT: contactsheet-accion-{tipo}-{batch}.png

Generate a contact sheet with {len(tandas)} action cards, all {tipo}.
Actions: {nombres}

Visual: Minimal scenes, 1–2 figures or dynamic elements per card.
Emotion: {tipo_narrativa.get(tipo, "dynamic")}
Dramatic lighting, high contrast. 1:1 grid.

Wider color range (orange, green, purple) than patient/resource cards.

{ESTILO}
"""
            prompts["acciones-" + tipo].append(prompt.strip())
            batch += 1

    return prompts

def gen_prompts_personajes(datos):
    """Genera prompts para 6 personajes."""
    prompts = {"personajes": []}

    arquetipos = {
        "Diostor": "Age ~50, absolute confidence, hand raised as teaching. Badge, stethoscope.",
        "Médico Fantasma": "Ethereal, stylized transparency, vintage uniform. Slightly faded.",
        "Doctor Amor": "Accessible, genuine smile, welcoming gesture. Modern scrubs, charm.",
        "Director": "Formal, hand on hip or arms crossed. Authority, leadership. Suit or formal wear.",
        "Gestora": "Administrative, clipboard, organized posture. Professional attire.",
        "Esotérico": "Mysterious, ambiguous symbol or strange light. Vague uniform."
    }

    for p in datos:
        nombre = p.get("nombre", "Unknown")
        nombre_limpio = nombre.replace("El ", "").replace("La ", "").strip()
        arquetipo = arquetipos.get(nombre_limpio, "Medical professional")
        habilidad = p.get("habilidad", "Special ability")
        frase = p.get("frase", "")

        prompt = f"""
ID: {p["id"]}
NOMBRE: {nombre}
OUTPUT: personaje-{p["id"]}.png

Character avatar: {nombre}
Archetype: {arquetipo}
Special ability: {habilidad}
Quote: {frase}

Visual: Full body or 3/4 body, characteristic pose. Full-bleed ICU corridor or ward
background, 2:3 portrait. Reference anchors: arte/raw/C01-diostor.jpg, C03, C05, C06.
Clothing: Medical coat or scrubs with small indicators (badge, stethoscope, watch, pen).
Humanizing detail: Coffee mug, gesture, expression showing personality.
AMBIENT COLOR FAMILY: neutral hospital teal (anchor #4a8a96), with ONE accent detail
allowed (like DIOSTOR's golden halo).

Scale: Body occupies ~70% of canvas.

{ESTILO}
"""
        prompts["personajes"].append(prompt.strip())

    return prompts

def gen_prompts_sumarios(datos):
    """Genera prompt para 1 sumario administrativo."""
    prompts = {"sumarios": []}

    for s in datos:
        prompt = f"""
ID: {s["id"]}
NOMBRE: {s["nombre"]}
OUTPUT: sumario-{s["id"]}.png

Game mechanic: {s["nombre"]}
Narrative: {s.get("frase", "Administrative curse")}

Visual: Wavy document, stamps, signature, perhaps hand signing.
Emotion: Overwhelming bureaucracy, silent threat.
Scale: Document occupies 50%, shadow beneath it to enlarge it.

Bureaucratic symbols: Handwritten notes, official stamps, "CONFIDENCIAL", checklist marks.

{ESTILO}
"""
        prompts["sumarios"].append(prompt.strip())

    return prompts

def main():
    ap = argparse.ArgumentParser(
        description="Genera prompts de imagen para ilustraciones de ¡VAYA TURNO!"
    )
    ap.add_argument("--tipo", choices=["pacientes", "recursos", "eventos", "acciones", "personajes", "sumarios", "todos"],
                    default="todos", help="Tipo de cartas a generar prompts")
    ap.add_argument("--salida", default=None, help="Archivo de salida (stdout si omitido)")
    ap.add_argument("--batch", type=int, default=None, help="Filtrar solo un batch específico")
    args = ap.parse_args()

    # Carga datos
    try:
        pacientes = cargar_csv("pacientes.csv")
        recursos = cargar_csv("recursos.csv")
        eventos = cargar_csv("eventos.csv")
        acciones = cargar_csv("acciones.csv")
        personajes = cargar_csv("personajes.csv")
        sumarios = cargar_csv("sumarios.csv")
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    todos_prompts = {}

    if args.tipo in ("pacientes", "todos"):
        todos_prompts.update(gen_prompts_pacientes(pacientes))
    if args.tipo in ("recursos", "todos"):
        todos_prompts.update(gen_prompts_recursos(recursos))
    if args.tipo in ("eventos", "todos"):
        todos_prompts.update(gen_prompts_eventos(eventos))
    if args.tipo in ("acciones", "todos"):
        todos_prompts.update(gen_prompts_acciones(acciones))
    if args.tipo in ("personajes", "todos"):
        todos_prompts.update(gen_prompts_personajes(personajes))
    if args.tipo in ("sumarios", "todos"):
        todos_prompts.update(gen_prompts_sumarios(sumarios))

    # Output
    lineas = []
    for categoria, prompts_lista in sorted(todos_prompts.items()):
        lineas.append(f"\n{'='*80}")
        lineas.append(f"CATEGORÍA: {categoria.upper()}")
        lineas.append(f"{'='*80}\n")
        for i, p in enumerate(prompts_lista, 1):
            lineas.append(p)
            lineas.append("")

    salida = "\n".join(lineas)

    if args.salida:
        with open(args.salida, "w", encoding="utf-8") as f:
            f.write(salida)
        print(f"✓ Prompts guardados en {args.salida}", file=sys.stderr)
    else:
        print(salida)

if __name__ == "__main__":
    main()
