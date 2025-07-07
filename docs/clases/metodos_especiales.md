---
tags:
  - Clases
  - Sobrecarga
---



# Métodos Especiales (*dunder*)

Los métodos especiales son métodos 
reservados del lenguaje Python 
para definir o modificar el comportamiento de las clases 
ante determinadas condiciones 
u operadores.
Los métodos especiales van marcados
con doble guion a ambos lados de su nombre,
por eso se los llama **dunder** (*double underscore*).

En este ejemplo se muestran algunos de los métodos especiales más usados: 

```python hl_lines="3 8  12  17" title="Métodos especiales"
class Persona:
    # Inicializador de instancias
    def __init__(self, nombre,edad):     
        self.nombre = nombre
        self.edad = edad

    # Conversion a texto todo el contenido
    def __str__(self):      
        return f'Persona(nombre={self.nombre}), edad={self.edad}'

    # Crea un formato para representar la clase como texto
    def __repr__(self):     
        return f"Persona('{self.nombre}','{self.edad}')"

    # Metodos para la sobrecarga de operadores
    # Ejemplo: suma de clases
    def __add__(self, otro):        
        nuevo_valor= self.edad + otro.edad  
        return Persona(self.nombre+otro.nombre, nuevo_valor)
```

Ejemplo de uso:

```python 
# Creacion objeto (instancia)
yo = Persona('Sam', 138)

# lectura del objeto como texto
texto = yo
print(texto)               

# representacion del objeto en formato texto
repre = repr(yo)
print(repre)

# Reconstruccion del objeto desde texto
resultado = eval(repre)     # funcion  eval()
print(resultado.nombre)
print(resultado.edad)

# "Suma" de clases 
tu = Persona('Ana', 89)
tu_y_yo = tu + yo
print(tu_y_yo)
```


## Sobrecarga de operadores

### Introducción

La *sobrecarga de operadores*
es la capacidad de los lenguajes
para ejecutar diferentes operaciones
al usar un mismo operador,
dependiendo del tipo de operandos
que sean afectados.

Por ejemplo, el operador `+` ("suma") 
se comporta de distinta manera
ante variables de tipo `int`, `float` y `str`:

```py title="Sobrecarga de operadores - Suma"
# suma de enteros
entero = 3 + 1              # '4'

# suma de flotantes   
flotante = 1.21 + 2.5       # '3.71'

# concatenación de strings
texto = "Hola " + "Mundo"   # 'Hola Mundo'         
```
En este ejemplo, 
las instrucciones del procesador 
involucradas para la suma de flotantes 
son distintas a las necesarias para la suma de enteros.
Más aún, la "suma" entre *strings* ni siquiera es una suma aritmética 
sino que es una concatenación
(copia de datos al final).
En cualquier caso, el intérprete 
"elige" qué operaciones ejecutar 
para cada operador según qué tipos de variables afecte.

Sin embargo,
el intérprete no puede adivinar 
qué instrucciones ejecutar 
ante variables que no tengan un comportamiento predefinido.
Por ejemplo, si se define una clase 
para manejar vectores de dos dimensiones:

```py title="Clase para vectores"
class Vector2D:
    def __init__(self, x=0, y=0):
        """Crea un vector de dos dimensiones."""
        # componentes internos: x e y
        self.x = x
        self.y = y
```

el intérprete no sabe qué hacer en caso de intentarse la suma entre objetos de esta clase:

```py title="Suma de vectores - No implementada"
v = Vector2D( 3,  1 )
w = Vector2D( 1, -3 )

t = v + w       # error
```

y entonces se dispara una excepción:

```bash
TypeError: unsupported operand type(s) for +: 'Vector2D' and 'Vector2D'
```

### Implementación

En el ejemplo previo
se necesita implementar 
la suma vectorial,
que deberá ejecutarse con el operador `+`.

La operación de suma
se implementa con ayuda 
del método especial `__add__`:

```py title="Clase para vectores - Suma vectorial"
class Vector2D:
    def __init__(self, x=0, y=0):
        """Crea un vector de dos dimensiones."""
        # componentes internos: x e y
        self.x = x
        self.y = y

    def __add__(self, otro):
        """Habilita la suma vectorial con el operador '+'. """
        # Implemento la suma componente a componente
        x = self.x + otro.x
        y = self.y + otro.y
        # Creo un nuevo vector con el resultado
        return Vector2D(x, y)
```

Como la operación de suma
se realiza entre dos objetos,
la método toma como referencia
al primer elemento (`self`) 
e incorpora como argumento al segundo 
(`otro`).

Una vez implementado el método,
con el se calculan los valores del nuevo vector 
y se crea un vector nuevo como retorno.

```py title="Suma de vectores - Implementada"
v = Vector2D( 3,  1 )
w = Vector2D( 1, -3 )

t = v + w       # 't.x=4', 't.y=-2'
```
Ahora el intérprete sabe como ejecutar esta suma.

A continuación se enumeran 
algunos de los métodos especiales
implementados en Python 
para definir el comportamiento 
de los operadores.

!!! info  "Operadores unarios vs operadores binarios"

    - Los ***operadores unarios*** son aquellos 
    que afectan a un solo elemento. 
    Sus métodos reservados requieren solamente el argumento `self`.
    - Los ***operadores binarios*** son aquellos 
    que afectan a dos elementos en simultáneo.
    Sus métodos reservados requieren un argumento adicional.

