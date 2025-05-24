# Poetry



https://youtu.be/Ji2XDxmXSOM

https://python-poetry.org/docs/

https://www.datacamp.com/tutorial/python-poetry


[entornos](https://python-poetry.org/docs/managing-environments/#switching-between-environments)


<!-- 
## Configuración

Resumen:


```bash
poetry config --list
```

 -->


## Entornos virtuales


<!-- !!! info "PIPX"

    Poetry utiliza PIPX, que es una versíon mejorada de PIP con manejo mejorado de los paquetes.  -->

<!-- 
!!! info "Ubicacion de entornos"

    A diferencia de VENV, Poetry crea los entornos locales en una carpeta de usuario dedicada.
    Por ejemplo en Linux dicha carpeta suele ser:
    `~/.cache/pypoetry/virtualenv`


 -->








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




## SELF


```bash
poetry self
poetry self add poetry-core@latest
poetry self install
```


## Show

```bash
poetry show
```


## Source



## Update




## cache

```
poetry cache clear PyPI --all
poetry cache list
``` 

## PACKS


poetry-core         
poetry-plugin-shell