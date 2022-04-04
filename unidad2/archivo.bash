#!/bin/bash

bandera="1"
while [ "$bandera" -eq "1" ]
do
	echo "Manejo de archivos - Parametrizado"
	echo ""
	echo "Selecciona una opción"
	echo "1) Buscar archivos que contengan cierto texto"
	echo "2) Reemplazar el texto de ciertos archivos que contengan cierto texto"
	echo "3) Mostrar archivos filtrados por tamaño"
	echo "4) Salir"
	echo "Elige una opcion: "
	read opcion
	echo "Selección: $opcion"

	if [ "$opcion" -eq "1" ]
	then
		echo "Ingresa el texto a buscar: "
		read textoBusqueda

		sudo grep -lir "$textoBusqueda" ./

		echo ""
	elif [ "$opcion" -eq "2" ]
	then
		echo "Ingresa el texto a buscar"
		read textoBusqueda
		echo "Ingresa el texto a reemplazar"
		read textoReemplazo

		find . -type f -print0 | xargs -0 sed -i "s/$textoBusqueda/$textoReemplazo/g"

		echo ""
	elif [ "$opcion" -eq "3" ]
	then
		echo "Ingresa el tamaño a buscar en Megas(M), bytes(c). Ej. +5M o +5c: "
		read tamanio
		find -type f -size $tamanio
		echo ""
	else
		bandera=0
		echo "Saliendo..."
	fi

done

