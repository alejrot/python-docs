---
tags:
  - venv
  - Modulos
  - Entornos virtuales
---




# VENV

**`venv`** es la herramienta integrada de Python para trabajar con entornos virtuales.
Se incluye desde la versión 3.4.

## Creacion entorno virtual 

Se elige la ruta de un directorio donde se creará el entorno virtual:
```bash title="Creación de entorno virtual"
py -m venv RUTA_ENTORNO
```
Se crea automáticamente la carpeta contenedora
y dentro de ella
se crearán todos los archivos y directorios auxiliares necesarios para empezar a trabajar,
incluyendo el ejecutable de Python y el de PIP.
Alí se guardarán también los paquetes a añadirse al proyecto.

Es muy habitual crear el entorno virtual dentro del directorio del proyecto
en una carpeta oculta llamada `venv`:

```bash title="Creación - dentro del proyecto"
py -m venv .venv
```

???+ info "Árbol de archivos"

      Cuando se crea el entorno virtual se crea una estructura de archivos similar a la siguiente:

      ```bash
      .venv
      ├── bin                      
      │       # rutinas de shell -> comando 'deactivate'
      │   ├── activate
      │   ├── activate.csh
      │   ├── activate.fish
      │   ├── Activate.ps1
      │       # clientes PIP
      │   ├── pip
      │   ├── pip3
      │   ├── pip3.13
      │       # enlaces simbólicos al intérprete Python global
      │   ├── python -> /usr/bin/python
      │   ├── python3 -> python
      │   └── python3.13 -> python
      │
      ├── include
      │   └── python3.13            # (vacío)
      │
      ├── lib
      │   └── python3.13
      │       └── site-packages     # paquetes instalados localmente
      │           ├── pip                       # código de paquete   
      │           └── pip-24.3.1.dist-info      # información de paquete
      │
      ├── lib64 -> lib
      │
      └── pyvenv.cfg                # configuración del entorno actual (automático)
      ```
      donde la numeración de PIP y de Python corresponde a la versión global disponible, en este ejemplo la 3.13.

      En el caso de Windows la carpeta `bin` es reemplazada por la carpeta `Scripts`. 

      El archivo de configuración `pyenv.cfg`
      tiene un contenido como el siguiente:

      ```bash
      home = /usr/bin
      include-system-site-packages = false
      version = 3.13.3
      executable = /usr/bin/python3.13
      command = /usr/bin/python -m venv RUTA_PROYECTO/.venv
      ```

      El diagrama de árbol previo puede trazarse con el comando `tree` de Bash:

      ```bash
      tree .venv  -L 4
      ```



## Activacion entorno virtual

La activación consiste en ejecutar
alguno de los *scripts* de nombre *"activate"*.
El script correcto dependerá de la terminal usada:


=== "Bash"

      ```bash title="Activación - Bash"
      source RUTA_ENTORNO/bin/activate  # Linux y MacOs
      source RUTA_ENTORNO/Scripts/activate  # Windows
      ```

=== "CMD"

      ```cmd title="Activación - CMD"
      RUTA_ENTORNO\Scripts\activate.bat
      ```

=== "PowerShell"

      ```cmd title="Activación - PowerShell"
      RUTA_ENTORNO\Scripts\Activate.ps1
      ```

En el caso de haber creado la carpeta oculta `venv`:

=== "Bash"

      ```bash title="Activación (local) - Bash"
      source .venv/bin/activate  # Linux y MacOs
      source .venv/Scripts/activate  # Windows
      ```

=== "CMD"

      ```cmd title="Activación (local) - CMD"
      .venv\Scripts\activate.bat
      ```

=== "PowerShell"

      ```cmd title="Activación (local) - PowerShell"
      .venv\Scripts\Activate.ps1
      ```


La activación se verifica en Bash con el comando `which`:

```bash title="Consultar intérprete actual"
which python
```
cuyo resultado debe apuntar a alguno de los enlaces a Python internos:

```bash title="Intérprete actual"
RUTA_ENTORNO/bin/python   # Linux y MacOs
RUTA_ENTORNO/Scripts/python   # Windows
```

Además se debe verificar que PIP no detecta paquetes adicionales instalados:

```bash title="Paquetes preinstalados"
pip list
```
dando lugar a una lista como esta:
```
Package Version
------- -------
pip     24.3.1
```


El entorno virtual permanecerá activado hasta que se cierre la terminal o se desactive explícitamente con el comando [`deactivate`](#desactivar-entorno-virtual).



## Instalar paquetes manualmente


Los paquetes se instalan con ayuda de PIP:
```bash title="Instalar paquete Python"
pip install nombre_paquete
```
Hay que asegurarse primero que el entorno virtual esté activado.

La lista de paquetes disponibles localmente se realiza con el comando `list`:
```bash title="Listar paquetes"
pip list
```
La lista puede guardarse en archivo:
```bash title="Guardar lista de paquetes"
pip list > nombre_archivo.txt
```

## Anotar e instalar dependencias

La versión actual de los paquetes se puede guardar en formato texto con el comando *freeze*:
```bash title="Registrar paquetes"
# paquetes actuales y su versión actual
pip freeze > requirements.txt
```
En el ejemplo se guardan todos los nombres de paquete y sus versiones en el archivo de texto *requirementsd.txt*.
Esta lista creada sirve para automatizar la descarga e instalación de todos los paquetes necesarios con un único comando:

```bash title="Instalar lista de paquetes"
# instalacion desde archivo
pip  install -r requirements.txt
```
En el contexto de un entorno virtual se minimiza la lista de paquetes a instalar,
mejorando el control sobre el proyecto
y evitando instalar dependencias inútiles para el proyecto actual.


## Desactivar entorno virtual

El entorno virtual se desactiva fácilmente con el comando *deactivate*:
```bash title="Desactivar entorno"
deactivate
```
De esta manera se retoma el uso de los paquetes globales de manera inmediata
y el intérprete de Python detectado vuelve a ser el global:

```bash title="Intérprete global"
which python      # En Linux: '/usr/bin/python'
```

## Uso sin activación


El intérprete local de Python puede ser **ejecutado directamente** a partir de su ruta.
Invocándolo directamente se ahorra el paso de activación de su entorno virtual.

Uso en Bash:

```bash title="Sin activación - interprete local"
RUTA_ENTORNO/bin/python   # Linux y MacOs
RUTA_ENTORNO/Scripts/python   # Windows
```


## Eliminar entorno virtual

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
