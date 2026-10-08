# Eficiencia de Algoritmos y Resolución de Recurrencias

## Conceptos Básicos de Algorítmica

### Algoritmo
Secuencia finita y ordenada de pasos, exentos de ambigüedad, tal que al llevarse a cabo con fidelidad se obtendrá la solución del problema planteado con recursos limitados y en tiempo finito.

### Características

* **a) Finitud:** Ha de terminar en un tiempo acotado.
* **b) Especificidad:** Cada etapa debe estar precisamente definida.
* **c) Input:** Tiene $0$ o más inputs.
* **d) Output:** Tiene $1$ o más outputs.
* **e) Efectividad:** Todas las operaciones deben ser básicas, para que se hagan exactamente y en un periodo finito.

---

### Notación Asintótica

* **$O(g(n))$:** Expresión que acota superiormente.
* **$\Omega(g(n))$:** Expresión que acota inferiormente.
* **$\Theta(g(n))$:** Expresión que une las dos anteriores y acota superior e inferiormente.

---

## Resolución de Recurrencias

### Recurrencias Homogéneas

Dada la recurrencia:
$$t_n - 3t_{n-1} - 4t_{n-2} = 0 \quad \text{con las condiciones iniciales } t_0 = 0, \ t_1 = 1$$

#### a) Ecuación característica
A partir de la recurrencia, planteamos su ecuación característica:
$$x^2 - 3x - 4 = 0 \implies (x + 1)(x - 4) = 0$$

Obtenemos las raíces:
$$x = -1, \quad x = 4$$

#### b) Solución general
La solución general se expresa como una combinación lineal de las raíces elevadas a la $n$:
$$t_n = c_1 (-1)^n + c_2 4^n$$

#### c) Sistema de ecuaciones ($n = 0, \ n = 1$)
Aplicando las condiciones iniciales:
$$\begin{cases} 
c_1 + c_2 = 0 & (n = 0) \\ 
-c_1 + 4c_2 = 1 & (n = 1) 
\end{cases}$$

Resolviendo el sistema:
$$c_1 = -\frac{1}{5}, \quad c_2 = \frac{1}{5}$$

#### d) Solución final
Sustituyendo los coeficientes obtenidos:
$$t_n = -\frac{1}{5}(-1)^n + \frac{1}{5} 4^n \implies t_n = \frac{1}{5} \left[ 4^n - (-1)^n \right]$$

> **Nota sobre raíces múltiples:**
> Si una raíz $r$ se repite con multiplicidad, los términos de la solución general se expanden de la forma:
> $$t_1 = r^n, \quad t_2 = n \cdot r^n, \quad t_3 = n^2 \cdot r^n, \ \dots$$

---

### Recurrencias No Homogéneas

Dada la recurrencia:
$$t_n - 2t_{n-1} - 3^n = 0$$

#### a) Agrupación de la parte homogénea y no homogénea
Separamos los términos:
$$t_n - 2t_{n-1} = 3^n$$

#### b) Identificar la parte no homogénea siguiendo la forma $b^n p(n)$

* **Ejemplo 1:** 
  Para el término $3^n$:
  $$\begin{aligned}
  b &= 3 \\
  p(n) &= 1 \\
  g(p(n)) &= 0 \quad (\text{grado del polinomio } p(n))
  \end{aligned}$$

* **Ejemplo 2:** 
  Para un término del tipo $3^n(n + 2)$:
  $$\begin{aligned}
  b &= 3 \\
  p(n) &= n + 2 \\
  g(p(n)) &= 1
  \end{aligned}$$

#### c) Ecuación característica con la forma $(\text{Ec. caract. homo})(x - b)^{g(p(n)) + 1} = 0$

Para nuestro caso (**Ejemplo 1**), la parte homogénea $t_n - 2t_{n-1} = 0$ tiene la ecuación característica $(x - 2) = 0$.

Añadiendo el factor de la parte no homogénea con $b = 3$ y $g(p(n)) = 0$:
$$(x - 2)(x - 3)^{0 + 1} = 0 \implies (x - 2)(x - 3) = 0$$

Cuyas raíces son:
$$x = 2, \quad x = 3$$

---

## Cambio de Variable

Dada la relación de recurrencia:
$$T(n) = 4 T\left(\frac{n}{2}\right) + n \quad \text{para } n > 1$$

#### a) Reemplazamos $n$ por $2^k$
Asumiendo que $n = 2^k$ (es decir, $k = \log_2 n$):
$$T(2^k) = 4 T(2^{k-1}) + 2^k$$

Haciendo el cambio de variable $t_k = T(2^k)$, obtenemos una ecuación de recurrencia lineal:
$$t_k = 4 t_{k-1} + 2^k$$

#### b) Resolución
*(A partir de aquí, se resolvería de forma análoga a una recurrencia no homogénea para hallar $t_k$ y posteriormente deshacer el cambio para obtener $T(n)$).*