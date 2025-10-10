"""main.py - Rutina principal - incluye el maquetado de la pagina web"""

# paquetes
from fastapi import FastAPI

# modulos
from sql import leer_todas_personas_db, guardar_persona_db
from persona import nueva_persona

# objeto renderizable por el server Uvicorn
app = FastAPI()


# paths implementados
@app.get("/")
async def root():
    """Un mero mensaje informativo"""
    return {"message": "Backend hecho en FastAPI"}


@app.post("/nuevo")
async def nuevo_usuario():
    """Path elegido para ordenar la creación de un nuevo usuario."""
    persona = nueva_persona()
    datos_nuevos:dict = await guardar_persona_db(persona)
    return datos_nuevos


@app.get("/leer_todos")
async def leer_usuarios():
    """Path elegido para leer los datos de todos los usuarios en la base de datos.
    se devuelven como una lista de diccionarios."""
    lista_todos: list[dict]
    lista_todos = await leer_todas_personas_db()
    return lista_todos
