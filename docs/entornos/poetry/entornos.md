---
date:
    created: 2025-03-23
    updated: 2025-08-16
---


# Gestión de Entornos Virtuales


Poetry admite gestionar múltiples entornos de ejecución para un mismo proyecto.
Cada entorno virtual del proyecto viene vinculado a un intérprete de Python disponible en el sistema, típicamente de distintas versiones.
Esto significa que Poetry permite crear un entorno virtual del proyecto para cada versión del intérprete de Python a utilizar.

<!-- 
Esto significa que, si existe un único intérprete de Python, entonces Poetry creará un único entorno virtual.
 -->
 
## Comando `python`

Poetry incluye su propio gestor de intérpretes Python
desde su versión 2.1.0.


### Instalación

Estos intérpretes se gestionan con el comando `python`: 
```bash title="Versión de Python - instalar"
poetry python install TAG_VERSION
```

Este comando permite disponer de
intérpretes Python desde su versión 3.7.x en adelante.
Estos intérpretes son basados en CPython,
es decir son intérpretes escritos en lenguaje C y luego compilados.

Por ejemplo, para instalar la versión 3.9 de Python el comando sería:

```bash title="Versión de Python - ejemplo"
poetry python install 3.9
```


### Consulta

La lista de versiones de Python descargadas y sus rutas
se consulta con el comando `list`:

```bash title="Versión de Python - listar"
poetry python list
```

Las versiones descargadas por Poetry se guardan en:

=== "GNU/Linux"

    ```bash
    # directorio '.local'
    CARPETA_USUARIO/.local/share/pypoetry/python
    ```

=== "Windows"

    ```bash
    
    ```


### Eliminación

La desinstalación de una versión específica de Python se realiza con el comando `remove`:

```bash title="Versión de Python - eliminar"
poetry python remove TAG_VERSION
```

## Uso con Pyenv

Poetry también puede ser usado junto con el plugin **pyenv** para elegir una versión específica de Python para el proyecto.

```bash title="Versión de Python - con Pyenv"
pyenv install 3.9.8     # instalar Python 3.9.8
pyenv local 3.9.8       # elegir Python 3.9.8
```
Esta opción es útil para sistemas con versiones antiguas de Poetry. 

<!-- 
```bash
pyenv install 3.9.8     # instalar Python 3.9.8
pyenv local 3.9.8       # elegir Python 3.9.8
poetry install          # insta
```
 -->

## Entornos de Poetry

### Crear nuevo entorno

Mediante el comando `use` se puede elegir una versión de Python disponible.
Con este comando,
Poetry crea un nuevo entorno para el proyecto
y en él crea enlaces simbólicos al intérprete de Python elegido. 

El intérprete se elige por su ruta completa, por su nombre o simplemente por su número de versión:

```bash title="Entorno - crear y usar"
poetry env use ruta_interprete/bin/python3.9    # ruta completa
poetry env use python3.9                        # nombre y versión
poetry env use 3.9                              # sólo versión
```


### Listar entornos

los entornos ya creados se consultan con el comando `list`:

```bash title="Entorno - listado"
poetry env list
```

Este comando sólo muestra los entornos correspondientes al proyecto actual,
es decir no muestra los entornos correspondientes a otros proyectos.

Las rutas en el sistema de cada entorno se consultan agregando la opción `--full-path`: 

```bash title="Entorno - rutas de entornos"
poetry env list --full-path
```


Los entornos virtuales ya existentes se encuentran en la ruta:

=== "GNU/Linux"

    ```bash
    # directorio '.cache'
    CARPETA_USUARIO/.cache/pypoetry/virtualenvs/
    ```

=== "Windows"

    ```bash
    
    ```

<!--     
## Cambio de entorno

```bash
poetry env use ruta_entorno/bin/python3.9
```
-->


### Instalar dependencias

Los paquetes requeridos se descargan e instalan  en el entorno actual con el comando `install`:

```bash title="Entorno - instalar dependencias"
poetry install
```

Este comando instala todos los paquetes indicados en el proyecto.


<!-- 
- Si el archivo LOCK del proyecto existe
entonces Poetry replicará la instalación de dependencias en base a este archivo;
- Si el archivo LOCK del proyecto es inexistente
entonces Poetry usará el archivo TOML como referencia
y creará el archivo LOCK donde guardará el nombre y versión exacta
de todas las dependencias.

 -->
 
!!! warning "Empaquetado"

    Este comando requiere que el empaquetado esté **deshabilitado**.
    Para deshabilitar el empaquetado agregar al archivo TOML
    la sección `[tool.poetry]`
    y debajo deshabilitar el `package-mode`:

    ```
    [tool.poetry]
    package-mode = false
    ```

    O en su defecto corregir el valor de `package-mode` por `false`.



### Información

La información del entorno actual se lee con el argumento `info`:

```bash title="Entorno - información"
poetry env info                 # toda la información
poetry env info --executable    # ruta al interprete Python
```



### Eliminar

Los entornos se eliminan en base al número de versión de Python que usan:

```bash title="Entorno - borrar"
poetry env remove 3.13       # entorno actual
```

o también pueden ser eliminados todos juntos:

```bash title="Entorno - borrar todos"
poetry env remove --all  # todos
```

Nuevamente, estos comandos sólo pueden eliminar entornos virtuales del actual proyecto.
