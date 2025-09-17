---
status: new
date:
    created: 2025-07-01
    updated: 2025-08-26
---


# Variables de entorno

Las variables de entorno
son variables de texto
manejadas por el sistema operativo.
Se usan frecuentemente
para configurar opciones y parámetros de los programas
desde el sistema.


## Introduccion


Los contenedores funcionan
en entornos aislados por *default*.
Al ser desplegados,
sus programas internos 
son incapaces de acceder
a estas variables de entorno
por sí mismos.
Por este motivo
los gestores de contenedores
dan opciones para realizar copias
de las variables de entorno necesarias
y asignarlas a los contenedores
que las requieran.


### Variables en BASH

Las variables de entorno
se crean desde la *shell* Bash
con el comando `export`:

```bash title="Bash - crear variable de entorno"
export NOMBRE_VARIABLE=VALOR    # variable con valor
export NOMBRE_VARIABLE          # variable vacía
```

y se eliminan con el comando `unset`:

```bash title="Bash - eliminar variable de entorno"
unset NOMBRE_VARIABLE
```
La consulta manual de los valores
se hace con el comando `echo`
y el signo `$` delante del nombre de variable:

```bash title="Bash - consultar valor de variable"
echo $NOMBRE_VARIABLE
```

Los valores de estas variables se transmiten como *strings*.


### Lectura desde rutinas Python

Con el módulo `os` se pueden consultar
las variables de entorno en las rutinas de Python.
Estas son consultadas con la función `getenv()`

```py title="Python - leer variable de entorno"
import os

valor_variable = os.getenv(
    "NOMBRE_VARIABLE",          # variable buscada
    default=valor_respaldo      # opcional
    )
```

Si la variable pedida existe entonces se lee su valor;
en caso contrario se devuelve
el valor indicado por el argumento `default`.
Si este no fue definido
entonces se devuelve `None`.



## Asignación de variables

Cada contenedor del proyecto
debe ser configurado deliberadamente
para poder acceder a los valores
de las variables de entorno.
En el archivo `compose.yml` se indican
las variables de entorno necesarias
para cada contenedor
con ayuda del campo `environment`.

### Mapeo de variables

Las variables de entorno experimentan un *"mapeo"*:
a izquierda se indica el nombre de variable
que verá la rutina
adentro del contenedor
y a la derecha se indica el nombre de la variable
definida en la terminal del sistema anfitrión:

```yaml title="compose.yml - mapeo de variables"
services:

  programa_entorno:
    build: .
    environment:
      VARIABLE_PROGRAMA: "${VARIABLE_BASH}"
```

### Valor default

Dentro de la lectura del valor de la variable
se puede definir un valor *default* entre las llaves.
Este valor es asignado solamente
si la variable de entorno no fue definida.
Este valor de resguardo se 
consigue con el signo `-`:

```yaml title="compose.yml - leer variable (con valor default)"
services:

programa_entorno:
    build: .
    environment:
      VARIABLE_PROGRAMA: "${VARIABLE_BASH:-VALOR_DEFAULT}"
```

Si se agrega el signo `:`
también se autocompleta
ante variables existentes
pero sin valor.


### Valor de reemplazo

Existen casos donde se necesita sobreescribir 
el valor de entrada de la variable
por un valor sustituto.
Se marca con el signo `+`.

```yaml title="compose.yml - leer variable (con valor reemplazo)"
services:

programa_entorno:
    build: .
    environment:
      VARIABLE_PROGRAMA: "${VARIABLE_BASH:+VALOR_SUSTITUTO}"
```

Agregando el signo `:`
se sustituyen también
las variables nulas.

### Error ante faltante

Si la variable no está declarada o está vacía
entonces se permite lanzar una excepción
que interrumpe el despliegue
y lanza un mensaje en consola.
Esto se consigue con el signo `?`:

```yaml title="compose.yml - leer variable (con error por faltante)"
services:

programa_entorno:
    build: .
    environment:
      VARIABLE_PROGRAMA: "${VARIABLE_BASH:?'Error: valor faltante'}"
```

Nuevamente,
colocando el signo `:`
se dispara el error
ante variables nulas.



!!! tip "Interpolación - resumen"

    A estas políticas para asignar
    valores de respaldo,
    errores, etc.
    se las llama **interpolación**.

    Este es el resumen de secuencias posibles:

    |Secuencia| Uso|
    |:---:|:---|
    |`-`| variable no definida |
    |`:-`| variable no definida o nula|
    |`?`| variable no definida |
    |`:?`| variable no definida o nula|
    |`+`| variable no definida |
    |`:+`| variable no definida o nula|




