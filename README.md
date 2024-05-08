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
- Nicolas Pieroni
- Colavita Emiliano
- Espinosa Tomas
- Stuart Ian

## Convenciones de git
### commits
- STABLE(commit_msg): Version estable/probada de una funcionalidad o de una integración de features.
- ADD(commit_msg): Añade desarrollo a una funcionalidad existente.
- MOD(commit_msg): Modifica el código de una funcionalidad.
- REF(commit_msg): Refactorización de funcionalidad.
- FIX(commit_msg): Corrige un error para una funcionalidad.

### ramas
- MAIN (Rama principal del proyecto)
- NOMBRE_INTEGRANTE (Rama de desarrollo para cada integrante)
- NOMBRE_INTEGRANTE/FUNCIONALIDAD (Rama en opcional en caso de querer separar desarrollo)

### Correr el proyecto dockerizado.
1. Pararse en la carpeta bash de la raiz del proyecto.
2. ejecutar `./correr-contenedor.sh`
3. Esperar para que se cree la imagen y el contenedor vetsoft.
4. Acceder al proyecto desde `localhost:8001`
