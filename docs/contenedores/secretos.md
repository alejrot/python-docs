---
status: deprecated
date:
    created: 2025-07-01
    updated: 2025-08-26
---

# Secrets


Los secretos son elementos auxiliares creados
para cargar información sensible a los contenedores
que la necesiten.


## Uso en Compose

### Definición

Los *secrets* tienen su propia sección
dentro del archivo Compose:

```yaml title="compose.yml - Sección de secretos" 
# archivo 'compose.yml'
secrets:
  secreto-servicio:
    file: ./secreto-archivo.txt 
```

El archivo puede estar guardado
en la carpeta personal
del usuario,
en tal caso su ruta se suele indicar
con la variable `HOME`:

```yaml title="compose.yml - Sección de secretos" 
# archivo 'compose.yml'
secrets:
  secreto-servicio:
    file: $HOME/secreto-archivo.txt 
```

!!! warning "Secretos externos"

    Algunas implementaciones del comando Compose
    no admiten la especificación de secretos externos.


### Asignación

Sólo aquellos contenedores
a los que se les dé acceso explícito
a los secretos
podrán leer los datos guardados en ellos.
El acceso a los secretos
se asigna mediante listas
con el campo `secrets`:


```yaml title="compose.yml - Asignación de secretos" hl_lines="6-7"
# archivo 'compose.yml'
services:

  servicio:
    build: .
    secrets:
      - secreto-servicio

secrets:
  secreto-servicio:
    file: ./secreto-archivo.txt
```

### Ruta interna

Los secretos se montan como archivos
que el contenedor
encontrará dentro de la ruta `/run/secrets`.
El contenedor necesita conocer de antemano
el nombre o ruta del secreto
para poder leerlo.
Esto se soluciona en muchas imágenes
creando una variable de entorno
a la cual se le asigna la ruta del secreto:

```yaml title="compose.yml - Ruta en variables de entorno" hl_lines="5-6"
# archivo 'compose.yml'
services:

  servicio:
    build: .
    environment:
      RUTA_SECRETO: /run/secrets/secreto-servicio
    secrets:
      - secreto-servicio

secrets:
  secreto-servicio:
    file: ./secreto-archivo.txt
```

## Lectura

Los programas de Python
que tengan un secreto montado
podrán leer sus archivos 
como lo hacen con cualquier archivo normal.


```py title="Secretos - Lectura en Python"
ruta_secreto = "/run/secrets/secreto-servicio"

with open(ruta_secreto, "r",encoding="utf-8") as archivo:
    data = archivo.read()
    logging.info("Valor leído: '%s'", data)
``` 


Es una práctica habitual
indicar la ruta a dicho secreto
mediante una variable de entorno:


```py title="Secretos - Lectura en Python (ruta en variable de entorno)"
import os

ruta_secreto = os.getenv("RUTA_SECRETO")

with open(ruta_secreto, "r",encoding="utf-8") as archivo:
    data = archivo.read()
    logging.info("Valor leído: '%s'", data)
``` 





## Ejemplo

Se crea un demo sencillo
que lee un secreto guardado en archivo TXT
y lo muestra en la ventana de *logs*.


```bash title="Demo secretos - árbol de archivos"
.
├── compose.yml
├── demo
│   └── main.py
├── Dockerfile
└── secreto-archivo.t
```

```py title="Demo secretos - rutina en Python"
import logging
import os

logging.basicConfig(
    level=logging.INFO, # mínimo nivel de log a publicar
    format="%(message)s", #info incorporada
    )

ruta_secreto = os.getenv("RUTA_SECRETO")

logging.info("Secretos - desde archivo")
logging.info("Ruta interna: '%s'", ruta_secreto)

with open(ruta_secreto, "r",encoding="utf-8") as archivo:
    data = archivo.read()
    logging.info("Valor leído: '%s'", data)
    
logging.info("Finalizado")
``` 

```dockerfile title="Demo secretos - Dockerfile"
# imagen de referencia
FROM python:alpine

# directorio de trabajo (se crea automáticamente)
WORKDIR /code

# copia de rutinas al directorio de trabajo
COPY demo/ ./

# comandos 
CMD ["python", "main.py"]
```


```yml  title="Demo secretos - compose.yml"
name: demo_secretos

services:

  secreto:
    build: .
    image: demo_secretos
    environment:
      RUTA_SECRETO: /run/secrets/secreto-servicio
    secrets:
      - secreto-servicio


secrets:
  secreto-servicio:
    file: ./secreto-archivo.tx
```


El valor secreto
elegido como ejemplo es:

```txt title="Demo secretos - secreto-archivo.txt"
(No se lo digas a nadie)
```

## Referencias


[DockerHub - Manage secrets securely in Docker Compose](https://docs.docker.com/compose/how-tos/use-secrets/)