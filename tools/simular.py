#!/usr/bin/env python3
"""
Simulador de balance de ¡VAYA TURNO!

No simula personajes ni cartas de Acción individuales: modela la ECONOMÍA
base del juego (ingreso de recursos vs. demanda de los pacientes vs. reloj
de deterioro) con una IA codiciosa. Sirve para responder una sola pregunta:

    ¿cuántos pacientes salva un jugador que juega razonablemente bien,
    SIN ayuda de habilidades y SIN atacar a nadie?

Ese número es el suelo del balance. Si el suelo está bien, las habilidades y
los ataques mueven el juego alrededor de un centro sano.

Uso:  python3 tools/simular.py [--partidas 2000] [--rondas 8] [--jugadores 3]
      python3 tools/simular.py --jugadores 4 --camas 2 --robo 3 --rondas 10
"""

import argparse
import csv
import os
import random
from collections import Counter

# ── Reglas v0.21 (medidas en DISENO.md §4i–§4j) ──
TOPE_VISITA = 3          # máx. recursos colocados por turno (None = sin tope, v0.19)
ADMISION = "opcional"    # "forzada" (v0.19) | "opcional"
CAMA_VACIA = "punto"     # cama vacía al Fin de Guardia = −1 punto ("sumario"/"nada" son variantes)
UMBRAL_ADM = -3          # margen mínimo para admitir (política IA; -3 = casi siempre, lo medido óptimo)
# v0.21 Informe de Gestión de Camas: la primera carta de Urgencia está boca
# arriba. Medido: NO cambia ningún resultado (salv 67%, GIII 40% con y sin) —
# la regla cambia lo que el jugador SABE, no el estado del juego, y una IA con
# política fija no puede aprovecharla. Se deja en False para que las medidas
# sigan siendo comparables con la línea base afinada; ponlo en True para ver el
# efecto de admitir sabiendo el costo del que viene (solo deja más camas vacías).
URGENCIA_VISIBLE = False
TIPOS = ("IMAGEN", "FARMACOS", "PERSONAL", "PROCEDIMIENTOS")
COL = {"IMAGEN": "img", "FARMACOS": "far", "PERSONAL": "per", "PROCEDIMIENTOS": "proc"}
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def cargar():
    def leer(n):
        with open(os.path.join(RAIZ, "cartas", n), encoding="utf-8") as f:
            return list(csv.DictReader(f))

    pacientes = []
    for p in leer("pacientes.csv"):
        ficha = {
            "nombre": p["nombre"],
            "gravedad": p["gravedad"],
            "vida": int(p["vida"]),
            "sistema": p["sistema"],
            "pide": {t: int(p[COL[t]]) for t in TIPOS},
            "alta": int(p["puntos_alta"]),
            "fallece": int(p["puntos_fallece"]),
        }
        ficha["pide_total"] = sum(ficha["pide"].values())
        # la columna `copias` manda igual que en los recursos: hoy todos los
        # pacientes son únicos, pero el Taller deja subirla y el mazo tiene
        # que crecer de verdad si alguien lo hace.
        for _ in range(int(p.get("copias") or 1)):
            pacientes.append(ficha)

    # v0.10: el Mazo de Guardia son SOLO recursos. Las Acciones viven en el
    # mazo de Protocolos (se compran con el Canje) y la IA no las usa: este
    # simulador mide el suelo del balance.
    guardia = []
    for r in leer("recursos.csv"):
        # v0.14: la complicación va impresa en la propia carta ⚠️, con su
        # 🎯 objetivo. Ya no existe el Mazo de Eventos Centinela.
        comp = {"nombre": r.get("comp_nombre", ""),
                "objetivo": r.get("comp_objetivo", ""),
                "vida": int(r.get("comp_vida") or 0),
                "pide": r.get("comp_pide", ""),
                "descarta": r.get("comp_descarta", "")}
        for _ in range(int(r["copias"])):
            guardia.append({"clase": "recurso", "tipo": r["tipo"],
                            "previene": r.get("previene", ""),
                            "sistema": r["sistema"],
                            "comodin": r["comodin"] == "si",
                            "restriccion": r["restriccion"],
                            "warn": r["complicacion"] == "si",
                            "comp": comp})

    return pacientes, guardia


