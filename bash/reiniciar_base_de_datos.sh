#!/bin/bash
# Borra la base, reinicia las migraciones y corre los datos aleatorios para pruebas de datos
cd ..;
source ".env";
rm "$DB_NAME" && echo "Se borro la base de datos '$DB_NAME'";
python3 manage.py migrate && echo "se corrieron las migraciones de la base de datos";
python3 manage.py loaddata fixtures/data.json && echo "Se cargaron datos aleatorios";
