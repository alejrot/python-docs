

# Clases III - Principios SOLID



## Principios SOLID

Los principios SOLID son una guía de principios cuya aplicación busca lograr las siguientes ventajas:

- 1 - Mantenibilidad
- 2 - Reusabilidad
- 3 - Legibilidad
- 4 - Extensibilidad

SOLID son las siglas de los siguientes principios:

- SRP - Principio de Responsabilidad Única
- OCP - Principio de Abierto/Cerrado
- LSP - Principio de Sustitucion de Liskov
- ISP - Principio de Segregacion de Interfaz
- DIP - Principio de Inversion de Dependencias 

La aplicación de estos principios ayuda a mejorar la calidad del código; sin embargo no es una tarea trivial y debe sopesarse en cada proyecto sus ventajas e inconvenientes.

A continuacion se explica cada uno de estos principios.


## SRP - Principio de Responsabilidad Unica
Cada clase debe tener una única responsabilidad o tarea. Si se necesitan varias responsabilidades o tareas éstas deben repartirse en varias clases.

Ejemplo: un auto.
- Una clase "Tanque"  que registra el nivel de combustible del auto y gestiona la recarga. 
- una clase  "Auto" que gestiona la posición y el movimiento del mismo consumiendo combustible del tanque.

En este contexto "Tanque" es superclase de "Auto".

Una misma clase puede tener varios metodos pero éstos deben estar asociados a la misma funcionalidad. En el ejemplo: "Tanque" no controla ni la posicion ni el movimiento del auto, en tanto que "Auto" no gestiona la carga de combustible.


## OCP - Principio de Abierto/Cerrado
Las entidades de software (clases, funciones) deben ser "Abiertas para extension, cerradas para modificacion".


Ejemplo: una familia de clases para gestionar notificaciones remotas.

La clase "Notificador" (superclase) crea un método para manejar mensajes de notificacion cuyo comportamiento interno no está definido:

```python
class Notificador:
    def __init__(self, usuario, mensaje):
        self.usuario = usuario          # objeto con datos del usuario
        self.mensaje = mensaje


    def Notificar(self):                # Metodo genérico
        raise NotImplementedError       # error por comportamiento no definido
```

Las subclases se encargan de adaptar el envio de notificaciones en base a distintas vías de comunicacion: mail, SMS, etc. usando polimorfismo: 

```python
class NotificadorEmail( Notificador )
    def Notificar(self):
        print(f"Enviando MAIL a {self.usuario.email}")

class NotificadorSMS( Notificador )
    def Notificar(self):
        print(f"Enviando SMS a {self.usuario.sms}")

# (otros)
```

De esta manera en vez de reescribir el método de la clase original se crean clases hijas con el comportamiento deseado para cada situación.

## LSP - Principio de Sustitución de Liskov

Toda subclase hereda **todas** las propiedades de su superclase. Pero esto puede introducir conflictos lógicos bajo ciertas circunstancias.

Ejemplo: capacidad de vuelo de las aves.

```python
class Ave:
    def volar(self):
        return "Puedo volar"        # asumimos una propiedad general

class Avestruz(Ave):
    def volar(self):
        return "NO puedo volar"     # hay un conflicto de herencia
```

La solución a este problema consiste en crear distintas clases intermedias alternativas entre sí que se repartan las propiedades conflictivas: 

```python
class Ave:
    pass

class AveVoladora(Ave)
    def volar(self):
        return "Puedo volar"        

class AveNoVoladora(Ave)
    pass   

class Avestruz(AveNoVoladora):
    pass                        # No se hereda la propiedad de vuelo
```

## ISP - Principio de Segregacion de Interfaz

"Ningun usuario debe ser obligado a usar interfaces que no necesite". Hay que eliminar las dependencias que no se necesiten.

Python no usa la creacion de interfases, como sucede con otros lenguajes. En Python las interfases son implícitas.

Ejemplo: dos clases llamadas 'Humano' y 'Robot' que representan las actividades de conjunto: comer, dormir y trabajar.

