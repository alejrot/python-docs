---
status: new
date:
    created: 2025-07-01
    updated: 2025-08-26
---

# Primer demo

Se realiza una primera rutina para poner a prueba
el funcionamiento de los contenedores.


## Demo

###  Rutina original

En este ejemplo se implementó
una rutina llamamda `contar.py` que cuenta hasta 10
esperando un segundo entre cuentas y entonces cierra.



```py title="Rutina original"
# archivo 'contar.py'
from time import sleep
import sys


# salida por consola
try:
    # el numero maximo a contar se asigna como argumento
    n = int(sys.argv[1])
    print(f"Contando hasta {n}")

except Exception:
    # valor máximo por default en caso de error
    print("Argumento de entrada faltante o incorrecto (debe ser un entero)")
    n = 10
    print(f"Contando hasta {n} (valor default)")

finally:
    # el contador se incrementa cada 1 segundo
    i = 0
    while i <= n:
        print(f"i: {i:4}")
        sleep(1)
        i += 1
``` 

La rutina se implementó en un único archivo.
No hay paquetes que requieran ser instalados.

### Ejecución

El programa se ejecuta llamando al intérprete de Python
e indicándole el nombre del archivo con la rutina,
que en este ejemplo se llama `contar.py`: 

``` bash title="Ejecutar - cuenta default"
python contar.py
```

La cuenta máxima puede ser alterado mediante un argumento posicional,
el cual debe ser un número:

``` bash title="Ejecutar - cuenta custom"
python contar.py  4
```

Si hay más argumentos u opciones entonces éstos se ignoran.


### Rutina adaptada

Se utiliza el *logging*
y el *lazy formatting*
en la rutina
como reemplazo al *print*
y los *f-strings*.

Este es el resultado:

```py title="Rutina adaptada"
# archivo 'contar.py'
from time import sleep
import sys
import logging

# uso de la consola de logs
logging.basicConfig(
    level=logging.INFO, # mínimo nivel de log a publicar
    format="%(asctime)s - %(levelname)s - %(message)s", #info incorporada
    )

try:
    # el numero maximo a contar se asigna como argumento
    n = int(sys.argv[1])
    logging.info("Contando hasta %i", n)

except Exception:
    # valor máximo por default en caso de error
    logging.warning("Argumento de entrada faltante o incorrecto (debe ser un entero)")
    n = 10
    logging.warning("Contando hasta %i (valor default)", n)

finally:
    # el contador se incrementa cada 1 segundo
    i = 0
    while i <= n:
        logging.info("i: %4i",i)
        sleep(1)
        i += 1
``` 

## Configuraciones

### Estructura de archivos


En este ejemplo se ubican todas las rutinas del programa
dentro de una carpeta llamada `demo`
y a su lado se crean 
los archivos `compose.yml` y `Dockerfile`.

```bash title="Arbol de archivos"
.
├── demo
│   └── contar.py
├── compose.yml
└── Dockerfile
```
<!-- 
El archivo `compose.yml`
es llamado en muchos proyectos como `docker-compose.yml`.
También puede ponérsele la extensión `.yaml`.
 -->

### Dockerfile

El archivo `Dockerfile` requerido
en este caso
es muy sencillo.


```Dockerfile title="Dockerfile - básico"
# imagen de base
FROM python:alpine

# directorio de trabajo (se crea automáticamente)
WORKDIR /code

# copia de rutinas al directorio de trabajo
COPY demo/ ./

# comando, opciones y argumentos (sobreescribibles)
CMD ["python", "contar.py", "4"]
``` 

No hizo falta instalar dependencias.


<!-- 
En el archivo se siguen una serie de pasos básicos:

1. `FROM`: elige una imagen de contenedor de referencia,
en base a la cual se creara una nueva;
2. `WORKDIR`: crea y definer una ruta de trabajo 
para el programa
dentro del contenedor;
3. `COPY`: copia contenidos
(rutinas, directorios del programa,etc. )
a la ruta que se le especifica,
la cual es típicamente la carpeta de trabajo.
4. `CMD`: define el comando a ejecutar, sus opciones y argumentos.
Todos estos pueden ser sobreescritos.
 -->

