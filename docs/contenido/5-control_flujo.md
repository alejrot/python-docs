

# Control de Flujo


## Saltos condicionales y bucles

El control de flujo se realiza mediante saltos condicionales (cláusulas `if`, `else`, etc) y mediante bucles condicionales (`while`, `for`).


## Saltos Condicionales

### Clausula `if` (*"si"*)

Ejecuta un trozo de código solamente si el primer condicional es verdadero (retorna 'True').

```python title="condicional if"
if condicion:
	# SI condicion == 'True':
	# código_condicional
```

### Cláusula `else` (*"sino"*  )

Permite agregar rutinas que se ejecutan si las condiciones pevias no se cumplen.


```python title="condicional if-else"
if condicion:
	# SI condicion == 'True':
	# código_condicional
else:
	# SI condicion ==  'False':
	# codigo_alternativo
```
### Cláusula `elif` (*"sino si"*)

Permite agregar rutinas con condicionales  alternativos a la primera condición.  
```python title="condicional if-elif-else"
if condicion_1:
	# SI condicion_1 == 'True':
	# código_condicional
elif condicion_2:
	# SI condicion_1 ==  'False' Y condicion_2 == 'True':
	# codigo_condicional_alternativo
else:
	# SI condicion_1 ==  'False' Y condicion_2 == 'False':
	# codigo_alternativo_defecto
```

Puede haber múltiples cláusulas elif pero sólo una else y una sola if.


!!! hint "Dos puntos" 
	Prestar atención a los dos puntos ( `:` ), los cuales marcan el final de cada condicional.

!!! warning "Indentación"
	Hay que respetar la **indentación** que impone Python para que el programa funcione, de otro modo el programa se interrumpe. 

	Es habitual en Python usar cuatro espacios para el tabulado; 


Hay una forma resumida para escribir la clausula *if - else* en un solo rengón, esta es:
```python
instruccion1 if <condicion> else instruccion2
```


## Bucles condicionales


### Ciclos `while` (*"mientras"*)

Estructura de control que repite una instrucción o rutina mientras su condición de control se cumpla. Este tipo de bucles no tiene un numero predeterminado de iteraciones. Si la condición siempre es verdadera entonces el bucle será infinito. Verificar que la condición de control se haga falsa eventualmente para permitir la salida del bucle es responsabilidad del programador. Formato:

```python title="bucle while"
while condicion:	# 'mientras condición == True:'
	# rutina
	# actualizacion variable control
```

Para forzar la interrupción la ejecución de un bucle se puede usar la orden `break`, esto se hace dentro de un condicional interno del bucle. 

Si en cambio el bucle es infinito (`while True`) es indispensable incluir la orden `break` con un condicional acorde:

```python title="bucle while-True"
while True:	# 'mientras SIEMPRE'
	# rutina
	# actualizacion variable control
	if condicion_escape:
		break

```

El bucle while puede ser usado en conjunción con el condicional `else` lo cual permite ejecutar una rutina alterna al bucle:

```python title="bucle while-else"
while condicion:	# 'mientras condición == True:'
	# rutina
	# actualizacion variable control
else:				# 'sino:'
	#rutina alterna
```
!!! tip "Hint: cancelar ejecución"  
	Si se ejecuta un prograam con un bucle infinito es posible interrumpirlo apretando **‘Ctrl’ + ‘C’**

### Ciclos `for` (*"para"*)

Estructura de control que repite una instrucción o rutina un número predefinido de veces. El fin del bucle se indica con el indentado, por tanto debe respetarse. Formato habitual:

```python title="bucle for - range()"
for indice in range(inicio, fin, incremento):
	# Instruccion1
	# Instruccion2
	# …
```

La variable `indice` es la variable que mantiene el conteo de las repeticiones. Tener en cuenta que el valor `fin` no se alcanza, sino que el bucle se interrumpe justo un ciclo antes. Si `inicio` es cero (`0`) no hace falta indicarlo. Y si el `incremento` es unitario (`1`) entonces tampoco hace falta indicarlo.

```python title="Ejemplo: contar hasta tres"
for i in range(4):
	# i: variable indice
	print(i)		# da los números del cero al tres.
```
Nótese el uso de una función dentro del bucle llamada `range()`. Ésta es una función que retorna una lista (`list`) con los valores enteros entre los números `inicio` y `fin` (sin incluir este último) y con el `incremento` indicado. Ejemplos:

```python title="función range() - completa"
inicio = 3
fin = 12
incremento = 2 
lista_enteros = range(inicio, fin, incremento) # '[3, 5, 7, 9, 11]'
```

```python title="función range() - mínimo "
fin = 5
lista_enteros = range( fin) # '[0, 1, 2, 3, 4]'
```

A diferencia de otros lenguajes de programación, Python implementa el bucle `for` en base a recorrer un vector de elementos, una 'lista'. Esto permite implementar bucles `for` que no requieran el uso de variables indice sino que usan directamente los elementos internos, sean del tipo que sean. Formato: 

```python title="bucle for - lista"
lista_elementos: list
for elemento in lista_elementos:
	# Instruccion1
	# Instruccion2
	# …
```

El bucle for puede aplicarse sobre strings, listas, tuplas y diccionarios:  

```python title="Ejemplo: recorrer string"
texto = "hola mundo"
for letra in texto:   	#'texto' es 'str'
	print(letra)		# muestra una letra a la vez
```

 Listas y tuplas muestran un comportamiento análogo (un elemento por iteración), en tanto que los diccionarios podrían recorrerse así:

```python title="recorrer claves de diccionario"
for clave in diccionario:
	print(clave)
```
muestra las claves del diccionario una por una, en tanto que para mostrar los valores se puede usar el método `values()`:

```python title="recorrer valores de diccionario"
for valor in diccionario.values():
	print(valor)
```
Para consultar ambos elementos de a pares se puede recurrir al método `items()` :

```python title="recorrer pares clave-valor de diccionario"
for clave, valor in diccionario.items():
	print(clave, valor)
```

!!!info "`break` y `continue`"
	Para interrumpir el bucle antes de tiempo se puede usar la orden `break` asociada a un condicional. Como contrapartida de `break` existe la orden `continue` (similar al `goto` de C) sin embargo su uso es considerado actualmente como una mala práctica.
