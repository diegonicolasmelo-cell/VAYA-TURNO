#!/usr/bin/env python3
"""
Generador de print-and-play para ¡VAYA TURNO!

Lee los CSV de cartas/ y produce un HTML listo para imprimir (Ctrl+P →
"Guardar como PDF", tamaño A4, márgenes mínimos, activar gráficos de fondo).
Cartas de 63×88 mm, 9 por página. Sin dependencias: solo stdlib.

Uso:
    python3 tools/generar_pnp.py                    # todo
    python3 tools/generar_pnp.py --solo pacientes   # un mazo
    python3 tools/generar_pnp.py --salida /tmp/x.html
"""

import argparse
import csv
import html
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CARTAS = os.path.join(RAIZ, "cartas")

SIM = {"IMAGEN": "🩻", "FARMACOS": "💊", "PERSONAL": "🧑‍⚕️", "MONITOREO": "📈"}
NOM = {"IMAGEN": "Imagen", "FARMACOS": "Fármacos",
       "PERSONAL": "Personal", "MONITOREO": "Monitoreo"}
GRAV = {
    "I":    ("Gravedad I · Observación", "g1"),
    "II":   ("Gravedad II · Grave", "g2"),
    "III":  ("Gravedad III · Crítico", "g3"),
    "ROJO": ("★ CÓDIGO ROJO", "gr"),
}

CSS = """
:root{--tinta:#14202b;--suave:#5b6b7a;--linea:#c8d3dc;--papel:#fff}
*{box-sizing:border-box}
body{margin:0;background:#e9eef2;font-family:"Helvetica Neue",Arial,sans-serif;color:var(--tinta)}
.hoja{width:210mm;min-height:297mm;margin:0 auto 6mm;padding:6mm;background:var(--papel);
      display:grid;grid-template-columns:repeat(3,63mm);
      gap:0;justify-content:center;align-content:start;grid-auto-rows:min-content}
.carta{width:63mm;height:88mm;border:.25mm dashed var(--linea);padding:3.4mm;
       display:flex;flex-direction:column;overflow:hidden;background:var(--papel)}
.cab{display:flex;justify-content:space-between;align-items:flex-start;gap:2mm}
.nombre{font-size:3.5mm;font-weight:700;line-height:1.12;letter-spacing:-.01em}
.vida{font-size:5.2mm;font-weight:800;white-space:nowrap;line-height:1}
.tipo{font-size:2.35mm;text-transform:uppercase;letter-spacing:.09em;color:var(--suave);
      margin-top:1.2mm;font-weight:700}
.banda{height:1.6mm;margin:2mm -3.4mm;flex:none}
.g1 .banda{background:#4a9d6e}.g2 .banda{background:#d99c2b}
.g3 .banda{background:#c0492f}.gr .banda{background:#14202b}
.req{display:grid;grid-template-columns:1fr 1fr;gap:1mm 2mm;margin:1mm 0}
.req div{font-size:3.5mm;font-weight:700}
.req .off{color:#c3ccd4;font-weight:400}
.glifo{font-size:13mm;text-align:center;margin:auto 0;line-height:1}
.cuerpo{font-size:2.95mm;line-height:1.32;margin:1.5mm 0}
.pie{margin-top:auto;padding-top:1.6mm;border-top:.25mm solid var(--linea)}
.pts{display:flex;justify-content:space-between;font-size:2.9mm;font-weight:700;margin-bottom:1mm}
.frase{font-size:2.55mm;font-style:italic;color:var(--suave);line-height:1.28}
.warn{font-size:2.5mm;font-weight:700;color:#c0492f;letter-spacing:.04em}
.et{display:inline-block;font-size:2.2mm;font-weight:700;letter-spacing:.07em;
    border:.25mm solid var(--tinta);border-radius:1mm;padding:.3mm 1mm;margin-top:1mm}
.hab{font-size:2.75mm;line-height:1.3;margin-bottom:1.5mm}
.hab b{display:block;font-size:2.35mm;text-transform:uppercase;letter-spacing:.08em;color:var(--suave)}
.sep{grid-column:1/-1;font-size:3.4mm;font-weight:800;text-transform:uppercase;
     letter-spacing:.12em;padding:0 0 1.5mm;border-bottom:.4mm solid var(--tinta);margin-bottom:1.5mm}
.arte{flex:1;min-height:0;margin:1.5mm 0;border:.25mm dashed #dde4ea;border-radius:1mm;
      display:flex;align-items:center;justify-content:center;
      font-size:2.3mm;color:#c3ccd4;letter-spacing:.08em;text-transform:uppercase}
@media print{body{background:none}.hoja{margin:0;box-shadow:none;page-break-after:always}}
@page{size:A4;margin:0}
"""

E = html.escape


def leer(nombre):
    with open(os.path.join(CARTAS, nombre), encoding="utf-8") as f:
        return list(csv.DictReader(f))


