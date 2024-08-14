# Manejo de Archivos


## Apertura

Asumimos que los archivos están ubicados en el directorio del ejecutable o script.
Para trabajar con  un archivo podemos hacer:

```python title="Apertura archivos - cierre automático" hl_lines="1"
with open(“<ruta_archivo>”, “<modo_apertura>”) as  <descriptor_archivo>:
    # Rutina de archivo
    #...

# Cierre automático de archivo
```

El fin del indentado es interpretado como el cierre del archivo. Esto es así por haber utilizado la palabra `with` antecediendo la apertura. Si en cambio se prefiere hacer el cierre manualmente se puede hacer:

```python title="Apertura archivos - cierre manual" hl_lines="1 4"
<descriptor_archivo> = open(“<ruta_archivo>”, “<modo_apertura>”) 
# Rutina de archivo
# ...
<descriptor_archivo>.close()  # cierre manual
```
En este caso no se agrega indentado.


El asignar una variable descriptora para el archivo permite usar los métodos de Python para la manipulación de archivos, esto se verá más adelante. 

!!! info "Cierre de archivos"

	El cierre de archivo es importante para asegurar el guardado de datos en el archivo, el cual puede fallar si el archivo no se cierra correctamente. También permite liberar recursos del sistema operativo que, de otra manera, qeuedarían ocupados hasta el siguiente reinicio.


!!! tip "Cierre automático"

	Muchos desarrolladores consideran una buena práctica el uso de la cláusula `with` para de esa manera asegurar el cierre de archivo tras su acceso. 



## Modos de Apertura

El modo de apertura del archivo puede ser:

|Modo apertura| Descripcion |
|---- |------- |
| **r**  | ***read:*** leer  |
| **w** | ***write:*** escribir  |
| **a**  |  ***append:*** añadir al final  | 
| **x** | ***creación exclusiva:*** sólo crea el archivo si éste no existe |


Si se añade el signo más (`+`) al modo de apertura se incluye la lectura ó modificacion, según corresponda. Por ejemplo `"w+"` permite escribir y también leer, en tanto que `r+` permite leer y modificar.

!!! info "File pointer"

	Los descriptores de archivo incluyen un puntero o apuntador de archivo (*file pointer*) interno el cual apunta a alguno de los bytes o caracteres internos del archivo, funcionando como un índice. La posición de dicho apuntador dependerá del modo de apertura elegido, de las operaciones posteriores de lectura o de escritura, etc.


La tabla completa con los permisos y la posición del apuntador es la siguiente:

 | Permisos  y propiedades  | r  | r+ |  w | w+ |  a |  a+ |
| ------------------    |----|----|----|----|----|-----|
| leer                  | :material-check-bold:  | :material-check-bold:  |    |  :material-check-bold: |    |  :material-check-bold:  |
| escribir              |    | :material-check-bold:  |  :material-check-bold: |  :material-check-bold: |  :material-check-bold: |  :material-check-bold:  |
| escribir tras buscar  |    |:material-check-bold:  |  :material-check-bold: |  :material-check-bold: |    |     |
| crear                 |    |    |  :material-check-bold: |  :material-check-bold: | :material-check-bold: |  :material-check-bold: |
| borrar                |    |    |  :material-check-bold: |  :material-check-bold: |    |     |
| position at comienzo  | :material-check-bold: | :material-check-bold:  | :material-check-bold: |  :material-check-bold:|    |     |
| posición al final     |    |    |    |    |  :material-check-bold: | :material-check-bold:  |




!!! info "Apertura binaria"

    Añadiendo la letra `b` a las opciones de apertura se indica la modalidad *binaria* de lectura o escritura, es decir los datos se leen y escriben en binario. Por ejemplo, para leer archivos binarios y poder modificarlos la etiqueta correspondiente es `"rb+"`. 
    Los archivos binarios reprensentan cualquier tipo de contenido que no sea texto y pueden representar imagenes, audio, video, etc.





## Métodos del descriptor de archivos

### `close()`

Este método es el usado para el cierre manual del archivo. Uso: 

```py title="Cierre manual" hl_lines="5"
ruta = "texto.txt”
archivo =  open(ruta, "r") 
# Rutina
# ...
archivo.close()    # necesario / prudente
```

Si se hace la apertura con el comando **with** el cierre manual no es necesario.

```py title="Cierre manual redundante" hl_lines="5"
ruta = "texto.txt”
with open(ruta, "r") as archivo: 
  # Rutina
  # ...
  archivo.close()    # redundante
```


### `read()`

El método `read()` permite leer total o parcialmente el contenido del archivo.

```py title="read() - Leer todo" hl_lines="3"
ruta = "texto.txt"
with open(ruta, "r") as archivo: 
  print( archivo.read() )   # lee TODO el contenido como texto
```
Al método se le puede indicar la cantidad de caracteres a leer cada vez entre los paréntesis:

