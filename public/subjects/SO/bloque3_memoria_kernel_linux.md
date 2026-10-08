# Tema 3: Gestión de Memoria a Bajo Nivel en Linux y Cachés de Páginas

## 3.4 Gestión de memoria en Linux

Como resumen introductorio, la gestión de memoria en el núcleo Linux abarca tres pilares fundamentales:
1. **Gestión de memoria a bajo nivel**: Asignación de páginas físicas y bloques de memoria en el kernel.
2. **Espacio de direcciones de proceso**: Modelo de memoria virtual, descriptores de memoria (`mm_struct`) y áreas de memoria (`vm_area_struct`).
3. **Caché de páginas y escritura en disco**: Mecanismos de E/S desacoplada, paginación bajo demanda y políticas de desalojo basadas en listas LRU duales.

---

### Gestión de memoria a bajo nivel

* La **página física** es la unidad básica de gestión de memoria en Linux, representada internamente por la estructura `struct page`.
* Una página física puede ser utilizada para diversos fines dentro del ecosistema del kernel:
  * La caché de páginas (*page cache*).
  * Datos privados de controladores o subsistemas.
  * Proyección de la tabla de páginas de un proceso (*page tables*).
  * El espacio de direcciones de un proceso (segmentos de usuario mapeados).
  * Datos del kernel alojados dinámicamente.
  * El código del kernel (*text segment*).
  * Interfaces para asignación de memoria en páginas (y su posterior liberación).

#### Interfaces para la asignación y liberación en páginas

* Las funciones de bajo nivel operan liberando $2^{\text{order}}$ páginas a partir de la estructura de datos que representa la página o de la dirección lógica correspondiente:
  ```c
  void free_pages(unsigned long addr, unsigned int order);
  ```

#### Interfaces para la asignación y liberación de memoria en bytes

* El kernel proporciona funciones similares a `malloc()` y `free()` del espacio de usuario en C, optimizadas para el direccionamiento directo:
  ```c
  void *kmalloc(size_t size, gfp_t flags);
  void kfree(const void *ptr);
  ```

* **Zonas de memoria y modificadores `gfp_t`**: El tipo `gfp_t` (*Get Free Page*) permite especificar el comportamiento y las restricciones de la asignación de memoria mediante tres categorías de *flags*:
  1. **Modificadores de acción**: Indican cómo debe proceder el kernel si no hay memoria disponible (por ejemplo, si puede bloquearse, esperar a E/S o recursar).
  2. **Modificadores de zona**: Indican en qué zona de memoria física debe realizarse la asignación (`ZONE_DMA`, `ZONE_NORMAL`, `ZONE_HIGHMEM`).
  3. **Modificadores más abstractos**: Contextos de llamada de alto nivel.
  * *Ejemplos comunes*: `GFP_KERNEL` (asignación típica en contexto de proceso, puede dormir) y `GFP_USER` (memoria solicitada en nombre de un proceso de usuario).

---

### Cachés de bloques: El subsistema Slab / Slub

#### Organización

* La asignación y liberación frecuente de estructuras de datos (como descriptores de procesos, inodos, buffers de red) es una operación crítica y sumamente común en el kernel de un sistema operativo.
* Para agilizar estas operaciones y evitar la fragmentación externa e interna, Linux utiliza el nivel de bloques conocido como **Slab Layer** (o su evolución moderna **Slub/Slob**).

```
[ Nivel de Bloques: Slab Layer ]
  ├── Actúa como un nivel de caché de estructuras genérico.
  ├── Existe una caché independiente para cada tipo de estructura distinta (ej. "mm_struct_cachep", "inode_cache").
  ├── Cada caché contiene múltiples bloques (slabs) constituidos por una o más páginas físicas contiguas.
  └── Cada bloque aloja múltiples instancias de estructuras del tipo correspondiente a la caché.
```

#### Funcionamiento

* Cada bloque (*slab*) dentro de una caché puede encontrarse en uno de tres estados: **lleno**, **parcial** o **vacío**.
* Cuando el kernel solicita una nueva estructura:
  1. La solicitud se satisface a partir de un **bloque parcial** si existe alguno disponible.
  2. Si no existen bloques parciales, la asignación se satisface a partir de un **bloque vacío**.
  3. Si no existe ningún bloque vacío para el tipo de estructura requerido, se asignan nuevas páginas físicas para crear un nuevo bloque (*slab*).

---

### Espacio de direcciones de proceso

* Se trata del espacio de direcciones virtuales de los procesos ejecutándose en **modo usuario**. Linux hace un uso extensivo de la **memoria virtual (VM)**.
* A cada proceso se le asigna un espacio de direcciones virtuales plano de $32$ o $64$ bits. Dicho espacio puede compartirse de manera controlada entre procesos (por ejemplo, mediante el flag `CLONE_VM` en la llamada al sistema `clone()` para la creación de hebras o *threads*).
* El proceso únicamente tiene permiso para acceder a determinados intervalos de direcciones de memoria, los cuales se denominan **áreas de memoria** (*memory areas* o **VMAs**).

