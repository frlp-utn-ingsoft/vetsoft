# Vetsoft

Aplicación web para veterinarias utilizada en la cursada 2024 de Ingeniería y Calidad de Software. UTN-FRLP

## Dependencias

-   python 3
-   Django
-   sqlite
-   playwright
-   ruff

## Instalar dependencias

`pip install -r requirements.txt`

## Iniciar la Base de Datos

`python manage.py migrate`

## Iniciar app

`python manage.py runserver`

## Integrantes

-   Angel Daniel Marocchi
-   Dalma Florencia Muñoz
-   Tomas Maximiliano Sbert
-   Muñoz Joaquin
-   Llontop Jose

## Ejecutar Proyecto Dockerizado (vetsoft-app1.0)

1. Construir la imagen: docker build -t vetsoft-app:1.0 .
2. Ejecutar imagen: docker run -p 8000:8000 --env-file .env vetsoft-app:1.0
3. Verificar que la imagen se construyo: docker images
4. Modificar el archivo .env-example: cambiar el valor de las variables de entorno propias, luego cambiar el nombre de .env-example a .env
5. Listar los contenedores ejecutados: docker ps
6. Entrar al contenedor ejecutado: docker exec -it id_contenedor /bin/bash
7. Una vez adentro del contenedor ejecuto la migraciones: python manage.py migrate
