#!/usr/bin/env python3
"""
Genera el TALLER DE GUARDIA: una sola página con las 131 cartas dentro,
el tablero de constantes del mazo y un editor en vivo.

    python3 tools/generar_taller.py        # → taller.html

Los CSV de cartas/ son la fuente de la verdad; esto los empaqueta en HTML.
Cuando cambien los CSV, vuelve a correrlo.
"""

import base64
import csv
import glob
import io
import json
import os
import re

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CARTAS = os.path.join(RAIZ, "cartas")
ARTE_DIR = os.path.join(RAIZ, "arte", "raw")


def cargar_arte():
    """Ilustraciones de arte/raw/<ID>-*.jpg como data-URIs en miniatura.

    Si Pillow está instalado, reduce a 340px de ancho (≈20 KB por carta);
    si no, embebe el archivo tal cual. El Taller funciona igual sin arte.
    """
    arte = {}
    try:
        from PIL import Image
        pil = True
    except ImportError:
        pil = False
    for ruta in sorted(glob.glob(os.path.join(ARTE_DIR, "*.jpg"))):
        m = re.match(r"([A-Z]\d{2})-", os.path.basename(ruta))
        if not m:
            continue
        if pil:
            im = Image.open(ruta).convert("RGB")
            im.thumbnail((340, 510))
            buf = io.BytesIO()
            im.save(buf, "JPEG", quality=68)
            crudo = buf.getvalue()
        else:
            with open(ruta, "rb") as f:
                crudo = f.read()
        arte[m.group(1)] = "data:image/jpeg;base64," + base64.b64encode(crudo).decode()
    return arte

# Esquema de edición: por mazo, qué columnas y con qué control se editan.
# num = campo numérico · sel = desplegable · txt = línea · area = párrafo
SIS = ["", "RESP", "CARD", "NEURO", "METAB", "QUIR"]
ESQUEMA = {
    "pacientes": {
        "titulo": "Pacientes", "archivo": "pacientes.csv", "icono": "🛏️",
        "campos": [
            ("nombre", "txt", None), ("edad", "num", None),
            ("gravedad", "sel", ["I", "II", "III", "ROJO"]),
            ("sistema", "sel", SIS[1:]), ("vida", "num", None),
            ("img", "num", None), ("far", "num", None),
            ("per", "num", None), ("proc", "num", None),
            ("puntos_alta", "num", None), ("puntos_fallece", "num", None),
            ("frase", "area", None), ("entrega", "area", None),
            ("copias", "num", None),
        ],
    },
    "recursos": {
        "titulo": "Recursos", "archivo": "recursos.csv", "icono": "💊",
        "campos": [
            ("nombre", "txt", None),
            ("tipo", "sel", ["IMAGEN", "FARMACOS", "PERSONAL", "PROCEDIMIENTOS", "COMODIN"]),
            ("sistema", "sel", SIS), ("comodin", "sel", ["no", "si"]),
            ("restriccion", "sel", ["", "PERSONAL", "TURNO"]),
            ("complicacion", "sel", ["no", "si"]),
            ("comp_objetivo", "sel", ["", "ESTE", "MAS_GRAVE", "MEJOR", "MAS_TRATADO",
                                      "ESTABLE", "ELIGES", "MANO"]),
            ("comp_vida", "num", None),
            ("comp_pide", "sel", ["", "IMAGEN", "FARMACOS", "PERSONAL", "PROCEDIMIENTOS"]),
            ("comp_descarta", "sel", ["", "IMAGEN", "FARMACOS", "PERSONAL", "PROCEDIMIENTOS"]),
            ("copias", "num", None),
            ("previene", "txt", None), ("comp_nombre", "txt", None), ("comp_texto", "area", None),
            ("texto", "area", None), ("frase", "area", None),
        ],
    },
    "acciones": {
        "titulo": "Acciones", "archivo": "acciones.csv", "icono": "📋",
        "campos": [
            ("nombre", "txt", None),
            ("tipo", "sel", ["ATAQUE", "APOYO", "CAOS", "RESPUESTA", "EXTREMA"]),
            ("copias", "num", None), ("texto", "area", None), ("frase", "area", None),
        ],
    },
    "personajes": {
        "titulo": "Avatares", "archivo": "personajes.csv", "icono": "🩺",
        "campos": [
            ("nombre", "txt", None),
            ("frecuencia", "sel", ["PASIVA", "1×TURNO", "1×RONDA", "1×PARTIDA"]),
            ("habilidad", "area", None), ("frase", "area", None),
        ],
    },
    "sumarios": {
        "titulo": "Sumarios", "archivo": "sumarios.csv", "icono": "📎",
        "campos": [("nombre", "txt", None), ("copias", "num", None),
                   ("texto", "area", None), ("frase", "area", None)],
    },
}


def cargar():
    datos = {}
    for clave, meta in ESQUEMA.items():
        with open(os.path.join(CARTAS, meta["archivo"]), encoding="utf-8") as f:
            datos[clave] = list(csv.DictReader(f))
    return datos


