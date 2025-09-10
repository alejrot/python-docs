

# Expresiones Regulares (RegEx) - Modulo RE

## Modulo re

Python tiene un módulo dedicado para detectar y trabajar con secuencias llamado **re**. Este módulo debe importarse para su uso:

```python
import re
```

## Funciones 

El modulo **re** incluye múltiples funciones para trabajar con la detección de patrones, las cuales se explican a continuación. Estas funciones aceptan tanto el uso de secuencias fijas como de patrones regulares.

### Sintaxis y opciones

La mayoría de las funciones del módulo tienen el siguiente formato:
```python
<retorno> = re.<funcion>(<patron>, <texto>, <opcion>)
```
El pat


La opción de entrada agrega modificaciones a la detección del patrón.
Su indicación no es obligatoria y puede tomar varios valores predefinidos por el módulo.
Por ejemplo, la opción `re.I` (*re.IGNORECASE*) no distingue mayusculas de minúsculas.

Opciones habituales:

|Opcion | significado |
|:----:| :---- |
| `re.A` | sólo compara caracteres ASCII |
| `re.I` | no discrimina mayusculas de minusculas |
| `re.L` | depende de la configuración regional | 
| `re.M` | varias lineas | 
| `re.S` | si el patron incluye puntos estos son opcionales | 
| `re.U` | compara caracteres Unicode  | 
| `re.X` |  (verbose)  (?)| 


A continuación se explican las funciones del módulo. 

### `match()` 

`match()` busca una secuencia **justo al comienzo** de un string:

```python title="match() - uso"
<retorno> = re.match(<patron>, <texto>, <opcion>)
```
`match()` devuelve un objeto `re.Match()` cuando encuentra el patrón y sino devuelve `None`. 
`re.Match()` tiene un método llamado `span()` que indica los indices de inicio a fin de la secuencia en forma de tupla. 
Se lo llama así:

```python title="match() - indices de secuencia"
<retorno>.span()
```


Ejemplo:
```python
import re

patron = "leccion"

texto1 = "leccion 1: regex"
texto2 = "esta no es la leccion 1 sino la leccion 3"

retorno1 = re.match(patron, texto1, re.I)    # Devuelve 're.Match()'
retorno2 = re.match(patron, texto2, re.I)    # Devuelve None
```

Si el patrón fue detectado el retorno de la funcion `match()` será un objeto de tipo `re.Match` y de él se puede leer el resultado y su ubicación con ayuda de los métodos `group()` y `span()`. 
El método `span()` devuelve los indices de inicio y fin del primer patrón detectado, en tanto que el método `group()` devuelve el segmento del texto que cumple con el patrón.

```python
print(retorno1.group())     # patron detectado: leccion
print(retorno1.span())      # rango letras: (0,7)
```

Si en cambio el patrón no fue detectado el retorno de `match()` será `None` e intentar usar los métodos `group()` y `span()` dará error. 
Por ello es importante verificar el tipo de datos que arroja la función antes de intentar extraer una secuencia  de salida. 

Continuando con el ejemplo previo:
```python
retorno = retorno1      # hay coincidencia
# retorno = retorno2    # no hay coincidencia

if type(retorno)==re.Match:
    print("patron encontrado!")
    print("valor:    ",retorno.group())     # da 'leccion'
    print("ubicacion:" ,retorno.span())     # da '(0, 7)'
else:
    print("patron no detectado")    
```

### `search()` 

Busca la **primera** coincidencia de una secuencia en **cualquier lugar** del *string* indicado:

```python title="search()"
<retorno> = re.search(<patron>, <texto>, <opcion>)
```

`search()` devuelve un objeto `re.Match()` cuando encuentra el patrón (igual que la funcion `match()`) y sino devuelve None.

Ejemplo:

```python 
import re

patron = "leccion"

texto1 = "leccion 1: regex"
texto2 = "esta no es la leccion 1 sino la leccion 3"
texto3 = "aqui no se enseña nada"

retorno1 = re.search(patron, texto1, re.I)    # Devuelve 're.Match()'
retorno2 = re.search(patron, texto2, re.I)    # Devuelve 're.Match()'
retorno3 = re.search(patron, texto3, re.I)    # Devuelve 'None'
```
Al igual que con la función `match()`, con el método `span()` se obtienen los indices de inicio y fin del primer patrón detectado, en tanto que con el método `group()` se devuelve el resultado de la busqueda:

```python
print(retorno1.span()  )  # '(0, 7)'
print(retorno1.group() )  # 'leccion'
print(retorno2.span()  )  # '(14, 21)'
print(retorno2.group() )  # 'leccion'
```
Nuevamente hay que prestar atención al tipo de retorno de la función `search()` para evitar errores en la ejecución en caso de no detectarse el patrón buscado.


### `findall() `

Busca **todas** las coincidencias  de una secuencia en un string
```python title="findall()"
<retorno> = re.findall(<patron>, <texto>, <opcion>)
```
Devuelve una lista con todas coincidencias con el patrón indicado. Si no hay coincidencias la lista queda vacía.

Ejemplo:
```python
import re

patron = "leccion"

texto1 = "leccion 1: regex"
texto2 = "esta no es la leccion 1 sino la leccion 3"
texto3 = "aqui no se enseña nada"

retorno1 = re.findall(patron, texto1, re.I)  # devuelve '['leccion']'
retorno2 = re.findall(patron, texto2, re.I) # devuelve '['leccion', 'leccion']'
retorno3 = re.findall(patron, texto3, re.I) # devuelve '[]'
```


### `split()`

