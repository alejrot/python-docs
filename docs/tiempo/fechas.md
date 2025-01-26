---
tags:
  - datetime
  - Tiempo
  - Fechas
  - Clases
---


# Fechas y Horario


## Módulo `datetime`

El módulo **datetime** está dedicado al trabajo con fechas y horarios. Para usarlo se necesita importarlo.

```python title="'datetime' - Importación"
import datetime
```
Al igual que en otros módulos se puede importar unicamente los elementos necesarios del mismo.

En este tutorial se asume que se importan todos los elementos internos:

```python title="'datetime' - Importar todo"
from datetime import datetime
```

!!! warning "datetime vs time"

    Los módulos `datetime` y `time`
    tienen elementos que comparten nombre
    pero que no son compatibles entre síu.
    En caso de importar elementos de ambos módulos
    es mejor importarlos con su nombre de módulo o un alias
    para evitar conflictos inesperados.


## Lectura de fechas

La clase `datetime`
maneja fechas y horarios
en un único elemento

### Fecha y hora actual 

Este elemento dispone del método `now()` para consultar fecha y hora del sistema:

```python title="clase 'datetime' - fecha actual"
ahora = datetime.now()  #lectura fecha y hora actual (hora local)
print(ahora)
```
El resultado es un objeto de tipo `datetime.datetime` cuya data es la siguiente:

``` title="clase 'datetime' - formato de salida"
datetime.datetime(2023, 1, 1, 3, 6, 9, 300411)
```

El objeto incluye variables internas (*"atributos"*)
con los parámetros temporales de la fecha y hora:
año, mes, día,
hora, minuto, segundo y microsegundo.
Éstos son de sólo lectura 
y pueden ser consultados por su nombre:

```python title="clase 'datetime' - atributos internos"
print(ahora.year)
print(ahora.month)
print(ahora.day)
print(ahora.hour)
print(ahora.minute)
print(ahora.second)
# (no hay campo para los milisegundos)
print(ahora.microsecond)
```

### Métodos de lectura 

La clase `datetime`
posee varios métodos de lectura para extraer fecha, 
hora ó ambas juntas. 
Estos métodos son `timestamp()`, `date()` y `time()`:

```py title="Métodos de lectura"
# Métodos de lectura disponibles
fecha_hora = ahora.timestamp()    # Fecha y hora en formato POSIX
fecha = ahora.date()         # Sólo fecha
hora  = ahora.time()         # Sólo hora
```
El tiempo POSIX, tambien llamado tiempo UNIX, es el tiempo en segundos transcurrido desde el 1º de enero de 1970.

### Asignacion de fechas

Si se necesita crear un objeto con fecha y hora particular
hay que cargarlos en la clase `datetime`
para crear un objeto nuevo.
Los argumentos de esta función
son los parámetros temporales en orden:
año, mes , día, hora , minuto , segundo, microsegundo:

```python title="clase 'datetime' - Asignación de fechas"
# conversion de fechas
primer_dia = datetime(2023,1,1)         # obligatorio: año, mes, dia
primer_dia = datetime(2023,1,1,3,6,9)   # opcionales: hora, minuto, segundo, etc    
```
Los parámetros de la hora son opcionales, en tanto que los parámetros de la fecha son obligatorios.

### Intervalos de tiempo

Con los objetos `datetime`
se pueden calcular intervalos de tiempo
con una simple resta entre objetos.
En el ejemplo:
tiempo transcurrido desde el último 1 de enero.

```python title="Intervalos de tiempo - cálculo"
# tiempo actual
ahora = datetime.now()
# fecha referencia
primer_dia_anio = datetime(ahora.year,1,1)

# Tiempo pasado desde el 1 de enero
diferencia_temporal = ahora - primer_dia_anio
```

El resultado es algo como el siguiente:

``` title="Intervalos de tiempo - resultado"
datetime.timedelta(days=23, seconds=18618, microseconds=885041)
```



### Fecha

La clase `date()` permite manejar fechas prefijadas:

```python   title="Fecha prefijada"
from datetime import date

fecha = date(2023,12,25)  # fecha especificada: Navidad

anio = fecha.year 
mes  = fecha.month 
dia  = fecha.day 
```

Con esta clase
se puede leer también
la hora del sistema directamente
con ayuda del método `today()`:

```python title="Fecha actual"
from datetime import date

fecha_actual = date.today()      # fecha de hoy
```

### Horario

La clase `time()`
sirve para trabajar con horarios prefijados:

```python  title="Horario prefijado"
from datetime import time

hora_actual = time(17, 10, 6)       # asignacion manual

hora    = hora_actual.hour
minuto  = hora_actual.minute
segundo = hora_actual.second
# hora_actual.microsecond      # no se usa
```

Esta clase no es capaz de leer la hora del sistema directamente,
sino que lo hace a través del objeto `datetime` y su método `now()`:

```python title="Horario actual"
from datetime import datetime

ahora = datetime.now()  # lectura fecha y hora actual (hora local)

horario_actual = ahora.time()         
```

### `timedelta`

La clase `timedelta()` 
crea objetos que permiten calcular tiempos 
entre fechas especificadas como argumento:

```python  title="timedelta - resultado"
from datetime import timedelta

# tiempos
inicio = timedelta(0, 0, 0)
fin    = timedelta(0, 2, 1, 7)

# diferencia temporal
diferencia = fin - inicio     
```

El valor de la diferencia se ve así:

```  title="timedelta - resultado"
datetime.timedelta(seconds=2, microseconds=7001)
```

!!! note "Argumentos no ordenados"

    `timedelta` **no tiene ordenados** los argumentos. 
    Para imponerlos 
    se puede asignar cada parámetro 
    con su plabra reservada, 
    las cuales recorren el rango de los microsegundos hasta las semanas:

    ```py
    instante = timedelta(
        weeks        = 1,
        days         = 3, 
        hours        = 2, 
        minutes      = 14, 
        seconds      = 7, 
        milliseconds = 900,
        microseconds = 815
        )
    ```


## Referencias

[Documentación oficial - módulo `datetime`](https://docs.python.org/3/library/datetime.html)