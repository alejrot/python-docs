

# Módulo OS - Comandos del Sistema Operativo 


El módulo de interacción con el sistema operativo se llama **os**. Éste debe importarse para su uso:

```python title="importación"
import os
```

## Tratar con directorios

Éste incluye un surtido de funciones predeterminadas para ejercer acciones con ayuda del sistema operativo.

Ejemplo:

```python title="Operaciones con rutas de archivo"
os.getcwd() 	# Ver directorio actual de trabajo
os.chdir( ruta ) 	# Cambiar directorio actual de trabajo
os.listdir()    # Archivos y subcarpetas del directorio actual
```


## Ejecutar comandos

También incluye la función ***system()*** que permite ejecutar los comandos de la terminal, pero su funcionamiento depende del sistema operativo. Ejemplo con comandos Linux /Bash:

```python title="Comandos con os.system() "
os.system(“ls -l”)  # Da una lista de todos los archivos y carpetas visibles
os.system(“ls -la”) # Lista también todos los archivos y carpetas ocultos
```


## Eliminar archivos

Se puede pedir la eliminación de un archivo mediante la función ***remove()***:
```python title="eliminar archivo"
os.remove(ruta_archivo)
```



