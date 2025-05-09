---
tags:
  - Funciones
  - Operadores
  - Tipos
  - Variables
---




# Variables y Asignaciones


## Tipos de Variables

Las variables se crean al asignarles valor. Hay cuatro grandes tipos de variables:


| Función | Uso |
|:------:|:-------|
| `int`  | Números enteros. |
| `float` | Números flotantes. La parte decimal se indica con un punto. |
| `string`| 'Cadena de caracteres': secuencias de caracteres alfanuméricos, lo más cercano al formato texto simple.  |
| `bool` | Valores lógicos booleanos. Dos opciones: `True` y `False`.	|

No hay valor límite para las  variables numéricas. Python distingue entre mayúsculas y minúsculas a la hora de definir variables. 



Es convención en Python que todas  las letras en los nombres de variables sean enteramente en minúsculas y si están formados por varias palabras éstas se unan mediante *guiones bajos* (`_`). Pueden añadirse números en los nombres pero no al comienzo.

!!! info "Tipado dinámico"

    Python tiene ***tipado dinámico***:  las variables pueden cambiar de tipo durante la ejecución, por ejemplo de `int` a `string`, de `string` a `float`, etc. a medida que se guardan nuevos valores.
    
!!! note "función `type()`" 

    El tipo de datos de una variable puede averiguarse con la función `type()`.

    ```python title="Función type()"
    type(16)      # 'int'
    type(1.27)    # 'float'
    type("hola")    # 'str'
    ```



!!! tip "Tip: números complejos"
    Python incluye la posibilidad de trabajar con números complejos indicados como: 
    ```python title="Formato"
    complejo = real + imag j 
    ```
    , donde tanto la parte real como la imaginaria pueden ser tanto `int` como `float`. (Aunque técnicamente los complejos en Python son una clase predefinida)
    ```python title="Ejemplo"
    n = 3 + 4j 
    ```


## Asignaciones

Las asignaciones se realizan con el operador `=`:

```python title="Asignacion"
nombre_variable = valor
```

No hay carácter de fin de instrucción visible, sino que se interpreta como tal el fin de renglón.

Los espacios en blanco a ambos lados del signo `=` son buena práctica en este lenguaje.
Vienen dados por convención.

```python title="Ejemplos: asignaciones"
entero = 16      
flotante = 1.27
mensaje = “Hola mundo”   #(también pueden usarse comillas simples)
```


!!! tip "Tip: asignacion multiple"
    Se puede crear y asignar valor a múltiples variables en un solo renglón. 
    ```python 
    A, B, C = 1.6, 1 , “Hola mundo”
    A, *otros, ultimo = 1.6, 1 , “Hola mundo”, 14 , 8.9 , “chanchito”  
    #ver “desempaquetado de listas”
    ```
    Tambien se puede asignar el mismo valor a varias variables en simultáneo:
    ```python
    A = B = C = 7
    ```

### Indexación de strings
En Python el primer valor de las cadenas de caracteres es el cero. 
Para conocer la longitud de los *string* se usa la función `len()`:

```python title="Longitud de strings"
longitud = len(texto)
```
Si la longitud del vector es n entonces su último elemento será el número (n-1).
Para acceder a un elemento puntual se utiliza los corchetes ( `[]` ):

```python title="indice"
letra = texto[indice]
```

Si el indice cae afuera del string (indice > n-1 )el programa da error de memoria y cancela la ejecución. Sin embargo, en Python se tolera el uso de índices negativos mientras el módulo del índice sea menor a a la longitud de la cadena.



  ```python title="Ejemplo: indice fuera de rango"
  texto = "Hola mundo"
  n= len(texto)         # n = 10 (diez letras)

  letra = texto[ 0]      # letra 'H'  
  letra = texto[ 9]      # letra 'o'  
  letra = texto[10]     # Error: fuera de rango 

  letra = texto[-10]    # letra 'H' 
  letra = texto[-11]    # Error: fuera de rango 
  ```

