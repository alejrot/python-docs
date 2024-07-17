

# Programacion Funcional


## Listas por comprensión (*comprehension*)
las listas por comprensión se basan en el uso de variables calculadas a partir de una iteración. Algunos ejemplos de listas creadas a partir de un bucle for pueden ser:

```python title="Listas por comprensión"
lista_ascendente  = [ i for i in range(<maximo>)]
lista_cuadrado    = [ i * i  for i in range(<maximo>)]
lista_ambas       = [ (i, i  * i ) for i in range(<maximo>)]
```

## Funciones Lambda

Las funciones lambda son funciones anónimas, las cuales se se definen así:

```python title="funcion lambda - sin nombre"
lambda v1 , v2:  expresion
```
Esta forma de definirlas es útil para **definir manejadores** (***handlers***), es decir funciones que se ejecutan ante eventos específicos del programa.


!!! tip "Tip: manejadores (handlers)"

	```python title="Asignación de handlers - función común"
	# definicion
	def nombre_funcion(x):
		return expresion(x)

	# asignacion
	handler_evento = nombre_funcion
	```

	Con el uso de funciones lambda, esta rutina se reduce a:

	```python title="Asignación de handlers - funcion lambda"
	# defincion y asignacion en un solo pao
	handler_evento = lambda v1 , v2:  expresion
	```

	Las funciones lambda son análogas  y se usan de modo sumilar a a las **funciones flecha** de JavaScript.



Otro uso práctico de las funciones simplificadas es crear funciones que sólo se usarán en una única linea de código, ahorrando la definición y asiganción de nombre habitual. Este modo de uso es muy habitual dentro de funciones `map()`, `reduce()`, etc, las cuales se explican más adelante.


Si se requiere reutilización, a las funciones lambda se les puede asignar una variable para referenciarlas, el cual servirá como nombre de función:

```python title="funcion lambda - con nombre"
variable_lambda = lambda v1 , v2:  expresion
```
Y se llaman como una función normal:

```python title="funcion lambda - llamado"
retorno = variable_lambda(valor_1,valor_2)
```


!!! example "función lambda: multiplicación"
	```python title="definición"
	multiplicar = lambda a, b : a*b		
	```
	```python title="uso"
	resultado = multiplicar(2, 8)
	```


!!! tip "Tip: funciones con argumentos preasignados"
	Con las funciones lambda se puede crear variantes alternativas de otras funciones, por ejemplo asignándole  valores a algunos argumentos de entrada. Por ejemplo: crear varias funciones que calculan distintas potencias de un número de entrada a partir de una función genérica.
	
	```python title="Alias de funciones"
	# función con dos argumentos
	def potencia(x,y):
		return x**y

	# alias funcion, un argumento prefijado
	cuadrado    = lambda n: potencia(n, 2)		# y = 2
	cubo        = lambda n: potencia(n, 3)		# y = 3
	```

	```python title="llamado y tipo"
	# uso
	print( cuadrado(3)  )	# 3² = 9
	print( cubo(3)  )		# 3³ = 27

	# tipo
	print(type(cuadrado	))       # <class 'function'>
	print(type(cubo		))       # <class 'function'>
	```


!!! info
	Nótese que las funciones lambda son reconocidas por el intérprete de Python como si fueran funciones normales.

## Funciones de Orden Superior
Son funciones capaces de ejecutar a otras funciones especificadas por el usuario. Estas funciones son indicadas por su nombre como argumento de la funcion de orden superior.

```python title="funcion de orden superior"
def funcion_superior (valor_1, valor_2, funcion_usuario):
	# codigo
	# ...
 	funcion_usuario(parametros)
	# ...
```


```python title="ejemplo"
# Funcion orden superior
def incrementar_4 (x, f):
	# 'f' es una funcion de entrada
 	return f(x) + 4

# Funcion externa
def triplicar(x):
	return x*3

# Uso
x = 7
y = incrementar_4(x, triplicar)
print(y)	# Da (x)*3+4 = 25
```

### Closures

Las  *'closures'* son funciones de orden superior que dan como retorno una función definida internamente. 

```python title="Closures - Sintaxis" 
def nombre_closure():
	def funcion_interna(argumentos):
		# rutina
		return retorno
	
	return funcion_interna
```


