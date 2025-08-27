---
status: deprecated
date:
    created: 2025-07-01
    updated: 2025-08-26
---

# Volumenes

Los volumenes son almacenamientos persistentes
ubicados en el sistema anfitrión
a los cuales los contenedores tienen acceso.
Son necesarios para prevenir
la pérdida de los datos internos de los contenedores
cada vez que éstos son borrados o recreados.

Algunos usos habituales:

- bases de datos;
- archivos de los usuarios;
- reportes de funcionamiento;
- etc.


## Archivos en Python

A continuación se repasan algunos mecanismos disponibles de Python para manejar archivos y carpetas.


### Apertura de archivos

Dentro de los contenedores se puede
crear, leer, modificar y borrar archivos y carpetas
con ayuda de la [función `open()`](../archivos/archivos.md)
como también con las funciones dedicadas
que proporcionan los módulos `os`, `pathlib`, entre otros.
Lo mismo sucede con aquellos recursos ubicados en volumenes
a los cuales el contenedor tenga acceso.

Algunas funciones útiles del módulo `pathlib`: [alteración de recursos](../pathlib/alteracion.md)




### Logging en archivo


Los logs se pueden guardar en archivo 
al tiempo que se muestran en consola.
La configuración se realiza fácilmente
con ayuda de las funciones
`StreamHandler()` y`FileHandler()` del módulo `logging`
tal como se muestra a continuación:


``` py title="logging en archivo" hl_lines="10-15"
import logging

logging.basicConfig(
    level=logging.INFO, # mínimo nivel de log a publicar
    format="%(asctime)s - %(levelname)s - %(message)s", #info incorporada
    handlers=[
        # salida por consola
        logging.StreamHandler(), 
        # salida por archivo
        logging.FileHandler(
            filename=ruta_archivo,
            mode="a",             # agregado ('append')
            encoding="utf-8",
            delay=True,
            ),
        ],
    )
```

## Usuario *"root"*


El usuario predeterminado dentro del contenedor es `root`,
en analogía con el usuario *root*  (raíz o superusuario)
de los sistemas GNU/Linux.
Su "carpeta de usuario" se llama `root` 
pero no se encuentra en `/home` sino en la ruta raiz `/`.

Por ejemplo: si se indica la ruta de archivo
`~/salida.txt`
(archivo en carpeta de usuario)
esto se traduce en el contenedor como 
`/root/salida.txt`.

La función `Path()` es práctica para convertir las rutas relativas a la carpeta de usuario con su método `expanduser`: 
```py
from pathlib import Path

ruta_archivo = Path( "`~/salida.txt").expanduser()
``` 

!!! info "Permisos de root" 

    En Docker el usuario `root`
    posee todos los permisos de administrador por *default*.
    Esto es diferente en Podman,
    donde el usuario `root` no tiene dichos permisos por *default* y por eso ejecuta los contenedores en modo *rootless*.
    a menos que se inicie Podman en modo *rootful* deliberadamente.


## Uso de volumenes

El acceso de los contenedores
a los volumenes se indica 
mediante el campo `volumes`
del archivo `compose.yml`.
Un mismo proyecto permite definir múltiples volumenes;
además un mismo contenedor puede acceder
a varios volumenes simultáneamente.

Hay varias variantes de volumenes
que pueden ser creados,
las cuales se muestran a continuación.

### Volumenes anónimos

Los volumenes anónimos se crean
asignando un único valor
que corresponde a la ruta interna del contenedor:

```yaml
name: nombre_proyecto

services:

  servicio_volumen:
    build: .
    # lista de rutas internas
    volumes:
      - ruta_contenedor
```

En este caso el programa gestor de los contenedores
crea un volumen y le reserva al contenedor un directorio
para guardar los datos persistentes.

Si el despliegue se realiza en sistemas GNU/Linux
entonces los voúmenes se suelen alojar en la ruta
`/home/USUARIO/.local/share/containers/storage/volumes/`

Al volumen anónimo se le asigna un nombre aleatorio
de manera automática.

<!-- 
Al volumen anónimo se le asigna un nombre automáticamente
que está compuesto por el nombre del proyecto,
el nombre del servicio que lo usa
y una secuencia aleatoria.
Por ejemplo en este caso
el volumen sería llamado como
`nombre_proyecto_servicio_volumen_1c7d7b...`.
 -->
Esto es relevante si se necesita realizar
la inspección del volumen (ver más adelante).


### Volumenes con nombre

Los volumenes con nombre
son similares a los volumenes anónimos.
En este caso a cada ruta interna del contenedor
se le asigna un nombre
que funciona como un alias.

```yaml
name: nombre_proyecto

services:

  servicio_volumen:
    build: .
    # lista de volumenes accedidos
    volumes:
      # montajes (equivalencias)
      - nombre_volumen:/root/logs


# lista de volumenes implementados
volumes:
  nombre_volumen:
    external: false   # valor default
```

El nombre asignado al volumen 
suele estar compuesto por el nombre del proyecto
y el alias definido para el volumen.
Por ejemplo en este caso
el volumen se llamaría
`nombre_proyecto_alias_volumen`.

Este tipo de volumenes puede ser accedido
por múltiples contenedores mediante su alias.
Si el volumen requerido proviene de otro proyecto
entonces hace falta especificar el parámetro `external`
como `true`:

```yaml
# lista de volumenes implementados
volumes:
  nombre_volumen:
    external: true
