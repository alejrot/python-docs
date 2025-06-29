
# información de procesos

## ID de procesos

El número identificador (ID) del proceso creado
se consulta con el atributo `pid`:

```python title="ID del proceso"
pid = subproceso.pid
```
Este número es gestionado por el sistema operativo
y no es modificable.

El subproceso no es capaz de ver este atributo.



!!! tip "Modulo `os`"


    El módulo `os`
    incluye los métodos `getpid` y `getppid`
    para consultar el ID propio y el del proceso invocador.


    ```py title="IDs desde subproceso"
    os.getpid()     # ID proceso actual
    os.getppid()    # ID proceso padre
    ```

    Ejemplo de uso:

    ```py title="IDs - consulta"
    from multiprocessing import Process
    import os


    def identificador():
        print("Proceso hijo")
        print("ID:       %s" % (os.getpid()))
        print("ID padre: %s" % (os.getppid()))


    subproceso = Process(target=identificador)
    subproceso.start()
    subproceso.join()

    print("Proceso original")
    print("ID hijo:  %s" % (subproceso.pid))
    print("ID:       %s" % (os.getpid()))
    ```

    En el mensaje creado  en consola 
    se verifican que los números de ID coinciden: 

    ``` title="IDs - Reporte"
    Proceso hijo
    ID:       3502272
    ID padre: 3502271
    Proceso original
    ID hijo:  3502272
    ID:       3502271
    ```
