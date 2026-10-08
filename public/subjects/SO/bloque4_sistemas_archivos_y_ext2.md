# Tema 4: Gestión de Archivos, VFS y Estructura Interna de Ext2

---

## 4.1 Interfaz de los Sistemas de Archivos

### Concepto de Archivo
Un archivo se define formalmente como:
$$\text{def} \implies \left\{ \begin{array}{l} \text{Colección de información relacionada y almacenada en un dispositivo de almacenamiento secundario.} \\ \text{Espacio de direcciones lógicas contiguas.} \end{array} \right.$$

#### Estructura Interna (Lógica)
* **Secuencia de bytes:** El tipo de archivo determina su estructura.
  $$\text{Texto} \longrightarrow \text{caracteres, líneas y páginas}$$
  $$\text{Código fuente} \longrightarrow \text{subrutinas, funciones}$$
* **Secuencia de registros de longitud fija.**
* **Secuencia de registros de longitud variable.**

#### Tipos, Accesos y Atributos
* **Tipos de archivos:** Regulares, directorios y de dispositivo.
* **Formas de acceso:** Secuencial, aleatorio (directo), otros.
* **Atributos (Metadatos):** Nombre, tipo, localización, tamaño, protección, tiempo, fecha e identificación del usuario.

#### Operaciones sobre Archivos
* **Gestión:** Crear, borrar, renombrar, copiar, establecer y obtener atributos.
* **Procesamiento:** Abrir y cerrar, leer y escribir (modificar, insertar...).

---

### Estructura de Directorios
* **Organización:** Colección de nodos conteniendo información acerca de todos los archivos.
* **Residencia:** La estructura de directorios y archivos residen en el almacenamiento secundario.
* **Objetivo:** La organización (lógica) de los directorios debe proporcionar **eficiencia**, **denominación** y **agrupación**.

#### Casos de Estructura
* **En Árbol:** Necesidad de búsquedas eficientes, posibilidad de agrupación, directorio actual (de trabajo) y nombres de camino absolutos y relativos.
* **En Grafo:** Compartición de subdirectorios y archivos; más flexible y complejo.

---

### Protección
Consiste en proporcionar un acceso controlado a los archivos: **qué puede hacerse y por quién**.

* **Tipos de acceso:** Leer, escribir, ejecutar, añadir, borrar y listar.

#### Listas y Grupos de Acceso
* **Solución protección:** Acceso dependiente del identificativo del usuario.
  * *Inconveniente:* Las listas de acceso de usuarios individuales tienen el problema de su **longitud**.
* **Solución con clases de usuario:** Propietario, grupo y público.
* **Propuesta alternativa:** Asociar un *password* al archivo.
  * *Problemas:* Recordar todos o, si se usa un único *password*, acceso total o ninguno.

---

### Semánticas de Consistencia
Especifican cuándo las modificaciones de datos por un usuario se observan por otros usuarios.

1. **Semántica de Unix:** La escritura de un archivo es directamente observable. Existe un modo para que los usuarios compartan el puntero actual de posicionamiento de un archivo.
2. **Semántica de Sesión (Sistema de archivos Andrew):** Escritura no observable directamente; cuando se cierra un archivo, sus cambios solo se observan en sesiones posteriores.
3. **Archivos Inmutables:** Cuando un archivo se declara como compartido, no se puede modificar.

---

### Funciones Básicas del Sistema de Archivos
* Tener conocimiento de todos los archivos del sistema.
* Controlar la compartición y forzar la protección de archivos.
* Gestionar el espacio del sistema de archivos: **Asignación / Liberación de espacio disco**.
* Traducir las direcciones lógicas de archivo en direcciones físicas del disco.
  * *Nota:* Los usuarios especifican las partes que quieren leer/escribir en términos de direcciones lógicas relativas al archivo.

---

## 4.2 Diseño Software del Sistema de Archivos

### Problemas de Diseño
1. **Definir cómo debe ver el usuario el sistema de archivos:**
   * Definir un archivo y sus atributos.
   * Definir operaciones permitidas sobre un archivo.
   * Definir la estructura de directorios.
2. **Definir los algoritmos y estructuras de datos** que deben crearse para establecer la correspondencia entre el sistema de archivos lógico y los dispositivos físicos donde se almacenan.

---

### Organización en Niveles (Capas)

```
       [ Programas de aplicación ]
                   │
                   ▼
     [ Sistema lógico de archivos ]
(Maneja estructura de directorio y protección)
                   │
                   ▼
     [ Módulo de organización de archivos ]
   (Conoce archivos, bloques lógicos y físicos)
                   │
                   ▼
     [ Sistema de archivos básico ]
   (Órdenes para leer/escribir bloques físicos)
                   │
                   ▼
  [ Control de E/S (manejadores de dispositivo e interrupción) ]
                   │
                   ▼
            [ Dispositivo ]
```

* **Por eficiencia:** El SO mantiene una tabla indexada (por descriptor de archivo) de archivos abiertos.
* **Bloque de control de archivo:** Estructura con información de un archivo en uso.

---

### Métodos de Asignación de Espacio

#### 1. Contiguo
Cada archivo ocupa un espacio de bloques contiguos en disco.
* **Ventajas:** Sencillo (solo necesita localización de comienzo ($n^\text{o}$ bloque) y tamaño). Bueno tanto en acceso secuencial como directo.
* **Desventajas:** No se conoce universalmente el tamaño. Derroche de espacio (problema de la asignación dinámica $\rightarrow$ **fragmentación externa**). Los archivos no pueden crecer, a no ser que se realice compactación $\rightarrow$ **ineficiente**.

##### Asociación Lógica a Física (Bloques de $512$ bytes)
$$\text{Dirección Lógica (DL)} / 512 \longrightarrow C \text{ (Cociente)}, \ R \text{ (Resto)}$$
* $\text{Bloque a acceder} = C + \text{dirección de comienzo}$
* $\text{Desplazamiento en el bloque} = R$

---

#### 2. No contiguo - Enlazado
Cada archivo es una lista enlazada de bloques de disco. Los bloques pueden estar dispersos en el disco (**punteros**).
* **Ventajas:** Evita la fragmentación externa, el archivo puede crecer dinámicamente cuando hay bloques de disco libres (no es necesario compactar) y basta con almacenar el puntero al primer bloque del archivo.
* **Desventajas:** El acceso directo no es efectivo (sí el secuencial). Espacio requerido para los punteros (solución: agrupaciones de bloques *clusters*) y seguridad para la pérdida de punteros (Solución: lista doblemente enlazada + *overhead*).

##### Asociación Lógica a Física (dirección de $1$ byte)
$$\text{Dirección Lógica (DL)} / 511 \longrightarrow C \text{ (Cociente)}, \ R \text{ (Resto)}$$
* $\text{Bloque a acceder} = C\text{-ésimo}$
* $\text{Desplazamiento en el bloque} = R + 1$

* **Tabla de Asignación de Archivos (FAT):** Variación del método enlazado (Windows y OS/2). 
  $$\text{Localizar bloque} + \text{Leer FAT} \xrightarrow{\quad} \text{Optimiza acceso directo.}$$

---

#### 3. No contiguo - Indexado
Todos los punteros están juntos en una localización concreta: **bloque índice**.
* El directorio tiene la localización a este bloque índice y cada archivo tiene asociado su propio bloque índice.
* Para leer el $i$-ésimo bloque buscamos el puntero en la $i$-ésima entrada del bloque índice.
* **Ventajas:** Buen acceso directo y no produce fragmentación externa.
* **Desventajas:** Posible desperdicio de espacio en los bloques índice.

##### Tamaño del bloque índice. Soluciones:
* Bloques índices enlazados.
* Bloques índices multinivel $\rightarrow$ Tiene el problema de que es necesario el acceso a disco para recuperar la dirección de bloque para cada nivel de indexación. Se soluciona manteniendo algunos índices en M.P.
* Esquema combinado (UNIX).

---

### Gestión del Espacio Libre
El sistema mantiene una lista de los bloques que están libres.
* La FAT no necesita ningún método.
* La lista de espacio libre tiene diferentes implementaciones:
  * **Mapa o vector de bits:** ($0$ - Bloque libre; $1$ - Bloque ocupado).
  * **Lista enlazada:** Puntero al primer bloque (ineficiente $\rightarrow$ Atraviesa bloques vacíos).
  * **Lista enlazada con agrupación:** Cada bloque almacena $n-1$ direcciones libres.
  * **Cuenta:** Cada entrada de lista: una dirección de bloque libre y un contador del $n^\text{o}$ de bloques libres que le sigue.

---

### Implementación de Directorios
#### Contenido de una entrada de directorio. Casos:
* **a) Nombre de Archivo + Atributos + Dirección de los bloques de datos (DOS).**

  | 8 bytes | 3 bytes | 1 byte | 10 bytes | 2 bytes | 2 bytes | 2 bytes | 4 bytes |
  | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
  | Nombre archivo | Tipo archivo / extensión | Atrib | reservado | tiempo | fecha | $n^\text{o}$ primer bloque | tamaño |

