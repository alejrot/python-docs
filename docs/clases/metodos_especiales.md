---
tags:
  - Clases
---



# Métodos Especiales (*dunder*)

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

