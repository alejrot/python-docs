# Pipe


Las *pipes* ("tuberias") son un elemento de intercambio
que permite transmitir variables y datos entre dos procesos.
Los datos forman una estructura FIFO (*First In, First Out*):
los primeros datos en entrar son también los primeros en salir.

## Creación

La creación de tuberías
se realiza con la función `Pipe()`,
la cual se importa
desde el módulo `multiprocessing`:

``` py title="Pipe - creacion (duplex)"
from multiprocessing import Pipe

[extremo_A, extremo_B] = Pipe()
```

Esta función crea dos objetos juntos
que funcionan como extremos
del canal de comunicación.

Por *default* la transmisión es bidireccional (*duplex*).
Si se necesita hacer la transmisión unidireccional
entonces se asigna el valor `False` a su argumento `duplex`:

``` py title="Pipe - creacion (unidireccional)"
from multiprocessing import Pipe

[extremo_emisor, extremo_receptor] = Pipe(False)
```

## Métodos

### Sondeo

El método `poll()` ("sondeo", "encuesta")
permite tanto verificar la existencia de datos en la tubería
como bloquear la rutina hasta que se ingresen nuevos datos.

Modo sondeo: sin argumentos

```py title="Pipe - sondeo"
data_disponible = extremo.poll() 
```
Modo bloqueante: entrada `None`

```py title="Pipe - sondeo (modo bloqueante)"
extremo.poll(None) 
```


### Envío

Los objetos de entrada
(variables, datos estándar, otros)
se ingresan con el método `send()`:

```py title="Pipe - envio"
extremo.send( objeto_entrada )
```

Este método puede ser llamado
sucesivamente múltiples veces
para cargar múltiples objetos de datos en la tubería.
Estos datos quedan almacenados hasta que sean leídos.

El tamaño máximo típico del objeto enviado es de 32 MB.
Si se supera este valor
se dispara el error `ValueError`.

Si el objeto a enviar es una sucesión de bytes
entonces se usa el método `send_bytes()`

```py title="Pipe - envio binario"
extremo.send_bytes( objeto_binario )
```


### Recepción

La recepción se realiza con el método `recv()`,
el cual lee un único elemento recibido:

```py title="Pipe - recepción"
data = extremo.recv()
```
Este método bloquea la ejecución
si no hay datos dentro de la tubería.
El valor leído será el primero en haber sido ingresado
y será borrado de la tubería.

Si el otro extremo de la tuberia ya fue cerrado
y no quedan datos por leer se produce el error `EOFError`.

Si la información de entrada está en formato binario se usa el método `recv_bytes()`:

```py title="Pipe - recepción binaria"
data_binaria = extremo.recv_bytes()
```

### Identificación

El método `fileno()`
devuelve el identificador del extremo
de la tubería que lo llama:


``` py title="Pipe - identificador"
id_a = extremo_A.fileno()
id_b = extremo_B.fileno()
```

Nótese que los dos extremos no tienen el mismo ID.


### Cierre

El método `close()` cierra la conexión.
No anula el otro extremo del tubo.


## Ejemplo

Este demo sencillo muestra como mandar
una lista de valores predefinida
de un subproceso a otro.


```py
from multiprocessing import Process
from multiprocessing import Pipe

from time import sleep

# creacion de tuberia - unidireccional
[extremo_emisor, extremo_receptor] = Pipe(False)


def receptor(extremo_tubo):
    """Tarea para la recepcion de datos"""
    print("Receptor listo")
    if extremo_tubo.poll(None) is True:
        while extremo_tubo.poll() is True:
            # recepcion - un elemento a la vez
            elemento = extremo_tubo.recv()
            print(f"recibido: {elemento}")

        print("recepcion finalizada")
    else:
        print("tuberia vacia")

    extremo_tubo.close()
    print()


def transmisor(extremo_tubo):
    """Tarea para el envio de datos"""
    print("Transmisor listo")
    lista = ["hola", 1.0 , True, 27]
    for l in lista:
        # transmision - un elemento a la vez
        extremo_tubo.send(l)
        print(f"enviado: {l}")

    print("transmision finalizada")
    extremo_tubo.close()
    print()


# subprocesos para gestionar la tuberia
sub_transmisor = Process(
    target=transmisor,
    args=(extremo_receptor,),
    daemon=True,
    )

sub_receptor = Process(
    target=receptor,
    args=(extremo_emisor,),
    daemon=True,
    )

# se carga la tuberia 
sub_transmisor.start()
# lectura de datos atrasada
sleep(0.2)
sub_receptor.start()

# espera al cierre de procesos
sub_transmisor.join()
sub_receptor.join()
print("Finalizado")
```




## Referencias

[Python.org - Módulo `multiprocesing`](https://docs.python.org/es/3/library/multiprocessing.html#multiprocessing.connection.Connection)