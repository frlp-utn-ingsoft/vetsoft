# Vetsoft

Aplicación web para veterinarias utilizada en la cursada 2024 de Ingeniería y Calidad de Software. UTN-FRLP

Nombre de los integrantes:
    - Luciana Danise
    - Renata Victoria Catelli
    - Rocio Belen Tantos
    - Demian Bogado
    - Serrano Mariano Ezequiel

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

## Instrucciones Docker
    - El dockerfile esta creado con la imagen python:3.12-slim como base
    
    - Se agregó al requirements.txt la dependencia dotenv para poder importar los datos vulnerables ocultos en variables de entorno 

    - Al bajar el Dockerfile, agregar los valores de cada quien en la sección de ENV (Esta todo comentado). NO HACER PUSH DEL DOCKERFILE CON LOS VALORES

    - Correr la imagen creada indicando el puerto 8000 (docker run -p 8000:8000 imagen:version)
