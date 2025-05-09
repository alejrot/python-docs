---
tags:
  - venv
  - Modulos
  - Entornos
---

# Fundamentos de los entornos virtuales 


## Creación

Los entornos virtuales se construyen siguiendo los siguientes pasos:

1. Crear un directorio (es decir, una carpeta) independiente de la instalación de Python global,
típicamente en la ubicación del proyecto
o en una carpeta del usuario;
2. Crear una réplica del intérprete de Python o un enlace simbólico al mismo en el directorio.
3. Instalar los paquetes requeridos en dicho directorio,
permitiendo especificar qué versión se necesita de cada uno.


### Activación

Los entornos virtuales requieren activación para su uso.
La activación del entorno virtual consiste en modificar 
en la sesión actual (entiéndase la shell actual)
la variable **`PATH`** del sistema operativo,
colocándole al comienzo
la ruta del entorno virtual creado.

De esta manera el sistema operativo dará prioridad a los ejecutables y paquetes del entorno virtual respecto a sus equivalentes globales.

Por ejemplo: el intérprete global de Python en un sistema GNU/Linux
suele ser `/usr/bin/python`.
Dicha ruta puede ser consultada en la *shell* Bash con el comando `which`:

```bash title="Bash - Ruta de Python"
which python
```
Tras activar el entorno virtual,
al repetir la consulta el resultado cambia a una ruta de la forma `RUTA_ENTORNO/bin/python`.

Los cambios mencionados en la variable `PATH` pueden verificarse
con el comando:

```bash title="Bash - variable PATH"
echo $PATH
```

## Eliminación

Los entornos virtuales pueden ser eliminados fñacilmente mediante el borrado de su carpeta contenedora,
sin afectar en modo alguno a los entornos de otros proyectos ni al intérpete principal de Python.

## Ventajas e inconvenientes

El uso de entornos virtuales
introduce algunas ventajas respecto al uso del intérprete global:

- Cada proyecto puede tener una versión diferente de un mismo paquete,
evitando conflictos de instalación y de actualización;
- Se evita la carga de paquetes no incluidos en el proyecto,
permitiendo entornos mejor controlados para cada proyecto;
- Es posible agregar enlaces simbólicos de múltiples versiones de Python,
lo cual permite ejecutar el proyecto con distintas versiones del mismo.

Como contrapartida aumenta el espacio en disco ocupado,
por cuanto cada entorno virtual tiene su propia copia de los paquetes.

