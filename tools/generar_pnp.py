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
V030 = False   # rama experimental: mazos de cartas/v030/, coste en Acciones

SIM = {"IMAGEN": "🩻", "FARMACOS": "💊", "PERSONAL": "🧑‍⚕️",
       "PROCEDIMIENTOS": "💉", "COMODIN": "🃏"}
NOM = {"IMAGEN": "Imagen", "FARMACOS": "Fármacos", "PERSONAL": "Personal",
       "PROCEDIMIENTOS": "Procedimientos", "COMODIN": "Comodín"}
# Sistemas clínicos: la sinergia paciente ↔ recurso
SISTEMA = {
    "RESP":  ("Respiratorio", "🫁", "#3d7ea6"),
    "CARD":  ("Cardíaco",     "🫀", "#b03d29"),
    "NEURO": ("Neurológico",  "🧠", "#7a5ba6"),
    "METAB": ("Metabólico",   "🧪", "#2f8f6b"),
    "QUIR":  ("Quirúrgico",   "🔪", "#8a6a2f"),
}
RESTRIC = {
    "PERSONAL": "Solo sobre un paciente que ya tenga 🧑‍⚕️",
    "TURNO":    "Al jugarla, no puedes jugar más recursos este turno",
}
GRAV = {
    "I":    ("Gravedad I · Observación", "g1"),
    "II":   ("Gravedad II · Grave", "g2"),
    "III":  ("Gravedad III · Crítico", "g3"),
    "ROJO": ("★ CÓDIGO ROJO", "gr"),
}

FORMATOS = {
    "a4":    {"page": "A4",     "ancho": "210mm", "alto": "297mm",
              "pad": "6mm",        "sep": True,  "nombre": "A4 (210×297 mm)"},
    "carta": {"page": "Letter", "ancho": "216mm", "alto": "279mm",
              "pad": "7.5mm 13.5mm", "sep": False, "nombre": "Carta / Letter (216×279 mm)"},
}


def css_para(formato):
    """Ajusta el pliego. La carta mide 63×88 mm en los dos formatos."""
    f = FORMATOS[formato]
    css = (CSS.replace("__PAGESIZE__", f["page"])
              .replace("--ancho:210mm", "--ancho:" + f["ancho"])
              .replace("--alto:297mm", "--alto:" + f["alto"])
              .replace("--pad:6mm", "--pad:" + f["pad"]))
    if not f["sep"]:
        # en Carta no sobra alto: la banda de título saldría a una hoja nueva
        css += "\n.sep{display:none}"
    return css


CSS = """
:root{--tinta:#14202b;--suave:#5b6b7a;--linea:#c8d3dc;--papel:#fff;
      --ancho:210mm;--alto:297mm;--pad:6mm}
*{box-sizing:border-box}
body{margin:0;background:#e9eef2;font-family:"Helvetica Neue",Arial,sans-serif;color:var(--tinta)}
.hoja{width:var(--ancho);min-height:var(--alto);margin:0 auto 6mm;padding:var(--pad);background:var(--papel);
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
.comp{border-top:.3mm dashed #c0492f;margin-top:1mm;padding-top:1mm}
.et{display:inline-block;font-size:2.2mm;font-weight:700;letter-spacing:.07em;
    border:.25mm solid var(--tinta);border-radius:1mm;padding:.3mm 1mm;margin-top:1mm}
.hab{font-size:2.75mm;line-height:1.3;margin-bottom:1.5mm}
.hab b{display:block;font-size:2.35mm;text-transform:uppercase;letter-spacing:.08em;color:var(--suave)}
.sep{grid-column:1/-1;font-size:3.4mm;font-weight:800;text-transform:uppercase;
     letter-spacing:.12em;padding:0 0 1.5mm;border-bottom:.4mm solid var(--tinta);margin-bottom:1.5mm}
.sis{display:inline-block;font-size:2.2mm;font-weight:700;letter-spacing:.06em;
     color:#fff;border-radius:1mm;padding:.4mm 1.2mm;margin-top:1mm}
.restr{font-size:2.4mm;font-weight:700;line-height:1.25;color:#8a6a2f;margin-top:1mm}
.contra{font-size:2.4mm;font-weight:700;line-height:1.25;color:#c0492f;
        margin-top:.8mm}
.sinergia{font-size:2.4mm;line-height:1.25;margin-top:1mm}
.arte{flex:1;min-height:0;margin:1.5mm 0;border:.25mm dashed #dde4ea;border-radius:1mm;
      display:flex;align-items:center;justify-content:center;
      font-size:2.3mm;color:#c3ccd4;letter-spacing:.08em;text-transform:uppercase}
@media print{body{background:none}.hoja{margin:0;box-shadow:none;page-break-after:always}}
@page{size:__PAGESIZE__;margin:0}
"""

E = html.escape


