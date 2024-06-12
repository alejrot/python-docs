# Sys - Parámetros y funciones del sistema



En este resumen se explican algunas de las funcionalidades del módulo **sys**.

## Importación

El módulo debe ser importado para su uso:

```py  title="Importación"
import sys
```


## Intérprete Python, sistema operativo 

### `platform`
Indica el sistema operativo detectado:

```py title="Identificar plataforma"
plataforma = sys.platform
```

Valores posibles:

| Sistema operativo | valor |
| :---: | :---: |
| Windows | `win32` |
| Windows/Cygwin | `cygwin` |
| Linux | `linux` |
|  AIX | `aix`  |
| macOS | `darwin` |

### `platform.startwith()`

Este submétodo permite confinar código específico para cada plataforma posible:

```py title="Código exclusivo por plataforma"
if sys.platform.startswith('freebsd'):
    # rutina especifica para FreeBSD
elif sys.platform.startswith('linux'):
    # rutina especifica para Linux
elif sys.platform.startswith('aix'):
    # rutina especifica para AIX
```

### `version` , `version_info`

Dan información completa sobre el actual intérprete de Python: versión, fecha, licencia, etc.
```py title="Data de versión"
# info de version de Python 
sys.version         # data en string
sys.version_info    # data en tupla 
```

### `platlibdir`

Devuelve las rutas a las bibliotecas del sistema:
```py title="Ruta a las bibliotecas especificas"
sys.platlibdir  # ruta a las bibliotecas especificas de la plataforma
```

### `path`, `exec_prefix`, `executable`, `prefix`

Devuelven las rutas del entorno Python que se está ejecutando actualmente, el cual puede ser el global del sistema (el predefinido del sistema) o un entorno virtual:
```py
sys.path    # variable de entorno PYTHONPATH  actual (lista de rutas) 
sys.exec_prefix     # directorio de los archivos Python usados 
sys.executable      # ruta del ejecutable Python actual
sys.prefix    # directorio para archivos Python independientes de la plataforma
```

## Hilos
### `thread_info`


```py title="Data de hilos"
# Informacion del hilo actual: tipo hilo, tipo bloqueo, etc
sys.thread_info
```


## Argumentos de entrada

Los argumentos de entrada son los valores que se asignan a continuación del nombre del programa al llamarlo:
```bash title="Ventana de comandos"
py nombre_programa  argumento_1  argumento_2  ...
```
En tanto que los banderines (*flags*) se asignan luego del nombre del programa en la ventana de comandos:

```bash title="Banderines en ventana de comandos"
py nombre_programa -FLAG1 -FLAG2 ...
```

### `argv`

Los argumentos de entrada se leen con el metodo `argv`:

```py title="Lectura de argumentos"
argumentos = sys.argv  # 'argument values'

argumentos          # (lista completa)
argumentos[0]       # (nombre del script Python)
argumentos[1]       # 1º argumento
argumentos[2]       # 2º argumento
```
Todos los argumentos recibidos se leen como *variables string*.

### `flags`


Los flags recibidos se leen con el objeto de solo lectura `flags`:
```py title="Lectura de banderines (todos)"
sys.flags           # diccionario con todos los flags detectables
```
Dicho objeto tiene un flag específico para cada opción de entrada posible:
```py title="Lectura de banderines específicos"
# banderines especificos 
sys.flags.debug     # sólo flag de debugueo
sys.flags.inspect   # sólo flag de inspeccion
sys.flags.optimize  # sólo flag de optimizacion
# (etc)
```

**REVISAR --> flags insensibles**

## Uso de memoria


### `getsizeof()`

La función `getsizeof()` mide la longitud en bytes del objeto que se le asigne como argumento, sean variables, datos, etc:

```py  title="Bytes de datos"
texto = "soy un texto"
peso_bytes = sys.getsizeof(texto) 
```

### `getallocatedblocks()`

`getallocatedblocks()` indica cuántos bloques de memoria RAM le fueron asignados al programa actual por parte del intérprete.
```py title="Bloques de RAM"
# bloques de memoria asignados al programa actual
print(sys.getallocatedblocks())
```

## Salida del programa

### `exit()`

La función `exit()` ordena el cierre del proceso actual. 
```py title="Cierre de proceso"
sys.exit() 
```
Puede asignarse un número entero como retorno para comunicarle a los programas externos. Por ejemplo: el `-1` suele ser indicativo de error.
```py title="Cierre de programa con valor de retorno" 
retorno: int = -1       # uso  clasico: -1 -> error del programa
sys.exit([retorno]) 
```
Para funcionar correctamente el llamado debe hacerse desde el hilo principal del proceso actual. Esto es pertinente cuando se divide la rutina actual en varios hilos o *threads* para la ejecución paralela del código.

### `is_finalizing()`

La función `is_finalizing()` verifica si el programa ya se está cerrando.

```py title="Verificación de cierre"
cerrando = sys.is_finalizing()  
```

## Hooks, trace , profile

**PENDIENTE**


##  Referencias

[Documentación oficial](https://docs.python.org/es/3.10/library/sys.html#sys.setrecursionlimit)