#### ¿Qué puede contener un área de memoria?

Un espacio de direcciones virtuales se compone de múltiples mapas de memoria (*memory maps*):
* La **sección de código** (*text section*): Instrucciones ejecutables del binario mapeadas desde disco.
* La **sección de datos globales inicializados** (*data section*).
* Una proyección de la **página cero** (*zero-page*) para variables globales no inicializadas (*bss section*).
* Una proyección de la **página cero** para la pila (*stack*) del espacio de usuario, permitiendo su crecimiento dinámico bajo demanda.

---

### Descriptores y Estructuras de Control de Memoria

#### El Descriptor de Memoria (`mm_struct`)

El descriptor de memoria representa en el kernel de Linux todo el espacio de direcciones de un proceso. Su definición conceptual en C se modela mediante la estructura:

```c
struct mm_struct {
    struct vm_area_struct *mmap;       // Lista enlazada de áreas de memoria virtual (VMAs)
    rb_root_t mm_rb;                   // Árbol rojo-negro para búsqueda eficiente de VMAs
    pgd_t *pgd;                        // Puntero al Directorio Global de Páginas (tabla de niveles)
    atomic_t mm_users;                 // Contador de usuarios (procesos/hebras) compartiendo este espacio
    atomic_t mm_count;                 // Contador de referencias primarias al descriptor mm_struct
    unsigned long start_code, end_code;// Límites del segmento de código
    unsigned long start_data, end_data;// Límites del segmento de datos
    unsigned long start_brk, brk;      // Límites del *heap* (montículo)
    unsigned long start_stack;         // Dirección base de la pila de usuario
    // ...
};
```

#### ¿Cómo se asigna un descriptor de memoria?
* Mediante la copia del descriptor de memoria durante la ejecución de la llamada al sistema `fork()`.
* Mediante la compartición explícita del descriptor de memoria utilizando el flag `CLONE_VM` en la llamada `clone()`.

#### ¿Cómo se libera un descriptor de memoria?
1. El núcleo decrementa el contador `mm_users` (incluido dentro de `mm_struct`), el cual representa el número de procesos e hilos que usan este espacio de direcciones.
2. Si `mm_users` llega a $0$, se decrementa el contador principal `mm_count`. Si `mm_count` llega a $0$, se procede a liberar definitivamente la estructura `mm_struct` y sus tablas de páginas asociadas de la caché del kernel.

---

### Áreas de Memoria (`vm_area_struct`)

Un área de memoria, representada en el código fuente del kernel por la estructura `struct vm_area_struct`, describe un intervalo contiguo y homogéneo del espacio de direcciones virtuales del proceso.

```c
struct vm_area_struct {
    struct mm_struct *vm_mm;           // Descriptor de memoria propietario de esta VMA
    unsigned long vm_start;            // Dirección virtual de inicio del área
    unsigned long vm_end;              // Dirección virtual de fin del área
    pgprot_t vm_page_prot;             // Permisos de protección de acceso (Lectura, Escritura, Ejecución)
    unsigned long vm_flags;            // Flags de control (VM_READ, VM_WRITE, VM_EXEC, VM_SHARED, etc.)
    struct file *vm_file;              // Fichero asociado en caso de proyecciones mapeadas (mmap)
    // ...
};
```

* **Inspección mediante el sistema de ficheros procfs**: Utilizando el pseudofichero `/proc/<pid>/maps`, es posible inspeccionar en tiempo de ejecución las VMAs activas de cualquier proceso:
  ```bash
  cat /proc/self/maps
  ```
  El formato de cada línea del archivo expone la siguiente traza: 
  $$\text{start-end} \quad \text{permission} \quad \text{offset} \quad \text{major:minor} \quad \text{inode} \quad \text{file}$$

* **Llamadas al sistema para la gestión de VMAs**:
  * `do_mmap()`: Permite expandir una VMA ya existente o crear un nuevo intervalo de direcciones virtuales (área de memoria).
  * `do_munmap()`: Permite eliminar un intervalo de direcciones virtuales del espacio de direcciones del proceso.

---

## 3.5 Traducción de Direcciones Multinivel en Linux

Las direcciones virtuales generadas por la CPU deben convertirse de manera eficiente a direcciones físicas mediante tablas de páginas en memoria. En arquitecturas modernas, Linux implementa un esquema de **paginación multinivel independiente de la arquitectura hardware** estructurado en $3$ niveles lógicos principales:

1. **Más alto nivel**: Directorio global de páginas (**PGD** - *Page Global Directory*), constituido por un array de punteros de tipo `pgd_t`.
2. **Segundo nivel**: Directorio intermedio de páginas (**PMD** - *Page Middle Directory*), constituido por un array de tipo `pmd_t`.
3. **Último nivel**: Tabla de páginas (**PTE** - *Page Table Entry*), que contiene las entradas de mapeo físico final de tipo `pte_t`.

