# Vetsoft

Aplicación web para veterinarias utilizada en la cursada 2024 de Ingeniería y Calidad de Software. UTN-FRLP 

## Integrantes del Grupo 

Grupo 13:

- Facundo Larrauri
- Virginia Bruno
- María del Pilar Acosta
- Lucas Martinez

## Dependencias

- python 3
- Django
- sqlite
- playwright
- ruff

## Instalar dependencias

`pip install -r requirements.txt`

## Iniciar la Base de Datos

`python manage.py migrate`

## Iniciar app

`python manage.py runserver`

## Correr el proyecto con docker (vetsoft-app).
```
docker build -t vetsoft-app:1.0.0 .
docker run -e PORT=8000 -d -p8001:8000 --name vetsoft vetsoft-app:1.0.0 
```
Acceder al proyecto desde `localhost:8001`

## Correr el proyecto con docker-compose (vetsoft-app).
1. Crear el archivo .env
2. `docker-compose up -d`

Acceder al proyecto desde `localhost:${LOCAL_PORT}`