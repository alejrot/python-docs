---
date:
    created: 2025-07-01
    updated: 2025-08-26
---

# Primer despliegue


## Configuraciones

### Estructura de archivos


En este ejemplo se ubican todas las rutinas del programa
dentro de una carpeta llamada `demo`
y a su lado se crean dos archivos llamados `compose.yml` y `Dockerfile`.

```bash title="Arbol de archivos"
.
├── demo
│   └── contar.py
├── compose.yml
└── Dockerfile
```

El archivo `compose.yml`
es llamado en muchos proyectos como `docker-compose.yml`.
También puede ponérsele la extensión `.yaml`.

### Dockerfile

El archivo `Dockerfile` es el encargado de crear una imagen a medida del proyecto:

```Dockerfile title="Dockerfile - básico"
# imagen de base
FROM python:3.13.5-alpine3.22

# directorio de trabajo (se crea automáticamente)
WORKDIR /code

# copia de rutinas al directorio de trabajo
COPY demo/ ./

# comando, opciones y argumentos (sobreescribibles)
CMD ["python", "contar.py", "4"]
``` 

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
