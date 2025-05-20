

# Sincronización de dependencias



## Archivo LOCK


El archivo `poetry.lock` es el encargado de guardar la lista exhaustiva de los paquetes usados actualmente 
en el entorno actual
y sus dependencias,
cada uno con su número de versión.

Este archivo se crea automáticamente al instalar los paquetes con el comando `install`.
Si el archivo LOCK ya existe,
entonces `install` instalará la versión exacta de cada paquete especificado en él.

Este archivo ayuda a replicar de manera exacta la instalación de un proyecto en distintos entornos o equipos.


## Consistencia

El comando `check` verifica que el archivo LOCK
y el archivo TOML
sean consistentes entre sí.

```bash
poetry check
```


## Sincronización de dependencias


Con el comando `sync` se descartan todas las dependencias instaladas que no aparezcan en el archivo LOCK.

Uso básico:

```bash
poetry sync
```


## Sincronización por grupos

`sync` admite la sincronización las dependencias instaladas
en base a un grupo predefinido específico:

```bash
poetry sync --with nombre_grupo
poetry sync --without nombre_grupo
poetry sync --only nombre_grupo
```

Las opciones son las mismas disponibles en el comando `install`.

