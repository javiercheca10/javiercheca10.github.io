# Práctica 4 · Bomba Digital: Ingeniería Inversa & Depuración con GDB
**Asignatura:** Estructura de Computadores (EC)  
**Etapa:** 2º Curso · Doble Grado Ingeniería Informática + ADE (UGR)  
**Autor:** Francisco Javier Checa Casas  
**Documento Fuente:** `guia_practica4_bomba_digital.odt`  

---

## 1. Introducción & Metodología de la "Bomba Digital"
La práctica de la **Bomba Digital (*Binary Bomb*)** es uno de los retos clásicos de ingeniería inversa en arquitectura de computadores:
* **Escenario:** Un ejecutable compilado en C y ensamblador x86 sin símbolos de depuración (`gcc -O2` sin flag `-g`).
* **Objetivo:** Desactivar sucesivamente diversas fases de una "bomba virtual" descubriendo las contraseñas exactas o el formato de datos requerido mediante análisis del código máquina ensamblador.
* **Peligro:** Introducir una entrada incorrecta dispara la función crítica `boom()`, detonando la bomba y penalizando la puntuación del ejercicio.

---

## 2. Comandos Esenciales del Depurador GNU (GDB)

| Comando GDB | Sintaxis | Propósito Operativo |
| :--- | :--- | :--- |
| `file` | `file ./bomba` | Carga el ejecutable binario en el entorno de depuración. |
| `disassemble` | `disas main`, `disas fase1` | Desensambla una función a mnemónicos de ensamblador (sintaxis AT&T o Intel). |
| `break` | `b *0x08048532`, `b boom` | Establece un punto de ruptura en una dirección de memoria o símbolo de función. |
| `run` | `r [argumentos]` | Inicia la ejecución del programa con o sin fichero de entradas. |
| `nexti` / `stepi` | `ni`, `si` | Ejecuta la siguiente instrucción máquina (saltando sobre o dentro de llamadas). |
| `x/s` | `x/s 0x8049010` | Examina la memoria imprimiendo una cadena de caracteres terminada en nulo (`string`). |
| `x/i` | `x/i $pc` | Examina la instrucción que está a punto de ejecutarse en el contador de programa. |
| `info registers` | `i r` | Muestra el contenido hexadecimal y decimal de todos los registros del procesador. |

---

## 3. Estrategias de Desactivación & Análisis de Fases

### 3.1. Neutralización de la Rutina `boom()`
Para evitar detonaciones accidentales durante el análisis:
1. Poner un breakpoint en la primera instrucción de `boom()`:
   ```gdb
   (gdb) break boom
   ```
2. Si el programa salta a `boom`, examinar la pila de llamadas (*stack backtrace*) para ver qué instrucción provocó el salto condicional fallido:
   ```gdb
   (gdb) backtrace
   (gdb) frame 1
   ```

### 3.2. Localización de Comparaciones de Cadenas (`strcmp`)
En muchas fases, la contraseña introducida por el usuario se compara contra una cadena generada o almacenada en la sección de datos:
```assembly
mov    0x804a020, %edx        ; Dirección de la cadena secreta
mov    0x18(%esp), %eax       ; Dirección del buffer del usuario
mov    %edx, 0x4(%esp)
mov    %eax, (%esp)
call   0x8048380 <strcmp@plt> ; Llamada a strcmp
test   %eax, %eax
jne    0x80485d0 <boom>       ; Si eax != 0 (cadenas distintas) -> ¡BOOM!
```
* **Técnica de resolución:** Colocar un breakpoint en la instrucción anterior a `call strcmp` e inspeccionar el contenido de la memoria apuntada por `%edx`:
  ```gdb
  (gdb) x/s 0x804a020
  "clave_secreta_descubierta"
  ```

### 3.3. Estructuras de Datos Complejas & Desbordamientos
En fases avanzadas, el ejecutable evalúa:
* Arrays numéricos mediante sumas de comprobación acumuladas.
* Recorridos de grafos o árboles binarios donde cada nodo es una estructura en memoria con punteros izquierdo/derecho y un entero que debe ordenarse.
* Comprobaciones de longitud de buffer para prevenir desbordamientos de pila (*buffer overflow*).
