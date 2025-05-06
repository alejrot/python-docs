---
tags:
  - datos
  - funciones
  - tuplas
  - listas
  - diccionarios 
  - sets
---

# Funciones para datos

Python incluye varias funciones predefinidas
para manipular sus tipos de datos predefinidos. 


## Identificar elemento - `type`

El tipo de datos de una variable o estructura puede consultarse con la función `type()`:

```python title="tipo de datos"
tipo = type(elemento)  
print(tipo)
```

## Enumerar elementos - `enumerate` 

La función `enumerate()` permite enumerar los elementos de una lista,
convirtiéndolos a tupla.
Require el uso de la función `list()` para recuperar la data.

```py title="enumerate()"
lista = [1, "hola", True]

objeto = enumerate(lista) # tipo 'enumerate'
enumerados = list(objeto) # conversion a lista

# da '[(0, 1), (1, 'hola'), (2, True)]'
```

El índice inicial es `0` salvo indicación contraria.
El valor elegido como índice inicial se pasa como segundo valor de entrada para la función `enumerate()`: 

```py title="enumerate() "
lista = [1, "hola", True]
indice_inicial = 27

objeto = enumerate(lista, indice_inicial )  # tipo 'enumerate'
enumerados = list(objeto)   # conversion a lista

# da '[(27, 1), (28, 'hola'), (29, True)]'
```

El resultado final  es una lista de tuplas que incluyen cada una un par indice-elemento. Ambos datos pueden extraerse fácilmente con la cláusula `for`:

```py title="Extraccion de valores"
for indice, elemento in enumerados:
    print(f"Indice: {indice}; elemento: {elemento}")

# texto en pantalla
# 'Indice: 27; elemento: 1'
# 'Indice: 28; elemento: hola'
# 'Indice: 29; elemento: True'
```


Más sobre la cláusula `for`: [control de flujo](../contenido/5-control_flujo.md#ciclos-for-para)  

## Ordenamiento de datos - `sorted` 

La función `sorted()` ordena los elementos de listas y diccionarios, por defecto de manera ascendente / alfabética. 

```py title="Ordenamiento de listas - sorted()"
lista_ordenada = sorted( lista                )   # orden ascendente
lista_ordenada = sorted( lista, reverse=True  )   # orden descendente
lista_ordenada = sorted( lista, key = funcion_ordenamiento )   # criterio de ordenamiento definido por función
```
Esta función es muy similar al método `sort()` de las listas, de hecho tiene los mismos argumentos de entrada (`reverse` y `key`). El resultado es una lista con los elementos.

Esta función también sirve para ordenar diccionarios:

```py title="Ordenamiento de diccionario - por clave"
lista_ordenada = sorted( diccionario                )   # orden ascendente
lista_ordenada = sorted( diccionario, reverse=True  )   # orden descendente
lista_ordenada = sorted( diccionario, key = funcion_ordenamiento )   # criterio de ordenamiento definido por función
```

La función presupone que el ordenamiento es por clave. Si en cambio se busca ordenar los elementos por valores hay que usar el método `values()`:

```py title="Ordenamiento de diccionario - por valor"
lista_ordenada = sorted( diccionario.values()                )   # orden ascendente
lista_ordenada = sorted( diccionario.values(), reverse=True  )   # orden descendente
lista_ordenada = sorted( diccionario.values(), key = funcion_ordenamiento )   # criterio de ordenamiento definido por función
```

El resultado en estos casos es una lista de tuplas con los pares clave-valor.


## Conversion desde string - `eval`

Para poder evaluar una variable `str`
que representa sintácticamente un tipo de datos (una lista, un diccionario, etc.) 
se usa la función `eval()`

```python title="Función eval()"
data = eval(string_datos)
```

Algunos ejemplos sencillos:

```python title="Función eval() - lista"
texto = '["hola", 3]'
data = eval(texto)
type(data)      # da  "<class 'list'>"
```

```python title="Función eval() - diccionario"
texto = '{"valor": 3}'
data = eval(texto)
type(data)      # da  <class 'dict'>
```

Esta función es útil,
por ejemplo,
para interpretar un *string* de datos procedente de un archivo de texto o de una página web.


!!! danger "Ejecución de código"

    `eval()` interpreta el código ingresado como texto y lo ejecuta,
    sin importar su objetivo real.
    Por ello deben extremarse las precauciones al usar esta función,
    especialmente si los usuarios pueden pueden interactuar con el texto de entrada. 



## Copia de datos - `deepcopy`

La función `deepcopy` crea una réplica estricta de los datos de entrada:
listas, diccionarios, etc.,
copiando también sus datos y variables internos.
Para su uso se requiere su importación desde el módulo `copy`:


```py title="copia profunda"
from copy import deepcopy   # importacion 

copia = deepcopy(original)   # copia profunda
```

De esta forma la copia se vuelve completamente independiente de la información de entrada.

