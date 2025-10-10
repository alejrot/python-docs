---
date:
    created: 2025-07-01
    updated: 2025-09-12
---


# Networks

Las redes (*networks*) son elementos auxiliares
que permiten interconectar a los contenedores
del proyecto desde dentro de su entorno aislado,
sin necesidad de pasar por el sistema anfitrión.


### Introducción

El gestor de contenedores implementa las *networks*
como imitación de las redes privadas
y redirige las peticiones IP
de unos contenedores a otros.

Para el aprovechamiento de las redes
es clave el **nombre de servicio** de los contenedores.
El nombre de servicio de cada contenedor
funciona como un **nombre de dominio**.
Durante el despliegue
el gestor de los contenedores
asigna una IP privada
a cada contenedor del proyecto.
También implementa un servidor DNS
(*"Name Domain Server"*) local
que guarda la equivalencia entre servicios e IPs.
De esta manera los contenedores
podrán hacer peticiones IP
a otros contenedores
usando su nombre de servicio
para conformar las URLs a las cuales consultar.


Por ejemplo:
si un contenedor necesita consultar
una base de datos MySQL
desplegada en otro contenedor
entonces el "dominio" ya no será `localhost`
sino el nombre del servicio
asignado a la base de datos,
por ejemplo `servicio_db`:

```http title="URL network - Base de datos MySQL"
mysql://user:password@servicio_db:3306/nombre_db
```



## Implementación

Las redes se implementan
dentro del archivo `compose.yml`.


### Red default

De manera predeterminada
todos los contenedores de un mismo proyecto
comparten una *network* común,
llamada literalmente "default",
que les permite interconectarse los unos
con los otros.

Tomése como ejemplo el proyecto de un servidor
creado en tres partes:
frontend, backend y base de datos.
Con la *network default*
las tres partes pueden comunicarse directamente entre sí, 
en cualquier combinación y en cualquier sentido.

```mermaid
---
title: "Networks - Red default"
config:
  markdownAutoWrap: false
---
flowchart LR

    subgraph proyecto [Entorno proyecto]


        subgraph services [Servicios]
        front["`Frontend 
            frontend:8000`"]
        back["`Backend
            backend:8000`"]
        db["`Base de datos MySQL
            db:3306`"]
        end

        subgraph redes [Redes]
            red-default["(default)"]
        end

    end

    front --- red-default
    back --- red-default
    db --- red-default

    subgraph host [Host]
        subgraph ports [Puertos]
            port1["`Navegador
            localhost:8000`"]
        end
    end

    port1 -->|8000:8000| front
```

La implementación de este interconexionado
es tácita: no se indica por escrito.
Todo contenedor que no tenga
una network asignada manualmente
es conectada a la red *default*.

```yaml title="compose.yml - Red default"
services:

  frontend:
    image: imagen-front

  backend:
    image: imagen-back

  db:
    image: imagen-db
```


Esta implementación no es recomendada
para proyectos reales debido
a que todos los contenedores del proyecto
podrían acceder a información sensible
transmitida por los demás,
facilitando la aparición
de vulnerabilidades en el sistema.


### Subredes

La manera de definir (y limitar)
la conectividad entre contenedores
se realiza definiendo múltiples *networks*
dentro del proyecto.

En este ejemplo, sólo el servicio de *backend*
puede acceder directamente a la base de datos
y el servicio de *frontend* 
sólo puede interactuar con el *backend*:


```mermaid
---
title: "Networks - Redes partidas"
---
flowchart LR

    subgraph proyecto [Entorno proyecto]

        subgraph services [Servicios]
        front["`Frontend 
            frontend:8000`"]
        back["`Backend
            backend:8000`"]
        db["`Base de datos MySQL
            db:3306`"]
        end

        subgraph redes [Redes]
            red-front[red-frontend]
            red-db[red-db]
        end
    end


    front --- red-front
    back --- red-front
    back --- red-db
    db --- red-db


    subgraph host [Host]
        subgraph ports [Puertos]
            port1["`Navegador
            localhost:8000`"]
        end
    end

    port1 -->|8000:8000| front

```

