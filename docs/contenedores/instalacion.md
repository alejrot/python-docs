---
date:
    created: 2025-07-01
    updated: 2025-08-26
---

# Docker y Podman


Para este tutorial se necesita instalar Docker o Podman,
aunque se asume el uso de este último.


## Docker

Docker es el programa gestor de contenedores más popular del momento
y es el que sirve de referencia para otras implementaciones.
Docker trae integrado su propio intérprete de los archivos Compose
y su propio cliente gráfico llamado Docker Desktop.
Es software privativo.

Se descarga desde su [página oficial](https://www.docker.com).

!!! info "Docker Engine"

    El Docker Engine es el componente que hace funcionar a los contenedores.
    Este debe estar inicializado y en funcionamiento para poder trabajar.
    Docker Desktop permite su administración con el mouse.


## Podman

Podman es una imitación de Docker de código libre
que es altamente compatible con Docker en lo respectivo a los comandos y que usa sus mismas imágenes.
Este programa no trae por *default* la compatibilidad con el comando Compose sino que la habilita mediante dos opciones:

- La extensión Compose del entorno gráfico Podman Desktop,
que es un envoltorio (un *wrapper*)
de un paquete externo llamado `docker-compose`;
- el paquete `podman-compose` que está escrito en Python y se puede instalar por *shell*.

El cliente gráfico de Podman se llama Podman Desktop.

[Sitio oficial de Podman](https://podman.io/docs/installation)
[Podman Desktop](https://podman-desktop.io/downloads)


!!! info "Podman Machine"

    Podman Machine es el componente análogo al Docker Engine
    y también necesita ser inicializado y ouesto en marcha para poder trabajar. 
    Podman Desktop permite su administración mediante clicks.
    En caso de querer hacerlo desde terminal Bash:
    ```bash title="Bash - arranque de gestor"
    podman machine init
    podman machine start
    ```



## Comandos

Los comandos básicos de ambos programas toman esta forma genérica: 


=== "Docker"

    ```bash title="Bash - comandos"
    docker  comando subcomando 
    ```

=== "Podman"

    ```bash title="Bash - comandos"
    podman  comando subcomando 
    ```

La gran mayoría de los comandos son intercambiables entre ambos programas.


!!! tip "Alias"

    Desde Bash se pueden crear alias
    para los comandos: 

    ```bash title="Alias - Docker instalado"
    alias podman="docker"
    ```

    ```bash title="Alias - Podman instalado"
    alias docker="podman"
    ```

    de esta manera se puede llamar al gestor de contenedores disponible
    con cualquiera de los dos nombres.



## Windows vs GNU/Linux

Sobre el manejo de estos programas en Windows y en Linux se observan estas diferencias:

- En sistemas Windows se necesita activar el *Windows Subsystem for Linux* o WSL para ambos programas. En cambio en Linux ambos programas corren nativamente;
- En Windows los motores de los programas gestores pueden exigir varios gigabytes de memoria RAM para mantenerse en funcionamiento,
en tanto que en Linux este consumo extra no existe o es muy limitado;
- Windows tiene los instaladores de los programas integrados;
en tanto que en Linux la instalación de los componentes
se hace por separado y por ello suele ser algo más engorrosa.


