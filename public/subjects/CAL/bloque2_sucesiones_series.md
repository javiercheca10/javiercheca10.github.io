# Sucesiones

## Monotonía y Convergencia

### Monotonía
Para determinar la monotonía de una sucesión por inducción:
1. Verificar el caso base.
2. Probar si $x_n < x_{n+1}$ (creciente) o $x_n > x_{n+1}$ (decreciente).

### Convergencia
Si la sucesión converge:
1. Suponer que $\lim_{n\to\infty} x_{n+1} = \lim_{n\to\infty} x_n = L$.
2. Resolver la ecuación resultante para hallar el candidato a límite $L$.
3. Demostrar por inducción si la sucesión está acotada superior o inferiormente por el número calculado.

---

### Ejemplo: Calcular si una sucesión es convergente y su límite

Sea la sucesión definida por:
$$x_1 = 1, \quad x_{n+1} = \sqrt{3x_n} \quad \forall n \ge 1$$

#### 1. Ver por inducción si es creciente:

*   **1.1. Caso base:** Comprobar que $x_1 < x_2$
    $$x_1 = 1$$
    $$x_2 = \sqrt{3 \cdot 1} = \sqrt{3} \approx 1.73 \implies x_1 < x_2 \quad \text{(Se cumple)}$$

*   **1.2. Paso inductivo:** Si $x_n < x_{n+1}$, entonces $x_{n+1} < x_{n+2}$
    Como la función de recurrencia es creciente:
    $$x_{n+1} = \sqrt{3x_n} < \sqrt{3x_{n+1}} = x_{n+2}$$
    $$\text{¡Es creciente!}$$

#### 2. Ver si está acotada y calcular el límite:

*   **2.1.** Si está acotada, los límites de $x_n$ y $x_{n+1}$ coinciden en un valor $L$:
    $$L = \sqrt{3L} \implies L = 3$$

*   **2.2. Tomamos límites en la fórmula:**
    $$x = \sqrt{3x} \implies x^2 = 3x \implies x^2 - 3x = 0 \implies x(x-3) = 0 \implies x = 0 \quad \text{ó} \quad x = 3$$
    Como $x_1 = 1$ y la sucesión es creciente, el límite debe ser mayor que $1$. Por lo tanto:
    $$\lim_{n \to \infty} x_n = 3$$

---

## Criterio de Stolz

> **Criterio de Stolz**:
> Si tenemos un cociente de sucesiones de la forma $\frac{a_n}{b_n}$ donde la sucesión $\{b_n\}$ es monótona y cumple:
> *   Si es creciente: $\lim_{n \to \infty} b_n = \infty$
> *   Si es decreciente: $\lim_{n \to \infty} b_n = 0$
>
> Entonces, si existe el límite:
> $$\lim_{n \to \infty} \frac{a_n - a_{n-1}}{b_n - b_{n-1}} = a \quad \text{ó} \quad \lim_{n \to \infty} \frac{a_{n+1} - a_n}{b_{n+1} - b_n} = a$$
> Se cumple que:
> $$\lim_{n \to \infty} \frac{a_n}{b_n} = a$$

### Ejemplo de aplicación del Criterio de Stolz

Calcular el límite de la sucesión:
$$\left\{ \frac{1 + \sqrt{2} + \sqrt[3]{3} + \dots + \sqrt[n]{n}}{n^2} \right\}$$

Definimos:
$$a_n = 1 + \sqrt{2} + \sqrt[3]{3} + \dots + \sqrt[n]{n}$$
$$b_n = n^2 \quad (\text{monótona creciente y } \lim_{n\to\infty} b_n = \infty)$$

Aplicamos el criterio:
$$\frac{a_{n+1} - a_n}{b_{n+1} - b_n} = \frac{\left(1 + \sqrt{2} + \sqrt[3]{3} + \dots + \sqrt[n+1]{n+1}\right) - \left(1 + \sqrt{2} + \sqrt[3]{3} + \dots + \sqrt[n]{n}\right)}{(n+1)^2 - n^2}$$
$$= \frac{\sqrt[n+1]{n+1}}{(n+1)^2 - n^2} = \frac{\sqrt[n+1]{n+1}}{2n+1}$$

Calculamos el límite del numerador:
$$\lim_{n \to \infty} \sqrt[n+1]{n+1} = \lim_{n \to \infty} (n+1)^{\frac{1}{n+1}} = 1$$

Por tanto:
$$\lim_{n \to \infty} \frac{\sqrt[n+1]{n+1}}{2n+1} = 0$$

Concluimos que:
$$\lim_{n \to \infty} \frac{1 + \sqrt{2} + \sqrt[3]{3} + \dots + \sqrt[n]{n}}{n^2} = 0$$

---

## Criterio de la Raíz (para Sucesiones)

> **Criterio de la Raíz**:
> Si tenemos una sucesión de la forma $s_n = \sqrt[n]{a_n}$, su límite se puede calcular mediante:
> $$\lim_{n \to \infty} \sqrt[n]{a_n} = \lim_{n \to \infty} \frac{a_{n+1}}{a_n}$$

### Ejemplo de aplicación del Criterio de la Raíz

Calcular el límite de la sucesión:
$$\left\{ \frac{\sqrt[n]{2 \cdot 4 \cdot 6 \cdot \dots \cdot 2n}}{n+1} \right\}$$

