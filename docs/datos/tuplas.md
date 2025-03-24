---
tags:
  - datos
  - tuplas
---

# Tuplas (`tuple`)

Las tuplas son similares a las listas pero inmutables,
es decir no permiten modificar sus contenidos internos.
Las tuplas se indican con paréntesis ( `()` ) :

```python title="Definicion de tuplas"
tupla = (elemento_1, elemento_2, ...)
```

Las tuplas también pueden definirse mediante la función `tuple()`.

```python title="Definicion de tuplas"
tupla = tuple(elemento_1, elemento_2, ...)
```

!!! example  "conversión de lista a tupla"
    ```python
    lista = [3, "a", False]     # 'list'
    tupla = tuple( lista )      # 'tuple'
    ```

Los métodos más habituales para trabajar con tuplas son `count()` e `index()`, este último combinado con el operador `in`.