<a name="top"></a>

## [Volver](../Python.md#errores-y-excepciones)

# Errores y Excepciones

## Error de Sintaxis
Los errores de sintaxis (*SyntaxError*) son violaciones de las reglas de escritura del lenguaje. El intérprete las detecta a medida que ejecuta las rutinas.


## Excepción
Las excepciones son los errores detectados en tiempo de ejecución. Muchos de ellos no pueden prevenirse completamente por diseño.

Ejemplos de excepciones habituales:
  - **Exception:** error genérico (etiqueta comodín).
  - **IndexError:** elemento de una lista, tupla, etc. con indice indicado inexistente.
  - **KeyError:** clave de un diccionario inexistente.
  - **NameError:** variable no definida.
  - **ZeroDivisionError:**  se dispara ante una division por cero. 
  - **RecursionError:** recursividad infinita de las funciones, nunca se resuelve la funcion recursiva.
  - **TypeError:** tipo de datos incorrecto. Ejemplo: indexado con un string.
	```python
	valor = vector["10"]	#indice 'str' en vez de 'int'
	```
  - **ValueError:** valores imposibles de manejar o traducir. Ejemplo: convertir a entero una frase.
	```python
	numero = int("hola")	# ¿qué número sería ese?
	```
  - **ModuleNotFoundError:** no se encuentra el módulo requerido.
  - **ImportError:** no se encuentra el elemento requerido del módulo especificado.


## Sintaxis

### Clausulas try y except

Las excepciones pueden manejarse mediante la estructura **try - except**:

```python
try:
    #código a prueba
except:
	#se detiene el código a prueba
	#se ejecuta un código alternativo
```

Se puede diferenciar entre distintas excepciones escribiendo:

```python
except <tipo_excepcion1>:
	#codigo excepcion específica
except <tipo_excepcion2>:
	#codigo excepcion específica
#...
```

El tipo de error puede cargarse en una variable, quedaría:

```python
except <tipo_excepcion> as <variable>
	#codigo excepción específica
```
### Clausula else

Se puede colocar código extra pasada la parte vulnerable del programa con la cláusula else:

```python
try:
	#código a prueba
except:
	#se detiene el código a prueba
	#se ejecuta un código alternativo
else:
	#si no ocurrió una excepción en “try”
	#se ejecuta código adicional 
```

### Clausula finaly

Si se requiere ejecutar un trozo de código sí o sí se usa la cláusula **finaly**:

```python
try:
	#código a prueba
except:
	#se detiene el código a prueba
	#se ejecuta un código alternativo
finally:
	#código obligatorio (se ejecuta al finalizar)
```

----
----
----

## [Inicio](#errores-y-excepciones)

## [Volver](../Python.md#errores-y-excepciones)