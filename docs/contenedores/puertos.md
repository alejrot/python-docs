---
status: new
---

# Port Mapping


El *port mapping* o mapeo de puertos le permite
a las aplicaciones del sistema anfitrión
comunicarse con los contenedores 
mediante conexiones IP.

<!-- 
Se trata de crear una equivalencia entre un puerto del sistema anfitrión
y un puerto de un contenedor del proyecto.
 -->

Funciona de manera similar a un proxy reverso:
los clientes hacen una petición 
a la IP del gestor de contenedores
y éste redirige el tráfico
a alguno de los contenedores en actividad
en base al puerto usado.

Por ejemplo, si el cliente y los contenedores
corren en el mismo equipo
la petición se hace al `localhost`:

``` title="Port mapping - en local"
localhost:puerto_host --> contenedor:puerto_contenedor
```

Más sobre las IPs y sus conceptos relacionados: [ver anexo](../anexos/redes/ip.md)


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


El protocolo usado por el puerto
puede ser especificado de manera opcional:
 
```yaml title="compose.yml - port mapping (con protocolos)"
services:

  servicio_ip:
    image: imagen-servicio
    ports:
      - puerto_host:puerto_contenedor/protocolo
```

donde las elecciones disponibles son `tcp` y `udp`.
Véase el [anexo sobre TCP y UDP](../anexos/redes/tcp_udp.md) para más información.


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
    image: postgres:17.2-bookworm 
    ports:
      - 9999:5432
    # otras configuraciones
    restart: always
    volumes:
      - /var/lib/postgresql/data
    environment:
      POSTGRES_USER:     noname
      POSTGRES_PASSWORD: 123456
      POSTGRES_DB:       test-red
```


Más sobre las imágenes de PostgreSQL: [DockerHub](https://hub.docker.com/_/postgres/)