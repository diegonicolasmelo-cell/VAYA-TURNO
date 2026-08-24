#!/usr/bin/env python3
"""Simulador de la rama experimental v0.30 de ¡VAYA TURNO!

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
- v0.33: el límite de mano es 6 (era 5). Robas 4 y colocas 3, así que
  sobra 1 carta por turno: con mano 5 el descarte mordía el 69% de los
  turnos, con 6 el 58% y el resto mejora medio punto. Robar 3 en vez de
  4 —la otra salida— hunde el juego (salv 57%, el mazo nunca rebaraja).
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
PISO_RIVAL = 1           # un recurso rival no baja de aquí la vida


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
                            "cirujano": r["id"] == "R54",
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
        p -= getattr(self, "vacias", 0)
        p -= getattr(self, "auditoria", 0)
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
    cands = [(c, 2, "PERSONAL") for c in mano
             if jugable(c) and c.get("cirujano") and falta.get("PERSONAL", 0) > 0]
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
        return mazo_g.pop()

    jugadores = [Jugador(camas_c) for _ in range(n_jug)]

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

            # 1. ALTAS (consolidadas desde una ronda anterior)
            for i, c in enumerate(j.camas):
                if c and c.estable and c.estable_desde is not None \
                        and c.estable_desde < ronda \
                        and not (BASURA_BLOQUEA == "alta" and c.basura > 0):
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
                    j.camas[i].revisar(ronda)

            # 3. ROBO (fijo)
            for _ in range(robo):
                carta = robar()
                if carta is None:
                    break
                j.mano.append(carta)

            # 4. PASE DE VISITA: 3 colocaciones, menú
            colocaciones = 3
            if hasattr(j, "recorte"):      # A18 (no modelado, gancho)
                colocaciones = j.recorte
                del j.recorte
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
                            j.mano.remove(carta)
                            cama.basura += 1
                            cama.atacada = True
                            comp = carta.get("comp") or {"nombre": "", "vida": -1}
                            if not (comp["nombre"] and comp["nombre"] in cama.protege):
                                cama.vida = max(PISO_RIVAL, cama.vida + comp["vida"])
                                if carta.get("turno24") and duenio.mano:
                                    duenio.mano.pop(0)
                            cama.revisar(ronda)
                            colocaciones -= 1
                            continue
                # b) tratar lo propio
                jugada = None
                for cama in elegir_objetivos(j.camas):
                    carta, aporte, tipo = elegir_carta(j.mano, cama)
                    if carta is not None:
                        jugada = (carta, aporte, tipo, cama)
                        break
                if jugada:
                    carta, aporte, tipo, cama = jugada
                    j.mano.remove(carta)
                    descarte.append(carta)
                    cama.tiene[tipo] += aporte
                    if carta.get("previene"):
                        cama.protege.add(carta["previene"])
                    if carta.get("warn"):
                        resolver_warn(j, carta, cama)   # propio: sin piso
                    cama.revisar(ronda)
                    colocaciones -= 1
                # c) sabotaje con la basura de la mano
                elif ATAQUES and getattr(j, "ataca", True):
                    sab = elegir_sabotaje(j, rivales)
                    if sab is None:
                        break
                    carta, cama, duenio = sab
                    j.mano.remove(carta)
                    # el recurso queda sobre la cama rival como basura
                    cama.basura += 1
                    cama.atacada = True
                    comp = carta.get("comp") or {"nombre": "", "vida": -1}
                    if not (comp["nombre"] and comp["nombre"] in cama.protege):
                        cama.vida = max(PISO_RIVAL, cama.vida + comp["vida"])
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

            # 5. CERRAR SUMARIOS (2 cartas, sin colocación — balance final:
            #    con colocación nadie cerraba nunca, 0% medido; así, 94%)
            while j.sumarios > 0 and len(j.mano) >= 2:
                j.mano.sort(key=lambda c: (c.get("comodin", False),
                                           bool(c.get("sistema"))))
                descarte.append(j.mano.pop(0))
                descarte.append(j.mano.pop(0))
                j.sumarios -= 1

            # 6. CIERRE DE MANO (cada Sumario abierto muerde 1 de mano)
            while len(j.mano) > max(1, mano_max - j.sumarios):
                bota = j.mano[0]
                j.mano.remove(bota)
                descarte.append(bota)

            # 7. FIN DE GUARDIA
            for i, c in enumerate(j.camas):
                if c is None:
                    continue
                if not c.estable:
                    c.vida -= 1
                if c.vida <= 0:
                    j.muertos.append(c.f)
                    j.camas[i] = None
                    j.sumarios += 1

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
