#!/bin/bash 

bandera="1"
while [ "$bandera" -eq "1" ]
do
	echo "--- Calculadora ---"
	echo "Selecciona la opción deseada: "
	echo "1. Suma"
	echo "2. Resta"
	echo "3. Multiplicación"
	echo "4. Division"
	echo "5. Salir"
	read opcion
	echo "Valor: $opcion"

	if [ "$opcion" -eq "1" ]
	then
		echo "Ingresa el primer número: "
		read a
		echo "Ingresa el segundo número: "
		read b
		resultado=`expr $a + $b`
		echo "El resultado es: $resultado"
	elif [ "$opcion" -eq "2" ]
	then
		echo "Ingresa el primer número: "
		read a
		echo "Ingresa el segundo número: "
		read b
		resultado=`expr $a - $b`
		echo "El resultado es: $resultado"
	elif [ "$opcion" -eq "3" ]
	then
		echo "Ingresa el primer número: "
		read a
		echo "Ingresa el segundo número: "
		read b
		resultado=`expr $a \* $b`
		echo "El resultado es: $resultado"
	elif [ "$opcion" -eq "4" ]
	then
		echo "Ingresa el primer número: "
		read a
		echo "Ingresa el segundo número: "
		read b
		resultado=`expr $a / $b`
		echo "El resultado es: $resultado"
	else
		bandera=0
	fi
done
