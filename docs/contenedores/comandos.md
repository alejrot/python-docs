# Comandos

En esta sección se ven

## Elegir comandos

El comando a ser ejecutado por el contenedor
se puede reemplazar desde el archivo `compose.yml`
con ayuda del parámetro `command`.

Algunos ejemplos:


```yaml hl_lines="5" title="compose.yml - sobreescribir comandos"
services:

  demo-contador:
    build: .
    command: "python --version" # versión de Python
```


```yaml hl_lines="5" title="compose.yml - sobreescribir comandos"
services:

  demo-contador:
    build: .
    command: "uname -a"     # info sobre el kernel usado
```



## Fijar comandos



El archivo Dockefile tiene una cláusula específica
para fijar comandos, argumentos y opciones
a ser ejecutados por el contenedor llamada `ENTRYPOINT`.
Con esta cláusula se define
la parte obligatoria del comando
en tanto que la parte opcional
se delega en la cláusula `CMD`.


Por ejemplo, si el comando original es:

```Dockerfile title="Dcokerfile - comando sobreescribible"
# comando, opciones y argumentos (sobreescribibles)
CMD ["python", "contar.py", "4"]
``` 

entonces para forzar la ejecución de la rutina `contar.py` se hace:

```Dockerfile title="Dcokerfile - comando fijo"
# comando, opciones y argumentos fijos
ENTRYPOINT ["python", "contar.py"]

# opciones y argumentos opcionales/sobreescribibles
CMD ["4"]
``` 

y en el archivo Compose sólo se podrán asignar
los argumentos de la rutina:

```yaml hl_lines="5" title="compose.yml - sobreescribir argumentos"
services:

  demo-contador:
    build: .
    command: "7"     # valor opcional: cuenta máxima
```

En este caso
todo lo que se ingrese con la cláusula `command`
será pasado como argumento a la rutina de Python.