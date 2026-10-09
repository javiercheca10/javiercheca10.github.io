#!/bin/bash
echo "Los archivos del directorio $1 que han sido accedidos en los últimos $2 días son:"
$find $1 -atime $2
if ($2>$3) ; then echo $(($1*$2*$3)) [elif $2<$3; then echo $3-$2] else echo "son iguales"
