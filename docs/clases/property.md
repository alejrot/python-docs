




## Decoradores

Los decoradores añaden código a una funcion especificada de forma externa. El código añadido pueden ir antes, después o alrededor de la función.

Python implementa decoradores predefinidos para afectar a las clases creadas por el desarrollador.

<!-- 
[Más sobre los decoradores (genérico)](decoradores.md) 
-->



# Decorador 'Property'

El decorador *property* es un tipo reservado de decoradores que permite crear métodos de acceso, escritura y eliminación que comparten nombre y que no requerirán el uso de paréntesis.

El desarrollador trabajará con estos métodos modificados 
por el decorador *property*
como si fueran atributos.


## Definición


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

## Uso

Los métodos creados se ven y se usan como si fueran atributos públicos:

```python title="uso métodos 'property'" hl_lines="5-7"
# creacion de instancia
yo = Persona("Yoh")

# Los métodos son accedidos como si fueran atributos
name = yo.nombre        # lectura
yo.nombre = "Meh"       # escritura
del yo.nombre           # eliminación
```




