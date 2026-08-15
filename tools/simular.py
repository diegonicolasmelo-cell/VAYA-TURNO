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
      python3 tools/simular.py --jugadores 4 --camas 2 --robo 4 --rondas 10
"""

import argparse
import csv
import os
import random
from collections import Counter

TIPOS = ("IMAGEN", "FARMACOS", "PERSONAL", "MONITOREO")
COL = {"IMAGEN": "img", "FARMACOS": "far", "PERSONAL": "per", "MONITOREO": "mon"}
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def cargar():
    def leer(n):
        with open(os.path.join(RAIZ, "cartas", n), encoding="utf-8") as f:
            return list(csv.DictReader(f))

    pacientes = []
    for p in leer("pacientes.csv"):
        pacientes.append(
            {
                "nombre": p["nombre"],
                "gravedad": p["gravedad"],
                "vida": int(p["vida"]),
                "pide": {t: int(p[COL[t]]) for t in TIPOS},
                "alta": int(p["puntos_alta"]),
                "fallece": int(p["puntos_fallece"]),
            }
        )

    guardia = []
    for r in leer("recursos.csv"):
        for _ in range(int(r["copias"])):
            guardia.append({"clase": "recurso", "tipo": r["tipo"],
                            "warn": r["complicacion"] == "si"})
    for a in leer("acciones.csv"):
        for _ in range(int(a["copias"])):
            guardia.append({"clase": "accion", "tipo": None, "warn": False})

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

    def puntos(self):
        p = sum(c["alta"] for c in self.altas) + sum(c["fallece"] for c in self.muertos)
        if not self.muertos:
            p += 3          # bonus Guardia Limpia
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


def aplicar_evento(j, rng):
    """Modelo agregado del Mazo de Eventos Adversos (18 cartas)."""
    ocupadas = [c for c in j.camas if c]
    if not ocupadas:
        return
    r = rng.random()
    if r < 0.33:                                   # pérdida de vida
        c = min(ocupadas, key=lambda c: c.faltan_total())
        c.vida -= rng.choice([1, 1, 2])
    elif r < 0.66:                                 # pérdida de recursos
        c = rng.choice(ocupadas)
        con = [t for t in TIPOS if c.tiene[t] > 0]
        if con:
            c.tiene[rng.choice(con)] -= 1
    else:                                          # sube la exigencia
        c = rng.choice(ocupadas)
        c.pide[rng.choice(TIPOS)] += 1


def jugar(pacientes, guardia, n_jug, camas_c, rondas, rng, robo=5, mano_max=5, jugadas_max=99):
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

    # Admisión inicial
    for j in jugadores:
        for i in range(camas_c):
            if mazo_p:
                j.camas[i] = Cama(mazo_p.pop())

    for ronda in range(1, rondas + 1):
        for j in jugadores:
            # 1. DETERIORO
            for i, c in enumerate(j.camas):
                if not c:
                    continue
                if c.nuevo:
                    c.nuevo = False
                    continue
                if not c.estable:
                    c.vida -= 1
                    if c.vida <= 0:
                        j.muertos.append(c.f)
                        j.camas[i] = None

            # 2. ALTA (estabilizado desde una ronda anterior)
            for i, c in enumerate(j.camas):
                if c and c.estable and c.estable_desde is not None and c.estable_desde < ronda:
                    j.altas.append(c.f)
                    j.camas[i] = None

            # 3. ADMISIÓN (revela 2, elige 1)
            for i, c in enumerate(j.camas):
                if c is None and mazo_p:
                    opciones = [mazo_p.pop() for _ in range(min(2, len(mazo_p)))]
                    mejor = max(opciones, key=lambda f: (f["alta"] - f["fallece"]) / f["pide_total"])
                    opciones.remove(mejor)
                    mazo_p[:0] = opciones          # el otro al fondo
                    j.camas[i] = Cama(mejor)

            # 4. GUARDIA
            for _ in range(robo):
                carta = robar()
                if carta is None:
                    break
                j.mano.append(carta)
                if carta["warn"]:
                    aplicar_evento(j, rng)
                    for i, c in enumerate(j.camas):
                        if c and c.vida <= 0:
                            j.muertos.append(c.f)
                            j.camas[i] = None
                        elif c:
                            c.revisar(ronda)

            # 5. ACCIÓN (recursos ilimitados; la IA no juega Acciones)
            jugadas = 0
            while jugadas < jugadas_max:
                orden = elegir_objetivos(j.camas, [c["tipo"] for c in j.mano])
                colocada = False
                for cama in orden:
                    falta = cama.falta()
                    for carta in j.mano:
                        if carta["clase"] == "recurso" and falta.get(carta["tipo"], 0) > 0:
                            j.mano.remove(carta)
                            descarte.append(carta)
                            cama.tiene[carta["tipo"]] += 1
                            cama.revisar(ronda)
                            jugadas += 1
                            colocada = True
                            break
                    if colocada:
                        break
                if not colocada:
                    break

            # 6. CIERRE
            while len(j.mano) > mano_max:
                # bota primero las Acciones (esta IA no las usa)
                bota = next((c for c in j.mano if c["clase"] == "accion"), j.mano[0])
                j.mano.remove(bota)
                descarte.append(bota)

    return jugadores


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--partidas", type=int, default=2000)
    ap.add_argument("--rondas", type=int, default=8)
    ap.add_argument("--jugadores", type=int, default=3)
    ap.add_argument("--camas", type=int, default=3)
    ap.add_argument("--robo", type=int, default=5,
                    help="cartas robadas por turno (4 en partidas de 4 jugadores)")
    ap.add_argument("--mano", type=int, default=5, help="límite de mano")
    ap.add_argument("--semilla", type=int, default=7)
    args = ap.parse_args()

    pacientes, guardia = cargar()
    for f in pacientes:
        f["pide_total"] = sum(f["pide"].values())

    rng = random.Random(args.semilla)
    altas, muertos, puntos, limpias = [], [], [], 0
    por_gravedad = {g: [0, 0] for g in ("I", "II", "III", "ROJO")}   # [altas, muertes]

    for _ in range(args.partidas):
        for j in jugar(pacientes, guardia, args.jugadores, args.camas, args.rondas,
                       rng, robo=args.robo, mano_max=args.mano, jugadas_max=99):
            altas.append(len(j.altas))
            muertos.append(len(j.muertos))
            puntos.append(j.puntos())
            if not j.muertos:
                limpias += 1
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
    print(f"Guardias limpias       {100 * limpias / n:.1f}%   "
          f"(objetivo: 5-15%, debe ser una hazaña)\n")
    print(f"{'gravedad':<10}{'altas':>7}{'muertes':>9}{'% salvado':>11}")
    for g, (a, m) in por_gravedad.items():
        pct = 100 * a / (a + m) if a + m else 0
        print(f"{g:<10}{a:>7}{m:>9}{pct:>10.0f}%")


if __name__ == "__main__":
    main()