```python title="read() - Leer N caracteres" hl_lines="3 4"
ruta = "texto.txt"
with open(ruta, "r") as archivo:  # modo lectura
  print( archivo.read(20) )   # lee los primeros 20 caracteres  
  print( archivo.read(20) )   # lee los siguientes 20 caracteres
```

Nótese que cada nueva operación de lectura comienza donde terminó la anterior. Esto tiene que ver con el *"puntero de archivo"* que guarda dentro del descriptor de archivo esa información.


### `seek()`

El método `seek()` permite elegir el indice desde donde deben comenzar las operaciones de lectura o escritura. Afecta al *file pointer* interno.

```py title="seek() - argumentos"
archivo.seek(offset, whence)
```

Este método tiene dos argumentos: `offset` indica la posición relativa del puntero interno en tanto que `whence` es el punto de referencia.

|valor `whence`| Referencia |
|:---:|:---|
| 0 | Comienzo de archivo (valor predefinido)|
| 1 | Posición actual |
| 2 | Final de archivo |



Por ejemplo, si se desea leer el contenido desde el caracter Nº20 en adelante (repasar ejemplo previo) se puede hacer:


```py title="seek() - Buscar caracter N-ésimo" hl_lines="3"
ruta = "texto.txt”
with open(ruta, "r") as archivo:  # modo lectura
  archivo.seek(20)            # modificacion del puntero del archivo  - equivale a 'seek(20,0)' 
  print( archivo.read() )   # lee los siguientes caracteres
```
Este mismo método permite reiniciar las operaciones de lectura sin necesidad de reapertura del archivo, colocando el índice cero:

```py title="seek() - Reiniciar lectura" hl_lines="2"
  #....
  archivo.seek(0)            # puntero del archivo al comienzo de datos - equivale a 'seek(0,0)' 
  print( archivo.read() )   # lee los siguientes caracteres
```


También se puede buscar el fin de archivo con ayuda de esta función:

```py title="seek() - Fin archivo" hl_lines="1 2"
  archivo.seek(0, 2)   # Último carácter 
```


!!! warning "Restricciones de seek()"

    Cuando los archivos están abiertos en **modo texto**, la mayoría de las combinaciones de  `offset` y `whence` **lanzan error**.

    En cambio, dichas combinaciones sí se permiten cuando se abren los archivos en **modo binario**, donde la posición relativa `offset` representa cuántos bytes se debe avanzar o retroceder.


### `readline()`

Este método lee un renglón a la vez y le añade al final un signo de fin de carrera (`\n` en ASCII). Uso:

```py title="Leer" hl_lines="3 4"
ruta = "texto.txt”
with open(ruta, "r") as archivo:
  print( archivo.readline() )   # lee primer renglón  
  print( archivo.readline() )   # lee segundo renglón
```

Cada renglón leído se devuelve en formato `str` (*string*) y a cada uno se le agrega un carácter de fin de línea (`\n`). 

Si se alcanza el final del archivo la función `readline()` devuelve un *string* completamente vacío.


!!! example "Contador de renglones"

	  Se pueden contar los renglones de archivo con ayuda de un bucle `while`, el cual se abre cuando se detecta el string vacío:

    ```py title="Ejemplo: contador renglones" hl_lines="8"
    ruta = "texto.txt"
    with open(ruta, "r") as archivo:  # modo lectura
      contenido = True
      n = 0
      while contenido:
        renglon = archivo.readline()
        print(f"{renglon}")
        if not renglon:
          contenido = False
        else:
          n += 1
      print(f"Nº renglones: {n}")
    ```



### `readlines()`

Este método es similar al anterior pero lee todos los renglones del archivo juntos y los devuelve agrupados en una lista. Ejemplo uso:

```python
ruta = "texto.txt”
open(ruta, "r") as archivo:
  lista_renglones = archivo.readlines()    # lee todos los renglones como lista 
  for renglon in lista_renglones:
    print(renglon)		# presentación: un renglón por vez
```
Este método tambien añade un fin de carrera (`\n`) a cada renglón.


### `readable()`

Verifica la posibilidad de leer o no un archivo. Es afectado por el modo de apertura elegido. Ejemplos:


```py title="Verificar legibilidad" hl_lines="3 6"
ruta = "texto.txt”
open(ruta, "w") as archivo:
  legible = archivo.readable()    # devuelve 'False'
#...
open(ruta, "w+") as archivo:
  legible = archivo.readable()    # devuelve 'True'
```

### `write()`

Este método reescribe (o añade) contenido al archivo. Es afectado tanto por el modo de apertura de archivo como por el puntero del archivo (ver método `seek()`).


```py title="Reemplazo al comienzo - modo 'r+'" hl_lines="2"
ruta = "texto.txt”
archivo = open(ruta, "r+")  # modo lectura con añadido
agregado = "renglon añadido"
archivo.write( agregado )   # el contenido reemplaza al primer renglon
archivo.close()
```


