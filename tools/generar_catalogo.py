#!/usr/bin/env python3
"""Catálogo editable de todas las cartas — docs/catalogo-cartas.html

Una hoja de revisión, no un print-and-play: cada carta en una fila, con su
número, su tipo, lo que cuesta, lo que hace, y **una casilla en blanco para
comentar**. Se puede imprimir en Carta y rayarla a mano, o escribir en ella
en el navegador (los comentarios quedan guardados en el propio navegador).

    python3 tools/generar_catalogo.py
"""

import csv
import html
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SALIDA = os.path.join(RAIZ, "docs", "catalogo-cartas.html")

SIM = {"IMAGEN": "🩻", "FARMACOS": "💊", "PERSONAL": "🧑‍⚕️", "PROCEDIMIENTOS": "💉",
       "COMODIN": "🃏"}
SISTEMA = {"RESP": "🫁 RESP", "CARD": "🫀 CARD", "NEURO": "🧠 NEURO",
           "METAB": "🧪 METAB", "QUIR": "🔪 QUIR", "": "—"}
RESTRICCION = {
    "PERSONAL": "⚑ solo sobre un paciente que ya tenga al menos 1 🧑‍⚕️",
    "TURNO": "⚑ al jugarla termina tu Pase de Visita",
}
OBJETIVO = {"ESTE": "ESTE PACIENTE", "MEJOR": "EL QUE MEJOR VA",
            "ESTABLE": "EL ✅ ESTABILIZADO", "ELIGES": "TÚ ELIGES",
            "MANO": "TU MANO", "MAS_GRAVE": "EL MÁS GRAVE",
            "MAS_TRATADO": "EL MÁS TRATADO", "": "—"}


def leer(n):
    with open(os.path.join(RAIZ, "cartas", n), encoding="utf-8") as f:
        return list(csv.DictReader(f))


def e(s):
    return html.escape(str(s or ""))


def celda_comentario():
    return '<td class="com" contenteditable="true" spellcheck="false"></td>'


def tabla(titulo, nota, cabeceras, filas, anchos):
    cols = "".join(f'<col style="width:{w}">' for w in anchos)
    th = "".join(f"<th>{c}</th>" for c in cabeceras)
    cuerpo = "\n".join(filas)
    return f"""
<h2>{titulo} <small>{nota}</small></h2>
<table><colgroup>{cols}</colgroup>
<thead><tr>{th}</tr></thead>
<tbody>
{cuerpo}
</tbody></table>
"""


def bloque_pacientes():
    pac = leer("pacientes.csv")
    filas = []
    for i, p in enumerate(pac, 1):
        pide = " ".join(
            f"{SIM[t]}{p[c]}" for t, c in
            (("IMAGEN", "img"), ("FARMACOS", "far"),
             ("PERSONAL", "per"), ("PROCEDIMIENTOS", "proc"))
            if int(p[c]) > 0)
        filas.append(
            f'<tr><td class="n">{i}</td><td class="id">{e(p["id"])}</td>'
            f'<td class="nom">{e(p["nombre"])}<span class="frase">{e(p["frase"])}</span></td>'
            f'<td class="c">{e(p["gravedad"])}</td>'
            f'<td class="c sis">{SISTEMA.get(p["sistema"], e(p["sistema"]))}</td>'
            f'<td class="c num">{e(p["vida"])} ❤️</td>'
            f'<td class="coste">{pide}<b> = {e(p["total_recursos"])}</b></td>'
            f'<td class="c num">+{e(p["puntos_alta"])}</td>'
            f'<td class="c num">{e(p["puntos_fallece"])}</td>'
            + celda_comentario() + "</tr>")
    nota = (f"{len(pac)} cartas · el <b>coste</b> es lo que pide para estabilizarse · "
            "regla de tasación: <b>alta + |fallece| = recursos que pide</b>")
    return tabla("Pacientes", nota,
                 ["#", "id", "Carta", "Grav.", "Sistema", "Vida",
                  "COSTE (lo que pide)", "Alta", "Muere", "Comentario"],
                 filas,
                 ["3.5%", "5%", "26%", "5%", "8%", "6%", "17%", "5%", "5%", "19.5%"])


