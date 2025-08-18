---
date:
    created: 2025-08-18
    updated: 2025-08-18
---


# Empaquetar y publicar

Aquí se repasan los comandos más importantes
para crear paquetes distribuibles
y publicarlos. 


## Construir 


El comando `build` empaqueta el contenido del proyecto:

```bash title="Empaquetado - construir"
poetry build
```

creando la carpeta `dist` con dos distribuibles:

- un archivo comprimido TAR.GZ;
- un archivo .WHL (*Wheel Package*)


Agregando la opción `clean`
se asegura que se limpia el directorio de salida
antes de crear los nuevos paquetes:


```bash title="Empaquetado - construir (post limpieza)"
poetry build --clean
```




## Publicar


Las subidas a PyPI se hacen con el comando `publish`:


```bash title="Empaquetado - publicar"
poetry publish   # subida en PyPI
```

Las configuraciones de Poetry respecto al acceso
y la publicación de paquetes
se explican en la [seccion Repositories](https://python-poetry.org/docs/repositories/#supported-package-sources)
de su página oficial.