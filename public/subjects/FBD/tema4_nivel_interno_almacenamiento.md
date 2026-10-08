# Tema 4: Nivel Interno, Almacenamiento Físico, Índices (Árboles B+) y Hashing

---

## 1. Introducción al Nivel Interno y Almacenamiento Físico

### 1.1. Nivel Interno
* Expresa las operaciones sobre los datos utilizando **unidades mínimas de almacenamiento** (páginas o bloques).
* Permite al administrador **optimizar el almacenamiento y el acceso** a los datos.
* Está implementado directamente en el **SGBD** (Sistema de Gestión de Bases de Datos).

### 1.2. Nivel Físico
* Está implementado en el **sistema operativo** (S.O.).
* Proporciona al SGBD una **capa de abstracción sobre el hardware**.
* Realiza el acceso al almacenamiento secundario mediante **llamadas a servicios del S.O.**

---

## 2. Dispositivos de Almacenamiento

### 2.1. Memoria Principal
* Dispositivo de almacenamiento primario.
* Realiza trabajos de **caché** de uso más reciente.
* **Volátil:** El nivel interno debe mantener un respaldo persistente.
* Es **rápida y costosa**, por lo que se requiere **optimizar su uso**.

### 2.2. Discos Duros (HDD - Los más usados)
* **Estructura física:** Conjunto de discos magnéticos de dos caras. Cada cara tiene pistas, y cada pista se divide en sectores.
* **Localización de un bloque:** `[Cilindro, Superficie (pista), Sector]`
* **Parámetros principales:**
  * **Capacidad**
  * **Tiempo medio de acceso**
  * **RPM** (Revoluciones Por Minuto)
  * **Velocidad sostenida de lectura/escritura**

### 2.3. Medidas de Rendimiento
* **Tiempo medio de acceso ($t_a$):** Tiempo medio entre la petición de una instrucción y la obtención de la información.
* **Tiempo medio de búsqueda ($t_b$):** Tiempo medio de posicionamiento de la cabeza lectora en la pista adecuada.
* **Tiempo de latencia rotacional ($t_l$):** Tiempo medio de posicionamiento del sector bajo la cabeza lectora.
  $$\mathbf{t_a = t_b + t_l}$$
* **Tiempo medio entre fallos (MTBF):** Mide la fiabilidad del dispositivo.

---

## 3. Métodos de Acceso a la Base de Datos Almacenada

Para que el gestor pueda localizar un registro de manera unívoca, se utiliza un identificador único denominado **RID** (*Record Identifier*).

### 3.1. Estructura de un Registro
* **Cabecera:** Contiene metadatos como el número y tipo de las columnas.
* **Datos:** Contiene el contenido efectivo de las columnas.

### 3.2. Consideraciones del Gestor
* Las páginas lógicas de la base de datos deben tener un tamaño múltiplo de las páginas del S.O.
* Para recuperar un registro hay que determinar la página de la BD y los bloques físicos correspondientes.
* Se debe organizar la estructura y el acceso para **minimizar las E/S** (*Entradas/Salidas*) al almacenamiento secundario y optimizar la interacción con los dispositivos.

---

## 4. Gestor de Disco del S.O. y Gestor de Archivos del SGBD

### 4.1. Gestor de Disco del S.O.
* Actúa como intermediario entre el SGBD y la BD almacenada en el almacenamiento secundario.
* Organiza los datos en conjuntos de bloques o archivos del S.O. (una BD puede tener uno o más archivos de este tipo).
* Se encarga de gestionar el espacio libre.
* **Funciones principales:**
  * Crear o eliminar un archivo del S.O.
  * Añadir, eliminar, devolver o reemplazar un bloque ($b$) de un conjunto de bloques ($c$).

### 4.2. Gestor de Archivos del SGBD
* **Transformación:** $\text{Campos, Registros} \xrightarrow{\quad\text{Archivos almacenados}\quad} \text{Bloques, Conjuntos de bloques}$
* Organiza los datos para **minimizar el tiempo de acceso y las E/S a disco**.
* **Funciones principales:**
  * Crear o eliminar un archivo almacenado (asociar/desasociar un archivo a un conjunto de páginas o bloques de la BD).
  * Recuperar un registro ($r$) de un archivo ($a$): El SGBD proporciona el RID $\rightarrow$ Se obtiene la página que contiene el registro.
  * Añadir un registro al archivo:
    1. Localizar la página de la BD más adecuada (si no hay espacio disponible, se solicita una nueva página).
    2. Devolver el RID al SGBD.
  * Eliminar o actualizar un registro:
    1. Recuperar la página que lo contiene.
    2. Marcar el espacio como disponible.
    3. Intentar sustituir, o bien reubicar en otra página si es necesario.

---

## 5. Representación de la BD en el Nivel Interno y Agrupamiento

