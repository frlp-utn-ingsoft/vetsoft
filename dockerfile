#Utilizamos una imgane base ligera y especifica en lugar de una imgane pesada y general
FROM python:3.11.9-slim

#Establecemos el direcctorio de trabajo
WORKDIR /app

#Copiamos el archivo requirements
COPY requirements.txt .

#Instalamos las dependencias del proyecto
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt

FROM python:3.11-slim

WORKDIR /app

COPY --from=builder /app/wheels /wheels
COPY --from=builder /app/requirements.txt .

RUN pip install --no-cache /wheels/*

COPY . .

RUN ["python", "manage.py", "migrate"]
RUN ["python", "manage.py", "collectstatic", "--no-input"]
#Exponemos el puerto en el que se ejutara la aplicacion
EXPOSE 8000

#Definimos el comando predeterminado para ejecutar la aplicacion
CMD ["gunicorn", "--bind", ":8000", "--workers", "2", "vetsoft.wsgi"]