# Adaptaciones y precauciones previas


## Asegurar funcionamiento

Antes de intentar el despliegue en contenedores
es conveniente verificar
algunos pasos previos,
con el fin de prevenir errores posteriores:

- El programa de Python debe ser capaz de funcionar correctamente
con el intérprete global de Python
o desde un entorno virtual.
 - Si hay archivos o directorios de módulos,
configuraciones, traducciones, etc.
estos deben ser importados correctamente
por la rutina principal.
Es conveniente que estos archivos 
sean aledaños a al rutina principal
o estén ubicados en subdirectorios de la carpeta del proyecto,
con el fin de ser accedidos o copiados fácilmente.
- Prestar atención al comando utilizado
para la ejecución de la rutina
y también a sus argumentos posicionales y opciones de entrada.
En este sentido, tener en cuenta que el alias `py` para el intérprete de Python normalmente **no está disponible** en el contenedor.

Todo esto prevendrá errores y confusiones
a la hora de desplegar en contenedores.


## Versiones de dependencias

Si el programa requiere paquetes adicionales
entonces es importante fijar las versiones usadas
indicando sus etiquetas de versión,
por ejemplo mediante el comando `pip freeze`. 
Esto prevendrá que el código se "rompa"
si los paquetes usados son actualizados descontroladamente.

Asimismo no todas las versiones de Python
son capaces de correr las rutinas debidos
a los cambios de sintaxis, prestaciones nuevas u obsoletas, etc.
Por este motivo debe elegirse como base una imagen de Python
cuya versión instalada del intérprete pueda ejecutar el código correctamente.

Por último,
las dependencias usadas deben ser capaces de ser usadas
en el sistema operativo de la imagen.
Por ejemplo: el paquete `psycopg2`,
que es necesario para interactuar con bases de datos PostgreSQL,
sólo funciona el Windows.
Su equivalente para sistemas GNU/Linux
es el paquete `psycopg2-binary`.


## Uso de logging

En los contenedores la salida de texto por consola
a menudo no está implementada,
por este motivo excribir texto
mediante la función `print()` es problemática.
La alternativa es la lectura de texto desde la ventana de *logs*,
la cual es de uso estándar en los contenedores.
Para ello es necesario el uso de las funciones de *logging*,
las cuales requieren importación y configuración para su uso:

```py
import logging

# uso de la consola de logs
logging.basicConfig(
    level=logging.INFO, # mínimo nivel de log a publicar
    format="%(asctime)s - %(levelname)s - %(message)s", #info incorporada
    )
```

Hay varias funciones para crear los mensajes de *log*,
las cuales tienen distintos niveles de jerarquía:

```py
logging.debug("Texto de DEBUG")         # mínima jerarquía
logging.info("Texto de INFO")
logging.warning("Texto de WARNING")
logging.error("Texto de ERROR")
logging.critical("Texto de CRITICAL")   # máxima jerarquía
```

Es prudente evitar los *f-strings*, reemplazándolos por los *lazy format*.
Por ejemplo, la línea:

```py title="formatted-string - entero, 4 espacios"
print(f"valor: {entero:4}")
``` 

se convierte en:

```py title="lazy format - entero, 4 espacios"
logging.info("valor: %4i", entero)
``` 

Con esto se busca prevenir posibles excepciones inesperadas
debidos a un error de tipos en el formatted string,
las que podrían enmascarar otras excepciones.

Más información sobre el logging: [módulo logging](../modulos/logging.md)

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

