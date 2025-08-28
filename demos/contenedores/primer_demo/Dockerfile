# imagen de referencia
FROM python:alpine

# directorio de trabajo (se crea automáticamente)
WORKDIR /code

# copia de rutinas al directorio de trabajo
COPY demo/ ./

# comando, opciones y argumentos fijos
ENTRYPOINT ["python", "contar.py"]

# opciones y argumentos sobreescribibles
CMD ["4"]
