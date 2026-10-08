# Tema 1: Arquitectura de Computadores y Estructuras del Sistema Operativo

---

## 1. Fundamentos de Arquitectura de Computadores

El sistema operativo actúa como intermediario entre el hardware del sistema de cómputo y las aplicaciones del usuario. Para comprender su funcionamiento interno, es indispensable analizar la organización del hardware subyacente, especialmente la estructura de la CPU, los registros y los mecanismos de transferencia de datos.

### 1.1. Registros del Procesador

Los registros constituyen la memoria de más alto nivel y menor tiempo de acceso en la jerarquía de memoria. Se dividen funcionalmente en dos categorías principales:

#### A. Registros Visibles para el Usuario
Disponibles para todos los programas (tanto de sistema como de usuario). Pueden ser de propósito general o estar dedicados a funciones específicas:

*   **Registro Índice:** Utilizado para el direccionamiento indexado; suma un desplazamiento (*offset*) o índice a un valor base para calcular la dirección efectiva de memoria.
*   **Puntero de Segmento (*Segment Pointer*):** Contiene la dirección base de un segmento de memoria. En arquitecturas segmentadas, la memoria se divide en bloques lógicos de longitud variable.
*   **Puntero de Pila (*Stack Pointer* - SP):** Registro dedicado a almacenar la dirección de memoria de la cima de la pila del sistema (*stack*). Permite la ejecución de instrucciones de manipulación explícita o implícita de pila, tales como `PUSH` (apilar) y `POP` (extraer).

#### B. Registros de Control y Estado
Utilizados exclusivamente por la unidad de control de la CPU y por el sistema operativo (en modo privilegiado o supervisor) para controlar el funcionamiento general del procesador:

*   **Contador de Programa (*Program Counter* - PC):** Almacena la dirección de memoria de la próxima instrucción a ser leída e interpretada.
*   **Registro de Instrucción (*Instruction Register* - IR):** Guarda temporalmente la última instrucción leída desde la memoria principal para su posterior decodificación y ejecución.

```c
/* Representación conceptual en C del contexto de registros de una CPU */
struct cpu_registers {
    /* Registros visibles para el usuario */
    uint32_t general_purpose[8];
    uint32_t index_register;
    uint32_t segment_pointer;
    uint32_t stack_pointer;

    /* Registros de control y estado */
    uint32_t program_counter;      /* PC */
    uint32_t instruction_register;  /* IR */
    uint32_t processor_status_word;/* PSW */
};
```

---

### 1.2. Ejecución de Instrucciones y Ciclo de Instrucción

La función primaria de un procesador es ejecutar las instrucciones almacenadas en la memoria principal. El procesamiento individual de una instrucción constituye el **Ciclo de Instrucción**, el cual se compone formalmente de tres fases secuenciales básicas:

```
+-------------------------------------------------------------------+
|                        CICLO DE INSTRUCCIÓN                       |
|                                                                   |
|   +-------------------+     +-----------------+     +---------+   |
|   | 1. Lectura (Fetch)| --> | 2. Incremento   | --> | 3. Ej.  |   |
|   |    Se lee PC      |     |    del PC       |     |   (Exe) |   |
|   +-------------------+     +-----------------+     +---------+   |
+-------------------------------------------------------------------+
```

1.  **Fase de Lectura (*Fetch*):** El procesador lee la instrucción desde la dirección de memoria apuntada por el Contador de Programa ($PC$) y la carga en el Registro de Instrucción ($IR$).
2.  **Actualización del Contador de Programa:** El $PC$ se incrementa automáticamente para apuntar a la dirección de la siguiente instrucción consecutiva (salvo que ocurra una instrucción de salto o bifurcación).
3.  **Fase de Decodificación y Ejecución (*Execute*):** La CPU interpreta el código de operación (*opcode*) almacenado en el $IR$ y realiza la operación especificada (acceso a memoria, cálculo aritmético/lógico o control de E/S).

