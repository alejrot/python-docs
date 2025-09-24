
# imagen de referencia
FROM python:alpine


# directorio de trabajo (se crea automáticamente)
WORKDIR /code

# copia de rutinas al directorio de trabajo
COPY demo/ ./

# variable de entorno local
ENV VARIABLE_PYTHON="Me definieron en el Dockerfile"

# comandos 
CMD ["python", "main.py"]