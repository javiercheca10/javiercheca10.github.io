# Prácticas de Shell Scripting y Administración · Fundamentos del Software

**Asignatura:** Fundamentos del Software (FS)  
**Institución:** Universidad de Granada (UGR) · Doble Grado Informática + ADE  
**Autor:** Francisco Javier Checa Casas  
**Entorno:** Bash / GNU/Linux / POSIX Shell  

---

## 1. Introducción al Scripting en Bash

Las prácticas de Fundamentos del Software capacitan en la automatización de tareas en sistemas operativos tipo UNIX mediante intérprete de órdenes **Bash**. Se profundiza en:
* Control de flujo estructurado: bucles `for`, sentencias `if-elif-else`, comprobación de argumentos posicionales (`$#`, `$1`, `$2`).
* Inspección de atributos del sistema de ficheros con `test -d` y `test -f`.
* Redirección de descriptores estándar (stdout `>>`, stdin, pipes).
* Búsqueda avanzada de inodos y metadatos con `find` según marcas temporales (`-atime`, `-mtime`).

---

## 2. Práctica 1: Script de Inspección y Recorrido de Directorios

El script `guion_practica_bash.sh` implementa un flujo interactivo de 4 fases para validar rutas del sistema de archivos, contar elementos por tipo, comprobar paridad numérica y volcar salidas:

```bash
#!/bin/bash

# Validación de parámetros posicionales
if [ $# != 2 ]; then
    echo "Introduce dos argumentos"
    exit
fi

if test -d $1; then
    echo "Bien introducido $1"
else
    echo "$1 no es un directorio válido"
    exit
fi

if test -f $2; then
    echo "Bien introducido $2"
else
    echo "$2 no es un archivo válido"
    exit
fi

for (( CONTADOR=1; CONTADOR<5; CONTADOR++ )); do
    declare -i ARCHIVOS=0;
    declare -i DIRECTORIOS=0;
    declare -i ELEMENTOS=0;
    printf "Estamos en la interacción %d\n" $CONTADOR
    
    # Fase 1: Análisis cuantitativo de ficheros y directorios
    if [ $CONTADOR == 1 ]; then 
        for archivo in $1/*; do
            if test -f $archivo; then 
                let ARCHIVOS=ARCHIVOS+1 
                let ELEMENTOS=ELEMENTOS+1
            fi
            if test -d $archivo; then 
                let DIRECTORIOS=DIRECTORIOS+1 
                let ELEMENTOS=ELEMENTOS+1
            fi
        done
        printf "De un total de %d elementos hay %d archivos y %d subdirectorios\n" $ELEMENTOS $ARCHIVOS $DIRECTORIOS
    fi

    # Fase 2: Control interactivo y evaluación condicional
    if [ $CONTADOR == 2 ]; then
        printf "Introduzca un número: "
        read NUM
        if let $NUM%2==0; then 
            echo "$NUM es par"
        else 
            echo "$NUM es impar"
        fi
    fi

    # Fase 3: Filtrado y concatenación mediante head
    if [ $CONTADOR == 3 ]; then
        head -$NUM $2 >> ./resultado.txt
    fi

    # Fase 4: Terminación
    if [ $CONTADOR == 4 ]; then 
        echo "Se ha finalizado la ejecución del bucle"
    fi
done
```

---

## 3. Práctica 3-4: Búsqueda y Filtrado Temporal

El script `practica3_4_find_atime.sh` automatiza la consulta de archivos accedidos recientemente:

```bash
#!/bin/bash
echo "Los archivos del directorio $1 que han sido accedidos en los últimos $2 días son:"
find $1 -atime $2
```

Permite auditar el uso del sistema de archivos y monitorizar ficheros modificados o accedidos en ventanas temporales específicas mediante el comando nativo `find`.
