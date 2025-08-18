---
date:
    created: 2025-03-23
    updated: 2025-08-18
---


# Gestión de dependencias

Los paquetes y otras dependencias son gestionadas
por Poetry mediante comandos específicos.


## Agregado

Para agregar un nuevo paquete al proyecto
se usa el comando `add`:

```bash title="Paquetes - agregar"
poetry add nombre_paquete
```
Este comando incluye el paquete automáticamente como dependencia en el archivo TOML.

Este comando también:

- crea un entorno para el proyecto actual si aún no existe;
- instala el paquete en el entorno actual.

Poetry admite también el agregado de paquetes
ubicados en el sistema de archivos
en base a su ruta relativa:

```bash title="Paquetes - agregar (local)"
poetry add ./pack-local/                              # carpeta del paquete
poetry add ./pack-local/dist/pack-local-0.1.0.tar.gz  # comprimido
poetry add ./pack-local/dist/pack-local-0.1.0.whl     # 'wheel'
```

y también se pueden agregar dependencias remotas
con repositorios Git,
admitiendo la URL correspondiente en varios formatos:


```bash title="Paquetes - agregar (remoto)"
poetry add git+https://github.com/sdispater/pendulum.git    # HTTPS
poetry add git+ssh://git@github.com/sdispater/pendulum.git  # SSH
```

Más detalles en la [página oficial de Poetry](https://python-poetry.org/docs/cli/#add).


!!! info "Ubicacion de entornos"

    A diferencia de VENV,
    Poetry crea todos los entornos locales en una misma carpeta dedicada a tal fin.
    Por ejemplo en Linux dicha carpeta suele ser:
    `CARPETA_USUARIO/.cache/pypoetry/virtualenv`



## Especificacion de versiones

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


## Actualización

Se dispone del comando `update` para actualizar los paquetes
de acuerdo a los rangos de versiones predefinidos en el proyecto.

```bash title="Paquetes - actualización"
poetry update
```

## Remoción


El paquete se elimina del proyecto con el comando `remove`:

```bash title="Paquetes - remover"
poetry remove nombre_paquete
```
el cual desinstala el paquete del entorno actual y lo borra de la lista de dependencias.


