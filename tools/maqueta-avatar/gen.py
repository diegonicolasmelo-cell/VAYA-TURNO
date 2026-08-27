#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Prototipo tocable: la carta de avatar se agranda, se centra y se gira."""
import base64, csv, html, os
RAIZ = "/home/user/VAYA-TURNO"
AQUI = os.path.dirname(os.path.abspath(__file__))

def leer(*p): return list(csv.DictReader(open(os.path.join(RAIZ, *p), encoding="utf-8")))
def uri(cid):
    return "data:image/webp;base64," + base64.b64encode(
        open(os.path.join(AQUI, cid + ".webp"), "rb").read()).decode()
def e(s): return html.escape(s or "")

PER = {f["id"]: f for f in leer("cartas", "personajes.csv")}
TINTE = {"C01": "#e9eef0", "C19": "#85a39c", "C17": "#e8e5cf"}

def carta(cid, foco="center 20%"):
    c = PER[cid]
    hab = c["habilidad"]
    tit, hab = hab.split(" — ", 1) if " — " in hab else ("", hab)
    return f'''<div class="carta" data-id="{cid}" style="--tinte:{TINTE[cid]}">
 <div class="giro">
  <div class="cara frente">
   <div class="zona"><img src="{uri(cid)}" alt="{e(c['nombre'])}" style="object-position:{foco}">
    <div class="disuelve"></div>
    <div class="chips"><i class="chip">avatar</i><i class="chip hueco">{e(c['frecuencia'])}</i></div></div>
   <div class="panel">
    <h3>{e(c['nombre'])}</h3>
    {f'<p class="habtit">{e(tit)}</p>' if tit else ''}
    <p class="regla">{e(hab)}</p>
   </div>
  </div>
  <div class="cara dorso">
   <img src="{uri(cid)}" alt="" style="object-position:{foco}">
   <div class="lustre"></div>
   <div class="pieza-nom"><h3>{e(c['nombre'])}</h3>
    <p class="frase">{e(c['frase'])}</p></div>
  </div>
 </div></div>'''


