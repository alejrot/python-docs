---
status: new
date:
    created: 2025-10-09
    updated: 2025-10-09
---

# Archivos de Exclusión

Con el fin de prevenir
la copia accidental de ciertos archivos
desde el directorio del proyecto
a la nueva imagen
se implementan
los archivos ocultos
*dockerignore*.
En ellos se listan
aquellos archivos y carpetas
que deban ser ignorados
durante la construcción.

Ejemplo:

```py title="Dockerignore - Ejemplo para programas Python"
# codigo objeto de Python (CPython)
__pycache__/

# carpeta del control de versiones Git
.git/

# cachés de recursos remotos
.cache

# carpetas de entornos virtuales
venv/
.venv/

# archivos con variables de entorno
.env
*.env

# archivos de documentación Markdown
*.md

# (etc)
```


Estos archivos siguen las mismas reglas
que los archivos *gitignore*
utilizados por Git.
De hecho se puede tomar como referencia
el archivo `.gitignore`
para completar el archivo `.dockerignore`.