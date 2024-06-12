

# Entorno virtual: módulo VENV


## Entornos virtuales

Los *entornos virtuales* son instalaciones locales de los paquetes que permiten un mejor control de los paquetes y sus versiones, minimizando el riesgo de incompatibilidades entre paquetes, evitar problemas debidos a la actualización descuidada de los mismos, etc.

Los entornos virtuales funcionan creando una version alterada de la variable **PATH** del sistema operativo en la que agragan al comienzo la ruta local con los paquetes del entorno.
De esta manera el programa buscará sus dependencias primero en la ruta del entorno virtual y sólo si no encuentra los paquetes allí los busca en la instalacion global. De esta manera la versión local de cada paquete tendrá prioridad sobre la version global.


## VENV

VENV es la herramienta integrada de Python para trabajar con entornos virtuales.

### Creacion entorno virtual 
Se elige la ruta de un directorio donde se creará el entorno virtual:
```bash title="Creación de entorno virtual"
py -m venv ruta_directorio
```
Dentro del directorio elegido se crearán todos los archivos y directorios auxiliares necesarios para empezar a trabajar. En ellos se guardará el ejecutable de Python y se guardarán los paquetes a añadirse al proyecto.

### Activacion entorno virtual
La activación del entorno virtual consiste en colocar al comienzo
de la variable PATH la ruta del entorno virtual creado. De esta manera el sistema operativo dará prioridad a los ejecutables y paquetes del entorno virtual respecto a sus equivalentes globales.

El comando de activación dependerá de la terminal usada.

<!-- Bash (Linux and MacOs): -->
```bash title="Activación - Bash (Linux and MacOs)"
source ruta_directorio/bin/activate  # Linux y MacOs
source ruta_directorio/Scripts/activate  # Windows
```
<!-- Windows: -->
 <!-- -  En cmd.exe -->
```cmd title="Activación - CMD"
venv\Scripts\activate.bat
```
 <!-- -  En PowerShell -->
```cmd title="Activación - PowerShell"
venv\Scripts\Activate.ps1
```
El entorno virtual permanecerá activado hasta que se cierre la terminal o se desactive explícitamente con el comando [`deactivate`](#desactivar-entorno-virtual).



### Instalar paquetes manualmente


Los paquetes se instalan con el comando habitual:
```bash title="Instalar paquete Python"
pip install nombre_paquete
```
Hay que asegurarse primero que el entorno virtual esté activado.

La lista de paquetes disponibles se realiza con el comando *list*:
```bash title="Listar paquetes"
pip list
```
La lista puede guardarse en archivo:
```bash title="Guardar lista de paquetes"
pip list > nombre_archivo.txt
```


### Anotar e instalar dependencias

La versión actual de los paquetes se puede guardar en formato texto con el comando *freeze*:
```bash title="Registrar paquetes"
# paquetes actuales y su versión actual
pip freeze > requirements.txt
```
En el ejemplo se guardan todos los nombres de paquete y sus versiones en el archivo de texto *requirementsd.txt*. Esta lista creada sirve para automatizar la descarga e instalación de todos los paquetes necesarios con un único comando:
```bash title="Instalar lista de paquetes"
# instalacion desde archivo
pip  install -r requirements.txt
```
En el contexto de un entorno virtual se minimiza la lista de paquetes a instalar, mejorando el control sobre el proyecto y evitando instalar dependencias inútiles para el proyecto actual.


### Desactivar entorno virtual

El entorno virtual se desactiva fácilmente con el comando *deactivate*:
```bash title="Desactivar entorno"
deactivate
```
De esta manera se retoma el uso de los paquetes globales de manera inmediata.

### Eliminar entorno virtual
El entorno virtual se elimina borrando los directorios auxiliares del entorno:

```bash title="Eliminar entorno"
deactivate
rm -r ruta_directorio  # eliminacion recursiva
```

!!! warning "Eliminar entorno" 
      Prestar atención a que el código esté afuera del directorio del entorno virtual antes de eliminarlo. 




## Alternativas a VENV

Existen alternativas para crear entornos virtuales. Algunas de ellas son:

- **VirtualEnv**
- **PIPENV**
- **Poetry**



## Referencias


[Documentación oficial - VENV](https://docs.python.org/3/library/venv.html)

[PythonLand - How to Create, Activate, Deactivate, And Delete](https://python.land/virtual-environments/virtualenv)