```py title="Reemplazo al final - modo 'a'" hl_lines="2"
ruta = "texto.txt”
archivo = open(ruta, "a")  # modo añadido ('append')
agregado = "renglon añadido"
archivo.write( agregado )   # el contenido se agrega al final del archivo
archivo.close()
```

```py title="Sobreescritura total - modo 'w'" hl_lines="2"
ruta = "texto.txt”
archivo = open(ruta, "w")  # modo escritura estricta (tambien se puede hacer con "w+")
nuevo_contenido = "Mi nuevo texto"
archivo.write( nuevo_contenido )   # se borra TODO y se escribe el nuevo contenido
archivo.close()
```


!!! tip "Caracteres escritos" 
	
	`write()` tiene un valor de retorno numérico que representa el número de caracteres añadidos al archivo.


### `writable()`

Verifica que el archivo esté en condiciones de ser escrito. Es afectado por los modos de apertura. 


```py title="Verificar permisos de escritura" hl_lines="2 5"
archivo = open(ruta, "r")  # modo lectura con modificacion
print(archivo.writable() )    # da 'False'

archivo = open(ruta, "r+")  # modo lectura con modificacion
print(archivo.writable() )    # da 'True'
```

### `encoding`

La función `open()` tiene un argumento opcional llamado `encoding` el cual permite elegir la codificación para leer y escribir archivos.

```python title="Codificación de archivos" hl_lines="1 4 7"
with open("archivo_utf8.txt","w", encoding="utf-8") as archivo:
    archivo.write( "Hola UTF-8")

with open("archivo_utf16.txt","w", encoding="utf-16") as archivo:
    archivo.write( "Hola UTF-16")

with open("archivo_utf32.txt","w", encoding="utf-32") as archivo:
    archivo.write( "Hola UTF-32")
```


## Archivos JSON

Los archivos JSON (*JavaScript Object Notation*) son muy utilizados para guardar información en el formato de  los "objetos" de JavaScript, muy similar a los diccionarios de Python.

### Importación

Python tiene el módulo dedicado ***json***, el cual debe importarse para su uso:
```python title="Importación de módulo JSON" 
import json
```
Los archivos JSON deben estar codificados en formato `UTF-8`, `UTF-16` o `UTF-32`.


### Apertura y cierre
La operacion de apertura se hace con la función `open()`, igual que con otros tipos de archivo. El cierre de archivo se hace con el método `close()`*.
 
```python title="Apertura y cierre de JSON" hl_lines="3 5"
# crear archvio
ruta = "./datos.json"
archivo_json = open(ruta,"w+") 
# ....
archivo_json.close()  
```

### Guardado de diccionario

La escritura de archivo se hace con la función `dump()` del módulo **json**. Esta función da la opción de añadir un número de espacios para el indentado a la salida. Si no se indica todo el contenido se guarda en un único renglón

```py title="Guardado de diccionarios" hl_lines="14"
# nombre de archivo de salida
ruta = 'data.json'

#crear diccionario ("objeto" de JavaScript)
diccionario = {
    "Nombre": "Aitor",
    "Apellido":"Tilla",
    "Edad": 38,
    }

# apertura archivo de salida
with open(ruta, 'w') as archivo_json:
    # escribir archivo
    json.dump(diccionario, archivo_json, indent=4)
```

Nótese que el archivo de salida JSON debe ser creado primero con la función `open()` en modo escritura. La función `dump()` requiere el descriptor de archivo para funcionar.

### Lectura de diccionario

La lectura de los datos de archivo JSON se hace con la función `load()` del módulo **json**.
Esta lectura se hace tras la apertura del archivo con la función `open()`.


```py title="Lectura de diccionarios" hl_lines="6"
# nombre de archivo de entrada
ruta = 'data.json'

#leer diccionario desde archivo JSON
with open(ruta) as archivo:
    mi_data = json.load( archivo )  #lectura del diccionario desde JSON
```


### Conversion de tipo de datos

El módulo JSON incluye funciones para convertir diccionarios (*objetos JSON*) en textos simples y viceversa. Para ello se usan las funciones `loads()` y `dumps()`: 

```py title="Conversión de diccionarios" hl_lines="11 14"
import json

# datos en diccionario, compatible con JSON 
diccionario = { 
    "language": "es",
    "theme" : "light",
    "date" : "Jan 19"
    }

# conversion a texto
texto = json.dumps( diccionario , indent=4)

# conversion a diccionario
diccionario_2 = json.loads(texto)
```

[Repasar tipos datos: diccionarios](tipos_datos.md#diccionarios)





## Rewferencias

[StackOverflow - Difference between modes... ](https://stackoverflow.com/questions/1466000/difference-between-modes-a-a-w-w-and-r-in-built-in-open-function)