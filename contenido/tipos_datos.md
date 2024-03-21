<a name="top"></a>

## [Volver](../Python.md#tipos-de-datos)


# Tipos de Datos 

Python tiene sus propios tipos de datos predefinidos para facilitar el manejo y la organizacion de la data guardada en las variables, agrupándolas en estructuras más grandes y con diferentes propiedades. 

El tipo de datos de una variable o estructura puede consultarse con la función **type()**:

```python
type( <elemento>)   # retorna el tipo de datos
```
A continuacion se explican los tipos de datos estándar de Python.

## Listas

Estructura de datos para almacenar múltiples valores en secuencia. Se delimita con los corchetes ( **[]** ). Los datos pueden ser de distintos tipos que pueden ser modificados. Cada dato puede ser consultado mediante un índice. 

Formato:

```python
<lista> = [<elemento1>, <elemento2>,  ...]
```
Se habitúa dejar un espacio entre cada coma y su elemento siguiente.

Ejemplo:

```python
Listado = [1, “hola”, 78.3]
```
Para acceder a un elemento de la lista en base a su indice éste se indica entre corchetes:

```python
<elemento> = <lista>[<indice>]
```
Si el índice supera la longitud de la lista da error. Se pueden usar indices negativos hasta 

La longitud de la lista se puede contar con la funcion **len()** (viene del inglés *length*):
```python
longitud = len(<lista>)
```

Las listas pueden crearse vacías para ser completadas más tarde:
```python
lista = []
```

Las listas pueden ser definidas también usando la función **list()**. Esta funcion tambien permite convertir otros tipos de datos a lista.

Ejemplo aplicacion: Matrices. Para hacer una matriz de valores se la puede construir en base a una lista que contenga a múltiples listas internas  separadas con comas. Ejemplo matriz 2x3:
```python
<matriz>=[ [<v11>, <v12>, <v13>] ,  [<v21>, <v22>, <v23>] ]
```

### Métodos de las listas

Para añadir un nuevo elemento al final de la lista podemos usar el método **append()**:
```python
<lista>.append(<elemento>)
```
Si buscamos añadir un elemento en una posición particular podemos hacerlo indicando un valor indice dentro del método **insert()**:

```python
<lista>.insert(<indice> , <elemento>)
```

Para eliminar un elemento puede usarse el método **remove()**.Éste elimina la primera aparición del método indicado. Si el elemento indicado no existe el método devuelve error.
```python
<lista>.remove(<elemento>)
```
Para verificar la existencia de un elemento en la lista se puede usar el operador **in** el cual devuelve un valor booleano.
```python
<elemento> in <lista>
```
Buscar la posición de un elemento:
```python
<lista>.index(<elemento>)
```
(Si el elemento no existe da error).

Ejemplo de uso: 
```python
if elemento in lista:
    posicion = lista.index(elemento) 
```

Reescribir una posicion particular de la lista:
```python
<lista>[<indice>]  = <nuevo_valor>
```

Contar repeticiones de un elemento:
```python
<lista>.count(<elem>):
```

Concatenar una segunda lista al final de la primera:

```python
<lista1>.extend(<lista2>)
```

Eliminar último elemento:

```python
<lista>.pop()
```

Invertir el orden de los elementos:
```python
<lista>.reverse()
```

Ordenar los elementos:
 ```python
<lista>.sort()  # Orden ascendente
<lista>.sort( reverse = True)  # Orden descendente
<lista>.sort( key = <funcion>)  # Criterios personalizables mediante una funcion lambda
```
Ejemplo: ordenar una lista de strings
 ```python
lista = ["aaa", "bb", "cccc"]
# ordenamiento alfabético 
lista.sort()
print(lista)
# ordenamiento alfabético inverso
lista.sort(reverse = True)
print(lista)
lista = ["aaa", "bb", "c"]
# ordenamiento por longitud: len( elemento )
lista.sort(key=len)
print(lista)
 ```

Eliminar todo el contenido de la lista:
```python
<lista>.clear()
```

### Funciones para las listas

La función **sorted()** ordena los elementos de una lista, por defecto de manera ascendente.

La funcion **enumerate()** permite enumerar los elementos de una lista ,pero los convierte también a tupla (ver más adelante).


## Tuplas (Tuples)

Similar a las listas pero inmutables. Las tuplas se indican con paréntesis ( () ) :

```python
<tupla>=(<elem1>, <elem2>, ….)
```

Las tuplas también pueden definirse mediante la funcion **tuple()**.

ejemplo: convertir lista a tupla
```python
lista = [3, "a", False]
tupla = tuple( lista )
```

Los métodos más habituales para trabajar con tuplas son **.count()** e **.index()**, este último combinado con el operador **in**.

## Conjuntos (Sets)
Son una colección de elementos no repetidos  y no ordenados. Para definirlos se usa la función **set()** la cual descarta los elementos repetidos :

```python
<conjunto> = set( <lista_elementos>  )
```

Los conjuntos también pueden ser inicializados con llaves ( **{ }** ):

```python
<conjunto> = {<elemento1>, <elemento2>, ...}
```

Los elementos de los sets no pueden ser consultados por índice. 

**Importante:** *set()* trata las variables *string* como si fueran vectores de letras y por ello las descompone, devolviendo **el conjunto de letras**. 

Ejemplo:
```python
conjunto = {"hola"}         # '{'hola'}'
conjunto = set("hola")      #'{'l', 'o', 'h', 'a'}' 
```
### Métodos de los Sets

Para añadir y quitar elementos se puede usar los métodos *.add()* y *.remove()*.
```python
<set1>.add(<elemento>)
<set1>.remove(<elemento>)
```


Los conjuntos no pueden ser consultados por índice. Para vaciar por completo el conjunto se usa el método  *.clear()*.

