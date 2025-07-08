---
status: new
---

# Port Mapping


El *port mapping* o mapeo de puertos le permite
a las aplicaciones del sistema anfitrión
comunicarse con los contenedores 
mediante conexiones IP.
Se trata de crear una equivalencia entre un puerto del sistema anfitrión
y un puerto de un contenedor del proyecto.


## Sintaxis

A cada contenedor que necesite ser accedido desde el exterior
se le configura el parámetro `ports`
asignando los números de los puertos de a pares:

```yaml title="compose.yml - port mapping"
services:

  servicio_ip:
    image: imagen-servicio
    ports:
      - puerto_host:puerto_contenedor
```

Un mismo contenedor puede tener varios puertos mapeados
hacia el *host*.


El protocolo usado por el puerto puede ser especificado también:
 
```yaml title="compose.yml - port mapping (con protocolos)"
services:

  servicio_ip:
    image: imagen-servicio
    ports:
      - puerto_host:puerto_contenedor/protocolo
```

donde las elecciones disponibles son `tcp` y `udp`.

!!! info "TCP vs UPD" 

    Estas son las diferencias entre los dos protocolos:

    - TCP está pensado para asegurar la transimisión
    de los paquetes de datos entre el cliente y el servidor,
    para ello implementa el reporte de paquetes recibidos
    y políticas de reenvío de paquetes faltantes o dañados.
    Los servicios de sitios web,
    correos electrónicos,
    tranferencia de archivos,
    interacciones con bases de datos,
    etc. se basan en TCP. 

    - UDP está pensado para transmitir
    los paquetes de datos en tiempo real,
    sin asegurar su llegada a destino.
    Es usado por ejemplo por *streams* en vivo de audio y video.



## Ejemplo

Supóngase por ejemplo el despliegue
de una base de datos.
En este ejemplo se eligió un gestor de bases de datos PostgreSQL,
el cual por *default* acepta conexiones al puerto **5432**.
Para que el contenedor pueda ser consultado
se eligió arbitrariamente el puerto 9999
y además se necesita configurar algunos parámetros
como el nombre de usuario,
el nombre de la base de datos a crear
y una contraseña para el acceso,
lo que se hace con variables de entorno predefinidas.


```yaml hl_lines="7-9"
name: database_container 

services:

  base_datos:
    restart: always
    image: postgres:17.2-bookworm 
    ports:
      - 9999:5432
    volumes:
      - volumen_db:/var/lib/postgresql/data
    environment:
      POSTGRES_USER:     noname
      POSTGRES_PASSWORD: 123456
      POSTGRES_DB:       test-red


volumes:
  volumen_db:
```

Más sobre las imágenes de PostgreSQL: [DockerHub](https://hub.docker.com/_/postgres/)