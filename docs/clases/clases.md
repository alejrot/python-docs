---
tags:
  - Clases
---


# Clases 



Las **clases** son objetos que poseen atributos y funcionalidad
integrados:

- Los **atributos** son valores guardados de los parámetros, es decir son variables internas de la clase.
- La funcionalidad de la clase es representada por **métodos**, que son funciones específicas de la clase. 


## Definición

Las clases se definen así:

```python title="Clases - Definición "
class nombre_clase:
    # inicialización
	def __init__(self, param1, param2, ...):
		self.atributo1 = param1		
		self.atributo2 = param2
```

La palabra `self` es un elemento auxiliar
que hace referencia a cada nuevo objeto 
creado por las clases, 
los cuales son llamados *instancias*.


## Métodos

Para utilizar los atributos 
de cada instancia de clase 
se añaden los métodos, 
que se definen así:

```python title="Clases - Definición (con métodos)"
class nombre_clase:
    # inicialización
	def __init__(self, param1 , param2, ...):	
		self.atributo1 = param1		
		self.atributo2 = param2

	def metodo1(self):
		#código 1

	def metodo2(self):
		#código 2
```

Los métodos se definen de manera muy similar a las funciones,
pero incorporando como primer argumento el objeto `self`.



## Instancias

Para crear *instancias* (variables con el formato y métodos de la clase) se llama a la clase y se asignan valores a todos los parámetros en orden excepto a `self` (éste se omite):

```python title="Clases - Instancia"
nueva_instancia = nombre_clase(valor_1, valor_2, ...)
```



## Atributos públicos y privados

Los *atributos* de la clase son *públicos* por defecto, es decir pueden ser accedidos directamente por su nombre:

```python
nombre_instancia.atributo = valor
variable = nombre_instancia.atributo
```


Para hacer que los atributos de la clase sean *"privados"* se les antepone en su definición dos *guiones bajos* (**`__`**):

```python title="Clases - atributos privados"
class nombre_clase:
	def __init__(self, param1 , param2, ...):	
        #inicialización (obligatoria)
		self.atributo1    = param1	# atributo público		
		self.__atributo2  = param2	# atributo privado
```

Si se intenta acceder a un atributo privado desde afuera de los métodos de la clase no se disparará un error; 
en cambio se creará un atributo alterno con el mismo nombre. 
Por este motivo hay que evitar a toda costa el intentar acceder a los atributos privados desde afuera. 

!!! info "*getters* y *setters*"

    En Python **se prefiere evitar** 
    los métodos 'get' y  'set' para lectura y escritura de atributos,
    por ello lo habitual es declarar públicos los atributos de interés para el acceso externo 
    y dejar privados los atributos con data interna de los métodos. 

    Este hábito contrasta con otros lenguajes donde sí se habitúa crear metodos específicos para leer y escribir la data interna
    (ejemplo: JavaScript).


## Eliminar atributos

Los atributos pueden ser eliminados llamando al deleter 
`del`:

```python
del nombre_instancia.atributo
```

Sólo se eliminará el atributo en la instancia elegida.
Todas las demás preservarán su atributo intacto.




### Metodos privados

Es posible crear metodos privados definiéndolos con dos giones adelante, igual que se hace con los atributos:

```python title="Clases - Métodos privados"
class nombre_clase:
    # inicialización
	def __init__(self, param1 , param2, ...):	
        # codigo inicializacion

    def publico(self):
        self.__privado(self)
        # codigo publico

    def __privado(self):
        # codigo privado
```

Si se intenta acceder a un metodo privado desde afuera de la clase se producirá un error. 

Los métodos privados son útiles para hacer rutinas auxiliares de los métodos públicos de la clase.



## Referencias

[Stack Overflow - What's the pythonic way to use getters and setters](https://stackoverflow.com/questions/2627002/whats-the-pythonic-way-to-use-getters-and-setters)

[HecktorProfe - Herencia múltiple](https://docs.hektorprofe.net/python/herencia-en-la-poo/herencia-multiple/)

[BarcelonaGeeks - Agregación y Composición](https://barcelonageeks.com/python-oops-agregacion-y-composicion/)