---

### 1.3. Mecanismos de Comunicación de Entrada/Salida (E/S)

La interacción entre el procesador y los periféricos de E/S se realiza mediante tres técnicas fundamentales:

#### 1. E/S Programada
El procesador emite una orden de E/S a un módulo especializado y entra en un bucle de espera activa (*busy waiting*), comprobando continuamente el estado del dispositivo hasta que la operación finaliza.
*   **Desventaja:** Ineficiencia extrema; degrada severamente el rendimiento de la CPU al desperdiciar ciclos de reloj comprobando el estado del hardware.

#### 2. E/S Dirigida por Interrupciones
El procesador inicia la operación de E/S y continúa inmediatamente con la ejecución de otras tareas útiles. Cuando el módulo de E/S completa la transferencia, genera una señal física de interrupción hacia la CPU.

**Secuencia de atención a la interrupción:**
1.  El módulo de E/S envía la señal de interrupción al procesador.
2.  El procesador finaliza la instrucción en curso.
3.  Se salva el estado del proceso actual (registros, $PC$, estado del sistema).
4.  La CPU ejecuta la Rutina de Servicio de Interrupción (*Interrupt Service Routine* - ISR) correspondiente.
5.  Se restaura el contexto del proceso interrumpido y se reanuda su ejecución.

#### 3. Acceso Directo a Memoria (*Direct Memory Access* - DMA)
Para transferencias de grandes volúmenes de datos, la E/S dirigida por interrupciones genera una sobrecarga inaceptable en la CPU. El controlador DMA asume el control del bus del sistema para transferir datos directamente entre el dispositivo periférico y la memoria principal sin intervención directa de la CPU.

El procesador configura la transferencia DMA enviando un bloque de parámetros al módulo DMA:
*   **Tipo de operación:** Indicar si se trata de una lectura o una escritura.
*   **Dirección del dispositivo E/S:** Puerto o identificador de hardware del periférico.
*   **Dirección inicial de memoria:** Posición de memoria principal origen/destino de la transferencia.
*   **Contador de palabras:** Número total de palabras/bytes a transferir.

```c
/* Estructura de control de un bloque de transferencia DMA */
struct dma_transfer_descriptor {
    uint8_t  operation_type;   /* 0: Lectura, 1: Escritura */
    uint16_t io_device_id;     /* Dirección del puerto de E/S */
    void    *mem_start_addr;   /* Dirección base en memoria RAM */
    size_t   block_size;       /* Cantidad de palabras/bytes a transferir */
};
```

---

## 2. El Sistema Operativo: Conceptos y Visión Global

Un Sistema Operativo (S.O.) es el programa fundamental que actúa como capa de abstracción entre el hardware físico y el software de aplicación.

### 2.1. Objetivos Principales del Sistema Operativo

1.  **Facilidad de Uso (*Convenience*):** Oculta la complejidad del hardware mediante abstracciones de alto nivel (ficheros, procesos, sockets).
2.  **Eficiencia:** Optimiza la asignación y gestión de los recursos computacionales (CPU, memoria, dispositivos de almacenamiento).
3.  **Capacidad de Evolución:** Debe ser diseñado de manera modular para permitir el desarrollo, prueba e introducción de nuevas funciones del sistema sin interferir con los servicios existentes.

---

### 2.2. Funciones Clave del Sistema Operativo

#### A. Como Interfaz de Usuario / Entorno de Servicio
El S.O. proporciona un entorno estructurado para el desarrollo y ejecución de programas ofreciendo servicios clave:
*   **Desarrollo y ejecución de programas:** Cargadores, enlazadores y controladores del ciclo de vida de los procesos.
*   **Acceso a E/S y al sistema:** Controladores unificados que abstraen las particularidades físicas de cada dispositivo.
*   **Detección y respuesta ante errores:** Gestión de excepciones de hardware, fallos de página, errores de bus y condiciones anómalas de software.

