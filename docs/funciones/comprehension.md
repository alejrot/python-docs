---
tags:
#   - Funciones
---

# Listas por comprensión (*comprehension*)

Las listas por comprensión se basan en el uso de variables calculadas a partir de una iteración. Algunos ejemplos de listas creadas a partir de un bucle for pueden ser:

```python title="Listas por comprensión"
lista_ascendente  = [ i for i in range(<maximo>)]
lista_cuadrado    = [ i * i  for i in range(<maximo>)]
lista_ambas       = [ (i, i  * i ) for i in range(<maximo>)]
```