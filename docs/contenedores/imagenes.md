# Imágenes de Python

## Introducción

Las imágenes son las copias del software
que le dan funcionalidad a los contenedores.
Son el equivalente a las imágenes de instalación
de los sistemas operativos.

Cada imagen tiene un nombre característico
y una etiqueta de versión asignada.
Tambien suelen usarse las etiquetas `latest`, `stable`, etc.
a modo de comodines para apuntar a versiones recomendadas de las imágenes.


En [Docker Hub](https://hub.docker.com/) se dispone de un [surtido de imágenes de Python](https://hub.docker.com/_/python)
las cuales ya traen el intérprete de Python preinstalado
y son las recomendadas para trabajar.


Las imágenes de Python prearmadas se distinguen
unas de otras por los siguientes factores:

- versión del intérprete Python, indicado por su versión:
`3.9`, `3.10`, etc;
- distribución de origen;
- componentes adicionales;
- plataforma de uso.

Estas son las distribuciones compatibles
con su ejecución en PC:

|Nombre clave | Distribución base| 
|:---|:---:|
|`bookworm`| Debian 12|
|`bullseye`| Debian 11|
|`alpine`| Alpine|
<!-- |`windowsservercore`|Windows Server Core| -->


El comando `pull` sirve para descargar imágenes.
Por ejemplo para descargar la imagen predefinida de Python :

```bash
podman image pull python
```

La imagen descargada por *default* es es la etiquetada como `latest`.
Para descargar una imagen en particular
se indica la etiqueta elegida:

```bash
podman image pull python:tag_version
```

Por ejemplo, para descargar varias imágenes
de Python con el intérprete 3.13.5:

```bash
podman image pull python:latest
podman image pull python:3.13.5-bookworm
podman image pull python:3.13.5-slim-bookworm
podman image pull python:3.13.5-alpine3.22
```


## Imágenes de Debian

Las imágenes etiquetadas como `bookworm` y `bullseye`
han sido creadas en base a imágenes del sistema operativo Debian.
Éstas son las imágenes completas,
y son también las más pesadas.
Sus bibliotecas de utilitarios son
`glibc` (GNU C library) y `coreutils` (GNU coreutils),
que son las bibliotecas más habituales en los entornos GNU/Linux.

<!-- 
Las imágenes basadas en Debian son las predefinidas
La imagen predefinida más reciente `latest`
 -->

## Imágenes *slim*

Las imágenes etiquetadas como `slim`
son versiones "adelgazadas" de las imágenes
basadas en Debian,
las cuales ocupan mucho menos espacio
que las originales en solitario.
Sin embargo,
estas imágenes pueden ocupar más espacio
que las originales cuando hay varias versiones
y además
su funcionalidad en aplicaciones exigentes puede ser inferior.



## Imágenes de Alpine

Alpine Linux es una distribución GNU/Linux
cuyas bibliotecas de utilitarios son `musl libc` y `Busybox`.
Estas imágenes de disco son muy compactas,
permitiendo crear imágenes muy livianas;
no obstante pueden dar lugar a 
comportamientos y errores inesperados
en el caso de aplicaciones demandantes.




## Comparativa de espacios


Para ver las características
de las imágenes ya descargadas
se tiene el comando `list`:


```bash
podman image list python
```

Esta tabla es un ejemplo de reporte resumido
tras descargar varias imágenes de Python:

| TAG | IMAGE ID |   SIZE |
|:---|:---:|---:|
| `latest`               | 3b29f43b7fff | 1.04 GB |
| `3.13.5-bookworm`      | 3b29f43b7fff | 1.04 GB |
| `3.13.5-slim-bookworm` | 300924e3c7de | 125 MB  |
| `3.13.5-alpine3.22`    | f3abd857d733 | 47.6 MB |


Nótese que al momento de la redacción
la etiqueta `latest` coincide con la imagen `3.13.5-bookworm` 
basada en Debian y que tiene el intérprete 3.13.5


!!! info "Capas (*layers*)"

    Las imágenes de contenedores no son monolíticas
    sino que están divididas en varias secciones
    llamadas capas o *layers*.
    Las capas son reutilizadas por el gestor de contenedores
    para varias imágenes cuando esto es posible.
    Esto ayuda a que el espacio ocupado en el almacenamiento por las imágenes no sea exageradamente grande.