Dentro del archivo `compose.yml`
se crea una sección llamada `networks`
donde se definen las redes que estarán disponibles
en el proyecto.
Por otra parte,
a cada contenedor
se le define el campo `networks`
donde se asigna una lista de redes 
a las cuales podrá conectarse:



```yaml title="compose.yml - Redes custom"
services:

  frontend:
    image: imagen-front
    # acceso
    networks:
      - red-frontend

  backend:
    image: imagen-back
    # acceso
    networks:
      - red-frontend
      - red-db

  db:
    image: imagen-db
    # acceso
    networks:
      - red-db


# definición de redes
networks:
  red-front:
  red-db:
```

En este esquema, cada contenedor
sólo puede comunicarse
con aquellos contenedores
con los cuales comparta al menos una red.
Aquellos contenedores que no tengan
asignada al menos una *network*
permanecerán aislados del resto.

### Redes externas

Las redes también pueden ser externas:
tan sólo requieren que se les agregue la opción `external: true`:

```yaml title="compose.yml - Redes externas"
# definición de redes
networks:
  red-externa:
    external: true
```
Dichas redes pueden proceder de otros proyectos Compose
o también pueden ser creadas manualmente.

### Drivers y parámetros adicionales

Normalmente no es necesario especificar
parámetros adicionales para utilizar las redes.
Sin embargo, se pueden especificar diferentes *drivers*,
elegir el protocolo IPv6 frente al IPv4,
asignar máscaras de red y *gateways*, etc.

