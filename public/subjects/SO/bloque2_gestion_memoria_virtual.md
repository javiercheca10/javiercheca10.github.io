# Tema 2: Gestión de Memoria Principal y Memoria Virtual

---

## 3.1 Gestión de Memoria Principal

* **Jerarquía de memoria:**
  $$\text{CPU (registros)} \xrightarrow{\text{Bus de memoria}} \text{Caché} \xrightarrow{\text{Bus de memoria}} \text{Memoria Principal (MP)} \xrightarrow{\text{Bus E/S}} \text{Memoria Auxiliar (MS)}$$

* **Conceptos sobre caché:** Aciertos, fallos, tiempo de acceso efectivo y localidad.
* **Espacio de direcciones lógicas y espacio de direcciones físico.**
* **Mapa de memoria de un proceso:** 
  $$\text{Imagen de un proceso} = \text{mapa} + \text{PCB}$$

* **Objetivos generales de la gestión de la memoria:** Organización, gestión y protección.
  * **Organización:** ¿Cómo se divide la memoria?
  * **Gestión:** Estrategias de asignación (continua y no continua), estrategias de sustitución o reemplazo y estrategias de búsqueda o recuperación.
  * **Protección:** Del SO, de procesos de usuario o procesos usuario entre ellos.

* **Intercambio (*swapping*):** Intercambiar procesos entre memoria y un almacenamiento auxiliar. El intercambiador debe gestionar y asignar el espacio de intercambio.

---

## 3.2 Memoria Virtual: Organización

* **Concepto de Memoria Virtual:** El tamaño del programa, los datos y la pila pueden exceder la cantidad de memoria física disponible para él.
  $$\Rightarrow \text{Almacenamiento en dos niveles: Memoria Principal y Memoria Secundaria}$$
  * Se resuelve el problema de crecimiento dinámico de los procesos.
  * Permite aumentar el grado de multiprogramación.

* **Unidad de Gestión de Memoria (MMU):** Traduce direcciones virtuales a direcciones físicas (gestionado por el SO).

```
  Dirección virtual
  +-----+      +------+
  | CPU | ---> | MMU  | 
  +-----+      +--+---+
                  |   
                  v Bus
              +-------+
              |   MP  |
              +-------+
                  |
         Dirección física
```

* **Esquema MMU simple:**
  * El valor del registro base se añade a cada dirección generada por el proceso usuario al mismo que es enviado a memoria.
  * Los programas usuario solo tratan con direcciones lógicas, nunca reales.
  * La MMU debe detectar si la aludida se encuentra o no en MP y generar una **excepción** si no se encuentra en MP.

---

## 3.3 Paginación

El espacio de direcciones físicas de un proceso puede ser no contiguo.
* La memoria física se divide en bloques de tamaño físico, **marcos de página**, de tamaño potencia de 2.
* El espacio lógico de un proceso se divide en bloques del mismo tamaño, **páginas**.

$$\text{Marcos de páginas} \longrightarrow \text{contienen} \longrightarrow \text{páginas de los procesos}$$

### Direcciones Lógicas y Físicas
* **Direcciones lógicas:** Son las que genera la CPU y se dividen en número de página ($p$) y desplazamiento dentro de la página ($d$).
* **Direcciones físicas:** Se dividen en número de marco ($m$) y desplazamiento ($d$).

Al traducir una dirección lógica a una física, la **tabla de páginas** mantiene la información necesaria para la traducción. Existe una tabla de páginas por proceso.

* **Tabla de ubicación en disco:** (una por proceso), ubicación de cada página en el almacenamiento secundario.
* **Tabla de marcos de página:** Usada por el SO y contiene información sobre cada marco de página.

#### Contenido de la Tabla de Páginas (Una entrada por página del proceso):
1. Número de marco (dirección base del marco) si está en MP.
2. Bit de presencia o válido.
3. Bit de modificación.
4. Modo de acceso autorizado (bits de protección).

---

## Esquema de Traducción (Paginación)

```
[ Nº página | Desplazamiento ] (Dirección virtual)
     |
     v
[ RBTP ] (+) ---> [ Nº marco (m) | Presencia (1) | Modificación | Prot ] (Tabla de páginas)
     |                  |
     |                  +----------------------------+
     |                                               |
     v                                               v
[ Dir. TUD ] (+)                               [ m | Desplazamiento ] (Dirección real)
     |
     v
[ Tabla de Ubicación en Disco ]
```

