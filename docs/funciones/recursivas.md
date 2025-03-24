---
tags:
  - Funciones
---



# Funciones Recursivas

La recursión consiste en definir algo en función de si mismo. 

Las funciones recursivas son funciones que se llaman a sí mismas un numero limitado de veces (*caso recursivo*), cuidando de incluir las condiciones iniciales que permitan resolver la función y detengan la invocación de sí mismas (*caso base)*.

Ejemplos clásicos de algoritmos recursivos:

``` title="Serie de Fibonacci"
fib(n) = fib(n-1) + fib(n-2) 	caso recursivo
fib(1)=1 , fib(0)=0		        caso base
```

``` title="Factorial"
n!=n * (n-1)!	caso recursivo
1! =0!=1	    caso base
```


Las funciones recursivas sirven como alternativa al uso de bucles y a veces permiten resolver algoritmos de forma más simple; sin embargo suelen ocupar mayor uso de memoria por la necesidad de llamarse a sí misma múltiples veces para resolver el algoritmo.

!!! example "Ejemplo aplicado: factorial"

    El factorial se calcula fácilmente con una función recursiva:
    
    ```python title="Factorial recursivo"
    # definicion de funcion recursiva
    def factorial(n):
        n = int(n)    
        if n > 1:
            m = n * factorial(n-1)	# caso recursivo
        else:
            m = 1       # caso base
        return m


    # Ejemplo de uso
    for i in range(5):
        print(f"factorial de {i}: {factorial(i)}")
    ```

