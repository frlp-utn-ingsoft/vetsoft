# Usamos la imagen de python, la version 3.12.3-slim. 3.12.3 porque consideramos que es una versión estable, la cual no va a tener conflictos de compatibilidad con las dependencias. Slim porque es una imagen optimizada, ligera, para reducir tiempos de construcción y despliegue.
FROM python:3.12.3-slim

# Establece el directorio de trabajo en /usr/src/app
WORKDIR /usr/src/app

# Copia el archivo de requisitos (requirements.txt) al directorio de trabajo
COPY requirements.txt ./

# Instala las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de la aplicacion al contenedor
COPY . .

# Ejecuta las migraciones de la base de datos antes de iniciar la aplicación
RUN python manage.py migrate

# Exponemos el puerto en el que escucha la aplicación
EXPOSE 80

# Definimos el comando predeterminado para ejecutar la aplicación
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]