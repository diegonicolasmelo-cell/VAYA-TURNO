#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera docs/PROMPTS-ARTE.md: un prompt COMPLETO y personalizado por
carta, listo para pegar en Nano Banana / Google Flow, más la ficha de cada
una (id, prompt, descripción, frase, añadido extra).

Las ESCENAS están escritas a mano en este archivo — son la dirección de
arte, no un dato: editarlas ES editar el brief. La ficha de juego sale de
los CSV, así que el documento nunca contradice las cartas vivas.

    python3 tools/generar_prompts_arte.py
"""
import csv, os, sys

RAIZ = "/home/user/VAYA-TURNO"

def leer(*p):
    return list(csv.DictReader(open(os.path.join(RAIZ, *p), encoding="utf-8")))

# El estilo de la casa, derivado de las primeras 10 imágenes reales que
# salieron de Flow (agosto 2026) — NO del ideal teórico anterior. Dos
# cambios de fondo respecto de la v1: proporciones adultas en vez de
# cabezones, y sombreado suave en vez de color plano puro.
#
# 🔴 REGLA DURA: aquí NO se menciona el cansancio. El bloque v1 pedía
# "caras cansadas y ojeras" en las 115 cartas, y por eso todos los
# personajes salían siendo la misma persona agotada. El ánimo se define
# carta por carta (ANIMO), y el cansancio es la excepción, no la regla.
BASE = ("Modern flat-vector cartoon illustration in the style of a "
        "contemporary animated TV series. Clean digital finish: smooth flat "
        "color fills with soft two-step cel shading plus gentle airbrushed "
        "gradients on skin and fabric. No visible brush texture, no grain, "
        "no photorealism.\n"
        "LINE: medium-weight outline in desaturated dark brown or deep teal, "
        "never pure black; even and confident, slightly tapered at the ends. "
        "Interior detail lines noticeably thinner than the silhouette.\n"
        "CHARACTERS: adult naturalistic proportions with a slightly enlarged "
        "head (about 5 to 6 heads tall). Large round eyes with clear white "
        "sclera and dark irises; thick expressive eyebrows doing most of the "
        "acting; simple mouths, soft rounded jawlines. Ordinary hospital "
        "clothing: teal or navy scrubs, white coats, lanyards, stethoscopes. "
        "Chilean public-hospital cast: varied ages, builds and skin tones.\n"
        "EXPRESSION: the mood and energy of each card are specified below in "
        "MOOD — follow them exactly. Do NOT add generic tiredness, eye bags "
        "or worry to a face that was not asked for them.\n"
        "COLOR: the ENTIRE image is graded into ONE dominant hue — "
        "background, props, skin and clothing all sit inside that single "
        "color family, with a narrow value range and low overall contrast. "
        "Only two or three supporting accent colors are allowed.\n"
        "BACKGROUND: a real, readable interior drawn simplified and "
        "flattened, painted in the same hue as the subject and pushed one "
        "step lower in contrast so the subject separates cleanly.\n"
        "LIGHT: soft ambient overhead light, gentle falloff, no hard "
        "shadows, no rim light, no lens flare.\n"
        "TONE: affectionate workplace comedy — competent people, warm "
        "humour, never cruel and never grim.\n"
        "COMPOSITION: board-game card art — one strong silhouette, one clear "
        "readable action, filling about 70% of the frame at eye level. Full "
        "bleed, never white.\n"
        "CROP SAFETY (important): the head and the identifying object must "
        "sit in the UPPER HALF of the frame, with the eyes about one third "
        "down from the top. The game shows only a wide strip taken from the "
        "top of the image on the small card, so anything in the bottom third "
        "may never be seen. Leave a small margin at every edge: nothing "
        "important touches the border.\n"
        "AVOID: photorealism, watercolor, painterly texture, thick black "
        "comic-book inking, chibi or super-deformed proportions, neon or "
        "rainbow palettes, real brand logos, and any text longer than two "
        "words.\n"
        "Portrait orientation, aspect ratio 3:4 (or 2:3 if available) — "
        "never square and never landscape.")

FAM = {"RESP": "hospital teal-blue (#5b9dc4)",
       "CARD": "burnt orange / brick red (#e0705a)",
       "NEURO": "dark lavender purple (#a184c9)",
       "METAB": "olive green (#5cb583)",
       "QUIR": "amber / mustard (#c19a4e)",
       "": "neutral hospital teal (#4a8a96)"}
FAM_ACC = {"ATAQUE": "brick red / rust conflict palette (#b5533c)",
           "APOYO": "warm amber / honey palette (#c98d3e)",
           "CAOS": "night slate-blue palette (#4a5a78)",
           "RESPUESTA": "calm hospital teal (#4a8a96)",
           "EXTREMA": "deep nocturnal purple, almost black (#3d2b52)"}
NOCHE = "nocturnal dark hospital teal (#2e5a63)"

GRAV = {"I": "awake and sitting up, dramatic or annoyed, at most a nasal "
             "cannula, 30-50 years old",
        "II": "drowsy, Venturi mask or oxygen, monitor visible behind, "
              "40-70 years old",
        "III": "intubated, deep sedation, arterial line, the monitor is a "
               "protagonist, over 60",
        "ROJO": "ventilated, several infusion pumps running, the most "
                "extreme scene in the deck"}

MARCO_P = ("PATIENT PORTRAIT: frontal bust from chest to head, soft frontal "
           "light, ICU monitor and IV pole simplified behind.")
MARCO_R = ("OBJECT CARD: the object nearly isolated, 3/4 or frontal view, "
           "filling about 60% of the frame, on an ambient monochrome "
           "hospital background, never white.")
MARCO_RP = ("STAFF PORTRAIT: bust or half body of the person in their "
            "working gesture, competent and absorbed in the task, ICU "
            "ambience behind.")
MARCO_A = ("ACTION SCENE: minimal scene, one or two figures or a single "
           "element in motion. THIS CARD HAS TO BE FUNNY — build the whole "
           "frame around ONE visual gag: an exaggerated reaction, an absurd "
           "detail, a comic contrast between what is said and what is seen. "
           "Push the expressions further than in the rest of the deck. The "
           "joke leads; the detail follows.")
MARCO_C = ("CHARACTER PORTRAIT: full body, signature pose, filling about "
           "70% of the frame. This is an archetype portrait — draw the "
           "personality, not the uniform.")

# ══ PACIENTES ═══════════════════════════════════════════════════════
EP = {
"P01": "middle-aged man clutching his chest with theatrical agony while side-eyeing the hospital bill on his tray table; one eyebrow says the pain moved when the price appeared",
"P02": "patient sitting up with an innocent guilty smile, holding an empty pill bottle upside down; a lone cotton ball missing from the cotton jar beside him",
"P03": "relaxed man shrugging with total confidence, a dusty unopened pill box with cobwebs on his nightstand, calendar behind showing eight months crossed out",
"P04": "bruised patient with an arm sling insisting with a straight face, while the whole scene behind him (wet floor sign, rubber duck) contradicts his story",
"P05": "hyperventilating woman gripping the bed rails with catastrophic eyes, monitor behind showing a perfectly normal rhythm; a wall calendar with every Tuesday circled",
"P06": "sunburnt young man with cracked lips holding up four fingers proudly, empty beer cans arranged like a trophy on the tray, IV line already running",
"P07": "smug patient in bed holding out a thick printed stack titled with a diagnosis, treatment plan bookmarked, the doctor's clipboard hanging defeated at the bedside",
"P08": "post-op patient camped in the bed with personal slippers, a plant and three days of newspapers; surgical drain still attached, roots almost growing",
"P09": "gray-faced man mid-cough with a Venturi mask lifted to talk, one month of crumpled tissue packets on the blanket, dark rings of a sleepless month",
"P10": "young woman breathing deep and fast (Kussmaul), empty insulin pen on the nightstand, calendar showing Thursday to Sunday crossed out, sweet fruity breath drawn as tiny wavy lines",
"P11": "elderly patient with one side of the face drooping, a wall clock behind with a giant question mark on it, family silhouettes shrugging at the door",
"P12": "pale patient with a knowing look away from the doctor, six little tally marks scratched on the bed rail, a basin discreetly at hand",
"P13": "grandfather with swollen ankles propped up, oxygen on, surrounded by the loving evidence: a thermos of cazuela, soup cup, juice box and a dessert plate on the tray",
"P14": "exhausted woman in work uniform still holding her lanyard, fever flush on the cheeks, an IV starting; her phone buzzing with work messages on the tray",
"P15": "patient with hands on the belly, in a tug-of-war of pointing arrows: a surgical cap silhouette points left, a stethoscope silhouette points right; he belongs to no one",
"P16": "wiry old man with a Venturi mask, his oxygen tank on one side of the bed and his cigarette pack peeking from the robe pocket on the other; both drawn as loyal pets",
"P17": "young man with spiral eyes and a chalkboard of question marks behind, toxicology chart on the wall with everything circled; he shrugs too",
"P18": "sweet grandmother asleep like an angel in daylight... with a tiny inset moon showing her conducting an invisible orchestra with the IV pole as baton at night",
"P19": "gravely ill patient, flushed and sweaty, four infusion pumps stacked like a totem beside the bed, a melted golden hourglass on the monitor shelf",
"P20": "young man in cervical collar and full fixation, monitor busy; a tiny speedometer at 120 and an unbuckled seatbelt drawn as ghost icons above",
"P21": "serene intubated patient, almost peaceful, while the chest X-ray on the lightbox behind is a storm of frosted glass; the calm and the storm in one frame",
"P22": "intubated patient with EEG leads, four empty syringes lined up on the cart like spent shells, a tiny lightning bolt still crossing the monitor trace",
"P23": "big man intubated with a distended belly, dreaming (thought bubble) of a single innocent asado skewer with a halo; enzyme numbers towering on the monitor",
"P24": "patient on high-flow oxygen gripping the bed, a suitcase with flight stickers still at the bedside, boarding pass on the floor; one leg drawn swollen",
"P25": "the most tangled bed of the deck: ventilator, pumps, lines and drains all at once, each labeled organ waving a tiny white flag in alphabetical order",
"P26": "patient ready and packed on the stretcher, IV pole as flag mast; through the window a tiny plane circles and the OR doors behind have a CLOSED sign",
}

# ══ RECURSOS ════════════════════════════════════════════════════════
ER = {
"R01": "a proud wide-spectrum antibiotic IV bag hanging center stage with a superhero glow, covering the whole scene with its shadow like a protective cape",
"R02": "the same wide-spectrum IV bag, but a tiny army of smug bacteria wearing helmets and carrying microscopic shields marches across the tubing unharmed",
"R46": "a sedation syringe pump purring softly, zzz bubbles floating up, a serene sleeping patient silhouette in the background; the whole ward exhales",
"R47": "the same syringe pump at night, the zzz bubbles turning into ?! sparks, the patient silhouette behind wide-eyed conducting an invisible orchestra",
"R05": "an anticoagulation vial balanced dead-center on a tiny seesaw, one side a blood drop, the other a clot; both watching each other with suspicion",
"R06": "the same vial and seesaw, tipped hard: the blood-drop side flooding, tiny red drips escaping the frame; the balance was never fair",
"R07": "a blood bag arriving in a cooler with a heroic entrance, dramatic light, its paper tag missing — just a torn string where the form should be",
"R08": "a noradrenaline syringe pump with a pressure gauge climbing, the needle rising like a thermometer in summer; steady hands hold the frame",
"R09": "the same pump, gauge needle buried in red, the ECG trace behind gone jagged like a mountain range; everything vibrates slightly",
"R10": "a nebulizer mask puffing majestic clouds of vapor that fill the top of the frame like a spa; a tiny rubber duck silhouette in the mist",
"R13": "an insulin pump beside a glucometer, both flanked by a clock face marked every two hours; a stack of used test strips like a tiny card deck",
"R48": "a corticosteroid vial radiating a mighty power aura, flexing its glow; everything around it stands a little straighter",
"R49": "the same vial, but a pyramid of sugar cubes has piled up behind it and the glucometer beside shows a screaming high number with sweat drops",
"R50": "a crystal-clear saline bag glinting like a jewel, one perfect drop mid-fall, calm and generous",
"R51": "the same saline bag overflowing, a puddle spreading below, tiny sandbags stacked around the IV pole like flood defense",
"R16": "a chest X-ray film held up to the light — slightly rotated, slightly crooked, clipped anyway; the lightbox hums with routine dignity",
"R17": "the same film with one tiny circled shadow in a corner, three question marks orbiting it; nobody asked for this discovery",
"R18": "a bedside ultrasound machine with a proud gray blob on screen, the probe raised like a sword; conviction without certainty",
"R19": "the same ultrasound, the blob on screen now suspiciously shaped like a fish, the probe scratching its own cable in doubt",
"R20": "a CT scanner donut glowing at the end of a corridor while a stretcher rolls toward it at full speed, motion lines and a flying chart",
"R21": "the same corridor mid-disaster: stretcher drifting a corner, IV pole tipping, papers airborne — the scanner still glowing patiently far away",
"R22": "an angio-CT console showing vessels lit up like a golden subway map, the contrast injector standing by like a rocket booster",
"R52": "the same console, but the contrast bottle drips its last drop and a kidney-shaped warning light blinks on the corner of the screen",
"R23": "an MRI machine glowing like a mythical portal behind a velvet rope, a take-a-number ticket dispenser beside it showing 87",
"R24": "an arterial line finally in place on a wrist, drawn triumphant; behind, a tray discreetly hides four bent needles under a cloth",
"R25": "the same wrist, the fingertips drawn faintly blue-violet, a tiny alarm bell above; the line itself whistles innocently",
"R26": "a central line kit laid out on a sterile field like surgical jewelry, ultrasound at the ready, an audience of small silhouettes at the door",
"R27": "the same kit, but a conga line of tiny green germs with party hats climbs up the catheter; the sterile field pretends not to see",
"R30": "a mechanical ventilator with its knobs and screen, connected by tubing drawn as a tug-of-war rope to a small pair of stubborn lungs",
"R31": "the same ventilator, tiny germs surfing down the tubing on droplets, the lungs bracing; the machine keeps its dignity",
"R32": "an arterial blood gas syringe resting on crushed ice like a delicacy, a pH strip beside reading catastrophic; someone must now say something smart",
"R33": "the same syringe shaken like a cocktail — foam, pink froth and a tiny paper umbrella planted on top; the lab will not be amused",
"R44": "a chest tube kit with chalk marks counting rib spaces on a diagram, the water-seal chamber bubbling politely in a corner",
"R45": "a lumbar puncture needle poised over the curved back of a patient curled like a shrimp, a dotted target line between two vertebrae",
"R34": "veteran ICU nurse, bust, taping a line with perfect technique while giving the viewer the polite look of someone who already knows the answer",
"R35": "ICU technician carrying half the unit in one arm — supply stack, monitor cable, and the dignity of the whole shift — without dropping anything",
"R36": "the same technician on hour twenty-four: two coffee mugs, cap slightly crooked, one eye twitching, still standing, still carrying everything",
"R37": "young medical fellow with an open manual, enthusiastic sparkle, pockets bursting with pocket guides; a heart full of theory and hands full of hope",
"R38": "bed manager holding a clipboard where the beds are drawn as Tetris pieces that don't fit; he brings no beds, only questions about beds",
"R39": "respiratory physiotherapist mid chest-percussion, already half out of the door in motion blur; came, aspirated, mobilized, vanished",
"R53": "gleaming operating room double doors opening with rays of light — and one dotted silhouette where the anesthesiologist should be standing",
"R54": "scrubbed surgeon counting instruments with theatrical confidence; on the count tray, one gauze slot conspicuously empty and glowing",
"R42": "the general practitioner on duty, bust, holding a swiss-army stethoscope with a tool for everything; the one who is always there",
"R43": "an open ward drawer with the survivors: odd gloves, one saline flush, a bandage roll and a tiny tumbleweed of gauze rolling past",
}

# ══ ACCIONES ════════════════════════════════════════════════════════
EA = {
"A01": "a nurse silhouette walking off toward the exit with a suitcase and a sun hat, leaving a glowing dotted outline at the bedside; an HR stamp floats above, freshly inked",
"A02": "a circle of rival staff reluctantly handing supplies to one beaming resident holding a birthday cake; every gift has a tiny invisible debt attached",
"A03": "a long meeting table with a wall clock at the two-hour mark, resources sliding across the table like poker chips toward their new beds",
"A04": "a hand rescuing one shining card from a trash bin of crumpled papers, a note attached reading like a polite suggestion; the find goes to the pocket, not the bed",
"A05": "one doctor with two ID badges, three coffees and an armful of extra cards, while a ghost version of tomorrow-him slumps in the corner",
"A06": "a dead computer screen at the nurses station with a yellowed sticky note, staff frozen mid-click around it; a cable drawn like a crime scene",
"A07": "two white coats swapping mid-air between two horrified doctors, name tags trading places; a medical leave form flutters down like a feather",
"A08": "a red wall phone ringing itself off the hook, twelve tally marks scratched beside it, the corridor lights flickering to attention",
"A09": "an auditor with a clipboard leaning uncomfortably close over someone's fanned hand of cards, smiling the smile of someone who is definitely fiscalizing",
"A10": "two full hands of cards crossing mid-air in a small tornado between two desks, name stickers flying loose; nobody knows who rotates where",
"A11": "two steaming coffee cups on a tray raised like a shield, an incoming complication bolt bouncing off the steam; somewhere, a kettle did its duty",
"A12": "a dusty institutional binder glowing on a shelf as it photocopies the last played card by itself, the copy sliding out still warm",
"A13": "the far end of a dark corridor: a hooded skeletal figure in scrubs politely asking at bed 4, two coins spinning in the air above an open palm",
"A14": "a doctor with one enormous magnifying-glass eye squinting at three face-down cards on the deck, one of them sweating",
"A15": "a signed blank prescription flying through the ward like a golden ticket, staff diving after it; the signature is a lightning scribble",
"A16": "a CPR training dummy heroically raising a shield to block an incoming complication bolt aimed at the bed behind it; it has seen worse",
"A17": "a pharmacy shelf empty except for a small sign promising Thursday, a spider web in the corner and one loyal box of the wrong size",
"A18": "a giant pair of budget scissors cutting a ribbon shaped like an IV line; below, a hand holds two indication tokens where three used to be",
"A19": "the deep bottom drawer opening with a golden glow while a veteran nurse guards it, key on a necklace; inside, exactly what was needed",
"A20": "a sample tube shaken like a cocktail shaker with a tiny umbrella, next to an X-ray sliding into a bin with a REPEAT stamp mid-air",
"A21": "a wall of machines looming over one tiny bed, one more device being plugged in by insistent hands; new ribs gleam, nobody asked the question",
"A22": "a patient in street clothes sprinting out the ward door trailing ECG leads like streamers, discharge paper stamped mid-air, one slipper left behind",
}

# ══ PERSONAJES: escenario rotado + pose característica ══════════════
EC = {
"C01": ("hospital corridor as his personal catwalk: smug senior attending, "
        "immaculate flowing coat, arms open in a blameless shrug, a faint "
        "saint-like halo; a junior trails behind carrying his paperwork",
        None),
"C02": ("the night door of the on-call residence: a half-translucent doctor "
        "with coffee slipping backwards out of frame, ghostly motion trail, "
        "his pager glowing and ringing unanswered on the desk", NOCHE),
"C03": ("ward corridor at golden lamp light, posing as if for a magazine "
        "cover: she leans on an IV pole like a lamppost, one hand on her "
        "chest, winking straight at the viewer, a rose tucked in the coat "
        "pocket, tiny sparkles around her; the ECG on the monitor behind "
        "traces a heart shape", None),
"C04": ("top-floor office overlooking the hospital through glass: suited "
        "director with hospital badge, phone at the ear, one hand feeding a "
        "report into a shredder, political smile, golf trophy on the shelf",
        None),
"C05": ("the bed-management whiteboard as a war room: sharp woman with radio "
        "in hand moving bed magnets like chess pieces; behind her, a "
        "stretcher waits with a suitcase on it", None),
"C06": ("a dim on-call room turned ritual den: doctor with amulets and "
        "crystals over the scrubs, sage smoke curling, lab results spread "
        "like tarot cards around a candle", NOCHE),
"C07": ("the dark ward under one pool of lamplight: serene night nurse "
        "sitting guard with a thermos, finger to her lips in a shh; the "
        "alarm bells behind her wrapped in gauze", NOCHE),
"C08": ("hospital corridor photo-op: gray-haired chief posing with a thumbs "
        "up for a framed picture, camera flash frozen; behind him the "
        "exhausted team does the actual work", None),
"C09": ("the supply warehouse aisle: supply queen among tall shelves of "
        "labeled boxes, walkie-talkie on her belt, SAFETY BOOTS, hi-vis "
        "vest over the uniform, checking inventory on a clipboard with a "
        "pen chained to it, one finger counting boxes", None),
"C10": ("OUTSIDE the hospital entrance in open daylight: union leader with "
        "sash and megaphone, fist raised high, a stack of petitions under "
        "the arm, a protest banner strung between two poles behind, "
        "coworkers with little flags", None),
"C11": ("a quiet consult office with a diploma wall: elegant subspecialist "
        "examining one single ECG strip through a magnifying glass, "
        "unhurried, one eyebrow raised; a four-day-old interconsult form "
        "waits in the inbox tray", None),
"C12": ("a corridor checkpoint: infection-control nurse in impeccable PPE "
        "holding a giant folded spreadsheet printout cascading to the "
        "floor, pointing at a hand-hygiene poster; an alcohol-gel spray "
        "holstered like a sheriff", None),
"C13": ("the on-call study desk at dawn: young resident with heroic dark "
        "circles, a tower of highlighted textbooks, three coffee cups, "
        "pens lined in the pocket, eager overachiever smile", None),
"C14": ("bedside mid-code, lit from below by the monitor: intense doctor "
        "with defibrillator paddles raised and charging, absolute NOT "
        "TODAY determination; a nurse hands adrenaline from the side",
        None),
"C15": ("the ward exit door: doctor stamping discharge papers in a motion "
        "blur of triple stamps, a half-dressed patient already being "
        "wheeled out; behind, the empty bed is being remade at speed",
        None),
"C16": ("the dark reading room lit only by lightbox glow: radiologist "
        "holding a film up close, intrigued squint, dictaphone in the "
        "other hand; a leaning tower of unread studies beside", NOCHE),
"C17": ("mid-corridor, mid-everything: handyman-orderly with a utility belt "
        "mixing wrench, BP cuff, plunger and cables, a monitor under one "
        "arm and a mop in the other hand, unbothered", None),
"C18": ("bedside, first try: confident nurse flexing her wrist with a tiny "
        "halo on it, syringe with one perfect drop, the patient's arm "
        "relieved; a caught butterfly needle drawn like a medal", None),
"C19": ("the eye of the storm: dead-calm intensivist sipping coffee while "
        "every monitor around flashes and alarms; his face says this is a "
        "normal Tuesday", None),
"C20": ("a night corridor corner: lanky figure peeking around the wall, "
        "sneaky grin, wheeling an IV pole loaded like a shopping cart "
        "with borrowed equipment, eyes locked on an unattended monitor",
        NOCHE),
"C21": ("the supply-room doorway: doctor opening his coat like a street "
        "vendor to reveal contingency folders, spare batteries, masks and "
        "a tiny umbrella; behind, a wall calendar with March circled in "
        "red and a told-you-so face", None),
"C22": ("the nurses station as a fortress: formidable head nurse, arms "
        "crossed, reading glasses on a chain, looking over them straight "
        "at the viewer; her staff sheltered behind her and a metrics "
        "board of all-green checkmarks", None),
}
# ══ EL FÍSICO DE CADA PERSONAJE ═══════════════════════════════════════
# El arreglo del "todos se parecen": sin esto el generador dibuja 22 veces
# la misma cara. Cada uno lleva edad, contextura, pelo y UN rasgo que lo
# hace reconocible de lejos, en la miniatura de la carta.
FISICO = {
"C01": "man in his 50s, tall and lean, silver at the temples, aquiline nose, immaculately groomed",
"C02": "man in his 40s, average build, bald with dark heavy eyebrows, permanent five-o'clock shadow",
"C03": "woman in her 30s, glamorous and poised, long honey-blonde hair, dramatic lashes, glossy lips",
"C04": "man in his 60s, heavy-set, thinning gray hair combed back, double chin, expensive suit",
"C05": "woman in her 40s, petite and wiry, dark hair in a tight bun, reading glasses pushed up on her head",
"C06": "man in his 30s, slim, long hair in a loose bun, beaded necklaces over the scrubs, wispy beard",
"C07": "woman in her 50s, sturdy and grounded, short gray-streaked curls, calm heavy-lidded eyes",
"C08": "man in his 60s, barrel-chested, full white beard, tortoiseshell glasses",
"C09": "woman in her 40s, stocky and strong, dark hair in a practical ponytail, big hoop earrings",
"C10": "man in his 40s, broad-shouldered, thick black moustache, receding hairline",
"C11": "man in his 50s, very thin, hair parted with a ruler, half-moon glasses, bow tie under the coat",
"C12": "woman in her 30s, tall, tight braids, freckles across the nose, impeccable PPE",
"C13": "young man in his 20s, skinny, messy dark hair, patchy first beard",
"C14": "man in his 30s, athletic and broad, buzzcut, thick forearms, set jaw",
"C15": "man in his 40s, medium build, salt-and-pepper hair, quick darting eyes, pen behind the ear",
"C16": "man in his 50s, soft build, pale from the reading room, round glasses, cardigan under the coat",
"C17": "man in his 50s, wiry and weathered, gray stubble, worn cap, rolled sleeves",
"C18": "young woman in her 20s, petite, dark hair in a high ponytail, small tattoo on the forearm",
"C19": "man in his 40s, compact and solid, shaved head, thick dark beard",
"C20": "man in his 30s, very tall and lanky, long neck, thin moustache, darting eyes",
"C21": "man in his 40s, medium build, neat side part, thick glasses, a row of pens in the pocket",
"C22": "woman in her 50s, imposing presence, silver hair in a severe bun, reading glasses on a chain",
}

# ══ EL ÁNIMO ══════════════════════════════════════════════════════════
# El cansancio es de UNOS POCOS, no de todos (petición del autor). Solo
# las cartas listadas aquí llevan instrucción de ánimo; el resto se dibuja
# con la expresión que pida su escena, sin ojeras impuestas.
ANIMO = {
# los que de verdad están reventados — y en quienes el cansancio ES el chiste
"C13": "MOOD: wrecked but eager — heavy dark circles, running on coffee and enthusiasm",
"C07": "MOOD: the calm tiredness of the night shift — serene, heavy-lidded, unhurried",
"C17": "MOOD: worn out and completely unbothered, has seen worse",
"R36": "MOOD: hour twenty-four — visibly exhausted, eye twitch, still standing",
"R35": "MOOD: tired but unstoppable, carrying everything without complaint",
"R37": "MOOD: bright-eyed and over-caffeinated, no tiredness at all",
# los que explícitamente NO deben salir cansados (el generador tiende a ello)
"C01": "MOOD: supremely confident and untroubled, not a worry in the world",
"C03": "MOOD: radiant, flirtatious, delighted with herself",
"C14": "MOOD: pure adrenaline and focus, wide awake",
"C19": "MOOD: unnervingly calm, mildly bored, this is a normal Tuesday",
"C22": "MOOD: composed authority, absolutely in control",
"C18": "MOOD: quietly cocky, enjoying being good at this",
"C12": "MOOD: alert and meticulous, mildly evangelical about hand hygiene",
"C09": "MOOD: brisk and businesslike, in charge of her warehouse",
"C10": "MOOD: fired up, righteous, shouting",
}

# ══ LA OVEJA NEGRA ════════════════════════════════════════════════════
# Cartas que rompen el molde A PROPÓSITO: cambian el REGISTRO de dibujo,
# nunca el encuadre ni la familia de color, para que sigan siendo del
# mismo mazo. Petición del autor: "que rompa el molde y esté en otro
# nivel, pero el encuadre debe ser el mismo".
ROMPE = {
"C03": ("STYLE BREAK — this ONE card deliberately leaves the house style: "
        "render it as glossy telenovela / fashion-magazine glamour — "
        "airbrushed skin, dramatic eyelashes, glossy lips, idealized "
        "proportions, little sparkle highlights, a beauty-shot finish. "
        "Everything else stays identical to the rest of the deck: same 2:3 "
        "framing, same subject size, same single ambient color family, same "
        "hospital background treatment. It must read as the one character "
        "who believes she is starring in a different show."),
}

MICRO = {
"C01": "se ajusta la solapa y se mira en el reflejo del vidrio",
"C02": "mira el celular, se da media vuelta y se desvanece un poco más",
"C03": "guiña un ojo y aparece la rosa",
"C04": "saca un papel del bolsillo, lo mira y lo guarda",
"C05": "mueve un imán de cama de una columna a otra",
"C06": "sopla el humo del sahumerio hacia la cámara",
"C07": "se lleva el dedo a los labios (shh)",
"C08": "pose de foto y flash",
"C09": "marca una casilla del inventario con el lápiz encadenado",
"C10": "alza el megáfono y el puño un poco más",
"C11": "baja la lupa y asiente, lento",
"C12": "rocía alcohol gel al aire",
"C13": "pasa una página y subraya",
"C14": "frota las paletas entre sí",
"C15": "timbra un papel más",
"C16": "gira la placa 90 grados y entrecierra los ojos",
"C17": "cambia de herramienta sin mirar",
"C18": "gira la muñeca, elegante",
"C19": "sorbe el café, imperturbable",
"C20": "se asoma y se esconde tras la esquina",
"C21": "abre y cierra el abrigo",
"C22": "baja los lentes y te mira por encima",
}

SIS_NOM = {"RESP": "🫁 Respiratorio", "CARD": "🫀 Cardiológico",
           "NEURO": "🧠 Neurológico", "METAB": "🧪 Metabólico",
           "QUIR": "🔪 Quirúrgico", "": ""}
TIPO_ICO = {"IMAGEN": "🩻 Imagen", "FARMACOS": "💊 Fármacos",
            "PERSONAL": "🧑‍⚕️ Personal", "PROCEDIMIENTOS": "💉 Procedimientos",
            "COMODIN": "🃏 Comodín"}

def prompt(marco, familia, escena, fisico="", animo="", rompe="",
           extra_linea=""):
    """Arma el prompt completo. El orden importa: el estilo general primero,
    el encuadre después, y al final lo que distingue a ESTA carta — físico,
    escena y ánimo — que es lo que el generador retiene con más fuerza."""
    p = (BASE + "\n" + marco + "\n"
         "AMBIENT COLOR FAMILY: " + familia + " — the whole image lives in "
         "this ONE monochromatic family; background and subject share the "
         "same color temperature.")
    if fisico:
        p += "\nWHO: " + fisico + ". This person must be instantly "
        p += "distinguishable from every other character in the deck."
    p += "\nSCENE: " + escena + "."
    if animo:
        p += "\n" + animo
    if rompe:
        p += "\n" + rompe
    if extra_linea:
        p += "\n" + extra_linea
    return p

def bloque(fh, cid, nombre, ptxt, ficha, frase, extra):
    fh.write(f"### {cid} · {nombre}\n\n")
    fh.write("```text\n" + ptxt + "\n```\n\n")
    fh.write(f"- **Descripción:** {ficha}\n")
    if frase:
        fh.write(f"- **Frase de la carta:** «{frase}»\n")
    fh.write(f"- **Añadido extra:** {extra}\n\n")

def pide_txt(p):
    IC = {"img": "🩻", "far": "💊", "per": "🧑‍⚕️", "proc": "💉"}
    return " ".join(f"{IC[k]}{p[k]}" for k in ("img", "far", "per", "proc")
                    if int(p[k]) > 0)

def main():
    pacientes = leer("cartas", "pacientes.csv")
    recursos = leer("cartas", "v030", "recursos.csv")
    acciones = leer("cartas", "v030", "acciones.csv")
    personajes = leer("cartas", "personajes.csv")

    # parejas de recursos: mismo nombre, una limpia y una ⚠️
    por_nombre = {}
    for r in recursos:
        por_nombre.setdefault(r["nombre"], []).append(r)

    ruta = os.path.join(RAIZ, "docs", "PROMPTS-ARTE.md")
    fh = open(ruta, "w", encoding="utf-8")
    fh.write("""# Los prompts del arte, carta por carta

