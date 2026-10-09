#!/bin/bash

if [ $# != 2 ];
	then echo "Introduce dos argumentos"
	exit
fi

if test -d $1 ;
	then echo "Bien introducido $1"
	else echo "$1 no es un directorio válido"
	exit
fi

if test -f $2 ;
	then echo "Bien introducido $2"
	else echo "$2 no es un archivo válido"
	exit
fi

for (( CONTADOR=1; CONTADOR<5; CONTADOR++ )) ; do
	declare -i ARCHIVOS=0;
	declare -i DIRECTORIOS=0;
	declare -i ELEMENTOS=0;
	printf "Estamos en la interacción %d\n" $CONTADOR
	if [ $CONTADOR == 1 ];
	then 
		for archivo in $1/*
		do
			if test -f $archivo; then let ARCHIVOS=ARCHIVOS+1 let ELEMENTOS=ELEMENTOS+1; fi
			if test -d $archivo; then let DIRECTORIOS=DIRECTORIOS+1 let ELEMENTOS=ELEMENTOS+1; fi
		done
		printf "De un total de %d elementos hay %d archivos y %d subdirectorios\n" $ELEMENTOS $ARCHIVOS $DIRECTORIOS
	fi

	if [ $CONTADOR == 2 ];
	then
		printf "Introduzca un número: "
		read NUM
		if let $NUM%2==0; then echo "$NUM es par"; else echo "$NUM es impar"; fi
		
	fi

	if [ $CONTADOR == 3 ];
	then
		head -$NUM $2 >> ./resultado.txt
	fi

	if [ $CONTADOR == 4 ];
	then echo "Se ha finalizado la ejecución del bucle"
	fi
done
