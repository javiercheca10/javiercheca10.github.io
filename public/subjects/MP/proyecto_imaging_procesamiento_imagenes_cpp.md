# Proyecto Imaging: Tratamiento Digital de Imágenes en C++

**Asignatura:** Metodología de la Programación (MP)  
**Institución:** Universidad de Granada (UGR) · Doble Grado Informática + ADE  
**Autor:** Francisco Javier Checa Casas  
**Tecnologías:** C++ modular, Punteros & Memoria Dinámica, Formato PGM, Doxygen, Make  

---

## 1. Arquitectura del Proyecto de Software

El proyecto **Imaging** aborda el desarrollo de una biblioteca orientada a objetos en C++ para la manipulación y procesamiento de imágenes digitales en escala de grises bajo formato **PGM** (Portable GrayMap, formato binario `P5` y texto `P2`).

### Módulos Principales:
1. **Módulo Byte (`Byte.h`, `Byte.cpp`):**
   * Abstracción de un píxel de 8 bits ($0 \le \text{valor} \le 255$).
   * Operaciones bit a bit (máscaras, desplazamientos, operadores lógicos `&`, `|`, `^`).
2. **Módulo Histogram (`Histogram.h`, `Histogram.cpp`):**
   * Cálculo de distribución de frecuencias de niveles de gris (256 bins).
   * Ecualización de histograma y umbralización óptima para binarización de imágenes.
3. **Módulo Image (`Image.h`, `Image.cpp`):**
   * Gestión dinámica de matrices bidimensionales continuas en el montículo (*heap*).
   * Constructor de copia profundo (*deep copy*), operador de asignación (`operator=`) y destructor (`~Image`) para prevenir fugas de memoria (*memory leaks*).
   * Filtros morfológicos, convolución espacial, recorte de regiones de interés (ROI) e inspección de metadatos.

---

## 2. Gestión de Memoria Dinámica y Principios de Diseño en C++

El núcleo de la asignatura exige la aplicación rigurosa de las reglas de diseño en C++:
* **Regla de los Tres (Rule of Three):** Al administrar punteros a memoria dinámica para el búfer de píxeles, la clase `Image` implementa explícitamente constructor de copia, operador de asignación y destructor.
* **Separación de Interfaz e Implementación:** Cabeceras (`include/*.h`) estrictamente desacopladas de las implementaciones (`src/*.cpp`).
* **Documentación Doxygen:** Especificación formal de precondiciones (`@pre`), poscondiciones (`@post`), parámetros (`@param`) y valores devueltos (`@return`).

---

## 3. Código Fuente y Repositorio Oficial

El código fuente completo de la biblioteca, la batería de pruebas unitarias y de integración, las imágenes de prueba en formato `.pgm` y el archivo `Makefile` de compilación automatizada se encuentran alojados en el repositorio oficial de GitHub:

* **Repositorio GitHub:** [github.com/javiercheca10/imaging](https://github.com/javiercheca10/imaging)
* `Image.h` & `Image.cpp` · Clase principal de gestión de imagen matricial, segmentación y operaciones espaciales.
* `Histogram.h` & `Histogram.cpp` · Cálculo de frecuencias, mediana de balance y umbralización adaptativa.
* `Byte.h` & `Byte.cpp` · Abstracción de píxel de 8 bits y operaciones a nivel de bit.
* `Makefile` · Script de compilación automatizado (`make`, `make run`, `make clean`).
