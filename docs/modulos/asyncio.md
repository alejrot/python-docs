



# Ejecución Asincrónica - Módulo Asyncio

Asyncio (*asynchronous I/O*) es el módulo encargado de implementar los mecanismos de ejecución asincrónica. La ejecución asincrónica consiste en repartir aquellas rutinas del programa que dependan de recursos no siempre disponibles (respuestas de servidores externos, entradas de usuario, etc) de modo que éstas puedan ejecutarse de manera independientes unas de otras a medida que los recursos estén disponibles. De esta manera se aprovecha mejor el tiempo cuando los recursos requeridos están ocupados minimizando los tiempos muertos. 

Asyncio también incluye gestión de streams , manejo de colas ,etc.

## Importacion

El módulo debe importarse cada vez que se requiera su uso:

```py
import asyncio
```


## Corrutinas

La ejecución asíncrona se basa en **corrutinas**. Las corrutinas son funciones no bloqueantes, es decir que si no pueden continuar su ejecución éstas quedan en suspenso y mientras tanto se pueden ejecutar otras corrutinas que sí dispongan de las condiciones para ejecutarse.

### Definición y ejecución simple

Las corrutinas se definen como funciones comunes, excepto que son precedidas con la sentencia `async`:

```py title="Corrutinas " hl_lines="5 12"
import asyncio
from datetime import datetime

# definicion de corrutina
async def corrutina(nombre :str , duracion: int):
    print(f"Nombre: {nombre}, inicio: {datetime.now()}, duracion: {duracion}s")
    await asyncio.sleep(duracion)   # NO bloquea la ejecucion de otras corrutinas
    print(f"Nombre: {nombre}, fin: {datetime.now()}")


# ejecucion de corrutina
asyncio.run(corrutina("A",1))
```
La función `run()` ordena la ejecución de la corrutina desde la rutina principal del programa.


### Ejecución secuencial

Si se intenta ejecutar varias corrutinas con la función  `run()` entonces éstas se ejecutarán en sucesión, es decir cada una esperará a la finaliazación de la anterior para comenzar:

```py title="Corrutinas - Ejecución sucesiva" 
asyncio.run(corrutina("A",1))
asyncio.run(corrutina("B",1))
asyncio.run(corrutina("C",1))
asyncio.run(corrutina("D",1))
```

`run()` se recomienda para ejecutar los puntos de acceso de máximo nivel. Las corrutinas pueden ser ejecutadas dentro de otras corrutinas con ayuda de la sentencia `await`:

```py title="Corrutinas - Ejecución sucesiva" 
async def principal():
    await corrutina("A", 1)
    await corrutina("B", 1)
    await corrutina("C", 1)
    await corrutina("D", 1)


asyncio.run(principal())
```

!!! warning "await"

    La sentencia `await` (*esperar*) espera a que la corrutina indicada finalice y devuelva su retorno para poder continuar.

    La sentencia `await` sólo puede usarse dentro de las corrutinas, en caso contrario se produce un `SyntaxError`.


### Ejecucion concurrente


La ejecución concurrente hace que las corrutinas comiencen todas al mismo tiempo y se espere a que todas estén completas para finalizar la ejecución.

Para poder ejecutar las corrutinas de forma concurrente se usa la función `gather()`:

```py title="Corrutinas - Ejecución concurrente" hl_lines="2 10"
async def corrutinas_concurrentes():
    await asyncio.gather(
        corrutina("A", 1),
        corrutina("B", 2),
        corrutina("C", 3),
        )


# orden de ejecucion asincrona
asyncio.run(corrutinas_concurrentes())
```

Con `await` se espera a que todas las corrutinas terminen de ejecutarse para poder continuar. 





!!! info "Función sleep()"
    El ḿodulo **asyncio** implementa su propia versión de la función `sleep()`. Esta versión, a diferencia de la implementación en el módulo **time**, no bloquea la ejecución del programa sino que deja la corrutina en suspenso hasta el final del retardo. 

    ```py title="Función sleep()" 
    await asyncio.sleep(tiempo)   
    ```
    Esta función se usa siempre dentro de corrutinas y se invoca con la cláusula `await` que permite el retorno a la corrutina tras la espera.




## Tareas


Con la función `create_task()` se pueden crear múltiples tareas, cada una de las cuales ejecutará una corrutina interna.


```py title="Tareas" hl_lines="3 4"
async def principal():

    tarea1 = asyncio.create_task( corrutina("A", 3) )
    tarea2 = asyncio.create_task( corrutina("B", 1) )

    await tarea1
    await tarea2


asyncio.run(principal())
```

Las tareas son usadas para programar corrutinas **concurrentemente**.
Éstas se programan automáticamente para ser ejecutadas en breve.

Las tareas deben ser esperadas con `await`. Si la corrutina interna levanta un error entonces éste se propagará a la tarea. 

Las tareas se pueden cancelar con el metodo `cancel()`. Al interrumpirse la tarea se elevará un error del tipo `CancelledError`. Si una tarea ya está ejecutándose cuando se intenta cancelarla entonces ésta se interrumpirá al llegar al próximo `await`.



## TaskGroup() 

Con la clase `TaskGroup()` se pueden agrupar múltiples tareas en un unico grupo para ejecutarlas de forma concurrente:

```py title="Tareas con TaskGroup()"  hl_lines="2"
async def principal():
    async with asyncio.TaskGroup() as grupo:
        # tareas internas - ejecucion concurrente
        tarea1 = asyncio.create_task( corrutina("A", 3) )
        tarea2 = asyncio.create_task( corrutina("B", 1) )

        await tarea1
        await tarea2


asyncio.run(principal())
```


La cláusula `with` asegura el cierre del grupo y la liberación de recursos al terminar, lo cual es considerado una buena práctica.



