# Errores y Excepciones


## Error de Sintaxis
Los errores de sintaxis (*SyntaxError*) son violaciones de las reglas de escritura del lenguaje. El intérprete las detecta a medida que ejecuta las rutinas.


## Excepción
Las excepciones son los **errores detectados en tiempo de ejecución**. Muchos de ellos no pueden prevenirse completamente por diseño.

Ejemplos de excepciones habituales:

| Excepción | Significado |
|:---:|:---|
| `Exception`| error genérico (etiqueta comodín).|
| `IndexError`| elemento de una lista, tupla, etc. con indice indicado inexistente.|
| `KeyError` |clave de un diccionario inexistente.|
| `NameError`|variable no definida.|
| `ZeroDivisionError`|  se dispara ante una division por cero. |
| `RecursionError`| recursividad infinita de las funciones, nunca se resuelve la funcion recursiva.|
| `TypeError`| tipo de datos incorrecto. Ejemplo: indexado con un string.|
| `ValueError`| valores imposibles de manejar o traducir. Ejemplo: convertir a entero una frase.|
| `ModuleNotFoundError`| no se encuentra el módulo requerido.|
| `ImportError`| no se encuentra el elemento requerido del módulo especificado.|


!!! example "Ejemplos de excepciones"
	```python title="TypeError"
	valor = vector["10"]	#indice 'str' en vez de 'int'
	```

	```python title="ValueError"
	numero = int("hola")	# ¿qué número sería ese?
	```

	```python title="IndexError"
    W = [1, 2, 3]	# Lista de 3 elementos
    Z = W[4]		# Elemento Nº5 inexistente
	```

	```python title="ZeroDivisionError"
    x = 4
    y = 0
    z = x / y       
	```

## Sintaxis

### Uso básico - Clausulas `try` y `except`

Las excepciones pueden manejarse mediante la estructura `try `- `except`:

```py title="Excepción genérica" hl_lines="1 3"
try:
    #código a prueba
except:
	#se detiene el código a prueba
	#se ejecuta un código alternativo
```


!!! tip "Cláusula `raise`"
	Agregando la cláusula `raise` al final de la rutina de excepción se puede abortar la ejecución tras mostrar el reporte de erroir predeterminado
	```py title="raise" hl_lines="6"
	try:
		#código a prueba
	except:
		#se detiene el código a prueba
		#se ejecuta un código alternativo
		raise
	```


### Código condicional - Clausula `else`

Se puede colocar código extra pasada la parte vulnerable del programa con la cláusula `else`. Este código sólo se ejecuta si la ejecución de la rutina vulnerable fue exitosa.

```py title="Código condicional" hl_lines="6"
try:
	#código a prueba
except:
	#se detiene el código a prueba
	#se ejecuta un código alternativo
else:
	#si no ocurrió una excepción en “try”
	#se ejecuta código adicional 
```

### Código de cierre - Clausula `finaly`

Si se requiere ejecutar un trozo de código sí o sí, el cual es independiente de la existencia o no de excepciones previas, se usa la cláusula `finaly`:

```py title="Código de cierre" hl_lines="6"
try:
	#código a prueba
except:
	#se detiene el código a prueba
	#se ejecuta un código alternativo
finally:
	#código obligatorio (se ejecuta al finalizar)
```

### Excepciones específicas


Se pueden crear fácilmente múltiples rutinas de excepciones para abordar distintos tipos de error posibles.Sólo hay que indicar el nombre de la excepción indicada justo después de la cláusula `except`:

```py title="Excepciones múltiples" hl_lines="13 16 19 22"
try:
	#código a prueba

	# division por cero
    x = 4
    y = 0
    z = x / y       

	#  error de indice
    W = [1, 2, 3]
    Z = W[4]			

except ValueError:
    print("Valor erróneo ")

except TypeError:
    print("Tipo de datos erróneo")

except ZeroDivisionError:
    print("Division por cero")

except IndexError:
    print("Error de índice")
```



### Excepciones como variable


Se puede usar el comodín `Except` para guardar el tipo de excepción producida como una variable con ayuda de la cláusula `as`. Esto se muestra a continuación:


```py title="Captando excepción genérica" hl_lines="3"
try:
	#código a prueba
except Exception as variable_excepcion:
	print(f"Excepción producida: {variable_excepcion}")
	print( type(variable_excepcion) )
```
La variable creada es del mismo tipo que la excepción disparada e internamente guarda su mensaje descriptivo.




!!! example "Ejemplo: captando 'ZeroDivisionError'"

	```py title="Division por cero"
	try:
		#código a prueba
		x = 4
		y = 0
		z = x / y       # division por cero

	except Exception as ex:
		print(f"Excepción producida: '{ex}'")
		print( type(ex) )
	```

	```bash title="Salida por consola"
	Excepción producida: 'division by zero'
	<class 'ZeroDivisionError'>
	```




## Referencias


[StackOverflow - Cómo determinar tipo de excepción](https://stackoverflow.com/questions/9823936/how-do-i-determine-what-type-of-exception-occurred)