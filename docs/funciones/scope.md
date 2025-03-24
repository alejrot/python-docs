---
tags:
  - Funciones
---

# Visibilidad *(scope)*


El *scope* o visibilidad
indica dónde se puede usar una variable.
Hay dos opciones:
*local* y *global*.

## Variables locales

Las variables locales son aquellas definidas dentro de las funciones
y son de uso exclusivo de la función que las crea.


Ejemplo: 
```python
# definicion de funcion, sin valores de entrada
def mostrar_a( ):
    # variable local: 'a' 
    a = 3
    print(a) 


# Código programa principal
mostrar_a( )  # '3'       
print(a)        # ERROR: variable local no visible desde afuera de su funcion
```


## Variables globales

Las variables globales son aquellas definidas
por fuera de las funciones 
y son visibles por fuera de ellas.
Las funciones son incapaces de acceder a las variables globales,
excepto cuando estas variables son declaradas
adentro de las funciones
con la palabra clave `global` : 

```python title="Variables globales" hl_lines="1 5"
nombre_variable_global = 0      #creacion 

def incrementar_global():
    # ...
    global nombre_variable_global       # declaración
    valor = nombre_variable_global      # lectura
    nombre_variable_global = 1          # modificación
```


!!! warning "Uso de variables globales"

    El uso de variables globales 
    por **dentro** de las funciones
    se considera una **mala práctica**
    y es mejor evitarlo siempre que sea posible.
    Esto se debe a las posibles interaciones imprevistas entre varias funciones
    mediante una misma variable global.




