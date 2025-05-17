# Poetry



https://youtu.be/Ji2XDxmXSOM

https://python-poetry.org/docs/

https://www.datacamp.com/tutorial/python-poetry


[entornos](https://python-poetry.org/docs/managing-environments/#switching-between-environments)



## Configuración

Resumen:


```bash
poetry config --list
```




## Entornos virtuales


!!! info "PIPX"

    Poetry utiliza PIPX, que es una versíon mejorada de PIP con manejo mejorado de los paquetes. 


!!! info "Ubicacion de entornos"

    A diferencia de VENV, Poetry crea los entornos locales en una carpeta de usuario dedicada.
    Por ejemplo en Linux dicha carpeta puede ser:
    `~/.cache/pypoetry/virtualenv`






## Especificacion de versiones



| Simbolo | Significado | Ejemplo|
|---|---|---|
| `^` |Sólo actualizaciones menores y patches | `n.x.x` |
| `~` | Sólo actualizaciones patch | `n.m.x` |
| `@` | Version exacta | `n.m.o` |
| `>` | Version superior a  | más reciente que `n.m.o` |
| `>=` | Version igual o superior a  | `n.m.o` o más reciente |
| `<` | Version inferior a  | más antiguo que `n.m.o` |
| `<=` | Version igual o inferior a  | `n.m.o` o más antiguo |
| `>=n.m.o, <=w.y.z` | Rango de versiones  | `n.m.o` a `w.y.z` |
|`*`| Comodín| `n.m.*` |


**REVISAR**


## Grupos de dependencias

### definicion

Los paquetes pueden repartirse en varios grupos 

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

### instalacion

Instalar grupos opcionales:


```bash
poetry install --with nombre_grupo
```

Excluir grupos predefinidos:

```bash
poetry install --without nombre_grupo
```


Instalar sólo grupos específicos


```bash
poetry install --only nombre_grupo
```

Instalar sólo dependencias no agrupadas (`main`)

```bash
poetry install --only main
```

### Actualizacion


Se actualizan los paquetes en base al archivo TOML presente. 

```bash
poetry update
```


### Sincronización de dependencias


Con el comando `sync` se descartan todas las dependencias que no aparezcan en el archivo LOCK.

Uso:

```bash
poetry sync
```

se admite la sincronización en base a un grupo específico

```bash
poetry sync --with nombre_grupo
poetry sync --without nombre_grupo
poetry sync --only nombre_grupo
```

### Remoción
 

Los paquetes pueden ser removidos de los grupos mediante el uso de comandos:

```bash
poetry remove nombre_paquete --group  nombre_grupo
```



## Archivo Lock


El archivo `poetry.lock` es el encargado de guardar la lista exhaustiva de los paquetes usados actualmente y sus dependencias,
cada uno con su número de versión.

Este archivo se crea automáticamente al instalar los paquetes con el comando `install`.
Si el archivo Lock ya existe, entonces `install` instalará la versión exacta de cada paquete especificado en él.


### Consistencia

El comando `check` verifica que el archivo LOCK
y el archivo TOML
sean consistentes entre sí.

```bash
poetry check
```





## Publicar


El comando `build` compila el proyecto como nuevo paquete: 


```bash
poetry build     # construir distribucion
```
y con él se crea el archivo comprimido TAR.GZ


Las subida a PIP se hace con el comando `publish`


```bash
poetry publish   # subida en PIP
```





!!! warning "KDE Wallet"

    deshabilitar:

    ```bash
    python3 -m keyring --disable
    ```

    https://stackoverflow.com/questions/64570510/why-does-pip3-want-to-create-a-kdewallet-after-installing-updating-packages-on-us









