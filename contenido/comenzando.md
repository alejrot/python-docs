<a name="top"></a>

## [Volver](../Python.md#comenzando-con-python)

# Comenzando con Python


## Archivos y Ejecución

Los programas escritos en lenguaje Python se guardan en archivos de texto con extensión '*.py*'.

Para ejecutar las rutinas mediante intérprete desde la consola  se usa el comando 'python':

```bash
python  <nombre_archivo>.py
python3 <nombre_archivo>.py 
```
La versión más usada actualmente de Python es la versión 3; sin embargo todavía existe código *legacy* (no mantenible) en la versión 2. Según el sistema operativo y la versión de Python instalada puede requerirse un comando o el otro.

Desde la versión 3.10 se añadió el comando 'py' como abreviación del comando del intérprete:

```bash
py <nombre_archivo>.py
```

## Escribir en pantalla

El primer programa más habitual es el 'HelloWorld!', un programa que escribe un mensaje en consola. En Python los mensajes se escriben en pantalla con la función **print()**:

```python
print("¡Hola Mundo!")
print('Mi primera rutina en Python')
```

Python verifica la ***indentación*** (es decir, los espacios a izquierda) de las instrucciones para determinar las jerarquías y los controles de flujo dentro de los programas (esto se verá más adelante). Por ello debe tenerse cuidado de no dejar distintos espacios a izquierda de las instrucciones excepto cuando estas lo requieren. 

Ejemplo: un error debido a un indentado no consistente
```python
print("¡Hola Mundo!")
  print('Mi primera rutina en Python') # da IndentationError
```


## Comentarios 
Los comentarios de una línea son precedidos por el símbolo numeral (**#**).
```python
# Comentario, una linea
```
Los comentarios de múltiples líneas empiezan precedidos con tres comillas y terminan en tres comillas (**“”””**): 

```python
"""
Comentario, 
varias lineas
"""
```
Usar triple comilla simple (**\'\'\'**) antes y después de los comentarios también sirve para documentar:
```python
'''
Comentario, 
varias lineas
'''
```

## Documentación - MarkDown

MarkDown facilita crear codigos de texto remarcados según el lenguaje usado. Es un formato muy utilizado para documentar  código de software en archivos con extensión '.md'.

Usando triple comilla inclinada rodeando el bloque de código y la palabra 'python' como se muestra: 

    ```python
    # Código Python
    # ...
    ```

entonces el intérprete de MarkDown da estilo al bloque:

```python
# Código Python
# ...
```
Este documento presente usa extensivamente esta propiedad.


## Scripts ejecutables

Para convertir los archivos de Python en scripts ejecutables se puede incluir dentro del mismo archivo de programa un 'shebang' de modo análogo al usado en los scripts de Bash:
```python
#!/usr/bin/env python
print("¡Hola Mundo!")
```
Este realiza el llamado al intérprete de Python desde el mismo archivo. 

De este modo se puede ejecutar la rutina del archivo desde la consola directamente, poniendo punto y barra adelante del nombre:
```bash
./<nombre_archivo>.py
```
También se podrá ejecutar la rutina con doble click sobre el archivo; sin embargo esto puede no abrir la terminal (o cerrarla muy rápidamente).

**Importante:** Es posible que se requiera darle permisos de ejecución al archivo. Esto puede hacerse desde la terminal con el comando *chmod* o bien afectando las propiedades con clik derecho en el entorno gráfico del sistema operativo.

Asignar permisos de ejecucion desde la terminal:
```bash
chmod +x <archivo.py>
```

## Compilación

Hay varias herramientas para compilar el código, es decir para crear archivos ejecutables. Algunas de ellas son:
- py2exe;
- pyinstaller;
- Codon;
- etc.

Cada una de ellas tiene sus propiedades, distintos tipos de licencia, distintos sistemas operativos de destino, etc.


## Uso en Consola

Las instrucciones de Python se puede ejecutar escribiendo en la terminal en tiempo real. Para ello se invoca al intérprete de Pyhton desde la terminal usada:

```bash
python
py
```

Entonces se imprime la información de la actual versión de Python y del sistema operativo actual. Cada nueva linea de la terminal comienza con **\>\>\>** indicando que el intérprete de Python está abierto. Cada nueva línea de código se cierra pulsando la tecla ***'Enter'***.


Ejemplo: definir una variable en vivo y sumarle 1
```python
>>> x=3
>>> x+1
```
Resultado en pantalla:
```bash
>>> x=3
>>> x+1
4
```

Para salir del intérprete hay que escribir **exit()** ó **Ctrl + 'Z'** (en Linux)



## [Inicio](#comenzando-con-python)

## [Volver](../Python.md#comenzando-con-python)