# Problema de Asignación y Algoritmo Húngaro

Este bloque de apuntes de la asignatura **Algorítica** (ETSIIT, Universidad de Granada) aborda la resolución sistemática del problema de asignación óptima de tareas empleando el método clásico del **Algoritmo Húngaro**.

---

## 1. Pasos del Algoritmo Húngaro

A continuación se detallan las reglas y pasos del método tal y como están descritos en el manuscrito original:

1. **Se realiza la tabla con los costes** iniciales de asignación.
2. **Restar en cada fila su número menor** (reducción por filas).
3. **Se trazan líneas verticales y horizontales** para abarcar la mayor cantidad de ceros ($0$) posible utilizando el menor número de líneas.
4. **Se resta el número mínimo** de los elementos no cubiertos (restantes) a todos los elementos no cubiertos.
5. **Se repite el paso 3**, pero **sumando el número mínimo** a aquellos elementos situados en las intersecciones de las líneas.
6. **Criterio de parada:** Cuando se obtiene un número de líneas igual al orden de la matriz ($n = 4$ en este caso de ejemplo), se detiene el proceso de optimización.
7. **Se usan los ceros ($0$) para asignar** de forma unívoca y óptima las tareas.

---

## 2. Traza de Ejecución Paso a Paso

### Paso 1: Matriz Inicial de Costes
Se define la matriz de costes de dimensión $4 \times 4$ para asignar cuatro tareas/recursos ($1, 2, 3, 4$) a cuatro agentes ($A, B, C, D$):

$$
\begin{array}{c|cccc}
 & 1 & 2 & 3 & 4 \\
\hline
A & 48 & 48 & 50 & 44 \\
B & 56 & 60 & 60 & 68 \\
C & 96 & 94 & 90 & 85 \\
D & 42 & 44 & 54 & 46
\end{array}
$$

---

### Paso 2: Reducción por Filas
Restamos el menor valor de cada fila a todos los elementos de su respectiva fila:
*   Fila $A$: mín $= 44 \implies [4, 4, 6, 0]$
*   Fila $B$: mín $= 56 \implies [0, 4, 4, 12]$
*   Fila $C$: mín $= 85 \implies [11, 9, 5, 0]$
*   Fila $D$: mín $= 42 \implies [0, 2, 12, 4]$

$$
\begin{array}{c|cccc}
 & 1 & 2 & 3 & 4 \\
\hline
A & 4 & 4 & 6 & 0 \\
B & 0 & 4 & 4 & 12 \\
C & 11 & 9 & 5 & 0 \\
D & 0 & 2 & 12 & 4
\end{array}
$$

---

### Paso 3: Cobertura Inicial de Ceros
Trazamos el mínimo número de líneas para cubrir todos los ceros de la matriz reducida:
*   **Línea vertical 1** en la Columna $1$ (cubre los ceros en $B1$ y $D1$).
*   **Línea vertical 2** en la Columna $4$ (cubre los ceros en $A4$ y $C4$).

$$
\begin{array}{c|cccc}
 & \color{red}{\downarrow} & & & \color{red}{\downarrow} \\
 & 1 & 2 & 3 & 4 \\
\hline
A & \color{red}{4} & 4 & 6 & \color{red}{0} \\
B & \color{red}{0} & 4 & 4 & \color{red}{12} \\
C & \color{red}{11} & 9 & 5 & \color{red}{0} \\
D & \color{red}{0} & 2 & 12 & \color{red}{4}
\end{array}
$$

> ⚠️ **Nota académica sobre la traza:** 
> En este punto del manuscrito original se aprecia una pequeña inconsistencia aritmética por parte del alumno. El mínimo elemento no cubierto es $2$ (situado en $D2$). Al restar $2$ a los elementos no cubiertos de forma rigurosa, se deberían obtener valores ligeramente distintos en las filas $A$ y $C$. En los apuntes se muestra que el alumno restó $4$ en lugar de $2$ en algunas posiciones. A continuación se detalla la traza tal y como está escrita en el papel para preservar su fidelidad histórica.

