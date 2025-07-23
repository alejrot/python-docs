"""sql.py - Módulo dedicado a las consultas a la base de datos"""

# bibliotecas estandar
import os
from typing import Optional

# paquetes
from sqlmodel import Field, Session, SQLModel, create_engine, select

# modulos
from logs import info


# Variables de entorno - necesarias para componer la URL de la base de datos
user = os.getenv("POSTGRES_USER")
password = os.getenv("POSTGRES_PASSWORD")
database = os.getenv("POSTGRES_DB")
dominio = os.getenv("POSTGRES_DOMINIO")

# composicion de la URL dela base de datos
ruta_db = f"postgresql://{user}:{password}@{dominio}:5432/{database}"
info("URL de base de datos: %s", ruta_db)

# creación del conector
engine = create_engine(
    ruta_db,
    # echo=True,
    pool_pre_ping=True,
    )

# Diseño de tabla SQL
class Persona(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    direccion: str
    edad: Optional[int] = None

# creacion de base de datos vacía (sólo si aun no existe)
SQLModel.metadata.create_all(engine)
