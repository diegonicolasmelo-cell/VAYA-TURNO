# -*- coding: utf-8 -*-
"""Las tres maquetaciones. Mismo contenido, tres formas de repartirlo."""
from datos import *


def holgura(txt):
    """Cuánto texto trae la carta decide cuánto arte cabe."""
    n = len(txt or "")
    return " largo" if n > 150 else (" medio" if n > 80 else "")


def _chips_pac(p):
    ic, nom, col = SIS[p["sistema"]]
    return (f'<i class="chip" style="background:{GCOL[p["gravedad"]]}">G·{e(p["gravedad"])}</i>'
            f'<i class="chip" style="background:{col}">{ic} {nom}</i>')


# ══ A · VENTANA — el marco clásico, arte en ventana ═════════════════════
def a_pac(cid, foco):
    p = PAC[cid]; col = SIS[p["sistema"]][2]
    return f'''<article class="cta va medio" style="--tipo:{col}">
 <div class="tit"><h3>{e(p["nombre"])}</h3><span class="hpnum">{e(p["vida"])} <i class="hp"></i></span></div>
 <div class="ventana"><img src="{uri(cid)}" alt="" style="object-position:{foco}"></div>
 <div class="cuerpo">
  <div class="chips">{_chips_pac(p)}</div>
  <div class="reqs">{reqs(p)}</div>
  <div class="pie"><span>alta <b>+{e(p["puntos_alta"])}</b></span><span>fallece <b>{e(p["puntos_fallece"])}</b></span></div>
 </div></article>'''

def a_rec(cid, foco):
    r = REC[cid]; col = TCOL[r["tipo"]]
    return f'''<article class="cta va" style="--tipo:{col}">
 <div class="tit"><h3>{e(r["nombre"])}</h3><span class="tic">{TIC[r["tipo"]]}</span></div>
 <div class="ventana"><img src="{uri(cid)}" alt="" style="object-position:{foco}"></div>
 <div class="cuerpo">
  <div class="chips"><i class="chip" style="background:{col}">{e(r["tipo"].title())}</i></div>
  <p class="frase">{e(r["frase"])}</p>
 </div></article>'''

def a_acc(cid, foco):
    a = ACC[cid]; col = ACOL.get(a["tipo"], "#4a8a96")
    return f'''<article class="cta va{holgura(a["texto"])}" style="--tipo:{col}">
 <div class="tit"><h3>{e(a["nombre"])}</h3><span class="coste">{e(a["coste"])}</span></div>
 <div class="ventana"><img src="{uri(cid)}" alt="" style="object-position:{foco}"></div>
 <div class="cuerpo">
  <div class="chips"><i class="chip" style="background:{col}">{e(a["tipo"])}</i></div>
  <p class="regla">{e(a["texto"])}</p>
 </div></article>'''

def a_ava(cid, foco):
    c = PER[cid]; tit, hab = parte(c["habilidad"])
    return f'''<article class="cta va{holgura(c["habilidad"])}" style="--tipo:#0d6e78">
 <div class="tit"><h3>{e(c["nombre"])}</h3><span class="frec">{e(c["frecuencia"])}</span></div>
 <div class="ventana"><img src="{uri(cid)}" alt="" style="object-position:{foco}"></div>
 <div class="cuerpo">
  {f'<p class="habtit">{e(tit)}</p>' if tit else ''}
  <p class="regla">{e(hab)}</p>
 </div></article>'''


# ══ B · DOS TERCIOS — arte a sangre arriba, panel sólido abajo ══════════
def b_pac(cid, foco):
    p = PAC[cid]; col = SIS[p["sistema"]][2]
    return f'''<article class="cta vb" style="--tipo:{col}">
 <div class="zona-art"><img src="{uri(cid)}" alt="" style="object-position:{foco}">
  <div class="disuelve"></div><div class="chips flot">{_chips_pac(p)}</div>
  <div class="hpflot">{vidas(p)}</div></div>
 <div class="panel">
  <h3>{e(p["nombre"])}</h3>
  <div class="reqs">{reqs(p)}</div>
  <div class="pie"><span>alta <b>+{e(p["puntos_alta"])}</b></span><span>fallece <b>{e(p["puntos_fallece"])}</b></span></div>
 </div></article>'''

def b_rec(cid, foco):
    r = REC[cid]; col = TCOL[r["tipo"]]
    return f'''<article class="cta vb" style="--tipo:{col}">
 <div class="zona-art alto"><img src="{uri(cid)}" alt="" style="object-position:{foco}">
  <div class="disuelve"></div>
  <div class="chips flot"><i class="chip" style="background:{col}">{TIC[r["tipo"]]} {e(r["tipo"].title())}</i></div></div>
 <div class="panel"><h3>{e(r["nombre"])}</h3>
  <p class="frase">{e(r["frase"])}</p></div></article>'''

