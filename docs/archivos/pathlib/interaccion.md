---
tags:
  - Archivos
  - Carpetas
  - Rutas
  - Pathlib
---

# Interaccion con el sistema 

Pathlib incluye funcionalidades para explorar directorios,
modificar los "ficheros" (carpetas y archivos),
etcétera.




### Buscar y comprobar archivos y directorios


#### Busqueda de archivos y carpetas - *iterdir()*

```python title="Búsqueda simple"
ruta_carpeta: str
objeto_ruta = Path(ruta_carpeta)

objeto_busqueda = objeto_ruta.iterdir()
rutas_internas = list(objeto_busqueda)
```

#### Explorar todo - *walk()*

```python title="Búsqueda recursiva"
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


```python title="Búsqueda por patrón"
ruta:_directorio: str
patron: str

objeto = pathlib.Path(ruta_directorio).glob(patron)    # busqueda 
objeto = pathlib.Path(ruta_directorio).rglob(patron)   # busqueda recursiva

lista_rutas = list(objeto)      # resultado
```

Ejemplo de uso: busqueda recursiva de imagenes .png y .PNG

```python title="Ejemplo: búsqueda de imagenes .png y .PNG"
objeto = pathlib.Path(ruta).rglob("*.png", case_sensitive=False)
lista_imagenes = list(objeto) 
```

#### Comparar rutas - *samefile()*

```python title="Comparar rutas"
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

```python title="Ejemplo: comparando rutas"
# comparando directorio actual
ruta_actual = pathlib.Path().cwd()
iguales = pathlib.Path(ruta_actual).samefile("")  # 'True'

# comparando directorio padre
ruta_padre = pathlib.Path().cwd().parent
iguales = pathlib.Path(ruta_padre).samefile("../") # 'True'
```


#### Estadisticas de archivo - *stat()*

Provee información variada sobre la ruta: fechas de creacion y modificacion, espacio en disco, identificadores de usuario y de grupo, etc. 

Uso:
```python title="Estadisticas de archivo"
estadisticas = Path(ruta).stat()
```
Algunos atributos internos:

```python title="Datos de archivo"
# identificadores (ID)
estadisticas.st_uid     # identificador d usuario
estadisticas.st_gid     # identificador de grupo
# espacio disco (si es carpeta no incluye contenido)
estadisticas.st_size    # espacio disco en bytes 
# fechas - formato POSIX
estadisticas.st_ctime   # creacion
estadisticas.st_mtime   # ultima modificacion
estadisticas.st_atime   # ultimo acceso
```



#### Convertir rutas - *absolute()*

```python title="Conversión a ruta absoluta"
# Objeto 'Path'
nombre_archivo = objeto_ruta.absolute() # conversion a ruta absoluta
```

Ejemplo de uso: ruta del directorio con el ejecutable
```python title="Ruta absoluta actual"
# ruta directorio de ejecución actual
nombre_archivo = Path("").absolute()
```

#### Usuarios y grupos - *owner() y group()*

```python title="Propietario y Grupo"
usuario_propietario         = objeto_ruta.owner()
grupo_usuario_propietario   = objeto_ruta.group()
```

#### Verificar existencia - *exists()*
```python title="Verificar" hl_lines="1"
existe = Path(ruta).exists()
```


#### Cambio permisos - *chmod()*
```python title="Cambiar permisos" hl_lines="2"
numero_permisos: int    # numero en octal o hexadecimal
Path(ruta).chmod(numero_permisos)       # ver anexo sobre permisos
```

Ejemplo uso:
```python title="Ejemplo: cambiar permisos" hl_lines="3"
# Usuario actual: leer y escribir
# otros: solo leer
Path(ruta).chmod(0o644)
```


### Archivos

#### Objeto para ruta archivo

```python title="Path archivo" hl_lines="3"
ruta_archivo: str 
# Objeto 'Path'
objeto_archivo = pathlib.Path(ruta_archivo)
```


#### Crear, verificar y eliminar - *touch(), is_file() y unlink()*
```python title="Manipular archivos" hl_lines="3-6  8  12"
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
```python title="Leer y escribir texto" hl_lines="2 4"
# lectura
texto = objeto_archivo.read_text()
# escritura/sobreescritura
nro_caracteres = objeto_archivo.write_text('contenido de archivo.')
```

#### Lectura y escritura binaria - *read_bytes() y write_bytes()*
```python title="Leer y escribir bytes" hl_lines="2 4"
# lectura
data_binarios = objeto_archivo.read_bytes()
# escritura/sobreescritura
nro_bytes = objeto_archivo.write_bytes(b'contenido de archivo.')
```

### Directorios

#### Objeto para ruta de directorio

```python title="Path directorio" hl_lines="3"
ruta_directorio: str 
# Objeto 'Path'
objeto_directorio = Path(ruta_directorio)
```


#### Manipular carpetas - *mkdir(), is_dir() y rmdir()*


```python  title="Manipular carpetas" hl_lines="4-8  10 12"
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

```python title="ruta 'home'" hl_lines="1"
carpeta_usuaurio = pathlib.Path().home()   # carpeta personal del usuario actual
```

#### Carpeta actual del programa - *cwd()*
```python title="ruta actual" hl_lines="1"
carpeta_programa = pathlib.Path().cwd()   # carpeta actual del programa
```