El driver usado por defecto se llama **`bridge`**.
Más información sobre los drivers: [Docker Docs - Network drivers](https://docs.docker.com/engine/network/drivers/).


## Ejemplo: proxy reverso con NGINX


Este ejemplo se basa en el demo de la [web app con Flet](./puertos.md#ejemplo-webapp-con-python).
Esta web app consiste en un contenedor
cuyo nombre de servicio es `webapp-flet`
y acepta conexiones entrantes por el puerto `8000`

A este demo se le agrega un contenedor NGINX
que es configurado como proxy reverso,
esto es un servidor que redirige el tráfico
a distintas URLs dependiendo de qué ruta
se le indique a la entrada.

Este es el diagrama de bloques implementado:

```mermaid
---
title: "Network - Proxy reverso"
---
flowchart LR

    subgraph proyecto [Entorno proyecto]

        subgraph services [Servicios]
        front["`webapp-flet
            puerto 8000`"]
        proxy["`proxy-nginx
            puerto 80`"]
        end

        subgraph redes [Redes]
            red-default["red-proxy"]
        end

    end
    subgraph host [Host]
        subgraph ports [Puertos]

            port2["`Navegador
            localhost:1234`"]
        end
    end

    port2 --->|1234:80| proxy

    front <--- red-default
    proxy ---> red-default
```

Para el proxy 
se eligió el nombre de servicio 
`proxy-nginx`
y acepta conexiones por el puerto `80`.
Este puerto 80 (típicamente reservado en el *host*) 
es mapeado al puerto  **`1234`** del anfitrión.


### Organización de archivos


Se coloca el demo del *port mapping*
dentro del directorio `flet`, 
y a su lado se prepara
el directorio `nginx`
con los archivos de configuración necesarios:

```bash title="Demo proxy - Árbol de archivos"
.
├── compose.yml
├── flet
│   ├── demo
│   │   └── main.py
│   ├── Dockerfile
│   └── requirements.txt
└── nginx
    ├── default.conf
    └── Dockerfile
```

### Imagen del proxy

El archivo de configuración necesario
para el proxy
es el archivo `default.conf`.
En él se definen las rutas de entrada al proxy
y a qué URL deben ser redirigidas.
El destino es el contenedor del servidor Flet,
cuya URL está formada por su nombre de servicio
y su puerto de escucha.


```conf hl_lines="3-4 11-12 23-24" title="Demo proxy - default.conf"
server {
  # puerto en escucha: 80 (default)
  listen 80;
  listen [::]:80;

  server_name _;

  ### Redirección a sitio con WebSockets

  # petición a ruta '/'
  location / {
      proxy_pass         http://webapp-flet:8000/;
      proxy_http_version 1.1;
      proxy_set_header   Upgrade $http_upgrade;
      proxy_set_header   Connection keep-alive;
      proxy_set_header   Host $host;
      proxy_cache_bypass $http_upgrade;
      proxy_set_header   X-Forwarded-For $proxy_add_x_forwarded_for;
      proxy_set_header   X-Forwarded-Proto $scheme;
  }

  # petición a ruta '/ws'
  location /ws {
      proxy_pass         http://webapp-flet:8000/ws;
      proxy_http_version 1.1;
      proxy_set_header   Upgrade $http_upgrade;
      proxy_set_header   Connection "upgrade";
      proxy_set_header   Host $host;
      proxy_cache_bypass $http_upgrade;
      proxy_set_header   X-Forwarded-For $proxy_add_x_forwarded_for;
      proxy_set_header   X-Forwarded-Proto $scheme;
  }

}
```

Nótese las peticiones que el servidor proxy recibe 
en la URL `http://proxy-nginx:80/`
son redireccionadas
a la URL `http://webapp-flet:8000/`,
que corresponde al otro contenedor. 
El proxy requiere **redirección doble**
(`/` y `/ws`)
porque la *webapp* utiliza WebSockets. 

Este archivo es integrado en una nueva imagen
derivada de NGINX
con ayuda del archivo Dockerfile
en la ruta `/etc/nginx/conf.d/default.conf`:


```Dockerfile title="Demo proxy - Dockerfile (NGINX)"
# imagen de base: NGINX
FROM nginx

# copia del archivo de configuracion
COPY default.conf /etc/nginx/conf.d/default.conf
```


### Despliegue

El despliegue de ambos contenedores
se orquesta con el archivo Compose adaptado,
el cual ahora apunta a ambos Dockerfiles.
La creación y uso de una *network* *custom* es opcional.

```yaml title="Demo proxy - compose.yml"
name: demo-redes-proxy

services:

  webapp-flet:    
    build: flet/        
    image: webapp-flet
    networks:
      - red-proxy

  proxy-nginx:
    build: nginx/
    image: proxy-nginx
    command: [nginx, '-g', 'daemon off;']
    ports:
      - 1234:80
    tty: true
    stdin_open: true
    depends_on:
      - webapp-flet
    networks:
      - red-proxy


networks:
  red-proxy:
```



Se despliega el proyecto:

```bash title="Demo proxy - Despliegue"
podman compose up -d
```

y ahora el navegador web debe poder acceder 
a la página demo 
desde el [puerto **`1234`**](http://localhost:1234).
<!-- 
[Click para entrar al demo](http://localhost:1234){.md-button .md-button--primary}

 -->

## Manejo manual

Al igual que con otros elementos de los contenedores,
a veces es necesario manipular las redes mediante comandos.

Las redes existentes se enumeran con el comando `list`:

```bash title="Networks - Listado"
podman network list
```

y la inspección de las mismas
se realiza con el comando `inspect`:

```bash title="Networks - Inspección"
podman network inspect NOMBRE_RED
```

Una red se puede crear y asignarle un nombre
con el comando `create`:

```bash title="Networks - Creación"
podman network create NOMBRE_RED
```

El borrado de las redes no usadas actualmente
se realiza con el comando `prune`:

```bash title="Networks - Poda"
podman network prune
```

y la eliminación manual de redes específicas
se hace con `remove`:

```bash title="Networks - Borrado"
podman network remove NOMBRE_RED
```

!!! tip "Redes huérfanas"

    A veces quedan *networks* huérfanas
    que impiden desplegar los proyectos
    cuando su estructura es modificada.
    Esto se soluciona eliminando estas redes
    de manera manual con `prune` o `remove`.



## Referencias


[DockerDocs - Define and manage networks in Docker Compose](https://docs.docker.com/reference/compose-file/networks/)


[Docker Docs - Network drivers](https://docs.docker.com/engine/network/drivers/)

[Medium - [DevOps] Setting up a Docker Reverse Proxy Nginx — Multiple local apps](https://blog.devops.dev/devops-setting-up-a-docker-reverse-proxy-nginx-multiple-local-apps-21b6f03eefa0)

[Flet.dev - Self Hosting](https://flet.dev/docs/publish/web/dynamic-website/hosting/self-hosting/)