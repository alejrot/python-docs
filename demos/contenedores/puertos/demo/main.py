# importación
import flet as ft


# Diseño de página y eventos
def main(page: ft.Page):

    #contador: barra de texto
    counter = ft.Text("0", size=50, data=0)

    # evento: contar cuando se clickea el botón
    def increment_click(e):
        counter.data += 1
        counter.value = str(counter.data)
        counter.update()

    # botón flotante
    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.ADD, on_click=increment_click
    )

    # maquetado de página
    page.add(
        ft.SafeArea(
            ft.Container(
                counter,
                alignment=ft.alignment.center,
            ),
            expand=True,
        )
    )

# objeto desplegable con Uvicorn
app = ft.app(main, export_asgi_app=True)