### Excepciones y Control de Acceso:
* **Presencia = 1:** Se comprueba el acceso autorizado. Si es autorizado y requiere actualizar el bit de modificación, se genera la dirección real con $m$ + Desplazamiento. Si no es autorizado $\rightarrow$ Excepción (violación de privilegios).
* **Presencia = 0:** $\rightarrow$ Falta de página $\rightarrow$ Excepción.

---

## Falta de Página (Pasos de Tratamiento)

1. Bloquear proceso.
2. Encontrar la ubicación en disco de la página solicitada (tabla de ubicación en disco).
3. Encontrar un marco libre. En caso de no haber, se puede desplazar una página de MP.
4. Cargar la página desde el disco al marco de MP.
5. Actualizar tablas (bit presencia, nº marco, ...).
6. Desbloquear el proceso.
7. Reiniciar instrucción que originó la falta de página.

---

## Implementación de la Tabla de Páginas

* La tabla de páginas se mantiene en MP.
* El **Registro Base de la Tabla de Páginas (RBTP)** apunta a la tabla de páginas y suele almacenarse en el PCB del proceso.

### Problemas del esquema:
* Cada acceso a una instrucción o dato requiere dos accesos a memoria: uno a la tabla de páginas y otro a memoria $\rightarrow$ Se resuelve con **TLB (*Buffer* de traducción anticipada)**.
* **Problema:** Tamaño de la tabla de páginas.

---

## Ejemplo de Tamaño de Tabla de Página

* Dirección virtual $= 32\text{ bits}$
* Tamaño de página $= 4\text{ Kbytes } (2^{12}\text{ bytes})$
  * Tamaño del campo desplazamiento $= 12\text{ bits}$
  * Tamaño $n^{\text{o}}$ de página virtual $= 32 - 12 = 20\text{ bits}$
  * $N^{\text{o}}$ de páginas virtuales $= 2^{20} = 1.048.576\text{ páginas}$

---

## Paginación Multinivel

Para reducir el tamaño de la tabla de páginas usaremos paginación multinivel.
* Permite al SO dejar particiones no usadas sin cargar hasta que el proceso las necesita. Aquellas porciones del espacio de direcciones que no se usan no necesitan tener tabla de página.

### Paginación a dos niveles:
* Dividimos la tabla de páginas en partes del tamaño de una página.
* La dirección lógica se divide en:
  * $N^{\text{o}}$ de página ($n$ bits):
    * Un $n^{\text{o}}$ de página $p1 (= k)$
    * Desplazamiento de página $p2 (= n - k)$
  * Desplazamiento de página $d$ ($m$ bits).

$$\begin{array}{|c|c|c|}
\hline
p1 & p2 & d \\
\hline
\end{array}$$

* **Páginas compartidas:** Una copia de código de solo lectura (reentrante) compartido entre varios procesos.

---

## Segmentación

Esquema de organización de memoria que soporta mejor la visión de memoria del usuario: un programa es una colección de unidades lógicas (segmentos).

### Tabla de Segmentos:
* Una dirección lógica es una tupla: $\langle\text{número de segmento}, \text{desplazamiento}\rangle$.
* Aplica direcciones bidimensionales definidas por el usuario en direcciones físicas de una dimensión. Cada entrada de la tabla tiene los siguientes elementos (a parte de presencia, modificación y protección):
  * **Base:** Dirección física donde reside el inicio del segmento en memoria.
  * **Tamaño:** Longitud del segmento.

### Implementación de la Tabla de Segmentos:
* Se mantiene en MP.
* El **Registro Base de la Tabla de Segmentos (RBTS)** apunta a la tabla de segmentos y suele guardarse en el PCB.
* El **Registro Longitud de la Tabla de Segmentos (STLR)** indica el número de segmentos del proceso; el $n^{\text{o}}$ de segmento, generado en una dirección lógica, es legal si $s < \text{STLR}$ (suele guardarse en el PCB).

---

## Esquema de Traducción (Segmentación)

```
[ Nº segmento | d ] (Dirección virtual)
     |        |
     |        +---> [ d > t ] --(Sí)--> Excepción acceso indebido
     |                   | (No)
     v                   v
[ RBTS ] (+) ---> [ D. Base (s') | Tamaño (t) | Presencia (1) | Modificación | Prot ] (Tabla de Segmentos)
     |                   |
     v                   v
[ Dir. TUD ] (+) ---+---> [ s' + d = Dirección real ]
```

---

## Segmentación Paginada

