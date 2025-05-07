---
tags:
  - Argumentos
  - argparse
---

# Tipos de argumentos 



## Argumentos posicionales

Los argumentos posicionales son aquellos que deben ingresarse en el mismo orden de definición para poder ser leídos.
A estos argumentos se les asigna un nombre y no van precedidos por ningún símbolo de prefijo.


```py title="Argumentos posicionales - creación"
# agregar argumentos simples
analizador.add_argument("x")
analizador.add_argument("y")
```

Los argumentos posicionales son de uso obligatorio.

```bash title="Argumentos posicionales - uso"
py rutina.py  2  3  
```

Los argumentos posicionales son listados por el comando de ayuda bajo la sección `positional arguments`:

``` title="Argumentos posicionales - ayuda"
usage: nombre_programa [opciones]

positional arguments:
  x
  y

options:
  -h, --help     show this help message and exit
```

## Argumentos opcionales (no posicionales)


Los argumentos no posicionales son aquellos
que requieren ser indicados precedidos por su nombre o su abreviación.
Son no posicionales porque no necesitan ser ingresados con un orden preestablecido. 
Estos argumentos son opcionales de manera predefinida

El método `add_argument` admite definir dos notaciones para los argumentos: un nombre completo,
típicamente precedida por dos guiones (`--`)
y una abreviación, precedida por un guión (`-`):


```py title="Argumentos no posicionales - configuración"
analizador.add_argument(
    '-a',                   # abreviación
    '--argumento-entrada'   # nombre completo
    )
```
Estos dos argumentos pueden ser ingresados sin respetar su orden.

El valor del argumento se podrá consultar
en base al nombre del argumento,
pero sin sus prefijos y con las correcciones necesarias
para respetar las reglas de Python en cuanto a nombres se refiere.


En este ejemplo: `--argumento-entrada` se convierte a `argumento_entrada`:

```py title="Argumentos no posicionales - lectura"
# lectura de argumentos
valores_argumentos = analizador.parse_args()

# consulta como diccionario
valores = vars(valores_argumentos)    # clave: 'argumento_entrada'

# consulta desde atributo
x = valores_argumentos.argumento_entrada   # atributo: 'argumento_entrada'
```

Al imprimir la ayuda estos argumentos se listan bajo la sección `options`:


``` title="Argumentos no posicionales - ayuda"
usage: rutina.py [-h] [-a ARGUMENTO_ENTRADA]  x y

options:
  -h, --help            show this help message and exit
  -a, --argumento-entrada ARGUMENTO_ENTRADA
```



