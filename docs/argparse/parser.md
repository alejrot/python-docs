---
tags:
  - Argumentos
  - argparse
---

# Analizador


## Ayuda agregada

`ArgumentParser` posee varios argumentos para mejorar la legibilidad de la ayuda por consola:

```py
# nuevo analizador ('parser') 
analizador = argparse.ArgumentParser(
    prog="nombre_programa",
    usage='%(prog)s [opciones]',
    description="Descripción del programa",
    epilog='Texto al final de la ayuda',
    )
```

El texto obtenido por consola es algo como esto:

```
usage: nombre_programa [opciones]

Descripcion del programa

options:
  -h, --help     show this help message and exit

Texto al final de la ayuda
```

??? info "Rutina completa"


    ```py
    # importacion
    import argparse

    # nuevo analizador ('parser') 
    analizador = argparse.ArgumentParser(
        prog="nombre_programa",
        usage='%(prog)s [opciones]',
        description="Descripcion del programa",
        epilog='Texto al final de la ayuda',
        )

    # lectura de argumentos
    argumentos = analizador.parse_args()
    ```


## Prefijos de argumentos

Por *default* el prefijo de los argumentos de entrada es `-`. 
`prefix_chars` permite reemplazar el símbolo prefijo de los argumentos de entrada.

Esta opción se cambia al llamar la función `ArgumentParser`:


```py title="Prefijos de argumentos - configuración"
# nuevo analizador ('parser') 
analizador = argparse.ArgumentParser(
    prefix_chars="+"
    )

# argumento con prefijo cambiado
analizador.add_argument("+x", '++entrada-x')
```

de este modo la entrada de argumentos queda:

```bash title="Prefijos de argumentos - uso"
py rutina.py  +x 2          # abreviaciones
py rutina.py  ++entrada-x 2 # nombre completo
```

Se permite usar múltiples simbolos de prefijo alternativos.
Por ejemplo, para habilitar los signos `-`,  `+` y `/` se puede escribir simplemente: 

```py title="Múltiples prefijos - configuración"
# nuevo analizador ('parser') 
analizador = argparse.ArgumentParser(
    prefix_chars='-+/'
    )

# argumento con prefijos variados
analizador.add_argument("+x", '++entrada-x')
analizador.add_argument("/y", '//entrada-y' )
analizador.add_argument("-z", '--entrada-z')
```
en este caso la entrada de argumentos queda:

```bash title="Múltiples prefijos - uso"
py rutina.py  +x 2   /y 3   -z P                            # abreviaciones
py rutina.py  ++entrada-x  2 //entrada-y 3  --entrada-z  P  # nombre completo
```

Es necesario respetar los prefijos elegidos para cada argumento.
En caso de necesitarse usar distintos prefijos para un mismo argumento
entonces estos deben indicarse explícitamente en la definición.
Ejemplo:

```py title="Múltiples prefijos por argumento"
# argumento con prefijos variados
analizador.add_argument(
      "+x", '++entrada-x',
      "/x", '//entrada-x',
      "-x", '--entrada-x',
      )
```

??? info "Rutina completa"

    ```py
    import argparse

    # nuevo analizador ('parser') 
    analizador = argparse.ArgumentParser(
        prefix_chars='-+/'
        )

    # argumento con prefijos variados
    analizador.add_argument("+x", '++entrada-x')
    analizador.add_argument("/y", '//entrada-y' )
    analizador.add_argument("-z", '--entrada-z')

    # lectura de argumentos
    argumentos = analizador.parse_args()
    valores = vars(argumentos)
    print(valores)
    ```


## Argumentos desde archivo

Si los argumentos deben leerse desde archivo
se agrega durante la creación del *parser*
el parámetro `fromfile_prefix_chars`
y se le asigna un carácter indicador,
por ejemplo el arroba (`@`):


```py title="Argumentos desde archivo - configuración"
# nuevo analizador ('parser') 
analizador = argparse.ArgumentParser(
    fromfile_prefix_chars='@'   # prefijo de archivos
    )

# argumentos opcionales
analizador.add_argument('-x')
analizador.add_argument('-y')
analizador.add_argument('-z')
```

entonces al programa se le pasa el nombre de archivo
precedido por el arroba:

```bash title="Argumentos desde archivo - lectura"
py rutina.py @valores.txt
```

Si el archivo de texto trae los valores guardados en este formato:

``` title="archivo con argumentos"
-x=8
-y=hola
-z=mundo
```

entonces el programa podrá leer todos los argumentos juntos:
```
{'x': '8', 'y': 'hola', 'z': 'mundo'}
```

??? info "Rutina completa"

    ```py
    import argparse

    # nuevo analizador ('parser') 
    analizador = argparse.ArgumentParser(
        fromfile_prefix_chars='@'
        )

    analizador.add_argument('-x')
    analizador.add_argument('-y')
    analizador.add_argument('-z')

    # lectura de argumentos
    argumentos = analizador.parse_args()
    valores = vars(argumentos)
    print(valores)
    ```