Un prompt **completo y autosuficiente** por carta, listo para pegar en Nano
Banana (Google Flow) tal cual — no hay que armar nada. Cada uno trae el
estilo de la casa ("Retro de Guardia", BRIEF-IA §4.1), el encuadre de su
tipo de carta, su familia de color y la escena personalizada.

**Cómo usarlo:**

1. Copia el bloque de la carta y pégalo entero en el generador.
2. Si Flow acepta imagen de referencia, acompáñalo con una ilustración de
   `arte/raw/` ("match this style") — `C01-diostor.jpg` es el ancla.
3. Guarda el resultado con el **id como nombre de archivo** (`C09.png`,
   `P14.jpg`, `R30.webp`) y mándalo: la app lo integra sola.
4. Pide **2:3 vertical, mínimo 1024×1536**.

La inspiración compositiva es de ilustración de juego de mesa: una
silueta protagonista, UNA acción legible, el sujeto en el tercio central
— la carta se lee a tamaño de pulgar sobre la mesa. Las claves están
dentro de cada prompt; no lo recortes.

**El estilo de la casa se recalibró (agosto 2026)** sobre las primeras 10
imágenes reales que salieron de Flow, no sobre el ideal teórico anterior:
proporciones adultas en vez de cabezones, sombreado suave en vez de color
plano, línea media en vez de gruesa. Lo que sí se mantuvo intacto es lo
que estaba funcionando: **cada imagen vive en UNA sola familia de color**,
que es lo que hará que 115 cartas se vean del mismo mazo.

