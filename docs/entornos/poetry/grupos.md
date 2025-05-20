# Grupos de dependencias



Poetry permite clasificar las dependencias de un proyecto
en varios grupos.
Por ejemplo,
se puede crear en un mismo proyecto:

- un grupo *"dev"* con las actualizaciones más recientes; 
- un grupo *"stable"* para despliegue,
con dependencias más antiguas pero mejor probadas ; 
- un grupo *"test"* para hacer pruebas unitarias,
rutinas de *integración continua* (CI),
etc;
- etc.

Esto permite cambiar rápidamente los paquetes instalados en un mismo entorno
en función de las necesidades del momento
y evitar instalar dependencias innecesarias.


## Definición

Los paquetes pueden repartirse en varios grupos 
agregando la opción `group` en el agregado:


```bash
poetry add --group nombre_grupo  paquete_1 paquete_2 ...
```

Ahora las dependencias aparecerán marcadas en el archivo TOML como parte de un grupo:

```
[tool.poetry.nombre_grupo.dependencies]
paquete_1 = ^1.2.3
paquete_2 = ^5.3.7
...
```

Para que la instalacion de estos paquetes sea opcional hay que modificar manualmente el archivo TOML y agregar el parametro `optional`:

```
[tool.poetry.nombre_grupo.ui]
optional = true
[tool.poetry.nombre_grupo.dependencies]
paquete_1 = ^1.2.3
paquete_2 = ^5.3.7
...
```

## Instalación

la instalación se realiza con el comando `install`,
al cual se le indica la opción de instalación requerida
y el grupo de referencia.

Instalar grupos opcionales:

```bash
poetry install --with nombre_grupo
```

Excluir grupos predefinidos:

```bash
poetry install --without nombre_grupo
```

Instalar sólo grupos específicos:

```bash
poetry install --only nombre_grupo
```

Instalar sólo dependencias no agrupadas (`main`)

```bash
poetry install --only main
```

## Actualización


Se actualizan los paquetes en base al archivo TOML presente. 

```bash
poetry update
```

<!-- 
## Sincronización de dependencias


Con el comando `sync` se descartan todas las dependencias que no aparezcan en el archivo LOCK.

Uso:

```bash
poetry sync
```

`sync` admite la sincronización en base a un grupo predefinido específico:

```bash
poetry sync --with nombre_grupo
poetry sync --without nombre_grupo
poetry sync --only nombre_grupo
```

 -->


## Remoción
 

Los paquetes pueden ser removidos de los grupos mediante el uso del comando `remove`:

```bash
poetry remove nombre_paquete --group  nombre_grupo
```

