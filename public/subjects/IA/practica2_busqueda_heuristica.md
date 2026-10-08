# Práctica 2: Agente Deliberativo y Búsqueda Heurística A*

En la segunda práctica se dota al agente de capacidades deliberativas avanzadas mediante la formulación de problemas de **búsqueda en espacios de estados** y planificación de secuencias óptimas de acciones.

---

## 1. Espacio de Estados y Representación

El estado del agente se modela formalmente mediante una estructura que captura todas las variables relevantes para la toma de decisiones:

```cpp
struct ubicacion {
    int f;                 // Coordenada de fila
    int c;                 // Coordenada de columna
    Orientacion brujula;   // Orientación angular (8 direcciones)
};

struct stateN0 {
    ubicacion jugador;
    ubicacion colaborador;
    Action ultimaOrdenColaborador;
};
```

Un nodo del árbol/grafo de búsqueda almacena:
* El estado actual `st`.
* La secuencia de acciones acumuladas `plan` para alcanzarlo desde la raíz.
* El coste acumulado $g(n)$ (consumo de batería según el tipo de terreno).
* La estimación heurística $h(n)$ hasta el objetivo.
* La función de evaluación global:
$$f(n) = g(n) + h(n)$$

---

## 2. Niveles de Dificultad y Algoritmos Implementados

### Nivel 0 y Nivel 1: Búsqueda No Informada (BFS - Anchura)
* **Objetivo:** Encontrar el camino más corto en número de pasos hasta la casilla destino sin considerar el consumo energético del terreno.
* **Estructuras:** Cola FIFO para la frontera de exploración y conjunto cerrado (`std::set` / `std::unordered_set`) para evitar ciclos y estados repetidos.
* **Garantía:** Óptimo en número de pasos para costes unitarios.

### Nivel 2 y Nivel 3: Búsqueda de Coste Uniforme (Dijkstra) y Algoritmo A*
* **Función de Coste Real $g(n)$:**
  El coste de cada acción depende del terreno pisado y de los objetos que porte el agente:
  * Agua sin bikini: alto consumo; con bikini: consumo mínimo.
  * Bosque sin zapatillas: alto consumo; con zapatillas: consumo mínimo.
* **Función Heurística Admisible $h(n)$:**
  Distancia Chebyshev / Octile o Manhattan adaptada al movimiento en 8 direcciones:
  $$h(n) = \max(|f_n - f_{dest}|, |c_n - c_{dest}|)$$
  Al ser admisible ($h(n) \le h^*(n)$) y monótona/consistente, $A^*$ garantiza encontrar el plan con menor consumo de batería.

### Nivel 4: Agente Deliberativo en Entorno Parcialmente Observable
* Cuando el mapa no es completamente conocido a priori o el entorno cambia dinámicamente, el agente opera en un bucle continuo de:
  1. **Percepción:** Actualizar el mapa local con los sensores visuales.
  2. **Planificación:** Ejecutar $A^*$ sobre el mapa conocido hasta el objetivo más prometedor o casilla de recarga.
  3. **Ejecución y Monitoreo:** Avanzar según el plan hasta detectar un cambio imprevisto (obstáculo nuevo o agente móvil bloqueando el paso), provocando una replanificación reactiva inmediata.
