# imagen de referencia
FROM python:alpine

# directorio de trabajo (se crea automáticamente)
WORKDIR /code

# instalación de dependencias
COPY requirements.txt ./
RUN pip install -r requirements.txt --no-cache-dir 

# copia de rutinas al directorio de trabajo
COPY demo/ ./

# puerto de entrada (INFORMATIVO)
EXPOSE 8000

# comando, opciones y argumentos
CMD ["uvicorn", "main:app", "--port", "8000", "--host", "0.0.0.0"]