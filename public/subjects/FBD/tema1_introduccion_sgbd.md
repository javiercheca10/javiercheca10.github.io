# Tema 1: Introducción a las Bases de Datos y SGBD (con Formulario/Resumen)

---

## 1. Concepto Intuitivo de Base de Datos y Problemas de los Sistemas de Archivos Tradicionales

### 1.1. Dominio y Contexto Inicial
El **dominio** representa el universo del discurso o entorno del mundo real sobre el cual se recopila y gestiona información. 
* *Ejemplo (Entorno Hospitalario):* Médicos, pacientes, historias clínicas, turnos de enfermería, etc.

### 1.2. Problemas del Enfoque Tradicional (Sistemas de Archivos)
Gestionar información directamente mediante sistemas de ficheros o archivos gestionados por el sistema operativo presenta deficiencias críticas que motivan el uso de bases de datos:
1. **Redundancia:** Duplicidad innecesaria de datos almacenados en múltiples ficheros independientes.
2. **Inconsistencia:** Posibilidad de que existan valores contradictorios para el mismo dato en distintas copias, debido a una actualización parcial o incompleta.
3. **No reutilización (Aislamiento de datos):** Datos idénticos deben ser solicitados y gestionados en múltiples sitios (por ejemplo, registrar el alta de un paciente de forma repetida en cada departamento que visita).
4. **Dificultad de gestión con sistemas de archivos clásicos:**
   * Crear archivos con una estructura determinada y rígida.
   * Consultar o actualizar los archivos imponiendo condiciones complejas.
   * Modificar el esquema de los ficheros de forma dinámica sin romper los programas existentes.
   * Proteger los datos frente a accesos no autorizados.
   * Permitir el acceso concurrente y transparente desde cualquier plataforma o software.

---

## 2. Definiciones Fundamentales

### 2.1. Base de Datos (BD)
> **Definición formal:** Conjunto de datos relacionados lógicamente, almacenados de forma integrada y sin redundancia controlada, estructurados para que cualquier programa o usuario autorizado pueda acceder a ellos de manera independiente del lugar físico de almacenamiento y de la aplicación que los utilice.

### 2.2. Sistema Gestor de Bases de Datos (SGBD)
> **Definición formal:** Es un conjunto de software específico que sirve de interfaz entre la Base de Datos, los usuarios y las aplicaciones. Tiene la capacidad de definir, mantener, controlar y utilizar una base de datos de manera eficiente y segura.

**Capacidades principales que debe ofrecer un SGBD:**
* **Definición de estructuras:** Permite especificar los tipos de datos, estructuras y restricciones de integridad.
* **Acceso a los datos:** Facilita la recuperación, inserción, modificación y borrado de información.
* **Control de concurrencia y multiusuario:** Organiza y sincroniza las actualizaciones simultáneas para evitar interferencias o pérdida de datos.

---

## 3. Elementos Involucrados en una Base de Datos y Operaciones CRUD

### 3.1. Elementos Involucrados
1. **Datos:**
   * *Sin redundancia:* Minimizando duplicidades.
   * *Compartidos:* Accesibles de forma integrada por múltiples aplicaciones.
2. **Hardware:**
   * Soporte físico necesario (procesadores, memoria, almacenamiento secundario).
   * Arquitecturas de BD centralizadas, federadas o distribuidas.
3. **Software (SGBD y herramientas):**
   * Programas administradores y herramientas de gestión.
   * Programas de aplicación desarrollados para los usuarios finales.
4. **Usuarios:**
   * **Administrador de la Base de Datos (DBA):** Responsable del control global, seguridad y rendimiento.
   * **Programadores de aplicaciones:** Diseñan software que interactúa con el SGBD mediante lenguajes de consulta (SQL).
   * **Usuario final:** Consulta o manipula los datos a través de interfaces amigables sin necesidad de conocer los detalles internos de almacenamiento.

### 3.2. Operaciones Básicas de un SGBD sobre una BD (CRUD)
* **Insert (Crear / Inserción):** Añadir nuevos registros o tuplas a la base de datos.
* **Read / Select (Leer / Consulta):** Recuperar información almacenada según determinados criterios.
* **Update (Modificar / Actualización):** Cambiar los valores de los datos existentes.
* **Delete (Borrar / Eliminación):** Eliminar registros o entidades que ya no son necesarios.

---

## 4. Concepto de Dato Operativo y Arquitectura de Tres Niveles (Independencia de Datos)

### 4.1. Dato Operativo
Pieza de información básica y elemental que necesita una organización para su normal funcionamiento. Se compone de:
* **Ítem básico:** Elementos elementales sobre los que se solicita información.
* **Atributos:** Características descriptivas de los ítems básicos.
* **Relaciones:** Conexiones lógicas entre los diferentes ítems e entidades.

