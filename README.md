# Vetsoft

Aplicación web para veterinarias utilizada en la cursada 2024 de Ingeniería y Calidad de Software. UTN-FRLP

## Standard commits

- `[type]:<mensaje-commit>`
- `type: fix (arrreglamos bug), feat (agregamos una nueva funcionalidad), refactor (refactorizamos codigo)`

## Instrucciones para dockerizar la aplicación:
Aclaración: Se deberá tener instalado previamente docker en la PC

1. Construir la imagen
    `docker build -t vetsoft .` (-t para nombra "vetsoft" a la imagen, . indica donde buscar el dockerfile)

2. Desplegar el contenedor
    Una vez creada la imagen "vetsoft", ejecutar:
        `docker run -d -p 8000:80 vetsoft` (-d es para que ejecute la aplicación en segundo plano, -p hace el binding de puertos)

3. Ir a la URL localhost:8000 para poder utilizar la aplicación.


## Dependencias y procedimientos de la app, especificados en Dockerfile:
- Dependencias (requeriments.txt)
   python 3.12.3-slim
   Django 5.0.4
   sqlite
   playwright
   ruff
- Instalar dependencias: `pip install -r requirements.txt`
- Iniciar la Base de Datos: `python manage.py migrate`
- Iniciar app: `python manage.py runserver`

## Integrantes

- Peres, Benjamin
- Peres, Valentin
- Eguren, Rafael
- Lezcano, Juan Ignacio
- Milocco, Valentin