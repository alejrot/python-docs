# Arranque secuencial


## Dependencia entre contenedores


El arranque de los contenedores de un mismo proyecto
se realiza en un un orden aleatorio de manera predefinida.
Para aquellos casos donde se requiera
que unos contenedores arranquen después que otros
se utiliza el campo
`depends_on`:


```yaml title="compose.yml - dependencia (simple)"
services:

  primero:
    image: imagen_1

  segundo:
    image: imagen_2
    depends_on: 
    - primero
```

Durante el despliegue el segundo contenedor se crea después del primero.
Durante la eliminación el segundo contenedor es removido primero.

Un contenedor puede depender de múltiples servicios al mismo tiempo.


## Opciones agregadas

A las dependencias de servicios
se les puede configurar varias opciones adicionales:

```yaml title="compose.yml - dependencia (avanzado)"
services:

  primero:
    image: imagen_1

  segundo:
    image: imagen_2
    depends_on: 
        primero:
            restart: true
            condition: service_started  # valor default
            required: true              # valor por default
```

1. El parámetro `condition` admite varias opciones
repecto al servicio apuntado:

    - `service_started`: el servicio debe haber arrancado;
    - `service_healthy`: el servicio debe estar funcionando correctamente, esto se comprueba con un test específico;
    - `service_completed_successfully`: el servicio debe completarse exitosamente.

2. El parámetro `restart` ordena el reinicio del contenedor en cuanto sus servicios requeridos estén listos.

3. El parámetro `required` especifica si es obligatorio
que el servicio apuntado haya sido arrancado o esté disponible.
Si es seteado como `false` entonces 
el comando `compose` sólo advertirá en caso
que el servicio requerido no está disponible,
no inició o finalizó de manera incorrecta.



## Test de servicio


Cuando se elige una dependencia del tipo `service_healthy`
es necesario que el servicio apuntado 
tenga definido un test de funcionamiento.
Esto se hace con el parámetro `healthcheck`:


```yaml title="compose.yml - dependencia (con healthcheck)"
services:

  primero:
    image: imagen_1
    healthcheck:
        test: ["CMD-SHELL", "comando_test_custom"]
        start-period: 10s   # demora para el primer test
        interval: 10s   # intervalo entre intentos
        timeout: 60s    # tiempo limite de test
        retries: 5      # nº máximo de reintentos  
        disabled: false # bypass del test - desactivado por default

  segundo:
    image: imagen_2
    depends_on: 
        primero:
            condition: service_healthy  
```

De esta manera el gestor de contenedores verifica
que el primer contenedor funcione adecuadamente
antes de intentar la puesta en marcha del segundo.




## Referencias


[Docker Docs - Compose file reference - depends_on](https://docs.docker.com/reference/compose-file/services/#depends_on)


[Docker Docs - Compose file reference - Healthcheck](https://docs.docker.com/reference/compose-file/services/#healthcheck)

[Docker Docs - Dockerfile reference - Healthcheck](https://docs.docker.com/reference/dockerfile/#healthcheck)