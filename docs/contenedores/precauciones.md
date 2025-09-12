---
date:
    created: 2025-07-01
    updated: 2025-08-26
---

# Precauciones previas y tips

Antes de intentar el despliegue 
de aplicaciones Python 
en contenedores
es conveniente verificar
algunos pasos previos,
con el fin de minimizar errores posteriores.

<!-- 
## Asegurar funcionamiento

- El programa de Python debe ser capaz de funcionar correctamente
con el intérprete global de Python
o desde un entorno virtual.
 -->

## Agrupar importaciones

Si en el proyecto
hay archivos o directorios de módulos,
configuraciones, traducciones, etc.
es conveniente que estos archivos 
estén agrupados en subdirectorios de la carpeta del proyecto,
con el fin de ser copiados fácilmente
adentro del contenedor
en las rutas correctas.

<!-- 
estos deben ser importados correctamente
por la rutina principal
cuando el contenedor esté funcionando.
 -->

## Comandos ejecutables

Hay que atención al comando utilizado
para la ejecución de la rutina
y también a sus argumentos posicionales y opciones de entrada.
De esta manera el comando podrá ser adaptado
al archivo Dockerfile. 

En este sentido, tener en cuenta que el alias `py` para el intérprete de Python normalmente no está disponible en el contenedor.


<!-- 
Todo esto prevendrá errores y confusiones
a la hora de desplegar en contenedores.
 -->

## Versiones de dependencias

Si el programa requiere paquetes adicionales
entonces es importante fijar las versiones usadas
indicando sus etiquetas de versión.
Esto prevendrá que el código se "rompa"
si los paquetes usados son actualizados descontroladamente.

Por ejemplo, si se usa
PIP para gestionar los paquetes 
el comando `pip freeze` sirve asegurar las versiones
de todos los paquetes en archivo TXT.

En el caso de Poetry, ese mismo control fino se puede conseguir
con el archivo LOCK.
Otra opción es el uso del archivo TOML que define el versionado de una manera normalmente más laxa.


## Versiones de Python

No todas las versiones de Python
son capaces de correr las rutinas debidos
a los cambios de sintaxis, prestaciones nuevas y prestaciones obsoletas, etc.
Por este motivo debe elegirse como base una imagen de Python
cuya versión instalada del intérprete
pueda ejecutar el código fuente correctamente.

## Compatibilidad con la imagen

Las dependencias usadas deben ser capaces de ser usadas
en el sistema operativo de la imagen.

Por ejemplo: el paquete `psycopg2`,
que es necesario para interactuar con bases de datos PostgreSQL,
sólo funciona el Windows.
Su equivalente para sistemas GNU/Linux
es el paquete `psycopg2-binary`
y es ésta la versión que funcionará
en las imágenes de Python más habituales.


## print vs logging

En los contenedores la salida de texto por consola
a menudo no está implementada,
por este motivo escribir texto
mediante la función `print()` es problemático.
La alternativa es la lectura de texto desde la ventana de *logs*,
la cual es de uso estándar en los contenedores.
Para ello es necesario el uso de las funciones de *logging*,
las cuales requieren importación y configuración para su uso:

```py title="Logging - configuracion previa"
import logging

# uso de la consola de logs
logging.basicConfig(
    level=logging.INFO, # mínimo nivel de log a publicar
    format="%(asctime)s - %(levelname)s - %(message)s", #info incorporada
    )
```

Los *logs* se pueden guardar en archivo 
al tiempo que se muestran en consola.
La configuración se realiza fácilmente
con ayuda de las funciones
`StreamHandler()` y`FileHandler()` del módulo `logging`
tal como se muestra a continuación:


``` py title="logging en archivo" hl_lines="10-15"
import logging

logging.basicConfig(
    level=logging.INFO, # mínimo nivel de log a publicar
    format="%(asctime)s - %(levelname)s - %(message)s", #info incorporada
    handlers=[
        # salida por consola
        logging.StreamHandler(), 
        # salida por archivo
        logging.FileHandler(
            filename=ruta_archivo,
            mode="a",             # agregado ('append')
            encoding="utf-8",
            delay=True,
            ),
        ],
    )
```

Hay varias funciones para crear los mensajes de *log*,
las cuales tienen distintos niveles de jerarquía:

```py title="Logging - funciones de salida"
logging.debug("Texto de DEBUG")         # mínima jerarquía
logging.info("Texto de INFO")
logging.warning("Texto de WARNING")
logging.error("Texto de ERROR")
logging.critical("Texto de CRITICAL")   # máxima jerarquía
```

Las llamadas a funciones de *logging*
que no cumplan la jerarquía mínima configuradas
serán ignoradas durante la ejecución.



## f-strings vs lazy format

Es prudente evitar los *f-strings*,
porque si el tipo de datos de entrada
del string
es erróneo
se puede producir una excepción
que encubrirá la información del reporte original.

Su reemplazo son los strings con *lazy format*.

Por ejemplo, la línea:

```py title="formatted-string - entero, 4 espacios"
logging.info(f"valor: {entero:4}")
``` 

se convierte en:

```py title="lazy format - entero, 4 espacios"
logging.info("valor: %4i", entero)
``` 

<!-- 
    Con esto se busca prevenir posibles excepciones inesperadas
    debidos a un error de tipos en el *formatted string*,
    las que podrían enmascarar las excepciones originales.

 -->

Más información sobre el logging: [módulo logging](../modulos/logging.md)

<!-- 
## Ejemplo: demo

### Rutina demo


Supóngase por ejemplo
una rutina llamamda `contar.py` que cuenta hasta 10
esperando un segundo entre cuentas y entonces cierra.


```py
from time import sleep
import sys


# salida por consola
try:
    # el numero maximo a contar se asigna como argumento
    n = int(sys.argv[1])
    print(f"Contando hasta {n}")

except Exception:
    # valor máximo por default en caso de error
    print("Argumento de entrada faltante o incorrecto (debe ser un entero)")
    n = 10
    print(f"Contando hasta {n} (valor default)")

finally:
    # el contador se incrementa cada 1 segundo
    i = 0
    while i <= n:
        print(f"i: {i:4}")
        sleep(1)
        i += 1
``` 




### Ejecución

El programa se ejecuta llamando al intérprete de Python
e indicándole el nombre del archivo con la rutina,
que en este ejemplo se llama `contar.py`: 

``` bash
python contar.py
```

La cuenta máxima puede ser alterado mediante un argumento posicional,
el cual debe ser un número:

``` bash
python contar.py  5
```

Si hay más argumentos u opciones entonces éstos se ignoran.



### Rutina adaptada

Se implementa el *logging*
y el *lazy formatting*
en la rutina.

Este es el resultado:

```py
from time import sleep
import sys
import logging

# uso de la consola de logs
logging.basicConfig(
    level=logging.INFO, # mínimo nivel de log a publicar
    format="%(asctime)s - %(levelname)s - %(message)s", #info incorporada
    )

try:
    # el numero maximo a contar se asigna como argumento
    n = int(sys.argv[1])
    logging.info("Contando hasta %i", n)

except Exception:
    # valor máximo por default en caso de error
    logging.warning("Argumento de entrada faltante o incorrecto (debe ser un entero)")
    n = 10
    logging.warning("Contando hasta %i (valor default)", n)

finally:
    # el contador se incrementa cada 1 segundo
    i = 0
    while i <= n:
        logging.info("i: %4i",i)
        sleep(1)
        i += 1
``` 
 -->
