---
tags:
  - Funciones
  - Operadores
  - Tipos
  - Variables
  - Argumentos
  - Retorno
---


# Sintaxis



## Llamada

Para *llamar* a una función (es decir, para usarla) se la invoca por su nombre:

```py title="Llamada a función"
variable_salida = funcion( valor_entrada)
```
La función puede disponer o no de un valor de salida , como puede requerir o no valores de entrada. Un ejemplo de función sin valor de retorno es la función `print()` , en tanto que una funcion que a menudo se usa sin argumentos de entradas es `input()`.


## Definicion

La definición de la función es la especificación del nombre de la función y de su rutina interna,es decir su código interior, el cual se ejecutará cada vez que la función sea llamada.

Formato de definición en Python:

```python title="Formato de definición"
# definicion de funcion, sin valores de entrada
def nombre_funcion():
	# Código función
    # ....
    # final de código


# Código programa principal
# ....
nombre_funcion()	     # llamada a la función
```

En Python las funciones se definen **antes** de su primer llamado.

!!! info "Guía de estilos"
    Es una buena práctica de estilo dejar **dos renglones vacíos** debajo de cada definición de las funciones. Esto ayuda a interpretar visualmente hasta dónde llega el código de cada función.



## Argumentos

Los *argumentos* son los **valores** que se le asignan a los *parámetros* de entrada al llamar a una función.

```python title="argumentos de funciones"
nombre_funcion(valor_1, valor_2, ...) # funcion con argumentos de entrada asignados
```

### definición

Si la función tiene parámetros de entrada , es decir variables que afectarán al resultado de la función estos se indican entre los paréntesis y separados por comas: 

```python title="formato de definición - con argumentos de entrada"
# definicion de funcion, con valores de entrada
def nombre_funcion(parametro_1, parametro_2, ...):
	# Código función
    # ....
    # final de código


# Código programa principal
# ....
nombre_funcion(valor_1, valor_2, ...)      # llamada a la función
```

### xargs

La función puede aceptar un número indefinido de parámetros (*x-args*) con ayuda del asterisco (`*`) :

```python   title="argumentos indefinidos (x-args)" hl_lines="1"
def nombre_funcion( *variables ):
	for valor in variables:
        # Código función
        # ....
        # final de código
```

Esto crea una *tupla* interna que engloba a todos los argumentos sin nombre que se pasen por la entrada.

Tómese por ejemplo una función que muestra en pantalla los datos de entrada:

```python   title="x-args - variables entrada" hl_lines="7"
def funcion(*variables):
    print(variables)
    for v in variables:
        print(f"{v}")


funcion(1, 3, 8, 4)  
```
El resultado será
``` title="x-args - resultado"
(1, 3, 8, 4, 'hola')  
1
3
8
4
hola 
```
En este caso se agrupan todos los valores de entrada juntos dentro de una tupla. Por otra parte, si a la entrada se mandan datos (listas, diccionarios, etc):

```python   title="x-args - datos entrada" hl_lines="5"
def funcion(*variables):
    print(variables)


funcion( [1, 3, 8, 4] , {"hola":10, "chau":-7} )     
# da '([1, 3, 8, 4], {'hola': 10, 'chau': -7})'   
```
El resultado será esta vez:
``` title="x-args - resultado"
([1, 3, 8, 4], {'hola': 10, 'chau': -7})
[1, 3, 8, 4]
{'hola': 10, 'chau': -7}
```
Se observa que se crea una tupla interna donde el primer valor es la lista de entrada y el segundo es el diccionario.


### kargs
Para cargar **parámetros de diccionario** como argumento (*keyword args*,o  ***kwargs***) se usa el doble asterisco:

```python title="keyword args (k-args)" hl_lines="1"
def nombre_funcion( **diccionario_entrada ):
    # Código función
    # ....
    # final de código
```

Por ejemplo, si a una función se le pasa como argumentos:


```python title="k-args" hl_lines="7"
def funcion( **diccionario_entrada):
    print(diccionario_entrada)
    print(diccionario_entrada.keys())       
    print(diccionario_entrada.values())


funcion(hola=10, chau=-7, saludo="Buenos dias")
#  da:
# '{'hola': 10, 'chau': -7, 'saludo': 'Buenos dias'}'
# 'dict_keys(['hola', 'chau', 'saludo'])'
# 'dict_values([10, -7, 'Buenos dias'])'
```

la función construye entonces un dicconario interno al que le incorporan los *strings* como claves y los valores asignados como valores de claves.





!!! note "Argumentos con nombre"
    
    Los argumentos de este tipo de funciones deben explicitarse al llamar a la función, porque no hay un orden predefinido de argumentos como en otras funciones. Es decir, los argumentos sí o sí deben pasarse como pares clave-valor tal como se mostró

!!! warning "Nombres de argumentos"

    Los argumentos de entrada tienen las mismas restricciones de sintaxis que los nombres de variables.
    De hecho, los *k-args* están pensados para ser usados internamente como variables.

    ```python title="Errores de entrada"
    funcion("Buenos dias"=10 )  # ERROR: no se admiten strings como nombre de argumento
    funcion(yo soy Sam = 5)     # ERROR: los nombres de argumentos no aceptan espacios en blanco
    ```


### valores predefinidos

A las funciones se les puede dar valores de entrada por defecto, de modo de poder omitir argumentos al llamarlas:

```python title="Valores predefinidos"
def nombre_funcion( variable_1=valor_1 ,variable_2=valor_2 ):
	#codigo
```
También se las puede llamar con el orden de los argumentos cambiado mediante asignaciones:

```python title="Valores predefinidos - cambio de orden de entrada"
retorno = nombre_funcion( variable_2=valor_2, variable_1=valor_1 )
```


## Valor de retorno

Las funciones pueden tener un valor de retorno, es decir un valor de salida. Este se incluye al final de la definición de la función con la sentencia ***return***:

```python title="formato de definición - con valor de retorno"
def nombre_funcion():
	# Código función
    # ....
    # final de código
	return valor_retorno  # asignacion de retorno


# Código programa principal
# ....
retorno = nombre_funcion()    # llamada a la función
```

La sentencia `return` marca el final de la ejecución de la función, por tanto si hay código posterior a esta sentencia no se ejecutará.

El valor por defecto del retorno de las funciones es `None`.  El valor de retorno en Python puede ser prácticamente de cualquier tipo: un booleano, un string, un numero,una lista, un diccionario, un objeto de una clase especificada, etc. El el caso de no requerirse un valor de retorno el uso de `return` es opcional, tal como se muestra en los ejemplos previos 

En la terminal, si el valor de retorno se asigna a una variable entonces no se muestra en pantalla. Sólo se lo muestra si se pasa a la función `print()`.



