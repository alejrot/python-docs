---
tags:
  - Clases
  - ABC
  - POO
---


# Clases abstractas


## Abstracción

La abstracción
consiste en ocultar los detalles innecesarios y mostrar solamente las funcionalidades necesarias.

En la práctica la abstracción se realiza encapsulando los atributos y funcionalidades específicos adentro de funcionalidades más generales y por tanto más sencillos de manejar.


## Clases Abstractas

Las clases abstractas **sirven como plantilla** para crear otras clases.
En estas clases se enumeran los métodos y sus respectivos argumentos
que deberán ser implementados de manera obligatoria por sus clases derivadas. 


No se permite crear instancias directamente desde la clase abstracta,
sino que
se necesita crear subclases de la clase abstracta
y a partir de ellas se crean las instancias.

Las clases abstractas ayudan a "maquetar" el sistema de clases de los programas permitiendo un mejor diseño y una mejor mantenibilidad de los programas.
Esto se vincula con los [principios SOLID](SOLID.md) de diseño.


## Definición

Para crear clases abstractas deben importarse la clase `ABC` y el decorador `abstractclassmethod` desde el módulo `abc`:
```python
from abc import ABC, abstractclassmethod
```

La **clase `ABC`** es una clase abstracta que sirve de referencia para crear las demás como subclases. Por otra parte el **decorador `abstractclassmethod`** permite crear métodos abstractos, 
los cuales **deben usarse o redefinirse sí o sí** 
respetando además los argumentos de entrada indicados.

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
