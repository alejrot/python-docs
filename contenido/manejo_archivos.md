## [Volver](../Python.md#manejo-de-archivos)

# Manejo de Archivos
Asumimos que los archivos están ubicados en el directorio del ejecutable o script.
Para trabajar con  un archivo podemos hacer:

```python
with open(“<ruta_archivo>”, “<modo_apertura>”) as  <descriptor_archivo>:
    # Rutina de archivo
    #...

# Cierre automático de archivo
```

El fin del indentado es interpretado como el cierre del archivo. Esto es así por haber utilizado la palabra **with** antecediendo la apertura. Si en cambio se prefiere hacer el cierre manualmente se puede hacer:

```python
<descriptor_archivo> = open(“<ruta_archivo>”, “<modo_apertura>”) 
# Rutina de archivo
# ...
<descriptor_archivo>.close()  # cierre manual
```
En este caso no se agrega indentado. El cierre de archivo es importante para asegurar el guardado de datos en el archivo, el cual puede fallar si el archivo no se cierra correctamente.


El asignar una variable descriptora para el archivo permite usar los métodos de Python para la manipulación de archivos, esto se verá más adelante. 

## Modos de Apertura

El modo de apertura del archivo puede ser:

|Modo apertura| Descripcion |
|---- |------- |
| **r**  | ***read:*** leer  |
| **w** | ***write:*** escribir  |
| **a**  |  ***append:*** añadir al final  | 
| **x** | ***creación exclusiva:*** sólo crea el archivo si éste no existe |


Si se añade el signo más (**+**) al modo de apertura se incluye la lectura ó modificacion, según corresponda. Por ejemplo ***"w+"*** permite leer y escribir. Además, añadiendo la letra **b** se indica la modalidad *binaria* de lectura o escritura, es decir los datos se leen y escriben en binario (como están). Por ejemplo, para leer archivos binarios y poder modificarlos la etiqueta correspondiente es **"rb+"**. Los archivos binarios reprensentan cualquier tipo de contenido que no sea texto y pueden representar imagenes, audio, video, etc.


## Métodos de archivos

### close()

Este método es el usado para el cierre manual del archivo. Uso: 

```python
ruta = “./texto.txt”
archivo =  open(ruta, “r”) 
# Rutina
# ...
archivo.close()    # necesario / prudente
```

Si se hace la apertura con el comando **with** el cierre manual no es necesario.

```python
ruta = “./texto.txt”
with open(ruta, “r”) as archivo: 
  # Rutina
  # ...
  archivo.close()    # redundante
```


### read()

El método ***read()*** permite leer total o parcialmente el contenido del archivo

```python
ruta = “./texto.txt”
with open(ruta, “r”) as archivo: 
  print( archivo.read() )   # lee TODO el contenido como texto
```
Al método se le puede indicar la cantidad de caracteres a leer cada vez entre los paréntesis:

```python
ruta = “./texto.txt”
with open(ruta, “r”) as archivo:  # modo lectura
  print( archivo.read(20) )   # lee los primeros 20 caracteres  
  print( archivo.read(20) )   # lee los siguientes 20 caracteres
```

Nótese que cada nueva operacion de lectura comienza donde terminó la anterior. Esto tiene que ver con el "puntero de archivo" que guarda dentro del descriptor de archivo esa información.


### seek()

El método **seek()** permite elegir el indice desde donde deben comenzar las operaciones de lectura o escritura.

Por ejemplo, si se desea leer el contenido desde el caracter Nº20 en adelante (repasar ejemplo previo) se puede hacer:


```python
ruta = “./texto.txt”
with open(ruta, “r”) as archivo:  # modo lectura
  archivo.seek(20)            # modificacion del puntero del archivo  
  print( archivo.read() )   # lee los siguientes caracteres
```
Este mismo método permite reiniciar las operaciones de lectura sin necesidad de reapertura del archivo, colocando el índice cero:

```python
  #....
  archivo.seek(0)            # puntero del archivo al comienzo de datos 
  print( archivo.read() )   # lee los siguientes caracteres
```



### readline()

Este método lee un renglón a la vez y le añade al final un signo de fin de carrera (**'\n'** en ASCII). Uso:

```python
ruta = “./texto.txt”
with open(ruta, “r”) as archivo:
  print( archivo.readline() )   # lee primer renglón  
  print( archivo.realined() )   # lee segundo renglón
```

### readlines()

Este método es similar al anterior pero lee todos los renglones del archivo juntos y los devuelve agrupados en una lista. Ejemplo uso:

