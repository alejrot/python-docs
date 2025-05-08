---
tags:
  - main
---



## Sintaxis 

A diferencia de otros lenguajes de más bajo nivel,
Python no requiere indicar explicitamente una función principal (*main*) sino que presupone que la función principal es la rutina del archivo invocado por el usuario o por el sistema operativo. 
A esta función el intérprete de Python le da el nombre "`#!py __main__`"
y dicho valor se consulta desde la variable especial `#!py __name__`.

Esto contrasta con las funciones definidas dentro de la rutina principal,
las cuales son consideradas secundarias.
Lo mismo sucede con las rutinas de módulos y paquetes: estas sólo son consideradas como función *main* si son llamadas directamente por el intérprete de Python.

<!-- 
En cambio, las rutinas presentes en otros archivos serán consideradas por el intérprete de Python como funciones ó rutinas secundarias.


Esta diferenciación es importante cuando se usan módulos en un programa,
pues estos no quedan incluidos 
como parte de la función `main()`.
 -->


## Rutina exclusiva de `main()`

Para ejecutar una rutina únicamente en el programa principal
(es decir, si se invoca directamente al archivo que las contiene) se puede englobar la rutina con el siguiente condicional:

```python title="Rutina exclusiva de main()"
if __name__ == "__main__" :
    #rutina exclusiva de la funcion main
```
Esta forma es útil para crear demos y tests dentro de los archivos donde se crean funcionalidades, clases, etc. de modo que sólo se ejecuten los demos cuando se los llama directamente.
