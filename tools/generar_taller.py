#!/usr/bin/env python3
"""
Genera el TALLER DE GUARDIA: una sola página con las 159 cartas dentro,
el tablero de constantes del mazo y un editor en vivo.

    python3 tools/generar_taller.py        # → taller.html

Los CSV de cartas/ son la fuente de la verdad; esto los empaqueta en HTML.
Cuando cambien los CSV, vuelve a correrlo.
"""

import csv
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CARTAS = os.path.join(RAIZ, "cartas")

# Esquema de edición: por mazo, qué columnas y con qué control se editan.
# num = campo numérico · sel = desplegable · txt = línea · area = párrafo
SIS = ["", "RESP", "CARD", "NEURO", "METAB", "QUIR"]
ESQUEMA = {
    "pacientes": {
        "titulo": "Pacientes", "archivo": "pacientes.csv", "icono": "🛏️",
        "campos": [
            ("nombre", "txt", None), ("gravedad", "sel", ["I", "II", "III", "ROJO"]),
            ("sistema", "sel", SIS[1:]), ("vida", "num", None),
            ("img", "num", None), ("far", "num", None),
            ("per", "num", None), ("mon", "num", None),
            ("puntos_alta", "num", None), ("puntos_fallece", "num", None),
            ("frase", "area", None), ("copias", "num", None),
        ],
    },
    "recursos": {
        "titulo": "Recursos", "archivo": "recursos.csv", "icono": "💊",
        "campos": [
            ("nombre", "txt", None),
            ("tipo", "sel", ["IMAGEN", "FARMACOS", "PERSONAL", "MONITOREO", "COMODIN"]),
            ("sistema", "sel", SIS), ("comodin", "sel", ["no", "si"]),
            ("restriccion", "sel", ["", "PERSONAL", "TURNO"]),
            ("complicacion", "sel", ["no", "si"]),
            ("copias", "num", None), ("frase", "area", None),
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
    "eventos": {
        "titulo": "Eventos Centinela", "archivo": "eventos.csv", "icono": "⚠️",
        "campos": [
            ("nombre", "txt", None),
            ("categoria", "sel", ["RESP", "CARD", "NEURO", "METAB", "INFEC", "GENERAL"]),
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
.c-req{display:grid;grid-template-columns:1fr 1fr;gap:.1rem .3rem;font-size:.72rem;
  font-weight:700;font-family:ui-monospace,Menlo,monospace}
.c-req .off{color:var(--linea-fuerte);font-weight:400}
.c-pts{display:flex;justify-content:space-between;font-size:.65rem;font-weight:700}
.c-vida{font-size:.95rem;font-weight:800;white-space:nowrap}
.c-cab{display:flex;justify-content:space-between;align-items:flex-start;gap:.3rem}
.c-glifo{font-size:1.6rem;text-align:center;margin:auto 0;line-height:1}
.c-warn{font-size:.56rem;font-weight:800;color:var(--mal);letter-spacing:.04em}
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
const DATOS = window.__DATOS__, ESQUEMA = window.__ESQUEMA__;
const ORIG = JSON.parse(JSON.stringify(DATOS));
const TIPOS = ["FARMACOS","IMAGEN","MONITOREO","PERSONAL"];
const NOMT = {IMAGEN:"Imagen",FARMACOS:"Fármacos",PERSONAL:"Personal",
              MONITOREO:"Soporte Vital",COMODIN:"Comodín"};
const GLIFO = {IMAGEN:"🩻",FARMACOS:"💊",PERSONAL:"🧑‍⚕️",MONITOREO:"📈",COMODIN:"🃏"};
const SISTEMAS = ["RESP","CARD","NEURO","METAB","QUIR"];
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
  const COL = {IMAGEN:"img",FARMACOS:"far",PERSONAL:"per",MONITOREO:"mon"};
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

  // Sinergia por sistema: recursos específicos vs pacientes
  const filas = SISTEMAS.map(s => {
    const {rec,pac} = b.sis[s];
    const ratio = pac ? rec/pac : (rec ? 9 : 0);
    const lv = pac===0 ? 2 : nivel(Math.abs(Math.log(ratio||0.01)), 0.36, 0.7);
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
        <div class="barra-txt">Objetivo: tantos recursos específicos como pacientes de ese sistema.</div>
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
      </div>
    </div>`;
}

/* ── Galería ─────────────────────────────────────────────────── */
function tocada(k,i){ return JSON.stringify(DATOS[k][i]) !== JSON.stringify(ORIG[k][i]); }

function pintarCarta(k,f,i){
  const arte = `<div class="c-arte">arte</div>`;
  const t = s => arte + `<div class="c-frase">${esc(s)}</div>`;
  let dentro = "";
  if (k === "pacientes"){
    const req = [["IMAGEN","img"],["FARMACOS","far"],["PERSONAL","per"],["MONITOREO","mon"]]
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
    dentro = `<div class="c-cab"><div>
        <div class="c-nom">${esc(f.nombre)}</div>
        <div class="c-meta">${NOMT[f.tipo]||esc(f.tipo)}</div></div>
        <div class="c-vida">${GLIFO[f.tipo]||""}</div></div>
      ${chip}${nota}${rest}
      ${f.complicacion==="si"?'<div class="c-warn">⚠️ COMPLICACIÓN</div>':""}${t(f.frase)}`;
  } else if (k === "personajes"){
    dentro = `<div class="c-nom">${esc(f.nombre)}</div>
      <div class="c-meta">${esc(f.frecuencia)}</div>
      <div class="c-cuerpo">${esc(f.habilidad)}</div>${t(f.frase)}`;
  } else {
    const cat = f.categoria ? `<span class="chip ${esc(f.categoria)}">${esc(f.categoria)}</span>` : "";
    dentro = `<div class="c-nom">${esc(f.nombre)}</div>
      <div class="c-meta">${esc(f.tipo || f.categoria || "Maldición")}</div>${cat}
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
  document.getElementById("cajon").innerHTML = `
    <div class="cajon-cab">
      <div><div class="eyebrow">${ESQUEMA[mazo].icono} ${ESQUEMA[mazo].titulo} · ${esc(f.id)}</div>
        <strong style="font-size:1.02rem">${esc(f.nombre)}</strong></div>
      <button class="btn" id="cerrar" aria-label="Cerrar">✕</button>
    </div>
    <div class="cajon-cuerpo">
      ${largos.filter(c=>c[0]==="nombre").map(ctrl).join("")}
      <div class="fila-campos">${cortos.map(ctrl).join("")}</div>
      ${largos.filter(c=>c[0]!=="nombre").map(ctrl).join("")}
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
      p.total_recursos = String(n(p.img)+n(p.far)+n(p.per)+n(p.mon));
    }
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
      <p class="sub">Las 159 cartas de ¡Vaya Turno!, sus constantes y un editor
      en vivo. Tus cambios quedan guardados en este navegador.</p>
    </div>
    <div class="acciones-cab">
      <button class="btn" id="reset">Descartar mis cambios</button>
    </div>
  </header>

  <div class="monitor" id="monitor"></div>

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
</script>
<script>{JS}</script>
"""
    salida = os.path.join(RAIZ, "taller.html")
    with open(salida, "w", encoding="utf-8") as f:
        f.write(html)
    total = sum(sum(int(r.get("copias", 1) or 1) for r in v) for v in datos.values())
    print(f"✔ Taller con {total} cartas → {salida}")


if __name__ == "__main__":
    main()
