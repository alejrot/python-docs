---
tags:
  - datos
  - tuplas
  - listas
  - diccionarios 
  - sets
  - tipado
---

# Tipado de datos

Los datos pueden ser tipados manualmente para ayudar a prevenir y corregir errores por incompatibilidad de tipos. 

!!! warning "Tipado débil"
    Al igual que en el caso de las variables, el tipado manual es débil y **no impide la ejecución** del programa en caso de encontrarse inconsistencias.


## Datos simples

La notación básica es igual a la del tipado de variables :

Notación general:

```python title="Tipado simple"
dato: tipo_dato
```

Ejemplos:

```python title="Tipado elemental"
lista_textos:       list
tupla_enteros:      tuple
conjunto_textos:    set
diccionario:        dict     
```


## Tipado interno

Las variables internas de los datos
también se pueden tipar.
Para ello se añade el uso de corchetes
para delimitar los tipos de variables internas.

```python title="Tipado de variables"
dato: tipo_dato[ tipo_variable_1, tipo_variable_2, ...]
```

!!! example "Ejemplos"

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

## Datos compuestos

El tipado también se puede usar para datos compuestos, agrupando los tipos internos mediante corchetes (`[]`). 

Tómese por ejemplo el tipado de un diccionario con claves de texto y listas de enteros como valor

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


