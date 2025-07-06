---
status: new
---

# Doctest

El módulo `doctest` permite aprovechar los *docstrings* (bloques de comentarios) para incorporar tests automáticos para funciones y métodos de clases.


## Importación

El módulo se importa para habilitar los tests:

```py title="Importación"
import doctest
```

## Definicion de tests

Los tests se implementan dentro de los *docstrings*
con la siguiente notación:


```py title="Doctests - sintaxis" hl_lines="5 6 8 9"
def funcion( argumentos ):
    """
    Descripción de función (opcional)

    >>> funcion( valores_entrada_1 )     
    retorno_esperado_1

    >>> funcion( valores_entrada_2 )     
    retorno_esperado_2
    
    ...
    """
    # rutina función
    return retorno_funcion
```

Una misma función puede implementar
tantos ensayos dentro de su bloque de comentarios
como se considere necesario


```py title="Ejemplo de tests "
def suma(a, b):
    """
    Una funcion sencilla que suma.

    >>> suma(3, 4)
    7
    >>> suma(5, 1)
    6
    """
    return a + b
```

Estos ensayos son visibles como parte de la documentación
de las funciones pero no se ejecutan por *default*.


## Ejecución

La ejecución de los tests implementados se ordena tras la defiición de las funciones con la función `testmod()`:

```py title="Doctest - ejecución"
doctest.testmod()
```

Si los resultados obtenidos de todos los ensayos son los esperados
la ejecución continuará normalmente y la consola no indicará nada.
Si en cambio alguno de los tests es incorrecto 
entonces se interrumpirá la ejecución
y la consola indicará el primer error encontrado. 


!!! example "Ejemplo simple"

    ```py title="Ejemplo - test fallido" hl_lines="7 8" 
    import doctest

    def suma(a, b):
        """
        Una funcion sencilla que suma.

        >>> suma(3, 4)       
        7
        >>> suma(5, 1)       
        51
        """
        return a + b


    doctest.testmod()
    ```


    ```txt title="Texto en consola"
    Failed example:
        suma(5, 1)       
    Expected:
        51
    Got:
        6
    ```