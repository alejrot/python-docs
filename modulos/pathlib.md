## [Volver](../README.md#modulo-pathlib)

# Pathlib

### Contenidos:
- [Introducción](#introducción)
- [Análisis de rutas](#analisis-de-rutas)
- [Interaccion con el sistema de archivos](#interaccion-con-el-sistema-de-archivos)
    - [Buscar y comprobar archivos y directorios](#buscar-y-comprobar-archivos-y-directorios)
    - [Archivos](#archivos)
    - [Directorios](#directorios)
- [Anexo: permisos de usuario en linux](#anexo-permisos-de-usuario-en-linux)




## Introducción

El **módulo pathlib** facilita el manejo de rutas de archivo y también permite interactuar con archivos y directorios reales del sistema de archivos.

```python
import pathlib
```

Hay seis funciones/clases disponibles para trabajar con las rutas:  

- Path() 
    - PosixPath()       : solo rutas Posix (UINIX, Linux, etc)
    - WindowsPath()     : solo rutas Windows
- PurePath()
    - PurePosixPath()   : solo rutas Posix (UINIX, Linux, etc)
    - PureWindowsPath() : solo rutas Windows

La función más importante es ***Path()***, que es la más versatil y permite tanto trabajar con strings que representan rutas arbitrarias como también alterar archivos y carpetas reales del sistema, en tanto que ***PurePath()*** es la **versión recortada** de *Path()* que sólo permite manejar ***strings*** a modo de rutas. Ambas funciones aceptan rutas de Windows y de sistemas POSIX (UNIX, Linux, etc). Estas dos funciones tienen también sus versiones recortadas para uso exclusivo con rutas POSIX y Windows, respectivamente.

Estas funciones pueden importarse de forma aislada para su uso:

```python
from pathlib import Path, PurePath  # todo tipo de rutas
from pathlib import WindowsPath, PureWindowsPath    # solo rutas Windows
from pathlib import PosixPath, PurePosixPath    # solo rutas Linux/MAC/etc
```

**Importante:** Los resultados de usar algunos métodos de Path() y de PurePath() pueden variar en función del sistema operativo anfitrión. En tal caso es conveniente usar sus versiones exclusivas de Windows o de POSIX, según sea la ruta a trabajar (ver más adelante).


**Importante 2:** varias de las funciones del módulo *pathlib* coinciden en nombre con las funciones del modulo **os**, las cuales no necesariamente se usan igual.  

### Objetos Path

La funciones del módulo *pathlib* crean objetos para cada ruta que se le indique:

```python
ruta: str 
objeto_ruta = pathlib.Path(ruta)
objeto_ruta_pura = pathlib.PurePath(ruta) 

```
Estos objetos incluirán los métodos necesarios para trabajar con las rutas.

Como alternativa se pueden usar los métodos como si fueran funciones.

#### Nombre y extensión(es) de archivos - *name, suffix, suffixes, stem*

```python
# Objetos 'Path' y 'PurePath'
nombre_archivo = objeto_ruta.name       # nombre completo
nombre_archivo = objeto_ruta.suffix     # extension archivo
nombre_archivo = objeto_ruta.suffixes   # lista extensiones
nombre_archivo = objeto_ruta.stem       # nombre sin extensión archivo
```


### Analisis de rutas

#### Recorrido de ruta - *parent, parents y parts*

```python
# Objetos 'Path' y 'PurePath'
ruta_carpeta_superior = objeto_ruta.parent     # carpeta inmediatamente superior de la ruta
rutas_carpetas_superiores = objeto_ruta.parents    # todas las carpetas superiores que conforman la ruta 
lista_partes = objeto_ruta.parts       # descomposicion en partes
```

#### Rutas absolutas y relativas - *is_absolute()*
```python
absoluta = PurePosixPath("/").is_absolute()     # 'True'
absoluta = PurePosixPath("../").is_absolute()   # 'False'

absoluta = PureWindowsPath("c:\\").is_absolute()    # 'True'
absoluta = PureWindowsPath("..\\Documentos").is_absolute() # 'False'

# ....
absoluta = PurePath(ruta).is_absolute() # (depende del sistema operativo local)
```

Si se usa *Path()* o *PurePath()* hay que tener cuidado con el sistena operativo anfitrion porque en base a éste se puede descartar rutas absolutas de otros sistemas operativos

```python
# POSIX: MAC, UNIX, LINUX
ruta="/home"
absoluta = PureWindowsPath(ruta).is_absolute()   # 'False'
absoluta = PurePosixPath(ruta).is_absolute()     # 'True'
absoluta = PurePath(ruta).is_absolute() # 'True' solo en POSIX, 'False' en caso contrario

# WINDOWS
ruta="c:\\windows"
absoluta = PureWindowsPath(ruta).is_absolute()   # 'True'
absoluta = PurePosixPath(ruta).is_absolute()     # 'False'
absoluta = PurePath(ruta).is_absolute()     # 'True' solo en Windows, 'False' en caso contrario
```


#### Relacion entre rutas - *is_relative_to()*
```python
# Rutas POSIX exclusivamente
relativos = PurePosixPath("home/user").is_relative_to("home")    # 'True'
relativos = PurePosixPath("home/user").is_relative_to("user")    # 'False'

# Rutas Windows exclusivamente
x = PureWindowsPath("c:\\windows\\win32").is_relative_to("c:\\")    # 'True'
x = PureWindowsPath("c:\\windows\\win32").is_relative_to("windows") # 'False'

# Caso general
relativos = PurePath("home/user").is_relative_to("home")    # Sólo da 'True' en POSIX 
x = PurePath("c:\\windows\\win32").is_relative_to("c:\\")    # Sólo da 'True' en Windows
```


#### Composicion de rutas - *Path(), PurePath() y joinpath()*

```python
ruta_A: str = "home"
ruta_B: str = "user"

objeto_compuesto = PurePath(ruta_A, ruta_B)
objeto_compuesto = PurePath(ruta_A).joinpath(ruta_B)

# conversion a texto
ruta_compuesta = str(objeto_compuesto)  # '/home/user'
```


## Interaccion con el sistema de archivos

### Buscar y comprobar archivos y directorios


#### Busqueda de archivos y carpetas - *iterdir()*

```python
ruta_carpeta: str
objeto_ruta = Path(ruta_carpeta)

objeto_busqueda = objeto_ruta.iterdir()
rutas_internas = list(objeto_busqueda)
```

#### Explorar todo - *walk()*

```python
ruta_carpeta: str
objeto_ruta = Path(ruta_carpeta)

objeto_exploracion = objeto_ruta.walk(top_down=True)
objeto_directorios = list(objeto_exploracion)
# descomposicion en sus partes más elementales
for directorio in objeto_directorios:
    [ruta, subdirectorios, archivos ] = list(directorio)
    print(ruta)
    print(subdirectorios)
    print(archivos)
```


#### Busqueda de patrones - *glob() y rglob()*


```python
ruta:_directorio: str
patron: str

objeto = pathlib.Path(ruta_directorio).glob(patron)    # busqueda 
objeto = pathlib.Path(ruta_directorio).rglob(patron)   # busqueda recursiva

lista_rutas = list(objeto)      # resultado
```

Ejemplo de uso: busqueda recursiva de imagenes png y PNG
```python
objeto = pathlib.Path(ruta).rglob("*.png", case_sensitive=False)
lista_iamgenes = list(objeto) 
```

#### Comparar rutas - *samefile()*

```python
# rutas del sistema (DEBEN existir o da error)
ruta_A: str = "/home"
ruta_B: str = "/etc"

# compara
mismo_ruta = pathlib.Path(ruta_A).samefile(ruta_B) # 'False'   
misma_ruta = pathlib.Path(ruta_A).samefile(ruta_A) # 'True'
```
Nótese que *samefile()* sirve también para directorios.

Este metodo es práctico para comparar rutas relativas con rutas absolutas. 

Ejemplos:

```python
# comparando directorio actual
ruta_actual = pathlib.Path().cwd()
iguales = pathlib.Path(ruta_actual).samefile("")  # 'True'

# comparando directorio padre
ruta_padre = pathlib.Path().cwd().parent
iguales = pathlib.Path(ruta_padre).samefile("../") # 'True'
```


#### Estadisticas - *stat()*

Provee información variada sobre la ruta: fechas de creacion y modificacion, espacio en disco, identificadores de usuario y de grupo, etc. 

Uso:
```python
estadisticas = Path(ruta).stat()
```
Algunos atributos internos:

```python
# identificadores (ID)
estadisticas.st_uid
estadisticas.st_gid
# espacio disco (si es carpeta no incluye contenido)
estadisticas.st_size    # espacio disco en bytes 
# fechas - formato POSIX
estadisticas.st_ctime   # creacion
estadisticas.st_mtime   # ultima modificacion
estadisticas.st_atime   # ultimo acceso
```





#### Convertir rutas - *absolute()*

```python
# Objeto 'Path'
nombre_archivo = objeto_ruta.absolute() # conversion a ruta absoluta
```

Ejemplo de uso: ruta del directorio con el ejecutable
```python
# ruta directorio de ejecución actual
nombre_archivo = Path("").absolute()
```

#### Usuarios y grupos - *owner() y group()*

```python
usuario_propietario         = objeto_ruta.owner()
grupo_usuario_propietario   = objeto_ruta.group()
```

#### Verificar existencia - *exists()*
```python
existe = Path(ruta).exists()
```


#### Cambio permisos - *chmod()*
```python
numero_permisos: int    # numero en octal o hexadecimal
Path(ruta).chmod(numero_permisos)       # ver anexo sobre permisos
```

Ejemplo uso:
```python
# Usuario actual: leer y escribir
# otros: solo leer
Path(ruta).chmod(0o644)
```


### Archivos

#### Objeto para ruta archivo

```python
ruta_archivo: str 
# Objeto 'Path'
objeto_archivo = pathlib.Path(ruta_archivo)
```


#### Crear, verificar y eliminar - *touch(), is_file() y unlink()*
```python
# crea archivo vacio (puede dar error)
objeto_archivo.touch()       
objeto_archivo.touch(
    mode=0o666,     # permisos de usuarios: lectura y escritura por defecto (ver anexo)
    exist_ok=True   # omite error si el archivo ya existe
    )     
# verifica que exista el archivo
existencia = objeto_archivo.is_file()   
if existencia:
    objeto_archivo.unlink() # elimina archivo

objeto_archivo.unlink(missing_ok=True) # elimina archivo si existe
```

#### Lectura y escritura de texto - *read_text() y write_text()*
```python
# lectura
texto = objeto_archivo.read_text()
# escritura/sobreescritura
nro_caracteres = objeto_archivo.write_text('contenido de archivo.')
```

#### Lectura y escritura binaria - *read_bytes() y write_bytes()*
```python
# lectura
data_binarios = objeto_archivo.read_bytes()
# escritura/sobreescritura
nro_bytes = objeto_archivo.write_bytes(b'contenido de archivo.')
```

### Directorios

#### Objeto para ruta de directorio

```python
ruta_directorio: str 
# Objeto 'Path'
objeto_directorio = Path(ruta_directorio)
```


#### Manipular carpetas - *mkdir(), is_dir() y rmdir()*


```python
# crea directorio vacio, opciones predefinidas (puede dar error)
objeto_directorio.mkdir()
# crea directorio vacio
objeto_directorio.mkdir(
    mode=0o777,     # permisos de usuario: todos por defecto (ver anexo)
    parents=True,   # crea los directorios padre si éstos no existen
    exist_ok=True   # evita error por sobreeescritura
    )
# verifica que exista el directorio
existencia = objeto_directorio.is_dir()   
if existencia:
    objeto_directorio.rmdir() # elimina directorio (debe estar vacio)
```

#### Carpeta Usuario - *home()*

```python
carpeta_usuaurio = pathlib.Path().home()   # carpeta personal del usuario actual
```

#### Carpeta del Programa - *cwd()*
```python
carpeta_programa = pathlib.Path().cwd()   # carpeta actual del programa
```


## Pendiente: explorar los symlinks

los symilnks son los enlaces simbólicos de Linux. Son similares a los accesos directos de Windows

 

## Anexo: permisos de usuario en linux

Los permisos de usuario se asignan mediante por un numero binario / octal / hexadecimal de tres digitos. 

### Permisos para acciones

Cada dígito es una composición de banderines que otorgan permisos para leer, escribir y ejecutar. Los valores numéricos equivalentes para cada permiso aslado son:

|Permiso |binario|octal| hexadecimal|
|--- |:---:|:----:|:---:|
| Leer  (r)  |0b100 | 0o4 | 0h4 | 
| Escribir (w) |0b10 | 0o2 | 0h2 | 
| Ejecutar (x) |0b1 | 0o1 | 0h1 | 

Los numeros de los permisos se construyen combinando los numeros previos.

Ejemplos:

|Permiso combinado |binario|octal| hexadecimal|
|--- |:---:|:----:|:---:|
| sólo lectura (r)  |0b100 | 0o4 | 0h4 | 
| lectura y escritura (r+w) |0b110 | 0o6 | 0h6 | 
| lectura, escritura y ejecucion  (r+w+x) |0b111 | 0o7 | 0h7 | 
| sólo ejecucion  (x) |0b001 | 0o1 | 0h1 | 


### Permisos para usuarios

Los digitos con los permisos se asignan con el siguiente orden de usuarios:
- usuario actual;
- grupo del usuario actual;
- todos los usuarios.

Notacion resumida:

|Usuario|Grupo| Todos|
|---|---|---|
| rwx | rwx | rwx |


**Importante:** el usuario administrador (*'root'*) del sistema siempre tiene todos los derechos posibles, por ello no se lo especifica.


**Ejemplo:**
- usuario propietario con todos los permisos; 
- grupo del propietario con lectura y escritura;  
- accesos de sólo lectura para terceros.

Numero permisos:

**0o 111 110 100** (binario)  **|** **0o764** (octal)  **|** **0x764** (hexadecimal)

**Ejemplo 2:** 

Todos los permisos para todos los ususarios (mala práctica). Numero permisos:

**0o 111 111 111** (binario)  **|** **0o777** (octal)  **|** **0x777** (hexadecimal)



## Referencias

[Documentacion oficial del módulo Pathlib](https://docs.python.org/3/library/pathlib.html)



[FreeCodeCamp - crear y remover enlaces simbólicos](https://www.freecodecamp.org/espanol/news/tutorial-de-enlace-simbolico-en-linux-como-crear-y-remover-un-enlace-simbolico/)

----
----
----

## [Inicio](#pathlib) 

## [Volver](../README.md#modulo-pathlib)