---
date:
    created: 2025-08-16
    updated: 2025-08-16
status: new
---

# Entry Points


En esta sección se ven las opciones que da Poetry
para crear comandos propios (*"entrypoints"*)
del proyecto o paquete actual.

## Definir comandos


Los entrypoints se crean
editando manualmente 
el archivo TOML del proyecto.
Los comandos se especifican
dentro de secciones específicas,
en base a una asignación comando - *namespace*. 


### CLI

La *Command Line Interface* es 
la interfaz mostrada al usuario desde terminal.

A los comandos de terminal
les corresponde la sección `[project.scripts]`:

``` toml title="Entrypoints - CLI"
# archivo 'pyproject.toml'
[project.scripts]
nombre-cli = 'paquete.modulo-cli:funcion_comando'
```

A cada comando implementado le corresponde un *namespace*
que represente a la función a ejecutar.


### GUI


Estos *scripts* funcionan de manera análoga
a los comandos de CLI,
sólo que se usan habitualmente
para llamar a una interfaz gráfica del programa.

A estos comandos les corresponde la sección `[project.gui-scripts]`:

``` toml title="Entrypoints - GUI"
# archivo 'pyproject.toml'
[project.gui-scripts]
nombre-gui = 'paquete.modulo-gui:funcion_llamada'
```

En este caso también se requiere indicar un *namespace*,
que en este caso es 
el de la función que llame a la interfaz gráfica.


### Archivos precompilados

En el caso de requerirse el agregado
de archivos ya compilados
(por ejemplo, ejecutables)
esto se realiza con el campo
`[tool.poetry.scripts]`:

``` toml title="Entrypoints - Ejecutables"
# archivo 'pyproject.toml'
[tool.poetry.scripts]
ejecutable = { reference = "archivo.exe", type = "file" }
```

## Implementar comandos

Los comandos se crean
al llamar al comando `install` de Poetry:


```bash title="Entrypoints - Actualizar proyecto"
poetry install
```

Este comando creará las rutinas auxiliares
(los *scripts*) correspondientes a cada comando
y los ubicará dentro del entorno virtual actual
al lado del intérprete de Python,
dentro de la carpeta `bin` o `Scripts` según corresponda.

## Ejecución


Los scripts creados son autoejecutables,
por tanto puede ser llamados
sin necesidad de activar el entorno virtual
explícitamente:

```bash title="Comando - entorno desactivado"
cd ruta_script
./nombre-comando
```

Si en cambio el entorno virtual está activado
entonces a los comandos se los puede llamar por su nombre
directamente:

```bash title="Comando - entorno activado"
nombre-comando
```


<!-- 
!!! info "Autoejecución"

    El script creado es autoejecutable,
    por tanto puede ser llamado
    sin necesidad de activar su entorno virtual
    explícitamente:

    ```bash title="Comando - entorno desactivado"
    cd ruta_script
    ./nombre-comando
    ```
-->

!!! tip "Uso de enlaces"

    Al comando creado se le puede crear un enlace simbólico
    (algo parecido a un enlace directo de Windows)
    mientras el entorno virtual está activado:

    ```bash title="Comando - enlace simbólico"
    # activar entorno virtual
    eval $(poetry env activate)
    # consultar ruta
    RUTA=`which nombre-comando`
    echo $RUTA
    # crear enlace simbólico
    ln -s $RUTA ubicacion_enlace/nombre_enlace
    ```
    De allí en más,
    el comando se podrá ejecutar
    llamando al enlace simbólico
    y sin necesidad de activar previamente
    su entorno virtual:

    ```bash title="Comando - ejecutar desde enlace"
    # activar entorno virtual
    cd ubicacion_enlace
    ./nombre_enlace
    ```


## Ejemplo de uso

Se crea un proyecto nuevo con Poetry:

``` bash title="Comando - nuevo proyecto"
poetry new paquete
```

La estructura de archivos creados es la siguiente:

``` bash title="Comando - arbol del proyecto"
paquete
├── pyproject.toml
├── README.md
├── src
│   └── paquete
│       └──  __init__.py
└── tests
    └── __init__.py
```

En el archivo `__init__.py`
se crea una función
para ser ejecutada por consola:

```py title="Comando - crear función"
# archivo '__init__.py'
def texto_consola(argumentos):
    print("Comando CLI correcto")
```

Esta función es agregada al archivo TOML
bajo la sección `project.scripts`
y se le da un nombre de comando,
que en este ejemplo 
es llamado `paquete-cli`:

``` toml title="Comando - configurar archivo TOML"
# archivo 'pyproject.toml'
[project.scripts]
paquete-cli = "paquete:texto_consola"
```

En este contexto `paquete:texto_consola` es el *namespace*
correspondiente a la función de Python
que debe ejecutarse.
Al actualizar la configuración
del entorno virtual:


```bash title="Comando - Actualizar proyecto"
poetry install
```

se observa que se crea un *script* ejecutable
con el nombre de comando elegido,
justo al lado del intérprete de Python:

```bash hl_lines="9" title="Comando - árbol del entorno virtual"
ruta_entorno
├── bin
│   ├── activate
│   ├── activate.csh
│   ├── activate.fish
│   ├── activate.nu
│   ├── activate.ps1
│   ├── activate_this.py
│   ├── paquete-cli
│   ├── pip
│   ├── pip3
│   ├── pip-3.13
│   ├── pip3.13
│   ├── python -> /usr/bin/python3.13
│   ├── python3 -> python
│   └── python3.13 -> python
├── CACHEDIR.TAG
├── lib
│   └── python3.13
├── lib64
│   └── python3.13
└── pyvenv.cfg
```

Este script podrá ser llamado por su nombre
desde la terminal
para ser ejecutado:

```bash title="Comando - llamar"
paquete-cli
```

De esta forma el comando queda implementado.


## Referencias

[The pyproject.toml file - scripts](https://python-poetry.org/docs/pyproject/#scripts-1)


