
## [Volver](../README.md#condicionales-y-bucles)

# Control de Flujo

### Contenidos:
-  [Saltos condicionales y bucles](#saltos-condicionales-y-bucles)
-  [Saltos Condicionales](#saltos-condicionales)
  - [Clausula IF](#clausula-if)
  - [Cláusula ELSE](#cláusula-else)
  - [Cláusula ELIF](#cláusula-elif)
- [Bucles Condicionales](#bucles-condicionales)
  - [Ciclos WHILE](#ciclos-while)
  - [Ciclos FOR](#ciclos-for)


## Saltos condicionales y bucles

El control de flujo se realizamediante saltos condicionales (cláusulas if, else, etc) y mediante bucles condicionales (while, for).

**Importante:** hay que respetar la **indentación** que impone Python para que el programa funcione. Prestar atención a los dos puntos ( **:** )

## Saltos Condicionales

### Clausula IF
Ejecuta un trozo de código solamente si el condicional es verdadero (retorna 'True') 

```python
if <condicion>:
	#código_condicional
```

### Cláusula ELSE

```python
if <condicion>:
	#código_condicional
else:
	#codigo_alternativo
```
### Cláusula ELIF

```python
if <condicion1>:
	#código_condicional
elif <condicion2>:
	#codigo_condicional_alternativo
else:
	#codigo_alternativo_defecto
```

Puede haber múltiples cláusulas elif pero sólo una else y una sola if.

Hay una forma de escribir la clausula *if - else* en un solo rengón, esta es:
```python
instruccion1 if <condicion> else instruccion2
```
## Bucles condicionales


### Ciclos WHILE

Estructura de control que repite una instrucción o rutina mientras su condición de control se cumpla. Este tipo de bucles no tiene un numero predeterminado de iteraciones. Si la condición siempre es verdadera entonces el bucle será infinito. Verificar que la condición de control se haga falsa eventualmente para permitir la salida del bucle es responsabilidad del programador. Formato:

```python
while <condicion>:
	# rutina
	# actualizacion variable control
```

Para forzar la interrupción la ejecución de un bucle se puede usar la orden break, esto se hace dentro de un condicional interno del bucle. Si el bucle es infinito (*while True*) es indispensable incluir la orden break con un condicional acorde.
El bucle while puede ser usado en conjunción con el condicional else lo cual permite ejecutar una rutina alterna al bucle:

```python
while <condicion>:
	# rutina
	# actualizacion variable control
else:
	#rutina alterna
```
**Hint:** Si se ejecuta un bucle infinito es posible interrumpirlo apretando **‘Ctrl’ + ‘C’**

### Ciclos FOR

Estructura de control que repite una instrucción o rutina un número predefinido de veces.El fin del bucle se indica con el indentado, por tanto debe respetarse. Formato:

```python
for <entero> in range(<inicio>, <fin>):
	# Instruccion1
	# Instruccion2
	# …
```
La variable \<entero\> es la variable que mantiene el conteo de las repeticiones. Tener en cuenta que el valor \<fin\> no se alcanza, sino que el bucle se interrumpe justo un ciclo antes. 

*range()*  es una función y retorna los valores entre el inicio y el fin, sin incluir este último. Si \<inicio\> es cero no hace falta indicarlo. Ejemplo:

```python
for i in range(4):
	print(i)
```

da los números del cero al tres.
Por defecto el incremento de <entero> es unitario. Para cambiarlo se escribe:

```python
for <entero> in range(<inicio>, <fin>, <incremento>):
	# Instruccion1
	# Instruccion2
	# …
```
Para interrumpir el bucle antes de tiempo se puede usar la orden ***break*** asociada a un condicional. Como contrapartida de *break* existe la orden *continue* (similar al '*goto*' de C) sin embargo su uso es considerado actualmente como una mala práctica.

El bucle for puede aplicarse sobre strings, listas, tuplas y diccionarios. 
Por ejemplo: 

```python
for letra in “bucle”:   # "bucle" es string 
	print(letra)
```

muestra en pantalla todas las letras del string “bucle” de una en una. Listas y tuplas muestran un comportamiento análogo (un elemento por iteración), en tanto que los diccionarios podrían recorrerse así:

```python
for clave in diccionario:
	print(clave)
```
muestra las claves del diccionario una por una, en tanto que para mostrar los valores se puede usar el método *.values()*:

```python
for valor in diccionario.values():
	print(valor)
```
Para consultar ambos elementos de a pares se puede recurrir al método *.items()* :

```python
for clave, valor in diccionario.items():
	print(clave, valor)
```


----
----
----

## [Inicio](#control-flujo)

## [Volver](../README.md#condicionales-y-bucles)