#### B. Como Administrador de Recursos
El S.O. distribuye equitativamente el tiempo de procesador y el espacio de memoria entre los procesos competidores:
*   **Control del Procesador y Temporización:** Planificación de tareas y multiplexación en el tiempo.
*   **Residencia en Memoria:** Una parte fundamental del código del S.O. (el Kernel o Núcleo) debe residir permanentemente en memoria principal física protegida.
*   **Asignación Conjunta de Memoria:** Gestionada coordinadamente por el S.O. (mantenimiento de tablas de páginas/segmentos) y la Unidad de Gestión de Memoria (*Memory Management Unit* - MMU) del hardware.
*   **Arbitraje de E/S:** Garantiza el acceso exclusivo o compartido controlado a los dispositivos periféricos.

---

## 3. Arquitecturas y Estructuras del Sistema Operativo

### 3.1. Criterios de Diseño de una Buena Arquitectura

*   **Eficiencia:** Mínima sobrecarga (*overhead*) en la ejecución de llamadas al sistema (*system calls*) y cambios de contexto.
*   **Fiabilidad y Seguridad:** Capacidad de predecir, aislar y contener errores evitando que un fallo en un componente colapse el sistema completo.
*   **Adaptabilidad:** Facilidad para modificar o añadir nuevos módulos al S.O.

**Tipos de Vista Arquitectónica:**
*   *Arquitectura de Diseño:* Representación conceptual e interrelación de componentes "sobre el papel".
*   *Arquitectura de Ejecución:* Estructura real de cómo los componentes se construyen, compilan y ejecutan dinámicamente en el hardware.

---

### 3.2. Modelos Estructurales del Núcleo

#### 1. Estructura Monolítica
Todos los servicios del S.O. (planificador, gestión de memoria, sistemas de archivos, drivers) se compilan en un único ejecutable binario masivo que corre íntegramente en modo supervisor (protegido).

*   **Ventaja:** Máxima eficiencia y velocidad de comunicación inter-módulo (llamadas a funciones directas en memoria).
*   **Inconveniente:** Difícil de mantener y modificar. Un único fallo en un controlador o módulo en modo supervisor provoca una caída fatal de todo el sistema (*kernel panic* / *BSOD*).

#### 2. Arquitectura por Capas (*Layered Approach*)
El sistema se organiza en una jerarquía de niveles ($N_0, N_1, \dots, N_k$). La capa más baja ($N_0$) interactúa directamente con el hardware y la capa superior ($N_k$) interfaz con el usuario. Cada capa utiliza únicamente los servicios ofrecidos por la capa inmediatamente inferior.

*   **Ventajas:** Diseño modular, ocultamiento de la información y facilidades de depuración y aislamiento de fallos.
*   **Inconvenientes:** Menor eficiencia debido a la penalización por el cruce repetitivo de capas intermedias para completar una operación.

#### 3. Arquitectura Micronúcleo (*Microkernel*) / Cliente-Servidor
Reduce el núcleo a su mínima expresión funcional. El micronúcleo incluye únicamente los servicios esenciales: comunicación interproceso (IPC), gestión básica de memoria y planificación de nivel bajo. Los demás servicios del S.O. (drivers, sistemas de archivos) se ejecutan como procesos de usuario (*servidores*).

```
+-----------------------------------------------------------------+
|                         MODO USUARIO                            |
|  +------------------+    +-------------------+    +-----------+ |
|  | Proceso Cliente  |    | Servidor Ficheros |    | Driver E/S| |
|  +--------+---------+    +---------+---------+    +-----+-----+ |
|           |                        ^                    |       |
|           +----------- IPC --------+--------------------+       |
+--------------------------------|--------------------------------+
|                         MODO SUPERVISOR                         |
|  +-----------------------------------------------------------+  |
|  |                        MICRONÚCLEO                        |  |
|  |     (Planificación Básica, Gestión Memoria, IPC)          |  |
|  +-----------------------------+-----------------------------+  |
+--------------------------------|--------------------------------+
|                            HARDWARE                             |
+-----------------------------------------------------------------+
```