CSS = """
:root{
  --fondo:#e7ecee; --panel:#fbfcfd; --linea:#c6d3d8; --tinta:#15242b;
  --tinta-2:#5b7480; --acento:#0d6e78; --alerta:#b0442c; --ok:#237a5b;
  --sombra:0 1px 2px rgba(20,40,48,.08), 0 8px 24px rgba(20,40,48,.10);
  --papel:#fdfefe; --papel-tinta:#15242b; --papel-2:#5b7480;
}
@media (prefers-color-scheme: dark){ :root:not([data-theme="light"]){
  --fondo:#0f1619; --panel:#192328; --linea:#2a373d; --tinta:#e3ecef;
  --tinta-2:#93a8b1; --acento:#54c0c8; --alerta:#e08a70; --ok:#5fbb92;
  --sombra:0 1px 2px rgba(0,0,0,.4), 0 10px 30px rgba(0,0,0,.45);
}}
:root[data-theme="dark"]{
  --fondo:#0f1619; --panel:#192328; --linea:#2a373d; --tinta:#e3ecef;
  --tinta-2:#93a8b1; --acento:#54c0c8; --alerta:#e08a70; --ok:#5fbb92;
  --sombra:0 1px 2px rgba(0,0,0,.4), 0 10px 30px rgba(0,0,0,.45);
}
*{box-sizing:border-box}
body{margin:0;background:var(--fondo);color:var(--tinta);
  font-family:"Archivo Narrow","Helvetica Neue",Arial,sans-serif;line-height:1.55}
.env{max-width:760px;margin:0 auto;padding:34px 20px 80px}
.eyebrow{font-family:"IBM Plex Mono",ui-monospace,monospace;font-size:11px;
  letter-spacing:.16em;text-transform:uppercase;color:var(--acento);margin:0 0 8px}
h1{font-family:Petrona,Georgia,serif;font-weight:700;font-size:clamp(28px,6vw,40px);
  line-height:1.06;margin:0 0 10px;text-wrap:balance}
h2{font-family:Petrona,Georgia,serif;font-weight:700;font-size:clamp(21px,4vw,27px);
  margin:0 0 8px;text-wrap:balance}
p{max-width:64ch} .bajada{color:var(--tinta-2);margin:0 0 4px}
section{margin-top:44px;padding-top:26px;border-top:1px solid var(--linea)}
.nota{background:var(--panel);border:1px solid var(--linea);border-radius:10px;
  padding:14px 16px;margin:18px 0;box-shadow:var(--sombra)}
.nota.bien{border-left:4px solid var(--ok)}
.nota.grave{border-left:4px solid var(--alerta)}
.nota p{margin:0} .nota p+p{margin-top:8px}
.nota h4{font-family:"IBM Plex Mono",ui-monospace,monospace;font-size:11px;
  letter-spacing:.13em;text-transform:uppercase;color:var(--tinta-2);margin:0 0 6px}
ul.lista{max-width:64ch;padding-left:0;list-style:none;margin:12px 0}
ul.lista li{padding-left:20px;position:relative;margin-bottom:8px}
ul.lista li::before{content:"";position:absolute;left:2px;top:.62em;width:7px;height:7px;
  border-radius:2px;background:var(--acento)}

/* ══ la barra del avatar, como en la app ═══════════════════════════ */
.barra{display:flex;align-items:center;gap:10px;background:var(--papel);
  border-left:4px solid var(--acento);border-radius:11px;padding:9px 12px;
  box-shadow:var(--sombra);cursor:pointer;color:var(--papel-tinta);
  border:1px solid var(--linea);border-left:4px solid var(--acento);
  width:100%;text-align:left;font:inherit}
.barra:hover,.barra:focus-visible{box-shadow:0 0 0 2px var(--acento),var(--sombra);outline:none}
.barra .mini{width:34px;height:47px;border-radius:5px;object-fit:cover;flex:none;
  object-position:center 18%}
.barra .txt{flex:1;min-width:0}
.barra .rot{font-family:"IBM Plex Mono",ui-monospace,monospace;font-size:9.5px;
  letter-spacing:.11em;text-transform:uppercase;color:var(--papel-2)}
.barra .nom{font-family:Petrona,Georgia,serif;font-weight:700;font-size:17px;line-height:1.15}
.barra .pista{font-family:"IBM Plex Mono",ui-monospace,monospace;font-size:9.5px;
  letter-spacing:.08em;text-transform:uppercase;color:var(--acento);flex:none}
.barras{display:flex;flex-direction:column;gap:11px;margin-top:18px}

/* ══ el escenario: velo + carta centrada ═════════════════════════════ */
.velo{position:fixed;inset:0;z-index:50;background:rgba(9,18,22,.72);
  backdrop-filter:blur(7px);-webkit-backdrop-filter:blur(7px);
  display:grid;place-items:center;padding:22px;
  opacity:0;pointer-events:none;transition:opacity .26s ease}
.velo.abierto{opacity:1;pointer-events:auto}
.escena{perspective:1400px;display:flex;flex-direction:column;align-items:center;gap:16px}

.carta{--w:min(78vw, 260px);width:var(--w);height:calc(var(--w)*1.3968);
  position:relative;flex:none;font-size:calc(var(--w)*.0721);
  transform:scale(.82) translateY(14px);opacity:0;
  transition:transform .34s cubic-bezier(.2,.9,.3,1), opacity .26s ease}
.velo.abierto .carta{transform:none;opacity:1}
.giro{position:absolute;inset:0;transform-style:preserve-3d;
  transition:transform .62s cubic-bezier(.3,.9,.25,1)}
.carta.vuelta .giro{transform:rotateY(180deg)}
.cara{position:absolute;inset:0;backface-visibility:hidden;-webkit-backface-visibility:hidden;
  border-radius:calc(var(--w)*.045);overflow:hidden;background:var(--papel);
  box-shadow:0 18px 44px rgba(0,0,0,.5);border:calc(var(--w)*.015) solid var(--acento);
  display:flex;flex-direction:column}
.cara.dorso{transform:rotateY(180deg);background:var(--tinte)}

/* frente: la maquetación B, arte arriba y reglas en panel sólido */
.frente .zona{position:relative;height:calc(var(--w)*.727);flex:none;
  background:var(--tinte);overflow:hidden}
.frente .zona img{position:absolute;inset:0;width:78%;left:11%;height:100%;
  object-fit:cover;display:block}
.frente .disuelve{position:absolute;inset:auto 0 0;height:22%;
  background:linear-gradient(to top,var(--papel),rgba(253,254,254,0))}
.frente .chips{position:absolute;top:.42em;left:.46em;display:flex;gap:.26em}
.chip{font-family:"IBM Plex Mono",ui-monospace,monospace;font-size:.54em;font-weight:600;
  letter-spacing:.05em;text-transform:uppercase;font-style:normal;padding:.2em .48em;
  border-radius:.38em;background:var(--acento);color:#fff;line-height:1.6}
.chip.hueco{background:rgba(255,255,255,.16);border:1px solid rgba(255,255,255,.5)}
.frente .panel{flex:1 1 0;padding:.1em .58em .5em;display:flex;flex-direction:column;
  gap:.2em;min-height:0;color:var(--papel-tinta)}
.frente h3{font-family:Petrona,Georgia,serif;font-weight:700;font-size:1em;margin:0;line-height:1.06}
.habtit{margin:0;font-family:"IBM Plex Mono",ui-monospace,monospace;font-size:.5em;
  font-weight:700;letter-spacing:.07em;color:var(--acento)}
.regla{margin:0;font-size:.57em;line-height:1.34}

/* dorso: full art de verdad, sin una palabra de reglas */
.dorso img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;display:block}
.dorso .pieza-nom{position:absolute;inset:auto 0 0;padding:1.1em .8em .8em;color:#fff;
  background:linear-gradient(to top,rgba(6,14,18,.86),rgba(6,14,18,.5) 55%,transparent)}
.dorso h3{font-family:Petrona,Georgia,serif;font-weight:700;font-size:1.1em;margin:0;
  line-height:1.06;text-shadow:0 1px 6px rgba(0,0,0,.8)}
.dorso .frase{margin:.3em 0 0;font-family:Petrona,Georgia,serif;font-style:italic;
  font-size:.62em;line-height:1.28;text-shadow:0 1px 5px rgba(0,0,0,.85)}
/* el lustre solo vive en el dorso: es el lado bonito */
.dorso .lustre{position:absolute;inset:0;pointer-events:none;background:linear-gradient(
  108deg, transparent 32%, rgba(255,255,255,.05) 42%, rgba(255,255,255,.30) 48%,
  rgba(150,200,255,.16) 54%, transparent 64%);
  background-size:260% 100%;background-position:130% 0}
@media (prefers-reduced-motion: no-preference){
  .carta.vuelta .dorso .lustre{animation:lustre 4.2s ease-in-out .35s infinite}}
@keyframes lustre{0%,40%{background-position:135% 0}100%{background-position:-55% 0}}

.mandos{display:flex;gap:10px;align-items:center}
.btn{font:inherit;font-size:14px;font-weight:600;padding:9px 16px;border-radius:999px;
  border:1px solid rgba(255,255,255,.32);background:rgba(255,255,255,.12);color:#fff;
  cursor:pointer;backdrop-filter:blur(6px);-webkit-backdrop-filter:blur(6px)}
.btn:hover,.btn:focus-visible{background:rgba(255,255,255,.24);outline:none}
.btn.pri{background:#fdfefe;color:#15242b;border-color:transparent}
.ayuda{font-family:"IBM Plex Mono",ui-monospace,monospace;font-size:10.5px;
  letter-spacing:.1em;text-transform:uppercase;color:rgba(255,255,255,.72);margin:0}

@media (prefers-reduced-motion: reduce){
  .giro,.carta{transition:none}
}
"""

