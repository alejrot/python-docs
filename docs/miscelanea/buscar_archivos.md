

# Buscar Archivos y Carpetas


## scandir()



```python
from os import scandir, getcwd

ruta = getcwd()
print(ruta)

rutas = scandir(ruta)

for r in rutas:
    # print(r)
    print(r.name, r.is_dir(), r.is_file())
```

La búsqueda es no recursiva


<!-- 
## Path.iterdir()


El método **iterdir()** de la función **Path()** permite buscar archivos

```python
from pathlib import Path
ruta = Path.cwd()

rutas = Path(ruta).iterdir()
print(rutas)
for r in rutas:
    # print(r)
    print(r.name, r.is_dir(), r.is_file())
```
La búsqueda es no recursiva
 -->



## listdir()

La funcion **listdir()** del módulo **os** 

```python
from os import listdir

ruta = "./"
rutas =  listdir(ruta)
```

```python
from os.path import isfile, join
for r in rutas:
    print(r, isfile(join(ruta, r)))
```


## walk() y next() 

```python
from os import walk, getcwd

ruta = getcwd()     #ruta de búsqueda

dir, lista_subdirs, lista_archivos = next(walk(ruta))   
```
La función walk() devuelve un objeto generador. La función next() descompone el objeto en el directorio actual, la lista de subdirectorios y la lista de archivos.

Esta búsqueda es no recursiva.


## glob

La función **glob** del módulo **glob** permite buscar rutas de archivo fácilmente indicando la extensión deseada:

```python
from glob import glob

expr = '**' #todo (incluye carpetas)
expr = '*.*' # archivos con cualquier extensión
expr = '*.txt' # archivos con extensión especifica

lista_rutas = glob(expr)
```
El retorno es una *lista* de *strings*.

La búsqueda es no recursiva; sin embargo la recursividad se puede habilitar con el parámetro *recursive*:

```python
lista_rutas = glob(expr, recursive = True)
```
También se puede habilitar la búsqueda de archivos ocultos con el parámetro: 
```python
lista_rutas = glob(expr, include_hidden = True)
```

# Referencias

https://es.stackoverflow.com/questions/24278/cómo-listar-todos-los-archivos-de-una-carpeta-usando-python

https://www.delftstack.com/es/howto/python/python-directory-exists/#comprobar-si-el-directorio-existe-usando-el-método-pathisdir-del-módulo-os-en-python