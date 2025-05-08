---
tags:
  - main
  - sys
  - Retorno
  - Modulos
---



# Valor de retorno

La rutina principal puede tener un valor de retorno.
Este valor puede ser una simple variable 
que indique el éxito o el fracaso del procesamiento interno
.

El valor de retorno se envía con ayuda de la función `exit()` incluida en el módulo `sys`:

```py   title="Valor de retorno"
import sys


if __name__ == "__main__":
    # (Rutina principal)
    print("Rutina principal completa")
    sys.exit(0)         # codigo ejecución exitosa      
```

Esta función indica la intensión de salir del intérprete 
y su argumento es el valor de retorno.



Los valores habituales de salida son los siguientes:

|Valor| Significado|
|:---:|:---|
|`0`, `None`| Terminación exitosa|
|`1`| Error genérico|
|`2`| Error (sólo sintaxis de línea de comandos) |


El valor de retorno también puede ser un valor o una estructura de datos completa;
sin embargo 
estos casos deben manejarse con cuidado 
porque dichos valores pueden ser malinterpretados
por el sistema operativo
como códigos de error.




<!-- 
Estos valores pueden ser mostrados en consola (Bash, Powershell, etc)
en caso que la rutina sea llamada desde una *shell*.

En caso que el programa Python sea llamado por un proceso (un "programa") del sistema operativo
o por otras aplicaciones,
el valor de retorno será recibido como un argumento


sino que puede ser concatenada con otras rutinas de más jerarquía:
otras aplicaciones, 
procesos del sistema operativo, 
etc.
 -->
