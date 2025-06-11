# Bloqueos (*lock*)


A menudo se requiere sincronizar varios procesos paralelos para poder presentar resultados,
acceder a ciertos recursos compartidos, 
etc. de manera que sólo uno de ellos pueda acceder a la vez.
Uno de los métodos más habituales para este propósito
es el uso del bloqueo o candado (*lock*).


## Creación

El bloqueo es creado con la función `Lock()`,
el cual se importa desde el módulo `multirpocessing`:

```py title="Creacion candados"
from multiprocessing import Lock

bloqueo = multiprocessing.Lock()
```

## Uso

### Manual

Una forma de usar el bloqueo es mediante el uso manual del bloqueo
con los métodos `acquire()` y `release()`:

```python title="Uso candados" hl_lines="2 8"
# bloqueo manual
bloqueo.acquire()

# acceso al recurso protegido
numero_compartido.value += 1

# liberacion manual
bloqueo.release()
```

El método `acquire()` hace que el bloqueo impida
el acceso a otros procesos
del recurso compartido.
Una vez utilizado el recurso protegido 
es indispensable liberar su acceso
llamando al método `release()`,
de otra manera los otros procesos
quedarán suspendidos indefinidamente.


### Con administrador de contexto

Otra forma de usar el bloqueo es con la ayuda de la clásula `with`:

```python title="Uso candados - con with" hl_lines="1"
with bloqueo:
    # recurso compartido
    numero_compartido.value += 1
```

En este caso el bloqueo y la liberación del recurso
se hacen automáticamente.



## Ejemplo de uso

Tómese por ejemplo un programa que crea cuatro procesos,
los cuales acceden a un recurso compartido y se demoran en ello exactamente 0.5 segundos:

```py
from multiprocessing import Process, Value, Lock
from time import time, sleep


contador = Value('d', 0)
bloqueo  = Lock()

def incremento():
    """Se imita una tarea que intenta acceder a un recurso compartido."""
    with bloqueo:
        # se simula un recurso ocupado o una rutina exigente
        sleep(0.5)
        # acceso a un recurso compartido
        contador.value += 1


tiempo_inicio = time()

# procesos con acceso al recurso compartido
subprocesos = [Process(target=incremento) for n in range(4)]
for proceso in subprocesos:
    proceso.start()

# espera al cierre de procesos
for proceso in subprocesos:
    proceso.join()

tiempo_fin = time()
print("Tiempo ejecución: %.2f seg" % (tiempo_fin - tiempo_inicio))
print("El número compartido es %d" % (contador.value))
```

En este ejemplo
el resultado es la ejecución concurrente de los procesos
debido a que el bloqueo sólo admite el acceso de un proceso a la vez:

```
Tiempo ejecución: 2.01 seg
El número compartido es 4
```