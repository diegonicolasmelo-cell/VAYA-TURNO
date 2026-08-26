#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Le pone banda de sonido al video de portada: saca la música y deja la
unidad sonando de verdad — monitores, ventilador, dos alarmas lejanas y el
trapero, este último sincronizado con la imagen.

No hay biblioteca de efectos: todo se sintetiza acá con numpy. Las pasadas
del trapero NO están escritas a mano — se detectan midiendo hacia dónde se
mueve la mancha de movimiento en la banda baja del cuadro, así que el script
sigue sirviendo si Diego vuelve a generar el clip con otro timing.

    python3 tools/sonido_portada.py entrada.mp4 [salida.mp4]
"""
import os, subprocess, sys, tempfile
import numpy as np
from scipy.signal import butter, sosfilt, fftconvolve

SR = 48000

# ── el ffmpeg que haya ───────────────────────────────────────────────────
def ffmpeg():
    for cmd in ("ffmpeg",):
        r = subprocess.run(["which", cmd], capture_output=True, text=True)
        if r.returncode == 0:
            return r.stdout.strip()
    import imageio_ffmpeg
    return imageio_ffmpeg.get_ffmpeg_exe()

FF = ffmpeg()

def duracion(video):
    r = subprocess.run([FF, "-hide_banner", "-i", video],
                       capture_output=True, text=True)
    for lin in r.stderr.splitlines():
        if "Duration:" in lin:
            h, m, s = lin.split("Duration:")[1].split(",")[0].strip().split(":")
            return int(h) * 3600 + int(m) * 60 + float(s)
    raise SystemExit("no pude leer la duración del video")

# ── dónde y cuándo pasa el trapero ──────────────────────────────────────
def pasadas(video, fps=24, ancho=160, alto=104):
    """Devuelve (t, pan, fuerza, largo) por cada pasada del mopa.

    Recorta la banda baja del cuadro —donde vive el mopa y nada más—, mide
    el centroide horizontal del movimiento cuadro a cuadro y corta en cada
    cambio de dirección. El sonido va en el pico de velocidad, que es donde
    el mopa realmente barre."""
    crudo = subprocess.run(
        [FF, "-hide_banner", "-loglevel", "error", "-i", video,
         "-vf", f"crop=iw:ih*0.36:0:ih*0.57,scale={ancho}:{alto},format=gray",
         "-f", "rawvideo", "-pix_fmt", "gray", "-"],
        capture_output=True).stdout
    f = np.frombuffer(crudo, np.uint8).reshape(-1, alto, ancho).astype(np.float32)
    d = np.abs(np.diff(f, axis=0)); d[d < 6] = 0
    xs = np.arange(ancho)
    cx = np.array([(dd.sum(0) * xs).sum() / max(dd.sum(), 1e-6) for dd in d])
    k = np.hanning(9); k /= k.sum()
    cx = np.convolve(cx, k, mode="same")
    v = np.gradient(cx)
    sig = np.sign(v)
    cortes = [0] + [i for i in range(1, len(sig))
                    if sig[i] != sig[i - 1] and abs(v[i - 1]) > .25] + [len(v)]
    out = []
    for a, b in zip(cortes, cortes[1:]):
        if b - a < 5:
            continue
        tramo = np.abs(v[a:b])
        if tramo.max() < .6:
            continue
        i = a + int(tramo.argmax())
        out.append((i / fps,                        # cuándo
                    (cx[i] / ancho - .5) * 1.1,     # dónde, para el paneo
                    min(tramo.max() / 5.0, 1.0),    # con cuánta fuerza
                    (b - a) / fps))                 # cuánto dura
    return out

# ── ladrillos de síntesis ───────────────────────────────────────────────
def lp(x, fc, orden=4):
    return sosfilt(butter(orden, fc / (SR / 2), "low", output="sos"), x)

def hp(x, fc, orden=2):
    return sosfilt(butter(orden, fc / (SR / 2), "high", output="sos"), x)

def ruido_rosa(n, rng):
    """Ruido blanco integrado a 1/f, que es como suena el aire de una sala."""
    b = rng.standard_normal(n)
    B = np.fft.rfft(b)
    f = np.arange(len(B)); f[0] = 1
    return np.fft.irfft(B / np.sqrt(f), n)

def cola(largo=1.15, rng=None):
    """Impulso de pasillo: ruido que decae exponencial, con predelay. Un
    pasillo de hospital es duro y alargado, así que la cola es larga y
    bastante apagada de agudos."""
    n = int(largo * SR)
    ir = rng.standard_normal(n) * np.exp(-np.linspace(0, 6.5, n))
    ir[:int(.012 * SR)] = 0
    ir = lp(ir, 3200)
    return ir / np.abs(ir).sum() * 0.9

def pip(f0, dur=.075, tau=.022):
    """El bip del QRS: fundamental con dos armónicos y caída exponencial."""
    t = np.arange(int(dur * SR)) / SR
    s = (np.sin(2 * np.pi * f0 * t) +
         .35 * np.sin(4 * np.pi * f0 * t) +
         .12 * np.sin(6 * np.pi * f0 * t))
    env = np.exp(-t / tau)
    env[:int(.002 * SR)] *= np.linspace(0, 1, int(.002 * SR))
    return s * env

def pulso(f0, dur=.17, subida=.045):
    """Pulso de alarma: sin click, con ataque y caída suaves — así son los
    tonos de la norma de alarmas médicas, no son bips secos."""
    t = np.arange(int(dur * SR)) / SR
    s = np.sin(2 * np.pi * f0 * t) + .3 * np.sin(4 * np.pi * f0 * t)
    env = np.ones_like(t)
    k = int(subida * SR)
    env[:k] = np.linspace(0, 1, k)
    env[-k:] = np.linspace(1, 0, k)
    return s * env ** 1.6

def poner(bus, x, t, gan=1.0, pan=0.0):
    """Suma x en el bus estéreo en el instante t, con paneo de potencia
    constante (si no, lo que va al centro suena más fuerte que lo demás)."""
    i = int(t * SR)
    if i >= bus.shape[1]:
        return
    x = x[:bus.shape[1] - i]
    ang = (np.clip(pan, -1, 1) + 1) * np.pi / 4
    bus[0, i:i + len(x)] += x * np.cos(ang) * gan * 1.414
    bus[1, i:i + len(x)] += x * np.sin(ang) * gan * 1.414

# ── la escena ───────────────────────────────────────────────────────────
def banda(dur, mopa, semilla=7):
    rng = np.random.default_rng(semilla)
    n = int(dur * SR)
    bus = np.zeros((2, n))
    ir = cola(rng=rng)

    # aire de la sala: clima + un zumbido bajo de la ventilación
    aire = lp(ruido_rosa(n, rng), 300) * 3.4
    t = np.arange(n) / SR
    aire += np.sin(2 * np.pi * 118 * t) * .006 + np.sin(2 * np.pi * 59 * t) * .004
    bus[0] += aire * .55; bus[1] += np.roll(aire, 313) * .55

    # dos monitores a distinto pulso: eso es lo que hace que una UCI suene a
    # UCI. Uno cerca a la izquierda, otro lejos y apagado a la derecha.
    seco = np.zeros((2, n))
    for bpm, f0, gan, pan in ((68, 880, .30, -.42), (84, 1046, .125, .34)):
        p = pip(f0)
        if pan > 0:
            p = lp(p, 2600)                       # el lejano llega sin filo
        k = 0
        while k * 60 / bpm < dur:
            poner(seco, p, k * 60 / bpm, gan, pan)
            k += 1

    # ventilador: un ciclo lento de aire cada cuatro segundos
    ciclo = 4.0
    largo = int(2.3 * SR)
    tt = np.linspace(0, 1, largo)
    env = np.where(tt < .5, np.sin(np.pi * tt) ** 2, np.sin(np.pi * tt) ** 3)
    resp = lp(hp(rng.standard_normal(largo), 260), 1500) * env * .11
    k = 0
    while .6 + k * ciclo < dur:
        poner(seco, resp, .6 + k * ciclo, 1.0, .22)
        k += 1

    # dos alarmas, las dos de otra sala: nadie corre en esta escena
    bomba = np.concatenate([np.concatenate([pulso(1180, .1, .02),
                                            np.zeros(int(.09 * SR))])
                            for _ in range(3)])
    poner(seco, lp(bomba, 2000) * .20, 2.15, 1.0, .48)

    aviso = np.concatenate([np.concatenate([pulso(f, .16, .04),
                                            np.zeros(int(.1 * SR))])
                            for f in (660, 660, 588)])
    poner(seco, lp(aviso, 1900) * .26, 5.30, 1.0, .40)

    # el trapero, calzado con la imagen
    for tp, pan, fuerza, largo_p in mopa:
        d = np.clip(largo_p * .55, .16, .42)
        m = int(d * SR)
        tt = np.linspace(0, 1, m)
        env = np.sin(np.pi * tt) ** 1.3
        sw = lp(hp(rng.standard_normal(m), 500), 3400) * env
        sw += lp(hp(rng.standard_normal(m), 1800), 5600) * env * .28   # agua
        poner(seco, sw * .055 * (.45 + .55 * fuerza), tp, 1.0, pan * .6)

    bus += seco
    # el pasillo: todo lo puntual se moja un poco, el aire ya venía difuso
    for c in (0, 1):
        bus[c] += fftconvolve(seco[c], ir)[:n] * .40

    bus = np.tanh(bus * 1.05) * .92
    k = int(.12 * SR); bus[:, :k] *= np.linspace(0, 1, k)
    k = int(.45 * SR); bus[:, -k:] *= np.linspace(1, 0, k)
    return (bus / max(np.abs(bus).max(), 1e-9) * .89).T


def main():
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    ent = sys.argv[1]
    sal = sys.argv[2] if len(sys.argv) > 2 else "portada-con-sonido.mp4"
    dur = duracion(ent)
    mopa = pasadas(ent)
    print(f"· {dur:.2f}s · {len(mopa)} pasadas del trapero detectadas")
    for tp, pan, fu, la in mopa:
        print(f"    {tp:5.2f}s  pan={pan:+.2f}  fuerza={fu:.2f}")
    x = banda(dur, mopa)
    with tempfile.TemporaryDirectory() as tmp:
        wav = os.path.join(tmp, "banda.wav")
        import wave
        with wave.open(wav, "wb") as w:
            w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
            w.writeframes((x * 32767).astype("<i2").tobytes())
        subprocess.run([FF, "-hide_banner", "-loglevel", "error", "-y",
                        "-i", ent, "-i", wav,
                        "-map", "0:v:0", "-map", "1:a:0",   # el audio viejo se cae acá
                        "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
                        "-shortest", sal], check=True)
    print(f"✔ {sal} ({os.path.getsize(sal)/1e6:.1f} MB) — sin música, con la unidad sonando")


if __name__ == "__main__":
    main()