def leer(nombre):
    with open(os.path.join(CARTAS, nombre), encoding="utf-8") as f:
        return list(csv.DictReader(f))


def carta_paciente(p):
    etiqueta, cls = GRAV[p["gravedad"]]
    nom_s, ico_s, col_s = SISTEMA[p["sistema"]]
    sis = (f'<div class="sis" style="background:{col_s}">{ico_s} '
           f'{nom_s.upper()}</div>')
    req = "".join(
        f'<div class="{"" if int(p[c]) else "off"}">{SIM[t]} ×{p[c]}</div>'
        for t, c in (("IMAGEN", "img"), ("FARMACOS", "far"),
                     ("PERSONAL", "per"), ("PROCEDIMIENTOS", "proc"))
    )
    # v0.60 · la contraindicación. Va pegada a «Requiere» porque es parte del
    # requisito: dice cuál de los recursos que pide NO le sirve.
    contra = (f'<div class="contra">⛔ Nada de {E(p["contra"])}</div>'
              if p.get("contra", "").strip() else "")
    return f"""<div class="carta {cls}">
  <div class="cab"><div><div class="nombre">{E(p['nombre'])}</div>
    <div class="tipo">{E(etiqueta)}</div>{sis}</div>
    <div class="vida">❤️{p['vida']}</div></div>
  <div class="banda"></div>
  <div class="tipo">Requiere</div><div class="req">{req}</div>{contra}
  <div class="arte">ilustración</div>
  <div class="pie"><div class="pts"><span>Alta +{p['puntos_alta']}</span>
    <span>Fallece {p['puntos_fallece']}</span></div>
    <div class="frase">{E(p['frase'])}</div></div>
</div>"""


def carta_recurso(r):
    sis, sinergia = "", ""
    if r["sistema"]:
        nom_s, ico_s, col_s = SISTEMA[r["sistema"]]
        sis = (f'<div class="sis" style="background:{col_s}">{ico_s} '
               f'{nom_s.upper()}</div>')
        sinergia = (f'<div class="sinergia"><b>Cuenta doble</b> sobre un '
                    f'paciente {nom_s}.</div>')
    if r["comodin"] == "si":
        # v0.60 · el comodín ya no vale 1 en todo: tiene casa propia. Puesto
        # como su tipo cuenta 2; como cualquier otro, 1. Así elegir el hueco
        # es una decisión y no un trámite.
        casa = r.get("doble_en", "").strip()
        sinergia = ('<div class="sinergia"><b>Comodín.</b> Cuenta como '
                    '1 recurso del tipo que elijas.</div>')
        if casa:
            sinergia = (f'<div class="sinergia"><b>Comodín.</b> Vale '
                        f'<b>2</b> como {SIM[casa]} {NOM[casa]}, o '
                        f'<b>1</b> del tipo que elijas.</div>')
    elif r.get("doble_en", "").strip():
        casa = r["doble_en"].strip()
        sinergia += (f'<div class="sinergia"><b>Cuenta doble</b> como '
                     f'{SIM[casa]} {NOM[casa]}.</div>')
    if r.get("soporte", "").strip() == "si":
        sinergia += ('<div class="sinergia"><b>Soporte vital.</b> Mientras'
                     ' siga puesta, este paciente <b>no pierde ❤️</b> en el'
                     ' Fin de Guardia. No lo cura.</div>')
    restr = (f'<div class="restr">⚑ {RESTRIC[r["restriccion"]]}</div>'
             if r["restriccion"] else "")
    efecto = (f'<div class="cuerpo">{E(r["texto"])}</div>'
              if r.get("texto", "").strip() else "")
    # v0.14: el ⚠️ trae su complicación impresa, con su 🎯 objetivo
    if r["complicacion"] == "si":
        # v0.30: no hay 🎯 — la complicación pega donde se ubica la carta
        diana = ('<div class="et" style="border-color:#c0492f;color:#c0492f">'
                 '🎯 DONDE SE UBICA</div>' if V030 else
                 (f'<div class="et" style="border-color:#c0492f;color:#c0492f">'
                  f'🎯 {E(OBJETIVO.get(r["comp_objetivo"], r["comp_objetivo"]))}</div>'
                  if r.get("comp_objetivo") else ""))
        wa = (f'<div class="comp"><div class="warn">⚠️ '
              f'{E(r.get("comp_nombre") or "COMPLICACIÓN")}</div>{diana}'
              f'<div class="cuerpo">{E(r.get("comp_texto",""))}</div></div>')
    else:
        wa = ""
    return f"""<div class="carta">
  <div class="cab"><div><div class="nombre">{E(r['nombre'])}</div>
    <div class="tipo">{NOM[r['tipo']]}</div>{sis}</div>
    <div class="vida">{SIM[r['tipo']]}</div></div>
  {sinergia}{efecto}{restr}{wa}
  <div class="arte">ilustración</div>
  <div class="pie"><div class="frase">{E(r['frase'])}</div></div>
</div>"""


