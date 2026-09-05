# El sonido de la unidad

Aquí vive el **ambiente de fondo de la UCI**: la grabación que suena
bajito, en bucle, mientras hay guardia abierta — ventilación mecánica,
monitores, la unidad respirando.

## El contrato, en una línea

> **Un archivo llamado `ambiente.mp3` (u `.ogg`, `.m4a`, `.wav`) en esta
> carpeta, que sea una grabación REAL con licencia libre.**

Con eso `generar_app.py` lo incrusta solo, el Panel de guardia gana el
interruptor «🫁 Sonido de la unidad» (apagado por defecto, recordado por
teléfono), y la app lo repite en bucle a volumen 0,35 mientras la guardia
esté abierta. Sin archivo: ni interruptor ni sonido. **La app no trae un
ambiente sintético a propósito** — o suena una UCI de verdad, o no suena
nada.

## De dónde sacarlo (sin pagar y sin pisar a nadie)

La regla: **grabación real, licencia CC0 o dominio público** (no pide
atribución y sirve aunque el juego algún día se venda). Si es CC-BY,
también sirve — pero hay que anotar el crédito aquí abajo.

1. **freesound.org** — buscar `mechanical ventilator`, `ICU ambience`,
   `hospital room tone`, `ventilator breathing`. En los filtros de la
   izquierda marcar **License → Creative Commons 0**. Bajar el MP3 de
   vista previa ya sirve (128 kbps, liviano).
2. **bigsoundbank.com** — banco francés, todo gratis incluso para uso
   comercial. Buscar `hospital`, `respirateur`.
3. **Wikimedia Commons** — commons.wikimedia.org, buscar
   `ventilator sound` o la categoría *Audio files of medical equipment*;
   revisar la licencia de cada archivo en su página.

Qué buscar al oído: un ciclo respiratorio de máquina claro (inspiración /
pausa / espiración), monitores lejanos, **sin voces** (una voz en bucle
se nota a la segunda vuelta) y **sin alarmas fuertes** (una alarma
repetida cada 40 s es tortura, no ambiente).

## Formato

- **Duración: 30 a 90 segundos.** Más corto se nota el ciclo; más largo
  pesa de más.
- **Que cierre en bucle**: el final tiene que empalmar con el principio
  sin clic. Si la fuente no cierra, un fundido cruzado de ~0,5 s en
  cualquier editor (Audacity) lo arregla.
- **Peso: bajo 1 MB.** MP3 mono 96–128 kbps sobra para un fondo a
  volumen 0,35. El artefacto entero tiene tope de 16 MB y hoy va en ~6.
- Nombre exacto: `ambiente.mp3` (o la extensión que sea, pero la base
  `ambiente`).

## Cómo entra

Como el arte: se deja el archivo en la carpeta de Drive
**«Vaya turno Claude»** (o directo aquí) y se corre:

    python3 tools/ingresar_sonido.py ~/bajadas/icu-ambience.mp3

El guion lo copia aquí con el nombre que toca, avisa si pesa de más y
recuerda reconstruir la app.

## Créditos

| archivo | fuente | autor | licencia |
|---|---|---|---|
| _(vacío — todavía no hay grabación)_ | | | |

## Por qué no vino ya puesto

Se intentó traer la grabación desde este entorno y la red del sandbox
solo alcanza GitHub y los registros de paquetes: freesound, archive.org,
Wikimedia y los demás bancos de sonido están bloqueados. Lo que sí había
al alcance (packs CC0 de efectos de juego) era sintetizado o sin licencia
clara por archivo, y este juego merece una UCI de verdad. Queda la
ranura lista y este manual de dos minutos.
