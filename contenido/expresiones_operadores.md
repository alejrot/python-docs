<a name="top"></a>

## [Volver](../Python.md#expresiones-y-operadores)


# Expresiones y Operadores

## Expresiones
Las expresiones son un conjunto de operandos (variables y valores) y operadores que al evaluarse dan valor. Las expresiones se evalúan de izquierda a derecha y respetando la jerarquía de las operaciones. 


## Operadores

### Operadores Aritméticos

| Operador | Símbolo   |
|---|---|
| Suma | +   |
| Resta | -   |
| Multiplicación | *  |
| Division  |  / |
| Division entera | //  |
| Exponente | **  |
|  Módulo| %   |

**Importante:** el operador + también puede usarse para **concatenar** cadenas de texto (*strings*). Y si se usa el operador * se concatena la misma frase un número fijo de veces

### Jerarquía de las operaciones aritmeticas
Las operaciones aritméticas tienen una jerarquía de aplicacion por defecto.
Este es el orden de jerarquía de las operaciones, de las primeras en aplicarse a las últimas: 

Paréntesis → Exponente → Multiplicación → División → Adición → Sustracción

Nemotécnico jerarquías: **PEMDAS**


## Operadores Lógicos

Los operadores lógicos trabajan con valores y variables booleanos. 

Modo de uso:
```python
<resultado> = <condicion_1>  <operador> <condicion_2>
```
Los operadores disponibles son los siguientes:

| Operador | Símbolo   |
|---|---|
| Y (AND)           |  and |
| O (OR)            |    or |
|  NO (NOT)         |    not |
| O exclusiva (XOR) |    ^ |


### Jerarquía de operaciones lógicas  
not → and → or

### Operadores Relacionales

Los operadores relacionales permiten comparar números enteros y flotantes. También sirve para comparar strings (caracteres, frases, etc).

Los operadores disponibles en Python son:

| Operador | Símbolo   |
|-------|-------|
| mayor    |    >      
| menor    |     <      |
| igual    |     ==     |
| mayor o igual  |     >=  |
| menor o igual  |    <=   |
| distinto       |     !=  |

**Importante:** el operador == sirve para comparar si dos strings son idénticos. Los otros operadores también pueden usarse para comparar strings por longitud y por contenido de caracteres (revisar)

Ejemplos:
```python
print('B'  < 'A')	# False
print('B'  >= 'A')	# True
print('ABC' > 'A')  # True
print('ABC' == 'A') # False
print('ABC' <= 'A') # False
```

### Operadores de Asignación
Combinan operaciones aritméticas con la asignación (=) a continuación. A la variable de salida se la afecta con el operador aritmético indicado y una variable o valor adicional.

 Ejemplo:   
```python
edad += 3
```
equivale a: 

```python
edad = edad +3
```

----
----
----

## [Inicio](#expresiones-y-operadores)

## [Volver](../Python.md#expresiones-y-operadores)
