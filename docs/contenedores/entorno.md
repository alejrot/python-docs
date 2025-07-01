# Variables de entorno


## Introduccion

Las variables de entorno
sirven para configurar opciones de los programas
desde el sistema.


### Variables en BASH

Las variables se crean desde la *shell* Bash
con el comando `export`:

```bash title="Bash - crear variable de entorno"
export NOMBRE_VARIABLE=VALOR    # variable con valor
export NOMBRE_VARIABLE          # variable vacía
```

y se eliminan con el comando `unset`:

```bash title="Bash - eliminar variable de entorno"
unset NOMBRE_VARIABLE
```
Los valores de estas variables se transmiten como *strings*.

### Lectura desde Python

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


## Variables en Compose

Dentro del contenedor no rigen
las mismas variables de entorno
que en el sistema anfitrión.
Por este motivo,
el gestor de contenedores debe importar
las variables de entorno que sean necesarias
para que los contenedores puedan acceder a ellas. 


### Ordenar lectura

En el archivo `compose.yml` se indican
las variables de entorno necesarias
bajo el campo `environment`:

```yaml title="compose.yml - leer variable"
services:

  entornos_python:
    build: .
    environment:
      VARIABLE_PYTHON: "${VARIABLE_BASH}"
```

Nótese que las variables de entorno experimentan un "mapeo":
a izquierda se indica el nombre de variable
que verá la rutina de Python
adentro del contenedor
y a la derecha se indica el nombre de la variable
definida en la terminal del sistema anfitrión.

Dentro de la lectura del valor de la variable
se puede definir un valor *default* entre las llaves:

```yaml title="compose.yml - leer variable (con valor default)"
services:

entornos_python:
    build: .
    environment:
      VARIABLE_PYTHON: "${VARIABLE_BASH:-VALOR_DEFAULT}"
```


### Archivo `.env`

Una forma cómoda de crear las variables de entorno
es usar un archivo de texto con nombre `.env`.
En este archivo se crean
las variables de entorno necesarias,
una por renglón:


```env title="Archivo .env - sintaxis"
NOMBRE_VARIABLE_1=VALOR_1
NOMBRE_VARIABLE_2=VALOR_2
```


Este archivo es detectado por *default*
por el gestor de contendores;
sin embargo definir el mapeo de variables 
en el archivo `compose.yml`
sigue siendo necesario.

!!! tip "Comentarios"
    Los archivos `.env` admiten comentarios
    precedidos por un numeral (`#`).


!!! info "Jerarquía de valores"
    Si una variable de entorno es definida en terminal
    y en archivo entonces el valor leído será el de terminal.



### Archivo custom

Las variables de entorno también se pueden repartir
entre varios archivos,
los cuales típicamente tienen extensión `.env`.
Estos archivos requieren importación explícita,
la cual se realiza con el campo `env_file`:

```yaml hl_lines="7" title="compose.yml - archivo custom"
services:

  entornos_python:
    build: .
    environment:
      VARIABLE_PYTHON: "${VARIABLE_BASH}"
    env_file: archivo_custom.env
```


## Ejemplo de uso

En este demo se crea una variable de entorno
en un archivo `.env`
y es leída por unar rutina llamada `entorno.py`
desde adentro de un contenedor.

!!! example "Variables de entorno - ejemplo"

    ```tree title="Arbol de archivos"
    .
    ├── compose.yml
    ├── Dockerfile
    ├── .env
    └── entorno.py
    ```

    ```py title=".env"
    VARIABLE=14
    ```

    ```yaml title="compose.yml" hl_lines="5-6"
    services:

      entornos_python:
        build: .
        environment:
          ENTORNO: "${VARIABLE}"
    ```
    ```py title="entorno.py" hl_lines="11"
    import os
    import logging

    logging.basicConfig(
        level=logging.INFO, # mínimo nivel de log a publicar
        format="%(message)s", #info incorporada
        )


    # lectura
    valor_variable = os.getenv("ENTORNO")

    # muestra en ventana de logs
    logging.info("Variables de entorno")
    logging.info(f"Valor de VARIABLE: {valor_variable}")
    ```

    ```dockerfile title="Dockerfile"
    # imagen de referencia
    FROM python:3.13.5-alpine3.22

    # directorio de trabajo (se crea automáticamente)
    WORKDIR /code

    # copia de rutinas al directorio de trabajo
    COPY entorno.py ./

    # comando y opciones obligatorios
    ENTRYPOINT ["python"]

    # comandos adicionales
    CMD ["entorno.py"]
    ```
