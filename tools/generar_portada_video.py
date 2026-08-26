#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Convierte el clip crudo que sale de Flow en el fondo de la pantalla de
inicio: bucle de ida y vuelta, banda de sonido de la unidad y cuadro fijo
de respaldo.

    python3 tools/generar_portada_video.py clip-de-flow.mp4

Escribe arte/portada/portada.mp4 y arte/portada/portada.jpg.

Tres cosas que hace y por qué:

· IDA Y VUELTA. El clip de Flow no cierra el ciclo — entre el último cuadro
  y el primero saltan casi la mitad de los píxeles, así que en `loop` se
  vería un corte cada vuelta. Al pegarle su propio reverso el empalme es
  exacto, y a un tipo trapeando el movimiento al revés le calza.

· PESO. Flow entrega 1080x1920 a 9 Mbps. Eso son 9 MB por ocho segundos, y
  este archivo se embebe en base64 en el artifact y se precachea en la PWA.
  A 720x1280 con CRF 30 el dibujo plano no pierde nada visible y baja a
  menos de 2 MB.

· CUADRO FIJO. Va como `poster` del video y como fondo cuando el teléfono
  pide menos animación (prefers-reduced-motion) o cuando el video no carga.
"""
import os, subprocess, sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, "tools"))
import sonido_portada as sp                                   # noqa: E402

ANCHO, ALTO, CRF = 720, 1280, 30
DESTINO = os.path.join(RAIZ, "arte", "portada")


def main():
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    ent = sys.argv[1]
    os.makedirs(DESTINO, exist_ok=True)
    mudo = os.path.join(DESTINO, ".mudo.mp4")
    mp4 = os.path.join(DESTINO, "portada.mp4")
    jpg = os.path.join(DESTINO, "portada.jpg")

    print("· ida y vuelta")
    subprocess.run([
        sp.FF, "-hide_banner", "-loglevel", "error", "-y", "-i", ent,
        "-filter_complex",
        f"[0:v]scale={ANCHO}:{ALTO},fps=24,split[a][b];"
        "[b]reverse,trim=start_frame=1,setpts=PTS-STARTPTS[r];"
        "[a][r]concat=n=2:v=1,fps=24[v]",
        "-map", "[v]", "-an", "-r", "24", "-c:v", "libx264",
        "-preset", "veryslow", "-crf", str(CRF), "-pix_fmt", "yuv420p",
        "-profile:v", "main", mudo], check=True)

    print("· banda de sonido")
    dur = sp.duracion(mudo)
    mopa = sp.pasadas(mudo)
    print(f"  {dur:.2f}s · {len(mopa)} pasadas del trapero")
    x = sp.banda(dur, mopa, bucle=True)
    import tempfile, wave
    with tempfile.TemporaryDirectory() as tmp:
        wav = os.path.join(tmp, "b.wav")
        with wave.open(wav, "wb") as w:
            w.setnchannels(2); w.setsampwidth(2); w.setframerate(sp.SR)
            w.writeframes((x * 32767).astype("<i2").tobytes())
        subprocess.run([
            sp.FF, "-hide_banner", "-loglevel", "error", "-y",
            "-i", mudo, "-i", wav, "-map", "0:v:0", "-map", "1:a:0",
            "-c:v", "copy", "-c:a", "aac", "-b:a", "128k",
            "-movflags", "+faststart", "-shortest", mp4], check=True)

    print("· cuadro fijo")
    subprocess.run([
        sp.FF, "-hide_banner", "-loglevel", "error", "-y", "-i", mudo,
        "-frames:v", "1", "-q:v", "4", jpg], check=True)
    os.remove(mudo)

    for f in (mp4, jpg):
        print(f"✔ {os.path.relpath(f, RAIZ)} ({os.path.getsize(f)/1024:.0f} KB)")


if __name__ == "__main__":
    main()
