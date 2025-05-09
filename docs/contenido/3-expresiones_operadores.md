

# Expresiones y Operadores


## Expresiones
Las expresiones son un conjunto de operandos (variables y valores) y operadores que al evaluarse dan un valor. Las expresiones se evalúan de izquierda a derecha y respetando la jerarquía de las operaciones. 


## Operadores

### Operadores Aritméticos

A continuación se muestran los operadores aritméticos de Python, los cuales sirven para trabajar con números enteros y flotantes.

| Operador | Símbolo   |
|---|:---:|
| Suma | `+`   |
| Resta | `-`   |
| Multiplicación | `*`  |
| Division  |  `/` |
| Division entera | `//`  |
| Exponente | `**`  |
|  Módulo| `% `  |


Modo de uso:
```python title="Formato operaciones aritméticas"
resultado = numero_1 operador numero_2
```

```py title="Ejemplo: uso operaciones aritméticas"
n = 7 + 3   #  '10'  
n = 7 - 3   #  '4'
n = 7 * 3   #  '21'
n = 7 / 3   #  '2.3333333333333335'
n = 7 // 3  #  '2'
n = 7 % 3   #  '1'
```

!!! tip "Tip: operadores aritméticos sobre *strings*"
    Algunos operadores de Python permiten trabajar con `strings`: textos, frases, etc:
    
    - El operador + también puede usarse para **concatenar** cadenas de texto (`strings`). 
    - Con el operador * se puede concatenar la misma frase un número fijo de veces

    ```py title="Ejemplo: aritmetica sobre strings"
    texto = "hola_"
    texto + texto     # 'hola_hola_'
    texto * 3         # 'hola_hola_hola_'
    ```

Las operaciones aritméticas tienen una jerarquía de aplicacion por defecto.
Este es el orden de jerarquía de las operaciones, de las primeras en aplicarse a las últimas: 

1. Paréntesis 
2. Exponente 
3. Multiplicación 
4. División  
5. Adición 
6. Sustracción

Nemotécnico jerarquías: **PEMDAS**

### Operadores de Asignación

Combinan operaciones aritméticas con la asignación (`=`) a continuación. A la variable de entrada se la afecta con el operador aritmético indicado y una variable o valor adicional.

Ejemplo:   
```python
edad += 3
```
equivale a: 

```python
edad = edad + 3
```


### Operadores Lógicos

Los operadores lógicos trabajan con valores y variables booleanos. 

Modo de uso:
```python title="Formato operaciones lógicas"
resultado = valor_logico_1 operador valor_logico_2
```
Los operadores disponibles son los siguientes:

| Operador | Símbolo   |  Salida en 'True'  |
|:---|:---:| -----|
| Y (AND)           | `and` | Ambas entradas son 'True'   |
| O (OR)            | `or` | Al menos una entrada es 'True'   |
|  NO (NOT)         | `not` |  Entrada 'False'  |
| O exclusiva (XOR) | `^` | Entradas distintas  |

Esta es la jerarquía de las operaciones lógicas,
de mayor a menor:

1. `not` 
2. `and` 
3. `or`

??? note "Anexo: tablas de verdad"
    Los resultados de cada operador lógico se describen habitualmente con las ***tablas de verdad***,  donde el emoji ✅ es `True` y la celda vacía es `False`.:

    | entrada | salida NOT |  
    | :---: | :---: |
    |  | ✅ | 
    | ✅ |    |
 


    | entrada X | entrada Y | salida AND |  
    | :---: | :---: | :---: | 
    |  |  |  |   | 
    |  ✅|    |  | 
    |  | ✅   |  | 
    | ✅ | ✅ | ✅ | 


    | entrada X | entrada Y |  salida OR | 
    | :---: | :---:   | :---: |
    |  |  |    | 
    |  ✅|    |   ✅ | 
    |  | ✅   |   ✅  | 
    | ✅ | ✅ |   ✅ | 


    | entrada X | entrada Y |   salida XOR |
    | :---: | :---: | :---: |
    |  |  |    ✅ |
    |  ✅|    |     |
    |  | ✅   |     |
    | ✅ | ✅ |  ✅ |


    Las tablas de verdad  son estándar: **no** dependen del lenguaje de implementación



### Operadores Bit a Bit