Parte un string en trozos limitados por un caracter o secuencia patrón indicado:
```python title="split()"
<retorno> = re.split(<patron>, <texto>,<opcion>)
```
El valor de retorno es una lista con el texto dividido y el patrón eliminado.
```python
import re

patron = "leccion"

texto1 = "leccion 1: regex"
texto2 = "esta no es la leccion 1 sino la leccion 3"

retorno1 = re.split(patron, texto1, re.I)    # Devuelve "['', ' 1: regex']"
retorno2 = re.split(patron, texto2, re.I)    # Devuelve "['esta no es la ', ' 1 sino la ', ' 3']"
```
Nótese cómo la palabra "leccion" fue eliminada y como en la lista de retorno puede haber textos vacíos.

### `sub()`

Reemplaza una secuencia por otra dentro de un string todas las veces que aparezca.
```python
<retorno> = re.sub(<patron>, <sustituto>,<texto>)
```
Ejemplo:

```python
import re

texto1 = "leccion 1: regex"
texto2 = "esta no es la leccion 1 sino la leccion 3.1"
texto3 = "leccion 2.UNO"

retorno1 = re.sub("1", "UNO", texto1) # Devuelve "leccion UNO: regex"
retorno2 = re.sub("1", "UNO", texto2) # Devuelve "esta no es la leccion UNO sino la leccion 3.UNO"
retorno3 = re.sub(patron , sustituto , texto3) # Devuelve "leccion 2.UNO"  (No cambia nada)
```

## Patrones regulares 

Los patrones regulares son expresiones que sirven para describir combinaciones genéricas de caracteres que cumplan ciertas condiciones. Las expresiones tienen una notación estandarizada por lo que pueden aplicarse en distintos lenguajes de programación con iguales resultados.

En el caso de Python los patrones regulares se definen antecedidos por la letra *'r'*:

```python
<patron> = r"<patron_regex>"
```
Estos patrones se ingresan en las funciones explicadas previamente como argumento para modificar los datos de entrada: filtrar, cortar , reemplazar, etc.

### Patrón para cifras numéricas

Este patrón sirve para detectar una o varias cifras numéricas contiguas
```python
patron_cifras = r"[0-9]+" 
```
!!! example "Uso: aislar el primer número de un texto"

    ```python
    entrada = "imag_025"

    patron_cifras  = r"[0-9]+" 

    retorno = re.search(patron_cifras, entrada)
    detectado= retorno.group()      # devuelve '025'
    rango = retorno.span()          # indices: '(5, 8)'
    ```


### Patrón para fotos digitales

Este patrón sirve para filtrar archivos de cámaras digitales , smartphones, etc. 

```python
patron_foto = r"^[0-9]+_[0-9]+\.[A-Za-z]+$"
```
El nombre de archivo suele ser  un numero compuesto por la fecha con un guión bajo en el medio. Por ejemplo, una foto hecha el 23 de junio del 2022 , hora 06:59:12 probablemente tendrá por nombre de archivo:
```python
archivo = "20220623_065912.jpg" #foto camara digital /smartphone
```

!!! example "Uso: filtrar nombres de archivo de cámaras (sin renombrar)"

    ```python
    import re

    archivo1 = "20220623_065912.jpg" #foto camara digital /smartphone
    archivo2 = "20220623065912.jpg" # falta el guion
    archivo3 = "RTY220623_A65912.jpg" # hay letras
    archivo4 = "/carpetaPOSIX/20220623_065912.jpg" # ruta POSIX (Unix / Linux)
    archivo5 = "\carpetaWINDOWS\20220623_065912.jpg" # ruta Windows

    patron_foto = r"^[0-9]+_[0-9]+\.[A-Za-z]+$"
    # partes (en orden):
    # '[0-9]'   : sólo numeros
    # '_'       : guion
    # '[0-9]'   : sólo numeros
    # '.'       : un punto
    # '[A-Za-z]': sólo letras mayúsculas y minúsculas

    print(re.findall(patron_foto, archivo1))    # ['20220623_065912.jpg']
    print(re.findall(patron_foto, archivo2))    # []
    print(re.findall(patron_foto, archivo3))    # []
    print(re.findall(patron_foto, archivo4))    # []
    print(re.findall(patron_foto, archivo5))    # []
    ```


### Patrón para E-mails



```python
patron_email = r"^[A-Za-z0-9_.+-]+@[A-Za-z0-9]+\.[A-Za-z0-9-.]+$"
```

!!! example "Uso: filtrado de direcciones de correo inválidas"

    ```python
    import re

    email1 = "yo@miserver.net" 
    email2 = "yo@miserver" 
    email3 = "yo_miserver.net" 
    email4 = "no_responder@spammers.net" 
    email5 = "no_responder.mi_spam@spammers.net" 

    patron_email = r"^[A-Za-z0-9_.+-]+@[A-Za-z0-9]+\.[A-Za-z0-9-.]+$"

    print(re.findall(patron_email, email1))    # ['yo@miserver.net']
    print(re.findall(patron_email, email2))    # []
    print(re.findall(patron_email, email3))    # []
    print(re.findall(patron_email, email4))    # ['no_responder@spammers.net']
    print(re.findall(patron_email, email5))    # ['no_responder.mi_spam@spammers.net']
    ```


## Referencias

[**Módulo RE - Documentacion oficial**](https://docs.python.org/es/3/library/re.html)

[**Regex101: Diseño y análisis interactivo**](https://regex101.com)


[**Cheat Sheet**](https://cheatography.com/davechild/cheat-sheets/regular-expressions/)


[**RegEx 101: Guía de supervivencia para entender y usar expresiones regulares**](https://eudriscabrera.com/blog/2022/regex-101.html)

