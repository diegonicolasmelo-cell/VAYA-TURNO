#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Convierte el clip crudo del generador en el fondo de la pantalla de
inicio: bucle de ida y vuelta, su propio audio y cuadro fijo de respaldo.

    python3 tools/generar_portada_video.py clip-crudo.mp4

Escribe arte/portada/portada.mp4 y arte/portada/portada.jpg.

Cuatro cosas que hace y por qué:

· IDA Y VUELTA. El clip no cierra el ciclo solo: entre el último cuadro y
  el primero saltan casi la mitad de los píxeles, y en `loop` se vería un
  corte cada vuelta. Pegándole su propio reverso el empalme es exacto por
  los dos lados —el último cuadro con el último y el primero con el
  primero— y a un tipo trapeando el movimiento al revés le calza.

· PERO EL AUDIO NO SE DEVUELVE. El clip trae música, y son 125 pulsos por
  minuto —el ritmo de unas compresiones, que es el chiste—. Al revés se
  nota a la primera. Así que la imagen va y vuelve mientras el audio corre
  siempre hacia adelante: se repite el original tantas veces como haga
  falta para cubrir el ciclo, con una disolvencia corta en cada empalme Y
  en el cierre del bucle, de modo que al volver a empezar tampoco salta.
  Eso se hace en numpy y no con `acrossfade`, que devuelve cero muestras
  con entradas de esta largura y falla con un error que no apunta a nada.

· PESO. El generador entrega 1080x1920 a 10 Mbps. A 720x1280 con CRF 30 el
  dibujo plano no pierde nada visible: este clip se embebe en base64 en el
  artefacto y se precachea entero en la app instalable.

· CUADRO FIJO. Va como `poster` del video y como fondo cuando el teléfono
  pide menos animación (prefers-reduced-motion) o cuando el video no carga.

