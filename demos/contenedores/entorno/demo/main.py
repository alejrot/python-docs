import os
import logging

logging.basicConfig(
    level=logging.INFO, # mínimo nivel de log a publicar
    format="%(message)s", #info incorporada
    )

# lectura de variable
valor_variable = os.getenv("VARIABLE_PYTHON")

# reporte de valor
logging.info(f"Valor de 'VARIABLE_PYTHON': '{valor_variable}'")

