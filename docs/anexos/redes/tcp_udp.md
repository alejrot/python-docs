---
status: new
date: 2025-08-11
---

# Políticas de transmisión


Hay dos grande familias de conexiones basadas en IP
que son TCP y UDP.
Estas se diferencian en las políticas de entrega de paquetes de información: si hay confirmación de recepción de cada paquete,
si hay pedido de comunicación previo a la transferencia, etc.

## TCP

TCP (*Transmission Control Protocol*) está pensado para asegurar la transimisión
de los paquetes de datos entre el cliente y el servidor.
Los servicios de sitios web,
correos electrónicos,
tranferencia de archivos,
interacciones con bases de datos,
etc. se basan en TCP. 

La conexión TCP entre cliente y servidor
se realiza en tres pasos (*"3-way handshake"*):

1. el cliente envía un paquete al servidor pidiendo la conexión;
1. el servidor responde con un paquete aceptando o rechazando la conexión;
1. el cliente responde al paquete de respuesta con su propia confirmación,
el paquete `ACK` (*acknowledged*).

Si la conexión fue aceptada,
ambas partes pueden enviarse paquetes de información entre sí
y su llegada debe ser confirmada:

- una de las partes envía sus paquetes de datos por la red;
- su contraparte responde con un paquete `ACK`
por cada paquete recibido en tiempo real;
- si el emisor no recibe el `ACK`
de alguno de los paquetes que envió
dentro del tiempo limite preestablecido
entonces reenvía ese paquete particular.  

Este mecanismo asegura la llegada de los paquetes a destino
pero también puede ralentizar dramáticamente la velocidad de transferencia de datos
cuando la conexión es inestable.

!!! info "Ventana deslizante"

    Tanto el cliente como el servidor implementan
    el monitoreo de los paquetes enviados
    mediante un sistema de ventana deslizante con ancho limitado
    que funciona como una cola (FIFO):
    si el paquete mas antiguo de la ventana debe ser reenviado
    los más recientes ya enviados no pueden ser reemplazados
    por otros paquetes pendientes. 


La desconexión se hace en cuatro pasos (*"four-way handshake"*)
dando lugar a una "desconexion amable":

1. el cliente envía el paquete `FIN` al servidor;
2. el servidor responde con `ACK`;
3. el servidor envía su propio paquete `FIN` al cliente;
4. el cliente responde con `ACK`.



## UDP

UDP (*User Datagram Protocol*) está pensado para transmitir
los paquetes de datos en tiempo real,
sin asegurar su llegada a destino:
no hay paquete de respuesta
ni tampoco reenvío de paquetes.

En este protocolo hay dos variantes de uso,
que son los datagramas conectados
y los datagramas sin conexión:

- en el caso de los datagramas conectados
el cliente pide conectarse al servidor
y este responde.
De esta forma el cliente puede saber que el servidor ha estado disponible,
al menos al comienzo;
- en el caso de los datagramas desconectados
no hay intento de conexión previo a la transmisión,
por lo cual el emisor no sabe si hay al menos
Esta opción es usada por ejemplo
para emitir *streams* en vivo de audio y video.






## Referencias

[Wikipedia - TCP](https://es.wikipedia.org/wiki/Protocolo_de_control_de_transmisi%C3%B3n)

[Wikipedia - UDP](https://es.wikipedia.org/wiki/Protocolo_de_datagramas_de_usuario)