*   **Funciones Principales del Núcleo:**
    *   Proporcionar mecanismos de comunicación eficiente entre clientes y servidores (paso de mensajes).
    *   Garantizar fácil adaptación e integración en sistemas distribuidos.
*   **Ventajas:** Extensibilidad, alta flexibilidad, gran portabilidad y fiabilidad elevada (si falla un servidor de archivos, no se cae el núcleo).
*   **Inconvenientes:** Devaluación del rendimiento global por el consumo elevado de tiempos de cambio de contexto e IPC.

---

### 3.3. Virtualización y Máquinas Virtuales

La virtualización abstrae el hardware físico subyacente creando la ilusión de múltiples computadores independientes. El componente clave es el **Hipervisor** o **Monitor de Máquina Virtual** (*Virtual Machine Monitor* - VMM), el cual crea una capa intermedia entre el SO anfitrión (*Host*) y los SO invitados (*Guest*), gestionando y arbitrando los recursos físicos.

```
       ARQUITECTURA TIPO 1                   ARQUITECTURA TIPO 2
  +---------------------------+         +---------------------------+
  |  SO 1  |  SO 2  |  SO 3   |         |   SO Virtual 1  | SO Virt 2|
  +--------+--------+---------+         +---------------------------+
  |     HIPERVISOR (VMM)      |         |     HIPERVISOR (VMM)      |
  +---------------------------+         +---------------------------+
  |      HARDWARE FÍSICO      |         |        SO ANFITRIÓN       |
  +---------------------------+         +---------------------------+
                                        |      HARDWARE FÍSICO      |
                                        +---------------------------+
```

#### Clasificación de Hipervisores:
*   **Tipo 1 (*Native / Bare-Metal*):** El hipervisor se ejecuta directamente sobre el hardware físico. Ofrece mejor rendimiento y eficiencia.
*   **Tipo 2 (*Hosted*):** El hipervisor se ejecuta sobre un S.O. anfitrión convencional como una aplicación de software.

#### Problemas de la Virtualización:
1.  **Degradación del rendimiento:** Sobrecarga generada por la emulación o traducción de instrucciones privilegiadas y la gestión de tablas de páginas anidadas.
2.  **Aislamiento de red:** Las máquinas virtuales no pueden comunicarse directamente por canal físico sin la configuración explícita de interfaces de red virtuales o conmutadores genéricos (*vSwitches*).

---

## 4. Sistemas Operativos Especializados e Infraestructuras Multiprocesador

### 4.1. Sistemas Operativos de Tiempo Real (STR / RTOS)

Un Sistema Operativo de Tiempo Real debe responder correctamente y reaccionar a eventos externos dentro de un plazo o ventana temporal estrictamente determinada (*deadline*).

*   **Criterio de Diseño:** Prioriza los tiempos mínimos de latencia, acceso y respuesta garantizados sobre la máxima eficiencia o rendimiento medio de los recursos.

#### Tipos de Tareas según la Rigidez del Plazo:
*   **Tiempo Real Duro (*Hard Real-Time*):** El cumplimiento del plazo estipulado es crítico. Un fallo en el plazo provoca un fallo catastrófico del sistema entero.
*   **Tiempo Real Suave (*Soft Real-Time*):** El incumplimiento puntual de un plazo no invalida el resultado; la utilidad de la tarea disminuye progresivamente pero sigue teniendo sentido completarla y planificarla.

#### Clasificación por Periodicidad:
*   **Periódicas:** La tarea se activa y ejecuta secuencialmente a intervalos regulares fijados conocidos ($T$).
*   **Aperiódicas / Esporádicas:** Eventos impredecibles o imprevisibles que tienen un plazo dentro del cual se deben atender una vez desencadenados.

