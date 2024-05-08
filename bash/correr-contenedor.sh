#!/bin/bash

nombre_imagen="vetsoft-app:1.0.0"
nombre_contenedor="vetsoft"

if docker ps -a --format '{{.Names}}' | grep -q "$nombre_contenedor"; then
    echo "El contenedor $nombre_contenedor ya fue creado... corriendo contenedor"
    docker start "$nombre_contenedor" &&
    echo corriendo contenedor $nombre_contenedor ||
    echo Hubo un error al correr el contenedor $nombre_contenedor
else
    if docker image inspect "$nombre_imagen" &> /dev/null; then
        echo "La imagen $nombre_imagen ya existe. No se realizará la construcción."
    else
        echo "Creando imagen para $nombre_imagen!"
        cd ..
        docker build -t "$nombre_imagen" . --no-cache
    fi
    echo "Creando contenedor $nombre_contenedor de la imagen ->  $nombre_imagen..."
    docker run -d -p 8001:8000 --name "$nombre_contenedor" "$nombre_imagen" &&
    echo "Se ha levantado el contenedor"
fi

