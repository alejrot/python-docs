---
tags:
  - Bash
  - Interprete
---


# Uso en Consola

Las instrucciones de Python se puede ejecutar escribiendo en la terminal en tiempo real. 
Para ello se invoca al intérprete de Python desde la terminal usada:

```bash title="Uso en consola - Apertura del intérprete"
python
py
```

Entonces se imprime la información de la actual versión de Python y del sistema operativo actual. 
Cada nueva linea de la terminal comienza con `>>>` 
indicando que el intérprete de Python está abierto 
y 
las instrucciones se cierran pulsando la tecla `ENTER`.

```python title="Uso en consola - Instruccion a instruccion"
>>> instrucccion_1
>>> instruccion_2
>>> ....
```


!!! example "Ejemplo: definir una variable en vivo y sumarle 1"
    ```python 
    >>> x=3   # asignacion
    >>> x+1   # incremento
    ```
    Resultado en pantalla:
    ```bash 
    >>> x=3
    >>> x+1
    4
    ```

Para salir del intérprete hay que escribir `exit()` ó `Ctrl + Z` (en Linux)

```bash title="Uso en consola - Salida"
>>> exit()
```

Evidentemente, la escritura de rutinas en la consola de Python es muy poco práctica para crear rutinas, aún si estas son sencillas.
Sin embargo, 
la consola es una buena opción para 
hacer cuentas matemáticas sencillas,
probar pequeñas instrucciones, 
etc.