class Cama:
    """Un paciente ocupando una cama, con su tratamiento encima."""

    def __init__(self, ficha):
        self.f = ficha
        self.vida = ficha["vida"]
        self.pide = dict(ficha["pide"])   # puede crecer por eventos
        self.tiene = Counter()
        self.estable = False
        self.estable_desde = None         # ronda en que se estabilizó
        self.protege = set()              # complicaciones prevenidas (v0.20)
        self.nuevo = True                 # no se deteriora el turno que llega

    def falta(self):
        return {t: max(0, self.pide[t] - self.tiene[t]) for t in TIPOS}

    def faltan_total(self):
        return sum(self.falta().values())

    def revisar(self, ronda):
        """Recalcula el estado ✅ tras cualquier cambio."""
        completo = self.faltan_total() == 0
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

    def defendible(self):
        """Se te fueron solo los que se tenían que ir (Gravedad III o ROJO)."""
        return bool(self.muertos) and all(
            c["gravedad"] in ("III", "ROJO") for c in self.muertos)

    def puntos(self):
        p = sum(c["alta"] for c in self.altas) + sum(c["fallece"] for c in self.muertos)
        p -= getattr(self, "vacias", 0)   # v0.20: cama vacía = −1 (variante "punto")
        if not self.muertos:
            p += 3          # "No se me fue nadie"
        elif self.defendible():
            p += 1          # "Se hizo todo"
        return p


def elegir_objetivos(camas, mano_tipos):
    """
    Triage codicioso: reparte el foco en los pacientes con mejor
    (puntos ganados) / (recursos que aún faltan), descartando a los que ya
    no alcanzan a salvarse con el ingreso esperado.
    """
    vivos = [c for c in camas if c and not c.estable]
    puntuados = []
    for c in vivos:
        faltan = c.faltan_total()
        if faltan == 0:
            continue
        # ~2.1 recursos útiles por turno; hace falta que quepan en su vida
        alcanzable = faltan <= c.vida * 2.1
        valor = (c.f["alta"] - c.f["fallece"]) / faltan
        puntuados.append((alcanzable, valor, c))
    puntuados.sort(key=lambda x: (not x[0], -x[1]))
    return [c for _, _, c in puntuados]


def elegir_carta(mano, cama):
    """
    Devuelve (carta, aporte, tipo) para la mejor jugada sobre esta cama.
    Prioriza sinergia (el recurso de su sistema cuenta doble), luego recurso
    normal, y deja el comodín como último recurso.
    Respeta las restricciones: TAC exige 🧑‍⚕️ ya puesto sobre el paciente.
    """
    falta = cama.falta()
    if sum(falta.values()) == 0:
        return None, 0, None

    def jugable(c):
        if c["clase"] != "recurso":
            return False
        if c.get("restriccion") == "PERSONAL" and cama.tiene["PERSONAL"] == 0:
            return False
        return True

    # 1) sinérgica y necesaria → cuenta doble
    for c in mano:
        if (jugable(c) and c.get("sistema") and c["sistema"] == cama.f["sistema"]
                and falta.get(c["tipo"], 0) > 0):
            return c, 2, c["tipo"]
    # 2) recurso normal necesario
    for c in mano:
        if jugable(c) and not c.get("comodin") and falta.get(c["tipo"], 0) > 0:
            return c, 1, c["tipo"]
    # 3) comodín, al hueco más grande
    for c in mano:
        if c.get("comodin"):
            t = max(falta, key=lambda k: falta[k])
            if falta[t] > 0:
                return c, 1, t
    return None, 0, None


