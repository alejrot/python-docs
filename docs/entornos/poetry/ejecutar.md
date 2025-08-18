---
date:
    created: 2025-03-23
    updated: 2025-08-18
---


# Ejecución

Aquí se explica cómo ejecutar
los programas gestionados por Poetry
de la manera más simple posible.


## Ejecución directa

El comando `run` de Poetry permite ejecutar las rutinas del proyecto 
al tiempo que carga las dependencias:

```bash title="Entorno virtual - comando run"
poetry run python nombre_rutina
```


## Ejecución desde entorno virtual


El entorno virtual de Poetry se activa en Bash con la siguiente expresión:

```bash title="Entorno virtual - activar"
eval $(poetry env activate)
```

de esta manera el intérprete de Python puede ser llamado directamente:

```bash title="Entorno virtual - ejecutar rutina"
python nombre_rutina
```

Por último,
se dispone del comando `deactivate`
para deshabilitar el entorno actual:

```bash title="Entorno virtual - desactivar"
deactivate
```


!!! warning "Entornos VENV"

    Si en la carpeta del proyecto actual
    hay un entorno virtual creado por VENV
    es posible que se active este último
    en vez del entorno virtual gestionado por Poetry.
