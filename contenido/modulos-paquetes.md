<a name="top"></a>

## [Volver](../Python.md#modulos-y-paquetes)

# Módulos y Paquetes

## Módulos

Los programas a medida que crecen se dividen en módulos para facilitar el diseño, el mantenimiento y la reutilización. Un módulo es un archivo Python que contiene definiciones y sentencias relacionados. Para utilizar los módulos primero hay que importarlos.

La importación es una sentencia que da acceso a las funciones y constantes definidas en el módulo especificado
```python
import <modulo>
```
Las importaciones se hacen al comienzo del programa. 

Las funciones del módulo importado se usan así:

```python
<modulo>.<funcion>(<argumento>)
```
Las constantes se acceden así:

```python
<modulo>.<constante>
```
Al módulo se lo puede importar y asignarle un nombre alternativo dentro del programa:
```python
import <modulo> as <alias_modulo>
```
esto permite usar alias más cortos para usar sus componentes:
```python
<alias>.<constante>
<alias>.<funcion>(<argumento>)
```
Para importar un elemento específico de un módulo se puede usar la sentencia:
```python
from <modulo> import <elemento>
```
Los elementos también se pueden importar con nuevo nombre:
```python
from <modulo> import <elemento> as <alias_elemento>
```

Una mala práctica muy habitual es importar un módulo con la sentencia:
```python
from <modulo> import *
```
Ésta permite llamar a los elementos del módulo pero sin mencionarlo. Puede dar lugar a conflictos al llamar a múltiples módulos.

