---
tags:
  - Argumentos
  - argparse
---


# Grupos de argumentos

Los argumentos pueden ser agrupados en base a diferentes criterios.
Para ello el *parser* creado con `ArgumentParser`
dispone de varios métodos adicionales
para crear nuevos analizadores derivados,
cada uno representando un nuevo grupo.


## Grupos de argumentos


Los argumentos se pueden repartir en distintos grupos
con ayuda del método `add_argument_group`.
Con este método se crean *parsers* específicos para cada grupo a crear
y se les asigna un *string* de descripción: 


```py title="Grupos de argumentos - creación"
# grupo de entrada
analizador_entrada = analizador.add_argument_group("entrada")
# argumentos de entrada
analizador_entrada.add_argument("x")

# grupo de salida
analizador_salida = analizador.add_argument_group("salida")
# argumentos de salida
analizador_salida.add_argument("y")
```

Los argumentos de los grupos
se asignan a cada grupo con el método `add_argument`.

El uso de los argumentos permanece inalterado.
Lo que se altera es la organización del texto de ayuda,
que ahora reparte la información de los argumentos de acuerdo al grupo al que pertenecen:


``` title="Grupos de argumentos - ayuda"
usage: rutina.py [-h] x y global

options:
  -h, --help  show this help message and exit

entrada:
  x

salida:
  y
```

??? info "Rutina completa"

    ```py
    import argparse

    # nuevo analizador principal ('parser')
    analizador = argparse.ArgumentParser()

    # grupo de entrada
    analizador_entrada = analizador.add_argument_group("entrada")
    # argumentos de entrada
    analizador_entrada.add_argument("x")

    # grupo de salida
    analizador_salida = analizador.add_argument_group("salida")
    # argumentos de salida
    analizador_salida.add_argument("y")

    # lectura de argumentos
    argumentos = analizador.parse_args()
    ``` 

## Argumentos mutuamente excluyentes

Los argumentos que son mutuamente excluyentes
se crean en un nuevo objeto derivado del *parser* original
con el método `add_mutually_exclusive_group`:


```py title="Argumentos excluyentes - creación"
# nuevo analizador principal ('parser')
analizador = argparse.ArgumentParser()

# grupo de argumentos mutuamente exclªuyentes
analizador_excluyentes = analizador.add_mutually_exclusive_group()

# argumentos contrapuestos
analizador_excluyentes.add_argument('-s', '--si',action='store_true')
analizador_excluyentes.add_argument('-n', '--no',action='store_false')

# lectura de argumentos
argumentos = analizador.parse_args()
```

de esta manera al intentar ingresar ambos argumentos juntos:

```py title="Argumentos excluyentes - uso"
py rutina.py -s -n
```

se obtiene un mensaje de error como este:

``` title="Reporte - argumentos conflictivos"
nombre_programa: error: argument -n/--no: not allowed with argument -s/--si
```

En caso de necesitarse el ingreso de uno de los dos argumentos
se agrega el parámetro `required` durante la creacíon del grupo:

```py title="Argumentos excluyentes - requeridos"
analizador_excluyentes = analizador.add_mutually_exclusive_group(required=True)
```

en tal caso, si falta ingresar un argumento
se obtiene el mensaje de error correspondiente:

``` title="Reporte - argumentos faltantes"
nombre_programa: error: one of the arguments -s/--si -n/--no is required
```


??? info "Rutina completa"


    ```py
    import argparse

    # nuevo analizador principal ('parser')
    analizador = argparse.ArgumentParser()

    # grupo de argumentos mutuamente excluyentes
    analizador_excluyentes = analizador.add_mutually_exclusive_group(
        required=True
        )

    # argumentos contrapuestos
    analizador_excluyentes.add_argument('-s', '--si',action='store_true')
    analizador_excluyentes.add_argument('-n', '--no',action='store_false')

    # lectura de argumentos
    argumentos = analizador.parse_args()
    ```



## Argumentos anidados 

Mediante el anidado de analizadores
se pueden crear comandos para el programa.
El método requerido se llama `add_subparsers`,

```py
# analizador auxiliar
sub_analizador = analizador.add_subparsers(
    help="Sub-analizador",
    )
```

el cual crea un analizador auxiliar de menor jerarquía
con el cual se implementan los *parsers* derivados
mediante el método `add_parser`, 
uno por cada nuevo comando a implementar.

Por ejemplo,
si se busca crear los comandos `crear`, `listar` y `borrar`
para crear la rutina actual:

```bash title="Comandos - uso"
py rutina.py  crear   [opciones]
py rutina.py  listar  [opciones]
py rutina.py  borrar  [opciones]
```
cada uno de ellos requerirá su propio *parser* derivado del *subparser*
creado previamente:

```py title="Comandos - creación"
# creación de comandos - un parser para cada uno
analizador_crear = sub_analizador.add_parser(
    "crear",
    help="Crear objeto"
    )

analizador_listar = sub_analizador.add_parser(
    "listar",
    help="Listar objetos"
    )

analizador_borrar = sub_analizador.add_parser(
    "borrar",
    help="Borra objeto"
    )
```

Al consultar la ayuda de la rutina:

```bash title="Rutina - ayuda general"
py rutina.py  -h
```

Se listarán los comandos disponibles de esta manera:


``` title="Comandos - salida por consola"
usage: rutina.py [-h] {crear,listar,borrar} ...

positional arguments:
  {crear,listar,borrar}
                        Sub-analizador
    crear               Crear objeto
    listar              Listar objetos
    borrar              Borra objeto

options:
  -h, --help            show this help message and exit
```

Los argumentos de cada comando se agregan por separado
mediante el uso del método `add_argument`.
Por ejemplo,
para asignar argumentos al comando `crear` 
se llama al método `add_argument` desde su *parser*,
llamado aquí `analizador_crear`:


```py title="Comandos - argumentos"
# argumentos del comando 'crear'
analizador_crear.add_argument(
    "-n", "--nombre",
    help="Nombre del objeto a crear"
    )

analizador_crear.add_argument(
    "-s", "--sobreescribir",
    action="store_true",
    help="Habilita la sobreescritura de objetos preexistentes"
    )
```
Las opciones de cada comando se consultan por separado.
Por  ejemplo, al consultar los argumentos del comando `crear`:

```bash
py rutina.py crear -h
```

Se obtiene un texto por consola como este:

```cli 
usage: rutina.py crear [-h] [-n NOMBRE] [-s]

options:
  -h, --help           show this help message and exit
  -n, --nombre NOMBRE  Nombre del objeto a crear
  -s, --sobreescribir  Habilita la sobreescritura de objetos preexistentes
```


??? info "Rutina completa"

    ```py
    import argparse

    # nuevo analizador principal ('parser')
    analizador = argparse.ArgumentParser()

    # analizador auxiliar
    sub_analizador = analizador.add_subparsers(
        help="Sub-analizador",
        )

    # creación de comandos - un parser para cada uno
    analizador_crear = sub_analizador.add_parser(
        "crear",
        help="Crear objeto"
        )

    analizador_listar = sub_analizador.add_parser(
        "listar",
        help="Listar objetos"
        )

    analizador_borrar = sub_analizador.add_parser(
        "borrar",
        help="Borra objeto"
        )

    # Ejemplo: argumentos del comando 'crear'
    analizador_crear.add_argument(
        "-n", "--nombre",
        help="Nombre del objeto a crear"
        )

    analizador_crear.add_argument(
        "-s", "--sobreescribir",
        action="store_true",
        help="Habilita la sobreescritura de objetos preexistentes"
        )

    valores = analizador.parse_args()
    ```