def bloque_recursos():
    rec = leer("recursos.csv")
    filas = []
    for i, r in enumerate(rec, 1):
        marcas = []
        if r["comodin"] == "si":
            marcas.append("🃏 comodín — cuenta como 1 del tipo que elijas, nunca doble")
        if r["restriccion"]:
            marcas.append(RESTRICCION.get(r["restriccion"], "⚑ " + r["restriccion"]))
        if r["previene"] and not r["texto"]:
            marcas.append("🛡️ previene " + r["previene"])
        efecto = ""
        if r["texto"]:
            efecto = e(r["texto"])
        elif r["complicacion"] == "si":
            efecto = (f'<b class="warn">⚠️ {e(r["comp_nombre"])}</b> '
                      f'<span class="obj">🎯 {OBJETIVO.get(r["comp_objetivo"], "")}</span><br>'
                      f'{e(r["comp_texto"])}')
        if marcas:
            efecto = ('<span class="marca">' + " · ".join(e(m) for m in marcas)
                      + "</span>" + ("<br>" + efecto if efecto else ""))
        if not efecto:
            efecto = '<span class="vacio">sin texto — solo aporta su tipo</span>'
        filas.append(
            f'<tr><td class="n">{i}</td><td class="id">{e(r["id"])}</td>'
            f'<td class="nom">{e(r["nombre"])}<span class="frase">{e(r["frase"])}</span></td>'
            f'<td class="c">{SIM.get(r["tipo"], "")} {e(r["tipo"][:4].title())}</td>'
            f'<td class="c sis">{SISTEMA.get(r["sistema"], e(r["sistema"]))}</td>'
            f'<td class="c num">{e(r["copias"])}</td>'
            f'<td class="ef">{efecto}</td>'
            + celda_comentario() + "</tr>")
    copias = sum(int(r["copias"]) for r in rec)
    warn = sum(1 for r in rec if r["complicacion"] == "si")
    nota = (f"{len(rec)} diseños · {copias} cartas · {warn} llevan ⚠️ · "
            "el <b>coste</b> de todos es el mismo: <b>1 indicación</b> "
            "(el chip de sistema la hace valer 2 sobre su paciente)")
    return tabla("Recursos — el Mazo de Guardia", nota,
                 ["#", "id", "Carta", "Tipo", "Sistema", "Cop.",
                  "Efecto / ⚠️ complicación", "Comentario"],
                 filas,
                 ["3.5%", "5%", "22%", "8%", "8%", "4%", "30%", "19.5%"])


def bloque_acciones():
    acc = leer("acciones.csv")
    filas = []
    for i, a in enumerate(acc, 1):
        filas.append(
            f'<tr><td class="n">{i}</td><td class="id">{e(a["id"])}</td>'
            f'<td class="nom">{e(a["nombre"])}<span class="frase">{e(a["frase"])}</span></td>'
            f'<td class="c">{e(a["tipo"])}</td>'
            f'<td class="c num">{e(a["copias"])}</td>'
            f'<td class="ef">{e(a["texto"])}</td>'
            + celda_comentario() + "</tr>")
    copias = sum(int(a["copias"]) for a in acc)
    nota = (f"{len(acc)} diseños · {copias} cartas · "
            "el <b>coste</b> de todas es el mismo: <b>un Canje</b> "
            "(2 recursos + el Negocio del turno ≈ 2 indicaciones ≈ 1 punto)")
    return tabla("Protocolos — las Acciones", nota,
                 ["#", "id", "Carta", "Tipo", "Cop.", "Efecto", "Comentario"],
                 filas,
                 ["3.5%", "5%", "22%", "10%", "4%", "36%", "19.5%"])


def bloque_personajes():
    per = leer("personajes.csv")
    filas = []
    for i, c in enumerate(per, 1):
        filas.append(
            f'<tr><td class="n">{i}</td><td class="id">{e(c["id"])}</td>'
            f'<td class="nom">{e(c["nombre"])}<span class="frase">{e(c["frase"])}</span></td>'
            f'<td class="c">{e(c["frecuencia"])}</td>'
            f'<td class="ef">{e(c["habilidad"])}</td>'
            + celda_comentario() + "</tr>")
    nota = (f"{len(per)} avatares · se reparten <b>2 a cada jugador y cada uno "
            "elige 1</b> · banda sana medida: <b>+0,3 a +1,0 puntos</b> de "
            "ventaja sobre la mesa")
    return tabla("Personajes — los avatares", nota,
                 ["#", "id", "Carta", "Frecuencia", "Habilidad", "Comentario"],
                 filas,
                 ["3.5%", "5%", "20%", "10%", "42%", "19.5%"])


