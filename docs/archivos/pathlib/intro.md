---
tags:
  - Archivos
  - Carpetas
  - Rutas
  - Pathlib
---

# Funcionalidades



Hay dos grandes funcionalidades disponibles para trabajar con las rutas,
las cuales son:

## `Path()` 

`Path()` es la función más importante del módulo.
Es la más versatil y permite tanto trabajar con *strings* que representan rutas arbitrarias como también alterar archivos y carpetas reales del sistema. 
Esta función reconoce automáticamente
tanto rutas de sistemas Windows y de sistemas POSIX
(UNIX, Linux, etc).

Esta función tiene dos subvariantes:

- `PosixPath()`: dedicada a rutas POSIX (UINIX, Linux, etc).
- `WindowsPath()`: dedicada a rutas Windows.

!!! warning "Modulo **os**"
    
    El módulo `os` también tiene una función llamada `Path()`,
    la cual no es compatible conla proporcionada por `pathlib`.

    <!-- 
    Varias de las funciones del módulo *pathlib* coinciden en nombre con las funciones del modulo **os**,
    las cuales no necesariamente son compatibles entre sí.  
    -->


## `PurePath()`

`PurePath()` es la **versión restringida** de `Path()`
que sólo permite manejar *strings* a modo de rutas.


Esta función tiene también sus dos subvariantes:

- `PurePosixPath()`   : dedicada a rutas POSIX (UINIX, Linux, etc).
- `PureWindowsPath()` : dedicada a rutas Windows.


