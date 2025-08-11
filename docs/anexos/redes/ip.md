---
status: new
date: 2025-08-11
---


# Protocolo IP

## Introducción

El protocolo IP es la base para implementar 
todo tipo de servicios, tanto en local como en remoto:
paginas web, streamings de audio y video, correos electrónicos, transferencia de archivos, etc.

La información a transmitir entre las partes
no se envía entera
sino que es partida en pequeños trozos 
llamados **paquetes** o *packets*.


## Dirección IP

En este protocolo
cada equipo dispone de un indicador numérico configurable
conocido como **dirección IP**.
La forma más habitual de indicar la dirección IP
es mediante la notación de cuatro octetos (`x.x.x.x`)
donde cada `x` es un número entero entre el 0 y el 255.

La IP `0.0.0.0` se usa como un comodín,
en tanto que la IP `127.0.0.1` **siempre** apunta al equipo actual.





## Puertos

Un mismo equipo
soporta múltiples servicios basados en IP
pero diferenciados por un número entero carácterístico,
que es llamado **puerto**.
Este número está comprendido
entre el 1 y el 65535.




Algunos puertos de uso habitual en desarrollo:

|Puerto| Uso|
|:---:|:---:|
|3306| bases de datos MySQL/MariaDB|
|5432| bases de datos PostgreSQL|
|5000| servicios de frontend (típico)|
|8000| servicios de backend/webapps (típico)|


!!! info "Puertos reservados"

    Los primeros 1023 puertos son usualmente reservados
    para protocolos estandarizados:
    80 para HTTP, 443 para SSH y HTTPS, etc.

!!! info "Puertos dinámicos"

    Los puertos desde el 49152 en  adelante son usados por los clientes de manera temporal.


<!-- 

## Redes
Para que dos equipos puedan comunicarse entre sí
deben formar parte de una misma red.
Esto obliga a que 
 -->

<!-- 
## URL

A las direcciones IP se les puede colocar un identificador

El formato más general de 

esquema://usuario:contraseña@maquina:puerto/directorio/archivo
 -->


## Modelo cliente - servidor


El protocolo IP se basa en el modelo cliente-servidor.
El cliente es el equipo o programa que pide conectarse
a un servicio, en tanto que el servidor
es un equipo o programa
que proporciona un servicio y para ello queda "escuchando",
esto es que queda en espera
a que algun cliente intente conectarse
y entonces comienza la comunicación entre ambos,
la cual es bidireccional.

El servidor debe tener una dirección IP estática
para poder ser accedido,
en tanto que el cliente puede tener dirección dinámica o estática. 


!!! tip "Localhost"

    La IP `127.0.0.1` representa al equipo del cliente
    y se la llama habitualmente `localhost`.
    Esta IP sirve para realizar la conexión con servicios
    que se ejecutan desde el mismo sistema del cliente. 