---

### Pasos 4 y 5: Modificación de la Matriz y Nuevas Coberturas
La matriz resultante del manuscrito tras aplicar las restas y trazar una nueva cobertura de tres líneas (línea horizontal en la fila $B$, líneas verticales en columnas $2$ y $4$) es:

$$
\begin{array}{c|cccc}
 & 1 & \color{red}{\downarrow} & 3 & \color{red}{\downarrow} \\
\hline
A & 4 & 0 & 2 & 0 \\
\color{red}{\rightarrow}\ B & \color{red}{0} & \color{red}{2} & \color{red}{2} & \color{red}{12} \\
C & 11 & 5 & 1 & 0 \\
D & 2 & 0 & 10 & 4
\end{array}
$$

El menor valor no cubierto en esta configuración es $1$ (situado en la posición $C3$). Restamos $1$ de los elementos descubiertos y sumamos $1$ en las intersecciones cubiertas por dos líneas para obtener la siguiente matriz del manuscrito:

$$
\begin{array}{c|cccc}
 & 1 & 2 & 3 & 4 \\
\hline
A & 4 & 0 & 2 & 0 \\
B & 0 & 1 & 0 & 12 \\
C & 10 & 5 & 0 & 0 \\
D & 1 & 0 & 10 & 6
\end{array}
$$

---

### Paso 6: Verificación de Parada
Trazamos las líneas de cobertura sobre la matriz actual:
*   **Líneas horizontales:** Fila $B$ y Fila $C$.
*   **Líneas verticales:** Columna $2$ y Columna $4$.

$$
\begin{array}{c|cccc}
 & & \color{red}{\downarrow} & & \color{red}{\downarrow} \\
\hline
A & 4 & 0 & 2 & 0 \\
\color{red}{\rightarrow}\ B & \color{red}{0} & \color{red}{1} & \color{red}{0} & \color{red}{12} \\
\color{red}{\rightarrow}\ C & \color{red}{10} & \color{red}{5} & \color{red}{0} & \color{red}{0} \\
D & 1 & 0 & 10 & 6
\end{array}
$$

Como se requieren **4 líneas** para cubrir la totalidad de los ceros, el algoritmo finaliza satisfactoriamente.

---

### Paso 7: Asignación Final Óptima
Aislamos las posiciones con valor $0$ resultantes en el último paso:

$$
\begin{array}{c|cccc}
 & 1 & 2 & 3 & 4 \\
\hline
A & & 0 & & 0 \\
B & 0 & & 0 & \\
C & & & 0 & 0 \\
D & & 0 & & 
\end{array}
$$

Buscamos una asignación única uno a uno a partir de estas posiciones con valor cero:

*   Como el agente $D$ solo tiene un cero en la columna $2$, asignamos: **$2 \rightarrow D$**.
*   Con la columna $2$ ocupada, el agente $A$ debe tomar su otro cero en la columna $4$: **$4 \rightarrow A$**.
*   Con la columna $4$ ocupada, el agente $C$ debe tomar la columna $3$: **$3 \rightarrow C$**.
*   Con la columna $3$ ocupada, el agente $B$ toma la columna restante $1$: **$1 \rightarrow B$**.

Por tanto, la asignación óptima es:

$$\begin{aligned}
\mathbf{1} &\rightarrow \mathbf{B} \\
\mathbf{2} &\rightarrow \mathbf{D} \\
\mathbf{3} &\rightarrow \mathbf{C} \\
\mathbf{4} &\rightarrow \mathbf{A}
\end{aligned}$$

---

### Cálculo del Coste Mínimo Total
Consultamos los valores de coste correspondientes en la matriz original del paso 1:

*   Coste $(1, B) = 56$
*   Coste $(2, D) = 44$
*   Coste $(3, C) = 90$
*   Coste $(4, A) = 44$

$$\text{Coste Total} = 56 + 44 + 90 + 44 = \mathbf{234}$$