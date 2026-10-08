# Backtracking (Búsqueda con Retroceso) y Restricciones

## Conceptos Fundamentales

### Supuestos de Partida
El uso del esquema de diseño *Backtracking* se fundamenta en los siguientes supuestos:

* **a)** No disponemos de información suficiente para elegir de manera directa o inmediata entre un conjunto de decisiones posibles.
* **b)** Cada decisión individual nos conduce a un nuevo conjunto de soluciones (o subproblemas).
* **c)** Alguna sucesión particular de decisiones puede constituir una solución válida al problema.

---

### Representación de la Solución
La solución al problema debe poder expresarse formalmente como una $n$-tupla de la forma:

$$(x_1, x_2, \dots, x_n)$$

donde cada componente $x_i$ se elige a partir de un conjunto finito $S_i$ (es decir, $x_i \in S_i$).

---

### Filosofía del Algoritmo
* **Construcción incremental:** La idea central consiste en construir el vector solución componente a componente, seleccionando un elemento a la vez.
* **Funciones criterio:** Se utilizan funciones criterio para evaluar si el vector parcial en proceso de construcción tiene posibilidades reales de éxito.
* **Espacio de búsqueda:** Se realiza una búsqueda sistemática sobre grafos dirigidos y acíclicos (estructuras en forma de árbol de expansión) mediante un **recorrido en profundidad** (DFS - *Depth-First Search*).
* **Poda (*Pruning*):** Se realiza un descarte o poda de aquellas ramas del árbol de decisión que se consideren poco prometedoras, evitando así explorar caminos inviables de manera redundante.

---

## Resolución de Problemas

Para abordar y estructurar la resolución de un problema mediante *Backtracking*, se deben definir con precisión los siguientes elementos:

1. **Descripción del problema:** Definición formal del escenario y los datos de entrada.
2. **Restricción:** Condiciones y límites que deben cumplir los elementos constitutivos de la solución.
3. **Objetivo:** Definición matemática de lo que constituye una solución válida o una solución óptima.

### Comportamiento Dinámico del Proceso de Decisión
* No disponemos de suficiente información de forma local para asegurar la elección correcta en cada paso.
* Cada elección realizada nos traslada a otro conjunto de elecciones secundarias.
* Una determinada sucesión de elecciones nos puede guiar o no hacia la consecución de una solución final.

---

## Tipos de Restricciones

El espacio de búsqueda se ve acotado por dos tipos fundamentales de restricciones que guían el proceso de backtracking:

### 1. Restricciones Explícitas
* Son condiciones dadas directamente por el enunciado del problema que restringen el dominio o rango de valores individuales que puede tomar cada variable.
  
  $$\text{Ejemplos: } x_i \ge 0, \quad x_i \in \{0, 1\}$$

* **Espacio de soluciones:** El conjunto de todas las tuplas que satisfacen únicamente este tipo de restricciones explícitas define formalmente el **espacio de soluciones** (o espacio de búsqueda inicial).

### 2. Restricciones Implícitas
* Determinan cuál de las tuplas pertenecientes al espacio de soluciones satisface la función de criterio del problema. Describen la forma en que los diferentes elementos $x_i$ de la tupla se relacionan y condicionan mutuamente.
* Son las encargadas de imponer el camino específico que define la viabilidad de la solución.