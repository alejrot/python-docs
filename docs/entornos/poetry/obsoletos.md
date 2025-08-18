---
date:
    created: 2025-03-23
    updated: 2025-08-18
# status: new
---

# Comandos antiguos



## Poetry Shell

El comando `shell` fue removido de Poetry desde la versión 2.0.0.
Este comando servía para activar el entorno virtual actual.


Puede instalarse mediante el plugin [poetry-plugin-shell](https://github.com/python-poetry/poetry-plugin-shell)
.

Opciones de instalación:

```bash title="Shell - instalar"
poetry self add poetry-plugin-shell
pipx inject poetry poetry-plugin-shell
pip install poetry-plugin-shell
```


Con la shell se activa el entorno predeterminado del proyecto,
tal como se hace con **venv**:

```bash title="Shell - actualizar"
poetry shell
```

y ahora la rutina se ejecuta llamando directamente al intérprete Python:

```bash title="Shell - ejecutar"
python nombre_rutina
```





## Export

El comando `export` era usado para extraer la lista de dependencias
desde el archivo TOML a un archivo TXT.

Este coamndo ha sido descartado de Poetry desde la versión 2.0.0.
Puede reintregrarse con el plugin externo [poetry-plugin-export](https://github.com/python-poetry/poetry-plugin-export)
.




