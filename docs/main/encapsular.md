---
tags:
  - main
  - sys
  - Argumentos
  - Modulos
---


# Encapsular rutina principal

Se puede englobar la rutina principal 
y pasarla como argumento a la función `exit()` del módulo `sys`: 

```py   title="Rutina principal encapsulada"
import sys


# funcion wrapper
def principal():
    # (Rutina principal)
    print("Rutina principal completa")
    return 0    # valor de retorno


if __name__ == "__main__": 
    sys.exit(principal())    
```

de esta forma 
el intérprete ejecutará
la función *wrapper* (envolvente)
y su valor de retorno 
se pasará a la *shell* al terminar.