def bloque_sumarios():
    sm = leer("sumarios.csv")
    filas = []
    for i, s in enumerate(sm, 1):
        filas.append(
            f'<tr><td class="n">{i}</td><td class="id">{e(s["id"])}</td>'
            f'<td class="nom">{e(s["nombre"])}<span class="frase">{e(s["frase"])}</span></td>'
            f'<td class="c num">{e(s["copias"])}</td>'
            f'<td class="ef">{e(s["texto"])}</td>'
            + celda_comentario() + "</tr>")
    nota = ("no se juegan: te llegan · medido: dura <b>1,00 rondas</b> y se "
            "cierra el <b>100%</b> de las veces — su efecto real es "
            "«se te murió alguien: descarta 2 cartas»")
    return tabla("Sumario Administrativo", nota,
                 ["#", "id", "Carta", "Cop.", "Efecto", "Comentario"],
                 filas,
                 ["3.5%", "5%", "20%", "4%", "48%", "19.5%"])


CSS = """
@page{size:Letter portrait;margin:11mm 9mm}
*{box-sizing:border-box}
body{margin:0;font-family:"Helvetica Neue",Arial,sans-serif;color:#14202b;
     background:#fff;font-size:8.2pt;line-height:1.3}
header{border-bottom:1.4pt solid #14202b;padding-bottom:2.5mm;margin-bottom:4mm}
h1{font-size:15pt;margin:0;letter-spacing:.01em}
h1 span{font-weight:400;color:#5b6b7a;font-size:9pt}
.intro{color:#5b6b7a;font-size:7.6pt;margin-top:1.5mm;line-height:1.45}
.intro b{color:#14202b}
h2{font-size:11pt;margin:7mm 0 1.5mm;padding-bottom:1mm;
   border-bottom:.8pt solid #14202b;page-break-after:avoid}
h2 small{font-weight:400;color:#5b6b7a;font-size:7.2pt;margin-left:2mm}
table{width:100%;border-collapse:collapse;page-break-inside:auto}
th{background:#14202b;color:#fff;font-size:6.6pt;letter-spacing:.07em;
   text-transform:uppercase;text-align:left;padding:1.2mm 1.4mm;font-weight:700}
td{border-bottom:.4pt solid #d5dee5;padding:1.4mm;vertical-align:top}
tr{page-break-inside:avoid}
tbody tr:nth-child(even){background:#f6f9fb}
.n{color:#8fa0ae;text-align:right;font-variant-numeric:tabular-nums}
.id{color:#8fa0ae;font-size:7pt;font-variant-numeric:tabular-nums}
.nom{font-weight:700}
.frase{display:block;font-weight:400;font-style:italic;color:#7d8b98;
       font-size:6.8pt;line-height:1.25;margin-top:.4mm}
.c{text-align:center}
.num{font-variant-numeric:tabular-nums;white-space:nowrap}
.sis{font-size:6.8pt;color:#5b6b7a;white-space:nowrap}
.coste{font-size:8.6pt;letter-spacing:.04em}
.coste b{font-size:7.4pt;color:#5b6b7a;letter-spacing:0}
.ef{font-size:7.4pt;line-height:1.3}
.warn{color:#a8410f}
.obj{font-size:6.6pt;letter-spacing:.06em;color:#5b6b7a;white-space:nowrap}
.marca{font-size:6.8pt;color:#5b6b7a;letter-spacing:.03em}
.vacio{color:#b9c6d1;font-style:italic}
.com{background:#fffdf5;border-left:.8pt solid #c8d3dc;min-height:9mm}
.com:focus{outline:1.2pt solid #14202b;background:#fff}
.libre{margin-top:8mm;page-break-before:always}
.libre h2{margin-top:0}
.lineas{border:1pt solid #14202b;border-radius:1.5mm;overflow:hidden}
.lineas div{height:7.5mm;border-bottom:.4pt solid #dbe4eb}
.lineas div:last-child{border-bottom:none}
.pie{margin-top:5mm;font-size:7pt;color:#5b6b7a;line-height:1.4;
     border-top:.4pt solid #c8d3dc;padding-top:2mm}
.barra{position:fixed;right:6mm;bottom:6mm;background:#14202b;color:#fff;
       font-size:8pt;padding:2mm 3.5mm;border-radius:2mm;box-shadow:0 2px 8px #0004}
.barra button{font:inherit;color:#14202b;background:#fff;border:0;border-radius:1.2mm;
              padding:.8mm 2mm;margin-left:2mm;cursor:pointer}
@media print{.barra{display:none}.com{background:#fff}}
"""

