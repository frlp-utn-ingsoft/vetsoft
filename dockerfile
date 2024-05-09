# Utiliza una imagen base ligera y especifica en lugar de una imagen general
FROM python:3.12-slim

# Establece el directorio de trabajo
WORKDIR /usr/src/app

# Copia primero solo el archivo de requisitos para aprovechar el cache de Docker
COPY requirements.txt ./

# Instala las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de la aplicacion al contenedor
COPY . .

# Expone el puerto en el que escucha la aplicacion
EXPOSE 8000

# Define el comando predeterminado para ejecutar la aplicacion
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]