# Cola (Queue)

Las cola o *queue* es una estructura FIFO
implementada en base a tuberías y sincronizada mediante *locks* o *semaphores*.

A diferencia de las tuberías, las *queues*
son *Multiple In, Multiple Out* (MIMO),
es decir pueden ser accedidas desde más de dos procesos
tanto para leer información como para escribirla.
Sin embargo, si varios procesos
introducen datos dentro de la cola
en cortos periodos de tiempo
un tercer proceso que intente leerlos
podría ver alterado el orden de entrada.


## Creación


Las colas se crean desde la función `Queue()`,
la cual se puede obtener desde el módulo `multiprocessing`:

```py title="Queue - creación"
# importación
from multiprocessing import Queue

# creacion de cola
cola = Queue()
```

Por *default* el largo máximo de la cola es indefinido.
Con el atributo `maxsize` se puede limitar el tamaño máximo
de la cola:

```py title="Queue - creación, longitud limitada"
# importación
from multiprocessing import Queue

# creacion de cola
cola = Queue(maxsize = maximo_elementos)
```

Si el número ingresado es `0`
entonces la longitud es indefinida.


!!! warning "módulo `queue`"

    El [módulo `queue`](https://docs.python.org/es/3.13/library/queue.html#queue.Queue)
    proporciona una implementación más completa
    que la del módulo `multiprocessing`
    pero también más compleja de usar. 
    También incluye implementaciones alternativas.


## Métodos




### Contar elementos

El método `qsize()` cuenta cuántos elementos
hay guardados en la cola.


### Cola vacía

El método `empty()` chequea si la cola está
totalmente vacía.



### Cola llena

El método `full()` verifica si se alcanzó
la longitud máxima de cola.



### Cargar elemento

El método `put()` intenta cargar
el objeto elegido dentro de la cola:

```py
cola.put( objeto_entrada)
```

Si la cola está llena
entonces este método bloquea
la ejecución de la rutina
hasta que se libere espacio de la cola.
Este comportamiento puede alterarse
con los argumentos opcionales `block` y `timeout`:

- Si `block` es `False` se dispara de inmediato
    la excepción `queue.Full`;
- Si `block` es `True` y `timeout` es un numero entero
    entonces se espera ese númmero de segundos
    y si no se liberó espacio
    se dispara la excepción `queue.Full`.

Los valores predefinidos de estas opciones son
`block=True` y `timeout=None`


### Extraer elemento

El método `get()` lee el valor del primer elemento ingresado
en la cola y lo quita de la misma.

```py
cola.get( objeto_entrada)
```

Este método por *default*
bloquea la ejecución de la rutina
de manera indefinida
en caso que la cola esté vacía.

`get()` es el método complementario de `put()`
y tiene sus mismos argumentos opcionales, `block` y `timeout`.
La excepción producida por este método
se llama `queue.Empty`.


### Cierre

El método `close()` ordena el cierre de la cola
mientras impide la entrada de nuevos datos.
El cierre puede no ser inmediato
sino que se espera a su vaciado.
El vaciado completo se detecta
con otro método llamado `join_thread()`


## Otras implementaciones 

El módulo `multiprocessing` trae
dos variantes adicionales
de `Queue`:

### `SimpleQueue`


`SimpleQueue` es una versión simplificada de `Queue`
que sólo dispone de los métodos `get()`, `put()`, `empty()` y `close()`.
Los argumentos opcionales están deshabilitados.

### `JoinableQueue`

`JoinableQueue` es una variante más completa de `Queue`
que incluye los métodos adicionales
`task_done()` y `join()`.
<!-- 
`join()` bloquea la rutina hasta que la cola esté vacía,
 -->

## Ejemplo

Este ejemplo muestra una comunicación sencilla
entre dos subprocesos usando *queues*.

??? example "Queues - demo"

    En este primer ejemplo se crea una cola
    sin tope de longitud:

    ```py hl_lines="2 6 12-13 24"
    from multiprocessing import Process
    from multiprocessing import Queue
    from time import sleep

    # creacion de cola
    cola = Queue()


    def receptor(c: Queue):
        """Tarea para la recepcion de datos"""
        print("Receptor listo")
        while c.empty() is False:
            elemento = c.get()
            print(f"recibido: {elemento}")
        print("recepcion finalizada")
        print()


    def transmisor(c: Queue):
        """Tarea para el envio de datos"""
        print("Transmisor listo")
        lista = ["hola", 1.0 , True, 27]
        for l in lista:
            c.put(l)
            print(f"enviado: {l}")
        print("transmision finalizada")
        print()


    # subprocesos para gestionar la cola
    sub_transmisor = Process(
        target=transmisor,
        args=(cola,),
        )

    sub_receptor = Process(
        target=receptor,
        args=(cola,),
        )

    # puesta en marcha - leve delay entre procesos
    sub_transmisor.start()
    sleep(0.2)
    sub_receptor.start()

    # espera al cierre de procesos
    sub_receptor.join()
    sub_transmisor.join()
    print("Finalizado")
    ```

    El reporte es el siguiente:

    ``` 
    Transmisor listo
    enviado: hola
    enviado: 1.0
    enviado: True
    enviado: 27
    transmision finalizada

    Receptor listo
    recibido: hola
    recibido: 1.0
    recibido: True
    recibido: 27
    recepcion finalizada

    Finalizado
    ```


## Referencias

[Python.org - Módulo `multiprocesing`](https://docs.python.org/es/3/library/multiprocessing.html#multiprocessing.Queue)