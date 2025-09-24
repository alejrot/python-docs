---
status: new
date:
    created: 2025-07-01
    updated: 2025-08-26
---



# Fijar y modificar comandos 

En esta sección se ve cómo
se pueden cambiar los comandos elegidos
para las imágenes
desde el archivo `compose.yml`
y también como los comandos
pueden ser fijados
desde el Dockerfile.



## Elegir comandos
<!-- 
El comando a ser ejecutado por el contenedor
se puede reemplazar desde el archivo `compose.yml`
con ayuda del parámetro `command`.

 -->

El parámetro `command` del archivo `compose.yml`
sirve para sobreescribir el comando definido
con la cláusula `CMD` del Dockerfile.

En el ejemplo del [primer despliegue](despliegue_demo.md)
el demo se ejecuta desde la *sell* Bash
con la sentencia:

```bash title="Bash - ejecución de rutina"
python contar.py 4
```

El comando fue adaptado al Dockerfile
con la cláusula `CMD`.

```Dockerfile title="Dockerfile - comando sobreescribible"
# comando, opciones y argumentos (sobreescribibles)
CMD ["python", "contar.py", "4"]
``` 

Este comando puede ser ignorado
definiendo el campo `command`.
Por ejemplo, para cambiar la cuenta final
de 4 a 10:

```yaml hl_lines="5" title="compose.yml - sobreescribir cuenta"
services:

  demo-contador:
    build: .
    command: "python contar.py 10"  # cuenta máxima alterada
```


También se puede ignorar la rutina interna de la imagen,
por ejemplo para consultar
la versión del intérprete Python instalada:

```yaml hl_lines="5" title="compose.yml - omitir rutina interna"
services:

  demo-contador:
    build: .
    command: "python --version" # versión de Python
```

También se pueden ejecutar otros programas incluidos en la imagen
por ejemplo para conocer qué versión del kernel Linux
se incluyó internamente:

```yaml hl_lines="5" title="compose.yml - cambiar de comando"
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

```Dockerfile title="Dockerfile - comando sobreescribible"
# comando, opciones y argumentos (sobreescribibles)
CMD ["python", "contar.py", "4"]
``` 

entonces para forzar la ejecución de la rutina `contar.py` se hace:

```Dockerfile title="Dockerfile - comando fijo"
# comando, opciones y argumentos fijos
ENTRYPOINT ["python", "contar.py"]

# opciones y argumentos opcionales/sobreescribibles
CMD ["4"]
``` 

y en el archivo Compose sólo se podrán asignar
los argumentos de la rutina:

```yaml hl_lines="5" title="compose.yml - comando fijo"
services:

  demo-contador:
    build: .
    command: "7"     # valor opcional: cuenta máxima
```

En este caso
todo lo que se ingrese con la cláusula `command`
será pasado como argumento a la rutina de Python.