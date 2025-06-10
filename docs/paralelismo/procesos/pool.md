

# Reservas de trabajadores (*pools*)

Las *pools of workers* o "reservas de trabajadores" funcionan como una reserva de tareas a ejecutarse en procesos hijos paralelos.
Las reservas administran la cantidad de procesos hijos en simultáneo
de manera que éstos no superen la cantidad máxima elegida.
Cada tarea de entrada es asignada a un proceso hijo y puesta en marcha
automáticamente
a menos que la cantidad máxima de procesos elegida haya sido alcanzada.
En tal caso, la reserva deja las tareas sin asignar en espera
hasta que los procesos ya creados vayan terminando
e crea nuevos procesos hasta alcanzar el máximo nuevamente o terminar la lista.

Este mecanismo ayuda a utilizar más eficientemente los recursos del sistema ante un gran nuḿero de tareas,
al prevenir que una cantidad exagerada de procesos sean creados simultáneamente y consuman los recursos de manera inútil o lleven incluso al fallo del programa.

## Creación

La reserva se crea con la función `Pool()`, al cual debe indicársele el máximo número de procesos ejecutables en paralelo:

```py title="Crear pool"
pool = multiprocessing.Pool(processes=nro_procesos_simultaneos)    
```
El número de procesos elegidos
es típicamente el número de núcleos disponibles del procesador a usar.

## Asignación

Con el método `map()` se ordena la ejecución simultánea de un grupo de tareas:

```py   title="Arrancar pool"
pool.map(funcion_tarea, lista_argumentos) 
```

Los argumentos se condensan en una lista,
de manera que la reserva pueda asignar un elemento
a cada nuevo *worker*.

A medida que se termina una tarea se cierra su proceso y se arranca uno nuevo para ejecutar la próxima tarea pendiente. 

## Cierre

El cierre de la reserva se asegura con el método `terminate()`:

```py title="Cerrar pool"
pool.terminate()
```

Este método espera a que todos los *workers* internos hayan completado su tarea,
entonces la ejecución de la rutina continúa.


## Conteo de núcleos

El módulo `multiprocessing` dispone de la función `cpu_count()` para consultar el número de núcleos lógicos existentes en el sistema:

```py title="Nº de Núcleos" 
from multiprocessing import cpu_count

nro_cores = cpu_count()  
```
Debe tenerse en cuenta que algunos núcleos pueden no estar disponibles para su uso.


## Ejemplo de uso

En este ejemplo se crean varias tareas
que demoran un número arbitrario de segundos para finalizar.
Los argumentos de estas tareas
son el nombre asignado a cada una.


```py title="Ejemplo - demora arbitraria"
import random
import time
from multiprocessing import Pool, cpu_count


# tarea genérica con argumentos de entrada
def tarea(nombre: str) -> None:
    print(f'Arranca el trabajador de "{nombre}"')
    # tiempo de ejecución aleatorio
    tiempo_rutina = random.choice(range(1, 5))
    time.sleep(tiempo_rutina )
    print(f'Tarea "{nombre}" finalizada en {tiempo_rutina} segundos')


# lista de argumentos - nombres para cada tarea 
nombres_proceso = [f'Tarea_{i}' for i in range(1, 9)]

# consulta de nucleos logicos
nro_cores = cpu_count()            

# ejecución de a grupos 
pool = Pool(processes=nro_cores) 
pool.map(tarea, nombres_proceso)    

# cierre de reserva
pool.terminate()
```

Si el código es ejecutado en un equipo de 4 núcleos,
el resultado es un texto en consola como el que sigue:

``` title="Texto en consola"
Arranca el trabajador de "Tarea_1"
Arranca el trabajador de "Tarea_2"
Arranca el trabajador de "Tarea_3"
Arranca el trabajador de "Tarea_4"
Tarea "Tarea_4" finalizada en 1 segundos
Arranca el trabajador de "Tarea_5"
Tarea "Tarea_1" finalizada en 3 segundos
Arranca el trabajador de "Tarea_6"
Tarea "Tarea_5" finalizada en 2 segundos
Arranca el trabajador de "Tarea_7"
Tarea "Tarea_2" finalizada en 4 segundos
Arranca el trabajador de "Tarea_8"
Tarea "Tarea_3" finalizada en 4 segundos
Tarea "Tarea_8" finalizada en 1 segundos
Tarea "Tarea_7" finalizada en 2 segundos
Tarea "Tarea_6" finalizada en 4 segundos
```

Nótese como al comienzo
sólo se ponen en funcionamiento los primeros 4 procesos
y los demás se ponen en marcha de a uno
a medida que los anteriores se terminan.