* **b) Nombre del Archivo + Puntero a una estructura de datos que contiene toda la información relativa al archivo (UNIX).**

  | 2 bytes | 14 bytes |
  | :--- | :--- |
  | i-nodo | Nombre del archivo |

#### Cuando se abre un archivo:
1. El SO busca en su directorio la entrada correspondiente.
2. Extrae sus atributos y la localización de sus bloques de datos y los coloca en una tabla en **memoria principal**.
3. Cualquier referencia posterior usa la información de dicha tabla.

---

### Implementación de Archivos Compartidos (o Enlace)
1. **Enlaces simbólicos:**
   * Se crea nueva entrada en el directorio, se indica que es de tipo enlace y se almacena el camino de acceso absoluto o relativo del archivo al cual se va a enlazar.
   * Se puede usar en entornos distribuidos.
   * Gran número de accesos a disco.
2. **Enlaces absolutos (o *hard*):**
   * Se crea una nueva entrada en el directorio y se copia la dirección de la estructura de datos con la información del archivo.
   * Problema al borrar los enlaces que se soluciona con el **contador de enlaces**.

---

### Distribución del Sistema de Archivos
* Los sistemas de archivos se almacenan en discos que pueden dividirse en una o más particiones. (En cada partición habrá un sistema de archivos).
* **Formateo del disco:**
  * **Físico:** Pone los sectores (cabecera y código de corrección de errores) por pista.
  * **Lógico:** Escribe la información que el SO necesita para conocer y mantener los contenidos del disco.
