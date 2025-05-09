

# Entorno virtual: módulo VENV


## Entornos virtuales

Los *entornos virtuales* son instalaciones locales de los paquetes que permiten un mejor control de los paquetes y sus versiones, minimizando el riesgo de incompatibilidades entre paquetes, evitar problemas debidos a la actualización descuidada de los mismos, etc.

### Creación

Los entornos virtuales se construyen siguiendo los siguientes pasos:

1. Crear un directorio (es decir, una carpeta) independiente de la instalación de Python global,
típicamente en la ubicación del proyecto
o en una carpeta del usuario;
2. Crear una réplica del intérprete de Python o un enlace simbólico al mismo en el directorio.
3. Instalar los paquetes requeridos en dicho directorio,
permitiendo especificar qué versión se necesita de cada uno;
<!-- 
4. Crear una copia alterada de la variable **`PYTHONPATH`**, donde la primera ruta incluida será la del nuevo intérprete y sus dependencias.
5. Ejecutar el intérprete de Python local.

 -->
<!-- 
creando una version alterada de la variable **PYTHONPATH** del intérprete en la que agragan al comienzo la ruta local con los paquetes del entorno.
 -->

<!-- 
De esta manera el intèrprete de Python buscará sus dependencias primero en la ruta del entorno virtual y sólo si no encuentra los paquetes allí los busca en la instalacion global. 

 -->


Esto introduce algunas ventajas respecto al uso del intérprete global:

- Cada proyecto puede tener una versión diferente de un mismo paquete,
evitando conflictos de instalación y de actualización;
- Se evita la carga de paquetes no incluidos en el proyecto,
permitiendo entornos mejor controlados para cada proyecto;
- Es posible agregar enlaces simbólicos de múltiples versiones de Python,
lo cual permite ejecutar el proyecto con distintas versiones del mismo.


Como contrapartida aumenta el espacio en disco ocupado,
por cuanto cada entorno virtual tiene su propia copia de los paquetes.


### Activación

Los entornos virtuales requieren activación para su uso.
La activación del entorno virtual consiste en modificar 
en la sesión actual 
la variable **`PATH`** del sistema operativo,
colocándole al comienzo
la ruta del entorno virtual creado.
De esta manera el sistema operativo dará prioridad a los ejecutables y paquetes del entorno virtual respecto a sus equivalentes globales.

Por ejemplo: el intérprete global de Python en un sistema GNU/Linux
suele ser `/usr/bin/python`.
Dicha ruta puede ser consultada en la *shell* Bash con el comando `which`:

```bash title="Bash - Ruta de Python"
which python
```
Tras activar el entorno virtual,
al repetir la consulta el resultado cambia a una ruta de la forma `RUTA_ENTORNO/bin/python`.


## VENV

VENV es la herramienta integrada de Python para trabajar con entornos virtuales.
Se incluye desde la versión 3.4.

### Creacion entorno virtual 
Se elige la ruta de un directorio donde se creará el entorno virtual:
```bash title="Creación de entorno virtual"
py -m venv ruta_directorio
```
Dentro del directorio elegido se crearán todos los archivos y directorios auxiliares necesarios para empezar a trabajar. En ellos se guardará el ejecutable de Python y se guardarán los paquetes a añadirse al proyecto.

Es muy habitual crear el entorno virtual dentro del directorio del proyecto
en una carpeta oculta llamada `venv`:

```bash title="Creación - dentro del proyecto"
py -m venv .venv
```


### Activacion entorno virtual


El comando de activación dependerá de la terminal usada:


=== "Bash"

      ```bash title="Activación - Bash"
      source ruta_entorno/bin/activate  # Linux y MacOs
      source ruta_entorno/Scripts/activate  # Windows
      ```

=== "CMD"

      ```cmd title="Activación - CMD"
      ruta_entorno\Scripts\activate.bat
      ```

=== "PowerShell"

      ```cmd title="Activación - PowerShell"
      ruta_entorno\Scripts\Activate.ps1
      ```

En el caso de haber creado la carpeta oculta `venv`:

=== "Bash"

      ```bash title="Activación (local) - Bash"
      source venv/bin/activate  # Linux y MacOs
      source venv/Scripts/activate  # Windows
      ```

=== "CMD"

      ```cmd title="Activación (local) - CMD"
      venv\Scripts\activate.bat
      ```

=== "PowerShell"

      ```cmd title="Activación (local) - PowerShell"
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


