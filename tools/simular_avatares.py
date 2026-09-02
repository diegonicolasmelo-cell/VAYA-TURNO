#!/usr/bin/env python3
"""Simulador de AVATARES de ¡VAYA TURNO! (rama v0.30)

Copia de simular_v030.py con las 22 habilidades de avatar implementadas.
Se usa para el tier list de DISENO §4p: se asigna AVATARES = {0: "C13"} y
se mide ese asiento contra uno sin avatar, con la misma semilla.
No reemplaza a simular_v030.py: aquel es el suelo oficial del balance.

Salvedades del modelo: La Jefa de Unidad cuenta escaneos y no bloqueos en
USOS (su Δ sí es válido); La de la Buena Muñeca depende de la heurística de
"carta inútil" y probablemente esté subestimada.

Este archivo ya incluye el REBALANCE de DISENO §4q (agosto 2026): C01, C02,
C03, C06, C07, C11, C13, C18 y C19 llevan sus habilidades retocadas y los
textos de cartas/personajes.csv reflejan estas versiones.

ORIGINAL:


La v0.30 es el rediseño del autor (agosto 2026): sabotaje con recursos ⚠️,
Pizarra de Turno, admisión obligatoria y complicación unificada "donde se
ubica". La v0.21 estable se mide con tools/simular.py; este archivo mide el
suelo de la variante. Reglas completas en docs/REGLAMENTO-v030.md.

Qué modela:
- Admisión OBLIGATORIA (revela 2, elige 1). Se parte con 2 pacientes y la
  ronda 1 se juega así: la tercera cama se admite recién en la ronda 2.
- 3 colocaciones por turno gastables en un menú: tratar / sabotear /
  des-escalar / cerrar Sumario (1 colocación + 2 cartas).
- Toda ⚠️ quita 1 ❤️ al paciente DONDE SE UBICA, propio o rival, al colocarla.
  Las protecciones 🛡️ PREVIENE siguen funcionando (prospectivas, por nombre).
- Sabotaje: colocar una ⚠️ sobre un paciente rival. Si el tipo le sirve,
  cuenta para su receta (por eso la IA tira tipos que NO pide = basura).
  La basura bloquea el ✅ hasta que se retire (des-escalada, 1 colocación).
  COLOCAR NUNCA MATA: ninguna ⚠️ quita el último ❤️, ni la propia (piso 1).
  Máx. 1 sabotaje por cama y ronda.
- Sumario boca arriba en zona, pero MUERDE: cada uno abierto reduce tu
  límite de mano en 1. Cerrarlo cuesta 2 cartas (sin colocación).
  La Auditoría del Ministerio quedó como variante opcional (ver flag).
- Cama vacía solo penaliza al final (−1 c/u); con admisión obligatoria solo
  pasa si se agota el Mazo de Pacientes.
- El Cirujano de Turno cuenta como 2 🧑‍⚕️. El Turno Veinticuatro además
  descarta 1 carta de la mano del dueño de la unidad.
- NO modela: la Pizarra (Acciones), el Becado (busca Protocolo), el Pabellón
  (mover recurso). Igual que siempre: esto es el suelo del balance.
- v0.31 eliminó la fase de El Pasillo (el turno son 3 fases y la Pizarra se
  compra dentro del Pase de Visita). Este archivo no cambia ni una cifra:
  nunca modeló la compra de Protocolos, así que el suelo medido es el mismo.

    python3 tools/simular_v030.py --partidas 4000 --jugadores 2
"""

import argparse
import csv
import os
import random
from collections import Counter

TIPOS = ("IMAGEN", "FARMACOS", "PERSONAL", "PROCEDIMIENTOS")
COL = {"IMAGEN": "img", "FARMACOS": "far", "PERSONAL": "per", "PROCEDIMIENTOS": "proc"}
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ── Flags de la variante (para medir apagando piezas) ──
ATAQUES = True           # False = nadie sabotea (cota superior de suavidad)
BASURA_BLOQUEA = "alta"  # qué bloquea la basura rival: "estable" (el ✅),
                         # "alta" (estabiliza igual, pero no se va hasta limpiar)
AUDITORIA = False        # VARIANTE opcional: −3 al que junte más Sumarios.
                         # Apagada por defecto: medido, le pega al que YA iba
                         # perdiendo el 86-90% de las veces y ensancha la
                         # brecha de 5,4 a 7,1. Es sal en la herida.
PISO_RIVAL = 1
ALTA_YA = 0              # usos de "Alta Anticipada" del jugador 0 (medición)
ALTA_YA_DESDE = 1        # política: no gastarla antes de esta ronda
ALTA_YA_HASTA = 99       # regla: la carta no sirve después de esta ronda
ALTA_YA_ROBA = 0         # premio: roba N cartas al usarla
ALTA_YA_PENA = 0         # castigo: el alta apurada vale N puntos menos
PROTOCOLOS = False       # ¿se modela la Pizarra? False = suelo histórico
AVATARES = {}            # asiento → id de avatar ("C13"), o vacío = sin avatar
USOS = None              # Counter de veces que cada habilidad SIRVIÓ
PROT_ASIENTOS = None     # None = todos; {0} = solo el asiento A (asimétrico)
PROT_SOBRA = 0           # cuántas cartas de más exige la IA para comprar
STATS = None             # dict de jugabilidad (lo llena el arnés)


def cargar():
    def leer(carpeta, n):
        with open(os.path.join(RAIZ, carpeta, n), encoding="utf-8") as f:
            return list(csv.DictReader(f))

    pacientes = []
    for p in leer("cartas", "pacientes.csv"):
        ficha = {
            "nombre": p["nombre"], "gravedad": p["gravedad"],
            "vida": int(p["vida"]), "sistema": p["sistema"],
            "pide": {t: int(p[COL[t]]) for t in TIPOS},
            "alta": int(p["puntos_alta"]), "fallece": int(p["puntos_fallece"]),
        }
        ficha["pide_total"] = sum(ficha["pide"].values())
        for _ in range(int(p.get("copias") or 1)):
            pacientes.append(ficha)

    guardia = []
    for r in leer(os.path.join("cartas", "v030"), "recursos.csv"):
        comp = {"nombre": r.get("comp_nombre", ""),
                "vida": int(r.get("comp_vida") or 0)}
        for _ in range(int(r["copias"])):
            guardia.append({"clase": "recurso", "tipo": r["tipo"],
                            "nombre": r["nombre"],
                            "previene": r.get("previene", ""),
                            "sistema": r["sistema"],
                            "comodin": r["comodin"] == "si",
                            "restriccion": r["restriccion"],
                            "doble_en": (r.get("doble_en") or "").strip(),
                            "soporte": r.get("soporte", "") == "si",
                            "turno24": r.get("comp_nombre") == "El Turno Veinticuatro",
                            "warn": r["complicacion"] == "si",
                            "comp": comp if r["complicacion"] == "si" else None})
    return pacientes, guardia


