"""tabla_personas.py - Módulo implementado para diseñar la tabla gráfica."""

# paquetes
from flet import DataTable, DataCell, DataRow, DataColumn
from flet import Text, FontWeight

# modulos
from sql import Persona


class TablaPersonas(DataTable):
    """Tabla custom - con lectura de filas a medida"""

    def __init__(self):
        """Inicializacion de la tabla gráfica."""
        super().__init__(
            width=1200,
            height=700,
            heading_row_height=50,
            column_spacing=20,
            columns=[
                DataColumn(Text("Nombre", weight=FontWeight.BOLD, width=250)),
                DataColumn(Text("Dirección", weight=FontWeight.BOLD, width=500)),
                DataColumn(
                    Text("Edad", weight=FontWeight.BOLD, width=100), numeric=True
                ),
            ],
        )

    def nueva_persona(self, persona: Persona):
        """Agrega una fila a la tabla gráfica con los datos de entrada."""
        fila = DataRow(
            cells=[
                DataCell(Text(persona.nombre, width=250)),
                DataCell(Text(persona.direccion, width=500)),
                DataCell(Text(persona.edad, width=100)),
            ],
        )
        self.rows.append(fila)
        return fila