!!! warning "Argumentos inmutables"

    No se puede cambiar el número de argumentos
    de los métodos especiales. 
    Esto significa que 
    no se puede reescribir a un operador unario
    como si fuera binario
    y viceversa.


### Operadores aritméticos
<!-- 
Python implementa los siguientes métodos 
para las operaciones aritméticas: 
-->

|Operador| Método|
|:---:|:---|
|`+`|`__add__`|
|`-`|`__sub__`|
|`*`|`__mul__`|
|`**`|`__pow__`|
|`/`|`__truediv__`|
|`//`|`__floordiv__`|
|`%`|`__mod__`|

<!-- 
En ellos se necesita agregar un segundo objeto como argumento.  
-->



### Operadores lógicos

|Operador| Método|
|:---:|:---|
|`and`|`__and__`|
|`or` |`__or__`|
|`not`|`__not__`|

Nótese que el operador
`not`
es unario.

### Operadores bit a bit


|Operador| Método|
|:---:|:---|
|`and`, `&`|`__and__`|
|`or`, `|`|`__or__`|
|`^`|`__xor__`|
|`~`|`__invert__`|
|`<<`|`__lshift__`|
|`>>`|`__rshift__`|


Nótese que el operador
`~`
es unario.

### Operadores relacionales

|Operador| Método|
|:---:|:---|
| `==` | `__eq__`|
| `!=` | `__ne__`|
| `<` | `__lt__`|
| `<=` | `__le__`|
| `>` | `__gt__`|
| `>=` | `__ge__`|






## Métodos especiales


### `__str__`

Este método permite representar la data interna
de la instancia de clase 
como texto (`str`). 
Esta representación es informal y está pensada para dar información práctica al desarrollador.  

Esta información se consulta con la función `str()`:

```py
texto = str(objeto)
```


### `__repr__`

Este método también permite representar la data interna
como texto. 
A diferencia de `__str__`,
esta información debe
seguir un formato específico 
para poder ser usada por la función `eval()`:
  


```py
texto = eval(objeto)
```


### `__init__`

`__init__` es el método **constructor** o **inicializador**.
Es el encargado de darle estructura al nuevo objeto.


`__init__` siempre es llamado despues que `__new__`. 


### `__new__`

El método `__new__` es el encargado de crear las nuevas instancias de la clase.
Este método rara vez es sobreescrito.

```py
class Clase:
    def __new__(cls):
        # Crea la nueva instancia
        instancia = super().__new__(cls)
        # devuelve el objeto como retorno
        return instancia
```
El argumento `cls` representa a la nueva instancia,
en contraposición a `self` que se apunta a sí mismo. 

Para funcionar correctamente, 
`__new__` debe crear la nueva instancia
(`super().__new__(cls)`)
y retornarla. 

!!! warning  "Argumentos"
    A `__new__` debe asignársele 
    los mismos argumentos adicionales 
    que a `__init__` para que la ejecución sea correcta:

    ```py   
    class Clase:
        def __new__(cls, *args, **kwargs):      # argumentos genéricos
            instancia = super().__new__(cls)
            return instancia

        def __init__(self, argumento_1, argumento_2):
            pass
    ```

 `__new__` siempre es llamado antes que `__init__`. 



### `__call__`

Este método permite utilizar a los objetos de la clase
como si fueran funciones. 

Así es la definición:

```py title="Método __call__ - Definición y uso"
class Llamable:
    def __call__(self):
        print( "¿Me llamabais?" )


objeto = Llamable()     # creacion de instancia
objeto()                # llamado como si fuera una función
```

Este método puede manejar atributos y argumentos como cualquier otro.
Con ayuda de este método pueden crearse familias de objetos
utilizables como funciones:


```py title="Método __call__ - Ejemplo"
class Multiplicador:
    def __init__(self, valor):
        self.__valor = valor

    def __call__(self, arg):
        return self.__valor * arg 


# instancias con distintos valores de inicialización
doble     = Multiplicador(2)
triple    = Multiplicador(3)
cuadruple = Multiplicador(4)

# uso
v1 = doble(9)
v2 = triple(9)
v3 = cuadruple(9)
```


### `__dict__`

Este método ayuda a leer los valores
de los atributos internos convertidos a diccionario.
En él se respetan los nombres de los atributos,
que pasan a ser las claves del diccionario devuelto.


```py title="Método __dict__ - Ejemplo"
# coordenadas X, Y y Z como clase
class Coords:
    def __init__(self):
        self.x=3
        self.y=4
        self.z=-1


# instancia de clase
coord = Coords()
#  Lectura de diccionario interno
print(coord.__dict__)
```


## `dir()`

Esta función permite consultar los métodos implementados de la clase pasada por argumento.



## Referencias

[Bigcode.es - Métodos Especiales y Sobrecarga de Operadores en Python](https://bigcode.es/metodos-especiales-y-sobrecarga-de-operadores-en-python/)

[GeeksForGeeks - `__call__` in Python](https://www.geeksforgeeks.org/__call__-in-python/)

[GeeksForGeeks - `__init__` vs `__new__`](https://www.geeksforgeeks.org/python-init-vs-new/)