### `compose.yml`


Para este ejemplo se crea un único servicio
y se le indica que el Dockerfile
es aledaño al archivo `compose.yml`:


```yaml title="compose.yml - construir imagen"
name: contar-python

services:

  demo-contador:    # nombre de servicio - arbitrario
    # necesarios
    build: .        # Dockerfile en el mismo directorio
    # opcionales
    image: imagen-contador:v1
    container_name: contenedor-contador
```

También se aprovechó para etiquetar la nueva imagen
y darle nombre al contenedor,
pero esos pasos son meramente opcionales.

## Despliegue


Se ordena 
la construcción y el despliegue del proyecto:

```bash title="Construir y desplegar"
cd ruta_proyecto
podman compose up --build
``` 
Este paso debe:

- descargar la imagen de Python pedida;
- crear la nueva imagen derivada 
con el nombre `imagen-contador` y tag `v1`;
- crear el proyecto y su contenedor interno; 
- poner el contenedor en marcha.

Si todo salió bien debe observarse por consola los *logs*,
algo parecido a:

``` log title="Registro"
contenedor-contador  | 2025-08-27 04:42:57,880 - INFO - Contando hasta 4
contenedor-contador  | 2025-08-27 04:42:57,880 - INFO - i:    0
contenedor-contador  | 2025-08-27 04:42:58,880 - INFO - i:    1
contenedor-contador  | 2025-08-27 04:42:59,881 - INFO - i:    2
contenedor-contador  | 2025-08-27 04:43:00,882 - INFO - i:    3
contenedor-contador  | 2025-08-27 04:43:01,882 - INFO - i:    4
contenedor-contador exited with code 0
```

Este mismo resultado debe repetirse instantáneamente
al consultar los *logs* por terminal:

```bash title="Consultar registro"
podman compose logs
``` 

Se puede despertar al contenedor de nuevo:

```bash title="Desplegar"
podman compose up
```

y se verá que los nuevos registros
se concatenenan tras los anteriores,
sin borrarlos.


Para dar de baja el contenedor
y todos sus *logs* internos
simplemente usar el comando `down`:

```bash title="Borrar"
podman compose down
```




<!-- 

## Puesta en marcha

El comando Compose interpreta el archivo `compose.yml` y con el crea,
ejecuta, lee y borra los contenedores indicados en el proyecto.
La terminal debe estar ubicada en la ruta del archivo para funcionar.

!!! info "Implementaciones"

    Dependiendo de la implementación del comando Compose instalada en el sistema,
    el comando se debe llamar como:

    ```bash
    docker-compose  <comando>  # Docker - versiones viejas / paquete externo
    docker compose  <comando>  # Docker - versiones nuevas
    podman-compose  <comando>  # Podman - Paquete externo
    podman compose  <comando>  # Podman Desktop - extension
    ```

    Elegir la variante que corresponda según el componente instalado en el sistema.
    En este tutorial se asumirá que es `podman compose  <comando>` 




### Creación

El proyecto se crea con el comando `up`.

```bash
podman compose up
```

Este comando descarga la imagen indicada por el Dockerfile
en caso de ser necesario y crea la imagen personalizada.
Luego pone en marcha al contenedor
y muestra los mensajes de log a medida que se producen.


El comando `up` no reconstruye la imagen en caso de modificarse la rutina Python. Para forzar la reconstrucción hay que agregar la opción `build`:

```bash
podman compose up --build
```

### Arranque

La puesta en marcha en segundo plano se realiza con el comando `start`:

```bash
podman compose start
```

### Registro

La consulta del registro de *logs* pasados se hace con `logs`:

```bash
podman compose logs
```

Los logs de cada contenedor también se pueden consultar desde el cliente gráfico tanto de Docker como de Podman.


### Borrar

El proyecto se elimina con el comando `down`:


```bash
podman compose down
```

Este comando apaga los contenedores del proyecto y los elimina.
 -->