* **Segmentación:** Complica la gestión de MP y MS (Motivos: variabilidad del tamaño de los segmentos y la necesidad de memoria contigua dentro de un segmento).
* **Paginación:** Simplifica gestión pero complica la compartición y la protección.
* **$\Rightarrow$ Segmentación paginada:** Combina ambos enfoques, asumiendo las ventajas de la segmentación y eliminando los problemas de una gestión de memoria compleja.

### Esquema de Traducción (Segmentación Paginada):

```
[ S | P | d' ] (Dirección virtual)
  |   |
  |   +------------------------------------+
  v                                        |
[ RBTS ] (+) ---> [ s' | t ] (Tab. Segmentos)
                  (d <= t)                 v
                     |               [ m | d' ] (Tabla de páginas del segmento)
                     +-----------> (+) ---> [ m | d' ] (Dirección física)
```

---

## 3.3 Memoria Virtual: Gestión

* Criterios de clasificación respecto a:
  * **Políticas de asignación:** Fija o variable (continua o no continua).
  * **Políticas de búsqueda (recuperación):**
    * Paginación por demanda.
    * Paginación anticipada (!= prepaginación).
  * **Políticas de sustitución (reemplazo):**
    * Sustitución global.
    * Sustitución local.

### Criterios de Cumplimiento en Gestión de Memoria Virtual:
* **Páginas limpias frente a sucias:** Se pretende minimizar el coste de transferencia.
* **Páginas compartidas:** Se pretende reducir el $n^{\text{o}}$ de faltas de página.
* **Páginas especiales:** Algunos marcos pueden estar bloqueados.

### Influencia del Tamaño de la Página:
* **Cuanto más pequeñas:**
  * Aumento del tamaño de las tablas de página.
  * Aumento del $n^{\text{o}}$ de transferencia $\text{MP} \rightarrow \text{Disco}$.
  * Reducen la fragmentación interna.
* **Cuanto más grandes:**
  * Grandes cantidades de información que no serán usadas están ocupando MP.
  * Aumentan fragmentación interna.
* **$\Rightarrow$ Busca el equilibrio.**

---

## Algoritmos de Sustitución

* **Posibles combinaciones:** Asignación fija y sustitución local, Asignación variable y sustitución local, Asignación variable y sustitución global.
* **Algoritmos clásicos:** Óptimo, FIFO, LRU y Algoritmo del reloj.
  * **Óptimo:** Sustituye página que no se va a referenciar en un futuro.
  * **FIFO:** Sustituye página más antigua.
  * **LRU:** Sustituye la página que fue objeto de la referencia más antigua.

---

## Algoritmo del Reloj

* Cada página tiene un bit de referencia ($R$).
* Los marcos de página se representan por una lista circular y un puntero a la página visitada hace más tiempo.
* **Selección de una página:**
  1. Consultar marco actual.
  2. ¿Es $R$?
     * **No ($R=0$):** Ir al siguiente marco y volver al paso 1.
     * **Sí ($R=1$):** Seleccionar para sustituir e incrementar posición.

---

## Comportamiento de los Programas y Localidad

* Viene definido por la secuencia de referencias a página que realiza el proceso.
* Importante para maximizar el rendimiento del sistema de memoria virtual.

### Propiedad de Localidad:
* **Temporal:** Posición de memoria referenciada recientemente tiene la posibilidad de ser referenciada en un futuro próximo (bucles, rutinas, variables globales).
* **Espacial:** Si cierta posición de memoria ha sido referenciada es altamente probable que las adyacentes también lo sean (array, ejecución secuencial, ...).

### Conjunto de Trabajo (*Working Set*):
Conjunto de páginas que son referenciadas frecuentemente en un intervalo de tiempo.
$$\text{WS}(t, \tau) = \text{páginas referenciadas en el intervalo de tiempo } t-\tau \text{ y } t$$

---

## Hiperpaginación (*Thrashing*)

Si un proceso no tiene suficientes páginas, la tasa de faltas es alta.
$$\text{Hiperpaginación} = \text{SO ocupado en resolver faltas de página}$$

* **Formas de evitarla:**
  * **Algoritmos de asignación de variables:** Cada proceso tiene asignado un espacio en relación a su comportamiento.
  * **Algoritmos de regulación de carga:** Actúa directamente sobre el grado de multiprogramación.
* **Problemas de la hiperpaginación:**
  * Bajo uso de CPU.
  * SO aumenta multiprogramación.
  * Más falta de páginas.