JS = """
const velo = document.getElementById('velo');
const escena = document.getElementById('escena');
const cartas = {};
document.querySelectorAll('.carta').forEach(c => { cartas[c.dataset.id] = c; c.remove(); });
let viva = null;

function abrir(id){
  if(viva) viva.remove();
  viva = cartas[id];
  viva.classList.remove('vuelta');
  escena.prepend(viva);
  velo.classList.add('abierto');
  document.body.style.overflow = 'hidden';
  requestAnimationFrame(()=>document.getElementById('girar').focus());
}
function cerrar(){
  velo.classList.remove('abierto');
  document.body.style.overflow = '';
}
function girar(){ if(viva) viva.classList.toggle('vuelta'); }

document.querySelectorAll('.barra').forEach(b =>
  b.addEventListener('click', ()=>abrir(b.dataset.abre)));
document.getElementById('girar').addEventListener('click', girar);
document.getElementById('cerrar').addEventListener('click', cerrar);
velo.addEventListener('click', ev => { if(ev.target === velo) cerrar(); });
escena.addEventListener('click', ev => { if(ev.target.closest('.carta')) girar(); });
document.addEventListener('keydown', ev => {
  if(!velo.classList.contains('abierto')) return;
  if(ev.key === 'Escape') cerrar();
  if(ev.key === ' ' || ev.key === 'Enter'){ ev.preventDefault(); girar(); }
});
"""


