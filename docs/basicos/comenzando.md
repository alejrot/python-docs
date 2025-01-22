---
tags:
  - Bash
  - Comentarios
  - Instalacion
  - Interprete
---

# Comenzando con Python


## Instalación

Python utiliza un intérprete específico para hacer funcionar los programas. 
La forma más habitual de uso es instalarlo localmente.

En sistemas Windows la forma más sencilla de instalación es mediante su instalador.
[Descarga desde el sitio oficial de Python](https://www.python.org/downloads/)

En sistemas GNU/Linux el intérprete de Python suele venir preinstalado.
En caso de requerirse la instalación o la actualización esto puede hacerse desde el gestor de paquetes de la distribución o por consola.

Ejemplo: 

```bash title="Instalación - Fedora "
sudo dnf install python   # instalación
sudo dnf update  python   # actualización
```


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

Los comentarios de una línea son precedidos por el símbolo numeral (**`#`**).
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


## Scripts ejecutables

Para convertir los archivos de Python en scripts ejecutables se puede incluir dentro del mismo archivo de programa un 'shebang' de modo análogo al usado en los scripts de Bash:
```python title="Rutinas ejecutables"
#!/usr/bin/env python   # ruta al interprete Python (Linux)
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

