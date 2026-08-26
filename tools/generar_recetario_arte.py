#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Construye el Recetario de Arte — la versión de bolsillo de
docs/PROMPTS-ARTE.md, pensada para usar desde el teléfono mientras se
generan las imágenes: cada carta con su prompt copiable de un toque,
buscador, filtros por tipo y un check de avance que se guarda en el
navegador.

Las escenas y el estilo salen de generar_prompts_arte.py — este archivo
solo los presenta. Si cambia el arte, se regeneran los dos.

    python3 tools/generar_recetario_arte.py   → docs/recetario-arte.html
"""
import json, html, os, re, sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, "tools"))
import generar_prompts_arte as G

HEX = re.compile(r"#[0-9a-f]{6}")

def hex_de(familia):
    m = HEX.search(familia)
    return m.group(0) if m else "#4a8a96"

def entradas():
    pacientes = G.leer("cartas", "pacientes.csv")
    recursos = G.leer("cartas", "v030", "recursos.csv")
    acciones = G.leer("cartas", "v030", "acciones.csv")
    personajes = G.leer("cartas", "personajes.csv")
    por_nombre = {}
    for r in recursos:
        por_nombre.setdefault(r["nombre"], []).append(r)

    out = []
    for c in personajes:
        cid = c["id"]
        escena, fam_noct = G.EC[cid]
        fam = fam_noct or G.FAM[""]
        out.append({
            "id": cid, "nombre": c["nombre"], "cat": "personajes",
            "color": hex_de(fam),
            "prompt": G.prompt(G.MARCO_C, fam, escena,
                               fisico=G.FISICO.get(cid, ""),
                               animo=G.ANIMO.get(cid, ""),
                               rompe=G.ROMPE.get(cid, "")),
            "ficha": f"{c['frecuencia']} — {c['habilidad']}",
            "frase": c["frase"],
            "extra": (("🐑 OVEJA NEGRA: rompe el estilo a propósito (otro "
                       "registro de dibujo) pero conserva encuadre, tamaño "
                       "de sujeto y familia de color. " if cid in G.ROMPE
                       else "")
                      + f"Retrato vivo: variante 1 «same exact image, eyes "
                      f"closed»; variante 2 «same exact image, {G.MICRO[cid]}» "
                      f"(tradúcela al inglés). Archivos: {cid}.png, "
                      f"{cid}-b.png, {cid}-c.png."),
        })
    for p in pacientes:
        fam = G.FAM.get(p["sistema"], G.FAM[""])
        out.append({
            "id": p["id"], "nombre": p["nombre"], "cat": "pacientes",
            "color": hex_de(fam),
            "prompt": G.prompt(G.MARCO_P, fam,
                               G.EP[p["id"]] + ". Clinical state: "
                               + G.GRAV[p["gravedad"]]),
            "ficha": (f"Gravedad {p['gravedad']} · "
                      f"{G.SIS_NOM.get(p['sistema'], '')} · ❤️{p['vida']} · "
                      f"pide {G.pide_txt(p)} · alta +{p['puntos_alta']} / "
                      f"fallece {p['puntos_fallece']}"),
            "frase": p["frase"], "extra": "",
        })
    for r in recursos:
        rid = r["id"]
        fam = G.FAM.get(r["sistema"], G.FAM[""])
        marco = G.MARCO_RP if (r["tipo"] == "PERSONAL" or rid == "R42") else G.MARCO_R
        partes = [G.TIPO_ICO.get(r["tipo"], r["tipo"])]
        if r["sistema"]: partes.append(f"{G.SIS_NOM[r['sistema']]} ×2")
        if r["comodin"] == "si": partes.append("vale por cualquier tipo")
        if r["previene"]: partes.append(f"🛡️ previene {r['previene']}")
        if r["complicacion"] == "si": partes.append(f"⚠️ {r['comp_nombre']}")
        gemela = [x["id"] for x in por_nombre[r["nombre"]] if x["id"] != rid]
        extra = ""
        if gemela:
            cual = "limpia" if r["complicacion"] == "no" else "complicada"
            extra = (f"Pareja con {gemela[0]} — esta es la versión {cual}: "
                     f"mismo objeto y encuadre, cambia lo que sale mal.")
        out.append({
            "id": rid, "nombre": r["nombre"], "cat": "recursos",
            "color": hex_de(fam),
            "prompt": G.prompt(marco, fam, G.ER[rid],
                               animo=G.ANIMO.get(rid, "")),
            "ficha": " · ".join(partes) + f" · {r['copias']} copia(s)",
            "frase": r["frase"], "extra": extra,
        })
    for a in acciones:
        fam = G.FAM_ACC.get(a["tipo"], G.FAM[""])
        out.append({
            "id": a["id"], "nombre": a["nombre"], "cat": "acciones",
            "color": hex_de(fam),
            "prompt": G.prompt(G.MARCO_A, fam, G.EA[a["id"]]),
            "ficha": f"{a['tipo']} · coste {a['coste']} · {a['texto']}",
            "frase": a["frase"], "extra": "",
        })
    out.append({
        "id": "S01", "nombre": "Sumario Administrativo", "cat": "sumario",
        "color": "#5f7a80",
        "prompt": G.prompt(
            "OBJECT CARD: a single document as the whole threat, filling "
            "the frame with its shadow.",
            "cold gray-teal bureaucratic palette (#5f7a80)",
            "a manila folder bristling with red stamps and seals, grown "
            "huge, casting a long shadow over a tiny clinician's desk "
            "below; one paper clip like a padlock"),
        "ficha": ("La sanción del juego: cada Sumario abierto muerde 1 "
                  "carta del límite de mano; cerrarlo cuesta 2 cartas."),
        "frase": "El proceso será justo, transparente y eterno.",
        "extra": "Una sola imagen para las 6 copias.",
    })
    return out

CATS = [("todas", "Todas"), ("personajes", "Personajes"),
        ("pacientes", "Pacientes"), ("recursos", "Recursos"),
        ("acciones", "Acciones"), ("sumario", "Sumario")]

def construir():
    datos = entradas()
    n = len(datos)
    tarjetas = []
    for d in datos:
        buscar = html.escape((d["id"] + " " + d["nombre"]).lower(), quote=True)
        frase = f'<p class="frase">«{html.escape(d["frase"])}»</p>' if d["frase"] else ""
        extra = f'<p class="extra">{html.escape(d["extra"])}</p>' if d["extra"] else ""
        tarjetas.append(f"""