class Cama:
    def __init__(self, ficha):
        self.f = ficha
        self.vida = ficha["vida"]
        self.pide = dict(ficha["pide"])
        self.tiene = Counter()
        self.estable = False
        self.estable_desde = None
        self.protege = set()
        self.basura = 0            # recursos rivales que no pide (v0.30)
        self.atacada = False       # máx. 1 sabotaje por ronda
        self.puestos = []          # [(carta, tipo, aporte)] — para poder retirar
        self.escudo = False        # A19: cama cerrada al saqueo
        self.extra = 0             # A08: −1 ❤️ extra en el próximo Fin de Guardia

    def falta(self):
        return {t: max(0, self.pide[t] - self.tiene[t]) for t in TIPOS}

    def faltan_total(self):
        return sum(self.falta().values())

    def revisar(self, ronda):
        completo = self.faltan_total() == 0
        if BASURA_BLOQUEA == "estable" and self.basura > 0:
            completo = False       # la basura clínica bloquea el ✅
        if completo and not self.estable:
            self.estable, self.estable_desde = True, ronda
        elif not completo and self.estable:
            self.estable, self.estable_desde = False, None


class Jugador:
    def __init__(self, camas):
        self.camas = [None] * camas
        self.mano = []
        self.altas = []
        self.muertos = []
        self.sumarios = 0

    def defendible(self):
        return bool(self.muertos) and all(
            c["gravedad"] in ("III", "ROJO") for c in self.muertos)

    def puntos(self):
        p = sum(c["alta"] for c in self.altas) + sum(c["fallece"] for c in self.muertos)
        p -= getattr(self, "pena", 0)
        p -= getattr(self, "vacias", 0)
        p -= getattr(self, "auditoria", 0)
        if getattr(self, "sin_bonus", False):
            return p                      # C05 La Gestora renunció al cierre
        if not self.muertos:
            p += 3
        elif self.defendible():
            p += 1
        return p


def elegir_objetivos(camas):
    vivos = [c for c in camas if c and not c.estable]
    puntuados = []
    for c in vivos:
        faltan = c.faltan_total()
        if faltan == 0:
            continue
        alcanzable = faltan <= c.vida * 2.1
        valor = (c.f["alta"] - c.f["fallece"]) / faltan
        puntuados.append((alcanzable, valor, c))
    puntuados.sort(key=lambda x: (not x[0], -x[1]))
    return [c for _, _, c in puntuados]


def elegir_carta(mano, cama):
    falta = cama.falta()
    if sum(falta.values()) == 0:
        return None, 0, None

    def jugable(c):
        if c["clase"] != "recurso":
            return False
        if c.get("restriccion") == "PERSONAL" and cama.tiene["PERSONAL"] == 0:
            return False
        return True

    def orden(cands):
        # a igual jugada, primero la copia limpia; la ⚠️ es el plan B
        return sorted(cands, key=lambda x: bool(x[0].get("warn")))

    cands = [(c, 2, c["tipo"]) for c in mano
             if jugable(c) and c.get("sistema") and c["sistema"] == cama.f["sistema"]
             and falta.get(c["tipo"], 0) > 0]
    if cands:
        return orden(cands)[0]
    cands = [(c, 2, c["doble_en"]) for c in mano
             if jugable(c) and c.get("doble_en")
             and falta.get(c["doble_en"], 0) > 0]
    if cands:
        return orden(cands)[0]
    cands = [(c, 1, c["tipo"]) for c in mano
             if jugable(c) and not c.get("comodin") and c["tipo"] in TIPOS
             and falta.get(c["tipo"], 0) > 0]
    if cands:
        return orden(cands)[0]
    for c in mano:
        if c.get("comodin") and jugable(c):
            t = max(falta, key=lambda k: falta[k])
            if falta[t] > 0:
                return c, 1, t
    return None, 0, None


def contar_warn(duenio, ctx=None):
    duenio.warns_vistas = getattr(duenio, "warns_vistas", 0) + 1
    if getattr(duenio, "avatar", None) == "C12" and duenio.warns_vistas % 3 == 0:
        if ctx and ctx.get("mazo_a"):
            duenio.protocolos.append(ctx["mazo_a"].pop()["id"])
            marcar(duenio, "C12")

def resolver_warn(duenio, carta, cama):
    """La complicación v0.30: −1 ❤️ donde se ubica, con 🛡️ y Turno 24.
    Piso universal (balance final): COLOCAR NUNCA MATA — ni al propio.
    Medido: cero costo en juego experto, +6pp de salvamento al novato."""
    comp = carta.get("comp")
    if not comp:
        return
    if comp["nombre"] and comp["nombre"] in cama.protege:
        return                     # prevención prospectiva
    cama.vida = max(1, cama.vida + comp["vida"])
    if carta.get("turno24") and duenio.mano:
        duenio.mano.sort(key=lambda c: (c.get("comodin", False),
                                        bool(c.get("sistema"))))
        duenio.mano.pop(0)