def carta_accion(a):
    coste = ""
    if a.get("coste"):
        coste = (f'<div class="vida" style="font-size:4.5mm">💰{a["coste"]}</div>')
    return f"""<div class="carta">
  <div class="cab"><div><div class="nombre">{E(a['nombre'])}</div>
    <div class="tipo">Acción · {E(a['tipo'])}</div></div>{coste}</div>
  <div class="banda" style="background:#3a6ea5"></div>
  <div class="cuerpo">{E(a['texto'])}</div>
  <div class="arte">ilustración</div>
  <div class="pie"><div class="frase">{E(a['frase'])}</div></div>
</div>"""


OBJETIVO = {
    "ESTE": "ESTE PACIENTE",
    "MAS_GRAVE": "EL MÁS GRAVE · menos ❤️",
    "MEJOR": "EL QUE MEJOR VA · más ❤️",
    "MAS_TRATADO": "EL MÁS TRATADO · más recursos",
    "ESTABLE": "EL ✅ ESTABILIZADO",
    "ELIGES": "TÚ ELIGES",
    "MANO": "TU MANO",
    "TODOS": "TODOS TUS PACIENTES",
}


def carta_personaje(c):
    return f"""<div class="carta">
  <div class="cab"><div><div class="nombre">{E(c['nombre'])}</div>
    <div class="tipo">Personaje</div>
    <div class="et">{E(c['frecuencia'])}</div></div></div>
  <div class="banda" style="background:#14202b"></div>
  <div class="hab">{E(c['habilidad'])}</div>
  <div class="arte">ilustración</div>
  <div class="pie"><div class="frase">{E(c['frase'])}</div></div>
</div>"""


def carta_sumario(x):
    return f"""<div class="carta">
  <div class="cab"><div><div class="nombre">{E(x['nombre'])}</div>
    <div class="tipo">Maldición</div></div></div>
  <div class="banda" style="background:#7a5c12"></div>
  <div class="cuerpo">{E(x['texto'])}</div>
  <div class="arte">ilustración</div>
  <div class="pie"><div class="frase">{E(x['frase'])}</div></div>
</div>"""


def carta_logro(x):
    color = "#2f8f6b" if x["puntos"].startswith("+") else "#b03d29"
    return f"""<div class="carta">
  <div class="cab"><div><div class="nombre">{E(x['nombre'])}</div>
    <div class="tipo">Logro institucional</div></div>
    <div class="vida" style="color:{color}">{E(x['puntos'])}</div></div>
  <div class="banda" style="background:{color}"></div>
  <div class="cuerpo">{E(x['texto'])}</div>
  <div class="arte">ilustración</div>
  <div class="pie"><div class="frase">{E(x['frase'])}</div></div>
</div>"""


MAZOS = {
    "pacientes":  ("Pacientes",       "pacientes.csv",  carta_paciente),
    "recursos":   ("Recursos",        "recursos.csv",   carta_recurso),
    "acciones":   ("Acciones",        "acciones.csv",   carta_accion),
    "personajes": ("Personajes",      "personajes.csv", carta_personaje),
    "sumarios":   ("Sumarios",        "sumarios.csv",   carta_sumario),
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--solo", choices=list(MAZOS), action="append")
    ap.add_argument("--salida", default=os.path.join(RAIZ, "pnp.html"))
    ap.add_argument("--formato", choices=list(FORMATOS), default="a4",
                    help="pliego: a4 (por defecto) o carta / Letter")
    ap.add_argument("--variante", choices=["v030"],
                    help="rama experimental: recursos/acciones/logros de cartas/v030/")
    args = ap.parse_args()

    global V030
    if args.variante == "v030":
        V030 = True
        MAZOS["recursos"] = ("Recursos v0.30", os.path.join("v030", "recursos.csv"),
                             carta_recurso)
        MAZOS["acciones"] = ("Acciones v0.30", os.path.join("v030", "acciones.csv"),
                             carta_accion)
        MAZOS["logros"] = ("Logros", os.path.join("v030", "logros.csv"), carta_logro)

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
           f'<title>¡Vaya Turno! · Print & Play</title>'
           f'<style>{css_para(args.formato)}</style>'
           f'</head><body>{"".join(partes)}</body></html>')

    with open(args.salida, "w", encoding="utf-8") as f:
        f.write(doc)
    hojas = "".join(partes).count('class="hoja"')
    print(f"✔ {total} cartas · {hojas} hojas → {args.salida}")
    print(f"  Pliego: {FORMATOS[args.formato]['nombre']} · 9 cartas de 63×88 mm por hoja.")
    print("  Al imprimir: tamaño real / 100%, NO 'ajustar a la página', "
          "con gráficos de fondo.")


if __name__ == "__main__":
    main()
