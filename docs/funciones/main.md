---
tags:
  - Funciones
  - main
  - sys
  - Argumentos
  - Retorno
  - Modulos
  - Procesos
---

# Función `main()`

La función `main()` es, 
como su nombre indica,
la función que incluye la rutina principal del programa.
Esta rutina principal es siempre el lugar por donde comienza a ejecutarse el programa 
y, salvo indicación contraria, 
es donde también termina la ejecución. 


## Sintaxis 

Python no requiere indicar explicitamente una función principal (*main*) sino que presupone que la función principal es la rutina del archivo invocado por el usuario o el sistema operativo. 
A esta función el intérprete de Python le da el nombre "`#!py __main__`"
y dicho valor se consulta desde la variable especial `#!py __name__`
. 

En cambio, las rutinas presentes en otros archivos serán consideradas por el intérprete de Python como funciones ó rutinas secundarias.

Esta diferenciación es importante cuando se usan módulos en un programa, pues estos no quedan incluidos 
como parte de la función `main()`.

## Rutina exclusiva de `main()`

Para ejecutar una rutina únicamente en el programa principal
(es decir, si se invoca directamente al archivo que las contiene) se puede englobar la rutina con el siguiente condicional:

```python title="Rutina exclusiva de main()"
if __name__ == "__main__" :
    #rutina de la funcion main
```
Esta forma es útil para crear demos y tests dentro de los archivos donde se crean funcionalidades, clases, etc. de modo que sólo se ejecuten los demos cuando se los llama directamente.

## Argumentos de `main()`

Para leer los *argumentos* (valores) que se pasan al invocar el programa desde la terminal se puede usar el módulo `sys` y leer la variable `argv`, la cual es una lista con todos los argumentos en formato texto

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


## Valor de retorno

La rutina principal puede tener un valor de retorno.
Este valor puede ser una simple variable 
que indique el éxito o el fracaso del procesamiento interno
.

El valor de retorno se envía con ayuda de la función `exit()` incluida en el módulo `sys`:

```py   title="Valor de retorno"
import sys


if __name__ == "__main__":
    # (Rutina principal)
    print("Rutina principal completa")
    sys.exit(0)         # codigo ejecución exitosa      
```

Esta función indica la intensión de salir del intérprete 
y su argumento es el valor de retorno.



Los valores habituales de salida son los siguientes:

|Valor| Significado|
|:---:|:---|
|`0`, `None`| Terminación exitosa|
|`1`| Error genérico|
|`2`| Error (sólo sintaxis de línea de comandos) |


El valor de retorno también puede ser un valor o una estructura de datos completa;
sin embargo 
estos casos deben manejarse con más cuidado 
porque dichos valores pueden ser malinterpretados como códigos de error.


## Encapsular rutina principal

Se puede englobar la rutina principal 
y pasarla como argumento a la función `exit()`: 

```py   title="Rutina principal encapsulada"
import sys


# funcion wrapper
def principal():
    # (Rutina principal)
    print("Rutina principal completa")
    return 0    # valor de retorno


if __name__ == "__main__": 
    sys.exit(principal())    
```

de esta forma 
el intérprete ejecutará
la función *wrapper* (envolvente)
y su valor de retorno 
se pasará a la shell al terminar.



<!-- 
Estos valores pueden ser mostrados en consola (Bash, Powershell, etc)
en caso que la rutina sea llamada desde una *shell*.

En caso que el programa Python sea llamado por un proceso (un "programa") del sistema operativo
o por otras aplicaciones,
el valor de retorno será recibido como un argumento


sino que puede ser concatenada con otras rutinas de más jerarquía:
otras aplicaciones, 
procesos del sistema operativo, 
etc.
 -->




## Referencias

[Documentación oficial - `__main__`](https://docs.python.org/es/3/library/__main__.html)

[Documentación oficial - sys](https://docs.python.org/es/3/library/sys.html)