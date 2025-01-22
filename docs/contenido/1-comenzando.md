
# Comenzando con Python


## Archivos y Ejecución

Los programas escritos en lenguaje Python se guardan en archivos de texto con extensión `.py`.

Para ejecutar las rutinas mediante intérprete desde la consola  se usa el comando `python`:

```bash title="ejecutar rutina Python "
python  nombre_archivo.py
python3 nombre_archivo.py 
```
La versión más usada actualmente de Python es la versión 3; sin embargo todavía existe código *legacy* (no mantenible) en la versión 2. Según el sistema operativo y la versión de Python instalada puede requerirse un comando o el otro.

!!! tip "Abreviación comando"

    Desde la versión 3.10 se añadió el comando `py` como abreviación del comando del intérprete:

    ```bash title="ejecutar rutina Python - abreviado"
    py nombre_archivo.py
    ```

## Escribir en pantalla

El primer programa más habitual es el 'HelloWorld!', un programa que escribe un mensaje en consola. En Python los mensajes se escriben en pantalla con la función `print()`:

```python title="Hola mundo"
print("¡Hola Mundo!")
print('Mi primera rutina en Python')
```

Python verifica la ***indentación*** (es decir, los espacios a izquierda) de las instrucciones para determinar las jerarquías y los controles de flujo dentro de los programas (esto se verá más adelante). Por ello debe tenerse cuidado de no dejar distintos espacios a izquierda de las instrucciones excepto cuando estas lo requieren. 

Ejemplo: un error debido a un indentado no consistente
```python title="Error indentado"
print("¡Hola Mundo!")
  print('Mi primera rutina en Python') # da IndentationError
```


## Comentarios 
Los comentarios de una línea son precedidos por el símbolo numeral (**#**).
```python title="Comentarios simples"
# Comentario, una linea
```
Los comentarios de múltiples líneas empiezan precedidos con tres comillas y terminan en tres comillas (`“”””`): 

```python title="Comentarios multilínea - comillas"
"""
Un comentario, 
varias lineas
"""
```
Usar triple comilla simple (`'''`) antes y después de los comentarios también sirve para documentar:

```python title="Comentarios multilínea - comillas simples"
'''
Un comentario, 
varias lineas
'''
```

## Documentación - MarkDown

MarkDown facilita crear codigos de texto remarcados según el lenguaje usado. Es un formato muy utilizado para documentar  código de software en archivos con extensión `.md`.

Usando triple comilla inclinada rodeando el bloque de código y la palabra `python` (o `py`) como se muestra: 

```markdown title="Código en MarkDown - formato"
  ```python
  # Código Python
  # ...
  ```
```
entonces el intérprete de MarkDown da estilo al bloque:

```python title="Código en MarkDown - resultado"
# Código Python
# ...
```
Este documento presente usa extensivamente esta propiedad.


## Scripts ejecutables

Para convertir los archivos de Python en scripts ejecutables se puede incluir dentro del mismo archivo de programa un 'shebang' de modo análogo al usado en los scripts de Bash:
```python title="Rutinas ejecutables"
#!/usr/bin/env python   # ruta al interprete Python
print("¡Hola Mundo!")
```
Este realiza el llamado al intérprete de Python desde el mismo archivo. El *shebang* debe apuntar a un intérprete de Python instalado en el sistema para que el script funcione.

De este modo se puede ejecutar la rutina del archivo desde la consola directamente, poniendo punto y barra adelante del nombre:
```bash title="Autoejecución"
./nombre_archivo.py
```
También se podrá ejecutar la rutina con doble click sobre el archivo; sin embargo esto puede no abrir la terminal (o cerrarla muy rápidamente).

!!! hint "Permisos de ejecución"
    Es posible que se requiera darle permisos de ejecución al archivo. Esto puede hacerse desde la terminal con el comando *chmod* o bien afectando las propiedades con clik derecho en el entorno gráfico del sistema operativo.

    Asignar permisos de ejecucion desde la terminal:
    ```bash title="Habilitar autoejecución"
    chmod +x nombre_archivo.py
    ```



## Uso en Consola

Las instrucciones de Python se puede ejecutar escribiendo en la terminal en tiempo real. Para ello se invoca al intérprete de Pyhton desde la terminal usada:

```bash title="Uso en consola"
python
py
```

Entonces se imprime la información de la actual versión de Python y del sistema operativo actual. Cada nueva linea de la terminal comienza con ``>>>` indicando que el intérprete de Python está abierto y las instrucciones se cierran pulsando la tecla `ENTER`.

```python title="Uso en consola - Instruccion a instruccion"
>>> instrucccion_1
>>> instruccion_2
>>> ....
```


!!! example "Ejemplo: definir una variable en vivo y sumarle 1"
    ```python 
    >>> x=3   # asignacion
    >>> x+1   # incremento
    ```
    Resultado en pantalla:
    ```bash 
    >>> x=3
    >>> x+1
    4
    ```

Para salir del intérprete hay que escribir `exit()` ó `Ctrl + Z` (en Linux)

```bash title="Uso en consola - Salida"
>>> exit()
```

## Compilación

Con el fin de crear archivos ejecutables hay varias herramientas para compilar el código, es decir para crear archivos ejecutables. Algunas de ellas son:

- py2exe;
- pyinstaller;
- Codon;
- etc.

Cada una de ellas tiene sus propiedades, distintos tipos de licencia, distintos sistemas operativos de destino, etc.



!!! note "Uso interpretado"

    Si bien es posible crear los ejecutables en base a código Python lo más habitual es el uso por interpretado.