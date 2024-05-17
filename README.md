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
5. Ingresar a la app desde un navegador: http://localhost:8000

## Convención de Nomenclatura para Branches
| Branch | Descripción |
| ------------- | ------------- |
| master/main  | La rama principal del proyecto, donde se encuentra el código estable y listo para producción.  |
| develop/dev  | La rama de desarrollo principal, donde se fusionan todas las características antes de ser enviadas a producción.  |
| feature/[nombre-descriptivo] | Para nuevas características o funcionalidades. Ejemplo: feature/login-page.  |
| bugfix/[nombre-bug]  | Para solucionar errores o bugs. Ejemplo: bugfix/fix-navigation-bug. |
| hotfix/[nombre-bug] | Para correcciones rápidas de errores en producción. Ejemplo: hotfix/fix-security-issue. |

## Convención de Nomenclatura para Commits

| Commit | Descripción |
| ------------- | ------------- |
| feat | Para nuevas características o funcionalidades. |
| fix | Para correcciones de errores. |
| refactor | Para cambios en el código que no afectan el comportamiento externo pero mejoran la estructura o legibilidad. |
| docs | Para cambios en la documentación. |
| style | Para cambios que no afectan el comportamiento del código (espacios en blanco, formato, etc.). |
| chores | Para tareas de mantenimiento o tareas no relacionadas con el código (como cambios en configuraciones). |
| test | Para adiciones o modificaciones en pruebas. |
