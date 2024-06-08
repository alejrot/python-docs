
# Tipos de Datos 



## Tipos predefinidos

Python tiene sus propios tipos de datos predefinidos para facilitar el manejo y la organizacion de la data guardada en las variables, agrupándolas en estructuras más grandes y con diferentes propiedades. 

El tipo de datos de una variable o estructura puede consultarse con la función **type()**:

```python title="tipo de datos"
type( <elemento>)   # retorna el tipo de datos
```
A continuacion se explican los tipos de datos estándar de Python.

## Listas (`list`)

Estructura de datos para almacenar múltiples valores en secuencia. Se delimita con los corchetes ( `[]` ). Los elementos se separan con comas. Se habitúa dejar un espacio entre cada coma y su elemento siguiente.

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

### Métodos de las listas

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

Ordenar los elementos (cambios persistentes): método `sort()`
```python
lista.sort()  # Orden ascendente por defecto
lista.sort( reverse = True)  # Orden descendente
lista.sort( key = nombre_funcion)  # Criterios personalizables mediante una funcion lambda
```

Eliminar todo el contenido de la lista:

```python
lista.clear()
```


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

    ```python title="ordenamiento por longitud"
    lista = ["aaa", "bb", "c"]
    lista.sort(key=len)     # hace 'len( elemento)' 
    print(lista)        # '['c', 'bb', 'aaa']'
    ```


## Tuplas (`tuple`)

Similar a las listas pero inmutables. Las tuplas se indican con paréntesis ( `()` ) :

```python title="Definicion de tuplas"
tupla = (elemento_1, elemento_2, ...)
```

Las tuplas también pueden definirse mediante la función `tuple()`.

!!! example  "conversión de lista a tupla"
    ```python
    lista = [3, "a", False]     # 'list'
    tupla = tuple( lista )      # 'tuple'
    ```

Los métodos más habituales para trabajar con tuplas son `count()` e `index()`, este último combinado con el operador `in`.

## Conjuntos (`set`)
Son una colección de elementos no repetidos  y no ordenados. Para definirlos se usa la función `set()` la cual descarta los elementos repetidos :

```python
conjunto = set( lista_elementos  )
```

Los conjuntos también pueden ser inicializados con llaves ( `{}` ):

```python
conjunto = {elemento_1, elemento_2, ...}
```

Los elementos de los sets no pueden ser consultados por índice. 

!!! warning "Sets de strings"
    `set()` trata las variables *string* como si fueran vectores de letras y por ello las descompone, devolviendo **el conjunto de letras**. 

    Ejemplo:
    ```python
    conjunto = {"hola"}         # '{'hola'}'
    conjunto = set("hola")      #'{'l', 'o', 'h', 'a'}' 
    ```

### Métodos de los Sets

Para añadir y quitar elementos se puede usar los métodos `add()` y `remove()`:
```python
set_1.add(elemento)
set_1.remove(elemento)
```


Los conjuntos no pueden ser consultados por índice. Para vaciar por completo el conjunto se usa el método  `clear()`:

```python
set_1.clear()
```
Para crear un conjunto que reúna elementos de otros dos se puede usar el método `union()`

```python
nuevo_set = set_1.union( set_2 )
```

Con el método `difference()` se puede listar todos aquellos elementos del primer conjunto que no estén compartidos con el segundo:

```python
set_no_compartidos = set_1.difference(set_2)
```
### Operadores de los Sets

Los conjuntos se pueden relacionar también con operadores:

|Operacion | Retorno Elementos| Simbolo|
|:-----|:-----|:----:|
| **Unión** | todos   |       `|` |
| **Intersección** |  comunes |  `&` |
| **Diferencia** | no repetidos (del set izquierdo) | `-` |
| **Diferencia Simétrica** |  no repetidos (ambos sets) | `^` |

!!! example "Ejemplo aplicado: operaciones sobre sets"
    ```python title="Ejemplo aplicado: operaciones sobre sets"
    # conjuntos de ejemplo
    set_1 = {"A", "B", "C" , 1}
    set_2 = {"A", 1, "X"}

    # operaciones
    union                = set_1 | set_2    # {1, 'C', 'B', 'X', 'A'}
    interseccion         = set_1 & set_2    # {1, 'A'}
    diferencia           = set_1 - set_2    # {'C', 'B'}
    diferencia_simetrica = set_1 ^ set_2    # {'C', 'B', 'X'}
    ```


## Diccionarios (`dict`)

Son colecciones de pares clave-valor. Los diccionarios se definen con llaves ( `{}`) , el formato es el que sigue:
```python title="Formato diccionario"
diccionario = {clave_1: valor_1, clave_2: valor_2, ... }
```

Las claves deben ser **únicas e inmutables**, y sirven para acceder a su valor asociado. Deben ser de tipo `string`. Los valores pueden ser de cualquier tipo. Los pares *clave-valor* sí pueden ser modificados, añadidos y eliminados (son mutables).

