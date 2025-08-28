from time import sleep
import sys
import logging


# uso de la consola de logs
logging.basicConfig(
    level=logging.INFO, # mínimo nivel de log a publicar
    format="%(asctime)s - %(levelname)s - %(message)s", #info incorporada
    )

try:
    # el numero maximo a contar se asigna como argumento
    n = int(sys.argv[1])
    logging.info("Contando hasta %i", n)


except Exception:
    # valor máximo por default en caso de error
    logging.warning("Argumento de entrada faltante o incorrecto (debe ser un entero)")
    n = 10
    logging.warning("Contando hasta %i (valor default)", n)

finally:
    # el contador se incrementa cada 1 segundo
    i = 0
    while i <= n:
        logging.info("i: %4i",i)
        sleep(1)
        i += 1

