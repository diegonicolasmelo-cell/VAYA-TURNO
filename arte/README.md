# arte/ — Las ilustraciones de ¡VAYA TURNO!

El estilo canónico ("Retro de Guardia") está definido en
**[`../docs/ARTE.md`](../docs/ARTE.md)** §2: ligne claire de trazo grueso,
colores planos con cel shading mínimo, y **una familia de color monocroma
por imagen**. Fuente: las 39 ilustraciones finales del autor, recuperadas de
su Drive (carpeta "cartas vaya turno", 452 archivos) el 2026-08-18.

## Estructura

| Carpeta | Qué hay |
|---|---|
| `raw/` | Ilustraciones aprobadas, **nombradas por ID de carta** (`R29-carro-de-paro.jpg`). Son las que `generar_pnp.py` montará en las cartas. |
| `raw/extra/` | Las finales sin carta en la caja base: material listo para expansiones (Módulo Experiencia, METAB, RESP) o como variantes. |
| `referencias/` | El tablero de la UCI (`tablero-uci.jpg`) y la plantilla de carta vacía (`plantilla-carta.jpg`). No se imprimen: orientan el layout. |
| `final/` | Salida de `tools/normalizar_arte.py` cuando se normalice el lote completo. |

## Cobertura actual (18 / 124)

**Avatares (4/6):** C01 Diostor · C03 Doctor Amor · C05 Gestora · C06 Esotérico (el Chamán).
Faltan: C02 Médico Fantasma · C04 Director del Hospital.

**Recursos (11/43):** R16 Radiografía · R18 Ecografía · R20 TAC · R29 Carro de Paro ·
R30 Ventilación Mecánica · R34 Enfermera de UCI · R35/R36 Técnico (Reemplazo) ·
R37 Interno (Interno de Medicina) · R39 Kinesiólogo Respiratorio (Kinesaurio) ·
R42 Médico General de Turno (Médico Becado).

**Eventos (1/28):** E09 Paro Cardiorrespiratorio.
**Acciones (2/20):** A18 Recorte Presupuestario ("no hay plata") · A20 Muestra Hemolizada.

## En `extra/` (24 piezas para el futuro)

- **Módulo Experiencia / Personal con Apellido:** Médico Senior, Residente Yeta,
  En orientación, Reemplazo (3), Influencer, Enfermante ×2, Enfermera insegura,
  Enfermera tierna, Don Bisturí, y los 8 kinesiólogos restantes (Don Paper,
  Kine Chill, FAT, FIT, motora, Kinebriólogo, Perillero ×2, Sita Kine).
- **Expansiones de sistema:** Hemodiálisis + Enfermera de hemodiálisis (METAB),
  Oxigenoterapia (RESP).
- **Variantes:** Chamán (2), Carro de paro (2).

## Dónde está el resto del material

En el Drive del autor quedan **~180 escenas más en el estilo canónico**
(candidatas a Eventos y Acciones — hay que curarlas una a una), ~45 mockups
de carta con texto IA ilegible (solo referencia de layout), y ~90 fotos de
referencia/stock. **Lo con marca de agua (Getty/Dreamstime/123RF) no se usa:
no hay derechos.**

## Cómo generar las ~106 que faltan

1. Abre Gemini/Whisk y carga 2–3 anclas: `raw/C01-diostor.jpg`,
   `raw/R29-carro-de-paro.jpg`, `raw/extra/oxigenoterapia-soporte-vital.jpg`.
2. Copia el prompt del batch desde `tools/prompts-todos.txt` (ya llevan el
   bloque de estilo y la familia de color del sistema embebidos).
3. Guarda lo aprobado en `raw/` con su ID de carta.
4. Al final: `python3 tools/normalizar_arte.py --entrada arte/raw --salida arte/final`.
