---
tags:
  - Funciones
---


# Tipado en las funciones

Las funciones de Python admiten tipado de sus argumentos de entrada
y del valor de retorno 
para detectar inconsistencias 
y prevenir posibles errores.

La asignacion del tipo de datos de los argumentos
se realiza con el operador *dos puntos* (`:`),
en tanto que la asignación del tipo de salida
se realiza con el *operador flecha* (`->`).

Ejemplo: calcular potencias enteras de un numero flotante

```python title="Tipado de funciones"
def potencia(base: float, exp: int) -> float:    # retorno flotante
    return base**exp

x = 2.73    # valor flotante
y = 3       # valor entero
valor = potencia(x, y)   
```

