<a name="top"></a>

## [Volver](../Python.md#funciones)

# Funciones
Una función es un bloque de código reutilizable que ejecuta una sola tarea específica. 


## Llamada

Para *llamar* a una función (es decir, para usarla) se la invoca por su nombre:

```py
<variable_salida> = <funcion>( <valor_entrada> )
```
La función puede disponer o no de un valor de salida , como puede requerir o no valores de entrada. Un ejemplo de función sin valor de retorno es la función *print()* , en tanto que una funcion que a menudo se usa sin argumentos de entradas es *input()*.


## Definicion

La definición de la función es la especificación del nombre de la función y de su rutina interna,es decir su código interior, el cual se ejecutará cada vez que la función sea llamada.

Formato de definición en Python:

```python
# definicion de funcion, sin valores de entrada
def <funcion>():
	# Código función
    # ....
    # final de código


# Código programa principal
# ....
<funcion>()	     # llamada a la función
```

Si la función tiene parámetros de entrada , es decir variables que afectarán al resultado de la función estos se indican entre los paréntesis y separados por comas: 

```python
# definicion de funcion, con valores de entrada
def <funcion>(<parámetro1>, <parametro2>,...):
	# Código función
    # ....
    # final de código


# Código programa principal
# ....
<funcion>(<valor1>, <valor1>, ...)      # llamada a la función
```
Es una buena práctica de estilo dejar **dos renglones vacíos** debajo de cada definición de las funciones. Esto ayuda a interpretar visualmente hasta dónde llega el código de cada función.


## Valor de retorno

Las funciones pueden tener un valor de retorno, es decir un valor de salida. Este se incluye al final de la definición de la función con la sentencia ***return***:

```python
def <funcion>(<parámetro1>, <parametro2>,...):
	# Código función
    # ....
    # final de código
	return <valor_retorno>  # asignacion de retorno


# Código programa principal
# ....
<retorno> = <funcion>( <valor1>, <valor2>, ... )    # llamada a la función
```

La sentencia ***return*** marca el final de la ejecución de la función, por tanto si hay código posterior a esta sentencia no se ejecutará.

El valor por defecto del retorno de las funciones es ***None***.  El valor de retorno en Python puede ser prácticamente de cualquier tipo: un booleano, un string, un numero,una lista, un diccionario, un objeto de una clase especificada, etc. El el caso de no requerirse un valor de retorno el uso de *return* es opcional, tal como se muestra en los ejemplos previos 

En la terminal, si el valor de retorno se asigna a una variable entonces no se muestra en pantalla. Sólo se lo muestra si se pasa a la función *print()*.


## Argumentos
Los ***argumentos*** son los **valores** que se le asignan a los *parámetros* de entrada al llamar a una función.

```python
<función>(<valor1>, <valor2>,...) # funcion con argumentos de entrada asignados
```

### xargs

La función puede aceptar un número indefinido de parámetros (***xargs***), creando una lista interna con el asterisco (**\***) :

```python
def <funcion>( *<variable> ):
	for valor in variables:
        # Código función
        # ....
        # final de código
```

### kargs
Para cargar **parámetros de diccionario** como argumento (*keyword args*,o  ***kwargs***) se usa el doble asterisco:

```python
def <funcion>(**<variable> ):
```

Los argumentos de este tipo de funciones deben explicitarse al llamar a la función (no hay un orden predefinido de argumentos como en otras funciones).



A las funciones se les puede dar valores de entrada por defecto, de modo de poder omitir argumentos al llamarlas:

```python
def <funcion>(<variable1> = <valor1> ,<variable2> = <valor2>):
	#codigo
```
También se las puede llamar con el orden de los argumentos cambiado mediante asignaciones:

```python
<retorno> = <funcion>(<variable2> = <valor2>, <variable1> = <valor1>)
```

## Alcance de una variable (Scope)

Indica dónde se puede usar una variable. Dos opciones:**local** y **global**.

Las variables globales son definidas en el programa principal y son visibles sólo en el programa principal. Para poder acceder a una variable global desde dentro de una función se usa la palabra clave global : 

```python
global <variable_global> 
```
Sin embargo esto se considera una mala práctica y es mejor evitarlo siempre que sea posible.

