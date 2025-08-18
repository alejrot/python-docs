---
date:
    created: 2025-03-23
    updated: 2025-08-18
# status: new
---

# Comenzando con Poetry



## Crear proyecto

### Archivo TOML

El archivo `pyproject.toml` es el archivo de configuración principal.
En él se incluye la información de las dependencias,
las versiones de Python compatibles,
la información del autor y su contacto,
etc.
Lo habitual es dejar a Poetry crear este archivo mediante comandos.

### Proyecto vacío

El comando `new` permite crear un nuevo proyecto,
junto a algunos directorios:

```bash title="Nuevo proyecto"
poetry new nuevo_proyecto
```

Tras ejecutar este comando
se abre un menú interactivo en consola para configurar las opciones del proyecto una por una,
información del autor y de contacto,
licencia del proyecto, etc.
Es mejor que el directorio del proyecto no exista previamente para asegurar que Poetry cree todos los archivos y carpetas internos.

Este es el contenido generado:

```bash title="Nuevo proyecto - arbol de archivos"
nuevo_proyecto
├── pyproject.toml
├── README.md
├── src
│   └── nuevo_proyecto
│       └── __init__.py
└── tests
    └── __init__.py
```

Poetry asume por default que el proyecto será dedicado al desarrollo de paquetes,
por eso crea un directorio con el mismo nombre de proyecto adentro de la carpeta `src`.
El directorio `tests`
está pensado para correr tests unitarios
mediante paquetes como *Pytest*.

Todos los archivos se crean vacíos, excepto el archivo `pyproject.toml`
el cual es configurado interactivamente.

!!! info "src-layout"

    El esquema de archivos seguido por Poetry
    es llamado comunmente *src-layout*.


### Crear TOML

Para crear solamente el archivo `pyproject.toml` dentro del directorio actual se usa el comando `init`:

```bash title="Nuevo archivo de proyecto"
poetry init
```

Tras ejecutar este comando
se abre el mismo menú interactivo que en el caso del comando `new`.


## Gestión de paquetes 

### Agregado

Para agregar un nuevo paquete al proyecto
se usa el comando `add`:

```bash title="Paquetes - agregar"
poetry add nombre_paquete
```
Este comando incluye el paquete automáticamente como dependencia en el archivo TOML.

Este comando también:

- crea un entorno para el proyecto actual si aún no existe;
- instala el paquete en el entorno actual.


!!! info "Ubicacion de entornos"

    A diferencia de VENV,
    Poetry crea todos los entornos locales en una misma carpeta dedicada a tal fin.
    Por ejemplo en Linux dicha carpeta suele ser:
    `CARPETA_USUARIO/.cache/pypoetry/virtualenv`



### Especificacion de versiones

Las versiones de cada paquete
se pueden asignar mediante el uso de restricciones
(*constraints*)
junto al comando `add`,
los cuales se enumeran a continuación:


| Simbolo | Significado | Ejemplo|
|---|---|---|
| `^` |Sólo actualizaciones menores y patches | `n.x.x` |
| `~` | Sólo actualizaciones patch | `n.m.x` |
| `@` | Version exacta | `n.m.o` |




Ejemplos de uso: definiendo versiones del paquete cosmético `rich`:

```bash title="Paquete - agregar (ejemplos)"
poetry add rich^13.0       # versiones 13.0.0 a 14.0.0 
poetry add rich~13.0       # versiones 13.0.0 a 13.1.0 
poetry add rich@13.0.1     # sólo versión 13.1.0
```

Los cambios se verán reflejados en el archivo TOML.
Por ejemplo, si se elige especificar sólo la versión mayor del paquete:

```bash title="Paquetes - agregar version mayor"
poetry add rich^13.0 
```
Entonces el rango se indicará en el archivo `pyproject.toml`
entre paréntesis
bajo la sección `[project]`:

``` toml title="TOML - dependencias"
# archivo 'pyproject.toml'
[project]
dependencies = [
    "rich (>=13.0,<14.0)",
]
```


### Actualización

Se dispone del comando `update` para actualizar los paquetes
de acuerdo a los rangos de versiones predefinidos en el proyecto.

```bash title="Paquetes - actualización"
poetry update
```

### Remoción


El paquete se elimina del proyecto con el comando `remove`:

```bash title="Paquetes - remover"
poetry remove nombre_paquete
```
el cual desinstala el paquete del entorno actual y lo borra de la lista de dependencias.



## Ejecución

### Ejecución directa

El comando `run` de Poetry permite ejecutar las rutinas del proyecto 
al tiempo que carga las dependencias:

```bash title="Entorno virtual - comando run"
poetry run python nombre_rutina
```


### Activación y desactivación de entorno virtual


El entorno virtual se activa en Bash con la siguiente expresión:

```bash title="Entorno virtual - activar"
eval $(poetry env activate)
```

de esta manera el intérprete de Python puede ser llamado directamente:

```bash title="Entorno virtual - ejecutar rutina"
python nombre_rutina
```

Por último,
se dispone del comando `deactivate`
para deshabilitar el entorno actual:

```bash title="Entorno virtual - desactivar"
deactivate
```
