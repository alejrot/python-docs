


# Módulos

Los programas a medida que crecen se dividen en módulos para facilitar el diseño, el mantenimiento y la reutilización. 
Un módulo es un archivo Python que contiene definiciones y sentencias relacionados. 

## Importación de módulo

La importación es una sentencia que da acceso a las funciones y constantes definidas en el módulo especificado
```py 
import modulo
```
Las importaciones deben hacerse antes de usar sus componentes. 
Típicamente se hacen al comienzo del archivo. 

## Uso de componentes

Las funciones del módulo importado se usan así:

```py
modulo.funcion(argumento)
```
Las constantes se acceden así:

```py
modulo.constante
```


!!! example "Ejemplo: modulo request"

    El módulo *request* permite interactuar con API's de servidores remotos para hacer consultas.

    ```py
    import requests
    ```
    Con la función `get()` se hace la petición al servidor.

    ```py
    respuesta = requests.get( "https://pokeapi.co/api/v2/pokemon?limit=151")
    ```




## Alias de módulo

Al módulo se lo puede importar y asignarle un nombre alternativo dentro del programa:
```py
import modulo as alias_modulo
```
esto permite usar alias más cortos para usar sus componentes:
```py
alias.constante
alias.funcion(argumento)
```

## Importación de elementos

Para importar un elemento específico de un módulo se puede usar la sentencia:
```py
from modulo import elemento
```
Los elementos también se pueden importar con nuevo nombre:
```py
from modulo import elemento as alias_elemento
```


!!! warning "Importación sin nombre"

    Una mala práctica muy habitual es importar un módulo con la sentencia:
    ```py
    from modulo import *
    ```
    Ésta permite llamar a todos los elementos del módulo pero sin mencionarlo. Puede dar lugar a conflictos al llamar a múltiples módulos. 
    Por ejemplo, tanto el módulo `pathlib` como el módulo `os` poseen una función llamada `Path()`.



## Módulos estandar

La [Biblioteca Estándar de Python](https://docs.python.org/es/3/library/index.html) enumera y explica todos los módulos estándar del lenguaje Python.



## Módulos locales


### Crear módulos y submódulos

Los módulos se crean dentro de archivos con extensión `.py.
Si estos archivos se ubican dentro de *subdirectorios* en tal caso se habla de *submódulos*  

!!! info "Exportación de elementos"

    A diferencia de otros lenguajes, en Python todos los elementos internos son visibles y por eso no es necesario ordenar la exportación de elementos para que éstos sean accesibles por fuera del módulo. 

    Para reducir la visibilidad de los elementos internos se puede recurrir a los [archivos __init__](#archivos-__init__)



### Sintaxis de importación

Las barras(`/`) o barras invertidas (`\`) de la ruta de archivo se reemplazan por puntos (`.`) y del nombre de archivo se omite la extensión.
<!-- 
Entonces, para importar un archivo Python como módulo desde un subdirectorio de la ruta actual la notación queda: 
-->

### Importación absoluta


La importacion absoluta indica la ruta del archivo de módulo respecto al directorio raíz del proyecto. 
Por ejemplo, si el archivo está adentro de un directorio interno del proyecto la importación queda así:

```py title="Importación absoluta"
import directorio.archivo                                # importar modulo
import directorio.archivo as alias                       # importar modulo con alias
from directorio.archivo import elemento, funcion, Clase  # importar elementos particulares
```



### Importación relativa

<!-- 
Asimismo los módulos pueden tener dependencias con otros archivos de módulo. Para poder importarlos se toma como referencia la ruta del archivo de módulo y de ahí se toma la ruta relativa. Sintaxis: 
-->

La importación relativa se basa en definir la ruta del archivo de módulo respecto a la ruta del archivo actual:


```python title="Importación relativa"
from . import modulo_A      # archivo en directorio actual
from .. import modulo_B     # archivo en directorio padre
```

!!! warning "Rutas relativas" 
    
    El uso de importaciones relativas es motivo de debate respecto de las buenas prácticas y suele ser origen de múltiples problemas de dependencias.



### Ejecutar módulo

Si el archivo del módulo tiene código para ejecutar (por ejemplo, un demo o un test) esto se realiza imitando la importación absoluta, mediante la sintaxis:

```bash title="Ejecución de módulo"
# ruta raíz del proyecto
py -m directorio.archivo    # ejecucion módulo
```


### Archivos `__init__.py`

Es habitual colocar archivos llamados `__init__.py` al lado de los archivos de submódulo, los cuales permiten reducir la visibilidad de los mismos, acelerar la carga y prevenir errores. 

``` bash title="Archivo __init__.py - ubicación" 
directorio
    ├─ submodulo1.py
    ├─ submodulo2.py
    ├─ submodulo3.py
    ├─ ....
    ├─ submoduloN.py
    └─ __init__.py       
```

Para especificar qué submódulos deben ser accesibles se recurre al objeto `__all__` dentro de `__init__.py`:

```python title="Archivo __init__.py - contenido"
## archivo '__init__.py'
__all__ = [
    "submodulo1",      # archivo 'submodulo1.py'
    "submodulo2",      # archivo 'submodulo2.py'
    ]
```
De esta forma, si un archivo aledaño intentara importar todo:

```python
from directorio import *  # importa 'modulo1.py' y'modulo2.py'
```
se importará solamente a estos dos submódulos especificados en `__init__.py` incluso si hay otros módulos en el directorio.

!!! warning "__init__.py vacíos"

    Antiguamente era una práctica muy popular crear archivos `__init__.py` vacíos en cada subdirectorio, la cual era considerada necesaria. 
    Sin embargo, esto actualmente no es necesario y puede ser contraproducente. 

    Por ejemplo, al intentar ejecutar programas compilados con PyInstaller éstos son incapaces de acceder a los módulos creados y por ello la ejecución es abortada. 



## Referencias


[Documentacion oficial - Módulos](https://docs.python.org/es/3/tutorial/modules.html)

[Hektorprofe - Módulos](https://docs.hektorprofe.net/python/modulos-y-paquetes/modulos/)

