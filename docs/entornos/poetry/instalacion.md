---
date:
    created: 2025-03-23
    updated: 2025-08-18
# status: new
---


# Instalación

Poetry tiene múltiples opciones de instalación,
de las cuales se muestran las más importantes.



## Instalador oficial

=== "Bash"

    Instalación:

    ```bash title="Instalador oficial - instalar"
    curl -sSL https://install.python-poetry.org | python3 -
    ```

    Desinstalación

    ```bash title="Instalador oficial - desinstalar"
    curl -sSL https://install.python-poetry.org | python3 - --uninstall
    ```


=== "Powershell"

    ```powershell title="Instalador oficial - instalar"
    (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
    ```


Más detalles: [Usando el instalador oficial](https://python-poetry.org/docs/#installing-with-the-official-installer)

## Como paquete

Poetry puede ser instalado como un paquete de Python más
mediante el uso de gestores como PIP y PIPX:


Instalación:

```bash title="Manejo como paquete - instalación"
pip install poetry
```

Actualización:

```bash title="Manejo como paquete - actualización"
pip upgrade poetry
```

Desinstalación:

```bash title="Manejo como paquete - desinstalación"
pip uninstall poetry
```

!!! warning "Entornos aislados"

    En este caso,
    es prudente **instalar Poetry en un entorno virtual exclusivo**,
    para prevenir conflictos con las dependencias de otros paquetes
    y posibles errores debidos a actualizaciones descuidadas.


!!! info "PIPX"

    PIPX es una versíon modificada de PIP con manejo mejorado de los paquetes. 

Más detalles: [Instalando con PIPX](https://python-poetry.org/docs/#installing-with-pipx)


## Desde repositorios Linux

En el caso de plataformas GNU/Linux
se dispone de versiones instalables
con el gestor de paqeutes oficial de la distribución:
APT,YUM/DNF, Pacman...
Sin embargo, las versiones disponibles suelen ser anteriores a la versión `2.0.0`.



## Versión actual

La versión instalada de Poetry se consulta con el comando `--version`:

```bash title="Versión de Poetry"
poetry --version
```

Hay que tener en cuenta que
a partir de la versión `2.0.0`
se introdujeron cambios importantes 
respecto a las funcionalidades disponibles, comandos, etc.


## Configuración

El resumen de las configuraciones se consultan con el comando `config`:


```bash title="Resumen de configuraciones"
poetry config --list
```

