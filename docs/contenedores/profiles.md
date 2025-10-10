# Profiles

Los perfiles permiten la ejecución condicional
de los contenedores del proyecto.

## Definición

Cada contenedor admite
un campo opcional llamado `profile`.
En él se define al menos
un nombre de perfil a implementar:

```yml
services:

  servicio:
    image: imagen_servicio
    profiles:
      [perfil]
```

Los contenedores que posean
este campo definido
sólo se ejecutarán
si el nombre de perfil elegido
ha sido activado desde la *shell*.
En cambio, los contenedores
que no fueron asignados
a ningún perfil
se pondrán en marcha siempre.

Un mismo contenedor
puede tener asignados
varios perfiles:

```yml
services:

  servicio:
    image: imagen_servicio
    profiles:
      [perfil_1, perfil_2, ...]
```
en este caso el contenedor
será habilitado si al menos uno
de los perfiles indicados es activado.

## Despliegue por perfil

Los perfiles se activan de varias maneras.
Una de ellas es agregando la opción `profile`
al comando `compose`:

```bash
podman compose  --profile perfil  up
``` 
Si se necesita activar varios perfiles al mismo tiempo
esto se hace indicano varias veces la opción `profile`,
una por cada perfil a activar:

```bash
podman compose  --profile perfil_1 --profile perfil_2  up
``` 

La otra opción es recurrir
a la variable de entorno `COMPOSE_PROFILES`:

```bash
export COMPOSE_PROFILES=perfil
podman compose up
```

La asignación de múltiples perfiles
se realiza separando los nombres de perfil
con comas:

```bash
export COMPOSE_PROFILES=perfil_1,perfil_2 
podman compose up
```

## Detención por perfil

Los perfiles también
afectan a la detención de los contenedores
mediante el comando `down`.
La parada por perfil
se realiza
agregando la opción `profile`:

```bash
podman compose  --profile perfil  down
``` 
o mediante su variable de entorno:

```bash
export COMPOSE_PROFILES=perfil
podman compose down
```

Los contenedores detenidos serán:

- los que tengan asignado el perfil (o los perfiles) indicado;
- aquellos que no tengan ningún perfil asignado.

Si hay contenedores
asignados a otros perfiles
en funcionamiento
entonces éstos seguirán funcionando normalmente.


## Resolución de dependencias

Cada contenedor del proyecto
puede ser invocado directamente
por su nombre de servicio.
Para ello se utiliza el comando `run`:

```bash
podman compose run nombre_servicio
```

De esta manera
sólo se arranca:

- el servicio especificado;
- sus dependencias especificadas
por el campo `depends_on`;
- aquellos servicios con los perfiles cargados
mediante la opción `profile`
o la variable `COMPOSE_PROFILES`. 


## Referencias



[Docker Docs - Using profiles with Compose](https://docs.docker.com/compose/how-tos/profiles/)

[Docker Docs - Learn how to use profiles in Docker Compose](https://docs.docker.com/reference/compose-file/profiles/)