def b_acc(cid, foco):
    a = ACC[cid]; col = ACOL.get(a["tipo"], "#4a8a96")
    return f'''<article class="cta vb" style="--tipo:{col}">
 <div class="zona-art med"><img src="{uri(cid)}" alt="" style="object-position:{foco}">
  <div class="disuelve"></div>
  <div class="chips flot"><i class="chip" style="background:{col}">{e(a["tipo"])}</i></div>
  <span class="coste flot">{e(a["coste"])}</span></div>
 <div class="panel"><h3>{e(a["nombre"])}</h3>
  <p class="regla">{e(a["texto"])}</p></div></article>'''

def b_ava(cid, foco):
    c = PER[cid]; tit, hab = parte(c["habilidad"])
    return f'''<article class="cta vb" style="--tipo:#0d6e78">
 <div class="zona-art bajo"><img src="{uri(cid)}" alt="" style="object-position:{foco}">
  <div class="disuelve"></div>
  <div class="chips flot"><i class="chip" style="background:#0d6e78">avatar</i>
   <i class="chip hueco">{e(c["frecuencia"])}</i></div></div>
 <div class="panel"><h3>{e(c["nombre"])}</h3>
  {f'<p class="habtit">{e(tit)}</p>' if tit else ''}
  <p class="regla">{e(hab)}</p></div></article>'''


# ══ C · SANGRE — arte en toda la carta, panel flotante ══════════════════
def c_pac(cid, foco):
    p = PAC[cid]; col = SIS[p["sistema"]][2]
    return f'''<article class="cta vc" style="--tipo:{col}">
 <img class="fondo" src="{uri(cid)}" alt="" style="object-position:{foco}">
 <div class="velo-sup"></div>
 <header><div class="chips">{_chips_pac(p)}</div><h3>{e(p["nombre"])}</h3></header>
 <div class="flota">
  <div class="hpfila">{vidas(p)}</div>
  <div class="reqs">{reqs(p)}</div>
  <div class="pie"><span>alta <b>+{e(p["puntos_alta"])}</b></span><span>fallece <b>{e(p["puntos_fallece"])}</b></span></div>
 </div></article>'''

def c_rec(cid, foco):
    r = REC[cid]; col = TCOL[r["tipo"]]
    return f'''<article class="cta vc" style="--tipo:{col}">
 <img class="fondo" src="{uri(cid)}" alt="" style="object-position:{foco}">
 <div class="velo-sup"></div><div class="velo-inf"></div>
 <header><div class="chips"><i class="chip" style="background:{col}">{TIC[r["tipo"]]} {e(r["tipo"].title())}</i></div>
  <h3>{e(r["nombre"])}</h3></header>
 <footer class="banda"><p class="frase clara">{e(r["frase"])}</p></footer></article>'''

def c_acc(cid, foco):
    a = ACC[cid]; col = ACOL.get(a["tipo"], "#4a8a96")
    return f'''<article class="cta vc" style="--tipo:{col}">
 <img class="fondo" src="{uri(cid)}" alt="" style="object-position:{foco}">
 <div class="velo-sup"></div>
 <header><div class="chips"><i class="chip" style="background:{col}">{e(a["tipo"])}</i>
  <span class="coste">{e(a["coste"])}</span></div><h3>{e(a["nombre"])}</h3></header>
 <div class="flota"><p class="regla">{e(a["texto"])}</p></div></article>'''

def c_ava(cid, foco):
    c = PER[cid]; tit, hab = parte(c["habilidad"])
    return f'''<article class="cta vc" style="--tipo:#0d6e78">
 <img class="fondo" src="{uri(cid)}" alt="" style="object-position:{foco}">
 <div class="velo-sup"></div>
 <header><div class="chips"><i class="chip" style="background:#0d6e78">avatar</i>
  <i class="chip hueco">{e(c["frecuencia"])}</i></div><h3>{e(c["nombre"])}</h3></header>
 <div class="flota">{f'<p class="habtit">{e(tit)}</p>' if tit else ''}
  <p class="regla">{e(hab)}</p></div></article>'''


JUEGOS = {
 "a": (a_pac, a_rec, a_acc, a_ava),
 "b": (b_pac, b_rec, b_acc, b_ava),
 "c": (c_pac, c_rec, c_acc, c_ava),
}

def cuarteto(op):
    p, r, a, v = JUEGOS[op]
    return (p("P11", "center 24%") + r("R50", "center 38%") +
            a("A19", "center 26%") + v("C01", "center 20%"))
