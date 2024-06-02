#Utilizamos una imgane base ligera y especifica en lugar de una imgane pesada y general
FROM python:3.11.9-slim

#Establecemos el direcctorio de trabajo
WORKDIR /app

#Copiamos el archivo requirements
COPY requirements.txt .

#Instalamos las dependencias del proyecto
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt

#Copiamos el resto de los archivos
COPY . .

#Instalamos las dependencias desde las ruedas generadas
RUN pip install --no-cache /app/wheels/*

#Realizamos las migraciones de la base de datos
RUN ["python", "manage.py", "migrate"]

#Recolectamos los archivos estáticos
RUN ["python", "manage.py", "collectstatic", "--no-input"]

#Exponemos el puerto en el que se ejecutará la aplicación
EXPOSE 8000

#Definimos el comando predeterminado para ejecutar la aplicación
CMD ["gunicorn", "--bind", ":8000", "--workers", "2", "vetsoft.wsgi"]