# ffmpeg-python

ffmpeg-python es un ***wrapper*** (un conector) para interactuar con el utilitario FFMPEG, el cual permite manipular video, audio e imágenes.

[GitHub del proyecto](https://github.com/kkroening/ffmpeg-python)

[Documentación del proyecto](https://kkroening.github.io/ffmpeg-python/)


## Instalar 

Se necesita instalar el utilitario en el sistema operativo:

[Descargar FFmpeg](https://www.ffmpeg.org/download.html)

El wrapper (conector) para Python se instala mediante PIP
```bash
pip install ffmpeg-python
```

## Importar

```python
import ffmpeg
```


## Ejemplos de uso

### Cortar clip (*trim*)

```py
# REVISAR: IMAGEN CONGELADA AL COMIENZO
import ffmpeg

ruta_entrada = "demo.mp4"
ruta_salida = "clip.mp4"

video = ffmpeg.input(ruta_entrada)
video = video.trim(start=20, duration=5)  # MAL
video =  ffmpeg.output(video, ruta_salida) 

ffmpeg.run(video)
```

 
Otra alternativa:
```py
# ...
# tiempo en segundos
inicio = 10
fin = 20

video = ffmpeg.input(ruta_entrada, ss=inicio, to=fin) 
video =  ffmpeg.output(video, ruta_salida) 
ffmpeg.run(video)
```
**ss** es el tiempo de arranque, en tanto que **to** es el tiempo de parada.


Notación reducida:

```py
# ...
# tiempo en segundos
inicio = 10 
fin = 20
(
    ffmpeg.input(ruta_entrada,ss=inicio, to=fin) 
    .output( ruta_salida) 
    .run()
)
```

### Dimensiones

```py
import ffmpeg

ruta_entrada = "demo.mp4"

probe = ffmpeg.probe(ruta_entrada)

video = next(
    (stream for stream in probe["streams"] if stream["codec_type"] == "video"), None
)

ancho = int( video["width"])
alto = int(video["height"])
```

### Miniatura 


```py
import ffmpeg

ruta_entrada = "demo.mp4"

# Ejemplo 1: PNG con anchura 500 px
salida_png = "miniatura.png"

instante = 4  # segundo 4
ancho = 500  # 500 px
alto = -1  # automatico 

video = ffmpeg.input(ruta_entrada, ss=instante)
video = video.filter("scale", ancho, alto) # (mantiene proporcion)
video = ffmpeg.output(video, salida_png , vframes=1)

# orden de ejecucion
ffmpeg.run(video)
```

### Invertir imagen (*flip*)

```py
import ffmpeg

ruta_entrada = "demo.mp4"
salida_horizontal = "horizontal.mp4"
salida_vertical = "vertical.mp4"
```

Volteo horizontal

```py
# 'hflip': voltea de derecha a izquierda
video = ffmpeg.input(ruta_entrada)
video = ffmpeg.hflip(video)
video = ffmpeg.output(video, salida_horizontal)
# orden de ejecucion
ffmpeg.run(video)
```

Volteo vertical:

```py
# 'vflip' : voltea de arriba a abajo
video = ffmpeg.input(ruta_entrada)
video = ffmpeg.vflip(video)
video = ffmpeg.output(video, salida_vertical)
# orden de ejecucion
ffmpeg.run(video)
```

### Convertir Video

```py
import ffmpeg

ruta_entrada = "demo.mp4"
ruta_salida  = "demo.wmv"

(
	ffmpeg.input(ruta_entrada)
	.output(ruta_salida)
	.run()
)
```

### Extraer Audio

```py
import ffmpeg

ruta_entrada = "demo.mp4"
audio_salida = "audio.mp3"

(
	ffmpeg.input(ruta_entrada)
	.output(audio_salida)
	# .output(audio_salida , acodec='libshine') # codec personalizado
	.run()
)
```

### Extraer frames (imagenes del video)

- Número fijo de frames, desde el comienzo del video:

```py 
import ffmpeg

ruta_entrada = "demo.mp4"
frames_salida = "frame_%d.png" # formato para nombrar los frames de salida

nro_frames = 500 # primeros 500 frames de video

(
	ffmpeg.input(ruta_entrada)
	.output(frames_salida , vframes=nro_frames)      
	.run()
)
```

- Tasa de frames por segundo a elección, desde el comienzo:

```py 
import ffmpeg

ruta_entrada  = "demo.mp4"
frames_salida = "frame_%d.png" # formato para nombrar los frames de salida

fps = 0.1  # 1 frame cada 10 segundos

(
	ffmpeg.input(ruta_entrada)
	.output(frames_salida , vf=f'fps={fps}')
	.run()
)
```

### Thumbnails


- Una captura, tiempo elegido por usuario:

```py 
import ffmpeg

ruta_entrada  = "demo.mp4"
thumbnail_salida = "thumbnail.png" 
## instante fijo  
(
	ffmpeg.input(ruta_entrada, ss="00:00:15")
	.output(thumbnail_salida, vframes=1)
	.run()
)
```

- Una captura, elegida automáticamente entre los 100 primeros frames (valor predefinido):

```py 
import ffmpeg

ruta_entrada  = "demo.mp4"
thumbnail_salida = "thumbnail.png" 
# ventana seleccion 100 muestras (default)   
(
	ffmpeg.input(ruta_entrada)
	.filter('thumbnail')
	.output(thumbnail_salida, vframes=1)
	.run()
)
```

- Una captura, elegida automáticamente entre los N primeros frames:

```py 
import ffmpeg

ruta_entrada  = "demo.mp4"
thumbnail_salida = "thumbnail.png" 
nro_frames = 500
# ventana seleccion 500 muestras  
(
	ffmpeg.input(ruta_entrada)
	.filter('thumbnail', n=nro_frames)
	.output(thumbnail_salida, vframes=1)
	.run()
)
```


## Referencias

[DelfStack - FFmpeg en script Python](https://www.delftstack.com/es/howto/python/ffmpeg-python/)

[Bannerbear - How to Use FFMpeg in Python (with Examples)](https://www.bannerbear.com/blog/how-to-use-ffmpeg-in-python-with-examples/)