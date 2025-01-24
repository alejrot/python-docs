


# Modulo Logging - Informacion de Errores

Los logs o reportes funcionan como una alternativa superadora al uso de la función `print()` para dar información acerca del funcionamiento del sistema, permitiendo registrar valores de parámetros, registrar fallos de programa, fecha y hora de eventos, etc. creando mensajes con jerarquías asignables. También habilita la creación de archivos de logs, envío de reportes al sistema operativo, etc.


## Importación

```py title="Importación del módulo"
import logging
```

## Configuración de logs

Los reportes deben configurarse antes de su uso. Para ello se recurre la función `basicConfig()`. 

```py title="Configuración de reportes - A consola" hl_lines="1-4"
logging.basicConfig(
    level=logging.INFO, # mínimo nivel de log a publicar
    format="%(asctime)s - %(levelname)s - %(message)s", #info incorporada
    )
``` 

`level` es el argumento que indica el mínimo nivel de reporte a presentar de ahí en adelante, en tanto que `format` define qué información incluir en el reporte: 

- `%(asctime)s`     : fecha y hora local del reporte
- `%(levelname)s`   : nivel de error reportado
- `%(message)s`     : reporte explicativo del desarrollador (ver más adelante)


Se presupone la salida de los reportes por terminal. Esto puede reemplazarse indicando parámetros de archivo de salida:

```py title="Configuración de reportes - A archivo" hl_lines="4-8"
logging.basicConfig(
    level=logging.INFO, # mínimo nivel de log a publicar
    format="{asctime} - {levelname} - {message}",
    filename="app.log", # nombre archivo
    encoding="utf-8",   # codificacion
    filemode="a",       # modo agregado
    style="{",
    datefmt="%Y-%m-%d %H:%M",
    )
``` 


!!! warning "Orden de configuración"

    Si hay varios llamados sucesivos a `basicConfig()` entonces el primer llamado es el que define el  comportamiento del logger.

## Opciones de salida - manejadores


Hay un parámetro adicional que permite configurar múltiples salidas en simultáneo llamado `handlers`, al cual se le asignan todos los manejadores de interés:

```py title="Configuración de reportes - Multiples salidas" hl_lines="4 6 8-14"
logging.basicConfig(
    level=logging.INFO, # mínimo nivel de log a publicar
    format="%(asctime)s - %(levelname)s - %(message)s", #info incorporada
    handlers=[
         # salida por consola
        logging.StreamHandler(), 
        # salida por archivo
        logging.FileHandler(
            filename="reporte.log",
            mode="a",
            encoding="utf-8",
            delay=True,
            ),  
        ],
    
    )
``` 
El módulo `logging` ofrece para manejar reportes por consola la función `StreamHandler()`, en tanto que para manejar archivos ofrece `FileHandler()`. Hay otras funciones para manejar reportes mediante sockets (`SocketHandler` y `DatagramHandler` ), mediante colas (`QueueHandler`), etc.

Más sobre los handlers disponibles y sus opciones: [documentacion oficial](https://docs.python.org/3.12/library/logging.handlers.html) 



## Niveles de logs

Los niveles de reportes permiten clasificar los mensajes de reportes en base a una jerarquía de eventos, permitiendo filtrar los reportes en base al objetivo del reporte. Por ejemplo, para desarrollo es útil crear un reporte completo donde se incorporen mensajes informativos que releven incluso el buen funcionamiento del programa, en tanto que para el uso por el usuario final conviene reportar solamente los fallos ya producidos y posiblemente también las advertencias lanzadas preventivamente.

Los niveles de reportes implementados son los siguientes:


|opción| valor numérico| descripción|
|---|---|----|
|NOTSET|0 | (Se consulta a loggers previos para definir el comportamiento)|
|DEBUG|10|Información detallada, normalmente usada para debug.|
|INFO |20|Confirmación de funcionamiento esperado.|
|WARNING|30|El software funciona aún, pero puede haber problemas a futuro.|
|ERROR|40|Problema serio que anula una funcionalidad del software.|
|CRITICAL|50|Error serio que impide al software continuar funcionando.|



## Creación de logs

Cada nivel de reporte tiene su propia función emisora, al que se le puede asignar un mensaje explicativo. Uso básico: 

```py title="Creación de reportes" 
logging.debug("Texto de DEBUG")
logging.info("Texto de INFO")
logging.warning("Texto de WARNING")
logging.error("Texto de ERROR")
logging.critical("Texto de CRITICAL")
```

Cabe resaltarse que los logs se emiten al llamar a la función emisora elegida.

```py title="Creación de reportes" 
retorno = funcion()
if retorno == None:
    logging.info(f"Sin valor de retorno - OK")
else:
    logging.error(f"Tipo de dato recibido: {type(retorno)}")
```


## Uso aplicado: decoradores de logging


Una forma cómoda de aplicar el logging a las funciones es mediante el uso de decoradores, lo cual permite usar la misma rutina de logging a múltiples funciones.
[Más sobre decoradores](../funciones/decoradores.md)


!!! tip "TIP Nº1: Decorador logger para excepciones"
    Este primer ejemplo usa un decorador simple, dentro del cual se hace manejo de excepciones mediante `try` - `except`.

    ```py title="Definición" hl_lines="3-7"
    def logger_excepcion(funcion_entrada):
        def funcion_envolvente(*args, **kwargs):
            try:
                retorno = funcion_entrada(*args, **kwargs)
                logging.info(f"Funcion '{funcion_entrada.__name__}' - Sin excepciones producidas")
            except Exception as ex:
                logging.error(f"Funcion '{funcion_entrada.__name__}' - Excepción: '{type(ex).__name__}'")
        return funcion_envolvente
    ```

    ```py title="Uso" hl_lines="1 8"
    @logger_excepcion
    def dividir(a, b):
        return(a / b)


    dividir( 4, 7)
    dividir( 7, 4)
    dividir( 1, 0.5 )
    dividir( 1, 0)      # "ERROR - Funcion 'dividir' - Excepción: 'ZeroDivisionError'"
    ```


!!! tip "TIP Nº2: Decorador logger para verificar tipos de retorno"
    Este segundo ejemplo usa un decorador con argumentos, de manera de poder especificar el tipo de retorno deseado para cada función.


    ```py title="Definición" hl_lines="4-8"
    def logger_retorno(tipo:type=None):
        def _logger_retorno(funcion_entrada):
            def funcion_envolvente(*args, **kwargs):
                retorno = funcion_entrada(*args, **kwargs)
                if type(retorno) == tipo:
                    logging.info(f"Funcion '{funcion_entrada.__name__}' - Sin problemas de retorno")
                else:
                    logging.warning(f"Funcion '{funcion_entrada.__name__}' - Tipo de retorno incorrecto: '{type(retorno).__name__}'")
            return funcion_envolvente
        return _logger_retorno
    ```

    ```py title="Uso" hl_lines="1 8 9"
    @logger_retorno(int)
    def suma(x, y):
        return x + y


    suma(1, 1)
    suma(3,2)
    suma("hola", "mundo")   # "WARNING - Funcion 'suma - Tipo de retorno incorrecto: 'str'"
    suma(9.2 , 7)           # "WARNING - Funcion 'suma - Tipo de retorno incorrecto: 'float'"
    ```



## Referencias


[Documentacion oficial](https://docs.python.org/3.12/library/logging.html)