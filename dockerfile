#Utilizamos una imgane base ligera y especifica en lugar de una imgane pesada y general
FROM python:3.11.9-slim

#Establecemos el direcctorio de trabajo
WORKDIR /app

#Copiamos el archivo requirements
COPY requirements.txt .

#Instalamos las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

#Copiamos el resto de la aplicacion en el contenedor
COPY . .

#Exponemos el puerto en el que se ejutara la aplicacion
EXPOSE 8000

#Aplicamos las migraciones
RUN python manage.py migrate

#Definimos el comando predeterminado para ejecutar la aplicacion
CMD [ "python", "manage.py", "runserver","0.0.0.0:8000"]