* Bloque de arranque para inicializar el sistema localizado por *bootstrap*.
* Métodos para detectar y manejar bloques dañados.

---

### Recuperación
* Como los archivos y directorios se mantienen tanto en MP como en disco, el sistema debe asegurar que un fallo no genere pérdida o inconsistencia de datos.
* **Métodos:**
  1. **Comprobador de consistencia:** Compara los datos de la estructura de directorios con los bloques de datos en disco y trata cualquier inconsistencia. (Más fácil en listas enlazadas que con bloques índices).
  2. Usar programas para realizar copias de seguridad (*backup*) de los datos de disco a otros dispositivos y de recuperación de los archivos perdidos.

---

## 4.3 Implementación de la Gestión de Archivos en Linux

### El i-nodo: Representación interna de un archivo
* Un archivo tiene un único **i-nodo** asociado, aunque este puede tener distintos nombres (enlaces).
* Si un proceso:
  * **Crea un archivo** $\rightarrow$ Se le asocia un i-nodo.
  * **Referencia a un archivo por su nombre** $\rightarrow$ Se analizan los permisos y se lleva el i-nodo a memoria principal hasta que se cierre. (¿Motivo `close()` en C?).

---

### Sistema de Archivos
* SO implementa al menos un sistema de archivos (SA) estándar o nativo.
* En Linux: `ext2`, `ext3` y `ext4`.
* Necesidad de dar soporte a otros SA distintos (`FAT`, `ISO9660`, etc.): el kernel incluye una capa entre los procesos de usuario (o la biblioteca estándar) y la implementación del SA $\rightarrow$ **Sistema de Archivos Virtual (VFS)**.
* Linux abstrae el acceso a los archivos y a los SA mediante una interfaz virtual que lo hace posible.
* Flujo de operaciones/datos por las distintas partes del sistema en una llamada al sistema de escritura (`write`):

