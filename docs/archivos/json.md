---
tags:
  - JSON
  - Diccionarios
  - Archivos
---


# Archivos JSON

Los archivos JSON (*JavaScript Object Notation*) son muy utilizados para guardar información en el formato de  los "objetos" de JavaScript, muy similar a los diccionarios de Python.

## Importación

Python tiene el módulo dedicado ***json***, el cual debe importarse para su uso:
```python title="Importación de módulo JSON" 
import json
```
Los archivos JSON deben estar codificados en formato `UTF-8`, `UTF-16` o `UTF-32`.


## Apertura y cierre
La operacion de apertura se hace con la función `open()`, igual que con otros tipos de archivo. El cierre de archivo se hace con el método `close()`.
 
```python title="Apertura y cierre de JSON" hl_lines="3 5"
# crear archvio
ruta = "./datos.json"
archivo_json = open(ruta,"w+") 
# ....
archivo_json.close()  
```

## Guardado de diccionario

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

## Lectura de diccionario

La lectura de los datos de archivo JSON se hace con la función `load()` del módulo **json**.
Esta lectura se hace tras la apertura del archivo con la función `open()`.


```py title="Lectura de diccionarios" hl_lines="6"
# nombre de archivo de entrada
ruta = 'data.json'

#leer diccionario desde archivo JSON
with open(ruta) as archivo:
    mi_data = json.load( archivo )  #lectura del diccionario desde JSON
```


## Conversion de tipo de datos

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

[Repasar tipos datos: diccionarios](../datos/diccionarios.md)




