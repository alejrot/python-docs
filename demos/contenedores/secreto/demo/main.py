import logging
import os

logging.basicConfig(
    level=logging.INFO, # mínimo nivel de log a publicar
    format="%(message)s", #info incorporada
    )

ruta_secreto = os.getenv("RUTA_SECRETO")

logging.info("Secretos - desde archivo")
logging.info("Ruta interna: '%s'", ruta_secreto)

with open(ruta_secreto, "r",encoding="utf-8") as archivo:
    data = archivo.read()
    logging.info("Valor leído: '%s'", data)
    
logging.info("Finalizado")
