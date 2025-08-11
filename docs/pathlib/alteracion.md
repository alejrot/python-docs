---
tags:
  - Archivos
  - Carpetas
  - Rutas
  - Pathlib
---


# Alteración de recursos

`Path()` pueden crear, modificar y eliminar tanto carpetas como archivos.

En todo este capítulo se asume el uso de la función `Path()`
la cual se importa para su uso:

```py title="Path - Importación"
from pathlib import Path
```


## Cambio de permisos 

Cada recurso posee unos permisos de lectura, escritura y ejecución
los cuales no son iguales para todos los usuarios.
Estos permisos son representados por un número,
el cual se asigna con el método `chmod()`.

```python title="Cambiar permisos" hl_lines="2"
numero_permisos: int   
Path(ruta).chmod(numero_permisos)       # ver anexo sobre permisos
```

Ejemplo uso: 
```python title="Ejemplo: cambiar permisos"
# Usuario propietario: leer y escribir
# otros: solo leer
Path(ruta).chmod(0o644)
```

!!! info "Número de permisos"

    En [**este anexo**](../anexos/permisos.md) se explica cómo se compone el número de los permisos.


## Archivos

### Crear 


El método `touch()` es el encargado de crear nuevos archivos.
Estos se crean vacíos:

```python title="archivos - creación"
Path(ruta_archivo).touch()
```
Por defecto los archivos tienen permisos de lectura y escritura y,
en caso de existir un archivo con igual ruta,
se preserva el original. 
Esto puede modificarse con los argumentos `mode` (permisos) y `exists_ok`.

|argumentos| significado|
|:---|:---|
| `mode`   | número de permisos de usuario: lectura y escritura (ver anexo)|
| `exist_ok` | evita error por sobreeescritura|


### Manejo de texto

La lectura de archivo como texto
se realiza con el método `read_text()`:

```python title="archivos de texto - lectura"
texto = Path(ruta_archivo).read_text()
```

Su método complementario es `write_text()`:


```python title="archivos de texto - lectura"
texto: str
numero_caracteres = Path(ruta_archivo).read_text(texto)
```
el cual devuelve cuántos caracteres fueron escritos.
El contenido original se sobreescribe con cada llamado.


Ambos métodos tienen los siguientes argumentos opcionales:

|argumento| significado|
|----|----|
|`encoding`|tipo codificación: `utf-8`, `utf-16`, etc|
|`errors`||
|`newline`||



### Manejo de binarios


La lectura en formato binario
se realiza con el método `read_bytes()`:

```python title="archivos - lectura binaria"
cadena_bytes = Path(ruta_archivo).read_bytes()
```

y su contraparte es `write_bytes()`,
la cual reescribe el contenido interno de archivo. 

```python title="archivos - escritura binaria"
nro_bytes = Path(ruta_archivo).write_bytes(b'contenido de archivo.')
```

Estos métodos no tienen argumentos.

### Mover

El método `rename()` permite cambiar el nombre de archivo 
y también permite su reubicado:

```python title="archivos - renombrar"
nueva_ruta = Path(ruta_archivo).rename(ruta_destino)
```

Este método presupone que la ruta destino aun no exisye.
Si lo hace, el resultado varía de los permisos del programa
y del sistema operativo.


### Reemplazar

El método `replace()` permite sustituir un archivo
ubicado en la ruta de destino
por el archivo de la ruta original:

```python title="archivos - reemplazo"
nueva_ruta = Path(ruta_archivo).replace(ruta_destino)
```

Este método asume que el archivo de destino ya existe.


### Eliminar

Los archivos se eliminan con el método `unlink()`:

```python title="archivos - borrado"
Path(ruta_archivo).unlink(missing_ok=True) # elimina archivo (si existe)
```
Si se omite el argumento `missing_ok`
y el archivo no existe el método arrojará error.


## Directorios

### Crear

Los directorios se crean con el método `mkdir()`:

```python title="directorios - creación"
Path(ruta_carpeta).mkdir()
```

Este método tiene las siguientes opciones:

|argumentos| significado|
|:---|:---|
| `mode`   | número de permisos de usuario: todos por defecto (ver anexo)|
| `parents` | crea los directorios padre si éstos no existen|
| `exist_ok` | evita error por sobreeescritura|



### Eliminar


Con `rmdir()` se borra la carpeta elegida:

```python title="directorios - borrado"
Path(ruta_carpeta).rmdir()
```

Dicha carpeta debe estar vacía.