Las variables locales se definen dentro de las funciones y son de uso exclusivo de la función que las crea.

Ejemplo: 
```python
# definicion de funcion, sin valores de entrada
def triplicar_x( ):
    # variable local: a 
    a = 3
    print(a) 
    # acceso a variable global x
    global x 
    x = x * a 


# Código programa principal
# variable global: x 
x = 7
triplicar_x( )  # '3'       
print(x)        # '21'
print(a)        # ERROR: variable local no visible desde afuera de la funcion
```

## Tipado en las funciones

Las funciones de Python admiten tipado de sus argumentos de entrada y del valor de retorno  para detectar inconsistencias y prevenir posibles errores.

La asignacion del tipo de datos de los argumentos se realiza con el operador **dos puntos**, en tanto que la asignación del tipo de salida se realiza con el **operador flecha** (**->**)

Ejemplo: calcular potencias enteras de un numero flotante
```python
def potencia(a: float, b: int) -> float:    # retorno flotante
    return a**b


x = 2.73
y = 3
valor = potencia(x, y)   
```

## Funciones Recursivas

La recursión consiste en definir algo en función de si mismo. 


Ejemplos clásicos de algoritmos recursivos:

- *serie Fibonacci:*
  
    ```
    fib(n) = fib(n-1) + fib(n-2) 	caso recursivo
	fib(1)=1 , fib(0)=0		        caso base
    ```
- *Factorial:*
  
    ```
    n!=n * (n-1)!	caso recursivo
	1! =0!=1	    caso base
    ```
Las funciones recursivas son funciones que se llaman a sí mismas un numero limitado de veces (*caso recursivo*), cuidando de incluir las condiciones iniciales que permitan resolver la función y detengan la invocación de sí mismas (*caso base)*.

Ejemplo aplicado: función en Python para calcular recursivamente un factorial:
  
```python
# Funcion recursiva
def factorial(n):
    n = int(n)    
    if n > 1:
        m = n * factorial(n-1)	# caso recursivo
    else:
        m = 1       # caso base
    return m


# Ejemplo de uso
for i in range(5):
    print("factorial de: ",i, factorial(i))
```
Las funciones recursivas sirven como alternativa al uso de bucles y a veces permiten resolver algoritmos de forma más simple; sin embargo suelen ocupar mayor uso de memoria por la necesidad de llamarse a sí misma múltiples veces para resolver el algoritmo.


## Función Main() 
Python no requiere indicar explicitamente una función principal (*main*) sino que presupone que la función principal es la rutina del archivo invocado por el usuario o el sistema operativo. En cambio, las rutinas presentes en otros archivos serán consideradas por el intérprete de Python como funciones ó rutinas secundarias.

Para ejecutar una rutina únicamente en el programa principal
(es decir, si se invoca directamente al archivo que las contiene ) se puede englobar la rutina con el siguiente condicional:

```python
if __name__ == "__main__" :
    #rutina de la funcion main
```
Esta forma es útil para crear demos y tests dentro de los archivos donde se crean funcionalidades, clases, etc. de modo que sólo se ejecuten los demos cuando se los llama directamente.

## Argumentos de Main()
Para leer los *argumentos* (valores) que se pasan al invocar el programa desde la terminal se puede usar el módulo *sys* y leer la variable *argv*, la cual es una lista con todos los argumentos en formato texto

```python
import sys      #importacion del módulo del sistema
sys.argv        # lista de argumentos
```

Tener en cuenta que el primer valor de todos es al ruta del archivo del programa.

Ejemplo de uso: si el archivo 'ensayo.py' contenido en la carpeta 'pruebas' tiene el código:

```python
import sys

numero_argumentos = len(sys.argv)

for i in range(numero_argumentos):
    print(i , sys.argv[i])
```
y al llamarlo con la terminal (ej: Bash)  así:

```bash
py .\pruebas\ensayo.py hola 25 'hasta luego'
```
dará como resultado la siguiente lista de argumentos numerados:

```bash
0 .\pruebas\ensayo.py
1 hola
2 25
3 hasta luego
```
Se verifica que el primer argumento es la ruta relativa de archivo. 

----
----
----

## [Inicio](#funciones)

## [Volver](../Python.md#funciones)