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
                "sistema": p["sistema"],
                "pide": {t: int(p[COL[t]]) for t in TIPOS},
                "alta": int(p["puntos_alta"]),
                "fallece": int(p["puntos_fallece"]),
            }
        )

    # v0.10: el Mazo de Guardia son SOLO recursos. Las Acciones viven en el
    # mazo de Protocolos (se compran con el Canje) y la IA no las usa: este
    # simulador mide el suelo del balance.
    guardia = []
    for r in leer("recursos.csv"):
        for _ in range(int(r["copias"])):
            guardia.append({"clase": "recurso", "tipo": r["tipo"],
                            "sistema": r["sistema"],
                            "comodin": r["comodin"] == "si",
                            "restriccion": r["restriccion"],
                            "warn": r["complicacion"] == "si"})

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


def jugar(pacientes, guardia, n_jug, camas_c, rondas, rng, robo=4, mano_max=5,
          jugadas_max=99, sumario=True, deterioro="inicio", gracia=True):
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
                            if sumario:
                                j.sumarios += 1
                        elif c:
                            c.revisar(ronda)

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
            turno_bloqueado = False       # lo activa la Resonancia
            while jugadas < jugadas_max and not turno_bloqueado:
                orden = elegir_objetivos(j.camas, None)
                colocada = False
                for cama in orden:
                    carta, aporte, tipo = elegir_carta(j.mano, cama)
                    if carta is None:
                        continue
                    j.mano.remove(carta)
                    descarte.append(carta)
                    cama.tiene[tipo] += aporte
                    cama.revisar(ronda)
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
    ap.add_argument("--deterioro", choices=["inicio", "final"], default="inicio",
                    help="cuándo baja el contador: al abrir el turno o al cerrarlo")
    ap.add_argument("--sin-gracia", action="store_true",
                    help="el paciente recién admitido también se deteriora")
    args = ap.parse_args()

    pacientes, guardia = cargar()
    for f in pacientes:
        f["pide_total"] = sum(f["pide"].values())

    rng = random.Random(args.semilla)
    altas, muertos, puntos, limpias = [], [], [], 0
    por_gravedad = {g: [0, 0] for g in ("I", "II", "III", "ROJO")}   # [altas, muertes]

    for _ in range(args.partidas):
        for j in jugar(pacientes, guardia, args.jugadores, args.camas, args.rondas,
                       rng, robo=args.robo, mano_max=args.mano, jugadas_max=99,
                       sumario=not args.sin_sumario, deterioro=args.deterioro,
                       gracia=not args.sin_gracia):
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