def elegir_sabotaje(j, rivales):
    """Busca (carta, cama_rival, dueño) para un sabotaje que valga la pena:
    una ⚠️ de un tipo que la víctima NO pide (basura), sobre la cama rival
    más cercana a completarse. Nunca regala recursos útiles."""
    warns = [c for c in j.mano if c.get("warn")]
    if not warns:
        return None
    candidatas = []
    for r in rivales:
        for cama in r.camas:
            if cama is None or cama.atacada:
                continue
            for c in warns:
                falta = cama.falta()
                util_para_el = c.get("comodin") or falta.get(c["tipo"], 0) > 0 \
                    or (c.get("sistema") and c["sistema"] == cama.f["sistema"])
                if util_para_el:
                    continue       # sería un regalo
                # prioridad: bloquear al que está por cerrar
                urgencia = -cama.faltan_total() + (3 if cama.estable else 0)
                candidatas.append((urgencia, cama.vida, c, cama, r))
    if not candidatas:
        return None
    candidatas.sort(key=lambda x: (-x[0], -x[1]))
    urgencia, _, c, cama, r = candidatas[0]
    # solo atacar si de verdad estorba: cama a ≤2 de cerrar, o ya estable
    if urgencia < -2:
        return None
    return c, cama, r


# ══════════════════════════════════════════════════════════════════════
# LA PIZARRA (Protocolos / Acciones) — modelada para poder medirla.
# El suelo histórico de §4k–4l se midió SIN esto: PROTOCOLOS=False lo
# reproduce carta por carta. Con True, ambos jugadores compran y juegan.
# ══════════════════════════════════════════════════════════════════════

def av(j, cual):
    return getattr(j, "avatar", None) == cual

def marcar(j, cual):
    if USOS is not None and getattr(j, "avatar", None) == cual:
        USOS[cual] += 1

def cargar_acciones():
    with open(os.path.join(RAIZ, "cartas", "v030", "acciones.csv"),
              encoding="utf-8") as f:
        filas = list(csv.DictReader(f))
    mazo = []
    for a in filas:
        for _ in range(int(a["copias"])):
            mazo.append({"id": a["id"], "nombre": a["nombre"],
                         "tipo": a["tipo"], "coste": int(a["coste"])})
    return mazo


def quitar_puesto(cama, k):
    """Retira el k-ésimo recurso colocado y descuadra la receta como toca."""
    carta, tipo, ap = cama.puestos.pop(k)
    if tipo in TIPOS:
        cama.tiene[tipo] = max(0, cama.tiene[tipo] - ap)
    if carta.get("previene"):
        cama.protege.discard(carta["previene"])
    return carta


def poner_puesto(cama, carta, ronda):
    tipo = carta["tipo"]
    if carta.get("comodin"):
        f = cama.falta()
        tipo = max(f, key=lambda k: f[k])
    ap = 2 if (carta.get("sistema") and carta["sistema"] == cama.f["sistema"]) else 1
    if tipo in TIPOS:
        cama.tiene[tipo] += ap
    cama.puestos.append((carta, tipo, ap))
    if carta.get("previene"):
        cama.protege.add(carta["previene"])
    cama.revisar(ronda)


def _saqueables(rivales, filtro=None):
    out = []
    for r in rivales:
        for cama in r.camas:
            if cama is None or cama.escudo:
                continue
            for k, (c, t, a) in enumerate(cama.puestos):
                # C03 Doctor Amor y C22 La Jefa: su 🧑‍⚕️ no se toca
                if t == "PERSONAL" and getattr(r, "avatar", None) == "C22":
                    if filtro is None or filtro(c, t):
                        marcar(r, r.avatar)     # solo cuenta si iba a robarlo
                    continue
                if filtro is None or filtro(c, t):
                    out.append((r, cama, k))
    return out


def acciones_utiles(j, rivales, ronda, ctx):
    """Devuelve [(prioridad, id)] de las Acciones que HOY harían algo.
    La prioridad es la heurística de la IA: primero lo que más mueve
    la aguja, igual que hace con las colocaciones."""
    u = []
    saq_per = _saqueables(rivales, lambda c, t: t == "PERSONAL")
    saq_ip = _saqueables(rivales, lambda c, t: t in ("IMAGEN", "PROCEDIMIENTOS"))
    saq_any = _saqueables(rivales)
    # cuánto estorba: quitarle un recurso al que está por cerrar vale más
    def urgencia(lista):
        return max((3 - cam.faltan_total() for _, cam, _ in lista), default=-9)
    rival_cerca = [cam for r in rivales for cam in r.camas
                   if cam and not cam.escudo and not cam.estable]
    mios = [c for c in j.camas if c]
    mios_no_ok = [c for c in mios if not c.estable]

    if saq_per:  u.append((6 + urgencia(saq_per), "A01"))
    if saq_ip:   u.append((6 + urgencia(saq_ip), "A20"))
    if rival_cerca: u.append((7 + max(3 - c.faltan_total() for c in rival_cerca), "A21"))
    if saq_any:  u.append((5, "A02"))
    if rival_cerca: u.append((5, "A08"))
    if any(r.mano for r in rivales): u.append((3, "A09"))
    if rivales: u.append((4, "A17"))
    if rivales: u.append((5, "A18"))
    # apoyo
    if len(mios) > 1 and any(c.puestos for c in mios): u.append((4, "A03"))
    if ctx["descarte"] and mios_no_ok: u.append((6, "A04"))
    u.append((5, "A05"))
    if mios_no_ok: u.append((7, "A15"))
    if any(c.estable and c.estable_desde == ronda and c.basura == 0 for c in mios):
        u.append((6, "A22"))
    if any(not c.escudo and (c.estable or c.faltan_total() <= 1) for c in mios):
        u.append((6, "A19"))
    # respuesta / caos
    if ctx["ult_comp"] is not None: u.append((6, "A11"))
    if ctx["ult_comp"] is not None: u.append((6, "A16"))
    if any(len(r.muertos) >= 2 and any(r.camas) for r in rivales): u.append((4, "A13"))
    if rivales and len(j.mano) <= 2: u.append((3, "A10"))
    u.append((1, "A06"))
    u.append((2, "A14"))
    return u


ATAQUES_IDS = {"A01","A02","A08","A09","A17","A18","A20","A21","A13","A07"}

