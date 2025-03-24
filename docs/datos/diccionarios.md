---
tags:
  - datos
  - diccionarios
  - JSON
---

# Diccionarios (`dict`)

Los diccionarios son colecciones de pares clave-valor.
Los diccionarios se definen con llaves (`{}`),
el formato es el que sigue:
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

!!! warning "Claves repetidas" 
    Hay que tener cuidado de no repetir las claves porque sino **se pierden** los valores más antiguos.

## Métodos y operadores

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

La lectura de a pares clave-valor se hace con el método `items()`:
```python
objeto_items = diccionario.items()   # objeto 'dict_items'
lista_items = list(objeto_items)          # conversion a lista de tuplas clave-valor
```
donde cada par se engloba en una tupla y el conjunto se agrupa en una lista.

Con el operador `in` podemos chequear la existencia de una clave particular ó de un valor:
```python
existe_clave = clave in diccionario             # verificacion de clave directa
existe_valor = valor in diccionario.values()    # lectura de valores previa
```

Para crear un nuevo diccionario con claves pero todas con valor `None` existe el método `fromkeys()`:
```python
diccionario = dict.fromkeys([clave_1, clave_2, ...] ) 
```



!!! tip "Archivos JSON"
    Los archivos JSON están dedicados al guardado de pares clave-valor.
    Los diccionarios pueden guardarse y leerse
    en estos archivos con ayuda del 
    [módulo `json`.](../archivos/json.md)
