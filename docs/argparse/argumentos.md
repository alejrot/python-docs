---
tags:
  - Argumentos
  - argparse
---

# Configuración de argumentos


## Opciones de configuración


El método `add_argument` permite configurar una gran cantidad de opciones de uso para cada argumento,
las cuales se pasan como argumentos del método:


|parámetro| significado|
|---|---|
|`type`|tipo de valor de entrada - agrega conversión|
|`required`| obligatoriedad del argumento a la entrada (booleano) |
|`default`|valor predefinido salvo indicación desde comandos|
|`choices`|lista con los valores permitidos a la entrada |
|`dest`| nombre alternativo de la variable|
|`help`|texto de ayuda - se muestra al requerirla por comandos |
|||
|`action`| acciones predefinidas del argumento|
|`nargs`| numero de valores del argumento|


## Acciones

El parámetro `action` acepta las siguientes opciones de configuración.



### Guardar - `store`

Esta es la opción por *default*.
Guarda el valor de entrada en la variable del argumento.

```py title="store - configuración"
analizador.add_argument(
    '-a',
    action='store'
    )
```

```bash title="store - uso"
py rutina.py -a 5   # '5'
py rutina.py        # Error
```


### Guardar constante - `store_const`

Esta opción asigna el valor `const` como salida sólo si el argumento está presente al menos una vez.
En caso contrario devuelve `None`.


```py title="store_const - configuración"
analizador.add_argument(
    '-a', 
    action='store_const', 
    const='17'
    )
```

```bash title="store_const - uso"
py rutina.py -a     # '17'
py rutina.py -a -a  # '17'
py rutina.py        # 'None'
```

### Verdadero - `store_true`

Esta acción crea un argumento booleano
que es `True` si el argumento está presente.
En caso contrario da `False`.

Sirve para crear flags de habilitación de opciones.

```py title="store_true - configuración"
analizador.add_argument('-a', action='store_true')
```

```bash title="store_true - uso"
py rutina.py -a     # 'True'
py rutina.py        # 'False'
```

### Falso - `store_false`

Es el complemento de `store_true`.
Sirve para crear flags de bloqueo de opciones.

```py title="store_false - configuración"
analizador.add_argument('-a', action='store_true')
```

```bash title="store_false - uso"
py rutina.py -a     # 'False'
py rutina.py        # 'True'
```

### Adjuntar valores - `append`

Esta acción hace que al argumento se le pueda pueda asignar múltiples valores por separado y los junta todos en una lista.
Si el argumento no está presente en la entrada se devuelve `None`

```py title="append - configuración"
analizador.add_argument('-a', action='append')
```

```bash title="append - uso"
py rutina.py -a 8           # ['8']
py rutina.py -a 8 -a hola   # ['8', 'hola']
py rutina.py                # 'None'
```


### Adjuntar constante - `append_const`

Esta acción crea una lista donde se repite el valor de la constante indicada tantas veces como aparezca el argumento.
Si el argumento no está presente en la entrada se devuelve `None`

```py title="append_const - configuración"
analizador.add_argument(
    '-a', 
    action='append_const', 
    const='21'
    )
```

```bash title="append_const - uso"
py rutina.py        # 'None'
py rutina.py -a     # ['21']
py rutina.py -a -a  # ['21', '21']
py rutina.py -aa    # ['21', '21']
```



### Contar repeticiones - `count`

La acción `count` cuenta las repeticiones del argumento especificado,
devolviendo la cantidad como entero.
Si el argumento no se ingresa entonces se devuelve `False`. 

```py title="count - configuración"
analizador.add_argument('-a', action='count')
```

```bash title="count - uso"
py rutina.py         # 'None'
py rutina.py  -a     # '1'
py rutina.py  -a -a  # '2'
py rutina.py  -aa    # '2'
py rutina.py  -aaa   # '3'
```

### Versión - `version`

El argumento `version` permite leer la etiqueta de versión actual.

```py title="version - configuración"
analizador.add_argument(
    '-v', '--version',
    action='version'
    )
analizador.version="v1.0.0"
```

```bash title="version - uso"
py rutina.py -v     # 'v1.0.0'
```



### Ayuda - `help`


La acción `help` es la encargada de crear argumentos de ayuda por consola.
Muestra los textos de ayuda de todos los otros argumentos,
la descripción del programa incluida en el *parser*, etc.

```py title="help - configuración"
analizador.add_argument(
    '-a', '--ayuda',
    action='help',
    help="alternativa a 'help'"
    )
```

```bash title="help - uso"
py rutina.py -a
py rutina.py --ayuda
```

La salida por consola es algo similar a esto:

``` title="salida por consola"
options:
-h, --help   show this help message and exit
-a, --ayuda  alternativa a 'help'
```



## Múltiples valores

El parámetro opcional `nargs` es el encargado de determinar el número de valores de entrada permitidos en el argumento.
Los valores permitidos son los siguientes:


|valor| significado|
|----|----|
| N (entero) | N valores obligatorios - se guardan en una lista|
| `?`| un único valor - opcional|
| `*`| cantidad arbitraria - guardado en lista|
| `+`| cantidad arbitraria (al menos uno) - guardado en lista|
| `argparse.REMAINDER`| todos los valores asignados al final|


Supóngase por ejemplo un argumento que acepta múltiples valores de entrada y que no son obligatorios:

```bash title="cantidad arbitraria - configuración"
analizador.add_argument(
    '-a', 
    nargs='*'
    )

# ...

```

```bash title="cantidad arbitraria - uso"
py rutina.py -a 3 14 16   # '['3', '14', '16']'
py rutina.py -a           # '[]'
py rutina.py              # 'None'
```