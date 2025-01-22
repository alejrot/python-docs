---
tags:
  - Clases
  - Decoradores
  - Property 
---



# Decorador 'Property'

El decorador *property* es un tipo reservado de decoradores que permite crear métodos de acceso, escritura y eliminación que comparten nombre y que no requerirán el uso de paréntesis.

El desarrollador trabajará con estos métodos modificados 
por el decorador *property*
como si fueran atributos.

<!-- 
[Más sobre los decoradores (genérico)](decoradores.md) 
-->

Un aspecto interesante de los métodos afectados por *property* es la posibilidad de combinar el procesamiento de los datos internos de la clase con la manipulación de algún atributo específico. 
Lo habitual es afectar atributos privados.


## Definición


Se crean hasta tres métodos con igual nombre
pero que cambian de argumentos y decoradores:

- El método de lectura 
(*getter*) 
se implementa agregándole justo encima de la definición del método el decorador `property` 
y debe tener la cláusula `return`
para devolver el valor del atributo interno deseado;

- El método de escritura 
(*setter*)
incluye como decorador el nombre del método seguido de `.setter` 
y el método debe tener un argumento para ingresar el nuevo valor;

- El método de eliminación
(*deleter*) 
tiene como decorador el nombre del método seguido de `.deleter`. 
Este método elimina el atributo privado que se le indique con la cláusula `del`.

Sintaxis:

```python  title="Métodos 'Property' - Definición"
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

```python title="Métodos 'Property' - Uso" hl_lines="5-7"
# creacion de instancia
yo = Persona("Yoh")

# Los métodos son accedidos como si fueran atributos
name = yo.nombre        # lectura
yo.nombre = "Meh"       # escritura
del yo.nombre           # eliminación
```




