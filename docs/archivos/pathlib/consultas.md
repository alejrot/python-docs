---
tags:
  - Archivos
  - Carpetas
  - Rutas
  - Pathlib
---

# Consultas de recursos

`Path()` y sus derivados incluyen funcionalidades para explorar directorios,
leer información de los "ficheros" (carpetas y archivos),
etcétera.

En todo este capítulo se asume el uso de la función `Path()`:
```py title="Path - Importación"
from pathlib import Path
```

## Búsqueda de archivos y carpetas

### Búsqueda simple

Con el método `iterdir()` se buscan los archivos y carpetas
contenidas dentro de la ruta indicada.
No se exploran las carpetas internas.

```python title="Búsqueda simple - iterdir" hl_lines="2"
ruta_carpeta: str
objeto_busqueda = Path(ruta_carpeta).iterdir()
rutas_internas = list(objeto_busqueda)
```
La conversión a lista permite recuperar las rutas obtenidas.

Por ejemplo, para buscar contenidos en la carpeta actual se puede hacer:

```python title="Búsqueda simple - ruta actual"
objeto_busqueda = Path(".").iterdir()
rutas_internas = list(objeto_busqueda)
```

y para mostrar las rutas en consola:

```py title="muestra en consola"
for ruta in rutas_internas:
    print(str(ruta))
```

### Búsqueda recursiva

La búsqueda de todos los elementos internos del directorio elegido
se realiza con el método `walk()`.

```python title="Búsqueda recursiva" hl_lines="2"
ruta_carpeta: str
objeto_busqueda = Path(ruta_carpeta).walk(top_down=True)
lista_objetos   = list(objeto_busqueda)
```

El uso es muy similar al del método `iterdir()`:

```python title="Búsqueda recursiva - ruta actual" 
objeto_busqueda = Path(".").walk(top_down=True)
lista_objetos   = list(objeto_busqueda)
```

El resultado de este método es un objeto compuesto.
Al convertirlo en lista se obtiene una lista de objetos,
cada uno de los cuales tendrá internamente:
 
 - una ruta de carpeta;
 - una lista de subcarpetas;
 - una lista de archivos.

Toda esta información se obtiene convirtiendo los objetos internos en lista,
tal como se ve en el ejemplo:

```py title="muestra en consola" 
for directorio in lista_objetos:
    [ruta, subdirectorios, archivos ] = list(directorio)
    print(f"ruta           :  {ruta}")
    print(f"nombre carpetas:  {subdirectorios}")
    print(f"nombre archivos:  {archivos}")
```


### Búsqueda por patrones

Se dispone de dos métodos para buscar elementos
que cumplan con un patrón de texto específico
llamados `glob()` y `rglob()`:


=== "Búsqueda simple"

    ```python title="Búsqueda por patrón"
    ruta_directorio: str
    patron: str

    objeto = Path(ruta_directorio).glob(patron)   

    lista_rutas = list(objeto)      # resultado
    ```

=== "Búsqueda recursiva"

    ```python title="Búsqueda por patrón"
    ruta_directorio: str
    patron: str

    objeto = Path(ruta_directorio).rglob(patron)   

    lista_rutas = list(objeto)      # resultado
    ```

Ejemplo de uso: búsqueda recursiva de imagenes en base a su extensión.

```python title="Búsqueda de imagenes .png y .PNG"
objeto = pathlib.Path(ruta).rglob("*.png", case_sensitive=False)
lista_imagenes = list(objeto) 
```


## Información del sistema


### Carpeta de usuario 

Con el método `home()` se consulta la carpeta personal del usuario actual:

```python title="ruta 'home'" 
carpeta_usuaurio = Path().home()   # carpeta personal del usuario actual
```

### Carpeta actual del programa

El método `cwd()` devuelve la ruta del sistema
donde el programa actual está ubicado:

```python title="ruta actual" 
carpeta_programa = Path().cwd()   # carpeta actual del programa
```


## Información de recursos


### Verificar existencia

`exists()` devuelve `True` si el elemento indicado por la ruta existe, sino da `False`.

```python title="Verificar" 
existe = Path(ruta).exists()    
```


### Estadisticas de archivo 

El método `stat()`
provee información variada sobre el elemento especificado por la ruta:
fechas de creacion y modificacion, espacio en disco, identificadores de usuario y de grupo, etc. 

Uso:
```python title="Estadisticas de elemento"
objeto_estadisticas = Path(ruta).stat()
```
El objeto de salida contiene la información en forma de atributos internos. 
Algunos de ellos son:

|atributo | información |
|:---|:---|
| `st_uid`    | identificador d usuario|
| `st_gid`    | identificador de grupo|
| `st_size`   | espacio de disco en bytes (si es carpeta no incluye su contenido) | 
| `st_ctime`  | fecha creacion - formato POSIX|
| `st_mtime`  | fecha ultima modificacion - formato POSIX|
| `st_atime`  | fecha ultimo acceso - formato POSIX|

Por ejemplo, para consultar las fechas de creación, modificación y ultimo acceso de un elemento:

```python title="lectura de fechas"
estadisticas = Path(ruta).stat()
creacion     = estadisticas.st_ctime
modificacion = estadisticas.st_mtime
acceso       = estadisticas.st_atime
```

### Usuarios y grupos 

Los métodos `owner()` y `group()` son los encargados 
de proporcionar información acerca
del usuario propietario de un recurso
y de su grupo de usuarios:

```python title="Propietario y Grupo"
usuario_propietario       = Path(ruta_recurso).owner()
grupo_usuario_propietario = Path(ruta_recurso).group()
```


## Manejo de rutas

### Comparar

`samefile()` es un método que permite comparar dos rutas entre sí
basándose en la estructura de los directorios del sistema anfitrión.

```python title="Comparar rutas"
# rutas del sistema (DEBEN existir o da error)
ruta_A: str = "/home"
ruta_B: str = "/etc"

# compara
mismo_ruta = Path(ruta_A).samefile(ruta_B) # 'False'   
misma_ruta = Path(ruta_A).samefile(ruta_A) # 'True'
```
Nótese que `samefile()` sirve también para directorios.

Este metodo es práctico para comparar rutas relativas con rutas absolutas. 

Ejemplos:

```python title="comparando rutas - directorio actual"
# comparando directorio actual
ruta_actual = Path().cwd()
iguales     = Path(ruta_actual).samefile(".")  # 'True'
```

```python title="comparando rutas - directorio padre"
# rutas al directorio padre
ruta_padre = Path().cwd().parent
iguales    = Path(ruta_padre).samefile("../") # 'True'
```



### Convertir

El método `absolute()` sirve para convertir la ruta especificada
en ruta absoluta,
basándose en la estructura de los directorios del sistema anfitrión.

```python title="Conversión a ruta absoluta"
ruta_absoluta = Path(ruta).absolute() 
```

El resultado es un objeto `WindowsPath` o `PosixPath` con la ruta obtenida.


Ejemplo de uso: ruta absoluta del directorio con el ejecutable actual.

```python title="Ruta actual"
nombre_archivo = Path(".").absolute()
```

Una alternativa superadora es el método `resolve()`,
el cual resuelve los enlaces simbólicos que pudiera haber en la ruta.



### Expandir


El método `expanduser()`
convierte las rutas relativas respecto a la carpeta personal
en ruta absoluta en base a la carpeta personal del usuario actual.


=== "Windows"

    ```python title="Rutas de usuario"
    ruta_archivo = Path("~\documentos\hola.txt").expanduser()
    # WindowsPath('C:/Users/usuario/documentos/hola.txt')
    ```

=== "Posix"

    ```python title="Rutas de usuario"
    ruta_archivo = Path("~/documentos/hola.txt").expanduser()
    # PosixPath('/home/usuario/documentos/hola.txt')
    ```


### Leer enlaces

Los enlaces simbólicos son leídos con el método `readlink()`:

```python title="Ruta actual"
ruta_destino = Path(ruta_enlace).readlink()
```

El resultado es la ruta guardada dentro del enlace.


### Manejo de URIs

El método `as_uri()` convierte la ruta de entrada a URI (*Unified Resource Identifier*).
La ruta debe corresponder a un recurso existente.

=== "Windows"

    ```py title="Obtener URI"
    Path("C:\\windows").as_uri()    # 'file:///C:/windows'
    ```

=== "Posix"

    ```py title="Obtener URI"
    Path("/home/user").as_uri()
    ```




## Verificar recursos

Se dispone de varios métodos para chequear que existan
distintos tipos de elementos:
carpetas, archivos, sockets, volumenes , etc.


|método|descripción|
|:---|:---|
|`ìs_file()`| archivo|
|`ìs_dir()`| directorio |
|`ìs_symlink()`| enlace simbólico|
|`ìs_junction()`||
|`ìs_mount()`| punto de montaje |
|`ìs_socket()`| socket UNIX|
|`ìs_fifo()`| cola|
|`ìs_block_device()`|dispositivo "de bloque": HDD, SDD, CD, etc|
|`ìs_char_device()`|dispositivo "de caracter": mouse, teclado, joystick, placa audio |

La ruta indicada puede ser perteneciente a enlaces simbólicos al elemento elegido.

<!-- 
Ejemplo de uso: unidad `C:\\` en Windows

```py
montado = Path("C:\\").is_mount()
``` 
-->