def ejecutar_accion(aid, j, rivales, ronda, ctx, rng):
    """Aplica el efecto. Devuelve True si hizo algo."""
    def descartar(c): ctx["descarte"].append(c)
    if aid in ATAQUES_IDS:
        for r in rivales:
            if getattr(r, "avatar", None) == "C10":
                cc = ctx["robar"]()
                if cc: r.mano.append(cc)
                marcar(r, "C10")

    if aid == "A01" or aid == "A20":
        f = (lambda c, t: t == "PERSONAL") if aid == "A01" \
            else (lambda c, t: t in ("IMAGEN", "PROCEDIMIENTOS"))
        cand = _saqueables(rivales, f)
        if not cand: return False
        cand.sort(key=lambda x: x[1].faltan_total())      # al que está por cerrar
        r, cama, k = cand[0]
        pieza = quitar_puesto(cama, k); cama.revisar(ronda)
        if aid == "A01": r.mano.append(pieza)   # se fue de vacaciones: VUELVE
        else: descartar(pieza)                   # A20: la muestra arruinada no vuelve
        return True

    if aid == "A21":
        cand = [c for r in rivales for c in r.camas
                if c and not c.escudo and not c.estable]
        if not cand: return False
        cand.sort(key=lambda c: c.faltan_total())
        cama = cand[0]
        cama.vida = max(1, cama.vida - 1)
        if cama.puestos:
            descartar(quitar_puesto(cama, len(cama.puestos) - 1)); cama.revisar(ronda)
        return True

    if aid == "A02":
        botin = []
        for r in rivales:
            cand = _saqueables([r])
            if not cand: continue
            cand.sort(key=lambda x: -x[1].faltan_total())
            _, cama, k = cand[0]
            botin.append(quitar_puesto(cama, k)); cama.revisar(ronda)
        if not botin: return False
        for c in botin:
            destino = next((x for x in elegir_objetivos(j.camas)), None)
            if destino: poner_puesto(destino, c, ronda)
            else: descartar(c)
        return True

    if aid == "A08":
        cand = [c for r in rivales for c in r.camas
                if c and not c.escudo and not c.estable]
        if not cand: return False
        min(cand, key=lambda c: c.vida).extra += 1
        return True

    if aid == "A09":
        r = max(rivales, key=lambda x: len(x.mano))
        if not r.mano: return False
        r.mano.sort(key=lambda c: (c.get("comodin", False), bool(c.get("sistema"))))
        descartar(r.mano.pop())            # le quita la mejor
        return True

    if aid == "A17":
        rng.choice(rivales).sin_far = True; return True
    if aid == "A18":
        rng.choice(rivales).recorte = 2; return True

    if aid == "A03":
        # mueve hasta 3 recursos a la cama más cerca de cerrar
        objetivos = elegir_objetivos(j.camas)
        if not objetivos: return False
        destino = objetivos[0]
        movidos = 0
        for cama in j.camas:
            if cama is None or cama is destino: continue
            for k in range(len(cama.puestos) - 1, -1, -1):
                if movidos >= 3: break
                _, t, _ = cama.puestos[k]
                if destino.falta().get(t, 0) > 0:
                    poner_puesto(destino, quitar_puesto(cama, k), ronda)
                    cama.revisar(ronda); movidos += 1
        return movidos > 0

    if aid == "A04":
        objetivos = elegir_objetivos(j.camas)
        if not objetivos or not ctx["descarte"]: return False
        cama = objetivos[0]
        for i, c in enumerate(ctx["descarte"]):
            if c["clase"] == "recurso" and cama.falta().get(c["tipo"], 0) > 0:
                j.mano.append(ctx["descarte"].pop(i)); return True   # a la MANO
        return False

    if aid == "A05":
        for _ in range(3):
            c = ctx["robar"]()
            if c: j.mano.append(c)
        j.robo_mod = getattr(j, "robo_mod", 0) - 2
        return True

    if aid == "A15":
        objetivos = elegir_objetivos(j.camas)
        if not objetivos or not ctx["mazo"]: return False
        cama = objetivos[0]
        f = cama.falta()
        mejor, mi = None, None
        for i, c in enumerate(ctx["mazo"]):
            if c.get("warn"): continue
            v = (2 if (c.get("sistema") and c["sistema"] == cama.f["sistema"]) else 1) \
                if f.get(c["tipo"], 0) > 0 else 0
            if v and (mejor is None or v > mejor):
                mejor, mi = v, i
                if v == 2: break
        if mi is None: return False
        j.mano.append(ctx["mazo"].pop(mi)); rng.shuffle(ctx["mazo"])
        return True

    if aid == "A22":
        cand = [c for c in j.camas
                if c and c.estable and c.estable_desde == ronda and c.basura == 0]
        if not cand: return False
        c = max(cand, key=lambda x: x.f["alta"])
        if c.f["alta"] - 2 <= 0: return False          # no vale la pena
        j.altas.append(c.f); j.pena = getattr(j, "pena", 0) + 2
        j.camas[j.camas.index(c)] = None
        return True

    if aid == "A19":
        cand = [c for c in j.camas
                if c and not c.escudo and (c.estable or c.faltan_total() <= 1)]
        if not cand: return False
        cand[0].escudo = True; return True

    if aid in ("A11", "A16"):
        t = ctx["ult_comp"]
        if t is None or t not in [c for c in j.camas if c]: return False
        t.vida = min(t.f["vida"], t.vida + 1)
        ctx["ult_comp"] = None
        return True

    if aid == "A13":
        vics = [r for r in rivales if len(r.muertos) >= 2 and any(r.camas)]
        if not vics: return False
        if rng.random() < 0.25:                        # dos caras
            r = vics[0]
            cam = max((c for c in r.camas if c), key=lambda c: c.f["alta"])
            r.muertos.append(cam.f); r.camas[r.camas.index(cam)] = None
            r.sumarios += 1
        else:
            for c in j.mano: descartar(c)
            j.mano.clear()
        return True

    if aid == "A10":
        r = max(rivales, key=lambda x: len(x.mano))
        j.mano, r.mano = r.mano, j.mano
        return True

    if aid == "A06":
        ctx["bloqueo"] = ronda + 1; return True

    if aid == "A14":
        if ctx["mazo"] and ctx["mazo"][-1].get("warn"):
            ctx["mazo"].insert(0, ctx["mazo"].pop())   # la ⚠️ al fondo
            return True
        return False

    return False