---

### 4.2. Sistemas en Red frente a Sistemas Distribuidos

```
+---------------------------------------------------------------------------+
|                          SISTEMA MULTICOMPUTADOR                          |
|                                                                           |
|  +--------------------+   +--------------------+   +-------------------+  |
|  | Memoria 1          |   | Memoria 2          |   | Memoria 3         |  |
|  +--------------------+   +--------------------+   +-------------------+  |
|  | Procesador 1       |   | Procesador 2       |   | Procesador 3      |  |
|  +---------+----------+   +---------+----------+   +---------+---------+  |
|            ^                        ^                        ^            |
|            +--- Red de conexión / Paso de Mensajes ----------+            |
+---------------------------------------------------------------------------+
```

*   **Sistemas Operativos de Red:** Cada nodo ejecuta de forma independiente su propio S.O. local con sus propios usuarios. Se diferencian de un S.O. tradicional por incorporar software especializado de gestión de red y programas para el acceso remoto a archivos y recursos compartidos.
*   **Sistemas Operativos Distribuidos:** Múltiples computadores independientes se presentan ante los usuarios como un único sistema coherente y centralizado (*transparencia*). Los nodos están débilmente acoplados, no comparten memoria física ni reloj, y basan su coordinación exclusivamente en el paso de mensajes por red.

---

### 4.3. Arquitecturas Multiprocesador y Multiprocesamiento

Sistemas que incorporan más de una Unidad Central de Proceso (CPU) para incrementar la potencia de cálculo.

```
+---------------------------------------------------------------------------+
|                   SISTEMA MULTIPROCESADOR COMPARTIDO                     |
|                                                                           |
|  +---------------+        +---------------+        +---------------+      |
|  | Procesador 1  |        | Procesador 2  |        | Procesador 3  |      |
|  +-------+-------+        +-------+-------+        +-------+-------+      |
|          ^                        ^                        ^              |
|          +------------ Red de Conexión / Bus --------------+              |
|                                   |                                       |
|                  +----------------+----------------+                      |
|                  v                                 v                      |
|          +---------------+                 +---------------+              |
|          |    E / S      |                 | Memoria Princ.|              |
|          +---------------+                 +---------------+              |
+---------------------------------------------------------------------------+
```

#### Paradigmas de Multiprocesamiento:

1.  **Multiprocesamiento Simétrico (*Symmetric Multiprocessing* - SMP):**
    *   Todos los procesadores son idénticos en capacidades y comparten el acceso a la memoria principal y a los dispositivos de E/S a través de un bus común.
    *   Cada procesador ejecuta una copia del S.O. y planifica procesos de manera autónoma.
    *   Ofrece un elevado rendimiento global, equilibrado de carga y tolerancia a fallos.

2.  **Multiprocesamiento Asimétrico (*Asymmetric Multiprocessing* - AMP):**
    *   Existe un procesador "Maestro" (*Master*) y uno o varios procesadores "Esclavos" (*Slaves*).
    *   El procesador maestro ejecuta de manera exclusiva el código del Sistema Operativo, gestiona los recursos y asigna tareas de aplicación a los procesadores esclavos.
    *   Posee una capacidad de escalabilidad sensiblemente menor debido al cuello de botella introducido por la dependencia centralizada en el procesador maestro.

#### Cuadro Comparativo de Arquitecturas Multi-CPU:

| Característica | Multiprocesadores (SMP) | Multicomputadores / Distribuidos |
| :--- | :--- | :--- |
| **Memoria** | Compartida (*Shared Memory*) | Distribuida (*No-Shared Memory*) |
| **Reloj** | Único / Sincronizado | Independiente por nodo |
| **Acoplamiento** | Fuertemente acoplados | Débilmente acoplados |
| **Objetivo Principal** | Aumentar velocidad, rendimiento y confiabilidad | Aprovechamiento eficiente de recursos en red |