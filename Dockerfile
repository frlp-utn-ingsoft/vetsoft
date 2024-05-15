# Usar una imagen base con Python
FROM python:3.12-slim

# Establecer el directorio de trabajo en /app
WORKDIR /app

# Copiar el archivo de requerimientos al directorio de trabajo
COPY requirements.txt .

# Instalar las dependencias de Django
RUN pip install -r requirements.txt

# Copiar el contenido del directorio actual al directorio de trabajo
COPY . .

# Exponer el puerto 8000 para que Django pueda ser accedido
EXPOSE 8000

# Comando para ejecutar el servidor Django
CMD ["python","manage.py","migrate"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
