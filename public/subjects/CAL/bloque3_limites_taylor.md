# Batería de Ejercicios de Cálculo

## Dominio e Imagen

### Ejemplo
$$f(x) = \arctan\left(\frac{\log(x+1)}{\log(x)}\right)$$

### Dominio
Evaluar cuándo la función toma valores no válidos.

| Función | Excepción | En el ejemplo |
| :--- | :--- | :--- |
| **Fracción** | El $0$ en el denominador | El denominador no puede ser $0$, por lo que $\log(x) \neq 0 \Rightarrow x \neq 1$. |
| **Logaritmo ($\log$)** | $a \le 0$ | El argumento debe ser positivo: <br> $x+1 > 0 \Rightarrow x > -1$ <br> $x > 0$ |
| **Raíz** | $a < 0$ | |

Combinando estas condiciones para el ejemplo, el dominio debe ser positivo y además no puede ser $1$:
$$\text{Dom}(f) = (0, 1) \cup (1, +\infty)$$

---

### Imagen

#### Monotonía
Calculamos la primera derivada y evaluamos los signos:
*   $+$ crece
*   $-$ decrece

#### Extremos
Límites laterales.

---

## Límites

Indeterminación del tipo $1^\infty \Rightarrow$ **Regla del número $e$**:

$$\lim_{x \to \infty} f(x)^{g(x)} = e^{\lim_{x \to \infty} g(x)(f(x)-1)}$$

---

## Polinomio de Taylor

$$P_n(f, a)(x) = f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2 + \dots + \frac{f^{(n)}(a)}{n!}(x-a)^n$$

Donde:
*   $f \to$ función.
*   $a \to$ punto donde está centrado.
*   $x \to$ punto donde se evalúa.

### Estimación del Error (Resto de Lagrange)

$$|R_n(x)| = \left| \frac{f^{(n+1)}(c)}{(n+1)!}(x-a)^{n+1} \right|$$

Al final, para acotar el error, suele resultar en una relación del tipo:

$$\frac{1}{(n+1)!} < \text{error} \quad \text{ó} \quad (n+1)! > \text{error}^{-1}$$
