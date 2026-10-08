# Tema 2: Arquitectura de un SGBD (ANSI/SPARC, Lenguajes y Formulario/Resumen)

---

## 1. Arquitectura de un SGBD y la Arquitectura ANSI/SPARC

### ¿Por qué utilizar niveles de abstracción?
La arquitectura de los Sistemas de Gestión de Bases de Datos (SGBD) se fundamenta en la separación entre los programas de aplicación y los datos físicos, estructurándose clásicamente en **tres niveles** (según el estándar ANSI/SPARC):

1. **Independencia de datos:** Los usuarios pueden acceder a los mismos datos, pero desde distintas perspectivas.
2. **Flexibilidad organizativa:** La organización física de los datos puede modificarse sin afectar a las aplicaciones ni a la lógica conceptual.
3. **Transparencia física:** Los usuarios no tienen por qué gestionar la representación física, almacenamiento ni optimización de acceso a los datos.

---

### Los Tres Niveles de Abstracción

* **Nivel Interno (o Físico):**
  * *Analogía:* Como observar los huesos y órganos; solo accesible para personal cualificado o administradores del sistema.
  * *Definición:* Representa **cómo están almacenados** físicamente los datos (estructuras de índice, compresión, asignación de bloques en disco).
  
* **Nivel Conceptual (o Lógico):**
  * *Analogía:* Observar a la persona tal y como es con sus facciones globales.
  * *Definición:* Visión global de los datos. Define **qué datos están almacenados** y qué relaciones lógicas hay entre ellos, independientemente de su implementación física.

* **Nivel Externo (o de Vistas):**
  * *Analogía:* Podemos percibir a una persona de distintas maneras según quién la mire.
  * *Definición:* Parte de la Base de Datos que es relevante para cada usuario o aplicación particular. Permite definir múltiples visiones adaptadas a diferentes perfiles de usuario.

---

### Esquema Resumen de los Niveles

| Nivel ANSI/SPARC | Tipo de Visión | Elementos Implicados |
| :--- | :--- | :--- |
| **Nivel Externo** | Visión de Usuario ($\text{Visión}_1, \text{Visión}_2, \dots, \text{Visión}_N$) | Usuarios / Aplicaciones |
| **Nivel Conceptual** | Visión Lógica Global | Esquema Global de la BD |
| **Nivel Interno** | Visión Física Global | Estructuras de Almacenamiento |

---

## 2. Correspondencia (Mapping) entre Niveles

Para que un SGBD mantenga la independencia de datos, debe gestionar las correspondencias o mapeos entre los diferentes niveles de abstracción:

* **Correspondencia Conceptual / Interna:** 
  Define cómo se organizan las entidades lógicas y atributos del esquema conceptual en términos de registros, ficheros y campos del nivel interno.
* **Correspondencia Externa / Conceptual:** 
  Describe un esquema externo en términos del esquema conceptual subyacente. *Nota importante:* No siempre es bidireccional ni siempre es posible de forma automática.
* **Correspondencia Externa / Externas:** 
  Algunos SGBD avanzados permiten derivar esquemas externos a partir de otros esquemas externos ya definidos.

---

## 3. Lenguajes de una Base de Datos: El Sublenguaje de Datos (DSL)

Implementado en el SGBD, el lenguaje de definición y manipulación de datos se divide clásicamente en tres componentes principales:

1. **DDL (Data Definition Language - Lenguaje de Definición de Datos):**
   * Empleado para la definición de estructuras de datos, esquemas y restricciones de integridad.
2. **DML (Data Manipulation Language - Lenguaje de Manipulación de Datos):**
   * Empleado para manipular datos (inserción, borrado, actualización) y consultar esquemas.
3. **DCL (Data Control Language - Lenguaje de Control de Datos):**
   * Empleado para gestionar requisitos de acceso, privilegios de seguridad y administración.

### Consideraciones sobre Lenguajes
* El estándar **ANSI/SPARC** recomienda el uso de un DSL específico para cada nivel.
* **SQL** (*Structured Query Language*) constituye el intento más exitoso de estandarización universal.
* Para el desarrollo de aplicaciones sobre la BD, se emplean lenguajes de **propósito general** (Java, C++, etc.) o lenguajes **específicos embebidos** (PL/SQL en Oracle), combinando el procesamiento de datos con la interfaz de usuario.

