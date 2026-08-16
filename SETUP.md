# Setup · ¡VAYA TURNO!

Instrucciones para configurar el entorno y ejecutar los generadores.

## Requisitos Base

- **Python 3.9+**
- **Navegador moderno** (Chrome, Firefox, Safari, Edge)

## Paso 1: Verificar Instalación

```bash
python3 --version
# Debe ser 3.9 o superior
```

## Paso 2: Instalar Dependencias (Opcional)

Si planeas **normalizar ilustraciones** (herramienta `normalizar_arte.py`), instala Pillow:

```bash
pip install Pillow numpy
```

**Nota:** Los otros herramientas (`generar_taller.py`, `generar_pnp.py`, `prompts.py`, `simular.py`) 
no requieren dependencias externas — solo Python.

## Herramientas Disponibles

### 1. Taller de Guardia (Editor Visual)

```bash
python3 tools/generar_taller.py && open taller.html
```

Muestra:
- **Galería de 159 cartas** con búsqueda y filtros por sistema
- **Monitor de balance** con métricas por tipo
- **Editor en vivo** (edita CSV sin rechazar cambios)
- **Banco de Pruebas** (ejecuta simulador en el navegador, 300–3.000 partidas)

### 2. Generador de Print-and-Play

```bash
python3 tools/generar_pnp.py
# Genera: pnp.html (159 cartas en A4, listos para imprimir y recortar)

# Con ilustraciones (opcional):
python3 tools/generar_pnp.py --arte arte/final
```

### 3. Simulador de Balance

```bash
python3 tools/simular.py --partidas 2000 --rondas 8 --jugadores 3

# Opciones:
python3 tools/simular.py --help
```

Valida que el juego mantenga 55–70% de salvamento (objetivo de diseño).

### 4. Generador de Prompts para IA

```bash
# Generar todos los prompts
python3 tools/prompts.py --salida prompts-todos.txt

# O por tipo:
python3 tools/prompts.py --tipo pacientes
python3 tools/prompts.py --tipo recursos
python3 tools/prompts.py --tipo eventos
python3 tools/prompts.py --tipo acciones
python3 tools/prompts.py --tipo personajes
python3 tools/prompts.py --tipo sumarios
```

Genera **124 prompts listos para copiar-pega** en ChatGPT, DALL-E 3, Google Whisk o Stable Diffusion.

Incluye automáticamente el **bloque de estilo global** para coherencia visual.

### 5. Normalizador de Ilustraciones

```bash
# Redimensiona, reduce paleta, limpia fondo, ajusta contraste
python3 tools/normalizar_arte.py \
  --entrada arte/raw \
  --salida arte/final \
  --resize 512 \
  --paleta 64

# Requiere Pillow instalado (ver Paso 2)
```

Opciones:
- `--resize N`: Redimensionar a N×N píxeles (default: 512)
- `--paleta N`: Máximo colores en cuantización (default: 64)
- `--formato {png,jpg}`: Formato de salida (default: png)
- `--verbose`: Salida detallada

## Flujo Recomendado: Desarrollo

### Para Editores de Cartas

```bash
# 1. Abre el Taller (ve y edita cartas en vivo)
python3 tools/generar_taller.py && open taller.html

# 2. Modifica cartas en CSV (cartas/*.csv)

# 3. Vuelve al Taller, el cambio aparece instantáneamente

# 4. Corre el Banco de Pruebas en el Taller para simular partidas
# (o en terminal: python3 tools/simular.py --partidas 1000)

# 5. Cuando esté listo, regenera PnP
python3 tools/generar_pnp.py
```

### Para Generación de Ilustraciones

```bash
# 1. Lee docs/ARTE.md para entender el motor visual

# 2. Genera los 124 prompts
python3 tools/prompts.py --salida prompts-todos.txt

# 3. Copia prompts desde prompts-todos.txt y úsalos en:
#    - ChatGPT + DALL-E 3
#    - Google Whisk (image-to-image para variaciones)
#    - Stable Diffusion local

# 4. Guarda las 124 imágenes en arte/raw/

# 5. Normaliza el lote
python3 tools/normalizar_arte.py --entrada arte/raw --salida arte/final --resize 512

# 6. Regenera PnP con ilustraciones
python3 tools/generar_pnp.py --arte arte/final
```

## Flujo Recomendado: Playtest

```bash
# 1. Asegúrate que el balance es sano (simula 3.000 partidas)
python3 tools/simular.py --partidas 3000

# 2. Genera el PnP listo para imprimir
python3 tools/generar_pnp.py

# 3. Abre pnp.html, imprime en A4 (márgenes mínimos, con gráficos de fondo)

# 4. Recorta las cartas

# 5. Lee docs/PLAYTEST.md para el plan de 3 sesiones
```

## Archivos Generados

| Archivo | Descripción |
|---------|-------------|
| `taller.html` | Editor visual (15 MB, actualizado en `~1s` tras cambio CSV) |
| `pnp.html` | Print-and-play (32 páginas A4, ~2 MB) |
| `prompts-todos.txt` | 124 prompts ordenados por batch (~80 KB) |
| `arte/raw/` | Ilustraciones originales (usuario) |
| `arte/final/` | Ilustraciones normalizadas (post-procesadas) |

## Solución de Problemas

### El Taller tarda mucho en abrir

El taller es un HTML monolítico (~80 KB minificado). En navegadores antiguos puede tardar 2–3s.
Solución: Usa Chrome o Firefox recientes.

### El simulador dice "Necesitas al menos un paciente y un recurso"

Verificar que `cartas/pacientes.csv` y `cartas/recursos.csv` tengan al menos una fila con `copias > 0`.

### `normalizar_arte.py` falla con "PIL required"

Instala Pillow:
```bash
pip install Pillow numpy
```

### Las ilustraciones se ven pixeladas tras normalización

Aumenta `--resize`:
```bash
python3 tools/normalizar_arte.py --entrada arte/raw --salida arte/final --resize 1024
```

### El PnP no muestra ilustraciones

Verifica que:
1. Las imágenes existen en `arte/final/`
2. Los nombres coinciden con los IDs de cartas (ej: `arte/final/paciente-P01.png`)
3. Ejecutaste: `python3 tools/generar_pnp.py --arte arte/final`

## Uso en GitHub Actions / CI

```bash
#!/bin/bash
set -e

# Valida CSV
python3 tools/simular.py --partidas 300

# Genera PnP
python3 tools/generar_pnp.py

# Genera prompts (por si acaso)
python3 tools/prompts.py --salida prompts-todos.txt

echo "✓ Build OK"
```

## Referencias

- **[docs/REGLAMENTO.md](docs/REGLAMENTO.md)** — Reglas completas
- **[docs/DISENO.md](docs/DISENO.md)** — Números y su justificación
- **[docs/ARTE.md](docs/ARTE.md)** — Motor de ilustraciones
- **[docs/PLAYTEST.md](docs/PLAYTEST.md)** — Plan de sesiones y qué medir
- **[cartas/README.md](cartas/README.md)** — Especificación de CSVs

---

**Última actualización:** 2026-08-16  
**Versión:** v0.12
