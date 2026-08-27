# -*- coding: utf-8 -*-
CSS = """
:root{
  --fondo:#e7ecee; --panel:#fbfcfd; --panel-2:#f0f4f6;
  --linea:#c6d3d8; --linea-2:#dde6e9;
  --tinta:#15242b; --tinta-2:#5b7480; --tinta-3:#8ba0a9;
  --acento:#0d6e78; --alerta:#b0442c; --ok:#237a5b; --oro:#b0842a;
  --sombra:0 1px 2px rgba(20,40,48,.08), 0 8px 24px rgba(20,40,48,.10);
  --papel:#fdfefe; --papel-tinta:#15242b; --papel-2:#5b7480; --papel-linea:rgba(20,40,48,.16);
}
@media (prefers-color-scheme: dark){ :root:not([data-theme="light"]){
  --fondo:#0f1619; --panel:#192328; --panel-2:#141d21;
  --linea:#2a373d; --linea-2:#212d32;
  --tinta:#e3ecef; --tinta-2:#93a8b1; --tinta-3:#6b8189;
  --acento:#54c0c8; --alerta:#e08a70; --ok:#5fbb92; --oro:#d9ac53;
  --sombra:0 1px 2px rgba(0,0,0,.4), 0 10px 30px rgba(0,0,0,.45);
}}
:root[data-theme="dark"]{
  --fondo:#0f1619; --panel:#192328; --panel-2:#141d21;
  --linea:#2a373d; --linea-2:#212d32;
  --tinta:#e3ecef; --tinta-2:#93a8b1; --tinta-3:#6b8189;
  --acento:#54c0c8; --alerta:#e08a70; --ok:#5fbb92; --oro:#d9ac53;
  --sombra:0 1px 2px rgba(0,0,0,.4), 0 10px 30px rgba(0,0,0,.45);
}
/* el papel de la carta NO cambia con el tema: una carta impresa no tiene
   modo oscuro, y si lo tuviera dejaría de parecer una carta */

*{box-sizing:border-box}
body{margin:0;background:var(--fondo);color:var(--tinta);
  font-family:"Archivo Narrow","Helvetica Neue",Arial,sans-serif;
  font-size:16px;line-height:1.55;-webkit-text-size-adjust:100%}
.env{max-width:1080px;margin:0 auto;padding:38px 20px 90px}
.eyebrow{font-family:"IBM Plex Mono",ui-monospace,monospace;font-size:11px;
  letter-spacing:.16em;text-transform:uppercase;color:var(--acento);margin:0 0 8px}
h1{font-family:Petrona,Georgia,serif;font-weight:700;font-size:clamp(30px,6vw,44px);
  line-height:1.06;margin:0 0 10px;text-wrap:balance}
h2{font-family:Petrona,Georgia,serif;font-weight:700;font-size:clamp(22px,4.2vw,30px);
  line-height:1.12;margin:0 0 8px;text-wrap:balance}
.bajada{color:var(--tinta-2);max-width:64ch;margin:0 0 6px}
p{max-width:66ch}
section{margin-top:52px;padding-top:30px;border-top:1px solid var(--linea)}
strong{font-weight:700}
ul.lista{max-width:66ch;padding-left:0;list-style:none;margin:14px 0}
ul.lista li{padding-left:20px;position:relative;margin-bottom:9px}
ul.lista li::before{content:"";position:absolute;left:2px;top:.62em;width:7px;height:7px;
  border-radius:2px;background:var(--acento)}
.nota{background:var(--panel);border:1px solid var(--linea);border-radius:10px;
  padding:14px 16px;margin:20px 0;box-shadow:var(--sombra)}
.nota.grave{border-left:4px solid var(--alerta)}
.nota.bien{border-left:4px solid var(--ok)}
.nota p{margin:0} .nota p + p{margin-top:8px}
.nota h4{font-family:"IBM Plex Mono",ui-monospace,monospace;font-size:11px;
  letter-spacing:.13em;text-transform:uppercase;color:var(--tinta-2);margin:0 0 6px}

/* ══ la carta, común a las tres ══════════════════════════════════════ */
/* El alto va explícito y no por aspect-ratio: con aspect-ratio el reparto
   flex de los hijos se calculaba contra un alto indefinido, el panel no
   crecía y el texto quedaba cortado. 88/63 = 1,3968. */
.cta{--w:222px;position:relative;width:var(--w);height:calc(var(--w)*1.3968);flex:none;
  border-radius:calc(var(--w)*.045);overflow:hidden;isolation:isolate;
  background:var(--papel);color:var(--papel-tinta);box-shadow:var(--sombra);
  /* px * número / número = px. `var(--w)/222*1rem` era inválido —px
     dividido por un número da px, y px por rem no existe— así que el
     calc se descartaba entero y TODAS las cartas heredaban 16 px, con
     lo que la carta chica llevaba la letra de la grande. 16/222 = ,0721 */
  font-size:calc(var(--w)*.0721);display:flex;flex-direction:column}
.cta::after{content:"";position:absolute;inset:0;pointer-events:none;border-radius:inherit;
  border:calc(var(--w)*.015) solid var(--tipo);box-shadow:inset 0 0 0 1px rgba(255,255,255,.2)}
.cta h3{font-family:Petrona,Georgia,serif;font-weight:700;font-size:1em;
  line-height:1.06;margin:0;text-wrap:balance}
.chip,.frec,.coste,.tic,.hpnum{font-family:"IBM Plex Mono",ui-monospace,monospace;
  font-size:.54em;font-weight:600;letter-spacing:.05em;text-transform:uppercase;
  font-style:normal;line-height:1.6;padding:.2em .48em;border-radius:.38em;color:#fff}
.chip.hueco{background:rgba(255,255,255,.15);border:1px solid rgba(255,255,255,.45)}
.chips{display:flex;gap:.26em;align-items:center;flex-wrap:wrap}
.coste{background:#f5c916;color:#1d2b17;border-radius:50%;width:1.6em;height:1.6em;
  display:grid;place-items:center;padding:0;font-size:.74em;font-weight:700}
.hp{width:.5em;height:.5em;background:#c0492f;display:inline-block;flex:none;
  clip-path:polygon(50% 100%,0 38%,0 16%,14% 0,36% 0,50% 16%,64% 0,86% 0,100% 16%,100% 38%)}

/* las filas de requerimiento: fichas de color + nombre + número. Es la
   gramática del coste de energía de Pokémon, y funciona por lo mismo */
.reqs{display:flex;flex-direction:column;gap:.14em}
.req{display:flex;align-items:center;gap:.32em;font-size:.56em;line-height:1.5}
.fis{display:flex;gap:.14em;flex:none}
.fi{width:.62em;height:.62em;border-radius:50%;display:block;
  box-shadow:inset 0 -.1em .12em rgba(0,0,0,.28)}
.rnom{flex:1;color:var(--papel-2);letter-spacing:.02em}
.req b{font-family:"IBM Plex Mono",ui-monospace,monospace;font-weight:700}
.pie{display:flex;justify-content:space-between;margin-top:.3em;padding-top:.26em;
  border-top:1px solid var(--papel-linea);font-family:"IBM Plex Mono",ui-monospace,monospace;
  font-size:.5em;letter-spacing:.04em;text-transform:uppercase;color:var(--papel-2)}
.pie b{color:var(--papel-tinta)}
.regla{margin:0;font-size:.57em;line-height:1.34}
.habtit{margin:0 0 .18em;font-family:"IBM Plex Mono",ui-monospace,monospace;
  font-size:.5em;font-weight:700;letter-spacing:.07em;color:var(--acento)}
.frase{margin:.26em 0 0;font-family:Petrona,Georgia,serif;font-style:italic;
  font-size:.56em;line-height:1.26;color:var(--papel-2)}
.frase.clara{color:rgba(255,255,255,.94);text-shadow:0 1px 4px rgba(0,0,0,.85);margin:0}

/* ── A · VENTANA ─────────────────────────────────────────────────── */
.va{padding:calc(var(--w)*.032);gap:.3em;background:var(--papel)}
.va .tit{display:flex;align-items:baseline;gap:.4em;padding:0 .1em}
.va .tit h3{flex:1;font-size:.92em}
.va .hpnum,.va .frec,.va .tic{background:transparent;color:var(--papel-tinta);padding:0;
  font-size:.6em;display:flex;align-items:center;gap:.2em}
/* La ventana cede espacio cuando la regla lo pide, que es lo que hacen
   los juegos de verdad. El alto va en calc sobre el ANCHO, no en
   porcentaje: un % —o un flex-basis en %— dentro de un hijo flex no
   resuelve contra un alto que viene de aspect-ratio, se cae a `auto` y la
   ventana tomaba el alto entero de la imagen. La carta mide 1,397 anchos
   de alto, así que 42 % del alto son 0,587 anchos. */
.va .ventana{position:relative;height:calc(var(--w)*.587);flex:none;
  border-radius:.28em;overflow:hidden;
  border:.12em solid var(--tipo);background:#0d1417}
.va.largo .ventana{height:calc(var(--w)*.405)}
.va.medio .ventana{height:calc(var(--w)*.503)}
.va .ventana img{width:100%;height:100%;object-fit:cover;display:block}
.va .cuerpo{flex:1 1 0;display:flex;flex-direction:column;gap:.26em;padding:.1em .1em 0;
  min-height:0;overflow:hidden}
.va .cuerpo .pie{margin-top:auto}

/* ── B · DOS TERCIOS ─────────────────────────────────────────────── */
.vb .zona-art{position:relative;height:calc(var(--w)*.894);flex:none;background:#0d1417}
.vb .zona-art.alto{height:calc(var(--w)*1.006)}
.vb .zona-art.bajo{height:calc(var(--w)*.727)}
.vb .zona-art img{width:100%;height:100%;object-fit:cover;display:block}
/* el arte no termina en un corte: se disuelve en el panel */
.vb .disuelve{position:absolute;inset:auto 0 0;height:22%;
  background:linear-gradient(to top,var(--papel),rgba(253,254,254,0))}
.vb .flot{position:absolute;top:.42em;left:.46em;right:.46em}
.vb .hpflot{position:absolute;top:.42em;right:.5em;display:flex;gap:.08em;
  filter:drop-shadow(0 1px 3px rgba(0,0,0,.6))}
.vb .coste.flot{position:absolute;top:2em;right:.46em}
.vb .panel{flex:1 1 0;background:var(--papel);padding:.1em .58em .5em;
  display:flex;flex-direction:column;gap:.22em;min-height:0;overflow:hidden}
.vb .panel h3{font-size:.92em;margin-bottom:.06em}
.vb .panel .pie{margin-top:auto}

/* ── C · SANGRE ──────────────────────────────────────────────────── */
.vc{background:#0d1417}
.vc .fondo{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;display:block}
.vc .velo-sup{position:absolute;inset:0 0 auto;height:40%;
  background:linear-gradient(to bottom,rgba(6,14,18,.82),rgba(6,14,18,.4) 46%,transparent)}
.vc .velo-inf{position:absolute;inset:auto 0 0;height:26%;
  background:linear-gradient(to top,rgba(6,14,18,.72),transparent)}
.vc header{position:absolute;inset:0 0 auto;padding:.56em .62em 0;z-index:2;color:#fff}
.vc header h3{margin-top:.24em;text-shadow:0 1px 5px rgba(0,0,0,.75)}
.vc .flota{position:absolute;inset:auto .46em .46em;z-index:2;
  background:rgba(253,254,254,.94);backdrop-filter:blur(4px);-webkit-backdrop-filter:blur(4px);
  border:1px solid rgba(20,40,48,.18);border-radius:.46em;padding:.44em .52em;
  box-shadow:0 3px 12px rgba(0,0,0,.4);display:flex;flex-direction:column;gap:.2em}
.vc .hpfila{display:flex;gap:.08em;margin-bottom:.1em}
.vc .banda{position:absolute;inset:auto 0 0;z-index:2;padding:.6em .74em .68em}

/* ══ presentación ═══════════════════════════════════════════════════ */
.mazo{display:flex;gap:16px;flex-wrap:wrap;margin:20px 0 0}
.op{margin-top:46px;padding:24px;border-radius:14px;background:var(--panel-2);
  border:1px solid var(--linea)}
.op > h3{font-family:Petrona,Georgia,serif;font-size:24px;margin:0 0 4px;
  display:flex;align-items:baseline;gap:.4em}
.op > h3 .letra{font-family:"IBM Plex Mono",ui-monospace,monospace;font-size:13px;
  letter-spacing:.14em;color:var(--acento);font-weight:700}
.op .resumen{color:var(--tinta-2);margin:0 0 4px}
.balance{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));
  gap:12px;margin-top:20px}
.balance div{background:var(--panel);border:1px solid var(--linea);border-radius:9px;padding:12px 14px}
.balance h5{font-family:"IBM Plex Mono",ui-monospace,monospace;font-size:10.5px;
  letter-spacing:.12em;text-transform:uppercase;margin:0 0 6px}
.balance .si h5{color:var(--ok)} .balance .no h5{color:var(--alerta)}
.balance ul{margin:0;padding-left:16px;font-size:14.5px}
.balance li{margin-bottom:5px}
.mini{display:flex;gap:11px;flex-wrap:wrap;align-items:flex-start;margin-top:14px}
.mini .cta{--w:132px}
/* En la cama la carta NO lleva reglas ni frase: se toca y se abre grande.
   El panel se reduce a lo que hay que ver de un vistazo, y el arte se
   queda con lo que sobra. Esto no es un recorte de emergencia: es la
   maquetación de la carta chica. */
.mini .regla,.mini .frase,.mini .habtit,.mini .pie{display:none}
/* Y sin el nombre del tipo: a 132 px las fichas de color YA dicen de qué
   tipo es, y el emoji que lo acompañaba no baja de un tamaño mínimo —no
   encogía con la carta y era lo que hacía desbordar la fila—. Es lo mismo
   que hace Pokémon: en el coste del ataque no hay palabras, solo fichas. */
.mini .rnom{display:none}
/* en C el panel flotante se queda vacío si su única carga era la regla:
   se esconde, salvo en el paciente, que sí lleva vidas y requerimientos */
.mini .cta.vc .flota{display:none}
.mini .cta.vc .flota:has(.hpfila){display:flex}
.mini .cta.vc .banda{display:none}
.mini .req{gap:.42em}
.mini .fi{width:.9em;height:.9em}
/* El peor caso es un paciente con las CUATRO filas de requerimiento —y
   cuatro es el techo, porque hay cuatro tipos de recurso—. El arte de la
   carta chica se dimensiona para que ese caso quepa: si cabe ACV en
   Ventana, caben todos. */
.mini .cta.va .ventana{height:calc(var(--w)*.78)}
.mini .cta.vb .zona-art{height:calc(var(--w)*.94)}
/* En la carta chica solo el paciente necesita panel —lleva los
   requerimientos—. Recurso, protocolo y avatar solo muestran el nombre,
   así que el arte se queda con casi todo. */
.mini .cta.vb .zona-art.bajo,
.mini .cta.vb .zona-art.med,
.mini .cta.vb .zona-art.alto{height:calc(var(--w)*1.18)}
.rotulo{font-family:"IBM Plex Mono",ui-monospace,monospace;font-size:10.5px;
  letter-spacing:.1em;text-transform:uppercase;color:var(--tinta-2);margin:18px 0 0}
.tabla-env{overflow-x:auto;margin:20px 0;border:1px solid var(--linea);border-radius:10px;
  background:var(--panel)}
table{border-collapse:collapse;width:100%;min-width:520px;font-size:14.5px}
th,td{padding:9px 14px;text-align:left;border-bottom:1px solid var(--linea-2);vertical-align:top}
th{font-family:"IBM Plex Mono",ui-monospace,monospace;font-size:10.5px;letter-spacing:.1em;
  text-transform:uppercase;color:var(--tinta-2);font-weight:600}
tr:last-child td{border-bottom:0}
td.si{color:var(--ok);font-weight:700} td.no{color:var(--alerta);font-weight:700}
"""