CSS = """
:root{
  --papel:#eef2f4; --ficha:#ffffff; --panel:#e3eaee; --tinta:#0f1c24;
  --tenue:#5a6f7c; --linea:#cbd6dd; --linea-fuerte:#a5b6c0;
  --acento:#00757f; --acento-suave:#dcedee;
  --ok:#2f8f6b; --alerta:#b8801a; --mal:#b03d29;
  --ok-fondo:#e2f1eb; --alerta-fondo:#f7eeda; --mal-fondo:#f7e3df;
  --sRESP:#3d7ea6; --sCARD:#b03d29; --sNEURO:#7a5ba6; --sMETAB:#2f8f6b; --sQUIR:#8a6a2f;
  --chip-tinta:#ffffff; --editado:#b8801a;
}
@media (prefers-color-scheme:dark){ :root:not([data-theme="light"]){
  --papel:#080e12; --ficha:#111c23; --panel:#0d161c; --tinta:#dde7ec;
  --tenue:#8ba3af; --linea:#243440; --linea-fuerte:#3a5261;
  --acento:#3fbcc4; --acento-suave:#0f2a2d;
  --ok:#5cb583; --alerta:#dda43c; --mal:#e0705a;
  --ok-fondo:#122620; --alerta-fondo:#2a2313; --mal-fondo:#2b1815;
  --sRESP:#5b9dc4; --sCARD:#e0705a; --sNEURO:#a184c9; --sMETAB:#5cb583; --sQUIR:#c19a4e;
  --chip-tinta:#08121a; --editado:#dda43c;
}}
:root[data-theme="dark"]{
  --papel:#080e12; --ficha:#111c23; --panel:#0d161c; --tinta:#dde7ec;
  --tenue:#8ba3af; --linea:#243440; --linea-fuerte:#3a5261;
  --acento:#3fbcc4; --acento-suave:#0f2a2d;
  --ok:#5cb583; --alerta:#dda43c; --mal:#e0705a;
  --ok-fondo:#122620; --alerta-fondo:#2a2313; --mal-fondo:#2b1815;
  --sRESP:#5b9dc4; --sCARD:#e0705a; --sNEURO:#a184c9; --sMETAB:#5cb583; --sQUIR:#c19a4e;
  --chip-tinta:#08121a; --editado:#dda43c;
}

*{box-sizing:border-box}
body{margin:0;background:var(--papel);color:var(--tinta);
  font:400 15px/1.5 "Helvetica Neue",Helvetica,Arial,system-ui,sans-serif;
  -webkit-font-smoothing:antialiased}
.mono,.dato,td.n,.metrica b,.barra-txt{
  font-family:ui-monospace,"SF Mono",SFMono-Regular,Menlo,Consolas,monospace;
  font-variant-numeric:tabular-nums}
button,input,select,textarea{font:inherit;color:inherit}
:focus-visible{outline:2px solid var(--acento);outline-offset:2px}

.env{max-width:88rem;margin:0 auto;padding:0 1.25rem 5rem}

/* ── Cabecera ───────────────────────────────────────────────── */
header{padding:2rem 0 1rem;display:flex;justify-content:space-between;
  align-items:flex-end;gap:1rem;flex-wrap:wrap}
h1{margin:0;font-size:1.7rem;font-weight:800;letter-spacing:-.03em}
h1 em{font-style:normal;color:var(--acento)}
.sub{margin:.25rem 0 0;font-size:.9rem;color:var(--tenue)}
.acciones-cab{display:flex;gap:.5rem;flex-wrap:wrap}
.btn{background:var(--ficha);border:1px solid var(--linea-fuerte);color:var(--tinta);
  padding:.45rem .85rem;font-size:.85rem;font-weight:600;cursor:pointer;
  border-radius:2px;white-space:nowrap}
.btn:hover{border-color:var(--acento);color:var(--acento)}
.btn.primario{background:var(--acento);border-color:var(--acento);color:var(--papel)}
.btn.primario:hover{opacity:.88;color:var(--papel)}

/* ── Monitor de constantes ──────────────────────────────────── */
.monitor{background:var(--panel);border:1px solid var(--linea);
  padding:1rem 1.1rem;display:flex;flex-direction:column;gap:1rem}
.mon-cab{display:flex;justify-content:space-between;align-items:baseline;gap:1rem;flex-wrap:wrap}
.eyebrow{font-size:.63rem;font-weight:800;letter-spacing:.16em;
  text-transform:uppercase;color:var(--tenue)}
.veredicto{font-size:.8rem;font-weight:700;padding:.2rem .55rem;border-radius:2px}
.v-ok{background:var(--ok-fondo);color:var(--ok)}
.v-alerta{background:var(--alerta-fondo);color:var(--alerta)}
.v-mal{background:var(--mal-fondo);color:var(--mal)}

.rejilla{display:grid;grid-template-columns:repeat(auto-fit,minmax(15rem,1fr));gap:1px;
  background:var(--linea);border:1px solid var(--linea)}
.bloque{background:var(--ficha);padding:.85rem .95rem;display:flex;
  flex-direction:column;gap:.6rem}
.bloque h3{margin:0;font-size:.66rem;font-weight:800;letter-spacing:.13em;
  text-transform:uppercase;color:var(--tenue)}

.metrica{display:flex;justify-content:space-between;align-items:baseline;
  gap:.5rem;font-size:.85rem}
.metrica b{font-weight:700}
.metrica .obj{font-size:.72rem;color:var(--tenue)}

/* ── Banco de pruebas ───────────────────────────────────────── */
.banco{background:var(--panel);border:1px solid var(--linea);
  padding:1rem 1.1rem;display:flex;flex-direction:column;gap:.9rem;margin-top:1rem}
.banco-intro{margin:0;font-size:.82rem;color:var(--tenue);max-width:52rem}
.mandos{display:flex;gap:.75rem;flex-wrap:wrap;align-items:flex-end}
.mando{display:flex;flex-direction:column;gap:.2rem}
.mando label{font-size:.6rem;font-weight:800;letter-spacing:.11em;
  text-transform:uppercase;color:var(--tenue)}
.mando select{background:var(--ficha);border:1px solid var(--linea-fuerte);
  padding:.35rem .5rem;font-size:.85rem;border-radius:2px;color:var(--tinta)}
.mandos .btn{margin-left:auto}
.estado-sim{font-size:.78rem;color:var(--tenue);min-height:1.2em}
.tabla-sim{width:100%;border-collapse:collapse;font-size:.85rem}
.tabla-sim th{text-align:left;font-size:.6rem;font-weight:800;letter-spacing:.11em;
  text-transform:uppercase;color:var(--tenue);padding:.3rem .5rem;
  border-bottom:1px solid var(--linea-fuerte);white-space:nowrap}
.tabla-sim th.n,.tabla-sim td.n{text-align:right}
.tabla-sim td{padding:.38rem .5rem;border-bottom:1px solid var(--linea)}
.tabla-sim tr:last-child td{border-bottom:0}
.tabla-sim .obj{font-size:.72rem;color:var(--tenue)}
.delta{font-size:.75rem;font-weight:700;white-space:nowrap}
.d-sube{color:var(--ok)} .d-baja{color:var(--mal)} .d-igual{color:var(--tenue)}
.sim-envuelve{overflow-x:auto}
.sim-pie{font-size:.72rem;color:var(--tenue);margin:0}

/* barras comparativas demanda vs mazo */
.par{display:flex;flex-direction:column;gap:.22rem}
.par-cab{display:flex;justify-content:space-between;font-size:.8rem;align-items:baseline}
.barras{display:flex;flex-direction:column;gap:2px}
.pista{height:7px;background:var(--panel);position:relative;overflow:hidden}
.relleno{height:100%;transition:width .25s ease}
.r-dem{background:var(--linea-fuerte)}
.r-ok{background:var(--ok)} .r-alerta{background:var(--alerta)} .r-mal{background:var(--mal)}
.barra-txt{font-size:.7rem;color:var(--tenue)}

.puntos{display:inline-block;width:8px;height:8px;border-radius:50%;flex:none}
.p-ok{background:var(--ok)} .p-alerta{background:var(--alerta)} .p-mal{background:var(--mal)}

/* ── Filtros ────────────────────────────────────────────────── */
.filtros{display:flex;gap:.5rem;flex-wrap:wrap;align-items:center;
  padding:1rem 0 .75rem;position:sticky;top:0;background:var(--papel);z-index:20;
  border-bottom:1px solid var(--linea)}
.pestanas{display:flex;gap:1px;background:var(--linea);border:1px solid var(--linea)}
.pest{background:var(--ficha);border:0;padding:.4rem .7rem;font-size:.8rem;
  font-weight:600;cursor:pointer;color:var(--tenue);white-space:nowrap}
.pest[aria-selected="true"]{background:var(--acento);color:var(--papel)}
input[type="search"],select.filtro{background:var(--ficha);border:1px solid var(--linea-fuerte);
  padding:.4rem .6rem;font-size:.85rem;border-radius:2px;min-width:0}
input[type="search"]{flex:1;min-width:9rem;max-width:20rem}
.cuenta{font-size:.78rem;color:var(--tenue);margin-left:auto;white-space:nowrap}

/* ── Galería ────────────────────────────────────────────────── */
.galeria{display:grid;grid-template-columns:repeat(auto-fill,minmax(11.5rem,1fr));
  gap:.7rem;padding-top:1rem}
.carta{aspect-ratio:63/88;background:var(--ficha);border:1px solid var(--linea);
  padding:.55rem .6rem;display:flex;flex-direction:column;gap:.25rem;
  cursor:pointer;text-align:left;overflow:hidden;position:relative}
.carta:hover{border-color:var(--acento)}
.carta.tocada{border-color:var(--editado);border-width:2px;padding:calc(.55rem - 1px) calc(.6rem - 1px)}
.carta.tocada::after{content:"editada";position:absolute;top:0;right:0;
  background:var(--editado);color:var(--chip-tinta);font-size:.55rem;font-weight:800;
  letter-spacing:.06em;padding:.1rem .3rem;text-transform:uppercase}
.c-nom{font-size:.78rem;font-weight:700;line-height:1.15;text-wrap:balance}
.c-meta{font-size:.58rem;font-weight:700;letter-spacing:.09em;text-transform:uppercase;
  color:var(--tenue)}
.c-cuerpo{font-size:.63rem;line-height:1.32;overflow:hidden}
.c-frase{font-size:.58rem;font-style:italic;color:var(--tenue);line-height:1.25;
  margin-top:auto;padding-top:.3rem;border-top:1px solid var(--linea);
  display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden}
.c-arte{flex:1;min-height:1.6rem;margin:.15rem 0;border:1px dashed var(--linea);
  border-radius:2px;display:flex;align-items:center;justify-content:center;
  font-size:.5rem;letter-spacing:.1em;text-transform:uppercase;color:var(--linea-fuerte)}
.c-arte.con{border:1px solid var(--linea);padding:0;overflow:hidden}
.c-arte.con img{width:100%;height:100%;object-fit:cover;display:block}
.cajon-arte{width:100%;aspect-ratio:3/2;object-fit:cover;border:1px solid var(--linea);
  border-radius:2px;display:block}
.c-req{display:grid;grid-template-columns:1fr 1fr;gap:.1rem .3rem;font-size:.72rem;
  font-weight:700;font-family:ui-monospace,Menlo,monospace}
.c-req .off{color:var(--linea-fuerte);font-weight:400}
.c-pts{display:flex;justify-content:space-between;font-size:.65rem;font-weight:700}
.c-vida{font-size:.95rem;font-weight:800;white-space:nowrap}
.c-cab{display:flex;justify-content:space-between;align-items:flex-start;gap:.3rem}
.c-glifo{font-size:1.6rem;text-align:center;margin:auto 0;line-height:1}
.c-warn{font-size:.56rem;font-weight:800;color:var(--mal);letter-spacing:.04em}
.c-obj{font-size:.56rem;font-weight:800;letter-spacing:.05em;color:var(--acento);
  border:1px solid var(--acento);padding:.06rem .25rem;align-self:flex-start;border-radius:2px}
.c-efecto{border-left:2px solid var(--acento);padding-left:.3rem}
.c-comp{border-top:1px dashed var(--mal);margin-top:.2rem;padding-top:.2rem;
  display:flex;flex-direction:column;gap:.15rem}
.c-comp .c-obj{color:var(--mal);border-color:var(--mal)}
.chip{display:inline-block;padding:.08rem .3rem;font-size:.55rem;font-weight:800;
  letter-spacing:.05em;color:var(--chip-tinta);align-self:flex-start;
  font-family:ui-monospace,Menlo,monospace}
.RESP{background:var(--sRESP)}.CARD{background:var(--sCARD)}.NEURO{background:var(--sNEURO)}
.METAB{background:var(--sMETAB)}.QUIR{background:var(--sQUIR)}
.INFEC{background:var(--acento)}.GENERAL{background:var(--tenue)}
.tag{display:inline-block;min-width:1.7rem;text-align:center;padding:.08rem .3rem;
  font-size:.58rem;font-weight:800;color:var(--chip-tinta);
  font-family:ui-monospace,Menlo,monospace}
.gI{background:var(--ok)}.gII{background:var(--alerta)}
.gIII{background:var(--mal)}.gROJO{background:var(--tinta)}
:root[data-theme="dark"] .gROJO,:root:not([data-theme="light"]) .gROJO{background:var(--linea-fuerte)}
@media (prefers-color-scheme:light){:root:not([data-theme="dark"]) .gROJO{background:var(--tinta)}}

/* ── Cajón de edición ───────────────────────────────────────── */
.velo{position:fixed;inset:0;background:rgba(8,14,18,.45);z-index:40;border:0;padding:0;
  width:100%;cursor:default}
.cajon{position:fixed;top:0;right:0;bottom:0;width:min(26rem,100%);background:var(--ficha);
  border-left:1px solid var(--linea-fuerte);z-index:50;display:flex;flex-direction:column;
  box-shadow:-8px 0 28px rgba(8,14,18,.16)}
.cajon-cab{padding:1rem 1.1rem;border-bottom:1px solid var(--linea);
  display:flex;justify-content:space-between;align-items:flex-start;gap:.75rem}
.cajon-cuerpo{padding:1.1rem;overflow-y:auto;display:flex;flex-direction:column;gap:.85rem;flex:1}
.cajon-pie{padding:.85rem 1.1rem;border-top:1px solid var(--linea);display:flex;gap:.5rem}
.campo{display:flex;flex-direction:column;gap:.25rem}
.campo label{font-size:.63rem;font-weight:800;letter-spacing:.11em;
  text-transform:uppercase;color:var(--tenue)}
.campo input,.campo select,.campo textarea{width:100%;background:var(--papel);
  border:1px solid var(--linea-fuerte);padding:.4rem .55rem;font-size:.85rem;border-radius:2px}
.campo textarea{min-height:4.5rem;resize:vertical;line-height:1.4}
.campo.cambiado input,.campo.cambiado select,.campo.cambiado textarea{
  border-color:var(--editado);background:var(--alerta-fondo)}
.fila-campos{display:grid;grid-template-columns:1fr 1fr;gap:.6rem}
.campo.gemelas{background:var(--alerta-fondo);border:1px solid var(--alerta);
  padding:.5rem .6rem;border-radius:2px}

/* ── Salida ─────────────────────────────────────────────────── */
.salida{margin-top:2.5rem;display:flex;flex-direction:column;gap:.75rem}
.salida h2{margin:0;font-size:1rem;font-weight:800;letter-spacing:.1em;
  text-transform:uppercase;padding-bottom:.4rem;border-bottom:2px solid var(--tinta)}
.salida p{margin:0;font-size:.88rem;color:var(--tenue);max-width:44rem}
textarea.volcado{width:100%;min-height:14rem;background:var(--ficha);
  border:1px solid var(--linea-fuerte);padding:.7rem;border-radius:2px;
  font-family:ui-monospace,Menlo,monospace;font-size:.72rem;line-height:1.45;
  white-space:pre;overflow:auto}
.oculto{display:none !important}
@media (max-width:40rem){
  .galeria{grid-template-columns:repeat(auto-fill,minmax(9rem,1fr))}
  .filtros{position:static}
}
@media (prefers-reduced-motion:reduce){*{transition:none !important}}
"""

