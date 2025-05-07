---
tags:
  - Argumentos
  - argparse
---

# Analizador




prog
usage
description
epilog

prefix_chars
fromfile_prefix_chars
argument_default

exit_on_error 
conflict_handler


add_help






```py
# nuevo analizador ('parser') 
analizador = argparse.ArgumentParser(
    prog="nombre_programa",
    usage='%(prog)s [opciones]',
    description="Descripción del programa",
    epilog='Texto al final de la ayuda',
    )
```

El texto obtenido por consola es algo como esto:

```
usage: nombre_programa [opciones]

Descripcion del programa

options:
  -h, --help     show this help message and exit

Texto al final de la ayuda
```

??? info "Rutina completa"


    ```py
    # importacion
    import argparse

    # nuevo analizador ('parser') 
    analizador = argparse.ArgumentParser(
        prog="nombre_programa",
        usage='%(prog)s [opciones]',
        description="Descripcion del programa",
        epilog='Texto al final de la ayuda',
        )

    # lectura de argumentos
    argumentos = analizador.parse_args()
    ```







