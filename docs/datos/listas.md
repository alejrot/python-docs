---
tags:
  - datos
  - listas
---



# Listas (`list`)

La lista es una estructura de datos
para almacenar múltiples valores en secuencia.
Los valores internos se agrupan con los corchetes ( `[]` )
y se delimitan entre ellos con comas (`,`).
Se habitúa dejar un espacio entre cada coma y su elemento siguiente.

```python title="Formato de listas"
lista = [elemento_1, elemento_2,  ...]
```

Los datos pueden ser de distintos tipos y pueden ser modificados tanto en valor como en tipo. 

Ejemplo:

```python
Listado = [1, “hola”, 78.3]
```
Para acceder a un elemento de la lista en base a su indice éste se indica entre corchetes:
```python
elemento = lista[indice]
```
El primer índice tiene valor cero. Si el índice iguala o supera la longitud de la lista da error. Dicha longitud de la lista se puede obtener con la función `len()` (viene del inglés *length*):
```python title=""
longitud = len(lista)
```



!!! tip "Indices negativos"
    Se pueden usar indices negativos hasta la longitud máxima: índice `-1` es el último valor, índice `-2` es el penúltimo elemento, etc.

    Ejemplo: si una lista tiene 10 elementos entonces el rango de índices permitidos va de -10 a 9.



Las listas pueden crearse vacías para ser completadas más tarde:
```python
lista = []
```

Las listas pueden ser definidas también usando la función `list()`. Esta funcion también permite convertir otros tipos de datos a lista.

!!! example "Ejemplo aplicacion: Matrices" 
    Para hacer una matriz de valores se la puede construir en base a una lista que contenga a múltiples listas internas  separadas con comas. 
    ```python title="Ejemplo: matriz 2 x 3"
    matriz=[ [v11, v12, v13] ,  [v21, v22, v23] ]   # lista de listas de valores
    ```

## Métodos de las listas

Para añadir un nuevo elemento al final de la lista podemos usar el método `append()`:
```python
lista.append(elemento)
```
Si buscamos añadir un elemento en una posición particular podemos hacerlo indicando un valor indice dentro del método `insert()`:

```python
lista.insert(indice , elemento)
```

Para eliminar un elemento puede usarse el método `remove()`.Éste elimina la primera aparición del método indicado. Si el elemento indicado no existe el método devuelve error.
```python
lista.remove(elemento)
```

Para eliminar un elemento por índice y poder retornarlo se usa el método `pop()`.Si el elemento indicado no existe el método devuelve error.

```python
elemento = lista.pop( )           # elimina  el último elemento
elemento = lista.pop( indice )    # elimina el elemento por indice
```

La búsqueda de la posición de un elemento se hacer con el método `index()`,el cual presupone que el elemento existe :
```python
indice = lista.index(elemento)
```

!!! tip "Tip: operador `in`"
    Para verificar la existencia de un elemento en la lista se puede usar el operador `in` el cual devuelve un valor booleano.

    ```python
    existe_elemento = elemento in lista     # valor lógico: 'True' o 'False'
    ```
    Combinando este operador con el uso de condicionales se puede prevenir errores de ejecución por intentar afectar elementos inexistentes.


!!! example "Ejemplo de uso: eliminar elemento" 

    ```python title="1º aparicion"
    if elemento in lista:
        indice = lista.index(elemento) 
        lista.remove(elemento)
    ```
    ```python title="por indice"
    if indice < len(lista):
        elemento = lista.pop(indice) 
    ```


Reescribir una posicion particular de la lista:
```python
lista[indice]  = nuevo_valor
```

Contar repeticiones de un elemento: método `count()`
```python
lista.count(elemento):
```

Concatenar una segunda lista al final de la primera: método `extend()`

```python
lista_1.extend(lista_2)
```


Invertir el orden de los elementos (cambios persistentes): método `reverse()`
```python
lista.reverse()
```


Eliminar todo el contenido de la lista:

```python
lista.clear()
```

Ordenar los elementos (cambios persistentes): método `sort()`
```python
lista.sort()  # Orden ascendente por defecto
lista.sort( reverse = True)  # Orden descendente
lista.sort( key = funcion_ordenamiento)  # Criterios personalizables mediante una funcion lambda
```

Los argumentos de entrada `reverse` y `key` permiten alterar el orden y el criterio de ordenamiento de la función: 

- `reverse`: booleano que permite invertir el orden. Es `False` por defecto.   
- `key`: función para especificar el criterio de ordenamiento de los elementos. Esta función debe aceptar un solo elemento de la lista como entrada. Por defecto es `None`.

Ejemplos de uso:

!!! example "Ejemplos: ordenar una lista de strings con `sort()`"

    ```python title="ordenamiento alfabético"
    lista = ["aaa",  "cccc", "bb"]
    lista.sort()
    print(lista)        # '['aaa', 'bb', 'cccc']'
    ```

    ```python title="ordenamiento alfabético inverso"
    lista = ["aaa",  "cccc", "bb"]
    lista.sort(reverse = True)
    print(lista)        # '['cccc', 'bb', 'aaa']'
    ```

    ```python title="ordenamiento por longitud de caracteres"
    lista = ["aaa", "bb", "c"]
    lista.sort(key=len)     # hace 'len( elemento)' 
    print(lista)        # '['c', 'bb', 'aaa']'
    ```

## Copia y referencia de listas


Python permite **apuntar** a una lista preexistente con una simple asignación: 

```py title="Apuntador a lista"
referencia = lista
```

Si los elementos de la lista original son modificados entonces estos cambios se verán replicados en la lista de salida.

!!! example "Ejemeplo: cambios sobre lista"

    ```py 
    # creacion de lista original
    original = [ 1, "hola", True]

    # la nueva lista muestra el mismo contenido que la oiginal 
    referencia = original            #  referencia
    print(referencia)       # '[1, 'hola', True]'

    # al modificar la lista original la lista de salida cambia también
    original[1] = "chau"
    print(referencia)            # '[1, 'chau', True]'
    ```


Si se requiere independizar una lista de la otra y así prevenir cambios imprevistos se recurre a la **copia**.

!!! tip "Tip: copia de listas"
    Las listas tienen varias opciones para la copia de los valores. Una de ellas es el método `copy()`:

    ```py title="método copy()"
    copia = original.copy()
    ```
    ```py title="función list()"
    copia = list(original)
    ```
    ```py title="slicing y comprensión"
    copia = original[:]             # copia por slicing
    copia = [i for i in original]   # copia por comprension
    ```

!!! warning "Copia superficial y copia profunda"
    Los métodos de copia descritos previamente son de **copia superficial**. Esto significa que se copian los valores de las variables internas, pero en caso de haber listas u otros tipos de datos en el interior éstos se pasarán por referencia y por tanto serán susceptibles a cambios.

    La alternativa es la **copia profunda**, la cual copia recursivamente todo el contenido interno de la lista creando así una réplica totalmente independiente del original.

    En Python se implementó para tal fin la función `deepcopy()`:

    ```py title=" función deepcopy"
    from copy import deepcopy   # importacion de la funcion
    copia = deepcopy(original)   # copia profunda
    ```