#### Lógicos

Estos operadores aplican las operaciones lógicas vistas previamente pero bit a bit.
Lo que hacen estos operadores es basarse en la representación binaria
de la(s) variable(s) de entrada.



| Operador | Símbolo   |Bit salida en 'True'  |
|-------|:-------:|:---|
| Y (AND)           | `&` | Ambos bits son 'True'   |
| O (OR)            | `|` | Al menos un bit es 'True'   |
|  NO (NOT)         | `~` | Bit 'False'  |
| O exclusiva (XOR) | `^` | Bits distintos  |


Ejemplos de uso: 

```py
7 & 5   # '111' and '101' -> '7' (111)
7 | 5   # '111' or  '101' -> '5' (101)
7 ^ 5   # '111' xor '101' -> '2' (010)
```




#### Desplazamiento (*shift*)

Con los operadores de desplazamiento
se lee una variable como binario
y se elige cuántas posiciones se 'corre'.
Los espacios faltantes se autocompletan con ceros.



| Operador | Símbolo |
|-------|:-------:|
| Corrimiento a derecha   | `>>` |
| Corrimiento a izquierda | `<<` |


Ejemplos: 

```py title="Desplazamiento - a izquierda"
1 << 0 # no corrimiento -> '1'  (0001) 
1 << 1 # 1 bit          -> '2'  (0010)
1 << 3 # 2 bits         -> '4'  (0100)
1 << 3 # 3 bits         -> '8'  (1000) 
```

```py title="Desplazamiento - a derecha"
7 >> 0 # no corrimiento -> '7'  (0111)
7 >> 1 # 1 bit          -> '3'  (0011)
7 >> 2 # 2 bits         -> '1'  (0001)
7 >> 3 # 3 bits         -> '0'  (0000)
```



### Operadores Relacionales

Los operadores relacionales permiten comparar números enteros y flotantes. 

Los operadores disponibles en Python son:

| Operador | Símbolo   |
|-------|:-------:|
| mayor    | `>` |      
| menor    |  `<`  |
| igual    |  `==`  |
| mayor o igual |  `>=` |
| menor o igual | `<=`  |
| distinto a    |  `!=` |


!!! tip "Tip: operadores relacionales sobre strings"
    
    El operador `==` sirve para comparar si dos `strings` (caracteres, frases, etc) son idénticos. Los otros operadores también pueden usarse para comparar strings por longitud y por contenido de caracteres. 

    ```python title="Ejemplo: comparando strings"
    print('B'  < 'A')	# False
    print('B'  >= 'A')	# True
    print('ABC' > 'A')  # True
    print('ABC' == 'A') # False
    print('ABC' <= 'A') # False
    ```



### Operador de Pertenencia

El operador de pertenencia `in`
es el encargado de verificar
que un elemento o secuencia esté o no en una secuencia.

El operador de pertenencia son:

| Operador | Símbolo   |
|-------|:-------:|
| pertenencia|`in`|


El retorno es un booleano:
`True` si el elemento existe dentro de la secuencia
y `False` en caso contrario.

Ejemplo:
```py title="Pertenencia - valores"
inclusion = "a"  in "hola"  # 'True'
inclusion = "b"  in "hola"  # 'False'
```

La secuencia puede ser una variable `string`
como también una lista, una tupla, etc.


Con `in` también se puede verificar la existencia o no de una secuencia particular dentro de otra:

```py title="Pertenencia - secuencias"
inclusion = "la"  in "hola"  # 'True'
inclusion = "al"  in "hola"  # 'False'
```

La cláusula se puede usar combinada con el operador lógico `not`:


```py title="No pertenencia"
inclusion =  "n" not in "hola" # 'True'
inclusion = "al" not in "hola" # 'True'
```


### Operador de identidad

El operador de identidad `is` se encarga de verificar si dos variables
ocupan el mismo espacio en memoria.

| Operador | Símbolo   |
|-------|:-------:|
| identidad|`is`|

El retorno es un booleano: `True` si se cumple la identidad y `False` en caso contrario.

Este operador también suele usarse como alternativa al operador relacional de igualdad:

```py
valor = None
# uso
identidad = valor is True       # 'False'
identidad = valor is False      # 'False'
identidad = valor is None       # 'True'
``` 