Tres reglas nuevas que vale la pena conocer:

1. **El cansancio es de unos pocos, no de todos.** El bloque anterior
   pedía "caras cansadas y ojeras" en las 115 cartas — por eso todos los
   personajes salían siendo la misma persona agotada. Ahora el ánimo se
   define carta por carta (`MOOD`), y solo 5 lo piden: el Residente, la
   Enfermera de Noche, el Multiuso, el Turno Extra y el Técnico. A varios
   se les prohíbe explícitamente salir cansados.
2. **Cada personaje trae su físico** (`WHO`): edad, contextura, pelo y un
   rasgo reconocible de lejos. Es el otro arreglo del "todos se parecen".
3. **Las Acciones tienen que dar risa.** Su encuadre exige construir el
   cuadro alrededor de UN chiste visual y exagerar más que en el resto
   del mazo.

**La oveja negra:** *Doctor Amor* (C03) rompe el molde a propósito —
registro de telenovela glamorosa, otro nivel de dibujo— pero conserva
encuadre, tamaño de sujeto y familia de color, así que sigue siendo del
mismo mazo. Si quieres que otra carta sea la excepción (o agregar más),
es una línea en el diccionario `ROMPE` de
`tools/generar_prompts_arte.py`.

> ⚠️ **Fija la proporción en el selector, no solo en el texto.** En la
> primera tanda salieron verticales, cuadradas y apaisadas mezcladas.
> Usa **3:4 vertical** en todas — es la opción de retrato más común y
> calza casi exacto con una carta de póker real (63×88 mm = 0,716; 3:4 =
> 0,75). Si tampoco estuviera: 1:1 antes que 9:16, y **nunca apaisado**.
>
> ⚠️ **La cara va en la mitad de arriba.** La app muestra en la mano solo
> una franja ancha recortada del **borde superior** de la imagen: si el
> personaje queda centrado verticalmente, en la carta se ve el techo de la
> sala. Los ojos, más o menos a un tercio desde arriba. Ya va escrito en
> cada prompt, pero conviene revisarlo al elegir entre variantes.
>
> ⚠️ Pide **máximo dos palabras** de texto dentro de la imagen: las frases
> largas salen cortadas.

