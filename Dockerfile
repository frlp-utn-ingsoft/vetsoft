# Utiliza una imagen base más liviana
FROM python:slim

# Instala paquetes necesarios para compilar dependencias de Python
RUN apt-get update && \
    apt-get install -y build-essential libffi-dev libssl-dev

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app
COPY . /app/

# Instala las dependencias del proyecto (librerías de Python)
RUN pip install --no-cache-dir --no-cache --disable-pip-version-check -r requirements.txt

# Exponer el puerto
EXPOSE 8000

# Comando para inicializar la aplicación Django
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
