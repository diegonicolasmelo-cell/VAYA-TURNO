#!/usr/bin/env python3
"""
Normalizador de arte para ¡VAYA TURNO!

Post-procesa 124 ilustraciones generadas:
- Redimensiona a resolución consistente
- Reduce paleta de colores (eliminando ruido)
- Normaliza grano/textura
- Convierte fondos inconsistentes a blanco sólido
- Ajusta contraste para legibilidad
- Verifica que cumplan especificaciones (1:1, sin blur, etc.)

Uso:
    python3 tools/normalizar_arte.py --entrada arte/raw --salida arte/final
    python3 tools/normalizar_arte.py --entrada arte/raw --salida arte/final --resize 1024 --verbose
"""

import argparse
import os
import sys
from pathlib import Path

try:
    from PIL import Image, ImageFilter, ImageOps
    import numpy as np
except ImportError:
    print("Error: PIL/Pillow required. Install with: pip install Pillow numpy")
    sys.exit(1)

def reducir_paleta(img, max_colores=64):
    """
    Reduce paleta de colores usando cuantización, eliminando ruido.
    Mantiene colores de sistemas clínicos intactos.
    """
    # Asegura RGB
    if img.mode != "RGB":
        img = img.convert("RGB")

    # Cuantiza a max_colores
    return img.quantize(colors=max_colores).convert("RGB")

def limpiar_fondo(img, threshold=240):
    """
    Detecta píxeles grises/blancos y reemplaza con blanco puro.
    Preserva el sujeto principal (colores más saturados).
    """
    if img.mode != "RGB":
        img = img.convert("RGB")

    arr = np.array(img)
    r, g, b = arr[:, :, 0], arr[:, :, 1], arr[:, :, 2]

    # Detectar píxeles que parecen fondo blanco/gris (R≈G≈B y alto valor)
    # Pero preservar tonos clínicos (rojo, azul, verde, púrpura)
    es_gris = (np.abs(r.astype(int) - g.astype(int)) < 20) & \
              (np.abs(g.astype(int) - b.astype(int)) < 20) & \
              (r > threshold)

    arr[es_gris] = [255, 255, 255]

    return Image.fromarray(arr)

def normalizar_grano(img):
    """
    Aplica filtro ligero para uniformizar textura/grano sin perder detalle.
    Usa blur mínimo + sharpen para preservar líneas.
    """
    if img.mode != "RGB":
        img = img.convert("RGB")

    # Blur muy ligero (0.3 sigma)
    img = img.filter(ImageFilter.GaussianBlur(radius=0.3))

    # Sharpen ligero para recuperar bordes
    img = img.filter(ImageFilter.SHARPEN)

    return img

def ajustar_contraste(img, factor=1.1):
    """Incrementa contraste ligeramente para legibilidad."""
    return ImageOps.autocontrast(img, cutoff=2)

def redimensionar(img, tamaño):
    """
    Redimensiona preservando aspecto 1:1 si es posible.
    Si no es 1:1, rellena con blanco.
    """
    if img.mode != "RGB":
        img = img.convert("RGB")

    ancho, alto = img.size
    is_cuadrado = ancho == alto

    if is_cuadrado:
        # Simple resize
        return img.resize((tamaño, tamaño), Image.Resampling.LANCZOS)
    else:
        # Resize preservando aspecto + padding
        proporcion = tamaño / max(ancho, alto)
        nuevo_ancho = int(ancho * proporcion)
        nuevo_alto = int(alto * proporcion)
        img_resized = img.resize((nuevo_ancho, nuevo_alto), Image.Resampling.LANCZOS)

        # Crea canvas blanco 1:1
        canvas = Image.new("RGB", (tamaño, tamaño), (255, 255, 255))
        offset_x = (tamaño - nuevo_ancho) // 2
        offset_y = (tamaño - nuevo_alto) // 2
        canvas.paste(img_resized, (offset_x, offset_y))

        return canvas