!!! example "Ejemplo: definicion de diccionario"
    ```python title="valor único"
    diccionario = {"A": 45, "B": 30}
    ```

!!! info "Múltiples valores"
    Una misma clave puede tener múltiples valores agrupados en un tipo de datos acorde: una lista, una tupla, un set, un diccionario interno, etc.

    ```python title="valores múliples"
    diccionario = {"A": {45, 30}}   # hace A = {45,30} (set)
    diccionario = {"A": {45, 30} , "A": 5} # hace A=5 
    ```


### Métodos y operadores

Para acceder a un valor del diccionario se lo busca por su clave, la cual debe ser preexistente:
```python
valor = diccionario[clave]      # si la clave no existe da error
```
Otra forma es usar el método `get()`, el cual es más seguro : 
```python
diccionario.get(clave)  # si no se encuentra la clave se devuelve 'None'
```

Para añadir o modificar un par clave - valor se hace una asignación:
```python
diccionario[ nueva_clave ] = nuevo_valor
```
Para eliminar una clave se usa el operador `del` (delete):
```python
del diccionario[clave]
```

La lectura de todas las claves de un diccionario se puede usar el método `keys()`:
```python
claves = diccionario.keys()
```
En tanto que las lectura de los valores se realiza con el método `values()`:
```python
valores = diccionario.values()
```
Con el operador `in` podemos chequear la existencia de una clave particular ó de un valor:
```python
existe_clave = clave in diccionario             # verificacion de clave directa
existe_valor = valor in diccionario.values()    # lectura de valores previa
```

Para crear un nuevo diccionario con claves pero todas con valor None existe el método `fromkeys()`:
```python
diccionario = dict.fromkeys([clave_1, clave_2, ...] ) 
```


### Función eval()

Para poder convertir a diccionario una variable `str` (por ejemplo, una lectura desde un archivo de texto) se usa la función `eval()`:

```python title="Función eval()"
diccionario = eval(texto)
```


!!! warning "Claves repetidas" 
    Hay que tener cuidado de no repetir las claves porque sino **se pierden** los valores más antiguos.




!!! tip "Archivos JSON"
    Los archivos JSON están dedicados al guardado de pares clave-valor. Los diccionarios pueden guardarse y leerse en estos archivos con ayuda del módulo `json`. [Ir al tutorial sobre JSON](10-manejo_archivos.md#archivos-json)



## Tipado de datos

Los datos aquí analizados pueden ser tipados para ayudar a prevenir y corregir errores por incompatibilidad de tipos. 

### Datos simples

La notación básica es igual a la del tipado de variables :

Notación general:

```python title="Tipado simple"
<dato>: <tipo_dato>
```

Los datos y variables internas también se pueden tipar. Para ello se añade el uso de **corchetes** para delimitar los tipos de variables internas.

```python title="Tipado de variables"
<dato>: <tipo_dato>[ <tipo_variable1>, <tipo_variable2>, ...]
```


!!! example "Ejemplos"

    ```python title="Tipado elemental"
    lista_textos:       list
    tupla_enteros:      tuple
    conjunto_textos:    set
    diccionario:        dict     
    ```


    ```python title="Tipado de variables: listas, tuplas y conjuntos" 
    lista_textos:       list[  str ] # lista de cadenas de caracteres
    tupla_enteros:      tuple[ int ] # tupla de numeros enteros
    conjunto_textos:    set[   str ] # set de cadenas de caracteres
    ```


    ```python title="Tipado de variables: diccionario" 
    diccionario: dict[str, int]     # clave texto, valor entero
    diccionario = {
        "primero": 4,     # correcto
        "segundo": 7.5,   # error: tipo valor flotante
            27   : 10 ,    # error: tipo clave entera
        }
    ```

### Datos compuestos

El tipado también se puede usar para datos compuestos (), agrupando los tipos mediante corchetes. 

!!! example "Ejemplo de uso: tipado de diccionario"
    
    En este ejemplo se da tipado a un diccionario con claves de texto y listas de enteros como valor

    ```python
    # tipado
    diccionario_listas_enteros: dict[  str, list[int]  ]

    # uso
    diccionario_listas_enteros = { 
        "hola": [1, 2, 7],          # correcto
        "chau": [4,"b", 1],         # error:  string en la lista de valor 
        "adios": (4, 6) ,           # error: tupla como valor       
        }
    ```

El tipado detallado para datos puede ser un desafío debido a la variedad de datos y variables internos, especialmente cuando los datos son compuestos.


!!! warning "Recordar: tipado débil"
    Al igual que en el caso de las variables, el tipado manual es débil y **no impide la ejecución** del programa en caso de encontrarse inconsistencias.


## Funciones para datos

La función `sorted()` ordena los elementos de una lista, por defecto de manera ascendente.

La funcion `enumerate()` permite enumerar los elementos de una lista ,pero los convierte también a tupla (ver más adelante).