**El orden sugerido:** los 22 personajes primero (fijan las caras del
juego), después los 26 pacientes, después recursos, y al final Acciones
y el Sumario.

---

## 1. Personajes — los avatares (22)

Cuerpo entero, pose característica, ~70% del cuadro. **El escenario rota
con cada personaje** — no todos viven en la UCI: la de Abastecimiento
está en su bodega, el Dirigente afuera del hospital. El añadido extra de
cada uno trae la micro-acción para el **retrato vivo** (pide las
variantes como image-to-image sobre la imagen final: *"same exact image,
eyes closed"* y *"same exact image, <micro-acción>"*).

""")
    hab = {c["id"]: c for c in personajes}
    for c in personajes:
        cid = c["id"]
        escena, fam_noct = EC[cid]
        fam = fam_noct or FAM[""]
        ptxt = prompt(MARCO_C, fam, escena, fisico=FISICO.get(cid, ""),
                      animo=ANIMO.get(cid, ""), rompe=ROMPE.get(cid, ""))
        ficha = f"{c['frecuencia']} — {c['habilidad']}"
        extra = ""
        if cid in ROMPE:
            extra += ("🐑 **OVEJA NEGRA**: esta carta rompe el estilo a "
                      "propósito (otro registro de dibujo) pero conserva "
                      "encuadre, tamaño de sujeto y familia de color. Es la "
                      "excepción que confirma el mazo. ")
        extra += (f"Retrato vivo: variante 1 «same exact image, eyes closed»; "
                  f"variante 2 «same exact image, {MICRO[cid]}» (tradúcela al "
                  f"inglés al pedirla). Manda las 3 como {cid}.png, "
                  f"{cid}-b.png y {cid}-c.png.")
        bloque(fh, cid, c["nombre"], ptxt, ficha, c["frase"], extra)

    fh.write("""---

## 2. Pacientes (26)

Busto frontal, del pecho a la cabeza, luz suave; el monitor y el
portasueros van detrás, simplificados. El estado clínico lo marca la
gravedad (ya viene descrito dentro de cada prompt). La frase de la carta
es el chiste — y el prompt ya la convirtió en escena.

""")
    for p in pacientes:
        pid = p["id"]
        fam = FAM.get(p["sistema"], FAM[""])
        escena = EP[pid] + ". Clinical state: " + GRAV[p["gravedad"]]
        ptxt = prompt(MARCO_P, fam, escena)
        ficha = (f"Gravedad {p['gravedad']} · {SIS_NOM.get(p['sistema'],'')} · "
                 f"❤️{p['vida']} · pide {pide_txt(p)} · alta +{p['puntos_alta']} "
                 f"/ fallece {p['puntos_fallece']}")
        extra = {"I": "El más liviano del mazo: la comedia manda, cero cables.",
                 "II": "Punto medio: enfermo de verdad, humor intacto.",
                 "III": "Aquí el monitor es co-protagonista; el humor se vuelve negro.",
                 "ROJO": "La escena más extrema del mazo — que asuste un poco."
                 }[p["gravedad"]]
        bloque(fh, pid, p["nombre"], ptxt, ficha, p["frase"], extra)

    fh.write("""---

## 3. Recursos — el Mazo de Guardia (44 diseños)

El objeto casi aislado, 3/4 o frontal, ~60% del cuadro, sobre fondo
monocromo ambiental (nunca blanco). **Los 🧑‍⚕️ Personal son personas**:
busto o medio cuerpo en su gesto de trabajo. Las parejas (misma carta
limpia y con ⚠️) comparten objeto y encuadre: genera primero la limpia y
pide la complicada como variación de la misma imagen.

""")
    for r in recursos:
        rid = r["id"]
        fam = FAM.get(r["sistema"], FAM[""])
        marco = MARCO_RP if r["tipo"] in ("PERSONAL",) else MARCO_R
        if r["tipo"] == "COMODIN":
            marco = MARCO_RP if rid == "R42" else MARCO_R
        ptxt = prompt(marco, fam, ER[rid], animo=ANIMO.get(rid, ""))
        partes = [TIPO_ICO.get(r["tipo"], r["tipo"])]
        if r["sistema"]:
            partes.append(f"{SIS_NOM[r['sistema']]} ×2")
        if r["comodin"] == "si":
            partes.append("vale por cualquier tipo")
        if r["previene"]:
            partes.append(f"🛡️ previene {r['previene']}")
        if r["complicacion"] == "si":
            partes.append(f"⚠️ {r['comp_nombre']}")
        ficha = " · ".join(partes) + f" · {r['copias']} copia(s)"
        gemela = [x["id"] for x in por_nombre[r["nombre"]] if x["id"] != rid]
        extras = []
        if gemela:
            cual = "LIMPIA" if r["complicacion"] == "no" else "COMPLICADA"
            extras.append(f"Pareja con {gemela[0]} — esta es la versión "
                          f"{cual}: mismo objeto, mismo encuadre; cambia "
                          f"solo lo que sale mal.")
        elif r["complicacion"] == "si":
            extras.append("Sin gemela limpia: la complicación vive en la "
                          "misma imagen.")
        if r["sistema"]:
            extras.append("Lleva chip de sistema: en la app esta carta luce "
                          "la banda iridiscente al verla en grande.")
        if not extras:
            extras.append("Carta única, sin pareja.")
        bloque(fh, rid, r["nombre"], ptxt, ficha, r["frase"], " ".join(extras))

    fh.write("""---

## 4. Protocolos — las Acciones (22 diseños)

Escena mínima: una o dos figuras o un elemento en movimiento; la emoción
manda sobre el detalle. Aquí la paleta se suelta por tipo — ataque
rojizo, apoyo cálido, caos nocturno, respuesta serena, extrema oscura —
y ya viene puesta en cada prompt.

""")
    for a in acciones:
        aid = a["id"]
        fam = FAM_ACC.get(a["tipo"], FAM[""])
        ptxt = prompt(MARCO_A, fam, EA[aid])
        ficha = f"{a['tipo']} · coste {a['coste']} · {a['texto']}"
        extra = {"ATAQUE": "Conflicto de pasillo: que se note quién pierde.",
                 "APOYO": "Cooperación: manos que entregan, alivio visible.",
                 "CAOS": "Todo pasando a la vez; el desorden es el chiste.",
                 "RESPUESTA": "El gesto de DETENER algo en el aire.",
                 "EXTREMA": "El gesto más grande del mazo: respeto y humor negro a partes iguales."
                 }.get(a["tipo"], "")
        bloque(fh, aid, a["nombre"], ptxt, ficha, a["frase"], extra)

    fh.write("""---

## 5. El Sumario Administrativo (1)

""")
    ptxt = prompt(
        "OBJECT CARD: a single document as the whole threat, filling the "
        "frame with its shadow.",
        "cold gray-teal bureaucratic palette (#5f7a80)",
        "a manila folder bristling with red stamps and seals, grown huge, "
        "casting a long shadow over a tiny clinician's desk below; one "
        "paper clip like a padlock")
    bloque(fh, "S01", "Sumario Administrativo", ptxt,
           "La sanción del juego: cada Sumario abierto muerde 1 carta del "
           "límite de mano; cerrarlo cuesta 2 cartas.",
           "El proceso será justo, transparente y eterno.",
           "Burocracia como amenaza: el documento es el monstruo. Una sola "
           "imagen para las 6 copias.")

    fh.write("""---

*Generado con `python3 tools/generar_prompts_arte.py` sobre los CSV
vivos del repo — si una carta cambia de nombre o habilidad, regenerar.
Los prompts son autosuficientes: el estilo, el encuadre, el color y la
escena van adentro de cada bloque.*
""")
    fh.close()
    n = open(ruta, encoding="utf-8").read().count("```text")
    print(f"✔ {ruta} — {n} prompts")

    # nada puede quedar sin escena
    faltan = ([p["id"] for p in pacientes if p["id"] not in EP] +
              [r["id"] for r in recursos if r["id"] not in ER] +
              [a["id"] for a in acciones if a["id"] not in EA] +
              [c["id"] for c in personajes if c["id"] not in EC])
    if faltan:
        print("⚠️ SIN ESCENA:", faltan); sys.exit(1)

if __name__ == "__main__":
    main()
