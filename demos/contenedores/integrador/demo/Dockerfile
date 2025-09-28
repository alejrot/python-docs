
# imagen de referencia
ARG VERSION="3.13.5-alpine3.22"
FROM python:${VERSION}

# directorio de trabajo (se crea automáticamente)
WORKDIR /code

# instalación de dependencias
COPY requirements.txt ./
RUN pip install -r requirements.txt --no-cache-dir 

# copia de rutinas al directorio de trabajo
COPY app/ ./

# Puerto expuesto (meramente informativo)
EXPOSE 8000

# comando, opciones y argumentos fijos
ENTRYPOINT ["uvicorn", "main:app", "--port", "8000"]

# opciones y argumentos sobreescribibles
CMD ["--host", "0.0.0.0"]