def elegir_victima(j, objetivo):
    """Resuelve el 🎯 Objetivo impreso en la carta ⚠️ (REGLAMENTO §7)."""
    ocupadas = [c for c in j.camas if c]
    if not ocupadas:
        return None
    if objetivo == "MAS_GRAVE":
        return min(ocupadas, key=lambda c: c.vida)
    if objetivo == "MEJOR":
        return max(ocupadas, key=lambda c: c.vida)
    if objetivo == "MAS_TRATADO":
        return max(ocupadas, key=lambda c: sum(c.tiene.values()))
    if objetivo == "ESTABLE":
        est = [c for c in ocupadas if c.estable]
        return est[0] if est else max(ocupadas, key=lambda c: c.vida)
    # ELIGES: un jugador razonable se protege y manda el golpe al que ya perdió
    return max(ocupadas, key=lambda c: c.faltan_total() - c.vida)


def aplicar_complicacion(j, carta, descarte, cama_jugada=None):
    """v0.14: cada ⚠️ trae su complicación impresa en vez de mandarte a un
    mazo aparte. La carta dice qué pasa y a quién."""
    comp = carta.get("comp") or {}
    objetivo = comp.get("objetivo")
    if not objetivo:
        return

    if objetivo == "MANO":                  # golpea tu mano, no una cama
        if j.mano:
            j.mano.sort(key=lambda c: (c.get("comodin", False),
                                       bool(c.get("sistema"))))
            descarte.append(j.mano.pop(0))
        return

    # v0.18: ESTE = el paciente que recibió la carta. La NAVM le da al que
    # ventilaste, no a otro. Solo tiene sentido con el disparo al colocar.
    if objetivo == "ESTE":
        cama = cama_jugada
    else:
        cama = elegir_victima(j, objetivo)
    if cama is None:
        return
    # v0.20: la prevención es prospectiva — si el protector ya estaba, no ocurre
    if comp.get("nombre") and comp["nombre"] in cama.protege:
        return
    if comp.get("vida"):
        cama.vida += comp["vida"]
    if comp.get("pide"):
        cama.pide[comp["pide"]] += 1
    if comp.get("descarta") and cama.tiene[comp["descarta"]] > 0:
        cama.tiene[comp["descarta"]] -= 1
        if comp["descarta"] == "PERSONAL" and cama.tiene["PERSONAL"] <= 0:
            cama.protege.clear()          # el protector se fue con el resto


