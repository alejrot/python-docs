---
tags:
  - calendar
  - Tiempo
  - Fechas
  - Clases
---


# Calendario

El módulo `calendar`
está dedicado para dibujar calendarios 
en formato de texto simple o en formato HTML.

## Ejecución como módulo

Este módulo se puede ejecutar desde la *shell* para renderizar calendarios 
en la terminal.

### Calendario completo

El calendario 
requiere como argumento obligatorio 
el número del año pedido:

```bash title="Calendario - Año"
py -m calendar  nro_anio   
```

Por ejemplo el calendario del año 2025 se obtiene así:

```bash title="Calendario - Año 2025"
py -m calendar  2025   
```

El resultado es un calendario en idioma inglés 
y el formato predefinido del módulo:

``` 
      January                      February                      March
Mo Tu We Th Fr Sa Su         Mo Tu We Th Fr Sa Su         Mo Tu We Th Fr Sa Su
       1  2  3  4  5                         1  2                         1  2
 6  7  8  9 10 11 12          3  4  5  6  7  8  9          3  4  5  6  7  8  9
13 14 15 16 17 18 19         10 11 12 13 14 15 16         10 11 12 13 14 15 16
20 21 22 23 24 25 26         17 18 19 20 21 22 23         17 18 19 20 21 22 23
27 28 29 30 31               24 25 26 27 28               24 25 26 27 28 29 30
                                                          31
.....
```

### Opciones 

Las opciones de configuración disponibles son las siguientes.

|Opción | Valor| Significado|
|:---:|:---|:---|
|`-e`, `--encoding`|ejemplo: `utf8`| codificación de salida|
|`-L`, `--locale`|`en_us`, `es_ar`, etc| lenguaje y región (requiere definir codificación) |
|`-t`, `--type`|`text` o `html`| formato de salida: texto simple o HTML |
|`-c`, `--css`| Ruta o URL | hoja de estilos CSS (sólo para HTML)|
|`-w`, `--width`|  entero     | Nº de espacios por columna de día semanal (default: `2`) |
|`-s`, `--spacing`| entero | Nº de espacios entre meses (default: `6`)|
|`-l`, `--lines`| entero   | Nº de filas por semana (default: `1`)|
|`-m`, `--months`|entero | número de meses por fila (default: `3`)|
|`-f`, `--first-weekday`|rango `[0, 6]`| primer columna (default: lunes)|

Por ejemplo, 
para renderizar 
el calendario del 2025
en español de España
y comenzar por los domingos se hace:

```bash title="Calendario - Año 2025 (Español de España, comienza en domingo)"
py -m calendar 2025  -e utf8  -L es_es  -f 6
```
Así queda:

```
       enero                    febrero                    marzo
do lu ma mi ju vi sá      do lu ma mi ju vi sá      do lu ma mi ju vi sá
          1  2  3  4                         1                         1
 5  6  7  8  9 10 11       2  3  4  5  6  7  8       2  3  4  5  6  7  8
12 13 14 15 16 17 18       9 10 11 12 13 14 15       9 10 11 12 13 14 15
19 20 21 22 23 24 25      16 17 18 19 20 21 22      16 17 18 19 20 21 22
26 27 28 29 30 31         23 24 25 26 27 28         23 24 25 26 27 28 29
                                                    30 31
.....
```


### Calendario - mes específico

Especificando un número de mes 
se renderiza un único mes del calendario: 

```bash title="Calendario - Año y mes"
py -m calendar  nro_anio  nro_mes  
```

donde el mes 1 es enero.
Por ejemplo, 
para renderizar el mes de marzo del 2025 
se escribe:

```bash title="Calendario - Marzo 2025 (default)"
py -m calendar  2025 3 
```

Así queda:

```
     March 2025
Mo Tu We Th Fr Sa Su
                1  2
 3  4  5  6  7  8  9
10 11 12 13 14 15 16
17 18 19 20 21 22 23
24 25 26 27 28 29 30
31
```

La mayoría de las opciones están habilitadas en este caso. 
Por ejemplo, 
para renderizar 
el mes de marzo 
en español de España
y comenzar por los domingos se hace:

```bash title="Calendario - Marzo 2025 (español de España, comienza en domingo)"
py -m calendar 2025 3  -e utf8  -L es_es  -f 6
```
quedando así:

```
     marzo 2025
do lu ma mi ju vi sá
                   1
 2  3  4  5  6  7  8
 9 10 11 12 13 14 15
16 17 18 19 20 21 22
23 24 25 26 27 28 29
30 31
```

Sin embargo, esta opción no permite renderizar como HTML.


## Uso en programas

### Importación

Para su uso, el módulo requiere importación.
```py title="calendar - Importación"
import calendar 
```

### Clases 

`calendar` implementa varias clases para trabajar con calendarios:

- `Calendar` y `LocaleCalendar` para crear estructuras de datos;
- `TextCalendar` y `LocaleTextCalendar` para renderizar en formato de texto simple;
- `HTMLCalendar` y `LocaleHTMLCalendar` para renderizar en formato HTML.

donde las clases `Locale` incluyen la opción del cambio de idioma.



### Texto simple

Para crear calendarios 
en formato texto se crea un objeto de las clases dedicadas:

<div class="grid cards" markdown>

```py title="Clases de texto - Inglés"
# default: inglés
clase_calendario = calendar.TextCalendar(firstweekday=6)                      
```

```py title="Clases de texto - Lengua local"
# lengua local: 'locale'
clase_calendario = calendar.LocaleTextCalendar(firstweekday=6, locale=None)   
```

</div>

en este ejemplo se comenzó por el domingo.


#### Calendario completo

El renderizado del calendario anual se realiza con el método `formatyear`:

```py title="Renderizado - Calendario completo"
calendario_anio = clase_calendario.formatyear(anio, w=2 , l=1, c=6, m=3)  
```

Las opciones son similares
a las del uso por consola:

|Argumento|Significado|
|:---:|:---|
|`w`|*width*: ancho de columnas|
|`m`|*months*: número de meses por fila|
|`l`|*lines*: renglones por semana|
|`c`|*columns*: espacios entre columnas de meses|



#### Calendario - mes específico

El renderizado de un mes específico se realiza con el método `formatmonth`:

```py title="Renderizado - Mes específico"
calendario_mes  = clase_calendario.formatmonth(anio, mes, w=2 , l=1) 
```

Por ejemplo,
para renderizar un mes con ancho de columnas de 9 espacios:

```py title="Ejemplo - Septiembre de 2025 (ancho custom)"
calendario_mes = calendario.formatmonth(2025, 9, w=9 , l=1)  
```
da lugar a este resultado:

```
                           septiembre 2025
 domingo    lunes     martes  miércoles   jueves   viernes    sábado
               1         2         3         4         5         6
     7         8         9        10        11        12        13
    14        15        16        17        18        19        20
    21        22        23        24        25        26        27
    28        29        30
```


### Otros formatos

Las clases para crear estructuras y para crear HTMLs 
son similares a las clases para texto 
pero con algunas variantes en las opciones de configuración.
Ver la documentación oficial para más detalles.



## Referencias

[Documentación oficial - módulo `caledar`](https://docs.python.org/3/library/calendar.html#cmdoption-calendar-encoding)