<article class="c" data-cat="{d['cat']}" data-id="{d['id']}" data-buscar="{buscar}"
         style="--fam:{d['color']}">
  <div class="cab">
    <span class="cid">{d['id']}</span>
    <h3>{html.escape(d['nombre'])}</h3>
    <button class="listo" aria-label="Marcar {d['id']} como generada" title="Ya la generé">✓</button>
  </div>
  <p class="ficha">{html.escape(d['ficha'])}</p>
  {frase}{extra}
  <details><summary>Ver el prompt</summary><pre>{html.escape(d['prompt'])}</pre></details>
  <button class="copiar">Copiar prompt</button>
</article>""")

    chips = "".join(
        f'<button class="chip{" on" if k == "todas" else ""}" data-cat="{k}">{v}</button>'
        for k, v in CATS)
    prompts_js = json.dumps({d["id"]: d["prompt"] for d in datos},
                            ensure_ascii=False)

    pagina = f"""<title>Recetario de Arte</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo+Narrow:wght@500;600;700&family=IBM+Plex+Mono:wght@400;500&family=Petrona:ital,wght@0,600;0,700;1,500&display=swap">
<style>
/* Tema claro fijo a propósito: es el companion del tablero, que se juega
   bajo la luz del control de enfermería. Todo color es explícito. */
