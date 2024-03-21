<a name="top"></a>

## [Volver](../Python.md#fechas-y-horario)


# Fechas y Horario

El módulo **datetime** está dedicado al trabajo con fechas y horarios. Para usarlo se necesita importarlo.

```python
import datetime
```
Al igual que en otros módulos se puede importar unicamente los elementos necesarios del mismo.

## Datetime

### Lectura de fechas


El objeto ***datetime*** maneja fechas y horarios en un único objeto. 

```python
from datetime import datetime
```

Este objeto dispone del método ***now()*** para consultar fecha y hora del sistema:

```python
ahora = datetime.now()  #lectura fecha y hora actual (hora local)
print(ahora)
```

El objeto incluye variables internas (*"atributos"*) con los parámetros temporales de la fecha y hora. Éstos son de solo lectura. 

```python
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

El objeto *datetime* posee varios métodos de lectura para extraer fecha, hora ó ambas juntas. Estos métodos son ***timestamp()***, ***date()*** y ***time()***:

```python
# Métodos de lectura disponibles
print(ahora.timestamp() )   # Fecha y hora en formato POSIX
print(ahora.date())         # Fecha
print(ahora.time())         # Hora
```
El tiempo POSIX, tambien llamado tiempo UNIX, es el tiempo en segundos transcurrido desde el 1º de enero de 1970.

### Asignacion de fechas

Si se necesita crear un objeto con fecha y hora particular  hay que cargarlos en la ***función datetime()*** para crear un objeto nuevo. Los argumentos de esta función  son los parámetros temporales en orden: año, mes , día, hora , minuto , segundo, microsegundo: 

```python
# conversion de fechas
primer_dia = datetime(2023,1,1)         #obligatorio: año, mes, dia
primer_dia = datetime(2023,1,1,3,6,9)   # opcionales: hora, minuto, segundo, etc    
print(primer_dia)
```
Los parámetros de la hora son opcionales, en tanto que los parámetros de la fecha son obligatorios.

### Intervalos de tiempo

Con los objetos *datetime* se pueden calcular **intervalos de tiempo** con una simple resta entre objetos. En el ejemplo: tiempo transcurrido desde el último 1 de enero.

```python
ahora = datetime.now()
primer_dia_anio = datetime(ahora.year,1,1)
# Tiempo pasado desde el 1 de enero
diferencia_temporal = ahora - primer_dia_anio
print(diferencia_temporal)
```


## date()

La función **date()** permite manejar fechas prefijadas:

```python
from datetime import date

fecha_actual = date(2023,12,25)  # fecha especificada: Navidad

print(fecha_actual )
print(fecha_actual.year )
print(fecha_actual.month )
print(fecha_actual.day )
```

Con esta función se puede leer también  la hora del sistema directamente con ayuda del método ***today()***:

```python
from datetime import date

fecha_actual = date.today()      # fecha de hoy

print(fecha_actual )
```

## time()

La función **time()** sirve para trabajar con horarios prefijados: 

```python
from datetime import time

hora_actual = time(17, 10, 6)       # asignacion manual

print(hora_actual)
print(hora_actual.hour)
print(hora_actual.minute)
print(hora_actual.second)
# print(hora_actual.microsecond)      # no se usa
```
Esta función no es capaz de leer la hora del sistema directamente, sino que lo hace a través del objeto *datetime()* y su método ***now()***:

```python
from datetime import datetime

ahora = datetime.now()  #lectura fecha y hora actual (hora local)

print(ahora.time())         # Hora
```

## timedelta()

La función **timedelta()** crea objetos que permiten calcular tiempos entre fechas especificadas como argumento.

```python
from datetime import timedelta
#tiempos
inicio = timedelta(0, 0, 0)
fin    = timedelta(0, 2, 1, 7)
# diferencia temporal
print(fin - inicio)     
```
**Importante:** Esta función **no tiene ordenados** los argumentos. Para imponerlos se pueden asignar cada parámetro con su plabra reservada , las cuales recorren el rango de los microsegundos hasta las semanas:
```python
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



----
----
----

## [Inicio](#fechas-y-horario) 

## [Volver](../Python.md#fechas-y-horario)