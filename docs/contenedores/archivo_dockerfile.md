---
date:
    created: 2025-08-26
    updated: 2025-08-26
---

# Archivo Dockerfile

## Idea general

El archivo Dockerfile
es el archivo de configuración
que se necesita para crear y modificar las imágenes:
agregar las rutinas del programa,
instalar dependencias adicionales,
etc. 

Su uso es indispensable
para cualquier proyecto
que dependa de rutinas propias.


## Sintaxis genérica

Supóngase un proyecto sencillo
escrito en Python,
cuya estructura de archivos es la siguiente:


```bash title="Arbol de archivos - Proyecto"
.
├── src
│   └── rutina.py
└── requirements.txt
```

En este ejemplo las rutinas de Python
se alojan en la carpeta `src`
y se adjunta un archivo de requisitos
para instalar los paquetes necesarios.

Se agrega el archivo de configuración
al proyecto
para crear la imagen:

```bash title="Arbol de archivos - Proyecto (con Dockerfile)" hl_lines="5"
.
├── src
│   └── rutina.py
├── requirements.txt
└── Dockerfile
```

El archivo Dockerfile
tiene una forma como esta:


```Dockerfile title="Dockerfile - básico"
# imagen de base - version fija
FROM python:alpine

# directorio de trabajo del contenedor (se crea automáticamente)
WORKDIR /code

# copia de archivo de dependencias al directorio de trabajo
COPY requirements.txt ./

# instalación de paquetes de python
RUN pip install --no-cache-dir -r requirements.txt

# actualización de PIP
RUN pip install --upgrade pip

# copia de rutinas al directorio de trabajo
COPY src/ ./

# comando, opciones y argumentos
CMD ["python", "rutina.py"]
``` 

Al ser construida la imagen
su estructura interna toma esta forma:


```bash title="Arbol de archivos - Imagen" hl_lines="8-10"
/
|   # directorios estándar
├── run
├── root
├── etc
├── ...
|   # directorio de trabajo
└── code
    ├── requirements.txt
    └── rutina.py
```



## Cláusulas básicas


El archivo Dockerfile tiene una serie
de cláusulas básicas que se explican a continuación.



### `FROM` 

La cláusula `FROM` especifica qué imagen de base
se utilizará para el proyecto.
Permite indicar nombre y etiqueta de versión.

Uso:

``` Dockerfile title="Imagen de referencia"
FROM  nombre_imagen:tag_version
``` 

Esta cláusula es obligatoria y se indica al comienzo.


### `WORKDIR` 

`WORKDIR` definer una ruta de trabajo 
para el programa
dentro del contenedor.
Si dicha ruta no existe en la imagen original
entonces es creada automáticamente.

Uso:

``` Dockerfile title="Directorio de trabajo"
WORKDIR ruta_interna_contenedor
``` 

### `COPY` 

Con `COPY` se copian los contenidos
necesarios del proyecto
al interior de la nueva imagen.
El código fuente,
los archivos de dependencias, 
assets (iconos, imagenes, etc.)
se transfieren de esta manera.

Uso:

``` Dockerfile title="Copia de contenidos"
COPY archivo_proyecto   ruta_destino/   
COPY carpeta_proyecto/  ruta_destino/
``` 

Esta cláusula se usa igual que el comando `cp` de Bash.
Si la ruta de destino indicada es del tipo relativa
entonces se toma por referencia
el directorio de trabajo.


### `RUN`

Este comando se usa típicamente
para instalar paquetes adicionales
del sistema operativo.
Estos paquetes quedarán guardados dentro de la imagen final.

Por ejemplo, para instalar los paquetes de Python con PIP
lo habitual es hacerlo mediante archivo TXT
y deshabilitando la caché de PIP:

``` Dockerfile title="Paquetes - PIP"
RUN pip install --no-cache-dir -r requirements.txt
``` 

la instalación de paquetes en la imagen con PIP se hace de manera **global**:
crear un entorno virtual no trae ninguna ventaja
porque el mismo contenedor hará las veces de entorno virtual.

Si se necesitan instalar paquetes faltantes del sistema operativo
se llama a su gestor de paquetes:

=== "Debian"

    ``` Dockerfile title="Paquetes - Gestor APT"
    RUN apt install paquete_debian
    ``` 

=== "Alpine"

    ``` Dockerfile title="Paquetes - Gestor APK"
    RUN apk add paquete_alpine
    ``` 

Nótese que no es necesario agregar la cláusula `sudo`
para instalar paquetes dentro de las imágenes.
<!-- 

!!! tip "Poetry en contenedores"

    En caso que la gestión de dependencias
    se haga con herramientas alternativas a PIP
    éste debe ser instaladas deliberadamente.
 
    En este ejemplo se asume el uso del
    [gestor de proyectos Poetry](../entornos/poetry/index.md)
    :

    === "Debian"

        ```Dockerfile title="Poetry - Versión más reciente"
        # instalacion de Curl y Poetry
        RUN apt install curl
        RUN curl -sSL https://install.python-poetry.org | python3 -
        RUN export PATH="/root/.local/bin:$PATH"
        # copia de archivo de dependencias al directorio de trabajo
        COPY pyproject.toml ./
        # instalación de dependencias - archivo TOML
        RUN poetry install
        ```

    === "Alpine"

        ```Dockerfile title="Poetry - Versión más reciente"
        # instalacion de Curl y Poetry
        RUN apk add curl
        RUN curl -sSL https://install.python-poetry.org | python3 -
        RUN export PATH="/root/.local/bin:$PATH"
        # copia de archivo de dependencias al directorio de trabajo
        COPY pyproject.toml ./
        # instalación de dependencias - archivo TOML
        RUN poetry install
        ```

 -->


### `CMD`

`CMD` define qué comando
deberá ejecutar la imagen
cuando sea puesto en marcha
dentro de un contenedor.
También permite definir argumentos posicionales
y opciones preasignados.

La notación recomendada es la siguiente:

``` Dockerfile title="Comandos"
CMD ["comando", "argumento_1", "argumento_1", "--opcion_1", ...]
``` 

En el caso de implementar rutinas de Python
el comando habitual es `python`
y el primer argumento será el nombre de la rutina principal:

``` Dockerfile title="Comandos en Python"
CMD ["python", "rutina.py", "argumento_rutina", "--opcion_rutina"]
``` 

Los comandos y opciones definidos por `CMD`
pueden ser sobreescritos externamente
durante el despliegue del contenedor.

`CMD` siempre se especifica al final.


## Construcción

La construcción de la nueva imagen
se realiza siguiendo el orden
indicado en el archivo Dockerfile.

El gestor de contenedores usado
sólo repite los pasos de construcción
donde detecta cambios:
código fuente reemplazado,
cambios en las dependencias y sus versiones,
etc.

!!! tip "Copia de código fuente al final"

    El código fuente se copia cerca del final
    porque es lo que cambia con mayor frecuencia.
    De esta manera se minimiza el tiempo de construcción.


Hay varias maneras de construir las imágenes:


### directa - comando `build`

El comando `build` construye la imagen
y le asigna el nombre y versión especificados
por la opción `-t`.

Uso básico:

```bash title="Construir - build"
cd ruta_dockerfile
podman build .  -t nuevo_nombre:version 
```

### indirecta - comando `compose`

En este caso la construcción de la imagen
se realiza indirectamente
durante el despliegue
con el comando `compose`,
el cual requiere  a su vez
el archivo `compose.yml`

Esto se explica en capítulos posteriores.