JS = r"""
const DATOS = window.__DATOS__, ESQUEMA = window.__ESQUEMA__,
      ARTE = window.__ARTE__ || {};
const ORIG = JSON.parse(JSON.stringify(DATOS));
const TIPOS = ["FARMACOS","IMAGEN","PROCEDIMIENTOS","PERSONAL"];
const NOMT = {IMAGEN:"Imagen",FARMACOS:"Fármacos",PERSONAL:"Personal",
              PROCEDIMIENTOS:"Procedimientos",COMODIN:"Comodín"};
const GLIFO = {IMAGEN:"🩻",FARMACOS:"💊",PERSONAL:"🧑‍⚕️",PROCEDIMIENTOS:"💉",COMODIN:"🃏"};
const SISTEMAS = ["RESP","CARD","NEURO","METAB","QUIR"];
const OBJETIVO = {ESTE:"ESTE PACIENTE", MAS_GRAVE:"EL MÁS GRAVE", MEJOR:"EL QUE MEJOR VA",
                  MAS_TRATADO:"EL MÁS TRATADO", ESTABLE:"EL ✅ ESTABILIZADO",
                  ELIGES:"TÚ ELIGES", MANO:"TU MANO", TODOS:"TODOS TUS PACIENTES"};
const NOMS = {RESP:"Respiratorio",CARD:"Cardíaco",NEURO:"Neurológico",
              METAB:"Metabólico",QUIR:"Quirúrgico"};
const LLAVE = "vayaturno-taller-v1";
let mazo = "pacientes", busca = "", filtroSis = "";

const n = v => parseInt(v,10) || 0;
const copias = f => Math.max(0, n(f.copias ?? 1));
const suma = (arr, fn) => arr.reduce((a,x)=>a+fn(x),0);
const esc = s => String(s ?? "").replace(/[&<>"]/g, c =>
  ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));

/* ── Cálculo del balance ─────────────────────────────────────── */
function balance(){
  const P = DATOS.pacientes, R = DATOS.recursos;
  const dem = {}, ofe = {};
  TIPOS.forEach(t => { dem[t]=0; ofe[t]=0; });
  const COL = {IMAGEN:"img",FARMACOS:"far",PERSONAL:"per",PROCEDIMIENTOS:"proc"};
  P.forEach(p => TIPOS.forEach(t => dem[t] += n(p[COL[t]]) * copias(p)));
  R.forEach(r => { if (TIPOS.includes(r.tipo)) ofe[r.tipo] += copias(r); });
  const D = suma(TIPOS,t=>dem[t]) || 1, O = suma(TIPOS,t=>ofe[t]) || 1;

  const guardia = suma(R, copias);
  const warn = suma(R.filter(r=>r.complicacion==="si"), copias);
  const comod = suma(R.filter(r=>r.comodin==="si"), copias);

  const sis = {};
  SISTEMAS.forEach(s => sis[s] = {
    rec: suma(R.filter(r=>r.sistema===s), copias),
    pac: suma(P.filter(p=>p.sistema===s), copias),
  });

  const total = Object.keys(ESQUEMA).reduce((a,k)=>a+suma(DATOS[k],copias),0);
  return {dem,ofe,D,O,guardia,warn,comod,sis,total,
          espec: suma(R.filter(r=>r.sistema), copias)};
}

// nivel: 0 ok · 1 alerta · 2 mal
const nivel = (v,okMax,alertaMax) =>
  v<=okMax ? 0 : v<=alertaMax ? 1 : 2;
const CLASE = ["ok","alerta","mal"];

function renderMonitor(){
  const b = balance();
  let peor = 0;
  const marca = lv => { peor = Math.max(peor,lv); return CLASE[lv]; };

  // Demanda vs mazo, por tipo
  const pares = TIPOS.map(t => {
    const pd = 100*b.dem[t]/b.D, pm = 100*b.ofe[t]/b.O;
    const lv = nivel(Math.abs(pd-pm), 3, 6);
    return `<div class="par">
      <div class="par-cab"><span>${GLIFO[t]} ${NOMT[t]}</span>
        <span class="puntos p-${marca(lv)}"></span></div>
      <div class="barras">
        <div class="pista"><div class="relleno r-dem" style="width:${pd.toFixed(1)}%"></div></div>
        <div class="pista"><div class="relleno r-${CLASE[lv]}" style="width:${pm.toFixed(1)}%"></div></div>
      </div>
      <div class="barra-txt">piden ${pd.toFixed(0)}% · mazo ${pm.toFixed(0)}%</div>
    </div>`;
  }).join("");

  // Sinergia por sistema. El objetivo NO es emparejar con los pacientes: la
  // caja base cubre los cinco sistemas de forma pareja pero fina, para que
  // ninguno quede agotado antes de su propio módulo (ver EXPANSIONES.md §4).
  const filas = SISTEMAS.map(s => {
    const {rec,pac} = b.sis[s];
    const lv = (rec>=3 && rec<=6) ? 0 : ((rec===2 || rec===7) ? 1 : 2);
    return `<div class="metrica">
      <span><span class="chip ${s}">${NOMS[s]}</span></span>
      <span><b>${rec}</b><span class="obj"> rec / ${pac} pac</span>
        <span class="puntos p-${marca(lv)}"></span></span></div>`;
  }).join("");

  const pWarn = 100*b.warn/(b.guardia||1);
  const lvWarn = nivel(Math.abs(pWarn-27), 5, 12);
  const lvCom = b.comod>=2 && b.comod<=4 ? 0 : (b.comod>=1 && b.comod<=5 ? 1 : 2);
  const lvGuardia = nivel(Math.abs(b.guardia-63), 6, 14);
  marca(lvWarn); marca(lvCom); marca(lvGuardia);

  const vered = ["Mazo en rango","Revisar lo ámbar","Fuera de rango"][peor];

  document.getElementById("monitor").innerHTML = `
    <div class="mon-cab">
      <div><span class="eyebrow">Constantes del mazo</span></div>
      <span class="veredicto v-${CLASE[peor]}">${vered}</span>
    </div>
    <div class="rejilla">
      <div class="bloque">
        <h3>Lo que piden vs lo que hay</h3>${pares}
      </div>
      <div class="bloque">
        <h3>Sinergia por sistema</h3>${filas}
        <div class="barra-txt">Objetivo: <b>3–6 recursos específicos por sistema</b>. Pareja pero fina: la expansión de cada sistema necesita margen para traer los suyos.</div>
      </div>
      <div class="bloque">
        <h3>Densidades</h3>
        <div class="metrica"><span>⚠️ Complicación</span>
          <span><b>${b.warn}</b><span class="obj"> / ${b.guardia} · ${pWarn.toFixed(0)}%</span>
          <span class="puntos p-${CLASE[lvWarn]}"></span></span></div>
        <div class="metrica"><span>🃏 Comodines</span>
          <span><b>${b.comod}</b><span class="obj"> (objetivo 2–4)</span>
          <span class="puntos p-${CLASE[lvCom]}"></span></span></div>
        <div class="metrica"><span>Recursos específicos</span>
          <span><b>${b.espec}</b><span class="obj"> / ${b.guardia}</span></span></div>
        <div class="metrica"><span>Mazo de Guardia</span>
          <span><b>${b.guardia}</b><span class="obj"> (calibrado a 63)</span>
          <span class="puntos p-${CLASE[lvGuardia]}"></span></span></div>
      </div>
      <div class="bloque">
        <h3>Recuento</h3>
        ${Object.keys(ESQUEMA).map(k=>`<div class="metrica">
          <span>${ESQUEMA[k].icono} ${ESQUEMA[k].titulo}</span>
          <span><b>${suma(DATOS[k],copias)}</b><span class="obj"> / ${DATOS[k].length} dis.</span></span>
        </div>`).join("")}
        <div class="metrica" style="border-top:1px solid var(--linea);padding-top:.4rem">
          <span><b>Total</b></span><span><b>${b.total}</b></span></div>
        <div class="metrica"><span>🖼️ Con ilustración</span>
          <span><b>${Object.keys(ESQUEMA).reduce((a,k)=>a+DATOS[k].filter(f=>ARTE[f.id]).length,0)}</b><span class="obj"> / ${Object.keys(ESQUEMA).reduce((a,k)=>a+DATOS[k].length,0)} dis.</span></span></div>
      </div>
    </div>`;
}

/* ── Galería ─────────────────────────────────────────────────── */
function tocada(k,i){ return JSON.stringify(DATOS[k][i]) !== JSON.stringify(ORIG[k][i]); }

function pintarCarta(k,f,i){
  const arte = ARTE[f.id]
    ? `<div class="c-arte con"><img src="${ARTE[f.id]}" alt="" loading="lazy"></div>`
    : `<div class="c-arte">arte</div>`;
  const t = s => arte + `<div class="c-frase">${esc(s)}</div>`;
  let dentro = "";
  if (k === "pacientes"){
    const req = [["IMAGEN","img"],["FARMACOS","far"],["PERSONAL","per"],["PROCEDIMIENTOS","proc"]]
      .map(([tp,c])=>`<div class="${n(f[c])?"":"off"}">${GLIFO[tp]} ×${n(f[c])}</div>`).join("");
    dentro = `<div class="c-cab"><div>
        <div class="c-nom">${esc(f.nombre)}</div>
        <div class="c-meta">Gravedad ${esc(f.gravedad)}</div></div>
        <div class="c-vida">❤️${esc(f.vida)}</div></div>
      <span class="chip ${esc(f.sistema)}">${NOMS[f.sistema]||esc(f.sistema)}</span>
      <div class="c-req">${req}</div>
      <div class="c-pts"><span>Alta +${esc(f.puntos_alta)}</span>
        <span>Muere ${esc(f.puntos_fallece)}</span></div>${t(f.frase)}`;
  } else if (k === "recursos"){
    const chip = f.sistema ? `<span class="chip ${esc(f.sistema)}">${NOMS[f.sistema]}</span>` : "";
    const nota = f.comodin==="si" ? `<div class="c-cuerpo"><b>Comodín:</b> cuenta como el tipo que elijas.</div>`
      : f.sistema ? `<div class="c-cuerpo"><b>Cuenta doble</b> en ${NOMS[f.sistema].toLowerCase()}.</div>` : "";
    const rest = f.restriccion ? `<div class="c-warn">⚑ ${f.restriccion==="TURNO"?"CONSUME EL TURNO":"EXIGE 🧑‍⚕️"}</div>` : "";
    const txt = (f.texto||"").trim()
      ? `<div class="c-cuerpo c-efecto">${esc(f.texto)}</div>` : "";
    // ⚠️: la complicación va impresa en la propia carta, con su 🎯 objetivo
    const comp = f.complicacion==="si" ? `<div class="c-comp">
        <div class="c-warn">⚠️ ${esc(f.comp_nombre||"COMPLICACIÓN")}</div>
        ${f.comp_objetivo?`<div class="c-obj">🎯 ${esc(OBJETIVO[f.comp_objetivo]||f.comp_objetivo)}</div>`:""}
        ${f.comp_texto?`<div class="c-cuerpo">${esc(f.comp_texto)}</div>`:""}
      </div>` : "";
    dentro = `<div class="c-cab"><div>
        <div class="c-nom">${esc(f.nombre)}</div>
        <div class="c-meta">${NOMT[f.tipo]||esc(f.tipo)}</div></div>
        <div class="c-vida">${GLIFO[f.tipo]||""}</div></div>
      ${chip}${nota}${txt}${rest}${comp}${t(f.frase)}`;
  } else if (k === "personajes"){
    dentro = `<div class="c-nom">${esc(f.nombre)}</div>
      <div class="c-meta">${esc(f.frecuencia)}</div>
      <div class="c-cuerpo">${esc(f.habilidad)}</div>${t(f.frase)}`;
  } else {
    const cat = f.categoria ? `<span class="chip ${esc(f.categoria)}">${esc(f.categoria)}</span>` : "";
    const obj = f.objetivo
      ? `<div class="c-obj">🎯 ${esc(OBJETIVO[f.objetivo] || f.objetivo)}</div>` : "";
    const meta = f.tipo || "Maldición";
    dentro = `<div class="c-nom">${esc(f.nombre)}</div>
      <div class="c-meta">${esc(meta)}</div>${cat}${obj}
      <div class="c-cuerpo">${esc(f.texto)}</div>${t(f.frase)}`;
  }
  return `<button class="carta ${tocada(k,i)?"tocada":""}" data-i="${i}"
    aria-label="Editar ${esc(f.nombre)}">${dentro}</button>`;
}

function renderGaleria(){
  const q = busca.trim().toLowerCase();
  const lista = DATOS[mazo].map((f,i)=>({f,i})).filter(({f}) => {
    if (filtroSis && f.sistema !== filtroSis && f.categoria !== filtroSis) return false;
    if (!q) return true;
    return Object.values(f).some(v => String(v).toLowerCase().includes(q));
  });
  document.getElementById("galeria").innerHTML =
    lista.length ? lista.map(({f,i})=>pintarCarta(mazo,f,i)).join("")
    : `<p style="color:var(--tenue);grid-column:1/-1">Sin resultados para «${esc(busca)}».</p>`;
  document.getElementById("cuenta").textContent =
    `${lista.length} de ${DATOS[mazo].length} diseños · ${suma(DATOS[mazo],copias)} cartas`;
}

/* ── Cajón de edición ────────────────────────────────────────── */
let abierta = null;
function abrir(i){
  abierta = i;
  const f = DATOS[mazo][i], o = ORIG[mazo][i], campos = ESQUEMA[mazo].campos;
  const ctrl = ([col,tipo,ops]) => {
    const val = f[col] ?? "", dif = val !== (o[col] ?? "");
    const id = `c-${col}`;
    let input;
    if (tipo === "sel")
      input = `<select id="${id}" data-col="${col}">${ops.map(op =>
        `<option value="${esc(op)}" ${op===val?"selected":""}>${op===""?"— ninguno —":esc(op)}</option>`).join("")}</select>`;
    else if (tipo === "area")
      input = `<textarea id="${id}" data-col="${col}">${esc(val)}</textarea>`;
    else
      input = `<input id="${id}" data-col="${col}" type="${tipo==="num"?"number":"text"}"
        ${tipo==="num"?'min="0"':""} value="${esc(val)}">`;
    return `<div class="campo ${dif?"cambiado":""}">
      <label for="${id}">${col.replace(/_/g," ")}</label>${input}</div>`;
  };
  const cortos = campos.filter(c => c[1]==="num" || c[1]==="sel");
  const largos = campos.filter(c => c[1]!=="num" && c[1]!=="sel");
  // Cartas gemelas: mismo nombre en varias filas (la limpia y la del ⚠️).
  // Son la misma carta impresa distinto, así que el texto debe ir en todas.
  const gemelas = DATOS[mazo]
    .map((g,k) => ({g,k}))
    .filter(({g,k}) => k !== i && g.nombre === f.nombre);
  const avisoGemelas = gemelas.length ? `
    <div class="campo gemelas">
      <label style="display:flex;gap:.4rem;align-items:flex-start;text-transform:none;
                    letter-spacing:0;font-weight:400;font-size:.78rem;cursor:pointer">
        <input type="checkbox" id="sync-gemelas" checked
               style="width:auto;margin-top:.15rem;flex:none">
        <span>Esta carta tiene <b>${gemelas.length} gemela${gemelas.length>1?"s":""}</b>
        (${gemelas.map(({g})=>esc(g.id)).join(", ")}): la misma carta con ⚠️ o sin él.
        Copiar <b>texto</b> y <b>frase</b> a ${gemelas.length>1?"ellas":"ella"} al guardar.</span>
      </label>
    </div>` : "";
  document.getElementById("cajon").innerHTML = `
    <div class="cajon-cab">
      <div><div class="eyebrow">${ESQUEMA[mazo].icono} ${ESQUEMA[mazo].titulo} · ${esc(f.id)}</div>
        <strong style="font-size:1.02rem">${esc(f.nombre)}</strong></div>
      <button class="btn" id="cerrar" aria-label="Cerrar">✕</button>
    </div>
    <div class="cajon-cuerpo">
      ${ARTE[f.id] ? `<img class="cajon-arte" src="${ARTE[f.id]}" alt="Ilustración de ${esc(f.nombre)}">` : ""}
      ${largos.filter(c=>c[0]==="nombre").map(ctrl).join("")}
      <div class="fila-campos">${cortos.map(ctrl).join("")}</div>
      ${largos.filter(c=>c[0]!=="nombre").map(ctrl).join("")}
      ${avisoGemelas}
    </div>
    <div class="cajon-pie">
      <button class="btn primario" id="aplicar" style="flex:1">Guardar cambios</button>
      <button class="btn" id="revertir">Revertir</button>
    </div>`;
  document.getElementById("cajon").classList.remove("oculto");
  document.getElementById("velo").classList.remove("oculto");
  document.getElementById("cerrar").onclick = cerrar;
  document.getElementById("revertir").onclick = () => {
    DATOS[mazo][i] = JSON.parse(JSON.stringify(ORIG[mazo][i]));
    guardar(); cerrar(); refrescar();
  };
  document.getElementById("aplicar").onclick = () => {
    document.querySelectorAll("#cajon [data-col]").forEach(el => {
      DATOS[mazo][i][el.dataset.col] = el.value;
    });
    if (mazo === "pacientes"){
      const p = DATOS[mazo][i];
      p.total_recursos = String(n(p.img)+n(p.far)+n(p.per)+n(p.proc));
    }
    const sync = document.getElementById("sync-gemelas");
    if (sync && sync.checked)
      gemelas.forEach(({k}) => {
        ["texto","frase"].forEach(col => {
          if (col in DATOS[mazo][k]) DATOS[mazo][k][col] = DATOS[mazo][i][col];
        });
      });
    guardar(); cerrar(); refrescar();
  };
}
function cerrar(){
  abierta = null;
  document.getElementById("cajon").classList.add("oculto");
  document.getElementById("velo").classList.add("oculto");
}

/* ── Salida ──────────────────────────────────────────────────── */
function aCSV(k){
  const cols = Object.keys(ORIG[k][0]);
  const cel = v => { v = String(v ?? "");
    return /[",\n]/.test(v) ? '"'+v.replace(/"/g,'""')+'"' : v; };
  return [cols.join(","), ...DATOS[k].map(f => cols.map(c => cel(f[c])).join(","))].join("\n");
}
function diff(){
  const out = [];
  for (const k of Object.keys(ESQUEMA))
    DATOS[k].forEach((f,i) => {
      const o = ORIG[k][i];
      const cambios = Object.keys(o).filter(c => (f[c]??"") !== (o[c]??""));
      if (cambios.length) out.push(`${k}/${f.id} · ${o.nombre}\n` +
        cambios.map(c => `    ${c}: «${o[c]}» → «${f[c]}»`).join("\n"));
    });
  return out.length ? out.join("\n\n") : "Sin cambios todavía.";
}
function renderSalida(){
  const modo = document.getElementById("modo-salida").value;
  document.getElementById("volcado").value = modo === "diff" ? diff() : aCSV(modo);
}

/* ── Banco de pruebas ─────────────────────────────────────────────
   Port en JavaScript de tools/simular.py. Corre sobre las cartas que
   tienes en pantalla, no sobre los CSV: simula tu idea antes de
   guardarla. El Python sigue siendo la verdad — este mide lo mismo
   con menos partidas, para que puedas iterar sin salir de la página.
   Si tocas el motor, hay que tocarlo en los dos lados.            */
const SIM_TIPOS = ["IMAGEN","FARMACOS","PERSONAL","PROCEDIMIENTOS"];
const SIM_COL = {IMAGEN:"img",FARMACOS:"far",PERSONAL:"per",PROCEDIMIENTOS:"proc"};
const GRAVEDADES = ["I","II","III","ROJO"];

function rng32(semilla){                       // mulberry32
  let a = semilla >>> 0;
  return () => {
    a = (a + 0x6D2B79F5) >>> 0;
    let t = a;
    t = Math.imul(t ^ (t >>> 15), t | 1);
    t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}
const azar = (r,k) => Math.floor(r()*k);
const elige = (r,a) => a[azar(r,a.length)];
function barajar(a,r){
  for (let i=a.length-1;i>0;i--){ const j=azar(r,i+1); const x=a[i]; a[i]=a[j]; a[j]=x; }
  return a;
}

function simCargar(fuente){
  const pacientes = [];
  fuente.pacientes.forEach(p => {
    const pide = {};
    SIM_TIPOS.forEach(t => pide[t] = n(p[SIM_COL[t]]));
    const ficha = {gravedad:p.gravedad, vida:n(p.vida), sistema:p.sistema, pide,
                   alta:n(p.puntos_alta), fallece:n(p.puntos_fallece),
                   pideTotal: SIM_TIPOS.reduce((a,t)=>a+pide[t],0)};
    for (let i=0;i<copias(p);i++) pacientes.push(ficha);
  });
  const guardia = [];
  fuente.recursos.forEach(r => {
    // v0.14: la complicación viaja impresa en la propia carta ⚠️
    const comp = {nombre:r.comp_nombre||"", objetivo:r.comp_objetivo||"", vida:n(r.comp_vida),
                  pide:r.comp_pide||"", descarta:r.comp_descarta||""};
    for (let i=0;i<copias(r);i++) guardia.push({
      tipo:r.tipo, sistema:r.sistema, comodin:r.comodin==="si", previene:r.previene||"",
      restriccion:r.restriccion, warn:r.complicacion==="si", comp});
  });
  return {pacientes, guardia};
}

function camaNueva(f){
  return {f, vida:f.vida, pide:Object.assign({},f.pide),
          tiene:{IMAGEN:0,FARMACOS:0,PERSONAL:0,PROCEDIMIENTOS:0},
          protege:new Set(),
          estable:false, estableDesde:null, nuevo:true};
}
const faltaDe = c => {
  const o = {}; SIM_TIPOS.forEach(t => o[t] = Math.max(0, c.pide[t]-c.tiene[t])); return o;
};
const faltanTotal = c =>
  SIM_TIPOS.reduce((a,t)=>a+Math.max(0,c.pide[t]-c.tiene[t]),0);
function revisar(c, ronda){
  const completo = faltanTotal(c) === 0;
  if (completo && !c.estable){ c.estable = true; c.estableDesde = ronda; }
  else if (!completo && c.estable){ c.estable = false; c.estableDesde = null; }
}

/* Triage codicioso: mejor (puntos que se juegan) / (recursos que faltan),
   dejando al final a los que ya no alcanzan con el ingreso esperado. */
function elegirObjetivos(camas){
  const p = [];
  camas.forEach(c => {
    if (!c || c.estable) return;
    const faltan = faltanTotal(c);
    if (!faltan) return;
    p.push({c, alcanzable: faltan <= c.vida*2.1,
            valor: (c.f.alta - c.f.fallece)/faltan});
  });
  p.sort((x,y) => (x.alcanzable===y.alcanzable) ? y.valor-x.valor
                                                : (x.alcanzable ? -1 : 1));
  return p.map(x => x.c);
}

/* Devuelve [carta, aporte, tipo]. Sinergia primero (cuenta doble), luego
   recurso normal, y el comodín como último recurso. */
function elegirCarta(mano, cama){
  const falta = faltaDe(cama);
  if (SIM_TIPOS.reduce((a,t)=>a+falta[t],0) === 0) return null;
  const jugable = c =>
    !(c.restriccion === "PERSONAL" && cama.tiene.PERSONAL === 0);

  for (const c of mano)
    if (jugable(c) && c.sistema && c.sistema === cama.f.sistema && falta[c.tipo] > 0)
      return [c, 2, c.tipo];
  for (const c of mano)
    if (jugable(c) && !c.comodin && falta[c.tipo] > 0)
      return [c, 1, c.tipo];
  for (const c of mano)
    if (c.comodin){
      let t = SIM_TIPOS[0];
      SIM_TIPOS.forEach(x => { if (falta[x] > falta[t]) t = x; });
      if (falta[t] > 0) return [c, 1, t];
    }
  return null;
}

/* v0.14: cada ⚠️ trae su complicación impresa, con su 🎯 objetivo.
   Espejo de aplicar_complicacion() en tools/simular.py. */
function elegirVictima(camas, objetivo){
  const oc = camas.filter(Boolean);
  if (!oc.length) return null;
  const mejorPor = f => oc.reduce((a,b) => f(b) > f(a) ? b : a);
  if (objetivo === "MAS_GRAVE")   return mejorPor(c => -c.vida);
  if (objetivo === "MEJOR")       return mejorPor(c => c.vida);
  if (objetivo === "MAS_TRATADO") return mejorPor(c => SIM_TIPOS.reduce((a,t)=>a+c.tiene[t],0));
  if (objetivo === "ESTABLE")     return oc.find(c => c.estable) || mejorPor(c => c.vida);
  // ELIGES: el jugador se protege y descarga el golpe en el que ya perdió
  return mejorPor(c => faltanTotal(c) - c.vida);
}

function aplicarComplicacion(j, carta, descarte, camaJugada){
  const comp = carta.comp || {};
  if (!comp.objetivo) return;
  if (comp.objetivo === "MANO"){
    if (j.mano.length){
      j.mano.sort((a,b) => (a.comodin?1:0)-(b.comodin?1:0) ||
                           (a.sistema?1:0)-(b.sistema?1:0));
      descarte.push(j.mano.shift());
    }
    return;
  }
  // v0.18: ESTE = el paciente que recibió la carta (solo con disparo al colocar)
  const cama = comp.objetivo === "ESTE" ? camaJugada
                                        : elegirVictima(j.camas, comp.objetivo);
  if (!cama) return;
  // v0.20: la prevención es prospectiva — si el protector ya estaba, no ocurre
  if (comp.nombre && cama.protege.has(comp.nombre)) return;
  if (comp.vida) cama.vida += comp.vida;
  if (comp.pide) cama.pide[comp.pide] += 1;
  if (comp.descarta && cama.tiene[comp.descarta] > 0){
    cama.tiene[comp.descarta] -= 1;
    if (comp.descarta === "PERSONAL" && cama.tiene.PERSONAL <= 0) cama.protege.clear();
  }
}

function jugarPartida(pacientes, guardia, cfg, r){
  const {nJug, camasC, rondas, robo, manoMax, sumario, deterioro, gracia} = cfg;
  const mazoP = barajar(pacientes.slice(), r);
  const mazoG = barajar(guardia.slice(), r);
  const descarte = [];
  const robar = () => {
    if (!mazoG.length){
      while (descarte.length) mazoG.push(descarte.pop());
      barajar(mazoG, r);
    }
    return mazoG.length ? mazoG.pop() : null;
  };

  const jugadores = [];
  for (let i=0;i<nJug;i++)
    jugadores.push({camas:new Array(camasC).fill(null), mano:[],
                    altas:[], muertos:[], sumarios:0});
  jugadores.forEach(j => {
    for (let i=0;i<camasC;i++) if (mazoP.length){
      j.camas[i] = camaNueva(mazoP.pop()); revisar(j.camas[i], 0);
    }
  });

  const deteriorar = j => {
    j.camas.forEach((c,i) => {
      if (!c) return;
      if (c.nuevo){ c.nuevo = false; if (gracia) return; }
      if (c.estable) return;
      c.vida -= 1;
      if (c.vida <= 0){
        j.muertos.push(c.f); j.camas[i] = null;
        if (sumario) j.sumarios += 1;
      }
    });
  };

  for (let ronda=1; ronda<=rondas; ronda++){
    for (const j of jugadores){
      if (deterioro === "inicio") deteriorar(j);

      // 1. ENTREGA DE TURNO — altas
      j.camas.forEach((c,i) => {
        if (c && c.estable && c.estableDesde !== null && c.estableDesde < ronda){
          j.altas.push(c.f); j.camas[i] = null;
        }
      });
      // admisión: v0.20 OPCIONAL — revela 2, elige 1, o deja la cama vacía
      const pend = j.camas.reduce((a,c)=>a+(c?faltanTotal(c):0),0);
      j.camas.forEach((c,i) => {
        if (c !== null || !mazoP.length) return;
        if ((rondas - ronda + 1) * 3 - pend < -3) return;   // sobrecargado: no admite
        const op = [];
        for (let k=0;k<Math.min(2,mazoP.length);k++) op.push(mazoP.pop());
        let mejor = op[0];
        op.forEach(f => {
          if ((f.alta-f.fallece)/Math.max(1,f.pideTotal) >
              (mejor.alta-mejor.fallece)/Math.max(1,mejor.pideTotal)) mejor = f;
        });
        op.splice(op.indexOf(mejor),1);
        mazoP.unshift(...op);                       // el otro, al fondo
        j.camas[i] = camaNueva(mejor); revisar(j.camas[i], ronda);
      });
      // robo
      for (let k=0;k<robo;k++){
        const carta = robar();
        if (!carta) break;
        j.mano.push(carta);
      }

      // cerrar Sumarios: 2 cartas cada uno, botando lo que más sobra
      while (j.sumarios > 0 && j.mano.length >= 2){
        const sistemas = new Set(j.camas.filter(Boolean).map(c=>c.f.sistema));
        const cuenta = {};
        j.mano.forEach(c => cuenta[c.tipo] = (cuenta[c.tipo]||0)+1);
        const clave = c => [-(cuenta[c.tipo]||0), c.comodin?1:0,
                            (c.sistema && sistemas.has(c.sistema))?1:0];
        j.mano.sort((a,b) => { const x=clave(a), y=clave(b);
          return x[0]-y[0] || x[1]-y[1] || x[2]-y[2]; });
        descarte.push(j.mano.shift(), j.mano.shift());
        j.sumarios -= 1;
      }

      // 3. PASE DE VISITA — v0.20: máximo 3 recursos por turno
      let bloqueado = false, jugadas = 0;
      while (!bloqueado && jugadas < 3){
        let colocada = false;
        for (const cama of elegirObjetivos(j.camas)){
          const jugada = elegirCarta(j.mano, cama);
          if (!jugada) continue;
          const [carta, aporte, tipo] = jugada;
          j.mano.splice(j.mano.indexOf(carta),1);
          descarte.push(carta);
          cama.tiene[tipo] += aporte;
          if (carta.previene) cama.protege.add(carta.previene);
          revisar(cama, ronda);
          jugadas += 1;
          // v0.17: la ⚠️ se dispara AL COLOCAR la carta, no al robarla
          if (carta.warn){
            aplicarComplicacion(j, carta, descarte, cama);
            j.camas.forEach((c,i) => {
              if (!c) return;
              if (c.vida <= 0){
                j.muertos.push(c.f); j.camas[i] = null;
                if (sumario) j.sumarios += 1;
              } else revisar(c, ronda);
            });
          }
          colocada = true;
          if (carta.restriccion === "TURNO") bloqueado = true;
          break;
        }
        if (!colocada) break;
      }

      // descarte
      const tope = Math.max(1, manoMax - j.sumarios);
      while (j.mano.length > tope) descarte.push(j.mano.shift());

      // 4. FIN DE GUARDIA
      if (deterioro === "final") deteriorar(j);
      if (ronda < rondas)
        j.vacias = (j.vacias||0) + j.camas.filter(c=>c===null).length;
    }
  }
  return jugadores;
}

function simVacio(){
  const g = {}; GRAVEDADES.forEach(x => g[x] = [0,0]);
  return {n:0, altas:0, muertos:0, puntos:0, limpias:0, defendibles:0, grav:g};
}
function simAcumula(acc, jugadores){
  jugadores.forEach(j => {
    acc.n += 1;
    acc.altas += j.altas.length;
    acc.muertos += j.muertos.length;
    let p = -(j.vacias||0);            // v0.20: cama vacía = −1 por noche
    j.altas.forEach(f => p += f.alta);
    j.muertos.forEach(f => p += f.fallece);
    if (!j.muertos.length){ p += 3; acc.limpias += 1; }
    else if (j.muertos.every(f => f.gravedad === "III" || f.gravedad === "ROJO")){
      p += 1; acc.defendibles += 1;      // +1 "Se hizo todo"
    }
    acc.puntos += p;
    j.altas.forEach(f => { if (acc.grav[f.gravedad]) acc.grav[f.gravedad][0] += 1; });
    j.muertos.forEach(f => { if (acc.grav[f.gravedad]) acc.grav[f.gravedad][1] += 1; });
  });
}
function simResumen(acc){
  const salv = (acc.altas+acc.muertos) ? 100*acc.altas/(acc.altas+acc.muertos) : 0;
  const pct = g => { const [a,m] = acc.grav[g]; return (a+m) ? 100*a/(a+m) : null; };
  return {salv, altas:acc.altas/acc.n, muertos:acc.muertos/acc.n,
          puntos:acc.puntos/acc.n, limpias:100*acc.limpias/acc.n,
          defendibles:100*acc.defendibles/acc.n,
          gI:pct("I"), gII:pct("II"), gIII:pct("III"), gROJO:pct("ROJO")};
}

/* Corre en tandas para no congelar la página. */
async function simular(fuente, cfg, avisa){
  const {pacientes, guardia} = simCargar(fuente);
  if (!pacientes.length || !guardia.length)
    throw new Error("Necesitas al menos un paciente y un recurso con copias.");
  const r = rng32(cfg.semilla);
  const acc = simVacio();
  const TANDA = 200;
  for (let hechas=0; hechas<cfg.partidas; hechas+=TANDA){
    const hasta = Math.min(TANDA, cfg.partidas-hechas);
    for (let k=0;k<hasta;k++) simAcumula(acc, jugarPartida(pacientes, guardia, cfg, r));
    if (avisa) avisa(hechas+hasta);
    await new Promise(res => setTimeout(res, 0));
  }
  return simResumen(acc);
}

/* ── Banco de pruebas: la interfaz ───────────────────────────── */
const OBJETIVOS = {
  salv:   {nom:"Tasa de salvamento", uni:"%", obj:"55–70%",  ok:[55,70],  al:[50,75],  mejor:+1},
  altas:  {nom:"Altas por jugador",  uni:"",  obj:"2–3",     ok:[2,3],    al:[1.7,3.5],mejor:+1},
  muertos:{nom:"Fallecidos por jugador",uni:"",obj:"1–2",    ok:[1,2],    al:[0.7,2.5],mejor:-1},
  limpias:{nom:"«No se me fue nadie»", uni:"%", obj:"5–15%",   ok:[5,15],   al:[3,20],   mejor:0},
  gIII:   {nom:"Gravedad III salvada",uni:"%",obj:"40–50%",  ok:[40,50],  al:[33,57],  mejor:+1},
};
const ORDEN_SIM = ["salv","altas","muertos","limpias","gIII"];
let simCorriendo = false;

const nivelObj = (k,v) => {
  const o = OBJETIVOS[k];
  if (v === null || v === undefined || !isFinite(v)) return 2;
  if (v >= o.ok[0] && v <= o.ok[1]) return 0;
  if (v >= o.al[0] && v <= o.al[1]) return 1;
  return 2;
};
const cifra = (k,v) => (v === null || !isFinite(v)) ? "—"
  : (OBJETIVOS[k].uni === "%" ? v.toFixed(0) + "%" : v.toFixed(2));

function hayCambios(){
  return ["pacientes","recursos"].some(k =>
    JSON.stringify(DATOS[k]) !== JSON.stringify(ORIG[k]));
}
function leerMandos(){
  const v = id => document.getElementById(id).value;
  return {nJug:+v("s-jug"), camasC:+v("s-camas"), rondas:+v("s-rondas"),
          robo:+v("s-robo"), manoMax:+v("s-mano"), deterioro:v("s-reloj"),
          gracia:v("s-reloj")==="inicio", sumario:true, semilla:7,
          partidas:+v("s-partidas")};
}

function pintarSim(cfg, tuyo, base){
  let peor = 0;
  const filas = ORDEN_SIM.map(k => {
    const o = OBJETIVOS[k], v = tuyo[k];
    const lv = nivelObj(k,v); peor = Math.max(peor,lv);
    let comp = "";
    if (base){
      const d = v - base[k];
      const chico = Math.abs(d) < (o.uni === "%" ? 0.8 : 0.05);
      const clase = chico ? "d-igual" : (d*o.mejor > 0 ? "d-sube" : (o.mejor === 0 ? "d-igual" : "d-baja"));
      const signo = d > 0 ? "+" : (d < 0 ? "−" : "±");
      comp = `<td class="n"><span class="delta ${clase}">${chico ? "sin cambio"
        : signo + Math.abs(d).toFixed(o.uni === "%" ? 1 : 2) + o.uni}</span></td>
        <td class="n mono obj">${cifra(k, base[k])}</td>`;
    }
    return `<tr>
      <td>${o.nom}</td>
      <td class="n mono"><b>${cifra(k,v)}</b>
        <span class="puntos p-${CLASE[lv]}"></span></td>
      <td class="obj">${o.obj}</td>${comp}</tr>`;
  }).join("");

  const cab = `<tr><th>Métrica</th><th class="n">Tus cartas</th><th>Objetivo</th>` +
    (base ? `<th class="n">Cambio</th><th class="n">Originales</th>` : ``) + `</tr>`;
  const t = document.getElementById("s-tabla");
  t.innerHTML = `<thead>${cab}</thead><tbody>${filas}</tbody>`;
  t.hidden = false;

  const ver = document.getElementById("s-veredicto");
  ver.textContent = ["Balance en rango","Revisar lo ámbar","Fuera de rango"][peor];
  ver.className = "veredicto v-" + CLASE[peor];
  ver.hidden = false;

  const extra = [`I ${cifra("salv",tuyo.gI)}`, `II ${cifra("salv",tuyo.gII)}`,
                 `III ${cifra("salv",tuyo.gIII)}`, `ROJO ${cifra("salv",tuyo.gROJO)}`].join(" · ");
  document.getElementById("s-estado").innerHTML =
    `${cfg.partidas.toLocaleString("es")} partidas · ${cfg.nJug} jugadores · ` +
    `${cfg.camasC} camas · robo ${cfg.robo} · ${cfg.rondas} rondas. ` +
    `Puntaje medio <b class="mono">${tuyo.puntos.toFixed(1)}</b> · ` +
    `guardias con solo graves <b class="mono">${tuyo.defendibles.toFixed(0)}%</b>. ` +
    `Salvamento por gravedad: <span class="mono">${extra}</span>.` +
    (base ? "" : " Sin ediciones todavía: no hay con qué comparar.");
}

async function correrSim(){
  if (simCorriendo) return;
  simCorriendo = true;
  const boton = document.getElementById("s-correr");
  const estado = document.getElementById("s-estado");
  boton.disabled = true; boton.textContent = "Simulando…";
  const cfg = leerMandos();
  const comparar = hayCambios();
  const total = cfg.partidas * (comparar ? 2 : 1);
  let hechas = 0;
  const avanza = k => {
    estado.textContent = `Simulando… ${Math.round(100*(hechas+k)/total)}%`;
  };
  try {
    const tuyo = await simular(DATOS, cfg, avanza);
    let base = null;
    if (comparar){
      hechas = cfg.partidas;
      base = await simular(ORIG, cfg, avanza);
    }
    pintarSim(cfg, tuyo, base);
  } catch (e){
    estado.textContent = "No se pudo simular: " + e.message;
    document.getElementById("s-tabla").hidden = true;
    document.getElementById("s-veredicto").hidden = true;
  } finally {
    simCorriendo = false;
    boton.disabled = false; boton.textContent = "Simular";
  }
}

document.getElementById("s-correr").onclick = correrSim;
document.getElementById("s-jug").onchange = e => {
  // los presets del reglamento: 4 jugadores juegan con 2 camas y robo 3
  const cuatro = e.target.value === "4";
  document.getElementById("s-camas").value = cuatro ? "2" : "3";
  document.getElementById("s-robo").value = cuatro ? "3" : "4";
  document.getElementById("s-rondas").value = cuatro ? "10" : "8";
};

/* ── Tema: auto (sigue al sistema) · claro · oscuro ──────────── */
const TEMAS = ["auto","light","dark"];
const NOMTEMA = {auto:"◐ Tema: auto", light:"☀ Tema: claro", dark:"☾ Tema: oscuro"};
function ponerTema(t){
  if (t === "auto") document.documentElement.removeAttribute("data-theme");
  else document.documentElement.setAttribute("data-theme", t);
  document.getElementById("tema").textContent = NOMTEMA[t];
  try { localStorage.setItem(LLAVE + "-tema", t); } catch(e){}
}
let tema = "auto";
try { tema = localStorage.getItem(LLAVE + "-tema") || "auto"; } catch(e){}
if (!TEMAS.includes(tema)) tema = "auto";
ponerTema(tema);
document.getElementById("tema").onclick = () => {
  tema = TEMAS[(TEMAS.indexOf(tema) + 1) % TEMAS.length];
  ponerTema(tema);
};

/* ── Persistencia y arranque ─────────────────────────────────── */
function guardar(){
  try { localStorage.setItem(LLAVE, JSON.stringify(DATOS)); } catch(e){}
}
function cargar(){
  try {
    const g = JSON.parse(localStorage.getItem(LLAVE) || "null");
    if (g) for (const k of Object.keys(ESQUEMA))
      if (Array.isArray(g[k]) && g[k].length === DATOS[k].length) DATOS[k] = g[k];
  } catch(e){}
}
function refrescar(){ renderMonitor(); renderGaleria(); renderSalida(); }

cargar();
document.getElementById("pestanas").innerHTML = Object.keys(ESQUEMA).map(k =>
  `<button class="pest" role="tab" data-k="${k}" aria-selected="${k===mazo}">
    ${ESQUEMA[k].icono} ${ESQUEMA[k].titulo}</button>`).join("");
document.getElementById("pestanas").onclick = e => {
  const b = e.target.closest("[data-k]"); if (!b) return;
  mazo = b.dataset.k;
  document.querySelectorAll(".pest").forEach(p =>
    p.setAttribute("aria-selected", p.dataset.k === mazo));
  renderGaleria();
};
document.getElementById("buscar").oninput = e => { busca = e.target.value; renderGaleria(); };
document.getElementById("f-sistema").onchange = e => { filtroSis = e.target.value; renderGaleria(); };
document.getElementById("galeria").onclick = e => {
  const b = e.target.closest("[data-i]"); if (b) abrir(+b.dataset.i);
};
document.getElementById("velo").onclick = cerrar;
document.addEventListener("keydown", e => { if (e.key === "Escape" && abierta !== null) cerrar(); });
document.getElementById("modo-salida").onchange = renderSalida;
document.getElementById("seleccionar").onclick = () => {
  const t = document.getElementById("volcado"); t.focus(); t.select();
};
document.getElementById("reset").onclick = () => {
  if (!confirm("Descarta todos tus cambios y vuelve a las cartas originales.")) return;
  for (const k of Object.keys(ESQUEMA)) DATOS[k] = JSON.parse(JSON.stringify(ORIG[k]));
  try { localStorage.removeItem(LLAVE); } catch(e){}
  refrescar();
};
refrescar();
"""