### Grado de Acoplamiento
* **Débilmente acoplados:** Lenguajes de propósito general donde el SQL se encuentra embebido (ej. SQL inmerso en C).
* **Fuertemente acoplados:** Lenguajes de propósito específico orientados a un SGBD concreto (ej. PL/SQL de Oracle).

---

## 4. Evolución de los Enfoques de Arquitectura de un SGBD

1. **Inicialmente (Esquema Centralizado):**
   * Toda la carga computacional y de gestión recaía sobre un único servidor central.
   * El usuario accedía mediante terminales tontas.
   * *Problema:* Elevado coste de los servidores y saturación de recursos.
2. **Desplazamiento a PCs (Arquitectura Cliente / Servidor de 2 Capas):**
   * Traslado de parte de la carga a los ordenadores personales de los usuarios.
   * *Ventajas:* Reducción de costes de procesamiento central, terminales con mayor capacidad.
   * *Problema:* Alto coste de mantenimiento del software en los PCs cliente.
   * *Solución:* Separar las aplicaciones en dos capas lógicas:
     * Parte que interactúa con el usuario (Capa de Presentación).
     * Parte de ejecución lógica (Capa de Negocio / Servidor).
3. **Arquitectura Actual (3 Niveles / 3 Capas):**
   * **Nivel de Servidor de Datos:** Distribuido geográficamente. El SGBD permite organizar la información como una BD global unificada, traduciendo peticiones locales a las sedes donde residen los datos reales.
   * **Nivel de Servidor de Aplicaciones:** Evolución de los servidores web que proporcionan la lógica de negocio a clientes ligeros.
   * **Nivel de Cliente:** PCs ligeros o navegadores web. Permiten la ejecución de aplicaciones web con menor dependencia del hardware local y del sistema operativo.

### Ventajas e Inconvenientes de la Arquitectura Actual (3 Capas)
* **Ventajas:**
  * Reducción significativa de los costes de mantenimiento en los clientes.
  * Mayor usabilidad, flexibilidad y escalabilidad para el usuario final.
* **Inconvenientes:**
  * Mayor complejidad en:
    1. La configuración y administración de infraestructuras distribuidas.
    2. El desarrollo y despliegue de aplicaciones multicapa.

---

## 5. El Administrador de la Base de Datos (DBA)

El rol del DBA abarca funciones técnicas críticas de diseño, supervisión y mantenimiento del SGBD:

* Elabora y mantiene el **esquema conceptual**.
* Decide la estructura del **almacenamiento interno** y los métodos de acceso.
* Gestiona la **conexión con los usuarios** y atiende requerimientos de vistas externas.
* Define y aplica las **restricciones de integridad**.
* Define e implanta la **política de seguridad** y control de accesos.
* Define e implanta la **estrategia de recuperación** ante fallos (*backup & recovery*).
* **Optimiza el rendimiento** (*tuning*) del SGBD.
* **Monitoriza** de manera continua el funcionamiento general del sistema.

---

## 📌 Formulario & Chuletario de Resumen

### 1. Correspondencia de Niveles Arquitectura ANSI/SPARC
$$\text{Externo}_i \xrightarrow{\text{Mapeo Ext/Con}} \text{Conceptual} \xrightarrow{\text{Mapeo Con/Int}} \text{Interno}$$

### 2. Clasificación de Lenguajes del SGBD (DSL)
* **DDL:** `CREATE`, `ALTER`, `DROP` $\rightarrow$ Estructuras y Esquemas.
* **DML:** `SELECT`, `INSERT`, `UPDATE`, `DELETE` $\rightarrow$ Instancias y Datos.
* **DCL:** `GRANT`, `REVOKE` $\rightarrow$ Seguridad, Accesos y Privilegios.

### 3. Reglas Mnemotécnicas (Arquitectura 3 Niveles)
* **F**ísico / **I**nterno $\rightarrow$ **C**ómo se almacena (Discos, bloques, índices).
* **C**onceptual $\rightarrow$ **Q**ué datos existen y qué relaciones lógicas hay.
* **E**xterno $\rightarrow$ **P**ara **Q**uien (Vistas personalizadas del usuario).