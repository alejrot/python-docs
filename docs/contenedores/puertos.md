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


El protocolo usado por el puerto puede ser indicado:

```yaml title="compose.yml - port mapping (con protocolos)"
services:

  servicio_ip:
    image: imagen-servicio
    ports:
      - puerto_host:puerto_contenedor/protocolo
```

donde las elecciones disponibles son `tcp` y `udp`.
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

- UDP está pensado para transmitir datos en directo,
sin asegurar la llegada de datos a destino.
Es usado por ejemplo por *streams* en vivo de audio y video.









```yaml
name: demo_red

services:

  base_datos:
    restart: always
    image: postgres:17.2-bookworm     
    environment:
      POSTGRES_USER:     noname
      POSTGRES_PASSWORD: 123456
      POSTGRES_DB:       test-red
    ports:
      - 9000:5432
    volumes:
      - volumen_db:/var/lib/postgresql/data


volumes:
  volumen_db:
```