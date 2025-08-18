---
date:
    created: 2025-08-16
    updated: 2025-08-18
---


# Crear proyecto

Poetry proporciona herramientas para crear nuevos proyectos
y también puede ser agregado a un proyecto preexistente.


## Archivo TOML

El archivo `pyproject.toml` es el archivo de configuración principal.
En él se incluye la información de las dependencias,
las versiones de Python compatibles,
la información del autor y su contacto,
etc.
Lo habitual es dejar a Poetry crear este archivo mediante comandos.

## Proyecto vacío

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


El archivo TOML resultante
tiene un contenido como este:

```toml title=""
[project]
name = "nuevo_proyecto"
version = "0.1.0"
description = ""
authors = [{name = "", email = "yo@miserver.me"}]
readme = "README.md"
requires-python = ">=3.13"
dependencies = [
]

[tool.poetry]
packages = [{include = "paquete", from = "src"}]

[build-system]
requires = ["poetry-core>=2.0.0,<3.0.0"]
build-backend = "poetry.core.masonry.api"
```

Los campos creados pueden ser modificados manualmente.
También pueden agregarse los campos adicionales
que se indican en la 
[documentación oficial](https://python-poetry.org/docs/pyproject/).


## Crear TOML

Para crear solamente el archivo `pyproject.toml` dentro del directorio actual se usa el comando `init`:

```bash title="Nuevo archivo de proyecto"
poetry init
```

Tras ejecutar este comando
se abre el mismo menú interactivo que en el caso del comando `new`.
La organización de los archivos
queda en este caso
a discreción del desarrollador.