*A partir del análisis de los datos operativos, se obtiene el esquema lógico global de la organización.*

### 4.2. Independencia de Datos
La independencia de datos garantiza que las aplicaciones estén aisladas de los cambios en la estructura de almacenamiento físico y en la organización lógica de la información.

1. **Independencia Física:** 
   * *Definición:* El diseño lógico de la base de datos es independiente de la forma en que los datos se almacenan físicamente en los dispositivos de disco.
   * *Ventajas:* Permite realizar cambios en las estructuras físicas (índices, organización de ficheros, compresión) sin alterar la lógica de las aplicaciones ni los esquemas conceptuales.
2. **Independencia Lógica:**
   * *Definición:* Capacidad de modificar el esquema conceptual global (añadir nuevas entidades o atributos) sin necesidad de modificar las vistas de usuario existentes o los programas de aplicación.

---

## 5. Arquitectura ANSI/SPARC de Tres Niveles

Para garantizar la independencia de datos, los SGBD modernos implementan una arquitectura estructurada en tres niveles:

| Nivel Arquitectónico | Descripción y Componentes |
| :--- | :--- |
| **1. Nivel Externo (o de Vistas)** | Parte de la BD que resulta relevante para cada usuario o grupo de aplicación específico. Solo muestra aquellas entidades, atributos y relaciones de interés para un rol determinado, ocultando el resto de la base de datos. |
| **2. Nivel Conceptual** | Representa la visión global e integrada de los datos de toda la organización. Contiene **todas** las entidades, atributos, relaciones, restricciones de integridad y semántica de los datos, abstrayéndose por completo de los detalles físicos de almacenamiento. |
| **3. Nivel Interno (o Físico)** | Representa la implantación física de la BD en el ordenador. Describe cómo se almacenan realmente los datos (estructuras de almacenamiento, índices, organización de ficheros en bloques, compresión y cifrado). Busca maximizar el rendimiento de las operaciones. |

---

## 6. Objetivos y Ventajas de usar un SGBD

### 6.1. Objetivos Principales
* Independencia de datos (física y lógica).
* Diseño y utilización orientada al usuario.
* Centralización y control unificado de la información.
* Ausencia de redundancia o control estricto de la misma.
* Garantía de **consistencia**, **integridad**, **fiabilidad** y **seguridad** frente a accesos no autorizados y fallos del sistema.

### 6.2. Ventajas para el Usuario y el Sistema
* **Para el usuario final:** Acceso intuitivo, seguro y rápido a los datos necesarios para su labor.
* **Para el programador:** Abstracción de los detalles de bajo nivel, eliminando problemas complejos de diseño lógico/físico, depuración de errores y mantenimiento del almacenamiento.
* **Para el sistema:** 
  * Control centralizado por parte del DBA.
  * Criterios de uniformidad y estandarización corporativa.
  * Facilidad para la generación ágil de nuevas aplicaciones.
  * Resolución de conflictos ante requerimientos heterogéneos y alta **escalabilidad**.

---

## 📌 Formulario & Chuletario de Resumen

### 1. Resumen de Operaciones CRUD y Mapeo SQL
| Operación CRUD | Equivalente Conceptual | Sentencia SQL Básica |
| :--- | :--- | :--- |
| **C**reate | Inserción de datos | `INSERT INTO Tabla (...) VALUES (...);` |
| **R**ead | Consulta / Recuperación | `SELECT ... FROM Tabla WHERE ...;` |
| **U**pdate | Modificación de tuplas | `UPDATE Tabla SET ... WHERE ...;` |
| **D**elete | Borrado de registros | `DELETE FROM Tabla WHERE ...;` |

### 2. Relación de Niveles de Abstracción ANSI/SPARC
* **Vistas de Usuario (Nivel Externo):** $\text{Vistas } V_1, V_2, \dots, V_n$ orientadas a perfiles específicos.
* **Esquema Conceptual (Nivel Global):** Modelo Entidad-Relación o Relacional Global $\rightarrow$ Define restricciones e integridad semántica.
* **Esquema Interno (Nivel Físico):** Estructuras de ficheros, punteros, tablas Hash y árboles B/B+.

### 3. Propiedades ACID (Garantía de Integridad en Transacciones - Breve Introducción)
* **A (Atomicidad):** O todo se ejecuta (commit) o nada se aplica (rollback).
* **C (Consistencia):** La BD pasa de un estado válido a otro estado válido.
* **I (Aislamiento / Isolation):** Las transacciones concurrentes no interfieren entre sí.
* **D (Durabilidad):** Una vez confirmada una transacción, los cambios persisten ante fallos del sistema.