:root{{
  --mesa:#dfe7ea; --papel:#fffdf8; --tinta:#16242e; --tinta2:#4c6675;
  --tinta3:#87a0ad; --linea:#c7d6db; --acc:#0d6e78; --acc-suave:#d5e9eb;
  --ok:#237a5b;
}}
*{{box-sizing:border-box}}
html{{background:var(--mesa)}}
body{{margin:0;color:var(--tinta);
  font-family:"Archivo Narrow","Segoe UI",system-ui,sans-serif;
  background:radial-gradient(130% 100% at 50% 0%, #e6edf0 0%, var(--mesa) 55%, #ccd9d3 100%) fixed;
  min-height:100vh}}
main{{max-width:640px;margin:0 auto;padding:0 12px 60px}}

/* ── la barra de trabajo ── */
.barra{{position:sticky;top:0;z-index:10;margin:0 -12px;padding:10px 12px 8px;
  background:rgba(223,231,234,.88);backdrop-filter:blur(8px);
  border-bottom:1px solid var(--linea)}}
.barra .fila1{{display:flex;align-items:baseline;gap:10px}}
.barra h1{{font-family:Petrona,Georgia,serif;font-size:19px;margin:0;
  letter-spacing:-.2px}}
.avance{{margin-left:auto;font-family:"IBM Plex Mono",monospace;font-size:11px;
  color:var(--tinta2);font-variant-numeric:tabular-nums}}
.avance b{{color:var(--ok)}}
.busca{{width:100%;margin-top:8px;padding:9px 12px;border:1px solid var(--linea);
  border-radius:9px;font:500 14px "Archivo Narrow",sans-serif;
  background:var(--papel);color:var(--tinta)}}
.busca:focus{{outline:2px solid var(--acc);outline-offset:1px}}
.chips{{display:flex;gap:6px;margin-top:8px;overflow-x:auto;
  scrollbar-width:none;padding-bottom:2px}}
.chips::-webkit-scrollbar{{display:none}}
.chip{{flex:none;padding:6px 12px;border-radius:99px;border:1px solid var(--linea);
  background:var(--papel);color:var(--tinta2);font:600 12px "Archivo Narrow",sans-serif;
  letter-spacing:.02em;cursor:pointer}}
.chip.on{{background:var(--acc);border-color:var(--acc);color:#fff}}
.chip:focus-visible,.listo:focus-visible,.copiar:focus-visible{{
  outline:2px solid var(--acc);outline-offset:2px}}

/* ── las fichas ── */
.c{{position:relative;background:var(--papel);border:1px solid var(--linea);
  border-radius:12px;padding:12px 13px 12px 18px;margin-top:12px;
  box-shadow:0 1px 2px rgba(22,36,46,.07), 0 3px 10px rgba(22,36,46,.05)}}
.c::before{{content:"";position:absolute;left:0;top:0;bottom:0;width:5px;
  border-radius:12px 0 0 12px;background:var(--fam)}}
.c.hecha{{opacity:.55}}
.c.hecha .cid::after{{content:" ✓";color:var(--ok)}}
.c.oculta{{display:none}}
.cab{{display:flex;align-items:center;gap:9px}}
.cid{{font-family:"IBM Plex Mono",monospace;font-size:11px;font-weight:600;
  color:#fff;background:var(--fam);padding:2px 7px;border-radius:6px;
  letter-spacing:.05em;flex:none}}
.cab h3{{font-family:Petrona,Georgia,serif;font-size:16.5px;margin:0;
  line-height:1.15;text-wrap:balance;flex:1}}
.listo{{flex:none;width:34px;height:34px;border-radius:99px;
  border:1.5px solid var(--linea);background:var(--papel);color:var(--tinta3);
  font-size:15px;line-height:1;cursor:pointer}}
.c.hecha .listo{{background:var(--ok);border-color:var(--ok);color:#fff}}
.ficha{{font-size:12.5px;color:var(--tinta2);line-height:1.45;margin:7px 0 0}}
.frase{{font-family:Petrona,Georgia,serif;font-style:italic;font-size:12.5px;
  color:var(--tinta3);margin:6px 0 0;line-height:1.4}}
.extra{{font-size:11.5px;color:var(--tinta2);margin:6px 0 0;line-height:1.45;
  padding:6px 9px;background:var(--acc-suave);border-radius:8px}}
details{{margin-top:8px}}
summary{{font:600 11.5px "Archivo Narrow",sans-serif;letter-spacing:.04em;
  text-transform:uppercase;color:var(--acc);cursor:pointer;
  list-style-position:inside}}
pre{{margin:7px 0 0;padding:9px 11px;background:#f2f7f8;
  border:1px solid var(--linea);border-radius:8px;white-space:pre-wrap;
  font:11px/1.5 "IBM Plex Mono",monospace;color:var(--tinta2);
  overflow-x:auto}}
.copiar{{margin-top:9px;width:100%;padding:10px;border-radius:9px;border:none;
  background:linear-gradient(180deg,#118491,var(--acc) 55%,#0a5860);
  color:#fff;font:700 13.5px "Archivo Narrow",sans-serif;letter-spacing:.03em;
  cursor:pointer}}
.copiar.ok{{background:var(--ok)}}
.nada{{text-align:center;color:var(--tinta3);font-size:13px;padding:34px 0}}
.pie{{text-align:center;font-size:11px;color:var(--tinta3);margin-top:28px;
  line-height:1.6}}
@media (prefers-reduced-motion: no-preference){{
  .c{{transition:opacity .2s ease}}
  .copiar{{transition:background .2s ease}}
}}
</style>

<main>
<div class="barra">
  <div class="fila1"><h1>Recetario de Arte</h1>
    <span class="avance"><b id="hechas">0</b> / {n} listas</span></div>
  <input class="busca" id="busca" type="search"
         placeholder="Buscar por id o nombre (C09, abastecimiento…)">
  <div class="chips">{chips}</div>
</div>
<div id="lista">{"".join(tarjetas)}
  <p class="nada" id="nada" hidden>Ninguna carta calza con ese filtro.</p>
</div>
<p class="pie">¡Vaya Turno! · un prompt por carta, listo para Nano Banana.<br>
Pide 2:3 vertical, mínimo 1024×1536, y guarda cada imagen con su id.<br>
El ✓ marca tu avance y queda guardado en este teléfono.</p>
</main>

<script>
"use strict";
const PROMPTS = {prompts_js};
const LLAVE = "vt-recetario-listas";

function cargarListas(){{
  try{{ return new Set(JSON.parse(localStorage.getItem(LLAVE) || "[]")); }}
  catch(e){{ return new Set(); }}
}}
function guardarListas(s){{
  try{{ localStorage.setItem(LLAVE, JSON.stringify([...s])); }}catch(e){{}}
}}
const listas = cargarListas();

function pintaAvance(){{
  document.getElementById("hechas").textContent = listas.size;
}}
document.querySelectorAll(".c").forEach(c => {{
  const id = c.dataset.id;
  if(listas.has(id)) c.classList.add("hecha");
  c.querySelector(".listo").addEventListener("click", () => {{
    if(listas.has(id)) listas.delete(id); else listas.add(id);
    c.classList.toggle("hecha", listas.has(id));
    guardarListas(listas); pintaAvance();
  }});
  c.querySelector(".copiar").addEventListener("click", ev => {{
    const b = ev.currentTarget, txt = PROMPTS[id];
    const listo = () => {{
      b.textContent = "Copiado ✓"; b.classList.add("ok");
      setTimeout(() => {{ b.textContent = "Copiar prompt";
                          b.classList.remove("ok"); }}, 1600);
    }};
    if(navigator.clipboard && navigator.clipboard.writeText){{
      navigator.clipboard.writeText(txt).then(listo, () => aMano(txt, listo));
    }} else aMano(txt, listo);
  }});
}});
function aMano(txt, listo){{
  const ta = document.createElement("textarea");
  ta.value = txt; ta.style.position = "fixed"; ta.style.opacity = "0";
  document.body.appendChild(ta); ta.select();
  try{{ document.execCommand("copy"); listo(); }}catch(e){{}}
  ta.remove();
}}
pintaAvance();

let cat = "todas";
const chips = document.querySelectorAll(".chip");
chips.forEach(ch => ch.addEventListener("click", () => {{
  cat = ch.dataset.cat;
  chips.forEach(x => x.classList.toggle("on", x === ch));
  filtra();
}}));
const busca = document.getElementById("busca");
busca.addEventListener("input", filtra);
function filtra(){{
  const q = busca.value.trim().toLowerCase();
  let visibles = 0;
  document.querySelectorAll(".c").forEach(c => {{
    const va = (cat === "todas" || c.dataset.cat === cat) &&
               (!q || c.dataset.buscar.includes(q));
    c.classList.toggle("oculta", !va);
    if(va) visibles++;
  }});
  document.getElementById("nada").hidden = visibles > 0;
}}
</script>
"""
    ruta = os.path.join(RAIZ, "docs", "recetario-arte.html")
    open(ruta, "w", encoding="utf-8").write(pagina)
    print(f"✔ {ruta} ({len(pagina)//1024} KB · {n} cartas)")

if __name__ == "__main__":
    construir()
