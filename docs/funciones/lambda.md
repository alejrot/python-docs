---
tags:
  - Funciones
---


# Funciones Lambda

Las funciones lambda son funciones anónimas, las cuales se definen así:

```python title="funcion lambda - sin nombre"
lambda v1 , v2:  expresion
```

Un uso práctico de las funciones simplificadas es crear funciones que sólo se usarán en una única linea de código,
ahorrando la definición y asiganción de nombre habitual.
Este modo de uso es muy habitual dentro de funciones `map()`, `reduce()`, etc, las cuales se explican más adelante.


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


!!! info "Funciones flecha"

	Las funciones lambda son análogas a las **funciones flecha** de JavaScript y se usan de modo similar.