```python
# MAL
# Clase abstracta genérica describiendo multiples actividades
class Actividades(ABC):
    def trabajar(self):
        print("Trabajando")

    def comer(self):
        print("Comiendo")

    def dormir(self):
        print("Durmiendo")

# Los humanos trabajan, comen y duermen
class Humano( Actividades ):

# ERROR:
# Los robots no comen ni duermen pero heredan estas actividades
class Robot( Actividades ):
```

Para aplicar este principio primero se crean las clases abstractas para declarar cada método utilizable por las clases:
```python
from abc import ABC, abstractclassmethod

class Trabajador(ABC):
    @abstractclassmethod
    def trabajar(self):
        pass

class Comedor(ABC):
    @abstractclassmethod
    def comer(self):
        pass

class Durmiente(ABC):
    @abstractclassmethod
    def dormir(self):
        pass
```

Cada clase sólo usa las superclases abstractas que necesita y redefine sus métodos:

```python
# Los humanos trabajan, comen y duermen --> heredan todos
class Humano(Trabajador, Comedor, Durmiente):
    def comer(self):
        print("El humano está comiendo")

    def trabajar(self):
        print("El humano está trabajando")

    def dormir(self):
        print("El humano está durmiendo")


# Los robots no comen ni duermen --> No heredan lo que no necesitan
class Robot(Trabajador):
    def trabajar(self):
        print("El ROBOT está trabajando")

```
De esta manera cada clase sólo tiene acceso a los métodos que tienen sentido para ella.

```python
# instancias de prueba
humano = Humano()
robot  = Robot()

# métodos accesibles para cada objeto
robot.trabajar()

humano.comer()
humano.trabajar()
humano.dormir()

# métodos no habilitados
# robot.comer()         # da error (no está definido)
# robot.dormir()         # da error (no está definido)
```
En resumen, creando varios métodos abstractos en clases separadas se previenen problemas de herencia.


## DIP - Principio de Inversion de Dependencias 
- Los modulos de alto nivel **no** deben depender de los modulos de bajo nivel. Ambos deben depender de abstracciones;
- Los detalles deben depender de las abstracciones y no al revés. 

En general, las clases de alto nivel se encargarán de las generalidades en tanto que las clases de bajo nivel se dedicarán a tareas específicas.

Ejemplo: una clase para un corrector ortográfico que depende de una clase de bajo nivel representando un diccionario.

```python
# MAL: 'CorrectorOrtografico' (alto nivel) depende de 'Diccionario' (bajo nivel)

# clase bajo nivel
class Diccionario:
    def verificar_palabra(self, palabra):
        pass 

# clase alto nivel 
class CorrectorOrtografico:
    def __init__(self):
        # composicion con una clase de menor nivel
        self.diccionario = Diccionario()

    def corregir_texto(self, texto):
        pass


# Uso de la clase de alto nivel
corrector = CorrectorOrtografico(Diccionario())
```

La solución basada en el principio DIP consiste en crear una clase abstracta que sirva de base para  las clases aplicadas.

```python
from abc import ABC, abstractmethod

# clase abstracta de referencia
class VerificadorOrtografico(ABC):
    @abstractmethod
    def verificar_palabra(self, palabra):
        pass


# TODAS las otras clases se basan en la clase abstracta

# clase bajo nivel
class Diccionario(VerificadorOrtografico):
    def verificar_palabra(self, palabra):
        pass


# clase alto nivel (extra)
class ServicioWeb(VerificadorOrtografico):
    def verificar_palabra(self, palabra):
        pass


# clase alto nivel
class CorrectorOrtografico:
    def __init__(self, verificador: VerificadorOrtografico):
        # agregacion con una clase abstracta
        # el argumento está "moldeado" por una clase abstracta y por ello aceptará a cualquiera de sus clases hijas
        self.verificador = verificador

    def corregir_texto(self, texto):
        pass


# Uso de la clase de alto nivel
corrector = CorrectorOrtografico(Diccionario())
corrector = CorrectorOrtografico(ServicioWeb())
```



### Referencias


**[Soy Dalto - Curso de POO desde Cero (Completo)](https://youtu.be/HtKqSJX7VoM?t=10539)**


