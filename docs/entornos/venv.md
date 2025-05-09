---
tags:
  - venv
  - Modulos
  - Entornos
---





## VENV

**`venv`** es la herramienta integrada de Python para trabajar con entornos virtuales.
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

### Uso sin activación


El intérprete local de Python puede ser ejecutado directamente a partir de su ruta.
Invocándolo directamente se ahorra el paso de activación de su entorno virtual.

Uso en Bash:

```bash title="Sin activación - interprete local"
ruta_entorno/bin/python   # Linux y MacOs
ruta_entorno/Scripts/python   # Windows
```


### Eliminar entorno virtual

El entorno virtual se elimina borrando los directorios auxiliares del entorno:

```bash title="Eliminar entorno"
deactivate
rm -r ruta_directorio  # eliminacion recursiva
```

!!! warning "Eliminar entorno"

    Prestar atención a no incluir código del proyecto 
    adentro del directorio del entorno virtual.
    De otro modo,
    al eliminar el entorno virtual,
    también se eliminaría parte del código de programa.



## Referencias


[Documentación oficial - VENV](https://docs.python.org/3/library/venv.html)

[PythonLand - How to Create, Activate, Deactivate, And Delete](https://python.land/virtual-environments/virtualenv)
