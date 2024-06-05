# PythonDocs

Mis apuntes en español acerca del lenguaje Python y algunos de sus módulos y paquetes.

[Enlace a documentos internos](docs/index.md)


## [Versión online : GitHub Pages](https://marcelomarot.github.io/PythonDocs/)

Este documento usa [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) para crear el sitio estático. 

## Despliegue local

### Descarga del repositorio:
```bash
git clone https://github.com/MarceloMarot/PythonDocs
cd PythonDocs
```


### Entorno virtual (opcional)

```bash
py -m venv venv
source venv/Scripts/activate        # caso Windows
source venv/bin/activate            # caso GNU/Linux    
```

### Ejecucion (*live server*)


```bash
pip install mkdocs-material
mkdocs serve
```

Ruta del sitio web local: localhost (IP 127.0.0.1), puerto 8000

```bash
http://localhost:8000 
```

