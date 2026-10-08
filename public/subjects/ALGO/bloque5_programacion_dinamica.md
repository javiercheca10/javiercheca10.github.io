# Programación Dinámica y Problema del Cambio

Mantiene en memoria la solución a los subproblemas para evitar cálculos repetidos.

---

### Comparativa: Divide y Vencerás (DyV) vs. Programación Dinámica (PD)

| **Divide y Vencerás ($DyV$)** | **Programación Dinámica ($PD$)** |
| :--- | :--- |
| Recursividad ($+$ tiempo, $-$ memoria) | Iterativo/Memoizado ($-\text{tiempo}$, $+\text{memoria}$) |
| Subproblemas independientes | Subproblemas que se solapan |

---

### Pasos para diseñar un algoritmo de Programación Dinámica

1. **Poderse resolver por etapas.**
2. **Plantear el problema como una ecuación de optimización recursiva**, con $1$ o varios casos base.
3. **Encontrar una representación** para almacenar las subsoluciones.
4. **Verificar que se cumple el Principio de Optimalidad de Bellman:** 
   > Si tenemos una secuencia óptima de decisiones, cualquier subsecuencia de la misma debe ser también óptima.

---

### El problema del cambio de moneda

Asumimos que:

1. Hay monedas de $n$ valores diferentes.
2. Las monedas del tipo $i$ tienen valor $x_i$. 
   $$\text{Ejemplo: } \begin{cases} x_1 = 1 \\ x_2 = 5 \\ x_3 = 10 \end{cases}$$
3. Al cliente hay que devolverle un valor $W$.
4. Las monedas están ordenadas por su valor de forma ascendente.
5. **Objetivo:** Minimizar el número ($n^\circ$) de monedas a devolver.