https://learntutorials.net/es/python/topic/4110/procesos-e-hilos
https://docs.python.org/es/3/library/multiprocessing.html

<!-- # Procesos e Hilos
 -->


# Procesos (*proccess*)

Los procesos (***process***) son **"programas" unitarios** cuya ejecución es gestionada por el sistema operativo, el cual asigna cada proceso en activo a un núcleo del procesador que esté disponible para que se encargue de ejecutarlo. Los demás procesos quedan en espera hasta que el sistema operativo los ponga en activo de nuevo, los cierre o simplemente se terminen.

Un programa completo puede estar compuesto por múltiples procesos vinculados entre sí. Esto permite:

- modularizar el programa al dividirlo en rutinas específicas;
- mejorar los tiempos de ejecución al repartir varios subprocesos del programa entre los núcleos del procesador, permitiendo la ejecución simultánea.

## Importación

Crear procesos requiere de importar el modulo `multiprocessing`:

```python
import multiprocessing
```


## Uso de procesos

### Creación


El nuevo proceso se crea con la función `Process()`, al cual se le debe asignar el nombre de una función o *"tarea"* a ejecutar en un nuevo proceso:

```py title="Creación procesos" hl_lines="6"
# rutina para el nuevo proceso
def tarea():
    return

# creacion del proceso
proceso = multiprocessing.Process(target=tarea)
```

Si la rutina requiere argumentos de entrada estos se adjuntan como una lista o tupla dentro de la función `Process()`

```py title="Creación procesos - con argumentos" hl_lines="7"
def tarea(x, y):
    return

# argumentos = [x,y]      # argumentos en formato lista
argumentos = (x,y,)       # formato alternativo
# creacion del proceso
proceso = multiprocessing.Process(target=tarea, args=argumentos) 
```
!!! info "Proceso hijo"
    El nuevo proceso creado es considerado como ***proceso hijo*** del proceso que lo creó. También se lo suele llamar ***subproceso***.

### Arranque 

El nuevo proceso queda en stand-by hasta que se ordene el arranque con el método `start()`:

```python
# orden de ejecucion del proceso
proceso.start()
```


### Espera al cierre 


Si se requiere esperar el cierre del proceso creado para ejecutar más código se recurre al método `join()`. Con él el proceso que llama al método permanecerá en espera hasta que el proceso se termine:

```py title="Espera al cierre"
# espera a que el proceso se cierre
proceso.join()
```
Al método `join()` se le puede asignar un tiempo máximo de bloqueo como argumento:
```python title="Espera al cierre - con timeout"
# espera a que el proceso se cierre 
tiempo = 5
proceso.join(tiempo)  # bloqueo por 5 segundos como máximo
```

## Atributos



### Estado actual


El estado actual del proceso se consulta con el atributo `exitcode` o con el método `is_alive()`:
```python title="Estado de ejecución"
proceso.exitcode   # codigo de salida del proceso; 'None' si sigue vivo
proceso.is_alive() # booleano: 'True' si sigue vivo
```

### Identificación

El nombre y el número ID (identificador) del proceso hijo se consultan con los atributos `name` y `pid`:

```py title="Identificación de subproceso"
proceso.name    # nombre del proceso
proceso.pid     # numero identificador (ID) del proceso
```
<!-- Ejemplo:[procesos_multiples.py](procesos_multiples.py)  -->


En cambio, para conocer el identificador del proceso padre y el del proceso padre se recurre al módulo `os`(sistema operativo):

```py title="Identificación de subproceso"
os.getpid()     # ID proceso actual
os.getppid()    # ID proceso padre
```




!!! example "Ejemplo"

    ```py
    import multiprocessing
    import os
    import time

    # tareas de 1 segundo cada una
    def tarea():
        time.sleep(1)
        # print(proceso.is_alive())
        print("PID:  %s" % (os.getpid(),))
        print("El ID del proceso padre es: %s" % (os.getppid()))


    inicio = time.time()
    # Creacion de lista de procesos en bucle
    procesos = [multiprocessing.Process(target=tarea) for _ in range(4)]
    # llama a los procesos para ejecutar
    for proceso in procesos:
        proceso.start()
    # espera hasta que cada proceso termine
    for proceso in procesos:
        proceso.join()  
        
    fin = time.time()
        
    print("Tiempo ejecución: %.2f seg" % (fin - inicio))    # 'Tiempo ejecución: 1.04 seg'
    ```

### Configuración como 'daemon'

El atributo `daemon` configura al proceso como *'daemonic'*. Esto habilita el **cierre automatico** cuando el proceso padre sea cerrado e impide que el proceso 'daemonio' llame a sus propios subprocesos. Esta configuracion debe hacerse antes de llamar al metodo `start()`. 

```py title="Configuracion como daemon"
proceso.daemon = True
```


## Intercambios y sincronización


### Variables compartidas

Los procesos **no comparten variables** de manera predeterminada. Para crear variables y datos comunes a múltiples subprocesos se usan las funciones `Value()` y `Array()`:

```python title="Variables compartidas"
numero_compartido  = multiprocessing.Value('d', 0)  # variables
arreglo_compartido = multiprocessing.Array('i', range(10))  # datos
```



### Bloqueos (*lock*)


A menudo se requiere sincronizar varios procesos paralelos para poder presentar resultados, acceder a ciertos recursos compartidos, etc. Uno de los métodos más habituales es el bloqueo o candado (*lock*), creado con la función `Lock()`*