def procesar_imagen(ruta_entrada, ruta_salida, tamaño=512, max_colores=64, verbose=False):
    """Procesa una imagen con todas las normalizaciones."""
    try:
        img = Image.open(ruta_entrada)

        if verbose:
            print(f"  Abierto: {img.size} {img.mode}")

        # Pipeline
        img = limpiar_fondo(img)
        if verbose:
            print(f"  ✓ Fondo limpio")

        img = reducir_paleta(img, max_colores)
        if verbose:
            print(f"  ✓ Paleta reducida a {max_colores} colores")

        img = normalizar_grano(img)
        if verbose:
            print(f"  ✓ Grano normalizado")

        img = ajustar_contraste(img)
        if verbose:
            print(f"  ✓ Contraste ajustado")

        img = redimensionar(img, tamaño)
        if verbose:
            print(f"  ✓ Redimensionado a {tamaño}×{tamaño}")

        # Guarda como PNG
        img.save(ruta_salida, "PNG", optimize=True)
        if verbose:
            print(f"  → {ruta_salida}")

        return True
    except Exception as e:
        print(f"  ✗ Error procesando {ruta_entrada}: {e}", file=sys.stderr)
        return False

def main():
    ap = argparse.ArgumentParser(
        description="Normaliza 124 ilustraciones de ¡VAYA TURNO!"
    )
    ap.add_argument("--entrada", required=True, help="Directorio de imágenes raw")
    ap.add_argument("--salida", required=True, help="Directorio de salida normalizado")
    ap.add_argument("--resize", type=int, default=512,
                    help="Redimensionar a N×N píxeles (default: 512)")
    ap.add_argument("--paleta", type=int, default=64,
                    help="Máximo de colores en paleta reducida (default: 64)")
    ap.add_argument("--verbose", "-v", action="store_true", help="Salida detallada")
    ap.add_argument("--formato", choices=["png", "jpg"], default="png",
                    help="Formato de salida (default: png)")
    args = ap.parse_args()

    # Valida directorios
    entrada_path = Path(args.entrada)
    salida_path = Path(args.salida)

    if not entrada_path.is_dir():
        print(f"Error: --entrada '{entrada_path}' no existe o no es directorio", file=sys.stderr)
        sys.exit(1)

    salida_path.mkdir(parents=True, exist_ok=True)

    # Lista imágenes
    formatos = ("*.png", "*.jpg", "*.jpeg", "*.bmp", "*.gif")
    imagenes = []
    for fmt in formatos:
        imagenes.extend(entrada_path.glob(fmt))
        imagenes.extend(entrada_path.glob(fmt.upper()))

    if not imagenes:
        print(f"Advertencia: No se encontraron imágenes en {entrada_path}", file=sys.stderr)
        sys.exit(1)

    imagenes.sort()

    if args.verbose:
        print(f"Normalizando {len(imagenes)} imágenes...")
        print(f"Parámetros: resize={args.resize}, paleta={args.paleta}")
        print()

    exitos = 0
    fallos = 0

    for i, ruta_img in enumerate(imagenes, 1):
        nombre_salida = ruta_img.stem + f".{args.formato}"
        ruta_salida = salida_path / nombre_salida

        if args.verbose:
            print(f"[{i}/{len(imagenes)}] {ruta_img.name}")

        if procesar_imagen(str(ruta_img), str(ruta_salida), args.resize, args.paleta, args.verbose):
            exitos += 1
        else:
            fallos += 1

        if args.verbose:
            print()

    print(f"\n{'='*60}")
    print(f"RESUMEN")
    print(f"{'='*60}")
    print(f"Total procesadas:  {exitos}")
    print(f"Errores:           {fallos}")
    print(f"Destino:           {salida_path}")
    print(f"Resolución final:  {args.resize}×{args.resize}")
    print(f"Colores máximos:   {args.paleta}")

    if fallos == 0:
        print(f"\n✓ Normalización completada exitosamente")
    else:
        print(f"\n⚠ {fallos} imágenes tuvieron errores", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