* La representación en el nivel interno no tiene por qué coincidir con el nivel conceptual; cada conjunto de registros del mismo tipo no tiene por qué almacenarse en un único archivo físico.
* **Agrupamiento (*Clustering*):** La BD es un conjunto de páginas en las que se ubican los registros.
  * **Intra-Archivo (El más frecuente):** En una misma página se almacenan registros del mismo tipo.
  * **Inter-Archivo (Requiere relación previa):** Se ubican en una misma página registros de distinto tipo.
* No existe una relación biunívoca estricta entre fichero almacenado y fichero físico; los conjuntos de páginas se almacenan en uno o varios ficheros físicos del S.O.

---

## 6. Organización y Métodos de Acceso

* **Objetivo:** Minimizar la cantidad de páginas de BD involucradas en una operación.
* **Criterios para medir la calidad de una organización:**
  * Tiempo de acceso.
  * Porcentaje de memoria ocupada por los datos con respecto a las páginas que los contienen.
* **Dos niveles de actuación:**
  1. Organización de registros a nivel de almacenamiento.
  2. Adición de estructuras adicionales para acelerar el acceso (ej. índices).

### 6.1. Organización Secuencial
* Los registros se almacenan consecutivamente en orden físico (para acceder a uno, debemos recorrer los anteriores).
* Suelen estar ordenados por una **clave física**.

#### Algoritmos de Operación sobre Organización Secuencial:
* **Búsqueda secuencial:** En el peor de los caso (no se encuentra o está al final), supone recorrer todos los registros $\rightarrow \mathcal{O}(n)$.
* **Búsqueda por valor o intervalo:** Igual que el caso anterior pero delimitado por una cota inferior y una cota superior.
* **Inserción de un registro:**
  1. Buscar bloque: Si hay sitio disponible, se inserta.
  2. Si no hay sitio, se crea un nuevo bloque o se genera una zona de desbordamiento (*overflow*).
  * *Nota:* Es muy recomendable dejar espacio libre (*fill factor*) entre bloques para evitar reorganizaciones costosas.
* **Borrado de un registro:** Puede implicar una reorganización local de los bloques adyacentes.

---

## 7. Indexación

La indexación disminuye el tiempo de acceso mediante el uso de una clave de búsqueda, de manera similar al índice al final de un libro.

### 7.1. Ficheros Indexados
* Fichero secuencial cuyos registros contienen dos elementos fundamentales:
  * **Campo clave** (clave de búsqueda).
  * **Campo referencia** (RID del registro correspondiente).
* Los ficheros de índices son físicamente más pequeños que los ficheros de datos, aunque contienen el mismo número de referencias.

### 7.2. Tipos de Índices Básicos
* **Índice Primario:** La clave de indexación coincide con la clave física de ordenación del fichero de datos (*Clustering Index*).
* **Índice Secundario:** Construido sobre otros campos que no determinan el orden físico de almacenamiento.

### 7.3. Procesos de Consulta mediante Índices
* **Por un valor específico:**
  1. Buscar en el índice de manera secuencial hasta localizar la clave buscada.
  2. Obtener el RID asociado.
  3. Recuperar el registro directamente en disco mediante dicho RID.
* **Por rango de valores:**
  1. Realizar una búsqueda secuencial en el índice desde la cota inferior hasta la superior.
  2. Recuperar de forma secuencial/directa los registros mediante los RIDs obtenidos.

### 7.4. Índices Densos vs. No Densos
* **Índice Denso:** Existe una entrada en el índice para **cada uno** de los registros almacenados en el fichero de datos.
* **Índice No Denso (Disperso):**
  * Para reducir drásticamente el tamaño del índice, cada entrada se compone únicamente de:
    * Clave de búsqueda representativa.
    * Dirección de comienzo del bloque donde puede encontrarse el registro.
  * El número de entradas se reduce al número total de bloques.
  * **Ventajas e Inconvenientes:**
    * Una vez encontrado el bloque candidato mediante el índice no denso, es obligatorio cargarlo en memoria y realizar una búsqueda secuencial interna.
    * No se tiene garantía absoluta de encontrar el registro hasta examinar todo el bloque.
    * **Los índices no densos solo se pueden definir sobre claves físicas (ordenadas).**
    * El mantenimiento es mucho más económico, ya que solo ocurre cuando una inserción o borrado afecta al valor representativo de la cabecera del bloque.

### 7.5. Índices Jerárquicos y Árboles B+

Cuando los ficheros de índices crecen demasiado, se estructuran en varios niveles (índices sobre índices), dando lugar a los árboles multinivel y, por excelencia en bases de datos relacionales, a los **Árboles B+**.

#### Propiedades Estructurales de un Árbol B+ de Orden $M$ ($M = \text{número máx. de hijos}$):
* Cada nodo interior tiene un máximo de $M$ hijos y un mínimo de $\left\lceil \frac{M}{1} \right\rceil$ o $\lceil M/2 \rceil$ hijos.
* La raíz tiene al menos dos hijos (a menos que sea el único nodo del árbol).
* Todos los nodos hoja se encuentran exactamente en el mismo nivel inferior.
* Las claves de cada nodo actúan como guías para descender al nodo hijo del nivel inmediatamente inferior.
* Un nodo no hoja con $n$ hijos contiene:
  1. $n-1$ valores de clave almacenados ordenados.
  2. $n$ punteros $P_i$ que apuntan a los subárboles hijos.

