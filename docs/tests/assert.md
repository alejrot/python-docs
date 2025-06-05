# Assert

*Assert*, que puede traducirse como "afirmación" pero también como "reclamo",
permite implementar excepciones controladas dentro del código,
obligando a que se cumplan ciertas condiciones dentro de la rutina
so pena de lanzar una rutina de excepcion
o en su defecto interrumpir la ejecución del código.


## Idea básica

La cláusula `assert`
dispara una excepción condicional
en caso que no se cumpla la condición elegida.

Uso básico:

```py
assert condicion
```

También puede usarse el *assert* como función:

```py
assert(condicion)
```

Si la condición indicada se cumple
entonces la ejecución continua normalmente,
en caso contrario
se dispara una excepción especial llamada `AssertionError`.

Ejemplo:

```py
assert 1==2     # 'AssertionError'
assert(1==2)    # 'AssertionError'
```

### Mensaje de error

Si se usa `assert` como cláusula
entonces se permite definir un mensaje de error
para la excepción:

```py
assert condicion, mensaje_error     
```

!!! warning "Mensaje en función"

    El uso con paréntesis del mensaje de error no se permite porque siempre da `True`:

    ```py
    assert(condicion, mensaje_error)   # 'SyntaxWarning: assertion is always true, perhaps remove parentheses?'
    ```


### Tests en rutinas

Mediante la cláusula `assert`
se pueden definir tests unitarios.
Esto permite crear rutinas de verificación 
para comprobar la integridad del código y su buen funcionamiento.

```py 
def negacion(x: bool):
    return not x

# test de integridad
assert negacion( True)  == False 
assert negacion( False) == True 
```

La rutina de comprobación puede formar parte de las rutinas del programa
o bien puede ser incluida en archivos dedicados para correr los *test*.


### Test en funciones y métodos


Con ayuda de la cláusula `assert`
se pueden hacer tests integrados
dentro de las definiciones de funciones
y de métodos de clases.  

Estos tests internos se ejecutarán cada vez
que la función o método sea llamado.


!!! tip "Tipado duro"

    Creando tests de tipos de argumentos
    se puede imitar el tipado duro,
    el cual interrumpirá la ejecución
    si los valores de los argumentos son del tipo incorrecto.

    Ejemplo:

    ```py 
    def negacion(x: bool):
        assert type(x) == bool, "Error: argumento no booleano"
        return not x

    # funcionamiento normal
    y = negacion( True)     # 'False'
    y = negacion( False)    # 'True'
    # interrupción del programa
    y = negacion( "True")   # 'Error: argumento no booleano'
    ```

