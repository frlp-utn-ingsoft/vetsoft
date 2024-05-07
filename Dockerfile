FROM ubuntu:latest
RUN apt-get update && apt-get install -y python3 python3-pip

WORKDIR /app
COPY . /app/

RUN pip3 install --no-cache-dir --break-system-packages -r requirements.txt

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
