# Bifurcaciones (*forks*)

Un mecanismo antiguo para crear procesos es la bifurcación.
Consiste en hacer una réplica exacta del proceso actual
con ayuda de la función `fork()`,
cuyo retorno permite discernir
entre el proceso original y su clon.


!!! warning "Sólo POSIX"
    
    Este mecanismo sólo está disponible en sistemas POSIX.


## Creación

La función `fork()` se obtiene 
desde el módulo `os`.

```py title="Forks - Creación" 
from os import fork

retorno = os.fork()
```

Esta función no requiere argumentos adicionales.

El proceso clon es distinguido del original
en base al valor de retorno de la función,
tal como se ve a continuación.


## Retorno

El valor de retorno obtenido no es igual
para el proceso original que para su clon,
permitiendo diferenciarlos desde la rutina:

| retorno | significado|
|:---:|:---|
|`retorno > 0`| Proceso original - devuelve el ID del proceso clon|
|`retorno == 0` | Es un clon del proceso original |
|`retorno < 0`| Error de bifurcación - bifurcación fallida|


## Estructura

La bifurcación no delimita las rutinas específicas
del proceso original y de su clon
en base a "tareas" o funciones
sino que las delimita con el uso de saltos condicionales:


```py title="Forks - estructura" hl_lines="7"
from os import fork

# bifurcacion
retorno = fork()

# proceso original: 
if retorno > 0:
    # Rutina del original

# proceso clon: retorno = 0
elif retorno == 0:
    # Rutina del clon

# bifurcacion fallida
else:
    # Rutina de error
```


## Ejemplo de uso


Esta rutina sencilla crea un fork
y muestra los PIDs que ve cada uno de los procesos resultantes:

```py title="Forks - ejemplo" hl_lines="7"
from os import fork

# Rutina común
print("¡Vamos a hacer un fork de un proceso!")

# bifurcacion
retorno = fork()

# proceso original: retorno = ID proceso hijo
if retorno > 0:
    pid = os.getpid()
    print("Rutina del proceso original")
    print(f"pid: {pid}, retorno: {retorno}")

# proceso clon: retorno = 0
elif retorno == 0:
    pid = os.getpid()
    print("Rutina del proceso hijo")
    print(f"pid = {pid}, retorno: {retorno}")

# error : retorno < 0
else:
    print("Error de bifurcación")
```

El reporte en la *shell* es algo parecido a esto:

```txt title="Forks - reporte" 
¡Vamos a hacer un fork de un proceso!
Rutina del proceso original
pid: 2779587, retorno: 2779588
Rutina del proceso hijo
pid = 2779588, retorno: 0
```