La banda de sonido sintética de tools/sonido_portada.py ya no se usa —el
clip trae la suya—, pero el módulo se queda en el repo por si algún día
vuelve a llegar un clip mudo.
"""
import os, subprocess, sys, tempfile, wave
import numpy as np

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ANCHO, ALTO, CRF = 720, 1280, 30
SR = 48000
CRUCE = 0.45         # segundos de disolvencia en cada empalme del audio
APLANAR = True       # nivelar el crescendo del clip (ver aplanar())
VENTANA = 1.6        # segundos de la ventana con que se mide ese nivel
DESTINO = os.path.join(RAIZ, "arte", "portada")


def ffmpeg():
    r = subprocess.run(["which", "ffmpeg"], capture_output=True, text=True)
    if r.returncode == 0:
        return r.stdout.strip()
    import imageio_ffmpeg
    return imageio_ffmpeg.get_ffmpeg_exe()


FF = ffmpeg()


def correr(orden):
    subprocess.run([FF, "-hide_banner", "-loglevel", "error", "-y"] + orden,
                   check=True)


def duracion(video):
    r = subprocess.run([FF, "-hide_banner", "-i", video],
                       capture_output=True, text=True)
    for linea in r.stderr.splitlines():
        if "Duration:" in linea:
            h, m, s = linea.split("Duration:")[1].split(",")[0].strip().split(":")
            return int(h) * 3600 + int(m) * 60 + float(s)
    raise SystemExit("no pude leer la duración del clip")


def tiene_audio(video):
    r = subprocess.run([FF, "-hide_banner", "-i", video],
                       capture_output=True, text=True)
    return "Audio:" in r.stderr


def leer_wav(ruta):
    with wave.open(ruta, "rb") as w:
        n, canales = w.getnframes(), w.getnchannels()
        x = np.frombuffer(w.readframes(n), dtype="<i2").astype(np.float32) / 32768
    return x.reshape(-1, canales)


def escribir_wav(ruta, x):
    with wave.open(ruta, "wb") as w:
        w.setnchannels(x.shape[1]); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((np.clip(x, -1, 1) * 32767).astype("<i2").tobytes())


def aplanar(a, ventana):
    """El clip arranca bajito y termina fuerte: es un crescendo de ocho
    segundos. En bucle eso se oye como un vaivén —crece, vuelve a empezar,
    baja— y ninguna disolvencia lo arregla, porque una disolvencia mezcla,
    no inventa el crescendo que falta. Así que se nivela: se mide el nivel
    con una ventana larga (1,6 s, mucho más que un compás a 125, para no
    tocar el pulso) y se divide por él. La ganancia va acotada para que no
    bombee ni levante el silencio. Con APLANAR = False se deja el clip como
    viene."""
    n = int(ventana * SR)
    mono = a.mean(axis=1)
    # RMS corrido, por suma acumulada: rápido y sin dependencias
    pot = np.concatenate([[0.0], np.cumsum(mono.astype(np.float64) ** 2)])
    i = np.arange(len(mono))
    lo = np.maximum(0, i - n // 2)
    hi = np.minimum(len(mono), i + n // 2)
    rms = np.sqrt((pot[hi] - pot[lo]) / np.maximum(1, hi - lo))
    objetivo = float(np.median(rms[rms > 0])) or 1.0
    g = np.clip(objetivo / np.maximum(rms, 1e-5), 0.45, 2.2).astype(np.float32)
    return a * g[:, None]


def bed(a, total, cruce):
    """El audio original repetido hasta cubrir `total` muestras, con una
    disolvencia de `cruce` en cada empalme y otra que envuelve el final
    sobre el principio: así el bucle cierra sin salto de nivel."""
    L = int(cruce)
    if len(a) <= 2 * L:
        raise SystemExit("el audio del clip es más corto que dos disolvencias")
    rampa = np.linspace(0, 1, L, dtype=np.float32)[:, None]
    y = a.copy()
    while len(y) < total + L:
        # la cola de lo que llevamos se disuelve con la cabeza de otra copia
        y = np.concatenate([y[:-L],
                            y[-L:] * (1 - rampa) + a[:L] * rampa,
                            a[L:]])
    fuera = y[:total].copy()
    # y el cierre: la cabeza recibe lo que habría sonado justo después
    fuera[:L] = y[total:total + L] * (1 - rampa) + fuera[:L] * rampa
    return fuera


def main():
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    ent = sys.argv[1]
    os.makedirs(DESTINO, exist_ok=True)
    mp4 = os.path.join(DESTINO, "portada.mp4")
    jpg = os.path.join(DESTINO, "portada.jpg")

    dur = duracion(ent)
    con_audio = tiene_audio(ent)
    print(f"· {dur:.2f}s de origen · audio {'sí' if con_audio else 'no'}")

    with tempfile.TemporaryDirectory() as tmp:
        mudo = os.path.join(tmp, "mudo.mp4")
        print("· ida y vuelta")
        # trim=start_frame=1 en el reverso quita el cuadro repetido de la
        # bisagra; el del cierre del bucle se repite a propósito, que es lo
        # que hace que la vuelta empalme exacta
        correr(["-i", ent, "-filter_complex",
                f"[0:v]scale={ANCHO}:{ALTO},fps=24,split[a][b];"
                "[b]reverse,trim=start_frame=1,setpts=PTS-STARTPTS[r];"
                "[a][r]concat=n=2:v=1,fps=24[v]",
                "-map", "[v]", "-an", "-r", "24", "-c:v", "libx264",
                "-preset", "veryslow", "-crf", str(CRF),
                "-pix_fmt", "yuv420p", "-profile:v", "main", mudo])
        ciclo = duracion(mudo)

        if not con_audio:
            print(f"  {ciclo:.2f}s, sin pista de audio")
            correr(["-i", mudo, "-c:v", "copy", "-movflags", "+faststart", mp4])
        else:
            print("· el audio, siempre hacia adelante")
            wav_ent = os.path.join(tmp, "orig.wav")
            correr(["-i", ent, "-vn", "-ac", "2", "-ar", str(SR),
                    "-c:a", "pcm_s16le", wav_ent])
            a = leer_wav(wav_ent)
            if APLANAR:
                antes = float(np.sqrt((a[:SR] ** 2).mean()))
                a = aplanar(a, VENTANA)
                despues = float(np.sqrt((a[:SR] ** 2).mean()))
                print(f"  nivelado: el primer segundo sube de {antes:.3f}"
                      f" a {despues:.3f} de RMS")
            total = int(round(ciclo * SR))
            x = bed(a, total, CRUCE * SR)
            vueltas = total / len(a)
            print(f"  ciclo de {ciclo:.2f}s · {vueltas:.2f} pasadas del original"
                  f" · {CRUCE:.2f}s de disolvencia en cada empalme")
            wav_sal = os.path.join(tmp, "bed.wav")
            escribir_wav(wav_sal, x)
            correr(["-i", mudo, "-i", wav_sal, "-map", "0:v:0", "-map", "1:a:0",
                    "-c:v", "copy", "-c:a", "aac", "-b:a", "128k",
                    "-movflags", "+faststart", "-shortest", mp4])

    print("· cuadro fijo")
    correr(["-i", mp4, "-frames:v", "1", "-q:v", "4", jpg])

    for f in (mp4, jpg):
        print(f"✔ {os.path.relpath(f, RAIZ)} ({os.path.getsize(f)/1024:.0f} KB)")


if __name__ == "__main__":
    main()