def turno_pizarra(j, rivales, ronda, ctx, rng):
    # C21 El Precavido: saca una RESPUESTA 🛡️ del mazo, gratis
    if getattr(j, "avatar", None) == "C21" and not j.hab_p:
        for k, a in enumerate(ctx["mazo_a"]):
            if a["id"] in ("A11", "A16"):
                ctx["mazo_a"].pop(k)
                j.protocolos.append(a["id"])
                j.hab_p = True; marcar(j, "C21"); break
    """La IA usa la Pizarra: máx. 1 compra y 1 Acción jugada por turno."""
    # 1. JUGAR lo que ya tiene guardado
    if ctx["bloqueo"] != ronda:
        for prio, aid in sorted(acciones_utiles(j, rivales, ronda, ctx), reverse=True):
            if aid not in j.protocolos: continue
            if ejecutar_accion(aid, j, rivales, ronda, ctx, rng):
                j.protocolos.remove(aid)
                if STATS is not None:
                    STATS["acc_jugadas"] += 1; STATS["acc_por_id"][aid] += 1
                break
    # 2. COMPRAR: solo con cartas que de verdad sobran
    sobra = len(j.mano) - sum(1 for c in j.camas if c and not c.estable) * 2 - PROT_SOBRA
    if sobra <= 0 or not ctx["pizarra"]: return
    quiere = {aid for _, aid in acciones_utiles(j, rivales, ronda, ctx)}
    opciones = [(i, a) for i, a in enumerate(ctx["pizarra"])
                if a["coste"] <= min(sobra, len(j.mano)) and a["id"] in quiere]
    if not opciones: return
    prio = {aid: p for p, aid in acciones_utiles(j, rivales, ronda, ctx)}
    i, a = max(opciones, key=lambda x: prio.get(x[1]["id"], 0) - x[1]["coste"])
    j.mano.sort(key=lambda c: (c.get("comodin", False), bool(c.get("sistema"))))
    pagar = a["coste"] - (1 if getattr(j, "avatar", None) == "C09" else 0)
    if getattr(j, "avatar", None) == "C09": marcar(j, "C09")
    for _ in range(max(0, pagar)):
        if j.mano: ctx["descarte"].append(j.mano.pop(0))
    ctx["pizarra"].pop(i)
    if ctx["mazo_a"]: ctx["pizarra"].append(ctx["mazo_a"].pop())
    j.protocolos.append(a["id"])
    if STATS is not None: STATS["acc_compradas"] += 1


