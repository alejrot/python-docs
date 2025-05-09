


# Paquetes

Los paquetes son similares a los módulos pero no son componentes oficiales de Python. Además de la importación, los módulos requieren instalación previa para su uso. 



## Instalación


### PIP y Pypi

PIP es el instalador de Paquetes de Python. Se instala automáticamente con el intérprete de Python.

Primeros comandos de PIP:

```bash title="PIP - Instalar y actualizar"
pip install pip             # instalar PIP (normalmente innecesario)
pip --version               # version PIP actual  
pip install --upgrade pip   # actualizar PIP
```

PyPi es el repositorio oficial para obtener y publicar los paquetes. [Sitio oficial de PyPi](https://pypi.org/)


### Instalación de paquetes

Comandos útiles para manejar paquetes:

```bash  title="PIP - Comandos básicos"
pip install paquete     # instalar paquete (más reciente)
pip show paquete        # mostrar data del paquete
pip uninstall paquete   # desinstalar paquete
pip list                # enumerar paquetes instalados 
```
Opciones para manejar versiones de paquetes:
```bash  title="PIP - Comandos básicos"
pip install paquete==?          # consultar versiones online del paquete 
pip install paquete==version    # instalar version especificada
pip install paquete>=version    # instalar version especificada o más reciente
```
Listado de dependencias e instalacion desde las mismas:

```bash  
# guardado en texto de paquetes actuales y su versión actual
pip freeze > requirements.txt
# instalacion desde archivo
pip install -r requirements.txt
```


### Actualización de paquetes

Para actualizar los paquetes se puede usar el paquete auxiliar pip-review:

```bash
pip install pip-review
pip-review --local --interactive
```

Ubicacion de paquetes locales:
```bash
python -m site --user-site
```

## Importación


El manejo de los paquetes ya instalados es idéntico al de los módulos. 

Para usar el paquete se importa haciendo:

```python
import paquete
```

Si sólo se necesita usar algunas funciones (o submódulos) del paquete se usa:

```python
from paquete import <mi_archivo_funciones>
```

A los paquetes también se les puede poner alias en el programa:

```python
import paquete as alias
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

