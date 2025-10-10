"""main.py - Rutina principal - incluye el maquetado de la pagina web"""

# biblioteca estandar
from logging import basicConfig
from logging import info
from logging import INFO
import os

# paquetes
import flet as ft
import requests

# modulos
from tabla_personas import TablaPersonas

# uso de la consola de logs
basicConfig(
    level=INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",  # info incorporada
)

# URLs al backend
servicio_backend = os.getenv("SERVICIO_BACKEND")
puerto_backend   = os.getenv("PUERTO_BACKEND")

URL_CREAR_PERSONA = f"http://{servicio_backend}:{puerto_backend}/nuevo/"
URL_LEER_TODOS    = f"http://{servicio_backend}:{puerto_backend}/leer_todos/"


# diseño de página
def main(page: ft.Page):
    """Esta función define el diseño de la página web."""

    def crear_persona(e):
        """Este handler ordena crear una nueva persona ficticia."""

        # orden al backend para crear nueva persona
        requests.post(URL_CREAR_PERSONA, timeout=5)
        # # relectura de tablas
        actualizacion_tabla()
        info("Nueva persona creada")


    def actualizacion_tabla():
        """Esta funcion lee la tabla desde la base de datos y la carga a la página."""

        # lectura de tabla (completa)
        respuesta = requests.get(URL_LEER_TODOS, timeout=5)
        personas = respuesta.json()

        # borrado de filas
        tabla.rows = []

        # # creacion de filas - una a una
        for persona in personas:
            info(persona)
            tabla.nueva_persona(persona)

        # actualizacion grafica
        page.update()

    # boton flotante
    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.ADD,
        on_click=crear_persona,
    )

    # tabla web
    tabla = TablaPersonas()

    # maquetado y estilos
    page.add(
        ft.SafeArea(
            ft.Container(
                tabla,
                alignment=ft.alignment.center,
                expand=True,
            )
        )
    )

    # actualizacion grafica
    actualizacion_tabla()
    page.update()


# objeto renderizable por el server Uvicorn
app = ft.app(main, export_asgi_app=True)