def barra(cid):
    c = PER[cid]
    return f'''<button class="barra" data-abre="{cid}">
 <img class="mini" src="{uri(cid)}" alt="">
 <span class="txt"><span class="rot">tu avatar · {e(c['frecuencia'])}</span>
  <span class="nom">{e(c['nombre'])}</span></span>
 <span class="pista">ver ▸</span></button>'''

CUERPO = f'''
<div class="env">
<p class="eyebrow">Prototipo tocable · tócalo, no lo leas</p>
<h1>El avatar se agranda y se gira</h1>
<p class="bajada">Toca una barra: la carta crece, se centra y se puede girar
sobre su propio eje. Tócala otra vez, o usa el botón. En el teléfono es
donde hay que probarlo.</p>

<div class="barras">{barra("C01")}{barra("C19")}{barra("C17")}</div>

<section>
<h2>Por qué así y no al revés</h2>
<p>Preguntaste si el texto va al reverso girando la carta, o si se consulta
al seleccionarla. <strong>Las dos cosas son la misma cosa</strong>, porque
girar una carta de 132&nbsp;px te deja un reverso de 132&nbsp;px con 250
caracteres: ilegible. Para leer, la carta tiene que crecer. Y una vez que
creció, girarla es el gesto natural.</p>

<div class="nota grave">
<h4>Pero el reverso NO puede llevar las reglas</h4>
<p>Al empezar la partida eliges entre tres avatares. Si la habilidad está al
reverso, <strong>tienes que girar tres cartas para poder comparar</strong>, y
la decisión más importante del inicio pasa a ser un juego de memoria.</p>
<p>En papel es peor: la carta queda frente a ti toda la partida. Si la dejas
por el lado de la habilidad, nunca ves el dibujo; si la dejas por el dibujo,
no recuerdas tu poder.</p>
</div>

<div class="nota bien">
<h4>Se resuelve dándolo vuelta</h4>
<p>La habilidad va <strong>al frente</strong>, como quedó en la opción B. Lo
que hay al reverso es <strong>la ilustración completa, a sangre, sin una sola
palabra</strong> — con el lustre encima. Es tu opción C, pero como premio en
vez de como problema.</p>
<p>Así nunca escondes lo que necesitas, y ganas full art de verdad en la
carta que más te importa: la tuya.</p>
</div>

<ul class="lista">
<li><strong>Al elegir avatar</strong> los tres se ven de frente, con la
habilidad legible. Comparas sin girar nada.</li>
<li><strong>Durante la partida</strong> la barra de abajo te recuerda el
nombre; la tocas y la carta crece si necesitas releer la habilidad.</li>
<li><strong>El giro</strong> es para mirar el dibujo. No tiene función de
juego, y por eso puede ser puro gusto.</li>
<li><strong>En papel</strong> funciona igual: dejas la carta por el lado de
la habilidad y le das vuelta cuando quieras verte bonito.</li>
</ul>
</section>

<section>
<h2>Lo demás que decidiste</h2>
<p><strong>La frase de sabor se queda en los pacientes.</strong> Cabe: va bajo
las filas de requerimiento, encima de la línea de alta y fallece, en cursiva
y a menor cuerpo. En la carta chica de la cama se cae junto con el resto del
texto, que ahí ya no se lee igual.</p>
</section>
</div>

<div class="velo" id="velo">
 <div class="escena" id="escena">
  <div class="mandos">
   <button class="btn pri" id="girar">Girar la carta</button>
   <button class="btn" id="cerrar">Cerrar</button>
  </div>
  <p class="ayuda">También puedes tocar la carta</p>
 </div>
</div>
'''

PAG = f'''<title>El avatar se gira</title>
<script>
/* El artefacto arma su propio <head> y no trae viewport: sin esto el
   teléfono maqueta a 980 px y todo sale diminuto. Mismo parche que ya
   lleva la app en tools/app-plantilla.html. */
if(!document.querySelector(\'meta[name="viewport"]\')){{
  const mv = document.createElement("meta");
  mv.name = "viewport";
  mv.content = "width=device-width, initial-scale=1, viewport-fit=cover";
  document.head.appendChild(mv);
}}
</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Petrona:ital,wght@0,400;0,700;1,400&family=Archivo+Narrow:wght@400;600;700&family=IBM+Plex+Mono:wght@400;600;700&display=swap">
<style>{CSS}</style>
{CUERPO}
{"".join(carta(c) for c in ("C01","C19","C17"))}
<script>{JS}</script>
'''
sal = os.path.join(AQUI, "avatar-giro.html")
open(sal, "w", encoding="utf-8").write(PAG)
print(f"✔ {sal} ({os.path.getsize(sal)/1024:.0f} KB)")
