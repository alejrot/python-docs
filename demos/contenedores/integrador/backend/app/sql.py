"""sql.py - Módulo dedicado a las consultas a la base de datos"""

# bibliotecas estandar
import os
from pathlib import Path
from typing import Optional

# paquetes
from sqlmodel import Field, SQLModel, create_engine
from sqlmodel import Session, select


# Variables de entorno - necesarias para componer la URL de la base de datos
user = os.getenv("POSTGRES_USER")
database = os.getenv("POSTGRES_DB")
dominio = os.getenv("POSTGRES_DOMINIO")
ruta_password_secreto = os.getenv("POSTGRES_PASSWORD_FILE")


if Path(ruta_password_secreto).is_file():
    with open(ruta_password_secreto, "r",encoding="utf-8") as archivo:
        password = archivo.read()
else:
    password = os.getenv("POSTGRES_PASSWORD")

# composicion de la URL dela base de datos
ruta_db = f"postgresql://{user}:{password}@{dominio}:5432/{database}"


# creación del conector
engine = create_engine(
    ruta_db,
    # echo=True,
    pool_pre_ping=True,
)

# Diseño de tabla SQL
class PersonaSQL(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    direccion: str
    edad: Optional[int] = None


# creacion de base de datos vacía (sólo si aun no existe)
SQLModel.metadata.create_all(engine)


# funciones para peticiones remotas

async def guardar_persona_db(persona: dict)->dict:
    """Esta función guarda los datos de la persona en una base de datos."""
    # carga en base datos
    with Session(engine) as session:
        # carga de datos - fila a fila
        persona = PersonaSQL(
            nombre=persona["nombre"],
            direccion=persona["direccion"],
            edad=persona["edad"],
        )
        session.add(persona)
        # confirmación de cambios
        session.commit()
        return persona

    return None


async def leer_todas_personas_db()->list[dict]:
    """Esta función lee los datos de todas las personas registradas
    y los devuelve como lista de diccionarios. """
    # lectura desde base de datos 
    with Session(engine) as session:
        statement = select(PersonaSQL)
        resultados = session.exec(statement)
        data = resultados.all()
        personas = data
        return personas

    return []