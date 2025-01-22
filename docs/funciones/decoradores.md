---
tags:
  - Funciones
  - Decoradores
  - Argumentos
  - Retorno
---

# Decoradores

Los decoradores son funciones auxiliares que permiten agregar código tanto antes como después de la función que se les indique. Éstos permite implementar modificaciones a las funciones sin modificar su código interno.


## Definición - Formato función

### Idea básica

Los decoradores suelen definirse mediante funciones, de forma que éstas  engloben unas dentro de otras formando una *closure*. Este es el formato básico de definición:

```py title="Definición de decoradores"
def nombre_decorador(funcion_entrada):
    def funcion_envolvente()
        # rutina previa
        funcion_entrada()
        # rutina posterior

    return funcion_envolvente
```

### Funciones con argumentos

En la definición previa se asumió que la función no requiere argumentos de entrada. Los argumentos pueden pasarse de manera genérica con ayuda de los *xargs* y *kargs*:

```py title="Definición de decoradores - Funciones con argumentos" hl_lines="2 4"
def nombre_decorador(funcion_entrada):
    def funcion_envolvente(*args, **kwargs):
        # rutina previa
        funcion_entrada(*args, **kwargs)
        # rutina posterior

    return funcion_envolvente
```

Lo habitual es usar esta segunda forma, por su practicidad y sencillez.

### Decoradores con argumentos

Los decoradores pueden aceptar argumentos de entrada, para ello hay que agregar una  función adicional envolviendo a la *closure*:

```py title="Definición de decoradores - Decorador con argumentos" hl_lines="1 9"
def nombre_decorador(argumento_decorador):
    def _nombre_decorador(funcion_entrada):
        def funcion_envolvente(*args, **kwargs):
            # rutina previa
            funcion_entrada(*args, **kwargs)
            # rutina posterior

        return funcion_envolvente
    return _nombre_decorador
```

Esta función externa es la que acepta los argumentos de entrada del decorador. 


## Uso de decoradores

### Asignación 

El decorador se asigna justo antes de definir la función de interés con su nombre precedido de un asterisco (`@`):

```py title="Asignación de decoradores" hl_lines="1"
@nombre_decorador       # asignación
def nombre_funcion():
    # rutina
    return
```
### Asignación con argumentos

Para agregarle argumentos al decorador simplemente se le agrega el valor de entrada entre paréntesis:

```py title="Asignación de decoradores - Con argumentos" hl_lines="1"
@nombre_decorador(valor_entrada)       # asignación
def nombre_funcion():
    # rutina
    return
```

### Concatenación

Varios decoradores se pueden aplicar a la misma función:

```py title="Asignación de decoradores múltiples" hl_lines="1 2"
@nombre_decorador_1       # decorador externo
@nombre_decorador_2       # decorador interno
def nombre_funcion():
    # rutina
    return
```

De esta manera el primer decorador se aplica alrededor del siguiente, "rodeándolo". Esto se repite una y otra vez hasta acabar con los decoradores disponibles.


## Atributos internos

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


## Decoradores en formato de clase

Una forma alternativa de definir los decoradores es mediante el uso de clases:

```py title="Decorador - formato clase" hl_lines="1  3 8"
class nombre_decorador:
    # Una instancia (una "copia" de la clase) para cada funcion asignada
    def __init__(self, funcion_entrada):
        # referencia a la función de entrada
        self.funcion = funcion_entrada

    # Ejecucion de la funcion a traves del método 
    def __call__(self, *args, **kargs):
        # rutina previa
        self.funcion(*args, **kargs)
        # rutina posterior
```

El método `__init__` crea una "copia" de la clase (una *instancia*) para cada función que se le asigne el decorador, en tanto que el método `__call__` llama internamente a dicha función y ejecuta  el código agregado.


!!! example "Ejemplo: decorador - formato clase"


    ```py title="decorador debugger - formato clase"
    class debugger:

        # Una instancia (una "copia" de la clase) para cada funcion asignada
        def __init__(self, funcion_entrada):
            # Guardado de función de entrada
            self.funcion = funcion_entrada

        # Ejecucion de la funcion a traves de clase
        def __call__(self, *args, **kargs):
            print(f"Funcion '{self.funcion.__name__}'")
            print(f"Argumentos entrada: '{args} , {kargs}'")
            retorno = self.funcion(*args, **kargs)
            print(f"Retorno: '{retorno}'")
    ```

El uso y funcionamiento de estos decoradores es idéntico al de los decoradores definidos mediante closures.

## Ejemplos aplicados

Un ejemplo aplicado de decorador es un medidor de tiempo de ejecución como se muestra:

!!! tip "TIP Nº1 - medidor de tiempo de ejecución"

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

!!! tip "TIP Nº2 - Decorador para argumentos y retorno de funciones"

    ```py title="Decorador de argumentos y retorno - Definición"
    def debugger(debug:bool=False):
        def _debugger(funcion_entrada):
            def funcion_envolvente(*args, **kargs):
                if debug:
                    print(f"Funcion '{funcion_entrada.__name__}'")
                    print(f"Argumentos entrada: '{args} , {kargs}'")
                retorno = funcion_entrada(*args, **kargs)
                if debug:
                    print(f"Retorno: '{retorno}'")
                return    
            return funcion_envolvente
        return _debugger
    ```

    ```py title="Decorador de argumentos y retorno - Asignacion y uso"
    @debugger(True)
    def funcion_test(*args,**kargs):
        pass
    ```



!!! tip "TIP Nº3 - Decoradores de logging"
    Con ayuda de decoradores se pueden implementar reportes (*logs*) para las funciones y métodos de clase con facilidad, lo cual ayuda a detectar y corregir problemas. [**Ver capitulo de logging**](../modulos/logging.md#uso-aplicado-decoradores-de-logging)