```python
<set1>.clear()
```
Para crear un conjunto que reúna elementos de otros dos se puede usar el método *.union()*

```python
<nuevo_set> = <set1>.union( <set2> )
```

Con el método *.difference()* se puede listar todos aquellos elementos del primer conjunto que no estén compartidos con el segundo:

```python
<set_no_compartidos> = <set1>.difference(<set2>)
```
### Operadores de los Sets

Los conjuntos se pueden relacionar también con operadores:

|Operacion | Retorno Elementos| Simbolo|
|:-----|:-----|:----:|
| **Unión** | todos   |       **\|** |
| **Intersección** |  comunes |  **\&** |
| **Diferencia** | no repetidos (del set izquierdo) | **\-** |
| **Diferencia Simétrica** |  no repetidos (ambos sets) | **\^** |


Ejemplo aplicado:
```python
set_1={"A","B", "C" , 1}
set_2 ={"A", 1, "X"}

union                = set_1 | set_2 # {1, 'C', 'B', 'X', 'A'}
interseccion         = set_1 & set_2 # {1, 'A'}
diferencia           = set_1 - set_2 # {'C', 'B'}
diferencia_simetrica = set_1 ^ set_2 # {'C', 'B', 'X'}
```


## Diccionarios

Son colecciones de pares clave-valor. Los diccionarios se definen con llaves ( **{}** ) , el formato es el que sigue:
```python
{<clave1>: <valor1>, <clave2>: <valor2>, ... }
```
Ejemplo:
```python
diccionario = {"A": 45, "B": 30}
```
Las claves deben ser únicas e inmutables, y sirven para acceder a su valor asociado. Los valores pueden ser de cualquier tipo. Los pares clave-valor sí pueden ser modificados, añadidos y eliminados (son mutables).
Para acceder a un valor del diccionario se lo busca por su clave:
```python
<diccionario>[<clave>]
```
Otra forma es usar el método *.get()* : 
```python
<diccionario>.get(<clave>) #(si no se encuentra la clave se devuelve None)
```
Para añadir o modificar un par clave - valor se hace una asignación:
```python
<diccionario>[ <nueva_clave> ] = <nuevo_valor>
```
Para eliminar una clave se usa el operador *del* (delete):
```python
del <diccionario>[<clave>]
```
Con el operador **in** podemos chequear la existencia de una clave particular directamente:
```python
<clave> in <diccionario>
```
en tanto que para chequear la existencia de un valor hace falta la ayuda del método **values()**:
```python
<valor> in <diccionario>.values()
```

La lectura de todas las claves de un diccionario se puede usar el método **keys()**:
```python
<diccionario>.keys()
```
Para crear un nuevo diccionario con claves pero todas con valor None existe el método **fromkeys()**:
```python
<diccionario> = dict.fromkeys([<clave1>, <clave2>,...] ) 
```
**Importante:** una misma clave puede tener múltiples valores agrupados en un tipo de datos acorde: una lista, una tupla, un set, un diccionario interno, etc.
Sin embargo, hay que tener cuidado de no repetir la clave porque sino se pierden los valores más antiguos.

Ejemplo:
```python
diccionario = {"A": {45, 30}}   # hace A = {45,30} (set)
diccionario = {"A": {45, 30} , "A": 5} # hace A=5
```

Para poder convertir a diccionario un string (por ejemplo, una lectura desde un archivo de texto) se usa la función **eval()**:

```python
<diccionario> = eval(<texto>)
```

Los diccionarios se pueden convertir en texto y viceversa con ayuda del módulo json. [Ver módulo JSON](manejo_archivos.md#conversion-de-tipo-datos)



## Tipado de datos

Los datos aquí analizados pueden ser tipados para ayudar a prevenir y corregir errores por incompatibilidad de tipos. La notación general es similar a la del tipado de variables pero añade el uso de **corchetes** para delimitar los tipos de variables internas.

Notación general:
 
```python
<dato>: <tipo_dato>[ <tipo_variable1>, <tipo_variable2>, ...]
```
**Recordar:** al igual que en el caso de las variables, el tipado manual es débil y no impide la ejecución del programa en caso de encontrarse inconsistencias.

A continuacion se muestra el tipado aplicado a los casos más simples.

### Listas, tuplas y conjuntos

Estos son los tipos de datos más simples de tipar, con un solo tipo de variable entre corchetes.

Ejemplos:
```python
lista_textos:       list[  str ] # lista de cadenas de caracteres
tupla_enteros:      tuple[ int ] # tupla de numeros enteros
conjunto_textos:    set[   str ] # set de cadenas de caracteres
```

### Diccionarios

Las combinaciones de tipos de variables internas en este caso se hacen de a pares.
Ejemplo:
```python
diccionario: dict[str, int]     # clave texto, valor entero
diccionario = {
    "primero": 4,     # correcto
    "segundo": 7.5,   # error: tipo valor flotante
        27   : 10 ,    # error: tipo clave entera
    }
```

### Datos compuestos

El tipado se puede usar para datos compuestos, agrupando los tipos mediante corchetes. 

Ejemplo de uso: un diccionario con claves de texto y listas de enteros como valor
```python
diccionario_listas_enteros: dict[  str, list[int]  ]

diccionario_listas_enteros = { 
    "hola": [1, 2, 7],          # correcto
    "chau": [4,"b", 1],         # error:  string en la lista de valor 
    "adios": (4, 6) ,           # error: tupla como valor       
    }
```
El tipado para datos puede ser un desafío debido a la variedad de datos y variables internos, especialmente cuando los datos son compuestos.


----
----
----

## [Inicio](#tipos-de-datos)
## [Volver](../Python.md#tipos-de-datos)
