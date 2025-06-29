---
tags:
#   - Hilos
  - Paralelismo
  - Procesos
#   - Locks
#   - Forks
  - multiprocessing
---




# Gestión de Procesos


## Creación


El nuevo proceso se crea con la función `Process()`, al cual se le debe asignar el nombre de una función o *"tarea"* a ejecutar en un nuevo proceso:

```py title="Creación procesos" 
from multiprocessing import Process

# rutina para el nuevo proceso
def tarea():
    pass

# creacion del proceso
subproceso = Process(target=tarea)
```

!!! info "Subprocesos"

    El nuevo proceso creado es considerado como ***proceso hijo*** del proceso que lo creó. También se lo suele llamar ***subproceso***.


### Argumentos

Si la rutina requiere argumentos de entrada
estos se adjuntan como una lista o tupla
dentro de la función `Process()`:

```py title="Creación procesos - con argumentos"
from multiprocessing import Process

def tarea(*args, **kwargs):
    pass

# argumentos = [x,y]      # argumentos en formato lista
argumentos = (x,y,)       # formato alternativo
# creacion del proceso
subproceso = Process(
    target=tarea,
    args=lista_argumentos,
    kwargs=diccionario_argumentos,
    )
```

### 'daemon'

Los procesos demonios (*daemonic*) tienen dos características particulares:

- son cerrados automáticamente si el proceso invocador sea cerrado 
(no pueden quedar huérfanos);
- impide que el subproceso *'daemonio'* llame a sus propios subprocesos.

El proceso se puede configurar como daemonio en su definición:

```py title="Creación procesos - daemonio"
from multiprocessing import Process

def tarea():
    pass

# argumentos = [x,y]      # argumentos en formato lista
argumentos = (x,y,)       # formato alternativo
# creacion del proceso
subproceso = Process(
    target=tarea,
    daemon=True
    )
```

o también puede usarse el atributo `daemon`:

```py title="Configuracion como daemon"
subproceso.daemon = True
```

Esta configuración debe hacerse antes de ordenar la ejecución. 


### Nombre

A cada proceso se le puede asignar un nombre opcional
durante su creación mediante el argumento `name`.

El nombre también se puede cambiar en cualquier momento
con el atributo `name`:

```py title="Nombre del proceso"
subproceso.name = nombre_elegido
```

Si no se elige un nombre
entonces el programa tendrá como nombre
`Process-1`,`Process-2`, etc. 


## Arranque 

El nuevo proceso queda en *stand-by*
hasta que se ordene el arranque con el método `start()`:

```python
# orden de ejecucion del proceso
subproceso.start()
```

## Espera al cierre 

Si el proceso original
requiere esperar al cierre del proceso creado 
para ejecutar más código se recurre al método `join()`.
Con él el proceso padre permanecerá
en espera hasta que el proceso se termine:

```py title="Espera al cierre"
# espera a que el proceso se cierre
subproceso.join()
```
Al método `join()` se le puede asignar un tiempo máximo de bloqueo como argumento:
```python title="Espera al cierre - con timeout"
# espera a que el proceso se cierre 
tiempo = 5
subproceso.join(tiempo)  # bloqueo por 5 segundos como máximo
```

## Ordenar cierre

Se disponen de dos métodos llamados `close()` and `terminate()`
para pedir al sistema operativo el cierre del proceso:

```python title="Ordenar cierre"
subproceso.close()      # señal 'SIGKILL'
subproceso.terminate()  # señal 'SIGTERM'
```

Si hay subprocesos del proceso finalizados 
(procesos "nietos") entonces éstos quedarán huérfanos.

!!! danger "Sincronismos y comunicaciones"

    La terminación forzosa de un subproceso
    que tenga acceso a elementos de sincronismo (*locks*, *barrels*, etc.) 
    o de comunicación (*pipes*, *qeues*, etc. )
    puede dejar a éstos inutilizables y/o arruinar el funcionamiento
    del resto de procesos relacionados.
    
    Usar con cuidado.


## Consulta de estado


El método `is_alive` permite consultar si el proceso sigue activo:

```python title="estado actual"
retorno = subproceso.is_alive()
```

El retorno es `True` si sigue activo y `False` en caso contrario. 


## Valor de retorno

El valor de retorno de los procesos creados
se obtienen con el atributo `exitcode`:

```python title="valor de retorno"
retorno = subproceso.exitcode 
```

Si el subproceso aún está vivo se devuelve `None`;
en caso contrario típicamente se devuelve `0`
si la ejecución terminó correctamente.

El valor de retorno puede cambiarse llamando a la función `exit()` del módulo `sys` dentro de la tarea:

```py
import sys

def tarea():
    # (rutina)
    # ....
    # valor retorno
    sys.exit( valor_custom )
```

## Ejemplo

Este demo imita el procesamiento paralelo
de varias tareas demandantes
e integra las opciones
y métodos vistos previamente:
argumentos, valor de retorno, etc.

!!! example "Procesos con retorno"


    ```py
    from multiprocessing import Process
    import sys

    from time import sleep, time
    from random import random

    def perder_tiempo(x, delay):
        """Esta tarea imita el procesamiento de una tarea demandante"""
        print(f"Nro. proceso: {x}, delay: {delay: 3.3} segundos")
        sleep(delay)
        sys.exit( x )


    inicio = time()
    # nuevos subprocesos
    N = 3
    lista_procesos = []
    for i in range(N):
        # duracion arbitraria
        delay = random()*3
        # argumentos en formato lista
        argumentos = [i , delay]
        # creacion del proceso
        proceso = Process(
            target=perder_tiempo,
            args=argumentos)
        proceso.daemon = True
        proceso.start()
        lista_procesos.append(proceso)

    # espera al cierre de procesos
    for proceso in lista_procesos:
        proceso.join()
        retorno = proceso.exitcode
        print(f"Valor de retorno: {retorno}")

    # reporte de duración total
    fin = time()
    print(f"Terminado - tiempo transcurrido: {fin-inicio: 3.3} segundos")
    ```

    El reporte producido es parecido al siguiente:
    
    ```
    Nro. proceso: 1, delay:  1.26 segundos
    Nro. proceso: 0, delay:  1.33 segundos
    Nro. proceso: 2, delay:  1.18 segundos
    Valor de retorno: 0
    Valor de retorno: 1
    Valor de retorno: 2
    Terminado - tiempo transcurrido:  1.35 segundos
    ```