def jugar(pacientes, guardia, n_jug, camas_c, rondas, rng, robo=4, mano_max=6):
    mazo_p = pacientes[:]
    rng.shuffle(mazo_p)
    mazo_g = guardia[:]
    rng.shuffle(mazo_g)
    descarte = []

    def robar():
        if not mazo_g:
            if not descarte:
                return None
            mazo_g.extend(descarte)
            descarte.clear()
            rng.shuffle(mazo_g)
            if STATS is not None: STATS["rebarajes"] += 1
        return mazo_g.pop()

    jugadores = [Jugador(camas_c) for _ in range(n_jug)]
    for idx, j in enumerate(jugadores):
        j.alta_ya = ALTA_YA if idx == 0 else 0
        j.protocolos = []
        j.sin_far = False
        j.robo_mod = 0
        j.avatar = AVATARES.get(idx)
        j.hab_p = False          # la 1×PARTIDA ya se gastó
        j.diostor_r = False      # C01: ya desvió una complicación esta ronda
        j.guardado = None        # C11: recurso en reserva
        j.warns_vistas = 0       # C12: contador de ⚠️
        j.sin_bonus = False      # C05: pierde los logros de cierre
        # C17 El Multiuso: empieza con un comodín extra en la mano
        if j.avatar == "C17":
            com = next((c for c in mazo_g if c.get("comodin")), None)
            if com:
                mazo_g.remove(com); j.mano.append(com); marcar(j, "C17")

    # la Pizarra: 3 Protocolos boca arriba, se reponen al comprarse
    mazo_a = cargar_acciones() if PROTOCOLOS else []
    rng.shuffle(mazo_a)
    ctx = {"pizarra": [mazo_a.pop() for _ in range(min(3, len(mazo_a)))],
           "mazo_a": mazo_a, "mazo": mazo_g, "descarte": descarte,
           "robar": robar, "bloqueo": 0, "ult_comp": None}

    # Se parte con 2 pacientes; la tercera cama se llena por admisión.
    for j in jugadores:
        for i in range(min(2, camas_c)):
            if mazo_p:
                j.camas[i] = Cama(mazo_p.pop())

    for j in jugadores:
        for _ in range(robo):
            c = robar()
            if c:
                j.mano.append(c)

    for ronda in range(1, rondas + 1):
        for cama in (c for jj in jugadores for c in jj.camas if c):
            cama.atacada = False

        for j in jugadores:
            rivales = [x for x in jugadores if x is not j]
            # el escudo de A19 vence al empezar tu turno: te cubrió la vuelta
            for c in j.camas:
                if c: c.escudo = False
            j.diostor_r = False        # C01: su desvío es 1×RONDA

            # 1. ALTAS (consolidadas desde una ronda anterior)
            for i, c in enumerate(j.camas):
                if c and c.estable and c.estable_desde is not None \
                        and c.estable_desde < ronda \
                        and not (BASURA_BLOQUEA == "alta" and c.basura > 0):
                    if STATS is not None: STATS["altas_r"][ronda] += 1
                    if j.avatar == "C08" and not j.hab_p:
                        cc = robar()
                        if cc: j.mano.append(cc)
                        j.hab_p = True; marcar(j, "C08")
                    j.altas.append(c.f)
                    for _ in range(sum(c.tiene.values())):
                        pass       # los recursos vuelven al descarte (abstracto)
                    j.camas[i] = None

            # 2. ADMISIÓN OBLIGATORIA (revela 2, elige 1)
            # v0.32: la ronda 1 se juega con los 2 pacientes de la preparación;
            # la tercera cama se llena recién en la ronda 2. Medido: neutro
            # (salv 67% igual, GIII 43→45%, ROJO 80→73%, todo en banda).
            for i, c in enumerate(j.camas if ronda > 1 else []):
                if c is None and mazo_p:
                    opciones = [mazo_p.pop() for _ in range(min(2, len(mazo_p)))]
                    mejor = max(opciones,
                                key=lambda f: (f["alta"] - f["fallece"]) / max(1, f["pide_total"]))
                    opciones.remove(mejor)
                    mazo_p[:0] = opciones
                    j.camas[i] = Cama(mejor)
                    if j.avatar == "C19" and mejor["gravedad"] in ("III", "ROJO"):
                        j.camas[i].vida += 1; marcar(j, "C19")
                    j.camas[i].revisar(ronda)

            # 3. ROBO (fijo, ± lo que dejó Doblo Turno)
            n_robo = max(0, robo + getattr(j, "robo_mod", 0)); j.robo_mod = 0
            if j.avatar == "C02":
                if ronda == 1:
                    n_robo = max(0, n_robo - 1)   # el fantasma aún no llega
                elif ronda >= 4:
                    n_robo += 1; marcar(j, "C02")
            for _ in range(n_robo):
                carta = robar()
                if carta is None:
                    break
                j.mano.append(carta)

            # C18 La Buena Muñeca: cambia la peor carta de la mano por otra
            if j.avatar == "C18" and j.mano:
                inutil = next((c for c in j.mano
                                   if not c.get("warn") and not c.get("comodin")
                                   and not c.get("previene") and not c.get("doble_en")
                                   and not any(cam and cam.falta().get(c["tipo"], 0) > 0
                                               for cam in j.camas)), None)
                if inutil:
                    j.mano.remove(inutil); mazo_g.insert(0, inutil)
                    vistas = [c for c in (robar() for _ in range(3)) if c]
                    if vistas:
                        mejor = max(vistas, key=lambda c: (
                            c.get("comodin", False)
                            or any(cam and cam.falta().get(c["tipo"], 0) > 0
                                   for cam in j.camas), not c.get("warn")))
                        vistas.remove(mejor)
                        mazo_g[:0] = vistas        # el resto vuelve al fondo
                        j.mano.append(mejor)
                    marcar(j, "C18")
            # C11 El Subespecialista: lo guardado entra gratis y cuenta doble
            if j.avatar == "C11" and j.guardado is not None:
                dest = next((c for c in elegir_objetivos(j.camas)
                             if c.falta().get(j.guardado["tipo"], 0) > 0), None)
                if dest is not None:
                    tp = j.guardado["tipo"]
                    dest.tiene[tp] += 2
                    dest.puestos.append((j.guardado, tp, 2))
                    dest.revisar(ronda); marcar(j, "C11")
                else:
                    descarte.append(j.guardado)
                j.guardado = None

            # 3.5 LA PIZARRA: compra y juega Protocolos (máx. 1 de cada)
            if PROTOCOLOS and (PROT_ASIENTOS is None
                               or jugadores.index(j) in PROT_ASIENTOS):
                turno_pizarra(j, rivales, ronda, ctx, rng)

            # 4. PASE DE VISITA: 3 indicaciones, menú
            puestos_turno = {}
            colocaciones = 3
            if hasattr(j, "recorte"):      # A18 Recorte Presupuestario
                colocaciones = j.recorte
                del j.recorte
            # C03 Doctor Amor: le roba un 🧑‍⚕️ a un rival y se lo pone encima
            if j.avatar == "C03" and not j.hab_p:
                cand = _saqueables(rivales, lambda c, tp: tp == "PERSONAL")
                dest = next((c for c in elegir_objetivos(j.camas)
                             if c.falta().get("PERSONAL", 0) > 0), None)
                if cand and dest is not None:
                    r0, cam0, k0 = cand[0]
                    robado = quitar_puesto(cam0, k0); cam0.revisar(ronda)
                    j.mano.append(robado)   # colocarlo cuesta su indicación
                    j.hab_p = True; marcar(j, "C03")

            # C15 El Dador de Altas: descarta 2 y completa al que le falta 1
            if j.avatar == "C15" and not j.hab_p and len(j.mano) >= 2:
                cerca = next((c for c in j.camas
                              if c and 0 < c.faltan_total() <= 1), None)
                if cerca is not None:
                    descarte.append(j.mano.pop(0)); descarte.append(j.mano.pop(0))
                    f = cerca.falta()
                    tp = max(f, key=lambda k: f[k])
                    cerca.tiene[tp] += f[tp]
                    cerca.revisar(ronda)
                    j.hab_p = True; marcar(j, "C15")
            # C05 La Gestora de Camas: cambia un paciente imposible por otro,
            # pero paga Sumario y renuncia a los logros de cierre
            if j.avatar == "C05" and not j.hab_p and mazo_p:
                perdido = next((c for c in j.camas if c and not c.estable
                                and c.faltan_total() > c.vida * 2.1), None)
                if perdido is not None:
                    i2 = j.camas.index(perdido)
                    j.camas[i2] = Cama(mazo_p.pop())
                    j.camas[i2].revisar(ronda)
                    j.sumarios += 1; j.sin_bonus = True
                    j.hab_p = True; marcar(j, "C05")

            # C06 El Médico Esotérico: ofrenda 1 carta y revela; lo que salga
            # se coloca gratis (con su ⚠️ si la trae)
            if j.avatar == "C06" and j.mano and mazo_g \
               and getattr(j, "usos_c06", 0) < 2:
                j.usos_c06 = getattr(j, "usos_c06", 0) + 1
                descarte.append(j.mano.pop(0))
                rev = robar()
                if rev is not None:
                    dest = next((c for c in elegir_objetivos(j.camas)
                                 if c.falta().get(rev["tipo"], 0) > 0), None)
                    if dest is None:
                        descarte.append(rev)
                    else:
                        ap = 2 if (rev.get("sistema") and
                                   rev["sistema"] == dest.f["sistema"]) else 1
                        dest.tiene[rev["tipo"]] += ap
                        dest.puestos.append((rev, rev["tipo"], ap))
                        if rev.get("previene"): dest.protege.add(rev["previene"])
                        if rev.get("warn"): resolver_warn(j, rev, dest)
                        dest.revisar(ronda); marcar(j, "C06")

            # C11: guardar en reserva CUESTA 1 indicación (pagas 1 hoy por
            # 2 mañana) — antes era gratis y valía +5 puntos
            if j.avatar == "C11" and j.guardado is None and len(j.mano) > 4 \
               and colocaciones > 0 and getattr(j, "usos_c11", 0) < 1:
                util = next((c for c in j.mano if any(
                    cam and cam.falta().get(c["tipo"], 0) > 0 for cam in j.camas)), None)
                if util is not None:
                    j.mano.remove(util); j.guardado = util
                    colocaciones -= 1
                    j.usos_c11 = getattr(j, "usos_c11", 0) + 1

            while colocaciones > 0:
                # a) des-escalada: limpiar la basura que retiene el alta o
                # que bloquea un ✅ inminente
                if BASURA_BLOQUEA == "alta":
                    bloqueada = next((c for c in j.camas if c and c.basura > 0
                                      and (c.estable or c.faltan_total() <= 1)), None)
                else:
                    bloqueada = next((c for c in j.camas if c and c.basura > 0
                                      and c.faltan_total() <= 1), None)
                if bloqueada is not None:
                    if STATS is not None: STATS["limpiezas"] += 1
                    bloqueada.basura -= 1
                    colocaciones -= 1
                    bloqueada.revisar(ronda)
                    continue
                # a2) sabotaje PRIORITARIO: el rival está a 1 de cerrar y
                # tengo basura ⚠️ que bloquearle el ✅ — la jugada de tempo
                # que un humano no deja pasar
                if ATAQUES and getattr(j, "ataca", True):
                    sab = elegir_sabotaje(j, rivales)
                    if sab is not None:
                        carta, cama, duenio = sab
                        if cama.faltan_total() <= 1 and not cama.estable:
                            if STATS is not None: STATS["sabotajes"] += 1
                            j.mano.remove(carta)
                            cama.basura += 1
                            cama.atacada = True
                            comp = carta.get("comp") or {"nombre": "", "vida": -1}
                            if not (comp["nombre"] and comp["nombre"] in cama.protege):
                                cama.vida = max(PISO_RIVAL, cama.vida + comp["vida"])
                                ctx["ult_comp"] = cama
                                if carta.get("turno24") and duenio.mano:
                                    duenio.mano.pop(0)
                            cama.revisar(ronda)
                            colocaciones -= 1
                            continue
                # b) tratar lo propio
                jugada = None
                mano_ok = [c for c in j.mano
                           if not (getattr(j, "sin_far", False) and c["tipo"] == "FARMACOS")]
                for cama in elegir_objetivos(j.camas):
                    carta, aporte, tipo = elegir_carta(mano_ok, cama)
                    if carta is not None:
                        jugada = (carta, aporte, tipo, cama)
                        break
                if jugada:
                    carta, aporte, tipo, cama = jugada
                    if j.avatar == "C16" and carta["tipo"] == "IMAGEN" \
                       and carta.get("sistema") and aporte < 2:
                        aporte = 2; marcar(j, "C16")
                    puestos_turno.setdefault(id(cama), []).append(tipo)
                    pt = puestos_turno[id(cama)]
                    if j.avatar == "C13" and len(pt) == 3 \
                       and len(set(pt)) == 3 and aporte == 1:
                        aporte = 2; marcar(j, "C13")
                    j.mano.remove(carta)
                    descarte.append(carta)
                    cama.tiene[tipo] += aporte
                    cama.puestos.append((carta, tipo, aporte))
                    if carta.get("previene"):
                        cama.protege.add(carta["previene"])
                    if carta.get("warn"):
                        # C01 El Diostor: la complicación la sufre el rival
                        desviada = False
                        if j.avatar == "C01" and not j.diostor_r and len(j.mano) >= 3:
                            victima = next((cm for r in rivales for cm in r.camas
                                            if cm and not cm.escudo), None)
                            if victima is not None:
                                j.mano.sort(key=lambda x: (x.get("comodin", False),
                                                           bool(x.get("sistema"))))
                                descarte.append(j.mano.pop(0))
                                descarte.append(j.mano.pop(0))
                                comp = carta.get("comp") or {"nombre":"", "vida":-1}
                                if not (comp["nombre"] and comp["nombre"] in victima.protege):
                                    victima.vida = max(PISO_RIVAL, victima.vida + comp["vida"])
                                    victima.revisar(ronda)
                                j.diostor_r = True; desviada = True
                                marcar(j, "C01")
                        if not desviada:
                            resolver_warn(j, carta, cama)   # propio: sin piso
                            contar_warn(j, ctx)
                            ctx["ult_comp"] = cama
                    cama.revisar(ronda)
                    colocaciones -= 1
                # c) sabotaje con la basura de la mano
                elif ATAQUES and getattr(j, "ataca", True):
                    sab = elegir_sabotaje(j, rivales)
                    if sab is None:
                        break
                    carta, cama, duenio = sab
                    if STATS is not None: STATS["sabotajes"] += 1
                    j.mano.remove(carta)
                    # el recurso queda sobre la cama rival como basura
                    cama.basura += 1
                    cama.atacada = True
                    comp = carta.get("comp") or {"nombre": "", "vida": -1}
                    if not (comp["nombre"] and comp["nombre"] in cama.protege):
                        cama.vida = max(PISO_RIVAL, cama.vida + comp["vida"])
                        ctx["ult_comp"] = cama
                        if carta.get("turno24") and duenio.mano:
                            duenio.mano.pop(0)
                    cama.revisar(ronda)
                    colocaciones -= 1
                else:
                    break
                # muertes inmediatas por ⚠️ propia
                for i2, c2 in enumerate(j.camas):
                    if c2 and c2.vida <= 0:
                        j.muertos.append(c2.f)
                        j.camas[i2] = None
                        j.sumarios += 1

            j.sin_far = False   # A17 Quiebre de Stock: dura SOLO este pase

            # 4.5 ALTA ANTICIPADA (medición): egresa YA un paciente
            # estabilizado esta misma ronda y sin basura, saltando la
            # ventana de consolidación (y el sabotaje que cabe en ella)
            while j.alta_ya > 0 and ALTA_YA_DESDE <= ronda <= ALTA_YA_HASTA:
                listas = [(i2, c2) for i2, c2 in enumerate(j.camas)
                          if c2 and c2.estable and c2.estable_desde == ronda
                          and c2.basura == 0]
                if not listas:
                    break
                i2, c2 = max(listas, key=lambda x: x[1].f["alta"])
                j.altas.append(c2.f)
                j.camas[i2] = None
                j.alta_ya -= 1
                j.pena = getattr(j, "pena", 0) + ALTA_YA_PENA
                for _ in range(ALTA_YA_ROBA):
                    cr = robar()
                    if cr:
                        j.mano.append(cr)
                if STATS is not None:
                    STATS["altas_r"][ronda] += 1
                    STATS["alta_ya_usos"] += 1


            if STATS is not None:
                STATS["coloc"].append(3 - max(0, colocaciones))
                if colocaciones > 0 and not any(
                        elegir_carta(j.mano, c)[0] for c in j.camas if c):
                    STATS["mano_seca"] += 1
                STATS["turnos"] += 1

            # 5. CERRAR SUMARIOS (2 cartas, sin colocación — balance final:
            #    con colocación nadie cerraba nunca, 0% medido; así, 94%)
            # C04 El Director: perdona un Sumario 1×PARTIDA y luego cierra barato
            if j.avatar == "C04" and not j.hab_p and j.sumarios > 0:
                j.sumarios -= 1; j.hab_p = True; marcar(j, "C04")
            paga = 1 if j.avatar == "C04" else 2
            while j.sumarios > 0 and len(j.mano) >= paga:
                if paga == 1: marcar(j, "C04")
                j.mano.sort(key=lambda c: (c.get("comodin", False),
                                           bool(c.get("sistema"))))
                for _ in range(paga):
                    descarte.append(j.mano.pop(0))
                j.sumarios -= 1
                if STATS is not None: STATS["sum_cerrados"] += 1

            # 6. CIERRE DE MANO (cada Sumario abierto muerde 1 de mano)
            if STATS is not None and len(j.mano) > max(1, mano_max - j.sumarios):
                STATS["descarto"] += 1
            while len(j.mano) > max(1, mano_max - j.sumarios):
                bota = j.mano[0]
                j.mano.remove(bota)
                descarte.append(bota)

            # 7. FIN DE GUARDIA
            # C07 La Enfermera de Noche: descarta 2 y esta noche nadie cae
            velada = None
            if j.avatar == "C07" and not j.hab_p and len(j.mano) >= 3 \
               and any(c and not c.estable and c.vida <= 1 for c in j.camas):
                for _ in range(3): descarte.append(j.mano.pop(0))
                velada = min((c for c in j.camas if c and not c.estable),
                             key=lambda c: c.vida)
                j.hab_p = True; marcar(j, "C07")
            for i, c in enumerate(j.camas):
                if c is None:
                    continue
                # v0.61 · el soporte vital para el reloj mientras esté puesto
                soporte = any(x[0].get("soporte") for x in c.puestos)
                if not c.estable and c is not velada and not soporte:
                    c.vida -= 1 + c.extra          # A08 Llaman de Urgencias
                c.extra = 0
                if c.vida <= 0:
                    # C14 El Reanimador: lo salva una vez, sin sus recursos
                    if j.avatar == "C14" and not j.hab_p:
                        c.vida = 1; c.tiene = Counter(); c.puestos = []
                        c.estable = False; c.estable_desde = None
                        j.hab_p = True; marcar(j, "C14")
                        continue
                    j.muertos.append(c.f)
                    j.camas[i] = None
                    j.sumarios += 1
                    # C20 El Carroñero: le roba una carta al que puso el ✝️
                    for r in rivales:
                        if r.avatar == "C20" and j.mano:
                            r.mano.append(j.mano.pop()); marcar(r, "C20")
                    if STATS is not None: STATS["muertes_r"][ronda] += 1

    for j in jugadores:
        j.vacias = sum(1 for x in j.camas if x is None)

    if AUDITORIA and len(jugadores) > 1:
        abiertos = [j.sumarios for j in jugadores]
        tope = max(abiertos)
        if tope > 0 and abiertos.count(tope) == 1:
            jugadores[abiertos.index(tope)].auditoria = 3

    return jugadores


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--partidas", type=int, default=4000)
    ap.add_argument("--jugadores", type=int, default=2)
    ap.add_argument("--camas", type=int, default=3)
    ap.add_argument("--rondas", type=int, default=8)
    ap.add_argument("--semilla", type=int, default=42)
    ap.add_argument("--sin-ataques", action="store_true")
    args = ap.parse_args()

    global ATAQUES
    if args.sin_ataques:
        ATAQUES = False

    pacientes, guardia = cargar()
    rng = random.Random(args.semilla)
    import statistics
    pts, altas, mu = [], [], []
    limpio = 0
    g = {k: [0, 0] for k in ("I", "II", "III", "ROJO")}
    for _ in range(args.partidas):
        for j in jugar(pacientes, guardia, args.jugadores, args.camas,
                       args.rondas, rng):
            pts.append(j.puntos())
            altas.append(len(j.altas))
            mu.append(len(j.muertos))
            if not j.muertos:
                limpio += 1
            for f in j.altas:
                g[f["gravedad"]][0] += 1
            for f in j.muertos:
                g[f["gravedad"]][1] += 1

    tot = [sum(v[0] for v in g.values()), sum(v[1] for v in g.values())]
    print(f"— ¡VAYA TURNO! · rama v0.30 ({'con' if ATAQUES else 'SIN'} sabotaje) —")
    print(f"{args.partidas} partidas · {args.jugadores} jugadores · "
          f"{args.camas} camas · {args.rondas} rondas\n")
    print(f"Altas por jugador      {statistics.mean(altas):.2f}")
    print(f"Fallecidos por jugador {statistics.mean(mu):.2f}")
    print(f"Tasa de salvamento     {100 * tot[0] / sum(tot):.0f}%   (objetivo 55-70%)")
    print(f"Puntaje medio          {statistics.mean(pts):.1f}")
    print(f'"No se me fue nadie"   {100 * limpio / len(pts):.1f}%   (objetivo 5-15%)')
    print("\ngravedad    altas  muertes  % salvado")
    for k in g:
        a, m = g[k]
        print(f"{k:<10} {a:6} {m:8} {100 * a / max(1, a + m):9.0f}%")


if __name__ == "__main__":
    main()
