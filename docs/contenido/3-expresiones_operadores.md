

# Expresiones y Operadores


## Expresiones
Las expresiones son un conjunto de operandos (variables y valores) y operadores que al evaluarse dan un valor. Las expresiones se evalúan de izquierda a derecha y respetando la jerarquía de las operaciones. 


## Operadores

### Operadores Aritméticos

A continuación se muestran los operadores aritméticos de Python, los cuales sirven para trabajar con números enteros y flotantes.

| Operador | Símbolo   |
|---|:---:|
| Suma | +   |
| Resta | -   |
| Multiplicación | *  |
| Division  |  / |
| Division entera | //  |
| Exponente | **  |
|  Módulo| %   |


Modo de uso:
```python title="Formato operaciones aritméticas"
resultado = numero_1  <operador> numero_2
```

```py title="Ejemplo: uso operaciones aritméticas"
n = 7 + 3   #  '10'  
n = 7 - 3   #  '4'
n = 7 * 3   #  '21'
n = 7 / 3   #  '2.3333333333333335'
n = 7 // 3  #  '2'
n = 7 % 3   #  '1'
```

!!! tip "Tip: operadores aritméticos sobre strings"
    Algunos operadores de Python permiten trabajar con `strings`: textos, frases, etc:
    
    - El operador + también puede usarse para **concatenar** cadenas de texto (`strings`). 
    - Con el operador * se puede concatenar la misma frase un número fijo de veces

    ```py title="Ejemplo: aritmetica sobre strings"
    texto = "hola_"
    texto + texto     # 'hola_hola_'
    texto * 3         # 'hola_hola_hola_'
    ```

### Jerarquía de las operaciones aritmeticas
Las operaciones aritméticas tienen una jerarquía de aplicacion por defecto.
Este es el orden de jerarquía de las operaciones, de las primeras en aplicarse a las últimas: 

<!-- Paréntesis → Exponente → Multiplicación → División → Adición → Sustracción -->

1. Paréntesis 
2. Exponente 
3. Multiplicación 
4. División  
5. Adición 
6. Sustracción

Nemotécnico jerarquías: **PEMDAS**

### Operadores de Asignación
Combinan operaciones aritméticas con la asignación (=) a continuación. A la variable de entrada se la afecta con el operador aritmético indicado y una variable o valor adicional.

Ejemplo:   
```python
edad += 3
```
equivale a: 

```python
edad = edad + 3
```


## Operadores Lógicos

Los operadores lógicos trabajan con valores y variables booleanos. 

Modo de uso:
```python title="Formato operaciones lógicas"
resultado = valor_logico_1 <operador> valor_logico_2
```
Los operadores disponibles son los siguientes:

| Operador | Símbolo   |  Salida en 'True'  |
|:---|:---:| -----|
| Y (AND)           |  and | Ambas entradas son 'True'   |
| O (OR)            |    or | Al menos una entrada es 'True'   |
|  NO (NOT)         |    not |  Entrada 'False'  |
| O exclusiva (XOR) |    ^ | Entradas distintas  |



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





### Jerarquía de operaciones lógicas  
Esta es la jerarquía de mayor a menor:
1. not 
2. and 
3. or

### Operadores Relacionales

Los operadores relacionales permiten comparar números enteros y flotantes. 

Los operadores disponibles en Python son:

| Operador | Símbolo   |
|-------|:-------:|
| mayor    |    >      
| menor    |     <      |
| igual    |     ==     |
| mayor o igual  |     >=  |
| menor o igual  |    <=   |
| distinto a    |     !=  |


!!! tip "Tip: operadores relacionales sobre strings"
    
    El operador `==` sirve para comparar si dos `strings` (caracteres, frases, etc) son idénticos. Los otros operadores también pueden usarse para comparar strings por longitud y por contenido de caracteres. 

    ```python title="Ejemplo: comparando strings"
    print('B'  < 'A')	# False
    print('B'  >= 'A')	# True
    print('ABC' > 'A')  # True
    print('ABC' == 'A') # False
    print('ABC' <= 'A') # False
    ```

