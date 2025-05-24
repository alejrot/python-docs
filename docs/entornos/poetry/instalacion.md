# Instalación


## Instalador oficial

=== "Bash"

    Instalación:

    ```bash
    curl -sSL https://install.python-poetry.org | python3 -
    ```

    Desinstalación

    ```bash
    curl -sSL https://install.python-poetry.org | python3 - --uninstall
    ```


=== "Powershell"

    ```powershell
    (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
    ```

Se puede comprobar la correcta instalación consultando la versión actual:

```bash
poetry --version
```

Más detalles: [Usando el instalador oficial](https://python-poetry.org/docs/#installing-with-the-official-installer)

## Como paquete

Poetry puede ser instalado como un paquete de Python más
mediante el uso de gestores como PIP y PIPX:


Instalación:

```bash
pipx install poetry
```

Actualización:

```bash
pipx upgrade poetry
```

Desinstalación:

```bash
pipx uninstall poetry
```


!!! info "PIPX"

    PIPX es una versíon modificada de PIP con manejo mejorado de los paquetes. 

!!! warning "Entornos aislados"

    En este caso,
    es prudente **instalar Poetry en un entorno virtual exclusivo**,
    para prevenir conflictos con las dependencias de otros paquetes
    y posibles errores debidos a actualizaciones descuidadas.



Más detalles: [Instalando con PIPX](https://python-poetry.org/docs/#installing-with-pipx)




## Configuración

El resumen de las configuraciones se consultan con el comando `config`:


```bash
poetry config --list
```

