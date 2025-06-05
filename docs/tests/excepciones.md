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
