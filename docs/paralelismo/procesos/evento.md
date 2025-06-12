
# Evento (*event*)

El elemento de sincronismo `Event` permite
dejar en espera la rutina de un proceso
y habilitar su ejecución desde otro.

## Creación

Los eventos se crean con la función `Event()`,
la cual se importa desde el módulo `multiprocessing`:

```py title="Eventos - creación"
from multiprocessing import Event

evento = Event()
```
Esta función no tiene argumentos.
El evento se crea en estado deshabilitado.

## Uso


### Consulta de estado

El método `is_set()` verifica si el evento ha sido habilitado. 

```py title="Eventos - consulta"
evento.is_set()
```

### Espera de evento

La suspensión condicional de la rutina
se impone con el método `wait()`:

```py title="Eventos - espera"
evento.wait()
```

Si el evento fue habilitado 
entonces el evento permitirá la ejecución
de la rutina posterior;
en caso contrario el proceso quedará en espera.


### Orden de espera

El evento se deshabilita con el método `clean()`,
lo que ordena el bloqueo con el método `wait()`.

```py title="Eventos - borrado"
evento.clear()
```

### Orden de ejecución

El método `set()` es el encargado de habilitar el evento,
desbloqueando el método `wait()`:

```py title="Eventos - seteo"
evento.set()
```

## Ejemplo de uso

En este ejemplo se muestra la implementación de un medidor de progreso
implementado en un proceso hijo,
el cual se autobloquea cada vez que se imprime el proceso en pantalla.

```py title="Medidor de progreso - proceso indicador"
def mostrar_progreso():
    """Esta tarea reporta en consola el porcentaje de procesos completados."""
    while True:
        proceso_finalizado.wait()   # espera
        i = contador_procesos.value
        proceso_finalizado.clear()   # bloqueo
        print(f"Progreso: {100*i/N: 3.4}%")
```

El trabajo se reparte en otros subprocesos 
que liberan la ejecución del proceso medidor
a medida que se completan:


```py title="Medidor de progreso - procesos de carga"
def perder_tiempo(x, delay):
    """Esta tarea imita el procesamiento de una tarea demandante"""
    print(f"Nro. proceso: {x}, delay: {delay: 3.3} segundos")
    sleep(delay)
    contador_procesos.value += 1
    proceso_finalizado.set()    # liberacion
```

??? example "Rutina completa"

    ```py title="Medidor de progreso - rutina completa" hl_lines="7 14-16 25"
    from multiprocessing import Process
    from multiprocessing import Value, Event
    from time import sleep, time
    from random import random

    contador_procesos = Value('i', 0)
    proceso_finalizado = Event()

    N = 6

    def mostrar_progreso():
        """Esta tarea reporta en consola el porcentaje de procesos completados."""
        while True:
            proceso_finalizado.wait()
            i = contador_procesos.value
            proceso_finalizado.clear()
            print(f"Progreso: {100*i/N: 3.4}%")


    def perder_tiempo(x, delay):
        """Esta tarea imita el procesamiento de una tarea demandante"""
        print(f"Nro. proceso: {x}, delay: {delay: 3.3} segundos")
        sleep(delay)
        contador_procesos.value += 1
        proceso_finalizado.set()


    # proceso monitor - cierre automático
    monitor = Process(
        target=mostrar_progreso
        )
    monitor.daemon = True
    monitor.start()

    lista_procesos = []

    inicio = time()
    for i in range(N):
        # duracion arbitraria
        delay = random()*5
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

    # reporte de duración total
    fin = time()
    print(f"Terminado - tiempo transcurrido: {fin-inicio: 3.3} segundos")
    ```

    El reporte por consola es similar a este:

    ``` title="Medidor de progreso - reporte"
    Nro. proceso: 0, delay:  2.44 segundos
    Nro. proceso: 2, delay:  1.05 segundos
    Nro. proceso: 3, delay:  0.235 segundos
    Nro. proceso: 1, delay:  4.19 segundos
    Nro. proceso: 4, delay:  3.12 segundos
    Nro. proceso: 5, delay:  1.33 segundos
    Progreso:  16.67%
    Progreso:  33.33%
    Progreso:  50.0%
    Progreso:  66.67%
    Progreso:  83.33%
    Progreso:  100.0%
    Terminado - tiempo transcurrido:  4.2 segundos
    ```

