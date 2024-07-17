

# Decoradores

Los decoradores son funciones auxiliares que permiten agregar código tanto antes como después de la función que se les indique. Éstos permite implementar modificaciones a las funciones sin modificar su código interno.

Los decoradores son un caso particular del uso de las *closures*, tal como se puede observar en su formato básico de definición:

```py title="Definición de decoradores"
def nombre_decorador(funcion_interna):
    def funcion_envolvente()
        # rutina previa
        funcion_interna()
        # rutina posterior

    return funcion_envolvente
```

El decorador se asigna justo antes de definir la función de interés con su nombre precedido de un asterisco (`@`):

```py title="Asignación de decoradores" hl_lines="1"
@nombre_decorador       # asignación
def nombre_funcion():
    # rutina
    return
```

En la definición previa se asumió que la función no requiere argumentos de entrada. Los argumentos pueden pasarse de manera genérica así:

```py title="Definición de decoradores - Argumentos genéricos" hl_lines="2 4"
def nombre_decorador(funcion_interna):
    def funcion_envolvente(*args, **kwargs)
        # rutina previa
        funcion_interna(*args, **kwargs)
        # rutina posterior

    return funcion_envolvente
```

A la función interna del decorador se le puede agregar *atributos* (variables asociadas) para mantener el registro.

Por ejemplo, el siguiente decorador cuenta cuántas llamadas se hace sobre una misma función.  Para ello crea un atributo llamado `conteo_llamadas` que queda enlazado a cada función especificada:

```py title="Decorador 'contador_llamados' - Definición" hl_lines="4 8"
def contador_llamados(funcion):
    def contador_funcion(*args, **kwargs):
        # incremento de atributo contador
        contador_funcion.conteo_llamadas += 1
        print(f"La función '{funcion.__name__}' se ha llamado {contador_funcion.conteo_llamadas} veces.")
        return funcion(*args, **kwargs)

    # creacion e inicializacion de atributo contador
    contador_funcion.conteo_llamadas = 0
    return contador_funcion
```
Dentro del decorador se lee tanto el atributo estándar `__name__` de la función de entrada como el atributo inventado `conteo_llamadas`.

Para probarlo el mismo decorador se usa con distintas funciones:

```py title="Decorador 'contador_llamados' - Asignación"
@contador_llamados
def funcion_1():
    pass

@contador_llamados
def funcion_2():
    pass
```
Como el atributo se asigna a cada función que usa el decorador el conteo de llamadas a cada función se mantiene independiente:

```py title="Decorador 'contador_llamados' - Uso" hl_lines="4 5"
funcion_1() # "La función 'funcion_1' se ha llamado 1 veces."
funcion_1() # "La función 'funcion_1' se ha llamado 2 veces."
funcion_1() # "La función 'funcion_1' se ha llamado 3 veces."
funcion_2() # "La función 'funcion_2' se ha llamado 1 veces."
funcion_2() # "La función 'funcion_2' se ha llamado 2 veces."
funcion_1() # "La función 'funcion_1' se ha llamado 4 veces."
```

Un ejemplo aplicado de decorador es un medidor de tiempo de ejecución como se muestra:

!!! example "Ejemplo 2: medir tiempo de ejecución"

    ```py title="Decorador 'intervalo' - Definicion"
    from time import time, sleep

    # creación del decorador
    def intervalo(funcion):
        def tiempo_ejecucion(*args, **kwargs):
            inicio = time()
            funcion(*args, **kwargs)  
            fin    = time()
            print(f"Tiempo ejecución: {(fin-inicio):.6} segundos")

        return tiempo_ejecucion

    ```


    ```py title="Decorador 'intervalo' - Asignacion y uso"
    # Asignacion
    @intervalo
    def esperar(n: int):
        sleep(0.1*n)
        return 

    # Uso
    esperar(5)      # 'Tiempo ejecución: 0.500126 segundos'
    ```















