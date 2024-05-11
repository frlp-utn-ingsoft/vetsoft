# Vetsoft

Aplicación web para veterinarias utilizada en la cursada 2024 de Ingeniería y Calidad de Software. UTN-FRLP

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

## Integrantes

 - Bifano Ian
 - Pavoni Nicolás
 - Garcia Montes Luciano
 - Rodríguez Luciano Matias

## Levantar proyecto con Docker

1. Verificamos la existencia de la imagen : docker images
2. Construir la imagen : docker build -t vetsoft-app1.0 .
3. Ejecutar la imagen: docker run -d -p 8000:8000 vetsoft-app1.0
4. Verificar el contenedor ejecutado : docker ps