```py title="Creacion candados"
bloqueo = multiprocessing.Lock()
```

Una forma de usar el candado es mediante el uso manual del bloqueo con los métodos `acquire()` y `release()`:

```python title="Uso candados" hl_lines="2 8"
# bloqueo manual
bloqueo.acquire()

# recurso compartido
numero_compartido.value += 1

# liberacion manual
bloqueo.release()
```

Otra forma de usar el candado es con la ayuda de la clásula `with`:

```python title="Uso candados - con with" hl_lines="1"
with bloqueo:
    # recurso compartido
    numero_compartido.value += 1
```


!!! example "Ejemplo: variables compartidas y bloqueo de recursos" 

    ```py hl_lines="4 6 10 14 16"
    import multiprocessing, time

    numero_local = 0
    numero_compartido = multiprocessing.Value('d', 0)

    bloqueo = multiprocessing.Lock()

    def incremento():
        global numero_local
        with bloqueo:
            # se simula un recurso ocupado o una rutina exigente
            time.sleep(0.5)
            # Los subprocesos modifican COPIAS de la variable local
            numero_local += 1
            # El numero conpartido SÍ es modificado por los subprocesos
            numero_compartido.value += 1


    inicio = time.time()
    subprocesos = [multiprocessing.Process(target=incremento) for n in range(4)]
    for proceso in subprocesos:
        proceso.start()
    for proceso in subprocesos:
        proceso.join()
    fin = time.time()


    print("Tiempo ejecución: %.2f seg" % (fin - inicio)) 
    print("El numero local es %d; el numero compartido es %d" % (numero_local, numero_compartido.value))
    ```

    Resultado:
    ```
    Tiempo ejecución: 2.01 seg
    El numero local es 0; el numero compartido es 4
    ```



## Reservas (*pools*)

Las *pools* de procesos funcionan como una reserva de tareas a ejecutarse en procesos paralelos. 

La reserva se crea con la función `Pool()`, al cual debe indicársele el máximo número de procesos ejecutables en paralelo:

```py title="Crear pool"
pool = multiprocessing.Pool(processes=nro_procesos_simultaneos)    
```
El número de procesos es típicamente el número de núcleos disponibles del procesador a usar.

Con el método `map()` se ordena la ejecución simultánea de un grupo de tareas:

```py   title="Arrancar pool"
pool.map(funcion_tarea, argumentos) 
```
A medida que se termina una tarea se cierra su proceso y se arranca uno nuevo para ejecutar la próxima tarea pendiente. 

El cierre de la reserva se hace con el método `terminate()`:

```py   title="Cerrar pool"
pool.terminate()
```

!!! example "Ejemplo: Pool de 4 procesos, 16 tareas"

    ```py hl_lines="16 17 20"
    import random
    import time
    from multiprocessing import Pool

    # tarea genérica con argumentos de entrada
    def tarea(nombre: str) -> None:
        print(f'Started worker "{nombre}"')
        tiempo_rutina = random.choice(range(1, 5))
        time.sleep(tiempo_rutina )
        print(f'Tarea "{nombre}" finalizada en {tiempo_rutina} segundos')


    # nombres para cada tarea 
    nombres_proceso = [f'Tarea_{i}' for i in range(16)]

    pool = Pool(processes=4)            # cuatro procesos simultáneos
    pool.map(tarea, nombres_proceso)    # ejecución de a grupos de 4

    # cierre de reserva
    pool.terminate()
    ```


## Bifurcaciones (*forks*)

Un mecanismo antiguo para crear procesos es la bifurcación. Consiste en hacer una réplica exacta del proceso actual con ayuda de la función `fork()`, cuyo retorno permite discernir entre el proceso original y su clon. Recurre al módulo `os`.


```py title="Bifurcación (fork)" 
retorno = os.fork()
```

El valor de retorno obtenido no es igual para el proceso original que para su clon, permitiendo diferenciarlos desde la rutina:

| retorno | significado|
|:---:|:---|
|`valor > 0`| Es original $\rightarrow$ ID proceso clon|
|`valor == 0` | Es clon del proceso original |
|`valor < 0`| Error de bifurcación $\rightarrow$  clon fallido|



!!! example "Ejemplo: IDs de original y de clon"

    ```py title="Forks" hl_lines="7"
    import os

    # Rutina común
    print("¡Vamos a hacer un fork de un proceso!")

    # bifurcacion
    retorno = os.fork()

    # proceso padre: retorno = ID proceso hijo
    if retorno>=0:
        pid = os.getpid()
        print("Rutina del proceso original")
        print(f"pid: {pid}, retorno: {retorno}")

    # proceso hijo : retorno = 0
    elif retorno==0:
        pid = os.getpid()
        print("Rutina del proceso hijo")
        print(f"pid = {pid}, retorno: {retorno}")

    # error : retorno < 0
    else:
        print("Error de bifurcación")
    ```





## Asincronos
https://docs.python.org/es/3/library/asyncio-subprocess.html




## Referencias

[Learn Tutorials - Procesos e hilos](https://learntutorials.net/es/python/topic/4110/procesos-e-hilos)

[El Blog Python - Crea múltiples procesos en python](https://elblogpython.com/tutoriales-python/crea-multiples-procesos-en-python/)

[Documentación oficial - Multiprocessing](https://docs.python.org/es/3/library/multiprocessing.html)