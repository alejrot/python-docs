


## Hilos (*threads*)

Los ***threads*** (hilos, hebras, etc) son **bifurcaciones internas** de los procesos que el desarrollador realiza deliberadamente. Esta práctica ayuda a que un mismo núcleo del procesador modernos pueda ejecutar varios trozos de código en simultáneo. 

Los hilos comparten el acceso a las variables y funciones globales del programa. Además, el cambio de hilos en ejecución por el proceso es bastante rápido por no exigir el llamado al sistema operativo.

!!! info "Superescalabilidad"

    Existe un mecanismo tácito para aprovechar el paralelismo entre instrucciones de un mismo hilo llamado **superescalabilidad**, donde el hardware del procesador intenta detectar instrucciones independientes entre sí de la rutina actual y las ejecuta en paralelo. 
     

## Importación

Para poder crear nuevos hilos se requiere importar el módulo `threading`:

```python
import threading
```


## Uso de hilos

### Creación


El hilo se crea con la función `Thread()`, el cual incluye como argumento la función que engloba la rutina que debe ejecutarse: 

```python title="Creación de threads" hl_lines="5"
def tarea():
    return

# creacion del hilo
hilo = threading.Thread(target=tarea) 
```
Si la rutina / función requiere valores de entrada estos se adjuntan como una lista o tupla dentro de la función `Thread()`: 

```python title="Creación de threads - con argumentos" hl_lines="8"
def tarea(x,y):
    return

# argumentos = [x,y]      argumentos en formato lista
argumentos = (x,y,)       #formato alternativo

# creacion del hilo
hilo = threading.Thread(target=tarea, args=argumentos) 
```

### Arranque

La ejecución **no** comienza de inmediato sino que se ordena con el método `start()`:

```py title="Arranque de threads"
# orden de ejecucion del hilo
hilo.start()    
```

### Espera al cierre

Si se necesita esperar a la finalizacion del hilo creado se recurre al método `join()`. Con él el hilo principal queda en espera hasta que que el hilo se cierre.

```py title="Espera al cierre"
# espera a la finalizacion del hilo para continuar
hilo.join()     
```
Puede definirse un tiempo de cierre máximo para la espera de la función.

```py title="Espera al cierre - con timeout"
hilo.join(timeout)     
```
Si `timeout` es `None` entonces el tiempo de espera es indefinido.


## Intercambios y sincronización

### Variables compartidas

Los hilos de derivados de un hilo principal comparten con el mismo un mismo proceso , y por ello tienen acceso a todas sus variables globales y datos globales internos. Por ello, a diferencia de los subprocesos, no requieren en principio la creación de variables ni datos compartidos.


### Bloqueos

Los hilos, al igual que los procesos, recurren al uso de bloqueos para sincronizar hilos, proteger recursos compartidos, evitar errores, etc.

El módulo `threading` tiene su propia implementación de los bloqueos: *`threading.Lock()`*


```py title="Crear bloqueos"
bloqueo = threading.Lock()     
```

Los bloqueos pueden usarse con cierre y apertura manual , o bien con ayuda de la cláusula `with`


```py title="Uso bloqueos - manual"
bloqueo.adquire()     
# Rutina protegida    
bloqueo.release()     
```

```py title="Uso bloqueos - claúsula with"
with bloqueo:
    # Rutina protegida    
```

El estado actual del bloqueo se consulta con el método `locked()`:

```py title="Uso bloqueos - estado actual"
estado = bloqueo.locked()  
```


## Atributos de los *threads*


### Estado


`is_alive()`


`threading.active_count()`

`threading.current_thread()`




### Hilos 'daemon'

Los hilos daemonicos no admiten crear hilos derivados. Además se cierran automáticamente cuando el hilo principal del proceso se cierra. Deben configurarse como tales antes de comenzar la ejecución del hilo.

```py title="Configuracion como daemon"
hilo.daemon = True
```

## Barreras (*barrier*)

Las barreras son primitivas sencillas para sincronizar un numero fijo de hilos. Los hilos se bloquean al invocarse en ellos el método `wait()` hasta que todos ellos estén bloqueados por dicho método, liberándose entonces la ejecución de todos ellos.

```py title="Barreras"  hl_lines="1 5 10"
barrera = threading.Barrier( nro_hilos , timeout=None)

Tarea_1():

    barrera.wait()


Tarea_2():

    barrera.wait()
```



## Referencias

[Learn Tutorials - Procesos e hilos](https://learntutorials.net/es/python/topic/4110/procesos-e-hilos)


[Documentación oficial - Threading](https://docs.python.org/3/library/threading.html#threading.Barrier.wait)