```c
   write()        sys_write()       filesystem's write method
┌───────────┐    ┌───────────┐    ┌───────────────────────────┐    ┌────────────────┐
│ user-space│───▶│    VFS    │───▶│         filesystem        │───▶│ physical media │
└───────────┘    └───────────┘    └───────────────────────────┘    └────────────────┘
```

---

### Arquitectura de VFS en Linux

```
                [ Aplicaciones ]
                       │
                       ▼
            [ C-standard library (libc) ]
───────────────────────┴────────────────────── (user space / kernel space)
                       │ System Calls
                       ▼
               [ Virtual Filesystem (VFS) ]
                       │
         ┌─────────────┼─────────────┐
         ▼             ▼             ▼
      [ Ext2 ]      [ Ext3 ]      [ XFS ]
```

---

### Tipos de Sistemas de Archivos
Tres clases generales de SA:
1. **SA basado en disco (*Disk-based filesystems*):** Forma de almacenar archivos en medios no volátiles (básica): `Ext2/3`, `FAT`, `Reiserfs` e `ISO9660`.
2. **SA virtuales (*Virtual Filesystems*):** Generados por el kernel y constituyen una forma simple para permitir la comunicación entre los programas y los usuarios. 
   * *Ej.* `sysfs`. No requieren espacio de almacenamiento en ningún dispositivo hardware (la información está en MP).
3. **SA de red (*Network filesystems*):** Permiten acceder a los datos a través de la red.

---

### Modelo de Archivo Común
* Para un programa de usuario, un archivo se identifica por un **descriptor de archivo** ($n^\text{o}$ entero usado como índice en la tabla de descriptores que identifica el archivo en las operaciones relacionadas con él).
  * El descriptor lo asigna el kernel cuando se abre el archivo y es válido **sólo dentro de un proceso**.
  * Dos procesos pueden usar el mismo descriptor pero no apuntan al mismo archivo.
* Un **i-nodo** es la estructura asociada a cada archivo y directorio, y contiene sus **metadatos**.

---

### Contenido de un i-nodo
```c
struct inode {
    uid_t i_uid;                  // Identificador del propietario del archivo: UID, GID.
    umode_t i_mode;               // Tipo de archivo. Si es 0 el i-nodo está libre.
    struct file_operations *i_op; // Permisos de acceso.
    unsigned long i_atime;        // Tiempos de acceso (modificaciones, acceso y modif. i-nodo).
    unsigned int i_nlink;         // Contador de enlaces.
    // Tabla de contenidos para las direcciones de los datos en disco del archivo
    sector_t i_blocks[EXT2_N_BLOCKS]; 
    loff_t i_size;                // Tamaño.
};
```

---

### Acceso a un Archivo (Ej. `/usr/antonio`)
* Directorio raíz $\rightarrow$ i-nodo correspondiente a `usr` $\rightarrow$ Bloque correspondiente al i-nodo $\rightarrow$ Dentro de `usr` se asigna i-nodo de `antonio`.

---