!!! tip "Tip: indices y listas"
    Este manejo de índices también se usa en los 'vectores' de Python, que son llamados *'listas'* (o *'list'*).
    [Ver listas de Python](../datos/listas.md).

### Rebanado (Slicing)

El rebanado consiste en seleccionar una parte del vector o string en base a **índices numéricos**. Algunas formas de usar el rebanado son:

```python title="Rebanado"
vector[ inicio : ]  # copia desde el índice inicial hasta el final;
vector[ : final ]  	# copia desde el elemento cero hasta (final-1 );
vector[ inicio : final ] #copia desde indice inicial hasta (final-1) ;
vector[ inicio : final : paso ] #copia entre valores de índices pero salteando elementos definidos por 'paso' (valor de incremento);
vector[ : ]		# copia todo;
```

Para invertir el orden de un vector se puede hacer:

```python title="Inversion de vector"
vector[:: -1]	  # copia todo, incremento -1 --> inversion del vector
```

### Conversion de variables

A veces es necesario convertir los valores de una variable a un tipo de variable distinto. Otras veces se necesita asegurar que el tipo de variable es el requerido para una aplicación y no otro. Para estos casos existen ***funciones*** en Python encargadas de la conversion de variables, estas son:

| Función | Uso |
|:------:|:-------|
|  `str( )`   | Convierte a texto  |
|  `int( )`    | Convierte a entero         |
|  `float( )`  | Convierte a flotante       |
|  `bool( )`   | Convierte a valor lógico (booleano)        |

Las ***funciones*** son rutinas reutilizables con nombre, las cuales se usan así:
```py title="Uso funciones"
variable_salida = nombre_funcion( variable_entrada )
```

```py title="Ejemplos: conversion de tipo"
pi = 3.1416   # numero flotante ('float')

texto = str( pi )     # '3.1416'
entero = int(pi)      # '3'
flotante = float(texto)       # '3.1416'
```


Las conversiones de un tipo a otro no siempre dan resultados evidentes. Como ejemplo, se muestra el resultado de convertir a valores lógicos vía la funcion `bool()`:

```python title="Conversión a booleanos"
# entrada: enteros
print( bool( 2) )  # True
print( bool( 1) )  # True
print( bool( 0) )  # False
print( bool(-1) )  # True

# entrada: caracteres y texto
print( bool("")  )  # False
print( bool(" ") )  # False
print( bool("a") )  # True

# entrada: flotantes
print(  bool(3.14) ) # True
print(  bool(0.0)  ) # False
```
Hay que tener en cuenta que no todas las conversiones pueden realizarse, pudiendo dar lugar a la interrupción del programa. A continuacion se muestran algunos ejemplos:
```py
# Ejemplo Nº1
entero = int( "10" )    # uso correcto
entero = int( "hola" )  # ERROR: ¿qué numero equivale a "hola"?

# Ejemplo Nº2
entero = int('3.1416')   # ERROR: se necesita pasar a flotante primero
entero = int(float('3.1416'))   # correcto
```

### Tipado de variables

Python permite *'tipar'* (preasignar un tipo) a las variables. Esto permitirá que el intérprete pueda detectar inconsistencias al asignar valores a las variables.

La forma de tipar los datos es usando los dos puntos y el nombre del tipo de datos. 

Formato:
```python title="Tipado de variables"
entero   :  int
flotante :  float
texto    :  str
logica   :  bool
```


!!! tip "Reducción de bugs por tipado"

    El tipado manual en Python es ***suave***: **no impedirá** la ejecución del programa ni tampoco la abortará al llegar a las asignaciones de valor no compatibles por tipos. En cambio éstas asignaciones serán remarcadas por el entorno de desarrollo, permitiendo que el desarrollador corrija el código de ser necesario durante su escritura y ayudando a prevenir ***bugs*** (errores durante la ejecución del programa) los cuales pueden ser difíciles de identificar sin el uso del tipado.

