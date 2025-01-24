---
tags:
  - time
  - Tiempo
  - Procesos 
  - Hilos
  - Fechas
---


# Tiempo del Sistema


## Módulo `time`

Python dispone de un módulo estándar  
para el manejo temporal 
llamado `time`.

El módulo se importa por su nombre para poder ser usado:

```py title="time - Importación"
import time
```

Por cuestiones de comodidad,
en este tutorial se asume que todos los componentes del módulo
son importados directamente: 

```py title="time - Importar todo"
from time import *
```

## Espera

El módulo incluye una función para introducir *delays* (retardos) 
de manera intencional llamada `sleep()` ("dormir"):


```py title="retardos"
sleep(segundos)    
```

Esta función afecta al *thread* ("hilo") que la invoca,
suspendiendo su ejecución
.
Pasado el tiempo indicado, 
el sistema operativo 
pone el hilo actual en espera para retomar su ejecución.


!!! warning "Tiempos de espera inexactos"

    Debido a la intervención del sistema operativo,
    la ejecución de otros procesos, 
    las prioridades de cada uno,
    etc.,
    el retardo real está sometido a cierto error
    el cual puede alcanzar varios milisegundos.


## Cronometrado

### Tiempo POSIX actual - `time()` y `time_ns()`


El tiempo UNIX,
también llamado tiempo POSIX, 
es el tiempo transcurrido desde el 1 de enero de 1970
hasta el instante presente.

Hay dos funciones que miden este parámetro directamente.
Estas son `time()` y `time_ns()`


```py title="Tiempo POSIX"
tiempo_segundos     = time()       # 'float'
tiempo_nanosegundos = time_ns()    # 'int'
```

Mientras `time()` devuelve un número flotante
que representa el tiempo transcurrido en segundos, 
`time_ns()` devuelve un entero representando el tiempo en nanosegundos. 


!!! example "Medición de tiempo (en segundos)"

    ```py
    from time import time

    inicio = time()

    # ....
    # (rutina)
    # ....

    fin    = time()

    # Intervalo medido - máximo 3 decimales
    print(f"Tiempo transcurrido: {(fin - inicio):.3} segundos.")
    ```

## Tiempo de ejecución

El módulo posee varias funciones 
para medir los tiempos 
que el programa actual
le demanda al CPU para funcionar.

Estas funciones pueden ser tanto 

!!! info "Procesos e hilos"

    Las rutinas más básicas de Python ocupan 
    un solo [proceso](../paralelismo/procesos.md)
    el cual a su vez 
    utiliza un solo [hilo (*thread*)](../paralelismo/hilos.md), 
    a menos que específicamente 
    se ordene la creación de los mismos.

    Sin embargo, 
    los frameworks y bibliotecas,
    al ser utilizados 
    suelen repartir las tareas 
    en múltiples procesos y en múltiples hilos 
    con el fin de mejorar el rendimiento de los programas
    mediante el procesamiento de bloques de código en paralelo.




### Tiempo de CPU - `process_time()` y `process_time_ns()` 

El tiempo de CPU es el tiempo relativo consumido por el actual proceso.
Por ejemplo, 
si el proceso actual consume el 15% del tiempo de ejecución de un núcleo del CPU
entonces el tiempo de CPU será 0.15 segundos.

Se dispone de dos funciones 
para esta medición 
llamadas `process_time()` y `process_time_ns()`:

```py title="Tiempo de CPU"
cpu_segundos     = process_time()      # `float`
cpu_nanosegundos = process_time_ns()   # `int`
```

No se incluye el tiempo de *delay* 
en la medición 
porque `sleep()` libera temporalmente
al CPU de tener que ejecutar el programa actual.

### Tiempos de *thread* - `thread_time()` y `thread_time_ns()`


El tiempo de thread es el tiempo relativo consumido por el actual hilo de código.
Es análogo al tiempo de CPU.

Las funciones disponibles 
para este propósito 
son `thread_time()` y `thread_time_ns()`:

```py title="Tiempo de hilo"
hilo_segundos     = thread_time()       # 'float'
hilo_nanosegundos = thread_time_ns()    # 'int'
```

Estas funciones tampoco miden el tiempo de *sleep*
por los mismos motivos.


## Fechas y Horarios

El módulo `time` permite trabajar con fechas
tanto en formato *string* 
como con formato de estructura de datos.
Para ello implementa la estructura `struct_time`
la cual tiene los siguientes datos y valores:


