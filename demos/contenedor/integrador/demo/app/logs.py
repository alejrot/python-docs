"""logs.py - Módulo usado para configurar los mensajes de log."""

# biblioteca estandar
from logging import basicConfig 
from logging import info, INFO
from logging import debug, DEBUG


# uso de la consola de logs
basicConfig(
    level=INFO,
    format="%(asctime)s - %(levelname)s - %(message)s", #info incorporada
    )