JS = """
const CLAVE = "vaya-turno-catalogo";
const cajas = [...document.querySelectorAll(".com")];
cajas.forEach((c, i) => c.dataset.i = i);
try {
  const guardado = JSON.parse(localStorage.getItem(CLAVE) || "{}");
  cajas.forEach((c, i) => { if (guardado[i]) c.textContent = guardado[i]; });
} catch (err) { /* navegador sin almacenamiento: se usa en papel */ }
function guardar() {
  const datos = {};
  cajas.forEach((c, i) => { const v = c.textContent.trim(); if (v) datos[i] = v; });
  try { localStorage.setItem(CLAVE, JSON.stringify(datos)); } catch (err) {}
  const n = Object.keys(datos).length;
  document.getElementById("cuenta").textContent =
    n ? n + (n === 1 ? " comentario" : " comentarios") : "sin comentarios";
}
cajas.forEach(c => c.addEventListener("input", guardar));
document.getElementById("borrar").addEventListener("click", () => {
  if (!confirm("¿Borrar todos los comentarios escritos aquí?")) return;
  cajas.forEach(c => c.textContent = "");
  guardar();
});
guardar();
"""


def main():
    partes = [bloque_pacientes(), bloque_recursos(), bloque_acciones(),
              bloque_personajes(), bloque_sumarios()]
    doc = f"""<!doctype html>
<html lang="es"><meta charset="utf-8">
<title>¡Vaya Turno! · Catálogo editable de cartas</title>
<style>{CSS}</style>
<header>
  <h1>¡VAYA TURNO! <span>· catálogo de cartas · v0.21</span></h1>
  <p class="intro">
    Todas las cartas que existen hoy, por tipo, con lo que cuestan y lo que hacen.
    <b>La última columna está en blanco a propósito:</b> escribe ahí qué cambiarías.
    Puedes imprimirla y rayarla a mano, o escribir directo en el navegador —
    lo que escribas se guarda solo en este computador (no toca los CSV).
    <b>La fuente de verdad sigue siendo <code>cartas/*.csv</code> y el Taller;</b>
    esta hoja es para decidir, no para editar el juego.
  </p>
</header>
{''.join(partes)}
<div class="libre">
  <h2>Notas generales <small>lo que no cabe en una fila</small></h2>
  <div class="lineas">{"<div></div>" * 29}</div>
  <p class="pie">
    <b>Cómo usarla:</b> pasa carta por carta y anota solo donde algo te chirríe.
    Preguntas útiles para cada fila — ¿el nombre dice lo que hace? ¿el chiste
    funciona o estorba? ¿la jugarías alguna vez? ¿le sobra o le falta texto?
    Para pacientes: ¿el precio se siente justo (recuerda: alta + |fallece| =
    recursos que pide)? Para Acciones: ¿vale un Canje?
    &nbsp;·&nbsp; Cuando termines, los cambios se aplican en el Taller
    (<code>taller.html</code>) o directo en los CSV, y se vuelven a medir con
    <code>tools/simular.py</code> antes de reimprimir.
  </p>
</div>
<div class="barra"><span id="cuenta">sin comentarios</span>
  <button id="borrar">borrar</button></div>
<script>{JS}</script>
</html>
"""
    with open(SALIDA, "w", encoding="utf-8") as f:
        f.write(doc)
    n = sum(len(leer(x)) for x in
            ("pacientes.csv", "recursos.csv", "acciones.csv",
             "personajes.csv", "sumarios.csv"))
    print(f"✔ Catálogo con {n} diseños → {SALIDA}")


if __name__ == "__main__":
    main()
