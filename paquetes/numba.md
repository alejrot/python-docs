
# Numba


Numba permite compilar funciones de Python en tiempo de ejecución. Esto suele ayudar a mejorar los tiempos de ejecucion de la función.


## Instalacion

El paquete numba se instala con PIP

```bash
pip install numba
```


## Compilacion

La compilacion se ordena de forma genérica con el decorador **\@jit**:


```py
import numba

# funcion compilada
@numba.jit
def funcion( arg):
    # rutina
    return 

```

Sintaxis alternativa: 
```py
from numba import jit

# funcion compilada
@jit
def funcion( arg):
    # rutina
    return 

```

**Ejemplo aplicado:** búsqueda de numeros primos. Se crean dos funciones iguales , pero una lleva el decorador jit y la otra no.

Función interpretada pura:
```py
def numeros_primos(numero_maximo):
    """Devuelve una lista con los numeros primos encontrados con valor menor al indicado."""""
    #esta funcion verifica qué numeros son primos descartando los numeros divisibles por enteros previos
    #los numeros primos se guardan en una lista
    primos = [2]
    #se prueba cada numero candidato, uno a uno
    #sólo se verifican numeros impares: mejora casi imperceptible
    for valor in range(3,numero_maximo+1,2):
        divisible = False
        # sólo se divide por numeros primos ya encontrados 
        # los numeros no primos son redundantes
        for indice in range(0,len(primos)):
            divisor = primos[indice]
            if valor % divisor == 0:
                divisible = True
                break
        #si no es divisible se cuenta como primo
        if divisible == False:
            primos.append(valor)
    return primos     
```

Funcion con compilacion:
```py
@jit    # decorador de Numba
def numeros_primos_compilado(numero_maximo):
    """Devuelve una lista con los numeros primos encontrados con valor menor al indicado."""""
    #esta funcion verifica qué numeros son primos descartando los numeros divisibles por enteros previos
    #los numeros primos se guardan en una lista
    primos = [2]
    #se prueba cada numero candidato, uno a uno
    #sólo se verifican numeros impares: mejora casi imperceptible
    for valor in range(3,numero_maximo+1,2):
        divisible = False
        # sólo se divide por numeros primos ya encontrados 
        # los numeros no primos son redundantes
        for indice in range(0,len(primos)):
            divisor = primos[indice]
            if valor % divisor == 0:
                divisible = True
                break
        #si no es divisible se cuenta como primo
        if divisible == False:
            primos.append(valor)
    return primos     
```

Se creó una rutina que [ejecuta recursivamente estas funciones](numba/primos_numba.py). Al requerir la búsqueda de numeros primos por debajo de 10 mil: 

```bash
py primos_numba.py 10000
```
se obtuvieron tiempos de ejecución como estos:

|Interpretado| Compilado|
|:---:|:---:|
|92 mseg|560 mseg|
|90 mseg| 4 mseg|
|89 mseg| 4 mseg|

La compilación introdujo una penalización notable en el tiempo de la primera ejecución; sin embargo a partir de la segunda ejecución el tiempo se redujo más de veinte veces. 

Al repetir la búsqueda con tope en 40 mil:

```bash
py primos_numba.py 40000
```
Los nuevos tiempos fueron los siguientes:

|Interpretado| Compilado|
|:---:|:---:|
|1162 mseg| 660 mseg|
|1160 mseg| 44 mseg|
|1156 mseg| 44 mseg|

En este caso de mayor demanda computacional se obtiene una mejora para todos los ciclos.

Por tanto, debe analizarse en cada caso si es buena idea o no introducir la compilación.



