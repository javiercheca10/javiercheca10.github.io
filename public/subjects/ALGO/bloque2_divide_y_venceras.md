# Diseño Divide y Vencerás y Umbral de Recursividad

## 1. Esquema General de Divide y Vencerás (DyV)

El diseño de algoritmos basado en **Divide y Vencerás** es un paradigma fundamental en la algorítmica que consta de tres fases consecutivas:

1. **Dividir**: El problema original $P$ se descompone en un conjunto de subproblemas más pequeños del mismo tipo, denotados como $\{P_1, P_2, \dots, P_k\}$.
2. **Resolver (Vencer)**: Se resuelven recursivamente los subproblemas $P_i$. Si el tamaño de un subproblema es lo suficientemente pequeño (caso base), se aplica un algoritmo directo o básico de resolución.
3. **Combinar**: Se mezclan o recombinan las soluciones individuales de los subproblemas $\{S_1, S_2, \dots, S_k\}$ para construir la solución global $S$ del problema original.

### Metodología de Diseño (Esquema Algorítmico)

El comportamiento de un algoritmo genérico de tipo Divide y Vencerás se puede estructurar formalmente mediante el siguiente esquema en pseudocódigo:

```text
Función DyV(P)
    Si P es simple:
        Devolver básico(P)
    En otro caso:
        Descomponer P en subcasos (P_1), (P_2), ..., (P_k)
        Para i = 1 hasta k:
            S_i = DyV(P_i)   // Resolver recursivamente
        S = Recombinar(S_1, S_2, ..., S_k)
        Devolver S
```

---

## 2. Ecuación de Recurrencia Asociada

Todo algoritmo basado en el diseño de Divide y Vencerás lleva **SIEMPRE** asociada una ecuación de recurrencia para modelar su tiempo de ejecución $T(n)$ en función del tamaño de la entrada $n$:

$$T(n) = \begin{cases} 
t(n) & \text{si } n \le c \\ 
a T\left(\frac{n}{b}\right) + D(n) + C(n) & \text{en otro caso} 
\end{cases}$$

Donde los parámetros se definen de la siguiente manera:

*   **$a$**: Número de subproblemas independientes en los que se divide el problema original ($a \ge 1$).
*   **$n/b$**: Tamaño de cada uno de los subproblemas generados ($b > 1$). El factor $b$ representa la reducción de tamaño.
*   **$D(n)$**: Tiempo invertido en realizar la división del problema original en subproblemas de menor tamaño.
*   **$C(n)$**: Tiempo necesario para combinar las soluciones parciales obtenidas de manera recursiva y generar la solución final.
*   **$t(n)$**: Tiempo empleado por el algoritmo básico de resolución directa para casos cuyo tamaño está por debajo del límite elemental $c$ ($n \le c$).

---

## 3. Umbral de Recursividad ($n_0$)

### Concepto
El **umbral de recursividad** ($n_0$) se define como el tamaño de problema límite o de frontera en el que se produce la transición de conveniencia de uso entre el algoritmo básico (directo) y el algoritmo recursivo. 

> **Nota de diseño:** En la práctica, la recursión introduce una sobrecarga de memoria y tiempo debido a la gestión de la pila de llamadas de activación. Por tanto, para tamaños de entrada pequeños ($n \le n_0$), resulta computacionalmente más eficiente resolver el problema directamente mediante el algoritmo básico en lugar de seguir subdividiéndolo de forma recursiva.

Para calcular este punto de equilibrio, se deben **igualar las expresiones de coste** de ambos enfoques.

---

### Comportamiento según el valor de $n_0$

El valor del umbral óptimo $n_0$ teóricamente oscila entre los límites del intervalo $[0, \infty]$:

*   **Si $n_0 \to \infty$**: Significa que no es óptimo aplicar la estrategia de Divide y Vencerás para ningún tamaño de entrada viable. Siempre será preferible y más eficiente utilizar el **algoritmo básico**.
*   **Si $n_0 = 0$**: El coste del algoritmo básico no es competitivo en ningún escenario práctico. El algoritmo teórico se ejecutaría únicamente $1$ vez en el caso límite y se mantendría en **recursividad todo el tiempo**.

---

### Ejemplo Práctico de Determinación del Umbral

Definamos el coste de un algoritmo híbrido $t_C(n)$ que utiliza una solución básica de coste $t_A(n)$ por debajo del umbral $n_0$ y una estrategia de subdivisión en 3 subproblemas de tamaño $n/2$ por encima de él:

$$t_C(n) = \begin{cases} 
t_A(n) & \text{si } n \le n_0 \\ 
3 t_C\left(\frac{n}{2}\right) + t(n) & \text{si } n \ge n_0 
\end{cases}$$

Donde los costes particulares dados son:
*   **Algoritmo básico**: $t_A(n) = n^2$
*   **Coste de división y combinación**: $t(n) = 16n$
*   **Caso límite de ejemplo**: $n = 1024$

Para hallar el punto exacto del umbral $n_0$, planteamos la igualdad de coste en la frontera de decisión, es decir, el punto donde el coste del algoritmo básico iguala al de una iteración recursiva:

$$t_A(n) = 3 t_A\left(\frac{n}{2}\right) + t(n)$$

Sustituyendo las funciones correspondientes:

$$n^2 = 3 \cdot \left(\frac{n}{2}\right)^2 + 16n$$

Desarrollamos los términos algebraicos paso a paso:

$$n^2 = 3 \cdot \left(\frac{n^2}{4}\right) + 16n$$

$$n^2 = \frac{3}{4} n^2 + 16n$$

Restamos $\frac{3}{4}n^2$ en ambos miembros de la ecuación:

$$n^2 - \frac{3}{4} n^2 = 16n$$

$$\frac{1}{4} n^2 = 16n$$

Asumiendo que $n \neq 0$, simplificamos dividiendo ambos lados por $n$ y multiplicando por el denominador:

$$n = 16 \cdot 4$$

$$n_0 = 64$$

**Conclusión:** El umbral óptimo de recursividad es **$n_0 = 64$**. Para cualquier instancia del problema de tamaño $n \le 64$ se debe resolver directamente con el algoritmo básico $t_A(n)$, mientras que para $n > 64$ es computacionalmente preferible subdividir el problema recursivamente mediante el esquema de Divide y Vencerás.