### Esquema Conceptual de Resolución de Direcciones

$$\text{PGD} \xrightarrow{\text{Apunta a}} \text{PMD} \xrightarrow{\text{Apunta a}} \text{PTE} \xrightarrow{\text{Apunta a}} \text{Página Física (\texttt{struct page})}$$

---

### Diagrama de Tablas de Páginas Multinivel en Linux

```text
       Virtual Address
┌────────────────┬────────────────┬────────────┬────────┐
│ Global Directory│ Middle Directory│ Page Table │ Offset │
└────────┬───────┴────────┬───────┴─────┬──────┴────┬───┘
         │                │             │           │
         ▼                ▼             ▼           │
    ┌─────────┐      ┌─────────┐   ┌─────────┐      │
    │  Page   │      │  Page   │   │  Page   │      │
    │Directory│      │ middle  │   │  table  │      │
    │         │      │directory│   │         │      │
    │    ┌───┐│      │   ┌───┐ │   │   ┌───┐ │      │
    │    │ ──┼┼─────►│   │ ──┼─┼──►│   │ ──┼─┼──────┼──┐
    └────┴───┘│      └───┴───┘ │   └───┴───┘ │      │  │
         ▲           ──────────┘   ──────────┘      │  │
         │                                          │  │
     ┌───┴───┐                                      ▼  ▼
     │register│                             ┌─────────────────┐
     └───────┘                              │ Page frame in   │
                                            │ physical memory │
                                            └─────────────────┘
```

---

## 3.6 Caché de Páginas (*Page Cache*) y Desalojo

### Conceptos Fundamentales

* **Definición**: Estructura de datos global en memoria RAM constituida por páginas cuyos contenidos se corresponden directamente con bloques físicos ubicados en almacenamiento secundario (disco).
* El tamaño de la caché de páginas es **dinámico**, expandiéndose o contrayéndose en función de la presión de memoria del sistema operativo.
* El dispositivo o fichero sobre el cual se realiza la técnica de caché de páginas se denomina **almacenamiento de respaldo** (*backing store*).
* **Operaciones**: Soporta operaciones altamente optimizadas de lectura y escritura síncrona/asíncrona de bloques en disco.
* **Fuentes de datos**: Archivos regulares, archivos de dispositivos e imágenes de memoria proyectadas mediante mapeos de archivos (`mmap`).

---

### Desalojo de la Caché de Páginas

El desalojo es el proceso mediante el cual se eliminan datos obsoletos o fríos de la caché de páginas combinando políticas de reemplazo para decidir qué páginas expulsar de la memoria RAM.

1. Linux prioriza la selección y reutilización de **páginas limpias** (*clean pages*, cuyo contenido coincide exactamente con el almacenamiento en disco), ya que pueden sobrescribirse de inmediato sin necesidad de operaciones de E/S adicionales.
2. Si no existen suficientes páginas limpias disponibles, el kernel fuerza un proceso de sincronización y escritura asíncrona a disco (*flusher threads*) para convertir páginas sucias en limpias.
3. Una vez garantizada la disponibilidad, entra en juego la selección de la víctima (*victim selection*).

#### Algoritmo LRU (*Least Recently Used*) y el Sistema Dual de Listas de Linux

* El algoritmo tradicional **LRU** requiere mantener una traza temporal de cuándo se accede por última vez a cada página para seleccionar aquellas con marcas de tiempo más antiguas.
* **Problema del LRU clásico**: Operaciones masivas de lectura de archivos una sola vez (*streaming reads* o respaldos masivos) pueden contaminar la caché expulsando páginas calientes y frecuentemente utilizadas.
* **Solución adoptada por Linux**: Implementación de **dos listas pseudo-LRU independientes**:
  * `active_list`: Contiene las páginas frecuentemente accedidas y consideradas "calientes".
  * `inactive_list`: Contiene las páginas candidatas a ser desalojadas.

```text
┌────────────────────────────────────────────────────────┐
│                      LRU DUAL                          │
│                                                        │
│   ┌────────────────┐          ┌────────────────────┐   │
│   │  active_list   │ ───────> │   inactive_list    │   │
│   │  (Calientes)   │          │ (Frías / Víctimas) │   │
│   └────────────────┘          └─────────┬──────────┘   │
│                                         │              │
│                                         ▼              │
│                           [ Seleccionadas como Víctimas ]│
└────────────────────────────────────────────────────────┘
```

* **Reglas de transición**:
  * **Solo pueden ser seleccionadas como víctimas las páginas residentes en la `inactive_list`**.
  * Una página recién accedida que residía en la `inactive_list` puede ser promovida a la `active_list` tras superar los filtros de re-referenciación del kernel.
  * Este diseño previene de manera robusta que escaneos masivos de ficheros desplacen las páginas de trabajo activas de los procesos en ejecución.