#### Restricciones de Claves en Nodos:
* Los valores clave $C_i$ de un nodo están estrictamente ordenados: $C_1 < C_2 < \dots < C_{n-1}$.
* Para cualquier valor $X$ almacenado en el subárbol apuntado por el puntero $P_i$:
  * Si $i = 1 \implies X \le C_1$
  * Si $1 < i < n \implies C_{i-1} \le X < C_i$
  * Si $i = n \implies X \ge C_{n-1}$

#### Estructura de los Nodos Hoja:
* Contienen pares `(Clave - RID)`.
* Disponen de punteros explícitos bidireccionales al siguiente nodo hoja (y a veces al anterior) para acelerar las búsquedas por rango sin necesidad de volver a subir por el árbol.
* Todas las claves están ordenadas y los nodos hoja deben estar rellenados al menos hasta la mitad de su capacidad.

---

## 8. Acceso Directo y Hashing

### 8.1. Hashing Estático y Básico
* **Concepto:** No se requiere una estructura de árbol adicional; se utiliza una función matemática determinista (**función de dispersión** o *hash*) que calcula directamente la dirección física de almacenamiento a partir de un campo clave determinado (que debe identificar unívocamente al registro).
* **Funcionamiento:**
  1. Entrada: Campo clave $\rightarrow$ Función Hash $\rightarrow$ Salida: Entero (dirección de bloque o cubo).
* **Tipos de Algoritmos Hash habituales:**
  * Si la clave es alfanumérica, previamente se convierte a numérica.
  * Métodos de generación de números pseudoaleatorios:
    1. Elevación al cuadrado y extracción de dígitos centrales.
    2. División por un número primo $M$ y selección del resto ($h(k) = k \bmod M$).
    3. Superposición de dígitos binarios (plegado) y suma.
    4. Cambio de base numérica.
* **Problemas Principales:**
  * **Colisiones:** Dos claves distintas generan la misma dirección de cubo ($h(k_1) = h(k_2)$).
  * **Huecos:** Aparición de zonas vacías no asignadas que desperdician espacio en disco.
  * **Solución a colisiones:** Uso de listas de desbordamiento (*overflow chains*).

### 8.2. Hashing Dinámico
Para evitar los problemas de capacidad fija y desbordamientos masivos del hashing estático, el hashing dinámico permite que el espacio de almacenamiento crezca y decrezca de manera flexible a medida que se insertan o eliminan registros de la base de datos.
* Se parte de una configuración inicial uniforme con pocos cubos; los restantes se van generando bajo demanda.
* **Técnica:**
  * El valor transformado por la función hash apunta a una **tabla de índices** (directorio).
  * En dicha tabla se almacena la dirección del cubo físico donde se encuentran los registros.
  * Varias entradas de la tabla pueden apuntar al mismo cubo si este todavía no se ha dividido (*split*).
* **Algoritmo de división:**
  * Se gestiona una tabla índice con profundidad global $d$.
  * Cada cubo posee una profundidad local $b \le d$.
  * Cuando un cubo se llena, se divide en dos: los registros se redistribuyen en función del bit $(b+1)$-ésimo (a 0 para un cubo y a 1 para el otro).
  * Si la profundidad local supera la global ($b > d$), es necesario duplicar el tamaño de la tabla índice incrementando la profundidad global en una unidad.

---

## 📌 Formulario & Chuletario de Resumen

| Concepto / Estructura | Fórmula / Relación Clave | Características Principales |
| :--- | :--- | :--- |
| **Tiempo de Acceso a Disco** | $t_a = t_b + t_l$ | $t_b$: Tiempo de búsqueda en pista <br> $t_l$: Latencia rotacional media. |
| **Búsqueda Secuencial** | $\mathcal{O}(n)$ | Recorrido lineal completo. Peor caso absoluto. |
| **Árboles B+ (Nodos Interiores)** | $\text{Máx. Hijos} = M$<br>$\text{Mín. Hijos} = \lceil M/2 \rceil$ | Guías de navegación jerárquica. Contienen $n-1$ claves y $n$ punteros. |
| **Árboles B+ (Nodos Hoja)** | $\text{Mín. Claves} = \lceil (M-1)/2 \rceil$<br>$\text{Máx. Claves} = M-1$ | Pares `(Clave, RID)`. Enlazados horizontalmente para consultas por rango óptimas. |
| **Hashing Estático (Módulo)** | $h(k) = k \bmod M$ | $M$ suele ser un número primo para minimizar colisiones. Requiere gestión de desbordamiento. |
| **Hashing Dinámico** | Profundidad Local ($b$) vs. Global ($d$) | Crecimiento elástico mediante la duplicación de la tabla índice y división de cubos saturados. |