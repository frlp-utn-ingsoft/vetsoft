# usando la ultima version de ubuntu
FROM ubuntu:latest
# instalando python3 para usar DJango
RUN apt-get update && apt-get install -y python3 python3-pip

# usando el proyecto copiado en la carpeta app
WORKDIR /app
COPY . /app/

# instalo los requirements para el proyecto (librerias de python)
RUN pip3 install --no-cache-dir --break-system-packages -r requirements.txt

# expongo el puerto
EXPOSE 8000

# comando para que el contenedor inicialize la app vetsoft
CMD ["sh", "-c", "python3 manage.py migrate && python3 manage.py runserver 0.0.0.0:8000"]
