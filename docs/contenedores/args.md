---
status: new
date:
    created: 2025-09-23
    updated: 2025-09-23
---


# Argumentos de construcción


Dentro del Dockerfile
se permite pasar argumentos
para modificar los parámetros
de construcción de las imágenes.
Estos argumentos son borrados
cuando la construcción está completada.


## Creación

La cláusula reservada
para crear los argumentos de imagen es `ARG`.
Tras ella se define el nombre de argumento
y se le asigna un valor:

```Dockerfile title="Dockerfile - Argumentos"
ARG ARGUMENTO=valor_default
```

Un uso habitual
es la elección de la versión
de una imagen de referencia.
Por ejemplo se puede definir 
el argumento `TAG_IMAGEN`
para elegir el *tag* de la versión de Python:

```Dockerfile title="Dockerfile - Tags como argumentos"
# definicion de argumento
ARG TAG_IMAGEN=3.13-alpine3.21
# asignacion como default
FROM python:${TAG_IMAGEN}
```

entonces la versión elegida
para la contrucción de la imagen final
será el intérprete 3.13
instalada en Alpine Linux
salvo indicación contraria.


## Modificación

Con el pàrámetro
`args` del campo `build`
se elige un nuevo valor
para el arguimento.

La asignación
se puede hacer
por mapeo:

```yaml title="compose.yml - Argumentos" hl_lines="6-7"
services:

  contenedor: 
    build:
      context: .    # ruta al Dockerfile
      args:
        ARGUMENTO: valor_custom
```

La asignación
se puede hacer
también como lista:

```yaml title="compose.yml - Argumentos" hl_lines="6-7"
services:

  contenedor: 
    build:
      context: .    # ruta al Dockerfile
      args:
        - ARGUMENTO=valor_custom
```

En ambos casos se necesita indicar
la ruta al Dockerfile
con el campo `context`.

Retomando el ejemplo previo,
para elegir como referencia
la imagen reducida de Python 3.13
instalada en Debian Trixie:

```yaml title="compose.yml - Tag como argumento"
services:

  contenedor_python: 
    build:
      context: .    # ruta al Dockerfile
      args:
        TAG_IMAGEN: 3.13-slim-trixie
```



## Asignación desde terminal


El valor del argumento
se puede pasar durante el despliegue
con el comando `compose`
con ayuda de la opción `build-arg`:

```bash title="Despliegue - Tag desde shell"
podman compose up --build  --build-arg TAG_IMAGEN=3.13.1-slim-bookworm
```