def main():
    datos = cargar()
    arte = cargar_arte()
    esquema_js = {k: {"titulo": v["titulo"], "icono": v["icono"],
                      "campos": v["campos"]} for k, v in ESQUEMA.items()}

    def emb(obj):
        return json.dumps(obj, ensure_ascii=False).replace("</", "<\\/")

    html = f"""<title>Taller de Guardia</title>
<style>{CSS}</style>

<div class="env">
  <header>
    <div>
      <h1>Taller de <em>Guardia</em></h1>
      <p class="sub">Las 131 cartas de ¡Vaya Turno! (v0.15), sus constantes, el
      arte ya colocado y un editor en vivo. Tus cambios quedan guardados en
      este navegador.</p>
    </div>
    <div class="acciones-cab">
      <button class="btn" id="tema" aria-label="Cambiar tema">◐ Tema: auto</button>
      <button class="btn" id="reset">Descartar mis cambios</button>
    </div>
  </header>

  <div class="monitor" id="monitor"></div>

  <section class="banco">
    <div class="mon-cab">
      <div><span class="eyebrow">Banco de pruebas</span></div>
      <span class="veredicto v-ok" id="s-veredicto" hidden></span>
    </div>
    <p class="banco-intro">Juega miles de partidas con <strong>las cartas que
    tienes en pantalla</strong>, incluidas tus ediciones sin guardar. Modela la
    economía base: reloj, robo, sinergia, las 17 complicaciones ⚠️ exactas y el
    Sumario. No modela avatares,
    cartas de Acción ni el Trueque de Pasillo — mide el suelo del
    balance, no el techo.</p>
    <div class="mandos">
      <div class="mando"><label for="s-jug">Jugadores</label>
        <select id="s-jug"><option>2</option><option selected>3</option><option>4</option></select></div>
      <div class="mando"><label for="s-camas">Camas</label>
        <select id="s-camas"><option>2</option><option selected>3</option><option>4</option></select></div>
      <div class="mando"><label for="s-robo">Robo</label>
        <select id="s-robo"><option>2</option><option>3</option><option selected>4</option><option>5</option><option>6</option></select></div>
      <div class="mando"><label for="s-rondas">Rondas</label>
        <select id="s-rondas"><option>6</option><option selected>8</option><option>10</option><option>12</option></select></div>
      <div class="mando"><label for="s-mano">Mano</label>
        <select id="s-mano"><option>4</option><option selected>5</option><option>6</option><option>7</option></select></div>
      <div class="mando"><label for="s-reloj">Deterioro</label>
        <select id="s-reloj">
          <option value="final" selected>Fin de Guardia (v0.12)</option>
          <option value="inicio">Al abrir el turno (v0.11)</option>
        </select></div>
      <div class="mando"><label for="s-partidas">Partidas</label>
        <select id="s-partidas"><option>300</option><option selected>1000</option><option>3000</option></select></div>
      <button class="btn primario" id="s-correr">Simular</button>
    </div>
    <p class="estado-sim" id="s-estado">Aún no has simulado nada. Con 1.000
    partidas basta para decidir; el ruido es de ±1–2 puntos.</p>
    <div class="sim-envuelve"><table class="tabla-sim" id="s-tabla" hidden></table></div>
    <p class="sim-pie">El número que va al reglamento sale de
    <span class="mono">tools/simular.py</span>: mismo motor, más partidas.
    Este corre en tu navegador para que puedas iterar sin salir de la página.</p>
  </section>

  <div class="filtros">
    <div class="pestanas" id="pestanas" role="tablist"></div>
    <input type="search" id="buscar" placeholder="Buscar por nombre, texto o frase…"
           aria-label="Buscar cartas">
    <select class="filtro" id="f-sistema" aria-label="Filtrar por sistema">
      <option value="">Todos los sistemas</option>
      <option value="RESP">🫁 Respiratorio</option>
      <option value="CARD">🫀 Cardíaco</option>
      <option value="NEURO">🧠 Neurológico</option>
      <option value="METAB">🧪 Metabólico</option>
      <option value="QUIR">🔪 Quirúrgico</option>
      <option value="INFEC">Infeccioso</option>
      <option value="GENERAL">General</option>
    </select>
    <span class="cuenta" id="cuenta"></span>
  </div>

  <div class="galeria" id="galeria"></div>

  <section class="salida">
    <h2>Llevárselo</h2>
    <p>Elige qué sacar y cópialo. El <strong>parte de cambios</strong> es lo más
    útil para pegarme: dice qué tocaste y qué valor tenía antes. El CSV completo
    sirve si cambiaste muchas cartas de un mazo.</p>
    <div class="acciones-cab">
      <select class="filtro" id="modo-salida" aria-label="Qué exportar">
        <option value="diff">Parte de cambios</option>
        {"".join(f'<option value="{k}">CSV · {v["titulo"]}</option>' for k, v in ESQUEMA.items())}
      </select>
      <button class="btn primario" id="seleccionar">Seleccionar todo para copiar</button>
    </div>
    <textarea class="volcado" id="volcado" readonly
      aria-label="Contenido para copiar"></textarea>
  </section>
</div>

<button class="velo oculto" id="velo" aria-label="Cerrar editor"></button>
<div class="cajon oculto" id="cajon" role="dialog" aria-label="Editor de carta"></div>

<script>
window.__DATOS__ = {emb(datos)};
window.__ESQUEMA__ = {emb(esquema_js)};
window.__ARTE__ = {emb(arte)};
</script>
<script>{JS}</script>
"""
    salida = os.path.join(RAIZ, "taller.html")
    with open(salida, "w", encoding="utf-8") as f:
        f.write(html)
    total = sum(sum(int(r.get("copias", 1) or 1) for r in v) for v in datos.values())
    print(f"✔ Taller con {total} cartas y {len(arte)} ilustraciones → {salida}")


if __name__ == "__main__":
    main()