```python
ruta = “./texto.txt”
open(ruta, “r”) as archivo:
  lista_renglones = archivo.readlines()    # lee renglones como lista 
  for renglon in lista_renglones:
    print(renglon)
```
Este método tambien añade un fin de carrera a cada renglón.


### readable()

Verifica la posibilidad de leer o no de un archivo. Es afectado por el modo de apertura elegido. Ejemplos:


```python
ruta = “./texto.txt”
open(ruta, “w”) as archivo:
  legible = archivo.readable()    # devuelve False
#...
open(ruta, “w+”) as archivo:
  legible = archivo.readable()    # devuelve True
```

### write()

Este método reescribe (o añade) contenido al archivo. Es afectado tanto por el modo de apertura de archivo como por el puntero del archivo (ver método **seek()**) :

#### Reemplazo al comienzo:
```python
ruta = “./texto.txt”
archivo = open(ruta, “r+”)  # modo lectura con añadido
agregado = "renglon añadido"
archivo.write( agregado )   # el contenido reemplaza al primer renglon
archivo.close()
```

#### Añadido al final:
```python
ruta = “./texto.txt”
archivo = open(ruta, “a”)  # modo añadido ('append')
agregado = "renglon añadido"
archivo.write( agregado )   # el contenido se agrega al final del archivo
archivo.close()
```

#### Sobreescritura:
```python
ruta = “./texto.txt”
archivo = open(ruta, “w”)  # modo escritura estricta (tambien se puede hacer con "w+")
nuevo_contenido = "Mi nuevo texto"
archivo.write( nuevo_contenido )   # se borra TODO y se escribe el nuevo contenido
archivo.close()
```

*write()* tiene un valor de retorno numerico que representa al número de caracteres añadidos al archivo.


### writable()

Verifica que el archivo esté en condiciones de ser escrito. Es afectado por los modos de apertura. 

Ejemplo de uso: apertura en modo sólo lectura

```python
archivo = open(ruta, “r”)  # modo lectura con modificacion
print(archivo.writable() )    # da False
```
Ejemplo de uso: apertura en modo lectura con modificación

```python
archivo = open(ruta, “r+”)  # modo lectura con modificacion
print(archivo.writable() )    # da True
```

### encoding

La función **open()** tiene un argumento opcionarl llamado **encoding** el cual permite elegir la codificación para leer y escribir archivos.

```python
with open("archivo_utf8.txt","w", encoding="utf-8") as archivo:
    archivo.write( "Hola UTF-8")

with open("archivo_utf16.txt","w", encoding="utf-16") as archivo:
    archivo.write( "Hola UTF-16")

with open("archivo_utf32.txt","w", encoding="utf-32") as archivo:
    archivo.write( "Hola UTF-32")
```


## Archivos JSON

Los archivos JSON (*JavaScript Object Notation*) son muy utilizados para guardar información en el formato de  los "objetos" de JavaScript, muy similar a los diccionarios de Python.

Python tiene el módulo dedicado ***json***, el cual debe importarse para su uso:
```python
import json
```
Los archivos JSON deben estar codificados en formato UTF-8, UTF-16 o UTF-32.


### Apertura y cierre
La operacion de apertura se hace con la función **open()**, igual que con otros tipos de archivo. El cierre de archivo se hace con el método *close()*.
 
```python
# crear archvio
ruta = "./datos.json"
archivo_json = open(ruta,"w+") 
# ....
archivo_json.close()  
```

### Guardado de diccionario

La escritura de archivo se hace con la función **dump()** del módulo **json**. Esta función da la opción de añadir un número de espacios para el indentado a la salida. Si no se indica todo el contenido se guarda en un único renglón

```python
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

Nótese que el archivo de salida JSON debe ser creado primero con la función *open()* en modo escritura. La función *dump()* requiere el descriptor de archivo para funcionar.

### Lectura de diccionario

La lectura de los datos de archivo JSON se hace con la función **load()** del módulo **json**.
Esta lectura se hace tras la apertura del archivo con la función *open()*.


```python
# nombre de archivo de entrada
ruta = 'data.json'

#leer diccionario desde archivo JSON
with open(ruta) as archivo:
    mi_data = json.load( archivo )  #lectura del diccionario desde JSON
```


### Conversion de tipo datos

El módulo JSON incluye funciones para convertir diccionarios (*objetos JSON*) en textos simples y viceversa. Para ello se usan las funciones **loads()** y **dumps()**: 

```python
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


----
----
----

## [Inicio](#manejo-de-archivos) 

## [Volver](../Python.md#manejo-de-archivos)