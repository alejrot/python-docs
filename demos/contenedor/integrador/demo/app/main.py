"""main.py - Rutina principal - incluye el maquetado de la pagina web"""

# biblioteca estandar
from random import randint

# paquetes
import flet as ft
from faker import Faker

# modulos
from tabla_personas import TablaPersonas
from sql import Persona, engine, Session, select
from logs import info


 # diseño de página
def main(page: ft.Page):
    """Esta función define el diseño de la página web."""

    # generador de datos falsos - personas en español (Argentina)
    fake = Faker(locale="es_AR")

    # evento: carga de nuevos datos
    def nueva_persona(e):
        """Este handler crea los datos de una nueva persona ficticia.
        Luego los guarda en la abse de datos y actualiza la tabla grafica."""
        # generacion de nueva persona
        nombre = fake.name()
        direccion = fake.address()
        edad = randint(13,65)

        # carga en base datos
        with Session(engine) as session:
            # carga de datos - fila a fila
            persona = Persona(
                nombre=nombre,
                direccion=direccion,
                edad=edad,
                )
            session.add(persona)
            # confirmación de cambios
            session.commit()
        # relectura de tablas
        actualizacion_tabla()


    def actualizacion_tabla():
        """Esta funcion lee la tabla desde la base de datos y la carga a la página."""

        # lectura de tabla (completa)
        personas = []
        with Session(engine) as session:
            statement = select(Persona)
            resultados = session.exec(statement)
            data = resultados.all()
            personas = data

        # borrado de filas
        tabla.rows = []
        # creacion de filas - una a una
        for persona in personas:
            info(persona)
            tabla.nueva_persona(persona)

        # actualizacion grafica
        page.update()


    # boton flotante
    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.ADD,
        on_click=nueva_persona,
    )

    # tabla web
    tabla = TablaPersonas()

    # maquetado y estilos
    page.add(
        ft.SafeArea(
            ft.Container(
                tabla,
                alignment=ft.alignment.center,
                expand = True,
            )
        )
    )

    # actualizacion grafica
    actualizacion_tabla()
    page.update()


# objeto renderizable por el server Uvicorn
app = ft.app(main, export_asgi_app=True)
