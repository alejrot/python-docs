---
tags:
  - Funciones
  - docstring
  - Documentacion
---


# Docstrings

Los *docstrings* son textos de ayuda que se incluyen
en la definición de las funciones.
Funcionan a modo de manual para su consulta por los desarrolladores.

## Definición

Los docstrings se definen justo al abrir la definición de la función
y el texto se engloba entre triple corchete simple(`'''`)
o entre triple corchete doble (`"""`).

Ejemplo: 

```py title="Docstring - definición"
def potencia(base: float, exp: int) -> float:
    """
    Esta funcion calcula la potencia deseada de un número.
    
    Argumentos:
        b  (float): el numero base elegido
        exp(int): el exponente deseado  

    Retorno:
        float: el valor resultante
    """
    return base**exp
```

## Manual - `help`

El manual se puede desplegar con la función `help` desde dentro de la rutina:

```py title="Docstring - lectura en manual"
# ventana de ayuda
help(potencia)
```

El reporte lanzado en consola tiene un aspecto como el siguiente:

``` hl_lines="1 11" title="Docstring - reporte en consola"
Help on function potencia in module __main__:

potencia(base: float, exp: int) -> float
    Esta funcion calcula la potencia deseada de un número.

    Argumentos:
        b  (float): el numero base elegido
        exp(int): el exponente deseado
    
    ...
Help on potencia line 1 (press h for help or q to quit)
```

!!! tip "IDE"

    Los editores de texto tipo IDE
    incorporan funcionalidades y extensiones
    para desplegar los *docstrings* automáticamente
    cuando el desarrollador apunta sobre el nombre de las funciones.




## Lectura

La función creada tiene un método especial llamado `__doc__` donde se guarda el texto del *docstring*.
Éste puede ser leído para su uso en otras partes del programa.

Ejemplo:

```py title="Docstring - lectura como string"
info = potencia.__doc__
# texto por consola
print(info)
```

## Referencia

[Geeks for Geeks - Python Docstrings](https://www.geeksforgeeks.org/python-docstrings/)

[Python.org - PEP 257](https://peps.python.org/pep-0257/)