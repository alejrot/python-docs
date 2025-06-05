
# Manejo de excepciones


## Gestión de excepciones

Python permite enmarcar partes del código
que se consideran susceptibles de errores,
y proporcionar rutinas alternativas que sólo se ejecutarán
ante errores, los cuales pueden ser genéricos o específicos. 


### Uso básico - Claúsulas `try` y `except`

Las excepciones pueden manejarse mediante las cláusulas `try` - `except`:

```py title="Excepción genérica" hl_lines="1 3"
try:
	#código a prueba
    z = x / y   #  posible `ZeroDivisionError`
    Z = W[4]    #  posible `IndexError`
except:
	#se detiene el código a prueba
	#se ejecuta un código alternativo
    print("Ejecución interrumpida")
```

Dentro del segmento definido por `try`
se ubica el segmento de código sensible a errores,
en tanto que `except` enmarca el código alternativo.
Si durante al ejecución del código sensible se detecta un error
entonces su ejecución se detiene
y se pasa automáticamente a ejecutar la rutina alternativa.


<!-- 
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
 -->


### Código condicional - Clausula `else`

Se puede colocar código extra pasada la parte vulnerable del programa con la cláusula `else`. Este código sólo se ejecuta si la ejecución de la rutina vulnerable fue exitosa.

```py title="Código condicional" hl_lines="6"
try:
	#código a prueba
    z = x / y   #  posible `ZeroDivisionError`
    Z = W[4]    #  posible `IndexError`
except:
	#se detiene el código a prueba
	#se ejecuta un código alternativo
    print("Ejecución interrumpida")
else:
	#si no ocurrió una excepción en “try”
	#se ejecuta código adicional 
    print("Ejecución exitosa")
```

### Código de cierre - Clausula `finaly`

Si se requiere ejecutar un trozo de código sí o sí, el cual es independiente de la existencia o no de excepciones previas, se usa la cláusula `finaly`:

```py title="Código de cierre" hl_lines="6"
try:
	#código a prueba
    z = x / y   #  posible `ZeroDivisionError`
    Z = W[4]    #  posible `IndexError`
except:
	#se detiene el código a prueba
	#se ejecuta un código alternativo
    print("Ejecución interrumpida")
finally:
	#código obligatorio (se ejecuta al finalizar)
    print("Programa finalizado")
```

### Excepciones específicas


Se pueden crear fácilmente múltiples rutinas de excepciones para abordar distintos tipos de error posibles.Sólo hay que indicar el nombre de la excepción indicada justo después de la cláusula `except`:

```py title="Excepciones múltiples" hl_lines="13 16 19 22"
try:
	#código a prueba
    z = x / y   #  posible `ZeroDivisionError`
    Z = W[4]    #  posible `IndexError`	

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
        z = x / y   #  posible `ZeroDivisionError`
        Z = W[4]    #  posible `IndexError`	

	except Exception as ex:
		print(f"Excepción producida: '{ex}'")
		print( type(ex) )
	```

	```bash title="Salida por consola"
	Excepción producida: 'division by zero'
	<class 'ZeroDivisionError'>
	```


## Lanzamiento

Python dispone de la cláusula `raise` para lanzar excepciones de manera discrecional:


```py title="Lanzamiento - raise"
if condicion:
    raise nombre_excepcion
```

Por ejemplo, para prevenir una division por cero se puede evaluar el valor de la futura variable cociente
y si da cero disparar la excepción `ZeroDivisionError`:

```py title="Lanzamiento - division por cero"
if cociente == 0:
    raise ZeroDivisionError
```

## Referencias


[StackOverflow - Cómo determinar tipo de excepción](https://stackoverflow.com/questions/9823936/how-do-i-determine-what-type-of-exception-occurred)