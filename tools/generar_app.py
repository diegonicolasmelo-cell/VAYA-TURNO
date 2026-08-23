#!/usr/bin/env python3
"""App jugable de ¡VAYA TURNO! v0.30 — docs/app.html

Un solo archivo HTML sin servidor ni dependencias: inyecta los mazos de
`cartas/v030/` (y los pacientes/personajes de `cartas/`) dentro de
`tools/app-plantilla.html`. Se abre en cualquier navegador, funciona sin
internet salvo por las tipografías, y guarda la partida en el navegador.

El formato final del juego es FÍSICO. Esto existe para probar reglas donde
no se puedan llevar las cartas.

    python3 tools/generar_app.py
"""

import csv
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLANTILLA = os.path.join(RAIZ, "tools", "app-plantilla.html")
SALIDA = os.path.join(RAIZ, "docs", "app.html")
TIPOS = ("IMAGEN", "FARMACOS", "PERSONAL", "PROCEDIMIENTOS")
COL = {"IMAGEN": "img", "FARMACOS": "far", "PERSONAL": "per",
       "PROCEDIMIENTOS": "proc"}


def leer(*partes):
    with open(os.path.join(RAIZ, *partes), encoding="utf-8") as f:
        return list(csv.DictReader(f))


def datos():
    pacientes = []
    for p in leer("cartas", "pacientes.csv"):
        pide = {t: int(p[COL[t]]) for t in TIPOS}
        pacientes.append({
            "id": p["id"], "nombre": p["nombre"], "gravedad": p["gravedad"],
            "sistema": p["sistema"], "vida": int(p["vida"]), "pide": pide,
            "total": sum(pide.values()),
            "alta": int(p["puntos_alta"]), "fallece": int(p["puntos_fallece"]),
            "frase": p["frase"], "copias": int(p.get("copias") or 1),
        })

    recursos = []
    for r in leer("cartas", "v030", "recursos.csv"):
        recursos.append({
            "id": r["id"], "nombre": r["nombre"], "tipo": r["tipo"],
            "sistema": r["sistema"], "comodin": r["comodin"] == "si",
            "restriccion": r["restriccion"], "previene": r["previene"],
            "texto": r["texto"], "frase": r["frase"],
            "warn": r["complicacion"] == "si",
            "compNombre": r["comp_nombre"], "compTexto": r["comp_texto"],
            # dos excepciones con regla propia, marcadas por id/nombre
            "cirujano": r["id"] == "R54",
            "turno24": r["comp_nombre"] == "El Turno Veinticuatro",
            "copias": int(r["copias"]),
        })

    acciones = [{
        "id": a["id"], "nombre": a["nombre"], "tipo": a["tipo"],
        "coste": int(a["coste"]), "texto": a["texto"], "frase": a["frase"],
        "copias": int(a["copias"]),
    } for a in leer("cartas", "v030", "acciones.csv")]

    personajes = [{
        "id": c["id"], "nombre": c["nombre"], "frecuencia": c["frecuencia"],
        "habilidad": c["habilidad"], "frase": c["frase"],
    } for c in leer("cartas", "personajes.csv")]

    return {"pacientes": pacientes, "recursos": recursos,
            "acciones": acciones, "personajes": personajes}


def main():
    with open(PLANTILLA, encoding="utf-8") as f:
        plantilla = f.read()
    marca = "/*__DATOS__*/{}"
    if marca not in plantilla:
        raise SystemExit("La plantilla no tiene el marcador /*__DATOS__*/{}")
    d = datos()
    html = plantilla.replace(marca, json.dumps(d, ensure_ascii=False,
                                               separators=(",", ":")))
    os.makedirs(os.path.dirname(SALIDA), exist_ok=True)
    with open(SALIDA, "w", encoding="utf-8") as f:
        f.write(html)

    rec = sum(r["copias"] for r in d["recursos"])
    acc = sum(a["copias"] for a in d["acciones"])
    print(f"✔ App v0.30 → {SALIDA} ({len(html) // 1024} KB)")
    print(f"  {len(d['pacientes'])} pacientes · {rec} recursos · {acc} "
          f"protocolos · {len(d['personajes'])} avatares")


if __name__ == "__main__":
    main()
