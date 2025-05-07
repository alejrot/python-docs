---
tags:
  - Argumentos
  - argparse
---

# Uso básico

## Importación

El módulo se importa para su uso:

```py
import argparse
```


## Creación del *parser*

El componente fundamental es el analizador sintáctico,
el *parser*.
El analizador se crea con la clase `ArgumentParser`:


```py
# nuevo analizador ('parser') 
analizador = argparse.ArgumentParser()
```

## Lectura de valores

<!-- La lectura de argumentos de entrada -->
La ejecución del analizador
se realiza con el método `parse_args`,
el cual devuelve los valores leídos:

```py
# lectura de argumentos
valores_argumentos = analizador.parse_args()
```

El único argumento existente por defecto es el de ayuda (`help`). 
El argumento se pasa al ejecutar la rutina:

```bash
py rutina.py -h         # abreviación
py rutina.py --help     # nombre completo
```


El texto obtenido por consola es algo como esto:

```
usage: nombre_programa [opciones]

options:
  -h, --help     show this help message and exit
```

??? info "Rutina completa"


    ```py
    # importacion
    import argparse

    # nuevo analizador ('parser') 
    analizador = argparse.ArgumentParser()

    # lectura de argumentos
    valores_argumentos = analizador.parse_args()
    ```


## Agregar argumentos posicionales

Cada argumento de entrada se crea con el método `add_argument`
del *parser* creado:

```py
# agregar argumentos simples
analizador.add_argument("x")
analizador.add_argument("y")
```


Los valores de los argumentos son leidos por orden de entrada
y asignados por orden de creación:

```bash
py rutina.py  2  3  # x=2, y=3
```

Se asigna el valor 2 a `x` y el 3 a `y`.

Todos los argumentos creados de esta manera son obligatorios.
Si no se especifica alguno se producirá un error.

Estos argumentos serán listados por el comando de ayuda:

```
usage: nombre_programa [opciones]

options:
  -h, --help     show this help message and exit
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

    # agregar argumentos simples
    analizador.add_argument("x")
    analizador.add_argument("y")

    # lectura de argumentos
    valores_argumentos = analizador.parse_args()
    ```

## Lectura de valores


### Namespace

El retorno de `parse_args` es del tipo `argparse.Namespace`:

```py
# lectura de argumentos
valores_argumentos = analizador.parse_args()
```

La salida por consola es algo como lo siguiente:
```
Namespace(x=2, y=3)
```

### Atributos

Los valores de los argumentos pueden obtenerse
como atributos de la variable de retorno
que heredan el nombre de cada argumento:

```py
# lectura de argumentos
valores_argumentos = analizador.parse_args()

# lectura de atributos
x = argumentos.x
y = argumentos.y
```


### Diccionario

La lectura en formato diccionario se realiza con la función `vars`:

```py
# lectura de argumentos
valores_argumentos = analizador.parse_args()

# conversion a diccionario
diccionario_valores = vars(argumentos)
```

Por ejemplo en el ejemplo previo:

```bash
py rutina.py  2  3  # x=2, y=3
```
El resultado es el próximo diccionario:

```
{'x': '2', 'y': '3'}
```

## Texto de ayuda

El texto de ayuda puede ser publicado desde adentro el programa
con ayuda del método `print_usage`.

```py
analizador.print_usage()
```

Su resultado el equivalente al uso del argumento `--help`.



