"""sql.py - Módulo dedicado a las consultas a la base de datos"""

# bibliotecas estandar
import os
from pathlib import Path
from typing import Optional
from logging import info

# paquetes
from sqlmodel import Field, SQLModel, create_engine



# Variables de entorno - necesarias para componer la URL de la base de datos
user = os.getenv("POSTGRES_USER")
database = os.getenv("POSTGRES_DB")
dominio = os.getenv("POSTGRES_DOMINIO")
ruta_password_secreto = os.getenv("POSTGRES_PASSWORD_FILE")

# lenguaje y región del registro de personas
lenguaje_region = os.getenv("TAG_LENGUAJE",default="ES_ES")


if Path(ruta_password_secreto).is_file():
    with open(ruta_password_secreto, "r",encoding="utf-8") as archivo:
        password = archivo.read()
        info("Valor leído: '%s'", password)
else:
    password = os.getenv("POSTGRES_PASSWORD")

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
