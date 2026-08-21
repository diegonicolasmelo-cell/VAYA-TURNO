#!/usr/bin/env python3
"""Exporta el Print & Play a un PDF A4 listo para enviar a una imprenta o a un amigo.

Regenera pnp.html desde los CSV y lo imprime a PDF con Chromium (Playwright).

    python3 tools/exportar_pdf.py
    python3 tools/exportar_pdf.py --salida /ruta/VAYA-TURNO.pdf

    python3 tools/exportar_pdf.py --formato carta

El PDF sale sin márgenes de navegador, en A4 exacto (210×297 mm) o Carta
exacta (216×279 mm). Las cartas miden 63×88 mm reales —el tamaño estándar,
el de Mitos y Leyendas o Magic— SIEMPRE QUE se imprima al 100% ("tamaño
real"), nunca con "ajustar a la página".
"""
import argparse
import asyncio
import pathlib
import subprocess
import sys

RAIZ = pathlib.Path(__file__).resolve().parent.parent
CHROMIUM = "/opt/pw-browsers/chromium"


PAPEL = {"a4": "A4", "carta": "Letter"}


async def a_pdf(html: pathlib.Path, salida: pathlib.Path, formato: str = "a4",
                horizontal: bool = False):
    from playwright.async_api import async_playwright

    async with async_playwright() as p:
        kwargs = {}
        if pathlib.Path(CHROMIUM).exists():
            kwargs["executable_path"] = CHROMIUM
        navegador = await p.chromium.launch(**kwargs)
        pagina = await navegador.new_page()
        await pagina.goto(html.as_uri())
        await pagina.pdf(
            path=str(salida),
            format=PAPEL[formato],
            landscape=horizontal,
            print_background=True,
            margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
        )
        await navegador.close()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--salida", default=str(RAIZ / "VAYA-TURNO-imprimible.pdf"))
    ap.add_argument("--html", default=str(RAIZ / "pnp.html"))
    ap.add_argument("--formato", choices=list(PAPEL), default="a4",
                    help="pliego: a4 (por defecto) o carta / Letter")
    ap.add_argument("--horizontal", action="store_true",
                    help="pliego apaisado (tableros)")
    ap.add_argument("--no-regenerar", action="store_true",
                    help="usa el pnp.html existente sin volver a generarlo")
    args = ap.parse_args()

    html = pathlib.Path(args.html).resolve()
    if not args.no_regenerar:
        subprocess.run([sys.executable, str(RAIZ / "tools" / "generar_pnp.py"),
                        "--salida", str(html),
                        "--formato", args.formato], check=True)

    salida = pathlib.Path(args.salida).resolve()
    asyncio.run(a_pdf(html, salida, args.formato, args.horizontal))
    kb = salida.stat().st_size // 1024
    print(f"✔ {salida} ({kb} KB)")
    print(f"  Al imprimir: {PAPEL[args.formato]} · tamaño real / 100% · "
          f"NO 'ajustar a la página'.")


if __name__ == "__main__":
    main()