## Timeouts - tiempo limite 

`timeout()` pone un tope al tiempo de espera para completar las corrutinas internas, cuya ejecución es concurrente.

El tiempo de espera se indica en segundos.

```py title="Tareas con timeout()" hl_lines="2"
async def principal():
    async with asyncio.timeout(5):  # tiempo espera máximo: 5 segundos
        # tareas internas - ejecución concurrente
        tarea1 = asyncio.create_task( corrutina("A",  3) )
        tarea2 = asyncio.create_task( corrutina("B",  1) )
        tarea3 = asyncio.create_task( corrutina("C", 10) ) # tiempo espera excesivo

        await tarea1
        await tarea2
        await tarea3


asyncio.run(principal())
```


Si las tareas internas no se ejecutan dentro del tiempo límite éstas se cancelan y se eleva el error `TimeoutError`.  

Si el tiempo especificado es `None` el tiempo de espera es indefinido. El tiempo puede redefinirse con `Timeout.reschedule()`








## Loop de Eventos


Los bucles de eventos son APIs de bajo nivel del módulo, las cuales son la base de 

Este es un ejemplo de uso donde se usan varios métodos habituales del loop de eventos:

```py title="Uso del loop de eventos" hl_lines="6 14 17 18 21"
from datetime import datetime
import asyncio

async def corrutina(nombre :str , duracion: int):
    # consulta del loop actual
    bucle = asyncio.get_event_loop()
    print(bucle)

    print(f"Nombre: {nombre}, inicio: {datetime.now()}, duracion: {duracion}s")
    await asyncio.sleep(duracion)   
    print(f"Nombre: {nombre}, fin: {datetime.now()}")

# nuevo bucle asíncrono
loop = asyncio.new_event_loop()

# ejecucion secuencial, hasta terminar
loop.run_until_complete(corrutina("A", 1))
loop.run_until_complete(corrutina("B", 3))

# Cierre de bucle manual
loop.close()
```

[Más del buvle de eventos de Python: documentacion oficial](https://docs.python.org/3/library/asyncio-eventloop.html)


## Multithreading



Supongase el ejemplo de la siguiente función:

```py 
from datetime import datetime
import time

def rutina(nombre :str , duracion: int=4):

    print(f"Nombre: {nombre}, inicio: {datetime.now()}, duracion: {duracion}s")
    time.sleep(duracion)      # bloquea la ejecucion concurrente
    print(f"Nombre: {nombre}, fin: {datetime.now()}")
    return duracion

```

Ésta puede ser llamada desde una corrutina de varias maneras. Una de ellas es mediante la función `to_thread()`:


```py title="Multithreading - to_thread()" hl_lines="3"
# definicion de corrutina
async def principal():
    resultado = await asyncio.to_thread(rutina, nombre="Y", duracion=2) 
    print(resultado)    # '2'


# ejecucion de corrutina
asyncio.run(principal())
```

Otra forma es el método `run_in_executor()` del la clase `get_event_loop()`:

```py title="Multithreading - run_in_executor()" hl_lines="3 4"
# definicion de corrutina
async def principal():
    bucle = asyncio.get_event_loop()    # bucle actual
    resultado = await bucle.run_in_executor(None, rutina, "X", 3)   
    print(resultado)    # '3'


# ejecucion de corrutina
asyncio.run(principal())
```

Asimismo ambas formas pueden usarse juntas dentro de `gather()`:


```py title="Multithreading - gather" hl_lines="3-6"
# definicion de corrutina
async def principal():
    resultado = await asyncio.gather(
        bucle.run_in_executor(None, rutina, "X", 3),     
        asyncio.to_thread(rutina, nombre="Y", duracion=2) 
        )
    print(resultado)        # '[3,2]'


# ejecucion de corrutina
asyncio.run(principal())
```







El método `run_in_executor()`delega la ejecución a otro thread, lo cual permite activar el procesamiento paralelo por parte del procesador. **La función de entrada no debe ser corrutina** sino que debe ser una función normal.



## Manejo de errores

Se usan habitualmente las cláusulas `try` y `except` dentro de las corrutinas.

En caso de manejarse un bucle de eventos, el método `set_exception_handler()` del loop de eventos permite también el manejo de todas las corrutinas dentro del loop.


!!! danger "Propagación de errores"

    Los errores producidos en las corrutinas se propagan a las rutinas y corrutinas superiores. Por ello es fundamental implementar el manejo de errores para evitar errores y fallos críticos en el programa.


## Limitaciones de asyncio

- No es apta para tareas con uso intensivo de CPU.
- Las excepciones no manejadas dentro de las corrutinas no obligan a la salida inmediata del sistema, por ello suelen ser difíciles de debuggear.
- Las corrutinas usan un único hilo y no admiten por sí mismas el uso de multiples hilos.


## Buenas Prácticas

- Usar `asyncio.run()` es la forma recomendada de ejecutar funciones de alto nivel debido a su simplicidad.
- Manejar las excepciones previene que los errores se propaguen a la rutina principal
- `async with` para manejo de recursos.
- Limitar tareas concurrentes: funciones `asyncio.Semaphore` y `asyncio.BoundedSemaphore`.
- Usar  `asyncio.gather()` para ejecutar múltiples corrutinas simultáneas.


## Referencias

[Documentacion oficial de Python](https://docs.python.org/3/library/asyncio.html)

[Gyata AI - Mastering Asyncio in Python](https://www.gyata.ai/python/asyncio#best-practices-for-using-asyncio)

[MoureDev TV - Asincronía](https://youtu.be/YA8Ssd3AUwA?list=PLv0dxH7HRDx_kQRNoldG7iPvydy8DyvE3)