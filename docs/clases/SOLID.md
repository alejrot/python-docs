---
tags:
  - Clases
  - ABC
  - POO
  - UML
---





## 1. SRP - Principio de Responsabilidad Unica
Cada clase debe tener una única responsabilidad o tarea. Si se necesitan varias responsabilidades o tareas éstas deben repartirse en varias clases.

Ejemplo: un programa que simula el funcionamiento de un auto.

- Una clase "Tanque"  que registra el nivel de combustible del auto y gestiona la recarga. 
- una clase  "Auto" que gestiona la posición y el movimiento del mismo consumiendo combustible del tanque.

En este contexto "Tanque" es superclase de "Auto".

Una misma clase puede tener varios metodos pero éstos deben estar asociados a la misma funcionalidad. En el ejemplo: "Tanque" no controla ni la posicion ni el movimiento del auto, en tanto que "Auto" no gestiona la carga de combustible.

(REVISAR)

## 2. OCP - Principio de Abierto/Cerrado
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





## Referencias


**[Soy Dalto - Curso de POO desde Cero (Completo)](https://youtu.be/HtKqSJX7VoM?t=10539)**


