# -*- coding: utf-8 -*-
"""Los datos de las cartas de muestra, leídos de los CSV vivos."""
import base64, csv, html, os
RAIZ = "/home/user/VAYA-TURNO"
AQUI = os.path.dirname(os.path.abspath(__file__))

def leer(*p): return list(csv.DictReader(open(os.path.join(RAIZ, *p), encoding="utf-8")))
def uri(cid):
    return "data:image/webp;base64," + base64.b64encode(
        open(os.path.join(AQUI, cid + ".webp"), "rb").read()).decode()
def e(s): return html.escape(s or "")

PAC = {f["id"]: f for f in leer("cartas", "pacientes.csv")}
REC = {f["id"]: f for f in leer("cartas", "v030", "recursos.csv")}
ACC = {f["id"]: f for f in leer("cartas", "v030", "acciones.csv")}
PER = {f["id"]: f for f in leer("cartas", "personajes.csv")}

SIS = {"RESP": ("🫁", "Resp", "#5b9dc4"), "CARD": ("🫀", "Card", "#e0705a"),
       "NEURO": ("🧠", "Neuro", "#a184c9"), "METAB": ("🧪", "Metab", "#5cb583"),
       "QUIR": ("🔪", "Quir", "#c19a4e")}
GCOL = {"I": "#237a5b", "II": "#b57e14", "III": "#a8382a", "ROJO": "#7a1f16"}
TCOL = {"IMAGEN": "#3d7ea6", "FARMACOS": "#b03d29", "PERSONAL": "#2f8f6b",
        "PROCEDIMIENTOS": "#7a5ba6", "COMODIN": "#8a6a2f"}
TIC = {"IMAGEN": "🩻", "FARMACOS": "💊", "PERSONAL": "🧑‍⚕️",
       "PROCEDIMIENTOS": "💉", "COMODIN": "🃏"}
ACOL = {"ATAQUE": "#b5533c", "APOYO": "#c98d3e", "CAOS": "#4a5a78",
        "RESPUESTA": "#4a8a96", "EXTREMA": "#3d2b52"}
PIDE = [("img", "IMAGEN"), ("far", "FARMACOS"), ("per", "PERSONAL"),
        ("proc", "PROCEDIMIENTOS")]

def reqs(p):
    """Las filas de requerimiento. Es LA misma gramática que el coste de
    energía de un ataque Pokémon: fichas de color a la izquierda, número a
    la derecha. Por eso se lee sin leer."""
    out = ""
    for campo, tipo in PIDE:
        n = int(p[campo] or 0)
        if not n: continue
        fichas = "".join(f'<i class="fi" style="background:{TCOL[tipo]}"></i>'
                         for _ in range(n))
        out += (f'<div class="req"><span class="fis">{fichas}</span>'
                f'<span class="rnom">{TIC[tipo]} {tipo.title()}</span>'
                f'<b>{n}</b></div>')
    return out

def vidas(p):
    return "".join('<i class="hp"></i>' for _ in range(int(p["vida"])))

def parte(hab):
    return hab.split(" — ", 1) if " — " in hab else ("", hab)

# El tinte de cada ilustración: la mediana del borde. Con arte monocromo
# —que es lo que hay— rellenar los costados con este color es invisible.
TINTE = {
    "R50": "#54898e",
    "R07": "#5b9397",
    "P04": "#d2a043",
    "P11": "#a27eb4",
    "P02": "#a4c99d",
    "A01": "#e4a884",
    "A19": "#a8a5a2",
    "C17": "#e8e5cf",
    "C19": "#85a39c",
    "C01": "#ffffff",
}