def jugar(pacientes, guardia, n_jug, camas_c, rondas, rng, robo=4, mano_max=5,
          jugadas_max=99, sumario=True, deterioro="final", gracia=False):
    mazo_p = pacientes[:]
    rng.shuffle(mazo_p)
    mazo_g = guardia[:]
    rng.shuffle(mazo_g)
    descarte = []

    def robar():
        if not mazo_g:
            mazo_g.extend(descarte)
            descarte.clear()
            rng.shuffle(mazo_g)
        return mazo_g.pop() if mazo_g else None

    jugadores = [Jugador(camas_c) for _ in range(n_jug)]
    for j in jugadores:
        j.sumarios = 0

    # Admisión inicial
    for j in jugadores:
        for i in range(camas_c):
            if mazo_p:
                j.camas[i] = Cama(mazo_p.pop())

    def deteriorar(j):
        for i, c in enumerate(j.camas):
            if not c:
                continue
            if c.nuevo:
                c.nuevo = False
                if gracia:
                    continue
            if not c.estable:
                c.vida -= 1
                if c.vida <= 0:
                    j.muertos.append(c.f)
                    j.camas[i] = None
                    if sumario:
                        j.sumarios += 1

    for ronda in range(1, rondas + 1):
        for j in jugadores:
            # 1. DETERIORO (variante clásica: al abrir el turno)
            if deterioro == "inicio":
                deteriorar(j)

            # 2. ALTA (estabilizado desde una ronda anterior)
            for i, c in enumerate(j.camas):
                if c and c.estable and c.estable_desde is not None and c.estable_desde < ronda:
                    j.altas.append(c.f)
                    j.camas[i] = None

            # 3. ADMISIÓN (revela 2, elige 1) — v0.20: opcional
            pendiente = sum(x.faltan_total() for x in j.camas if x)
            for i, c in enumerate(j.camas):
                if c is None and mazo_p:
                    if ADMISION == "opcional":
                        ritmo = TOPE_VISITA or 3.5
                        margen = (rondas - ronda + 1) * ritmo - pendiente
                        # v0.21 Informe de Gestión de Camas: el primero de la
                        # fila está boca arriba, así que su costo se decide
                        # sabiéndolo, no a ciegas.
                        if URGENCIA_VISIBLE:
                            margen -= mazo_p[-1]["pide_total"]
                        if margen < UMBRAL_ADM:
                            continue
                    opciones = [mazo_p.pop() for _ in range(min(2, len(mazo_p)))]
                    mejor = max(opciones,
                                key=lambda f: (f["alta"] - f["fallece"]) / max(1, f["pide_total"]))
                    opciones.remove(mejor)
                    mazo_p[:0] = opciones          # el otro al fondo
                    j.camas[i] = Cama(mejor)
                    j.camas[i].revisar(ronda)

            # 4. GUARDIA
            for _ in range(robo):
                carta = robar()
                if carta is None:
                    break
                j.mano.append(carta)

            # 4b. SUMARIOS: cerrar cada uno cuesta 2 cartas. La IA paga
            # apenas puede, botando los tipos que más le sobran.
            while j.sumarios > 0 and len(j.mano) >= 2:
                sistemas = {c.f["sistema"] for c in j.camas if c}
                j.mano.sort(key=lambda c: (
                    -sum(1 for x in j.mano if x["tipo"] == c["tipo"]),
                    c.get("comodin", False),
                    c.get("sistema") in sistemas,
                ))
                descarte.append(j.mano.pop(0))
                descarte.append(j.mano.pop(0))
                j.sumarios -= 1

            # 5. ACCIÓN (recursos ilimitados; la IA no juega Acciones)
            jugadas = 0
            tope = TOPE_VISITA if TOPE_VISITA else jugadas_max
            turno_bloqueado = False       # lo activa la Resonancia
            while jugadas < min(tope, jugadas_max) and not turno_bloqueado:
                orden = elegir_objetivos(j.camas, None)
                colocada = False
                for cama in orden:
                    carta, aporte, tipo = elegir_carta(j.mano, cama)
                    if carta is None:
                        continue
                    j.mano.remove(carta)
                    descarte.append(carta)
                    cama.tiene[tipo] += aporte
                    if carta.get("previene"):
                        cama.protege.add(carta["previene"])
                    cama.revisar(ronda)
                    # v0.17: la complicación ⚠️ se dispara AL COLOCAR la carta
                    # sobre un paciente, no al robarla (REGLAMENTO §7).
                    if carta["warn"]:
                        aplicar_complicacion(j, carta, descarte, cama)
                        for i2, c2 in enumerate(j.camas):
                            if c2 and c2.vida <= 0:
                                j.muertos.append(c2.f)
                                j.camas[i2] = None
                                if sumario:
                                    j.sumarios += 1
                            elif c2:
                                c2.revisar(ronda)
                    jugadas += 1
                    colocada = True
                    if carta.get("restriccion") == "TURNO":
                        turno_bloqueado = True
                    break
                if not colocada:
                    break

            # 6. CIERRE (cada Sumario abierto resta 1 al límite de mano)
            while len(j.mano) > max(1, mano_max - j.sumarios):
                # bota primero las Acciones (esta IA no las usa)
                bota = next((c for c in j.mano if c["clase"] == "accion"), j.mano[0])
                j.mano.remove(bota)
                descarte.append(bota)

            # 7. FIN DE GUARDIA (variante propuesta: el día pasa al cerrar)
            if deterioro == "final":
                deteriorar(j)
            if ronda < rondas:
                vacias = sum(1 for x in j.camas if x is None)
                if vacias and CAMA_VACIA == "sumario" and sumario:
                    j.sumarios += vacias
                elif vacias and CAMA_VACIA == "punto":
                    j.vacias = getattr(j, "vacias", 0) + vacias

    return jugadores


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--partidas", type=int, default=2000)
    ap.add_argument("--rondas", type=int, default=8)
    ap.add_argument("--jugadores", type=int, default=3)
    ap.add_argument("--camas", type=int, default=3)
    ap.add_argument("--robo", type=int, default=4,
                    help="cartas robadas por turno (3 en partidas de 4 jugadores)")
    ap.add_argument("--sin-sumario", action="store_true",
                    help="desactiva la maldición del Sumario Administrativo")
    ap.add_argument("--mano", type=int, default=5, help="límite de mano")
    ap.add_argument("--semilla", type=int, default=7)
    ap.add_argument("--deterioro", choices=["inicio", "final"], default="final",
                    help="cuándo baja el contador: al abrir el turno (v0.11) "
                         "o en el Fin de Guardia (v0.12, por defecto)")
    ap.add_argument("--con-gracia", action="store_true",
                    help="el paciente recién admitido NO se deteriora su primer día "
                         "(regla de v0.11)")
    args = ap.parse_args()

    pacientes, guardia = cargar()
    for f in pacientes:
        f["pide_total"] = sum(f["pide"].values())

    rng = random.Random(args.semilla)
    altas, muertos, puntos, limpias, defendibles = [], [], [], 0, 0
    por_gravedad = {g: [0, 0] for g in ("I", "II", "III", "ROJO")}   # [altas, muertes]

    for _ in range(args.partidas):
        for j in jugar(pacientes, guardia, args.jugadores, args.camas, args.rondas,
                       rng, robo=args.robo, mano_max=args.mano, jugadas_max=99,
                       sumario=not args.sin_sumario, deterioro=args.deterioro,
                       gracia=args.con_gracia):
            altas.append(len(j.altas))
            muertos.append(len(j.muertos))
            puntos.append(j.puntos())
            if not j.muertos:
                limpias += 1
            elif j.defendible():
                defendibles += 1
            for f in j.altas:
                por_gravedad[f["gravedad"]][0] += 1
            for f in j.muertos:
                por_gravedad[f["gravedad"]][1] += 1

    n = len(altas)
    prom = lambda xs: sum(xs) / len(xs)
    print(f"— ¡VAYA TURNO! · balance base —")
    print(f"{args.partidas} partidas · {args.jugadores} jugadores · "
          f"{args.camas} camas · {args.rondas} rondas\n")
    print(f"Altas por jugador      {prom(altas):.2f}")
    print(f"Fallecidos por jugador {prom(muertos):.2f}")
    tot = prom(altas) + prom(muertos)
    print(f"Tasa de salvamento     {100 * prom(altas) / tot:.0f}%   "
          f"(objetivo de diseño: 55-70%)")
    print(f"Puntaje medio          {prom(puntos):.1f}   "
          f"(rango {min(puntos)} a {max(puntos)})")
    print(f'"No se me fue nadie"  {100 * limpias / n:>5.1f}%   '
          f"(+3 · objetivo 5-15%: debe ser una hazaña)")
    print(f'"Se hizo todo"       {100 * defendibles / n:>5.1f}%   '
          f"(+1 · tus únicos ✝️ fueron Gravedad III o ROJO)\n")
    print(f"{'gravedad':<10}{'altas':>7}{'muertes':>9}{'% salvado':>11}")
    for g, (a, m) in por_gravedad.items():
        pct = 100 * a / (a + m) if a + m else 0
        print(f"{g:<10}{a:>7}{m:>9}{pct:>10.0f}%")


if __name__ == "__main__":
    main()
