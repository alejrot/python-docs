# Incluir archivos Compose

Un archivo `compose.yml`
puede hacer referencia a otros archivos
del mismo tipo.
Esto permite desplegar múltiples
subproyectos como si fueran uno solo.
También permite modificar
las condiciones del despliegue
sin alterar los archivos `compose.yml` originales. 


## Uso básico

La forma más básica de uso
es definiendo una lista
de rutas 
en la seccón `include`:


```yml title="Incluir - Sintaxis corta"
# archivo  'compose.yml'

# archivos incluidos
include:
  - ruta_1/compose.yml
  - ruta_2/compose.yml

# contenedores agregados
services:
  servicio_extra:
    depends_on:
      - servicio_original
```

Las rutas especificadas
son relativas al archivo actual.


## Sintaxis larga

Hay una segunda forma
para indicar las rutas
que es la notación larga.

```yml title="Incluir - Sintaxis larga"
# archivo  'compose.yml' 

# archivos incluidos
include:
   - path: ruta_1/compose.yml
     project_directory: .
     env_file: custom.env

# contenedores agregados
services:
  servicio_extra:
    depends_on:
      - servicio_original
```


En esta se indican hasta tres rutas:

- `project_directory` es la ruta de referencia
para las otras rutas.
Por *default* es la ubicación
del archivo YAML aglutinante;
- `path` es la ruta relativa al archivo Compose a incluir.
- `env_file` es la ruta relativa al archivo
con las variables de entorno a importar.

Tanto `path` como `env_file`
admiten listas de rutas como entrada:

```yml title="Incluir - Sintaxis larga"
# archivo 'compose.yml'

# archivos incluidos
include:
   - path: 
      - ruta_1/compose.yml
      - ruta_2/compose.yml
     project_directory: .
     env_file: 
      - custom.env
      - ruta_extra/custom-extra.env
```

## Mezclar parámetros

A veces es necesario modificar o agregar
parámetros de configuración
para los contenedores
que ya están definidos
en los archivos Compose incluidos.

Esto se consigue mediante la notación larga,
incluyendo un archivo en `path`
con los cambios y agregados necesarios:

```yml title="Incluir - Sobreescritura" hl_lines="5"
# archivo 'compose.yml' 
include:
  - path:
    - ruta_original/compose.yml
    - override.yml
```
A este segundo archivo
habitualmente se lo nombra `override.yml`.

Por ejemplo:
un archivo compose podría

```yml title="Ejemplo - configuración original"
# archivo  'compose.yml' 
services:

  # Definición original
  servicio-web:
    build: .
    restart: always
    ports:
      - 9999:8000
    environment:
      VARIABLE:"valor original"  
```

A este contenedor
se lo altera con ayuda de otro archivo YML:


```yml title="Ejemplo - modificaciones"
# archivo  'override.yml' 
services:

  servicio-web:
    # sobreescritura de parámetros
    ports:
      - 7777:8000
    environment:
      VARIABLE:"valor sustituto"  
```

El despliegue resultante es el descrito a continuación:

```yml title="Ejemplo - resultado"
# resultante
services:

  servicio-web:
    build: .
    restart: always
    ports:
      - 9999:8000
      - 7777:8000
    environment:
      VARIABLE:"valor sustituto"  
```

La clave de entorno 
ve su valor sobreescrito
en tanto que el nuevo puerto
de acceso al *container*
es agregado junto al original.


## Sobreescribir variables

Mediante la sintaxis larga
se puede ignorar a
los archivos de entorno originales
de cada proyecto
y definir las variables de entorno
en nuevos archivos
para el despliegue actual:

```yml title="Incluir - Archivos de entorno"
# archivo  'compose.yml' 
include:
  - path: 
    - ruta_1/compose.yml
    env_file:
      - custom.env
```



## Referencias



[Docker Docs - Compose File Reference - Use include to modularize Compose files](https://docs.docker.com/reference/compose-file/include/)

