---
date:
    created: 2025-03-23
    updated: 2025-08-18
---

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


## Verificar consistencia

El comando `check` verifica que el archivo LOCK
y el archivo TOML
sean consistentes entre sí.

```bash title="Verificar consistencia"
poetry check
```


## Sincronización de dependencias


Con el comando `sync` se descartan
todas las dependencias instaladas
que no aparezcan en el archivo LOCK
e instala aquellas dependencias que faltan.


Uso básico:

```bash title="Instalar dependencias - archivo LOCK"
poetry sync
```

!!! info "sync vs install"

    El comando `sync` funciona de manera similar a `install`
    pero tomando el archivo LOCK como referencia
    en vez de usar el archivo TOML.

## Sincronización por grupos

`sync` admite la sincronización las dependencias instaladas
en base a un grupo predefinido específico:

```bash title="Instalar dependencias - archivo LOCK (por grupos)"
poetry sync --with nombre_grupo
poetry sync --without nombre_grupo
poetry sync --only nombre_grupo
```

Las opciones son las mismas disponibles en el comando `install`.



## Fijar dependencias


El comando `lock` crea o actualiza el archivo LOCK
pero sin instalar las dependencias en el entorno virtual.

Uso:

```bash title="Fijar dependencias"
poetry lock
```