## Archivos `.env`


Una forma cómoda de definir las variables de entorno
es usar un archivo de texto con nombre `.env`
(archivo oculto).
En este archivo se crean
las variables de entorno necesarias,
una por renglón:

```env title="Archivo .env - sintaxis"
# comentarios (opcionales)
NOMBRE_VARIABLE_1=VALOR_1
NOMBRE_VARIABLE_2=VALOR_2
```

Durante el despliegue
el gestor de contendores
busca por este archivo
en el directorio del proyecto.
Este archivo es leído
y los valores
de sus variables internas
son importadas automáticamente.

<!-- 
Definir el mapeo de variables 
en el archivo `compose.yml`
sigue siendo necesario.
 -->

!!! info "Jerarquía de valores"
    Si una misma variable de entorno
    es definida en terminal y en archivo 
    entonces el valor leído por el gestor
    será el de terminal.


!!! danger "Control de versiones"

    Agregar los archivos `.env`
    a los repositorios de los proyectos es una **mala práctica**
    porque implica publicar información potencialmente sensible.


<!-- 
### Archivos custom

Las variables de entorno también se pueden repartir
entre varios archivos,
los cuales típicamente tienen extensión `.env`.
Estos archivos requieren importación explícita,
la cual se realiza con el campo `env_file`:

```yaml hl_lines="7" title="compose.yml - archivo custom"
services:

  programa_entorno:
    build: .
    environment:
      VARIABLE_PROGRAMA: "${VARIABLE_BASH}"
    env_file: archivo_custom.env
```
 -->

## Ejemplo de uso

En este demo se crea una variable de entorno
en un archivo `.env`
y es leída por unar rutina llamada `entorno.py`
desde adentro de un contenedor.

```tree title="Demo entornos - Arbol de archivos"
.
├── demo
│   └── main.py
├── compose.yml
├── Dockerfile
└── .env
```

Se crea una rutina sencilla en Python
para leer una variable de entorno 
y reportar su valor en la ventana de *logs*:

```py title="Demo entornos -main.py" hl_lines="10"
import os
import logging

logging.basicConfig(
    level=logging.INFO, # mínimo nivel de log a publicar
    format="%(message)s", #info incorporada
    )

# lectura de variable
valor_variable = os.getenv("VARIABLE_PYTHON")

# reporte de valor
logging.info(f"Valor de 'VARIABLE_PYTHON': '{valor_variable}'")
```

Al demo se le asigna el siguiente Dockerfile
para construir la imagen:

```dockerfile title="Demo entornos - Dockerfile"
# imagen de referencia
FROM python:alpine

# directorio de trabajo (se crea automáticamente)
WORKDIR /code

# copia de rutinas al directorio de trabajo
COPY demo/ ./

# comandos 
CMD ["python", "main.py"]
```

Se configura el despliegue 
en varios contenedores paralelos
con distintas interpolaciones de variables:

```yaml title="Demo entornos - compose.yml" 
name: demo_variables_entorno

services:

  # crea una imagen común para todos los demos
  crear_imagen:
    build: .
    image: demo_entornos 

  # cada contenedor pone a prueba distintas interpolaciones
  entornos:
    image: demo_entornos 
    environment:
      VARIABLE_PYTHON: "${VARIABLE}"
    depends_on:
      crear_imagen:
        condition: service_completed_successfully

  entornos_default:
    image: demo_entornos 
    environment:
      VARIABLE_PYTHON: "${VARIABLE:-'valor predefinido'}"
    depends_on:
      crear_imagen:
        condition: service_completed_successfully

  entornos_error:
    image: demo_entornos 
    environment:
      VARIABLE_PYTHON: "${VARIABLE?'Error: variable no inicializada'}"
    depends_on:
      crear_imagen:
        condition: service_completed_successfully

  entornos_sustituir:
    image: demo_entornos 
    environment:
      VARIABLE_PYTHON: "${VARIABLE:+Sustituido}"
    depends_on:
      crear_imagen:
        condition: service_completed_successfully
```

Nótese que sólo uno de los contenedores
construye la imagen y los demás la reutilizan. 


Finalmente se crea un archivo `.env`
aledaño al archivo `compose.yml`
y se define dentro la variable de entorno:

```py title="Demo entornos - variable en archivo"
VARIABLE="Vengo del archivo '.env'"
```

o se declara en la *shell*:

```bash title="Demo entornos - variable en Bash"
export VARIABLE="Me definieron en BASH"
```

Por último se realiza el despliegue:

```bash title="Demo entornos - despliegue"
podamn compose up
```