Reescribimos la expresión introduciendo el denominador dentro de la raíz:
$$\sqrt[n]{\frac{2 \cdot 4 \cdot 6 \cdot \dots \cdot 2n}{(n+1)^n}}$$

Definimos $a_n = \frac{2 \cdot 4 \cdot 6 \cdot \dots \cdot 2n}{(n+1)^n}$ y aplicamos el cociente $\frac{a_{n+1}}{a_n}$:
$$\frac{a_{n+1}}{a_n} = \frac{\frac{2 \cdot 4 \cdot 6 \cdot \dots \cdot (2n)(2n+2)}{(n+2)^{n+1}}}{\frac{2 \cdot 4 \cdot 6 \cdot \dots \cdot 2n}{(n+1)^n}} = \frac{2n+2}{n+2} \cdot \frac{(n+1)^n}{(n+2)^n} = \frac{2n+2}{n+2} \left( \frac{n+1}{n+2} \right)^n$$

Tomamos el límite cuando $n \to \infty$:
$$\lim_{n \to \infty} \frac{2n+2}{n+2} = 2$$
$$\lim_{n \to \infty} \left( \frac{n+1}{n+2} \right)^n = \lim_{n \to \infty} \left( 1 - \frac{1}{n+2} \right)^n = e^{-1}$$

Por lo tanto:
$$\lim_{n \to \infty} \frac{\sqrt[n]{2 \cdot 4 \cdot 6 \cdot \dots \cdot 2n}}{n+1} = 2e^{-1} = \frac{2}{e}$$

---

## Regla del número $e$ (para Sucesiones)

> **Regla del número $e$**:
> $$\lim_{n \to \infty} a_n^{b_n} = e^{\lim_{n \to \infty} (b_n)(a_n - 1)}$$

### Ejemplo de aplicación de la Regla del número $e$

Calcular el límite:
$$\lim_{n \to \infty} \left( 1 + \log(n+1) - \log(n) \right)^n$$

Utilizando propiedades de los logaritmos:
$$\left( 1 + \log(n+1) - \log(n) \right)^n \implies \left( 1 + \log \frac{n+1}{n} \right)^n$$

Aplicamos la regla del número $e$:
$$\lim_{n \to \infty} \left( 1 + \log \frac{n+1}{n} \right)^n = e^{\lim_{n \to \infty} (n) \left( 1 + \log \frac{n+1}{n} - 1 \right)} = e^{\lim_{n \to \infty} (n) \left( \log \frac{n+1}{n} \right)}$$

Calculamos el límite del exponente:
$$\lim_{n \to \infty} (n) \left( \log \frac{n+1}{n} \right) = \lim_{n \to \infty} \log \left( \frac{n+1}{n} \right)^n$$

Como $\lim_{n \to \infty} \left( \frac{n+1}{n} \right)^n = e$, el límite del exponente es:
$$\lim_{n \to \infty} \log \left( \frac{n+1}{n} \right)^n = \log(e) = 1$$

*(Nota: También se puede resolver usando la equivalencia de infinitésimos $\log(1 + x) \sim x$ cuando $x \to 0$)*:
$$\lim_{n \to \infty} n \left( \frac{n+1}{n} - 1 \right) = \lim_{n \to \infty} n \left( \frac{1}{n} \right) = 1$$

Por lo tanto:
$$\lim_{n \to \infty} \left( 1 + \log(n+1) - \log(n) \right)^n = e^1 = e$$

---
---

# Series Numéricas

## Suma de Series Geométricas

> **Serie Geométrica**:
> Si una serie tiene la forma $\sum_{n=0}^{\infty} r^n$ con $-1 < r < 1$, entonces es convergente y su suma es:
> $$S = \frac{1}{1-r}$$

---

## Criterio de la Raíz (para Series)

> **Criterio de la Raíz**:
> Si el término general de la serie tiene la forma $(a_n)^n$, entonces calculamos:
> $$\lim_{n \to \infty} \sqrt[n]{(a_n)^n}$$
> *   Si el límite es $< 1$, la serie es **convergente**.

---

## Criterio del Cociente (para Series)

> **Criterio del Cociente**:
> Si el término general de la serie es de la forma $a_n = \frac{b_n}{c_n}$, evaluamos el límite:
> $$\lim_{n \to \infty} \frac{a_{n+1}}{a_n}$$
> *   Si el límite es $< 1$, la serie es **convergente**.

---
---

# Límites de Funciones

## Regla del número $e$ (para Funciones)

> **Regla del número $e$**:
> Consideramos el límite de la forma $\lim_{x \to a} f(x)^{g(x)}$ donde $\lim_{x \to a} f(x) = 1$.
>
> Evaluamos el límite del exponente modificado:
> $$\lim_{x \to a} g(x)[f(x) - 1]$$
>
> Dependiendo de su resultado, el límite original será:
> *   Si $\lim_{x \to a} g(x)[f(x) - 1] = L \implies \lim_{x \to a} f(x)^{g(x)} = e^L$
> *   Si $\lim_{x \to a} g(x)[f(x) - 1] = \infty \implies \lim_{x \to a} f(x)^{g(x)} = \infty$
> *   Si $\lim_{x \to a} g(x)[f(x) - 1] = -\infty \implies \lim_{x \to a} f(x)^{g(x)} = -\infty$