```python title="Ejemplo closure"
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

Otra utilidad posible es la creación de decoradores, los cuales agregan características a las funciones. [Más sobre los decoradores de Python.](decoradores.md)

### Map

La función `map()` es una funcion de orden superior que facilita el procesamiento de datos iterables  (particularmente: listas) por una función especificada, "mapeando" cada elemento de los datos de entrada con los argumentos de la funcion y evitando así el uso de bucles y la asignacion elemento a elemento.

Sintaxis:
```python
objeto_resultado = map(funcion, data_entrada_1, data_entrada_2, ...)
```

El retorno de la funcion map() es un objeto de clase `map` (una *instancia*). Con la función `list()` se convierte dicho objeto en una lista de valores, recuperando así los resultados de la función interna. 


```python  title="map() - procesamiento de listas"
objeto_resultado = map(funcion, lista_entrada)
resultado = list(objeto_resultado)
```



Ejemplo: elevar al cuadado todos los elementos de un vector

```python hl_lines="5"  title="map() - ejemplo uso"

def potencia_2 (x):
	return x**2

vector = [2, 5, 14, 3]
objeto = map(potencia_2, vector)
cuadrado = list(objeto)
```

La funcion `map()` admite multiples listas de entrada

```python hl_lines="5" title="map() - múltiples iterables"
def multiplicar(x,y):
    return x*y

vector = [2, 5, 14, 3]
objeto = map(multiplicar, vector, vector)
cuadrado = list(objeto)

```

`map()` acepta funciones *lambda* como argumento. Ejemplo:

```python hl_lines="3" title="map() - uso lambdas"
vector = [2, 5, 14, 3]

cuadrado = list(map(lambda numero: numero **2 , vector) )
```

### Filter

`filter()` es una función que filtra de la lista de entrada los valores que cumplen con una condición lógica definida por una función especificada.  

Sintaxis:
```python  title="filter() - sintaxis"
objeto_filtrados = filter(funcion_logica, data_entrada)
```
Nuevamente la salida es un objeto de la clase `filter` y para leer la lista de elementos filtrados hay que recurrir a la funcion `list()`.

Ejemplo: filtrar valores numericos mayores a diez de un vector

```python title="ejemplo: valores mayores a 10"
def mayor_a_10(x):
	return True if x > 10 else False  

vector = [2, 5, -1, 48,-9,-25, 14, 3]
objeto= filter(mayor_a_10, vector)
filtrados = list(objeto)
```

`filter()` también acepta funciones lambda como argumento. 


### Reduce

`reduce()` opera con todos los elementos de una lista de entrada, aplicándoles una función especificada de manera acumulativa. Esto permite trabajar con un número no predeterminado de argumentos agrupados dentro de una lista de entrada. Para ser utilizada debe ser importada previamente desde el módulo *functools*:
```python title="Importación de reduce()"
from functools import reduce
```
Ejemplo: una productoria (producto sucesivo) de números englobados en una lista

```python hl_lines="5" title="ejemplo: reduce() para hacer productoria"
def producto(x, y): 
    return x*y

vector = [2, 5, -1, -3]
productoria = reduce(producto, vector)
# 'productoria' es 2*5*(-1)*(-3) = 30
```
Como el retorno de la función `reduce()` es un valor no hace falta hacer conversiones de tipo adicionales.


### Partial

La función `partial()` permite asignar valores prefijados a una función como argumentos. Devuelve como retorno un objeto de clase *'partial'* el cual incluye toda la información agregada y que puede utilizarse como si fuera una función lambda. De esta forma con `partial()` se puede crear una o varias funciones simplificadas.

La función `partial()` debe importarse desde el módulo **functools**:

```python title="Importación de partial()"
from functools import partial
```

El formato general de esta función es:

```python title="Sintaxis de partial()"
objeto_partial = partial( nombre_funcion, arg1 = valor_1, arg2 = valor_2, ...)
```
En caso de no indicarse los nombres de los argumentos éstos se asignarán en orden de definición.

Los objetos partial se usan igual que cualquier función:

```python title="Uso de partial()"
valor = objeto_partial(argunentos)
```

!!! example "Ejemplo Nª1: cuadrado y cubo con partial()"
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

	```python hl_lines="6"
	x = 3	# valor de entrada

	print( cuadrado(x))		# 3² = 9
	print( cubo    (x))		# 3³ = 27

	print(type(cubo))  # devuelve " <class 'functools.partial'> "
	```


!!! example "Ejemplo Nª2: potencias con partial()"
	En este ejemplo se crea una lista de funciones que calculan distintas potencias de un número de entrada.

	```python title="definicion de partials"
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

	```python title="uso de partials"
	x = 3	# valor de entrada

	print( potencias[0](x) )		# 3⁰ = 1
	print( potencias[1](x) )		# 3¹ = 3
	print( potencias[2](x) )		# 3² = 9
	print( potencias[3](x) )		# 3³ = 27
	print( potencias[4](x) )		# 3⁴ = 81
	# ...
	```



