
# Tempfile - Archivos Temporales

Python tiene un módulo específico para manejar archivos y directorios temporales. Este módulo se llama **temptfile**, el cual debe ser importado para su uso: 

```python
import tempfile
```



## Archivos con nombre 

Los archivos temporales se crean con la función **NamedTemporaryFile()**:

```python
# Crear un archivo temporal con nombre 
archivo_temporal = tempfile.NamedTemporaryFile( 
        mode   = "w+b", # modo de apertura
        prefix = "",    # parte del nombre de archivo
        suffix = "",    # extensión de archivo
        delete = True   # si se cierra el archivo se elimina el archivo
        )
```
Esta funcion crea un descriptor de archivo , el cual no tiene contenido. Los parámetros *mode*, *delete* y *prefix* son opcionales y se pueden omitir. En cambio *suffix* puede ser necesario para especificar el formato de los datos mediante la extensión de archivo.

Para conocer el nombre de archivo asignado  y poder interactuar con él se usa el método  **.name**:

```python
nombre_archivo = archivo_temporal.name
```
Cabe señalar que el nombre de archivo incluye caracteres aleatorios entre lso campos prefix y suffix, por ello éstos no son obligatorios. El archivo **no** puede ser renombrado una vez creado.

La asignación de datos se realiza con el método .write():
```python
nombre_archivo.write( contenido)
```

El archivo temporal se elimina tan pronto se produzca el cierre del archivo temporal. Para alterar este comportamiento existe el parámetro *delete*:

```python
# Crear un archivo temporal con nombre 
archivo_temporal = tempfile.NamedTemporaryFile(delete = False)
```
En este caso el archivo temporal seguirá existiendo hasta su eliminación por el sistema operativo o hasta el reinicio del sistema. Para programar la eliminación del archivo se puede recurrir a la funcion *unlink()* del módulo *os*:
```python
import os

os.unlink(archivo_temporal.name)
``` 

Ejemplo aplicado: guardar un archivo de imagen PNG como archivo temporal


1.  Creación de archivo temporal

    ```python
    # Crear un archivo temporal con nombre 
    archivo_temporal = tempfile.NamedTemporaryFile( prefix="", suffix=".png")
    ```

2. Asignación de datos

    A. Uso de la función open() para leer data binaria:

    ```python
    # apertura archivo en modo lectura binaria
    archivo_disco = open('imagen.png', "rb")
    data = archivo_disco.read()

    # Asignacion de data al archivo
    archivo_temporal.write( data )
    archivo_temporal.seek(0)
    ```

    B. Delegar la transferencia de datos a bibliotecas específicas. Ejemplo: OpenCV
    ```python
    import cv2 as cv    # importacion OpenCV

    img = cv.imread('imagen.png') #lectura desde disco
    cv.imwrite(archivo_temporal.name, img) # escritura en RAM
    ```
    **Importante:** Para usar esta opción se necesita especificar correctamente el parámetro *suffix* al crear el archivo temporal




## Ubicacion de archivos temporales en el sistema

En GNU/Linux los archivos temporales se encuentran dentro del directorio **/tmp**.
Éstos pueden listarse en consola con dos comandos:

```bash
cd  /tmp
ls
```

En el caso de Windows los archivos temporales solían encontrarse en la carpeta '**Temp**' dentro de la carpeta de Windows. La lista desde consola se hace con:

```bash
cd 'C:\Windows\Temp'
ls
```
Windows 10 movió la ruta de los archivos temporales a la carpeta '**\AppData\Local**' dentro de la carpeta del usuario actual: 
```bash
C:\Users\nombre_usuario\AppData\Local\Temp
```


## Enlaces útiles:


[Documentación oficial - Modulo Tempfile](https://docs.python.org/es/3/library/tempfile.html)

[DelfStack - Cómo crear archivos temporales en Python](https://www.delftstack.com/es/howto/python/create-temporary-file-in-python/)


[Aprender Linux - directorio TMP de Linux todo lo que necesita saber](https://aprenderlinux.org/directorio-tmp-de-linux-todo-lo-que-necesita-saber/?expand_article=1)