| Atributo | Valores | Significado |
|---|----|---|
|`tm_year` |`int`| Año |
|`tm_mon` |rango: [1, 12] | Mes
|`tm_mday` | rango: [1, 31] | Dia del mes|
|`tm_hour` | rango: [0, 23] | Hora|
|`tm_min`  |rango: [0, 59] | Minuto|
|`tm_sec` | rango: [0, 61] | Segundo|
|`tm_wday` | rango: [0, 6]; el Lunes es 0| Día de la semana | 
|`tm_yday` |rango: [1, 366]| Día del año|
|`tm_isdst`|0, 1 o -1 | *Daylight Saving Time* (DLS)|
|`tm_zone`| `str` |Abreviacion del nombre de zona|
|`tm_gmtoff` |`int`| offset respecto a UTC (en segundos) |

El **DLS** (*Daylight Saving Time*) es la corrección de horario en base a la las horas de luz del territorio.



### Salida como estructura - `gmtime()` y `localtime()`

Estas funciones 
devuelven una estructura de datos 
llamada `struct_time`
con toda la información de la fecha y hora actual
:

```py  title="fecha y hora - instante actual"
data_tiempo = gmtime()       # UTC
data_tiempo = localtime()    # según hora local del sistema
```

Si se les pasa un número como argumento,
estas funciones asumirán que el argumento es el tiempo POSIX
medido en segundos 
y
devolverán la fecha equivalente
:

```py title="fecha y hora - tiempo POSIX"
tiempo_posix:   float
data_tiempo = gmtime(    tiempo_posix )   # UTC
data_tiempo = localtime( tiempo_posix )   # según hora local del sistema
```


Ambas funciones devuelven una estructura de datos como la siguiente:

``` title="fecha y hora - fecha (estructura)"
time.struct_time(tm_year=2025, tm_mon=1, tm_mday=23, tm_hour=23, tm_min=5, tm_sec=41, tm_wday=3, tm_yday=23, tm_isdst=0)      
```

Estos datos pueden consultarse uno a uno por su nombre:


```py   title="fecha y hora - campos disponibles"
anio = data_tiempo.tm_year
mes  = data_tiempo.tm_mon
dia  = data_tiempo.tm_mday
# ....
```



### Salida como texto - `ctime()` y `asctime()`

Con estas funciones se  obtiene la fecha actual en formato `str`:

```py 
texto_tiempo = ctime()        # según hora local del sistema
texto_tiempo = asctime()      # según hora local del sistema
```

El resultado es la fecha y hora del sistema:

```
'Thu Jan 23 22:24:24 2025'
```

Estas funciones devuelven también 
la fecha y hora del instante indicado como argumento.
`ctime()` requiere el instante definido como número: 


```py 
segundos_posix:  int = 1e6            # tiempo elegido 
texto_tiempo = ctime(segundos_posix)    
```


entonces el resultado es algo como esto:

```
'Mon Jan 12 10:46:40 1970'
```

En cambio,
`asctime()` requiere el instante definido como estructura:

```py
data_tiempo: struct_time          # tiempo elegido  
texto_tiempo = asctime( data_tiempo )   
```


### Salida como POSIX - `mktime()` 


`mktime()` convierte la estructura de entrada 
para devolver el tiempo 
medido
en formato POSIX:

```py
data_tiempo: str_time
tiempo_segundos = mktime(data_tiempo)   
```


### Conversión como string con formato - `strftime()`

`strftime()` permite definir el formato de salida de la fecha que se le indica.
Ejemplo de uso:

```py
tiempo_segundos = gmtime()
string_fecha = strftime("%a, %d %b %Y %H:%M:%S +0000", tiempo_segundos)
```
que devuelve algo como esto:
```
Fri, 24 Jan 2025 04:14:36 +0000
```


Para más información [ver la tabla de opciones]([https://docs.python.org/3/library/time.html#time.strftime) desde la página oficial.


### Conversión de string a estructura - `strptime()`


Esta función es complementaria a `strftime()` 
y permite convertir un string 
con un formato de fecha específico
a una estructura de datos.

```py
data_fecha = strptime("30 Nov 00", "%d %b %y")    
```

Nótese que se necesitan dos argumentos:

- El texto con la fecha y hora pedidos;
- El formato exacto del texto ingresado.








## Referencias



[Documentación oficial - modulo `time`](https://docs.python.org/3/library/time.html)














