"""persona.py - Este módulo crea los datos de personas ficticias."""

# bibliotecas estandar
import os
from random import randint

# paquetes
from faker import Faker

# lenguaje y región del registro de personas
lenguaje_region = os.getenv("TAG_LENGUAJE",default="ES_ES")


# generador de datos ficticios
datos_fake = Faker(locale=lenguaje_region)

# crear nueva persona
def nueva_persona()->dict:
    """Esta función crea los datos de una nueva persona ficticia."""
    # generacion de nueva persona
    nombre = datos_fake.name()
    direccion = datos_fake.address()
    edad = randint(13, 65)

    # agrupacion como diccionario
    data_persona = {
        "nombre": nombre ,
        "direccion": direccion,
        "edad": edad
    }

    return data_persona