### Estructura VFS
VFS está orientado a objetos, consta de dos componentes, archivos y SA, que necesita gestionar y abstraer.
Se representa a un archivo y a un SA con una familia de estructuras de datos hechas en C. **$4$ tipos de objetos primarios del VFS:**
* $\rightarrow$ **Objeto `superblock`:** Representa un SA montado.
* $\rightarrow$ **Objeto `inode`:** Representa a un archivo (cualquier tipo).
* $\rightarrow$ **Objeto `dentry`:** Representa a una entrada de un directorio.
* $\rightarrow$ **Objeto `file`:** Representa a un archivo abierto y es una estructura por proceso. Las anteriores son de sistema.

Cada uno de los objetos tiene un vector de `operations`. Estas funciones describen los métodos que el kernel invoca sobre los objetos primarios:
* $\rightarrow$ `super_operations`: `write_inode()` y `sync_fs()`.
* $\rightarrow$ `inode_operations`: `create()` y `link()`.
* $\rightarrow$ `dentry_operations`: `d_compare()` y `d_delete()`.
* $\rightarrow$ `file_operations`: `read()` y `write()`.

* Cada SA registrado está representado por una estructura `file_system_type`. Este objeto describe el SA y sus capacidades.
* Cada punto de montaje está representado por la estructura `vfsmount` que contiene información sobre el punto de montaje, como sus localizaciones y *flags*.
* Finalmente, existen dos estructuras por proceso que describen el SA y los archivos asociados con un proceso: `fs_struct` y `file_struct`.

---

### Información sobre los Bloques de un Archivo
* Linux usa un método de asignación de bloques **no contiguo** y cada bloque de un SA se identifica por un número.
* En el i-nodo se almacenan direcciones directas a un BD, un **primer nivel de indexación**, un **segundo nivel de indexación** y un **tercer nivel de indexación** (si es necesario).

---

### Montaje y Desmontaje de un Sistema de Archivos
* La llamada al sistema `mount` conecta un sistema de archivos al sistema de archivos existente y la llamada `unmount` lo desconecta.

$$\text{mount}(\langle \text{camino\_especial} \rangle, \langle \text{camino\_directorio} \rangle, \langle \text{opciones} \rangle)$$

* El núcleo tiene una **tabla de montaje** con una entrada por cada sistema de archivos montado:
  * $n^\text{o}$ de dispositivo que identifica el SA montado.
  * Puntero a un *buffer* que contiene una copia del superbloque.
  * Puntero al i-nodo raíz del SA montado.
  * Puntero al i-nodo del directorio punto de montaje.

---

## 4.4 Sistema de Archivos Ext2

* Divide el disco duro en un conjunto de bloques de igual tamaño donde se almacenarán los datos de los archivos y de administración.
* El elemento central de Ext2 es el **"grupo de bloques"** (*block group*).
* Cada SA consta de un gran número de bloques secuenciales.
* **Boot sector (Boot block):** Zona de disco cuyo contenido se carga automáticamente por la Bios y se ejecuta cuando el sistema arranca.
* Cuando se usa un SA (se monta), el bloque (*superblock*) y sus datos, se almacenan en MP.

---

### Descripción de un Grupo de Bloques ($4$ estructuras *"struct"*)
* **Superbloque (`Superblock`):** Estructura central para almacenar meta-información del SA (`struct ext2_super_block`).
* **Descriptores de grupo (`Group descriptors`):** Contienen información que refleja el estado de los grupos de bloques individuales del SA. $N^\text{o}$ bloques libres e i-nodos libres (`struct ext2_group_desc`).
* **Mapa de bits de bloques de datos y de i-nodos (`Data bitmap, Inode bitmap`):** Contienen un bit por bloque de datos y por i-nodo respectivamente para indicar si están libres o no (`struct ext2_inode`).
* **Tabla de i-nodos (`Inode Tables`):** Contiene todos los i-nodos del grupo de bloques. Cada i-nodo mantiene los metadatos asociados con un archivo o directorio del SA (`struct ext2_dir_entry_2`).