def carta_paciente(p):
    etiqueta, cls = GRAV[p["gravedad"]]
    req = "".join(
        f'<div class="{"" if int(p[c]) else "off"}">{SIM[t]} ×{p[c]}</div>'
        for t, c in (("IMAGEN", "img"), ("FARMACOS", "far"),
                     ("PERSONAL", "per"), ("MONITOREO", "mon"))
    )
    return f"""<div class="carta {cls}">
  <div class="cab"><div><div class="nombre">{E(p['nombre'])}</div>
    <div class="tipo">{E(etiqueta)}</div></div><div class="vida">❤️{p['vida']}</div></div>
  <div class="banda"></div>
  <div class="tipo">Requiere</div><div class="req">{req}</div>
  <div class="arte">ilustración</div>
  <div class="pie"><div class="pts"><span>Alta +{p['puntos_alta']}</span>
    <span>Fallece {p['puntos_fallece']}</span></div>
    <div class="frase">{E(p['frase'])}</div></div>
</div>"""


def carta_recurso(r):
    et = f'<div class="et">{E(r["etiqueta"])}</div>' if r["etiqueta"] else ""
    wa = '<div class="warn">⚠️ COMPLICACIÓN</div>' if r["complicacion"] == "si" else ""
    return f"""<div class="carta">
  <div class="cab"><div><div class="nombre">{E(r['nombre'])}</div>
    <div class="tipo">{NOM[r['tipo']]}</div>{et}</div></div>
  <div class="glifo">{SIM[r['tipo']]}</div>
  <div class="pie">{wa}<div class="frase">{E(r['frase'])}</div></div>
</div>"""


def carta_accion(a):
    return f"""<div class="carta">
  <div class="cab"><div><div class="nombre">{E(a['nombre'])}</div>
    <div class="tipo">Acción · {E(a['tipo'])}</div></div></div>
  <div class="banda" style="background:#3a6ea5"></div>
  <div class="cuerpo">{E(a['texto'])}</div>
  <div class="arte">ilustración</div>
  <div class="pie"><div class="frase">{E(a['frase'])}</div></div>
</div>"""


def carta_evento(e):
    return f"""<div class="carta">
  <div class="cab"><div><div class="nombre">{E(e['nombre'])}</div>
    <div class="tipo">Evento Adverso · {E(e['categoria'])}</div></div></div>
  <div class="banda" style="background:#c0492f"></div>
  <div class="cuerpo">{E(e['texto'])}</div>
  <div class="arte">ilustración</div>
  <div class="pie"><div class="frase">{E(e['frase'])}</div></div>
</div>"""


def carta_personaje(c):
    inm = (f'<div class="et">INMUNE · {E(c["inmunidad"])}</div>'
           if c["inmunidad"] else "")
    return f"""<div class="carta">
  <div class="cab"><div><div class="nombre">{E(c['nombre'])}</div>
    <div class="tipo">Personaje</div>{inm}</div></div>
  <div class="banda" style="background:#14202b"></div>
  <div class="hab"><b>Pasiva</b>{E(c['pasiva'])}</div>
  <div class="hab"><b>Turno Extra · 1×partida</b>{E(c['turno_extra'])}</div>
  <div class="pie"><div class="frase">{E(c['frase'])}</div></div>
</div>"""


MAZOS = {
    "pacientes":  ("Pacientes",       "pacientes.csv",  carta_paciente),
    "recursos":   ("Recursos",        "recursos.csv",   carta_recurso),
    "acciones":   ("Acciones",        "acciones.csv",   carta_accion),
    "eventos":    ("Eventos Adversos", "eventos.csv",   carta_evento),
    "personajes": ("Personajes",      "personajes.csv", carta_personaje),
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--solo", choices=list(MAZOS), action="append")
    ap.add_argument("--salida", default=os.path.join(RAIZ, "pnp.html"))
    args = ap.parse_args()

    elegidos = args.solo or list(MAZOS)
    partes, total = [], 0

    for clave in elegidos:
        titulo, archivo, render = MAZOS[clave]
        cartas = []
        for fila in leer(archivo):
            copias = int(fila.get("copias", 1) or 1)
            cartas.extend([render(fila)] * copias)
        total += len(cartas)

        partes.append(f'<div class="hoja"><div class="sep">{titulo} '
                      f'· {len(cartas)} cartas</div>')
        for i, c in enumerate(cartas):
            if i and i % 9 == 0:
                partes.append(f'</div><div class="hoja">'
                              f'<div class="sep">{titulo} · cont.</div>')
            partes.append(c)
        partes.append("</div>")

    doc = (f'<!doctype html><html lang="es"><head><meta charset="utf-8">'
           f'<title>¡Vaya Turno! · Print & Play</title><style>{CSS}</style>'
           f'</head><body>{"".join(partes)}</body></html>')

    with open(args.salida, "w", encoding="utf-8") as f:
        f.write(doc)
    print(f"✔ {total} cartas → {args.salida}")
    print("  Imprime en A4, márgenes mínimos, con gráficos de fondo activados.")


if __name__ == "__main__":
    main()
