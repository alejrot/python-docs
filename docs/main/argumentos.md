---
tags:
  - main
  - sys
  - Argumentos
  - Modulos
---



# Argumentos de `main()`

## *argument values* (`argv`)

Para leer los *argumentos* (valores) que se pasan al invocar el programa desde la terminal se puede usar el módulo `sys` y leer la variable `argv`, 
la cual es una lista con todos los valores ingresados
de argumentos en formato texto:

```python title="argument values (argv)"
from sys import argv      #importacion del módulo del sistema

lista_valores = argv        # lista de argumentos

argumento_0 = argv[0]   # ruta del programa
argumento_1 = argv[1]   # 1º argumento de entrada
argumento_2 = argv[2]   # 2º argumento de entrada
# ....
```

!!! info "argv[0]"
    Tener en cuenta que el primer valor de todos (`argv[0]`) es la ruta relativa del archivo del programa.

!!! example "Ejemplo 1: nombre y argumentos"
    Un archivo 'entrada.py' con el código:

    ```python
    import sys

    numero_argumentos = len(sys.argv)

    for i in range(numero_argumentos):
        print(i , sys.argv[i])
    ```
    y al llamarlo con la terminal (ej: Bash)  así:

    ```bash
    py entrada.py hola 25 'hasta luego'
    ```
    dará como resultado la siguiente lista de argumentos numerados:

    ```bash title="Texto de salida"
    0 entrada.py
    1 hola
    2 25
    3 hasta luego
    ```
    Se observa que el primer argumento coincide con el **nombre** del archivo de programa.

!!! example "Ejemplo 2: ruta y argumentos"
    Si la rutina previa está alojada en un subdirectorio llamado 'carpeta':

    ```bash title="Texto de salida"
    py carpeta/entrada.py hola 30 'hasta luego'
    ```

    dará como resultado esta vez:

    ```bash title="Texto de salida"
    0 carpeta/entrada.py
    1 hola
    2 30
    3 hasta luego
    ```
    Se verifica entonces que el primer argumento es la **ruta relativa** del archivo de programa.


Más información sobre los argumentos de `main()`: [módulo `sys`](../modulos/sys.md#argumentos-de-entrada)



## Otras opciones

Python dispone de varios módulos estándar para la lectura de los argumentos,
los cuales permiten mayor versatilidad y configuraciones.
Estos son:

- `getopt`;
- `optparse`;
- `argparse`;

El más recomendado para su uso en proyectos es el [**módulo argparse**](../argparse/index.md)



