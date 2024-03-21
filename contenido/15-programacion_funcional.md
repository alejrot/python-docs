
## [Volver](../README.md#programacion-funcional)

# Programacion Funcional
### Contenidos:
- [Listas por comprensión](#listas-por-comprensión)
- [Funciones Lambda](#funciones-lambda)
- [Funciones de Orden Superior](#funciones-de-orden-superior)
  - [Closures](#closures)
  - [Map()](#map)
  - [Filter()](#filter)
  - [Reduce()](#reduce)
  - [Partial()](#partial)



## Listas por comprensión
las listas por comprensión se basan en el uso de variables calculadas a partir de una iteracion. Algunos ejemplos de listas creadas a partir de un bucle for pueden ser:
```python
<lista_ascendente>  = [ i for i in range(<maximo>)]
<lista_cuadrado>    = [ i * i  for i in range(<maximo>)]
<lista_ambas>       = [ (i, i  * i ) for i in range(<maximo>)]
```

## Funciones Lambda

Las funciones lambda son funciones anónimas, las cuales se se definen así:

```python
lambda <v1> , <v2>:  <expresion>
```
Esta forma de definirlas permite compactar código.

A las funciones lambda se les puede asignar una variable para referenciarlas, el cual servirá como nombre de función:

```python
<variable_lambda> = lambda <v1> , <v2>:  <expresion>
```
Y se llaman como una función normal:

```python
<retorno> = <variable_lambda>(<valor1>,<valor2>)
```
Ejemplo:
```python
# definicion
multiplicar = lambda a, b : a*b		
# uso
resultado = multiplicar(2, 8)
```

Un uso práctico de las funciones simplificadas es crear funciones que sólo se usarán en una única linea de código, ahorrando la definición y asiganción de nombre habitual. Este modo de uso es muy habitual dentro de funciones *map()*, *reduce()*, etc, las cuales se explican más adelante. En este sentido, las funciones lambda son análogas  y se usan de modo sumilar a a las **funciones flecha** de JavaScript.

Otra utilidad de las funciones lambda es crear variantes alternativas de otras funciones, por ejemplo asignándole  valores a algunos argumentos de entrada. 

Por ejemplo: crear varias funciones que calculan distintas potencias de un número de entrada a partir de una función genérica.

```python
# función dos argumentos
def potencia(x,y):
    return x**y

# alias funcion, un argumento prefijado
cuadrado    = lambda n: potencia(n, 2)		# y = 2
cubo        = lambda n: potencia(n, 3)		# y = 3

print( cuadrado(3)  )	# 3² = 9
print( cubo(3)  )		# 3³ = 27

print(type(cuadrado	))       # <class 'function'>
print(type(cubo		))       # <class 'function'>
```
Nótese que las funciones lambda son reconocidas por el intérprete de Python como si fueran funciones normales.

## Funciones de Orden Superior
Son funciones capaces de ejecutar a otras funciones especificadas por el usuario. Estas funciones son indicadas por su nombre como argumento de la funcion de orden superior.

```python
def <funcion_superior> (<valor1>, <valor2>, <funcion_usuario>):
	# código
	...
 	<funcion_usuario>(<parámetros>)
```

Ejemplo:

```python
# Funcion orden superior
def incrementar_4 (x, f):
	# 'f' es una funcion de entrada
 	return f(x) + 4

# Funcion extra
def triplicar(x):
	return x*3

# Uso
x=7
y = incrementar_4(x, triplicar)
print(y)	# Da (x)*3+4 = 25
```

### Closures

Las  *'closures'* son funciones de orden superior que dan como retorno una función definida internamente. 

Sintaxis:
```python
def <nombre_closure>():
	def <funcion_interna>(<argumentos>):
		<rutina>
		return <retorno>
	
	return <funcion_interna>
```

Ejemplo:

```python
#definicion 
def sumar_diez():
	def add(valor):
		return valor + 10
	return add	#funcion interna como retorno

#uso
closure_sumar = sumar_diez()
print(closure_sumar(7))		# da 10 + 7 = 17
```

Una utilidad posible de las closures en englobar varias funciones internas alternativas y poder elegir una u otra dependiendo de un argumento.

### Map()

La función *map()* es una funcion de orden superior que facilita el procesamiento de listas por una función especificada, "mapeando" cada elemento de la lista con los argumentos de la funcion y evitando así el uso de bucles y la asignacion elemento a elemento.

Sintaxis:
```python
<objeto_resultado> = map(<funcion>, <lista>)
```

El retorno de la funcion map() es un objeto de clase 'map' (una *instancia*). Con la función *list()* se convierte dicho objeto en una lista de valores, recuperando así los resultados de la función interna. 

Ejemplo: elevar al cuadado todos los elementos de un vector

```python
vector = [2, 5, 14, 3]

def potencia_2 (x):
	return x**2

objeto = map(potencia_2, vector)
cuadrado = list(objeto)
```

*map()* acepta funciones *lambda* como argumento. Ejemplo:

```python
vector = [2, 5, 14, 3]

cuadrado = list(map(lambda numero: numero **2 , vector) )
```

### Filter()

*filter()* es una función que filtra de la lista de entrada los valores que cumplen con una condición lógica definida por una función especificada.  

Sintaxis:
```python
<objeto_filtrados> = filter(<funcion_logica>, <lista>)
```
Nuevamente la salida es un objeto de la clase 'filter' y para leer la lista de elementos filtrados hay que recurrir a la funcion *list()*.

Ejemplo: filtrar valores numericos mayores a diez de un vector

```python
vector = [2, 5, -1, 48,-9,-25, 14, 3]

def mayor_a_10(x):
    return True if x > 10 else False  

objeto= filter(mayor_a_10, vector)
filtrados = list(objeto)
```
*filter()* también acepta funciones lambda como argumento. 


### Reduce()

*reduce()* opera con todos los elementos de una lista de entrada, aplicándoles una función especificada de manera acumulativa. Esto permite trabajar con un número no predeterminado de argumentos agrupados dentro de una lista de entrada. Para ser utilizada debe ser importada previamente desde el módulo *functools*:
```python
from functools import reduce
```
Ejemplo: una productoria (producto sucesivo) de números englobados en una lista

```python
from functools import reduce

vector = [2, 5, -1, -3]

def producto(x, y):
    return x*y

productoria = reduce(producto, vector)
# 'productoria' es 2*5*(-1)*(-3) = 30
```
Como el retorno de la función *reduce()* es un valor no hace falta hacer conversiones de tipo adicionales.


### Partial()

La función *partial()* permite asignar valores prefijados a una función como argumentos. Devuelve como retorno un objeto de clase *'partial'* el cual incluye toda la información agregada y que puede utilizarse como si fuera una función lambda. De esta forma con *partial()* se puede crear una o varias funciones simplificadas.

La función *partial()* debe importarse desde el módulo **functools**:

```python
from functools import partial
```

El formato general de esta función es:

```python
<funcion_lambda> = partial( <nombre_funcion>, <arg1> = <v1>, <arg2> = <v2>, ...)
```
En caso de no indicarse los nombres de los argumentos éstos se asignarán en orden de definición.

**Ejemplo Nº1:** crear varias funciones que calculan distintas potencias de un número de entrada.

```python
# función general, dos parámetros 
def potencia(x, exponente):
    return x**exponente


# se crean objetos 'partial' para casos particulares
cuadrado = partial( potencia, exponente = 2 )
cubo	 = partial( potencia, exponente = 3 ) 
```
Estas funciones se usan fácilmente invocándolas por su nombre:

```python
x = 3	# valor de entrada

print( cuadrado(x))		# 3² = 9
print( cubo    (x))		# 3³ = 27

print(type(cubo))  # devuelve " <class 'functools.partial'> "
```

**Ejemplo Nº2:** crear una lista de funciones que calculan distintas potencias de un número de entrada.

```python
# función general, dos parámetros 
def potencia(x, exponente):
    return x**exponente

# lista de funciones lambdas
potencias = []
for i in range(10):
	# se fija el exponente
    p = partial( potencia, exponente = i )
    potencias.append(p)
```
De este modo el índice de la función lambda elegida representa el exponente elegido:

```python
x = 3	# valor de entrada

print( potencias[0](x) )		# 3⁰ = 1
print( potencias[1](x) )		# 3¹ = 3
print( potencias[2](x) )		# 3² = 9
print( potencias[3](x) )		# 3³ = 27
print( potencias[4](x) )		# 3⁴ = 81
# ...
```



----
----
----

## [Inicio](#programacion-funcional)

## [Volver](../README.md#programacion-funcional)