

# Singleton



Singleton es considerado un pàtrón de diseño.

Se trata de un tipo de clases
que crean una única instancia a lo largo de todo el programa.

## Definición

Este tipo de clases requiere definir el método `__new__`
y crear un atributo adicional con valor `None`,
que en este ejemplo se llama `_instance`:

```py title="Instancia única - definición básica"
class Singleton:

    _instance = None    # atributo compartido

    def __new__(cls):
        if not cls._instance:
            print("creacion de instancia Singleton")
            cls._instance = super(Singleton, cls).__new__(cls)
        else:
            print("instancia repetida")
        return cls._instance
```

Lo usual es agregar argumentos genéricos al método `__new__`
y definir el método `__init__`: 

```py title="Instancia única - definición típica"
class Singleton:

    _instance = None    # atributo compartido

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            print("creacion de instancia Singleton")
            cls._instance = super(Singleton, cls).__new__(cls)
        else:
            print("instancia repetida")
        return cls._instance

    def __init__(self, argumento_1, argumento_2):
        pass
```

## Uso

Si se intentara crear maś de una instancia
lo que se obtendrá como salida
es una referencia a la primera instancia creada:

```py title="Instancia única - llamado"
# todas las instancias son la misma
instancia_1 = Singleton()
instancia_2 = Singleton()

print(instancia_2 is instancia_1)   # 'True'
```

Esto puede verificarse en base a la dirección
del objeto creado,
el cual coincidirá en todas las instancias creadas:

```py title="Instancia única - dirección"
print(instancia_1)  # '<__main__.Singleton object at 0x7efc2cb474d0>'
print(instancia_2)  # '<__main__.Singleton object at 0x7efc2cb474d0>'
```

## Ejemplo

En este ejemplo se crea una clase
que guarda en su interior un nombre.

```py
class Unico:

    _creado = None

    def __new__(cls,  *args, **kwargs):
        if not cls._creado:
            cls._creado = super(Unico, cls).__new__(cls)
        return cls._creado

    def __init__(self, nombre):
        self.nombre=nombre


# dos llamados a la clase
instancia_1 = Unico("Simona")
instancia_2 = Unico("Alexio")
```

Se corrobora que el valor asignado al nombre
es el mismo para todas las instancias.

```py
print(instancia_1.nombre)   # 'Alexio'
print(instancia_2.nombre)   # 'Alexio'
```

## Referencias


[MouredevTV - Singleton (Youtube)](https://youtu.be/cOIcFo_w9hA?list=PLv0dxH7HRDx_kQRNoldG7iPvydy8DyvE3)
