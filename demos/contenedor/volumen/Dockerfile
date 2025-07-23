
# imagen de referencia
ARG TAG_IMAGEN=3.13.5-alpine3.22
# ARG TAG_IMAGEN=3.13.5-slim-bookworm
FROM python:${TAG_IMAGEN}
# FROM python:3.13.5-alpine3.22

# directorio de trabajo (se crea automáticamente)
WORKDIR /code

# copia de rutinas al directorio de trabajo
COPY demo/ ./

# comando, opciones y argumentos fijos
ENTRYPOINT ["python", "contar.py"]

# opciones y argumentos sobreescribibles
CMD ["4"]

