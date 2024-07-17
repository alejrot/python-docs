

# Clases II - Decoradores, Abstracciones y Métodos Especiales



## Decoradores

Los decoradores añaden código a una funcion especificada de forma externa. El código añadido pueden ir antes, después o alrededor de la función.

[Más sobre los decoradores](decoradores.md)



## Decorador 'Property'

El decorador `property` es un tipo reservado de decoradores que permite crear métodos de acceso, escritura y eliminación que comparten nombre y que no requerirán el uso de paréntesis.

Ejemplo de definición:

```python hl_lines="6 10 14" title="Uso decorador Property"
class Persona:
    def __init__(self, nombre):
        self.__myname = nombre      # atributo privado

    # Decorador 'Property'
    @property                   # metodo "getter": acceso
    def nombre(self):               
        return self.__myname        

    @nombre.setter              # metodo "setter": escritura
    def nombre(self, nuevo_nombre):     
        self.__myname = nuevo_nombre   

    @nombre.deleter             # metodo "deleter": eliminacion
    def nombre(self):                   
        del self.__myname
```
De esta forma los métodos creados se ven y se usan como si fuesen atributos públicos:

```python title="uso métodos 'property'" hl_lines="5-7"
# creacion de instancia
yo = Persona("Yoh")

# Los métodos son accedidos como si fueran atributos
name = yo.nombre        # lectura
yo.nombre = "Meh"       # escritura
del yo.nombre           # eliminación
```



## Abstracción

Consiste en ocultar los detalles innecesarios y mostrar solamente las funcionalidades necesarias.

En la práctica la abstracción se realiza encapsulando los atributos y funcionalidades específicos  adentro de funcionalidades más generales y por tanto más sencillos de manejar.


## Clases Abstractas

Las clases abstractas **sirven como plantilla** para crear otras clases. De éstas **no** pueden crearse instancias de una clase abstracta; para crear las instancias se necesita crear subclases de la clase abstracta.

Para crear clases abstractas deben importarse la clase `ABC` y el decorador `abstractclassmethod` desde el módulo `abc`:
```python
from abc import ABC, abstractclassmethod
```

La **clase `ABC`** es una clase abstracta que sirve de referencia para crear las demás como subclases. Por otra parte el **decorador `abstractclassmethod`** permite crear métodos abstractos, los cuales  deben usarse o redefinirse sí o sí respetando además los argumentos de entrada indicados.

```python title="Clase abstracta" hl_lines="2 5 12"
# Superclase abstracta
class Persona(ABC):
 
    # inicializador abstracto: se invoca o se reemplaza
    @abstractclassmethod
    def __init__(self, nombre, edad, actividad):
        self.nombre = nombre
        self.edad   = edad  
        self.actividad = actividad

    #metodo abstracto vacío: debe redefinirse por las subclases SI O SI
    @abstractclassmethod
    def hacer_actividad(self):
        pass                    # no hace nada             

    # metodo opcional con comportamiento ya definido
    def presentarse(self):
        print(f"Me llamo {self.nombre} y tengo {self.edad} años")
```
Lo interesante de crear un método abstracto es que éste obliga a las subclases a asignarle un comportamiento (polimorfismo) so pena de arrojar error.


```python title="Subclases de clase abstracta"
# Subclases de la clase abstracta
class Estudiante(Persona):
    def __init__(self, nombre, edad, actividad):
        # uso inicializador abstracto
        super().__init__(nombre,edad, actividad)

    #polimorfismo sobre metodo abstracto (obligatorio)
    def hacer_actividad(self):
        print(f"Estoy estudiando: {self.actividad}")


class Trabajador(Persona):
    def __init__(self, nombre, edad, actividad):
        # uso inicializador abstracto
        super().__init__(nombre,edad, actividad)    

    #polimorfismo sobre metodo abstracto (obligatorio)
    def hacer_actividad(self):
        print(f"Estoy trabajando en: {self.actividad}")
```

Las clases derivadas de la clase abstracta se usan normalmente:
```python title="Uso de subclases"
#instancias de las clases 'hijas'
yo = Estudiante("Meh","35", "developing")  
yo.presentarse() 
yo.hacer_actividad()    # uso metodo modificado

tu = Trabajador("Tuh","40", "SCRUM Mastering")   
tu.presentarse()
tu.hacer_actividad()    # uso metodo modificado
```

!!! failure "Error: instancias directas"
    La clase abstracta **no admite instancias directas**:
    ```python
    # instancia de clase abstracta
    yo = Persona("Meh","35")    # da ERROR
    ```

## Metodos Especiales ('dunder')

Los métodos especiales son métodos predefinidos del lenguaje Python para definir el comportamiento de las clases ante determinadas condiciones. Los métodos especiales van marcados doble guion a ambos lados de su nombre.

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

