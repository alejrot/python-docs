---
date:
    created: 2025-09-27
    updated: 2025-09-27
---


# Contenedores de bases de datos



## URLs

Los contenedores 
de bases de datos
mostrados a continuación
normalmente aceptan peticiones mediante URLs
que cumplan con el siguiente formato: 

``` title="URLs típicas"
DATABASE_URL="mysql://USER:PASSWORD@NOMBRE_SERVICIO:PUERTO/NOMBRE_DATABASE"
```

!!! danger "Data sensible"

    Nótese que usuarios y contraseñas
    de las bases de datos **quedan expuestos**
    como parte de la URL,
    por tal motivo es vital
    limitar el acceso a las bases de datos
    mediante el uso de *networks* a medida.
    También debe tenerse cuidado
    de no registrar las URLs peticionadas
    mediante los *logs* de los programas clientes.



## Bases SQL

Las bases de datos SQL
son bases de datos relacionales,
las cuales guardan los datos
en forma de tablas.

A continuación se resumen los parámetros
para los sistemas de administración (RDBMS)
más habituales.

=== "MySQL"


    |Parámetro | Valor |
    |:---|:---|
    |**Conexión**|
    |puerto escucha| `3306`|
    |protocolo URL|`mysql://`|
    |**Volumenes**|
    |ruta de datos| `/var/lib/mysql`|
    |ruta de configuración| `/etc/mysql/conf.d`|
    |**Variables entorno** |
    |user| `MYSQL_USER` |
    |pass|`MYSQL_PASSWORD` |
    |database|`MYSQL_DATABASE` |
    |pass (root)|`MYSQL_ROOT_PASSWORD`|
    |**Secretos**|
    |user| `MYSQL_USER_FILE` |
    |pass|`MYSQL_PASSWORD_FILE` |
    |database|`MYSQL_DATABASE_FILE` |
    |pass (root)|`MYSQL_ROOT_PASSWORD_FILE`|

    Documentación oficial: [Docker Hub - MySQL](https://hub.docker.com/_/mysql)


=== "MariaDB"


    |Parámetro | Valor |
    |:---|:---|
    |**Conexión**|
    |puerto escucha| `3306`|
    |protocolo URL|`mariadb://`|
    |**Volumenes**|
    |ruta de datos| `/var/lib/mysql`|
    |ruta de backup| `/backup`|
    |ruta de configuración| `/etc/mysql/conf.d`|
    |**Variables entorno** |
    |user| `MARIADB_USER` |
    |pass|`MARIADB_PASSWORD` |
    |database|`MARIADB_DATABASE` |
    |pass (root)|`MARIADB_ROOT_PASSWORD`|
    |**Secretos**|
    |user|`MARIADB_USER_FILE`|
    |pass| `MARIADB_PASSWORD_FILE`|
    |database|`MARIADB_DATABASE_FILE` |
    |pass (root)|  `MARIADB_ROOT_PASSWORD_FILE`|


    Documentación oficial: [Docker Hub - MariaDB](https://hub.docker.com/_/mariadb)




=== "PostgreSQL"

    |Parámetro | Valor |
    |:---|:---|
    |**Conexión**|
    |puerto escucha| `5432`|
    |protocolo URL|`postgresql://`|
    |**Volumenes**|
    |ruta de datos| `/var/lib/postgresql/data`|
    |ruta de configuración| `/etc/postgresql/postgresql.conf`|
    |**Variables entorno** |
    |user| `POSTGRES_USER` |
    |pass|`POSTGRES_PASSWORD` |
    |database|`POSTGRES_DB` |
    |**Secretos**|
    |user| `POSTGRES_USER_FILE` |
    |pass|`POSTGRES_PASSWORD_FILE` |
    |database|`POSTGRES_DB_FILE` |



    Documentación oficial: [Docker Hub - PostgreSQL](https://hub.docker.com/_/postgres)


### Ejemplo de uso

Los tres gestores
de bases de datos SQL explicadas
se manejan de manera muy similar
en el entorno de los contenedores.
Se adjunta un ejemplo de uso básico
con una imagen PostgreSQL:

```yaml title="SQL - compose.yml (PostgreSQL)"
services:
  db-postgres:
    restart: always
    image: postgres:17.2-bookworm     
    ports:
      - ${PUERTO_DB:-5432}:5432
    volumes:
      - volumen_db:/var/lib/postgresql/data
    environment:
      POSTGRES_USER:     ${USUARIO}
      POSTGRES_DB:       ${NOMBRE_DB}
      POSTGRES_PASSWORD_FILE: /run/secrets/secreto_db
    secrets:
      - secreto_db

volumes:
  volumen_db:

secrets:
  secreto_db:
    file: ./secreto.txt    
```


## No SQL

Las bases de datos no relacionales
típicamente guardan los datos
en forma de diccionarios
(pares clave-valor).


### MongoDB

|Parámetro | Valor |
|:---|:---|
|**Conexión**|
|puerto escucha| `27017`|
|protocolo URL|`mongodb://`|
|**Volumenes**|
|ruta de datos| `/data/db`|
|**Variables entorno** |
|user (root)|`MONGO_INITDB_ROOT_USERNAME` |
|pass (root)|`MONGO_INITDB_ROOT_PASSWORD`|
|database|`MONGO_INITDB_DATABASE` |
|**Secretos**|
|user (root)|`MONGO_INITDB_ROOT_USERNAME_FILE` |
|pass (root)|`MONGO_INITDB_ROOT_PASSWORD_FILE`|


Documentación oficial: [Docker Hub - MongoDB](https://hub.docker.com/_/mongo)


### Redis

Redis es un motor de bases de datos
que almacena la información en memoria RAM,
aunque puede usarse como base de datos persistente.

|Parámetro | Valor |
|:---|:---|
|**Conexión**|
|puerto escucha| `6379`|
|protocolo URL|`redis://`|
|**Volumenes**|
|ruta de datos| `/data`|
|ruta de configuración| `/usr/local/etc/redis`|


Documentación oficial: [Docker Hub - Redis](https://hub.docker.com/_/redis)





## Healthchecks

En el [repositorio HEALTHCHEK](https://github.com/docker-library/healthcheck/tree/master)
de [Docker Library](https://github.com/docker-library/)
se proponen algunos tests genéricos
para comprobar el funcionamiento correcto
de algunas bases de datos habituales.


