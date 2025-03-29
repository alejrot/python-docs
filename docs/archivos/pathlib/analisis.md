---
tags:
  - Archivos
  - Carpetas
  - Rutas
  - Pathlib
---

# Análisis y Composición



## Importación y creación de objetos

La funciones del módulo `pathlib` 
crean objetos para cada ruta que se le indique:

=== "Path"

    ```python title="Objetos Path"
    from pathlib import Path

    ruta: str 
    objeto_ruta      = Path(ruta)       # funcionalidad completa
    ```


=== "PurePath"

    ```python title="Objetos Path"
    from pathlib import PurePath

    ruta: str 
    objeto_ruta = PurePath(ruta)        # funcionalidad recortada
    ```

Estos objetos incluirán los métodos necesarios para trabajar con las rutas de entrada.

<!-- 
Como alternativa se pueden usar los métodos como si fueran funciones.
 -->

!!! info "Resultados según SO"

    Los resultados de usar algunos métodos de `Path()` y de `PurePath()` pueden variar en función del sistema operativo anfitrión.
    En tal caso es conveniente usar sus versiones exclusivas de Windows o de POSIX, según sea la ruta a trabajar (ver más adelante).


## Archivos y carpetas 

### Archivos

Los objetos así creados
traen los siguientes campos informativos de archivo:

|atributo archivo| significado|
|---|---|
|`name`| nombre completo del archivo|
|`suffix`|    extensíón (*sufijo*)|
|`suffixes`| lista de extensiones - habituales en POSIX|
|`stem`| nombre - sin extension de archivo|

Supóngase por ejemplo la ruta de archivo `/home/user/pack.tar.gz`:

```python 
from pathlib import PurePath

path_archivo = PurePath("/home/user/pack.tar.gz") 
```
Entonces al consultar estos atributos se leerá:

```python title="Archivo en ruta"
archivo = path_archivo.name       # 'pack.tar.gz'
sufijo  = path_archivo.suffix     # '.gz'
sufijos = path_archivo.suffixes   # '['.tar', '.gz']'
nombre  = path_archivo.stem       # 'pack.tar'
```

### Directorios

También se suministra información de las carpetas que conforman la ruta:


|atributo carpeta| significado|
|---|---|
|`parent`| carpeta inmediatamente superior |
|`parents`| arreglo de carpetas superiores (símil lista)  |
|`parts`| descomposición de ruta en partes - formato tupla |


Retomando el ejemplo previo:

```python title="Carpetas en ruta"
carpeta = path_archivo.parent       # PurePosixPath('/home/user')
carpeta = path_archivo.parents[0]   # PurePosixPath('/home/user')
carpeta = path_archivo.parents[1]   # PurePosixPath('/home')
carpeta = path_archivo.parents[2]   # PurePosixPath('/')

lista_partes = path_archivo.parts      # ('/', 'home', 'user', 'pack.tar.gz')
```
Nótese que la ruta de las carpetas es devuelta en formato `PurePosixPath` o el que corresponda al caso.
Éste se convierte a *string* con la función `str()` sin problemas. 




## Rutas absolutas y relativas

### Rutas abolutas

Se dispone del método `is_absolute()` para verificar que la ruta indicada sea absoluta. Es recomendable usar este método desde las funciones 
`PureWindowsPath` y `PurePosixPath`.


```python title="Verificación rutas absolutas"
from pathlib import PurePosixPath, PureWindowsPath

es_absoluta = PurePosixPath("/home").is_absolute()     # 'True'
es_absoluta = PurePosixPath("../").is_absolute()   # 'False'

es_absoluta = PureWindowsPath("c:\\windows").is_absolute()    # 'True'
es_absoluta = PureWindowsPath("..\\Documentos").is_absolute() # 'False'
```

Si se usa en cambio `Path()` o `PurePath()` hay que tener cuidado con el sistena operativo anfitrion porque en base a éste se puede descartar rutas absolutas de otros sistemas operativos:

=== "Windows"

    ```python title="Ambigüedad de verificacion"
    from pathlib import PurePath

    # Sistema WINDOWS
    es_absoluta = PurePath("/home"      ).is_absolute()    # 'False' 
    es_absoluta = PurePath("c:\\windows").is_absolute()    # 'True'
    ```

=== "POSIX"

    ```python title="Ambigüedad de verificacion"
    from pathlib import PurePath

    # Sistema POSIX: MAC, UNIX, LINUX
    es_absoluta = PurePath("/home"      ).is_absolute()    # 'True' 
    es_absoluta = PurePath("c:\\windows").is_absolute()    # 'False'
    ```


### Relacion entre rutas 

El método `is_relative_to()` es el encargado de verificar que dos rutas sean relativas entre sí.
Aquí también se recomienda usar el método desde las funciones 
`PureWindowsPath` y `PurePosixPath`:


```python title="Verificación rutas relativas"
from pathlib import PurePosixPath, PureWindowsPath
# Rutas POSIX exclusivamente
relativos = PurePosixPath("home/user").is_relative_to("home")    # 'True'
relativos = PurePosixPath("home/user").is_relative_to("user")    # 'False'

# Rutas Windows exclusivamente
x = PureWindowsPath("c:\\windows\\win32").is_relative_to("c:\\")    # 'True'
x = PureWindowsPath("c:\\windows\\win32").is_relative_to("windows") # 'False'
```

Nuevamente, existe el riesgo de resultados ambigüos al usar `Path()` o `PurePath()` para crear el objeto de ruta:

=== "Windows"

    ```py title="Ambigüedad de verificacion - relativos"
    from pathlib import PurePath

    relativos = PurePath("home/user").is_relative_to("home")             # 'False' 
    relativos = PurePath("c:\\windows\\win32").is_relative_to("c:\\")    # 'True'
    ```

=== "POSIX"

    ```py title="Ambigüedad de verificacion - relativos"
    from pathlib import PurePath

    relativos = PurePath("home/user").is_relative_to("home")             # 'True'  
    relativos = PurePath("c:\\windows\\win32").is_relative_to("c:\\")    # 'False'
    ```


## Composicion de rutas 


Las funciones del módulo permiten componer rutas nuevas
a partir de varios *strings*
separados con comas:


=== "POSIX"

    ```python title="Composición rutas - función"
    compuesta = PureWindowsPath("C:\\", "windows")  # 'PureWindowsPath('C:/windows')'
    compuesta = PurePosixPath("home", "user")       # 'PurePosixPath('home/user')'
    ```

Además se cuenta con el método `joinpath()`
para la misma función:


=== "POSIX"

    ```python title="Composición rutas - método joinpath"
    compuesta = PureWindowsPath("C:\\").joinpath("windows") # 'PureWindowsPath('C:/windows')'
    compuesta = PurePosixPath("home").joinpath("user")      # 'PurePosixPath('home/user')'
    ```

!!! tip "Formato de la ruta"

    Debe notarse que el formato de las rutas mostrado
    se "adapta" al del sistema operativo anfitrión.

    Por ejemplo: la ruta `C:\\windows` se ve en entornos Linux como `C:/windows`.