#Se pasa versión de docker como argumento#
ARG DOCKERFILE_VERSION=1.0

#Se importa imagen de python como base de container, 
#ya que una imagen siempre parte de otra imagen ya creada#
#En este caso, se opta por python-slim para minimizar tamañño de imagen#
FROM python:3.12-slim

#Variable de entorno configurada para evitar que se generen archivos .pyc y .pyo 
#(archivos compilados de phyton)#
ENV PYTHONDONTWRITEBYTECODE 1

#Variable de entorno para indicar a Docker que nos muestre el Standard Output (salida) 
#y Standard Error(errores) en la terminal como estamos acostumbrados.
ENV PYTHONUNBUFFERED 1

#Directorio donde se creará la app en el docker#
WORKDIR /app

#Tomar archivo requeriments.txt de máquina local a contenedor para tener dependencias#
COPY requirements.txt /app/

#Ejecuta línea de python para instalar dependencias necesarias de vetsoft#
RUN pip install --no-cache-dir -r requirements.txt

#Copia resto de código fuente de vetsoft al contenedor#
COPY . /app/

#Líneas de comando a ejectuar al levantar el contenedor#
#Se corren líneas de comando en la shell para
#1. Hacer migraciones necesarias
#2. Correr el server en el puerto indicado en variables de entorno: env-example#
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:${PORT}"]