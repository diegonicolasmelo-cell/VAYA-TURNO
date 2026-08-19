# Cartas retiradas

## `eventos-centinela-v013.csv` — el Mazo de Eventos Centinela

**Retirado en v0.14.** Sus 28 cartas dejaron de existir como mazo: cada
símbolo ⚠️ del Mazo de Guardia **trae ahora su propia complicación impresa**,
ligada al recurso que la causa (la Ventilación Mecánica trae la neumonía
asociada a ventilación mecánica, el catéter trae la bacteriemia, el
antibiótico trae la resistencia). Ver `docs/REGLAMENTO.md` §7 y
`docs/DISENO.md` §4c.

**Por qué se guarda:** unas 21 de las 28 se reabsorbieron en las 17
complicaciones de `recursos.csv` (columnas `comp_*`), pero el archivo
conserva el texto original de todas, incluidas las que no tenían recurso
anfitrión: *Corte de Suministro*, *Paro Cardiorrespiratorio*, *Hemorragia
Masiva*, *Cambio de Turno Caótico*. Son candidatas naturales a cartas de
Acción de tipo CAOS o a material de expansión.

No las borres: es contenido escrito y probado, solo que sin mazo donde vivir.