Ejemplo de uso:  módulo *request* (interactía con API's de servidores remotos para hacer consultas)
```python
import requests
respuesta = requests.get( "https://pokeapi.co/api/v2/pokemon?limit=151")
```

### Módulos Disponibles: Biblioteca Estándar
https://docs.python.org/es/3/library/index.html


## Paquetes externos: PIP
PIP es el "Indice de Paquetes de Python". Es un repositorio oficial para instalar dependencias (*"paquetes"*).

Comandos útiles para manejar paquetes:
```bash  
pip install paquete     # instalar paquete (más reciente)
pip show paquete        # mostrar data del paquete
pip uninstall paquete   # desinstalar paquete
pip list                # enumerar paquetes instalados
```
Opciones para manejar versiones de paquetes:
```bash  
pip install paquete==     # enumerar versiones online del paquete
pip install paquete==<version>    #instalar version especificada
pip install paquete>=<version>    #instalar version especificada o más reciente
```
Listado de dependencias e instalacion desde las mismas:
```bash  
# guardado en texto de paquetes actuales y su versión actual
pip freeze > requirements.txt
# instalacion desde archivo
pip  install -r requirements.txt
```
Actualizacion de PIP:
```bash
pip install pip    
pip install --upgrade pip   # actualizar PIP
pip --version               # version PIP actual  
```

Para actualizar los paquetes se puede usar el paquete auxiliar pip-review:

```bash
pip install pip-review
pip-review --local --interactive
```

Ubicacion de paquetes locales:
```bash
python -m site --user-site
```
El manejo de los paquetes ya instalados es idéntico al de los módulos. 

Para usar el paquete se importa haciendo:

```python
import <mi_paquete>
```

Si sólo se necesita usar algunas funciones (o submódulos) del paquete se usa:

```python
from <mi_paquete> import <mi_archivo_funciones>
```

A los paquetes también se les puede poner alias en el programa:

```python
import <mi_paquete> as <alias>
```
Ejemplo resumen: importando Rich (paquete de cosméticos para la consola).
```python
# alias para el paquete
import rich as r
r.print("[bold yellow]Textos enriquecidos!")

# sustitucion de funciones
from rich import print
print("[bold green]Funcion 'print' sustituida")

# renombrado funciones
from rich import print as rprint
rprint("[bold cyan]Funcion 'print' renombrada")
```

## Crear módulos

Los módulos se crean dentro de archivos con ***extensión .py***, a menudo dentro de ***subdirectorios***.   

Las barras(**/**) de la ruta de archivo se reemplazan por **puntos** y del nombre de archivo **se omite** la extension .py.

Entonces, para importar un archivo Python como módulo desde un subdirectorio de la ruta actual la notación queda:
```python
import <subdirectorio>.<archivo> as <alias>     # importar todo con alias
from <subdirectorio>.<archivo> import *    # Importar todo
from <subdirectorio>.<archivo> import <elemento>, <funcion>, <Clase>       # importar elementos particulares
```

Asimismo los módulos pueden tener dependencias con otros archivos de módulo. Para poder importarlos se toma como referencia la ruta del archivo de módulo y de ahí se toma la ruta relativa. Sintaxis:

```python
# importaciones con rutas relativas
from . import <modulo_A>  # actual directorio
from .. import <modulo_B> # directorio padre
from ..<alterno> import <modulo_C> # directorio aledaño
```
**Importante:** El uso de las rutas relativas es motivo de debate respecto de las buenas prácticas y suele ser origen de múltiples problemas de dependencias.

Si el archivo del módulo tiene código para ejecutar (por ejemplo, un demo o un test) esto se realiza mediante la sintaxis:

```bash
py -m directorio.archivo    # ejecucion módulo
```

Es habitual colocar archivos llamados '**\_\_init\_\_.py**' al lado de los archivos de módulo, los cuales ***pueden estar vacíos***. Sin embargo, en ellos se puede especificar qué elementos de los módulos se deben exportar cargando el objeto **\_\_all\_\_** :

```python
## archivo '__init__.py'
__all__ = [
    "<modulo1>",      # archivo 'modulo1.py'
    "<modulo2>",      # archivo 'modulo2.py'
]
```
De esta forma, si un archivo aledaño intenta importar todo:
```python

from <directorio> import *  # importa 'modulo1.py' y'modulo2.py'
```
Esto importará solamente a estos dos módulos especificados en '**\_\_init\_\_.py**' incluso si hay otros módulos en el directorio.


## Crear paquetes

Para crear un paquete se puede crear una carpeta con el nombre del paquete e introducir:
- Un archivo vacío llamado '**\_\_init\_\_.py**' ***dentro de cada subdirectorio*** incluido dentro del paquete;
- Uno (o varios) **archivos** de Python con las funciones , constantes etc añadidos;
- Un archivo '**setup.py**' para crear el archivo comprimido con el paquete, el cual tendrá terminación ***zip*** en Windows ó ***tar.gz*** en GNU/Linux.

El proceso se explica más facilmente mediante ejemplos:

1. Supongamos la creación de un paquete llamado "mipak" compuesto por un único script. Para ello se colocan en un mismo directorio los siguientes tres archivos:

    ```bash
    __init__.py     # archivo vacío
    mipak.py        # archivo con todo el contenido del paquete: funciones, clases, etc
    setup.py        # archivo instalacion
    ```

    El archivo de Python *setup.py* tendrá todas las configuraciones pertinentes:


    ```python
    # archivo 'setup.py' aledaño al script 'mipak.py'
    from setuptools import setup

    setup(
        name="mipak",    # nombre dek paquete, se usará para instalar e importar   
        version="0.3",   # numero de version, útil para gestionar las actualizaciones
        # info para la publicación online (opcional)
        description="Paquete con script único",
        author="Yo",
        author_email="yo@miserver.yo",
        url="http://miurl.com",
        # informacion de la composicion (importante)
        packages=['.'],                 # Ruta del directorio del paquete
        scripts=['mipak.py']            # Nombre script -- DEBE COINCIDIR con el nombre de paquete
    )
    ```
    El paquete comprimido se crea ejecutando el archivo de setup con la opcion **sdist**:  

    ```bash
    python setup.py sdist 
    py setup.py sdist           #version  abreviada
    ```
    Se creará un archivo comprimido (*zip* en Windows, *tar.gz* en Linux) con todo el contenido del paquete. Éste se encuentra en el subdirectorio */dist*.

    La instalación local del paquete se hará con el comando **pip install**. En el ejemplo:
    ```bash
    pip install dist/mipak-0.3.tar.gz       # instalación local
    ```
    Para poder usar este módulo en los scripts la importación se hace como:

    ```python
    import mipak
    ```

2.  Tómese por referencia el [ejemplo online de Hektorprofe](https://docs.hektorprofe.net/python/modulos-y-paquetes/paquetes/) de un paquete con dos submódulos:


    ```bash
    paquete/
        __init__.py     # archivo vacío
        hola/
            __init__.py     # archivo vacío   
            saludos.py 
        __init__.py     # archivo vacío
        adios/
            __init__.py     # archivo vacío   
            despedidas.py   

    setup.py        # archivo instalacion
    ```
    A este paquete le corresponde un 'setup.py' como el siguiente:

    ```python
    from setuptools import setup
    
    setup(
        name="paquete",
        version="0.1",
        description="Este es un paquete de ejemplo",
        packages=['paquete','paquete.hola','paquete.adios'], # Rutas del directorio y subdirectorios 
        scripts=[]                  # queda vacío
    )
    ```    
    Los pasos siguientes son empaquetar e instalar, tal como antes:
    ```bash
    py setup.py sdist                       # crear paquete
    pip install dist/paquete-0.1.tar.gz     # instalación local
    ```
    En este caso la importación deberá dar cuenta de toda la ruta de archico. Por ejemplo:
    ```python
    import paquete.hola.saludos     as saludos
    import paquete.adios.despedidas as despedidas
    ```
3. Si del ejemplo previo se eliminaran las subcarpetas pero se dejaran ambos scripts:
    ```bash
    paquete/
        __init__.py     # archivo vacío 
        saludos.py 
        despedidas.py   

    setup.py        # archivo instalacion
    ```
    al paquete le correspondería un 'setup.py' como el siguiente:

    ```python
    from setuptools import setup
    
    setup(
        name="paquete",
        version="0.2",
        description="Este es un paquete de ejemplo",
        packages=['paquete'],       # Ruta del directorio 
        scripts=[]                  # queda vacío
    )
    ```   
    El empaquetado  e instalacion son analogos al caso previo:
    ```bash
    py setup.py sdist                       # crear paquete
    pip install dist/paquete-0.2.tar.gz     # instalación local
    ```
    Y la importación queda como:
    ```python
    import paquete.saludos    as saludos
    import paquete.despedidas as despedidas
    ```

Links útiles:


https://docs.hektorprofe.net/python/modulos-y-paquetes/paquetes/

----
----
----


## [Inicio](#módulos-y-paquetes)

## [Volver](../Python.md#modulos-y-paquetes)