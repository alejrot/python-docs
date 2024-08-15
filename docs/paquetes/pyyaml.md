

# PyYAML


## YAML

YAML (*YAML Ain't Markup Language™*) es un formato de archivo muy popular para archivos de configuraciones y también se usa para intercambio de datos. Es un formato simple de leer aunque también es muy sensible respecto al indentado.


[Página oficial de YAML](https://yaml.org/)

Este formato no está implementado de forma nativa en Python, por ello se requiere recurrir a paquetes externos. 

### Formato

Los archivos YAML permiten guardar tanto listas como diccionarios. A continuación se muestran algunos ejemplos

#### Listas


```yaml title="Lista de valores - YAML"
- 4
- 9
- -1
```

```py title="Lista de valores - Python"
[4, 9, -1]
```

#### Listas de diccionarios

```yaml title="Lista de diccionarios - YAML"
- x : 4
- y : 9
- z : -1
```

``` py title="Lista de diccionarios - Python"
[{'x': 4}, {'y': 9}, {'z': -1}]
```


#### Diccionarios

```yaml title="Diccionario - YAML" 
debug: true     

data_numerica:   
- x : 4
- y : 9
- z : -1
```

```py title="Diccionario - Python"
{'debug': True, 'data_numerica': [{'x': 4}, {'y': 9}, {'z': -1}]}
```

Nótese que el valor `true` se convierte a booleano `True` automáticamente.

#### Multiples objetos

Un mismo archivo puede guardar varios objetos de datos: 

```yaml title="Objetos múltiples - YAML" hl_lines="7"
# objeto Nº1 
data_numerica:   
- x : 4
- y : 9
- z : -1

---  # separador de objetos

# objeto Nº2 
debug: true
```

Por último YAML soporta comentarios internos, tal como se ve en el ejemplo previo.


## PyYAML

PyYAML es el paquete más usado para dar soporte en Python. 

[Sitio de PyYAML](https://pyyaml.org/wiki/PyYAMLDocumentation)


## Instalacion

```bash title="Instalación - PIP"
pip install pyyaml
```


## Importacion

El módulo debe importarse para su uso.
```py title="Importación" 
import yaml
```


## Lectura desde archivo 


Para leer los archivos hay dos funciones específicas llamadas `safe_load()` y `safe_load_all()`.


!!! danger "Funcion load()"

    La función `load()` permite la ejecución de código malicioso guardado y por ello está marcada como obsoleta. `safe_load()` es su versión recortada, que tiene menos opciones pero que es mucho más segura de usar.



### Objeto único




Para leer y decodificar archivos con un único objeto de datos se usa la función `safe_load()`:


```py title="lectura desde archivo - objeto unico" hl_lines="3"
ruta = "data_simple.yml"
with open(ruta,  'r') as archivo:
    data_archivo = yaml.safe_load(archivo)

print(data_archivo)
print(type(data_archivo))   # 'dict'
``` 

!!! warning "Data única"

    `safe_load()` no admite archivos con data múltiple, porque de intentarse el intérprete dará error e interrumpirá el programa.


### Objetos múltiples

En caso deque el archivo contenga múltiples objetos de datos se usa la función `safe_load_all()`.

```py title="lectura desde archivo - objetos múltiples" hl_lines="4"
datos = []
ruta = "data_doble.yml"
with open(ruta,  'r') as archivo:
    data_archivo = yaml.safe_load_all(archivo)  # tipo salida 'generator'
    # la data debe extraerse antes de cerrar el archivo
    for data in data_archivo:    
        datos.append(data)
        
print(datos)
``` 
Esta función devuelve un objeto `generator` el cual debe recorrerse para rescatar la información antes de cerrar el archivo



## Conversion desde strings


Las funciones `safe_load()` y `safe_load_all()` admiten a su entrada datos en formato texto simple.


### Objeto único

``` py title="Lectura desde texto simple - objeto único"
nombres_texto = """
data_numerica:   
- x : 4
- y : 9
- z : -1
"""

data_nombres = yaml.safe_load(nombres_texto)  # diccionario
``` 

### Objetos múltiples

```py title="Lectura desde texto simple - objetos múltiples" hl_lines="7"
datos_texto = """
# objeto Nº1 
data_numerica:   
    - x : 4
    - y : 9
    - z : -1
---
# objeto Nº2
debug: true
"""

data_nombres = []
generador_data = yaml.safe_load_all(datos_texto)

for data in generador_data:
    data_nombres.append(data)


print(data_nombres)
```

!!! warning "Indentado"

    Hay que evitar a toda costa el tabular la secuencia `---` para evitar errores de lectura.



## Guardado de datos


Para el guardado de objetos en Python se usa la función `dump()`:

```py hl_lines="5" title="guardado de datos"
data_nombres: dict|list

ruta_salida = "data_salida.yml"
with open(ruta_salida, 'w') as archivo:
    yaml.dump(data_nombres, archivo)
```

Otras opciones:
```py
yaml.dump()
yaml.dump_all()
yaml.safe_dump()
yaml.safe_dump_all()
```


## Referencias




[Python Land - Python YAML: How to Load, Read, and Write YAML ](https://python.land/data-processing/python-yaml)