!!! example "Ejemplo aplicado: indexado de un *string*"
    ```python hl_lines="1 7"
    indice: int             # tipado 
    texto = "A la grande le puse Cuca"

    indice = 10             # asignacion correcta
    letra = texto[indice]   # indexado correcto --> letra 'e'

    indice = "Simon"        # tipo incorrecto --> el intérprete marca el error
    letra = texto[indice]   # fallo de programa
    ```
    Nótese como el tipado de la variable *indice* ayuda a prever el fallo de programa al asignarle un texto como valor, mas no impide su ejecución 


### Métodos 

Los ***métodos*** son operaciones comunes que afectan a las variables. Son similares a las *funciones*  pero están dedicados a los elementos. Los métodos se utilizan así:
```python title="Uso de métodos"
nombre_variable.nombre_metodo(argumento_1, argumento_2, ...)
```
donde los ***argumentos*** son valores de entrada que el método utiliza para procesar y dar su resultado. Los argumentos pueden ser opcionales ú obligatorios, dependiendo de cada método y de la informacion que da cada argumento.

Cada tipo de variable tiene sus propios métodos predefinidos.
En particular, las variables de tipo **string** tienen muchos métodos dedicados para manejarlas. Algunos de sus métodos más usados son:

| Método (string)| Uso |
|:------|:-------|
|`find( seq )`	| Indica la primera ubicacion de la secuencia indicada|
|`replace( seq1, seq2 )`  |   Reemplaza una secuencia por otra.    |
|`title()`  | Formatea como título.       |
|`index()` | 	Indica posición de  comienzo de la secuencia buscada. |
|`isalnum()` |	Verifica si solo hay valores numericos (devuelve `True` o `False`).|
|`isalpha()` |	Verifica si solo hay letras (devuelve `True` o `False`).|
|`isdecimal()` |	Verifica si solo hay decimales (devuelve `True` o `False`).|
|`isdig()`  | Verifica si solo hay dígitos (devuelve `True` o `False`).|
|`islower()`  | Verifica si solo hay minúsculas (devuelve `True` o `False`).|
|`isupper()`  | Verifica si solo hay mayúsculas (devuelve `True` o `False`).|
|`capitalize()` | Devuelve el texto con primera letra  mayúscula y lo demás en minusculas. |
| `lower()` |	Devuelve el texto en minúsculas.|
| `upper()` |	Devuelve el texto en mayúsculas.|
| `strip()` |	Elimina del texto espacios en blanco a derecha y a izquierda.|
| `lstrip()` | Elimina del texto espacios en blanco a izquierda.|
| `rstrip()` | Elimina del texto espacios en blanco a derecha.|
| `split( seq )` |	Divide el texto al detectar un carácter o secuencia indicada. Devuelve una "lista" (arreglo) de strings. El caracter o secuencia `seq` se elimina del resultado.|

La mayoría de estos métodos mencionados no requiere argumentos obligatorios, aunque muchos de ellos implementan argumentos opcionales. 

Una excepción a la regla es el método `split()` :
```python
lista_strings = texto_original.split( caracter_secuencia )
```
Ejemplo de uso:
!!! example "Ejemplo: método `split()`"
    ```python
    original = "tengo 2 naranjas."
    # da una lista (arreglo) de strings
    nuevo = original.split("2") # da ["tengo ", " naranjas."]
    # se separan los dos textos de la lista
    parte_1 = nuevo[0]  # "tengo "
    parte_2 = nuevo[1]  # " naranjas."
    ```

Otra excepción es el método `replace()`:
```python
nuevo = texto_original.replace(subcadena_a_reemplazar, texto_reemplazo, numero_reemplazos)
```
!!! example "Ejemplo: método `replace()`"
    ```python
    original = "tengo 2 naranjas y 2 manzanas."
    nuevo = texto_original.replace("2", "dos", 0 ) # no hace nada
    nuevo = texto_original.replace("2", "dos", 1 ) # sólo reemplaza el primer "2" por "dos"
    nuevo = texto_original.replace("2", "dos", 2 ) # reemplaza ambos "2" por "dos"
    ```

## Entrada de datos de usuario
Para que el usuario pueda ingresar datos se usa la función `input()`:

