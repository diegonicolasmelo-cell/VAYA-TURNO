#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Convierte el clip crudo del generador en el fondo de la pantalla de
inicio: bucle sin costura, su propio audio y cuadro fijo de respaldo.

    python3 tools/generar_portada_video.py clip-crudo.mp4

Escribe arte/portada/portada.mp4 y arte/portada/portada.jpg.

Tres cosas que hace y por qué:

· EL BUCLE, POR DISOLVENCIA. Hasta la v0.57 el clip se cerraba pegándole su
  propio reverso: ida y vuelta, empalme exacto, y a un tipo trapeando el
  movimiento al revés le calzaba. Pero el clip trae música —125 pulsos por
  minuto, que es justo el ritmo de unas compresiones— y la música al revés
  se nota a la primera. Así que el ciclo se cierra de la otra forma: la
  cola se disuelve sobre la cabeza. Se pierde medio segundo de clip y se
  gana un bucle que suena hacia adelante. En una cámara fija y un dibujo
  plano la disolvencia es casi invisible; la música al revés no lo era.

· EL AUDIO ES EL DEL CLIP. Antes se le sintetizaba una banda de unidad
  —monitores, alarmas, el trapero— con tools/sonido_portada.py, porque el
  clip venía mudo o con música de relleno. El clip nuevo trae la suya y es
  la que el autor quiere, así que entra tal cual y la banda sintética sale.
  El módulo sonido_portada.py se queda en el repo: no cuesta nada y sirve
  si algún día vuelve a llegar un clip mudo.

· PESO. El generador entrega 1080x1920 a 10 Mbps. A 720x1280 con CRF 30 el
  dibujo plano no pierde nada visible, y sin la vuelta atrás el archivo es
  la mitad del de antes: este clip se embebe en base64 en el artefacto y se
  precachea entero en la app instalable.

Y el cuadro fijo va como `poster` del video y como fondo cuando el teléfono
pide menos animación (prefers-reduced-motion) o cuando el video no carga.
"""
import os, subprocess, sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ANCHO, ALTO, CRF = 720, 1280, 30
CRUCE = 0.5          # segundos de disolvencia entre la cola y la cabeza
DESTINO = os.path.join(RAIZ, "arte", "portada")


def ffmpeg():
    r = subprocess.run(["which", "ffmpeg"], capture_output=True, text=True)
    if r.returncode == 0:
        return r.stdout.strip()
    import imageio_ffmpeg
    return imageio_ffmpeg.get_ffmpeg_exe()


FF = ffmpeg()


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


def main():
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    ent = sys.argv[1]
    os.makedirs(DESTINO, exist_ok=True)
    mp4 = os.path.join(DESTINO, "portada.mp4")
    jpg = os.path.join(DESTINO, "portada.jpg")

    dur = duracion(ent)
    con_audio = tiene_audio(ent)
    L = CRUCE
    if dur <= 3 * L:
        raise SystemExit(f"el clip dura {dur:.1f}s: muy corto para cerrarlo")
    fin = dur - L                       # el ciclo resultante dura `fin`
    print(f"· {dur:.2f}s de origen · audio {'sí' if con_audio else 'no'}"
          f" · bucle de {fin:.2f}s con {L:.2f}s de disolvencia")

    # La cola se disuelve sobre la cabeza y el resto va detrás sin tocar:
    #   [cola × cabeza]  +  [medio]   =  dur − L
    # La cabeza entra con alfa sobre la cola: `xfade` no sirve aquí porque
    # necesita que su primera entrada dure más que offset+duration, y la
    # cola mide exactamente la disolvencia. Con overlay y un fade de alfa
    # el resultado es el mismo y no depende de esa condición.
    filtro = (
        f"[0:v]scale={ANCHO}:{ALTO},fps=24,split=3[v1][v2][v3];"
        f"[v1]trim=0:{L},setpts=PTS-STARTPTS,format=yuva420p,"
        f"fade=t=in:st=0:d={L}:alpha=1[cabeza];"
        f"[v2]trim={L}:{fin},setpts=PTS-STARTPTS[medio];"
        f"[v3]trim={fin}:{dur},setpts=PTS-STARTPTS[cola];"
        f"[cola][cabeza]overlay=shortest=1,format=yuv420p[union];"
        f"[union][medio]concat=n=2:v=1:a=0,fps=24[v]"
    )
    orden = [FF, "-hide_banner", "-loglevel", "error", "-y", "-i", ent]

    if con_audio:
        # Mismo corte para el audio, y por la misma razón: `acrossfade`
        # devolvía cero muestras con entradas de la largura justa. Dos
        # rampas complementarias sumadas SIN normalizar son un crossfade.
        # El aformat de entrada no sobra: sin él el concat no arranca.
        filtro += (
            f";[0:a]aformat=sample_fmts=fltp:sample_rates=48000:"
            f"channel_layouts=stereo,asplit=3[a1][a2][a3];"
            f"[a1]atrim=0:{L},asetpts=PTS-STARTPTS,"
            f"afade=t=in:st=0:d={L}:curve=tri[acabeza];"
            f"[a2]atrim={L}:{fin},asetpts=PTS-STARTPTS[amedio];"
            f"[a3]atrim={fin}:{dur},asetpts=PTS-STARTPTS,"
            f"afade=t=out:st=0:d={L}:curve=tri[acola];"
            f"[acabeza][acola]amix=inputs=2:normalize=0:duration=longest[aunion];"
            f"[aunion][amedio]concat=n=2:v=0:a=1[a]"
        )
        orden += ["-filter_complex", filtro, "-map", "[v]", "-map", "[a]",
                  "-c:a", "aac", "-b:a", "128k", "-ar", "48000"]
    else:
        orden += ["-filter_complex", filtro, "-map", "[v]", "-an"]

    orden += ["-r", "24", "-c:v", "libx264", "-preset", "veryslow",
              "-crf", str(CRF), "-pix_fmt", "yuv420p", "-profile:v", "main",
              "-movflags", "+faststart", mp4]
    print("· codificando")
    subprocess.run(orden, check=True)

    print("· cuadro fijo")
    subprocess.run([
        FF, "-hide_banner", "-loglevel", "error", "-y", "-i", mp4,
        "-frames:v", "1", "-q:v", "4", jpg], check=True)

    for f in (mp4, jpg):
        print(f"✔ {os.path.relpath(f, RAIZ)} ({os.path.getsize(f)/1024:.0f} KB)")


if __name__ == "__main__":
    main()