```

### Volumenes de host

En este tipo de asignación
no se crea un elemento de volumen
sino que se monta una ruta del sistema anfitrión 
(el host) a la ruta de interés del contenedor.

```yaml
services:

  servicio_volumen:
    build: .
    # lista de volumenes accedidos
    volumes:
      # montajes (equivalencias)
      -  ruta_host:ruta_contenedor
    # opciones de seguridad
    security_opt: 
      - label=disable
```

Si la ruta indicada en el sistema host no existe
entonces se creará automáticamente.

!!! warning "Security Options"

    El atributo `security_opt`
    es opcional en Docker
    pero es indispensable en Podman
    para otorgar y configurar los permisos de acceso
    a los recursos del host
    por parte del contenedor.
    Haciendo `label=disable`
    se libera el acceso al contenedor
    de los recursos del usuario actual del sistema
    pero no se da acceso a los recursos
    que requieran permisos de administrador.



## Inspeccionar volumenes

La lista de volumenes existentes se consulta
con el comando `volume list`:

```bash
podman volume list
```

Los parámetros del volumen de interés
se consultan con el comando `volume inspect`:


```bash
podman volume inspect NOMBRE_VOLUMEN 
```

La ruta al contenido del volumen
se indica dentro del campo `Mountpoint`.
Su valor se puede consultar así:


```bash
podman volume inspect NOMBRE_VOLUMEN --format='{{.Mountpoint}}'
```

Accediendo a esta ruta se podrá acceder a los datos
para realizar copias de seguridad,
restablecer los datos,
realizar una migración de plataforma, etc.

!!! tip "Gestión gráfica"

    Las aplicaciones de escritorio de Docker y de Podman
    permiten visualizar y administrar los volumenes existentes de manera gráfica.




## Ejemplo demo


En este demo la rutina cuenta hasta un número especificado
pero en este caso los logs salen por consola
y por archivo en simultáneo.
El archivo es creado 
con el nombre `reporte.log` y los reportes son acumulativos.

!!! example "demo contar" 

    ```py title="contar.py" hl_lines="7 12-22"
    from time import sleep
    from pathlib import Path
    import sys
    import logging

    # ruta al reporte (en contenedor) : /root/logs/reporte.log
    ruta_log = Path( "~/logs/reporte.log").expanduser()

    logging.basicConfig(
        level=logging.INFO, # mínimo nivel de log a publicar
        format="%(asctime)s - %(levelname)s - %(message)s", #info incorporada
        handlers=[
            # salida por consola
            logging.StreamHandler(), 
            # salida por archivo
            logging.FileHandler(
                filename=ruta_log,
                mode="a",
                encoding="utf-8",
                delay=True,
                ),
            ],
        )


    try:
        # el numero maximo a contar se asigna como argumento
        n = int(sys.argv[1])
        logging.info("Contando hasta %i", n)

    except Exception:
        # valor máximo por default en caso de error
        logging.warning("Argumento de entrada faltante o incorrecto (debe ser un entero)")
        n = 10
        logging.warning("Contando hasta %i (valor default)", n)

    finally:
        # el contador se incrementa cada 1 segundo
        i = 0
        while i <= n:
            logging.info("i: %4i",i)
            sleep(1)
            i += 1
    ``` 

    ``` Dockerfile title="Dockerfile"
    # imagen de referencia
    ARG TAG_IMAGEN=3.13.5-alpine3.22
    # ARG TAG_IMAGEN=3.13.5-slim-bookworm
    FROM python:${TAG_IMAGEN}
    # FROM python:3.13.5-alpine3.22

    # directorio de trabajo (se crea automáticamente)
    WORKDIR /code

    # copia de rutinas al directorio de trabajo
    COPY demo/ ./

    # comando, opciones y argumentos fijos
    ENTRYPOINT ["python", "contar.py"]

    # opciones y argumentos sobreescribibles
    CMD ["4"]
    ``` 

    A continuación se muestran varias implementaciones alternativas
    de la gestión de volumenes:

    === "Volumen anónimo"

        ``` bash title="Arbol de archivos"
        .
        ├── compose.yml
        ├── Dockerfile
        └── demo
            └── contar.py
        ```

        ```yaml title="compose.yml"
        name: demo_volumen

        services:

          servicio_volumen:
            build: .
            volumes:
              - /root/logs
        ```



    === "Volumen con nombre"

        ``` bash title="Arbol de archivos"
        .
        ├── compose.yml
        ├── Dockerfile
        └── demo
            └── contar.py
        ```

        ```yaml title="compose.yml"
        name: demo_volumen

        services:

          servicio_volumen:
            build: .
            volumes:
              - registro_persistente:/root/logs


        volumes:
          registro_persistente:
        ```


    === "Volumen de host"


        ``` bash title="Arbol de archivos"
        .
        ├── compose.yml
        ├── Dockerfile
        ├── demo
        │   └── contar.py
        └── registro
            └── reporte.log
        ```



        ```yaml title="compose.yml"
        name: demo_volumen

        services:

          servicio_volumen:
            build: .
            volumes:
              - ./registro:/root/logs
            security_opt: 
              - label=disable
        ```




