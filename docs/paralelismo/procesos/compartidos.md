# Variables compartidas




Los procesos **no comparten variables** de manera predeterminada.
Al crearse los procesos hijos,
en estos se copian los valores de las variables originales del proceso padre
creándose réplicas que conservan los valores al momento de la creación
pero que son independientes de las variables originales.


Para crear variables y datos
que necesitan ser compartidos por
múltiples subprocesos se usan las funciones `Value()` y `Array()`.
Estas variables deben ser creadas **antes**
de crear los procesos hijos,
de otro modo no se compartirán.


Algunas opciones para ambas funciones:

|Opción| Descripción |
|---|---|
|`i`| entero con signo |
|`d`| flotante - doble precisión |




Más opciones: [modulo `array`](https://docs.python.org/es/3.13/library/array.html#module-array)


## Variables - `Value()`

### Creación

Las variables se crean con la función `Value()`,
a la que se le indica el tipo de variable interna y su valor inicial:

```python title="variable compartida - crear"
from multiprocessing import Value
numero_compartido  = Value(opcion, valor_inicial)  # variable
```

Por ejemplo, para crear una variable contador que pueda ser compartida entre varios procesos se hace: 

```python title="variable compartida - ejemplo""
contador = Value('i', 0)    # entero, valor inicial nulo
```

### Acceso

El objeto creado guarda el valor asignado dentro del campo `value`,
el cual admite lectura y escritura:

```python title="variable compartida - leer y modificar"
valor = numero_compartido.value     # leer
numero_compartido.value += 1        # escribir
```

### Protección

Las variables tienen una protección interna,
un *"lock"*.
Con él se puede prevenir el acceso simultáneo de múltiples procesos,
obligando al acceso secuencial de los procesos a la variable:


```python title="variable compartida - protección"
with numero_compartido.get_lock():     # bloqueo
    numero_compartido.value += 1       # acceso
```

Esto permite prevenir errores relacionados con la escritura:
una lectura mientras el valor está siendo cambiado por otro proceso,
una doble escritura en simultáeno,
etc. 


## Listas - `Array()`


### Creacion

La función `Array()` crea los arreglos
con el formato de datos y la lista inicial elegidos:

```python title="arreglo compartido - crear"
from multiprocessing import Array
arreglo_compartido = Array(opcion, lista_datos)
```

por ejemplo para crear una lista de valores enteros:

```python title="arreglo compartido - ejemplo"
arreglo_compartido = multiprocessing.Array('i', [8, 1 ,8, 0, 5 , -3])
```

###  Lectura

La lista de valores guardados se consulta con la función `list()`:

```python title="variable compartida - lectura"
lista = list(arreglo_compartido)
```
o también se puede hacer por *slicing*:

```python title="variable compartida - lectura"
lista = arreglo_compartido[:]
```

### Protección

Los arreglos también admite protección por bloqueo,
la cual se usa de manera análoga a las variables compartidas:

```python title="variable compartida - protección"
with arreglo_compartido.get_lock():
    lista = arreglo_compartido[:]
```