```python title="input()"
texto_variable = input (mensaje_consola)
```

```python title="Ejemplo: lectura entero"
num = input(“Ingrese un número: ”)    # 'string'
numero = int(num)                     # 'int'
```
El retorno de `input()` es un `string`. Para convertir strings en entero puede usarse la función `int()` , es tanto que para convertir strings en flotante se puede usar la función `float()`. 

!!! warning "Importante: booleanos" 
    La función `bool()` devuelve el valor lógico `False` si su entrada es cero ó un string vacío, en caso contrario da `True`.

## Salida de datos a pantalla

La *función* `print()` permite escribir en pantalla todos los tipos de variables del lenguaje sin importar su tipo. Además elige automáticamente el formato más idóneo para la mayoría de los casos: si la variable es un entero se imprime un entero; si es un numero flotante se escribe como un numero flotante, si es un texto se escribe como un `string`, etc.

Para imprimir el valor de una variable en pantalla simplemente se indica su nombre como argumento:
```python title="variable en pantalla"
print(nombre_variable)
```
Si se necesita hacer lo mismo con múltiples variables en un mismo renglón se escriben todas en orden, separadas por comas:
```python title="multiples variables en pantalla"
print(<variable1>, <variable2>, <variable3>, <...> )
```
`print()` concatena todos los argumentos que se le da al momento de la llamada.

Es posible combinar textos fijos con variables, nuevamente esto se realiza separando textos y variables con comas.

!!! example "Ejemplo aplicado: texto fijo y variables"
    ```python 
    numero = 17
    print("Valor numérico: ", numero )
    ```
 Hay una alternativa con mejor desempeño en lo referente a la ejecución llamada `f-string`, se explica a continuación.

### F-Strings

Los ***formatted-strings*** son **variables de texto** que son afectadas por otras variables. Este es el formato:
```python title="formato f-strings"
texto_variable = f'<texto> {<variable>}'
```
Se comienza el string con una letra 'f', se abren comillas simples ó dobles y dentro de ellas se escriben los textos y las variables, estas últimas entre llaves. Puede haber múltiples segmentos de texto y múltiples variables, siempre y cuando cada variable tenga sus propias llaves:

```python title="formato f-strings - varias variables"
texto_variable  = f'<texto1> {<variable1>} <texto2> {<variable2>} <...>'
```

Los *f-strings* son muy usados adentro de  `print()` directamente:

```python title="salida a consola"
numero = 17
print(f"Valor de la variable: {numero}")  # "Valor de la variable: 17"
```

Colocando dos puntos y un número se reservan espacios para el valor de una variable, los cuales se devan vacíos en caso de ser necesario:
 
```python title="f-strings - espacios reservados"
numero = 17
print(f"Valor de la variable: {numero:10}") # diez espacios reservados para el número
```

Para los números flotantes, colocar un numero tras un punto permite elegir cuántos decimales usar para representar el valor:

```python title="f-strings - nº decimales"
flotante = 13.5136717
print(f"Flotante: {flotante:.1}")   # Muestra 'Flotante: 1e+01'
print(f"Flotante: {flotante:.2}")   # Muestra 'Flotante: 1.4e+01'
print(f"Flotante: {flotante:.3}")   # Muestra 'Flotante: 13.5'
print(f"Flotante: {flotante:.4}")   # Muestra 'Flotante: 13.51'
```
Este mecanismo es combinable con la reserva de espacios vista previamente:

!!! example "Ejemplo: f-strings con espacios y decimales"
    ```python
    flotante = 13.5136717
    texto = f"Flotante:{flotante:7.4}" # seis espacios reservados para el numero, cuatro cifras

    print(texto)  # da 'Flotante:  13.51'  
    ```
    Nótese que en el ejemplo previo hay una variable de cuatro cifras , un punto y siete espacios, por ello se autocompletará con dos espacios vacíos. 


Para más opciones de formato ver el [**manual de entrada y salida de Python**](https://docs.python.org/es/3/tutorial/inputoutput.html)

