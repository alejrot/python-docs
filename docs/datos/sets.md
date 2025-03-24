---
tags:
  - datos
  - sets
---

# Conjuntos (`set`)

Los conjuntos o *sets* on una colección de elementos
no repetidos y no ordenados.
Para definirlos se usa la función `set()`
la cual descarta los elementos repetidos:

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
    Para mantener los strings integros estos pueden agruparse dentro de una lista mediante corchetes:
    ```python
    conjunto = set( ["hola"] )    # '{'hola'}'
    ```

## Métodos de los Sets

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
## Operadores de los Sets

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

