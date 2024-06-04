<a name="top"></a>

## [Volver](../Python.md#comandos-del-sistema-operativo---modulo-os)


## Comandos del Sistema Operativo - Modulo OS


El modulo de interacción con el sistema operativo se llama **os**. Éste debe importarse para su uso:

```python
import os
```



Se puede pedir la eliminación de un archivo mediante la función ***remove()***:
```python
os.remove(ruta_archivo)
```


## Listar archivos en directorio

Éste incluye un surtido de funciones predeterminadas para ejercer acciones con ayuda del sistema operativo.Ejemplo:

```python
os.getcwd() 	# Ver directorio actual de trabajo
os.chdir( ruta ) 	# Cambiar directorio actual de trabajo
os.listdir()    # Archivos y subcarpetas del directorio actual
```

También incluye la función system() que permite ejecutar los comandos de la terminal, pero su funcionamiento depende del sistema operativo. Ejemplo con comandos Linux /Bash:

```python
os.system(“ls -l”)  # Da una lista de todos los archivos y carpetas visibles
os.system(“ls -la”) # Lista también todos los archivos y carpetas ocultos
```


----
----
----

## [Inicio](#comandos-del-sistema-operativo---modulo-os) 

## [Volver](../Python.md#comandos-del-sistema-operativo---modulo-os)