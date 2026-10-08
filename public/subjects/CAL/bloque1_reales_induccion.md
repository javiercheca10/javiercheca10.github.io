# Cálculo: Tema 1: Conjuntos Numéricos

Se estudian las matemáticas a partir de:
* **Definiciones**: Ej: Factorial de un $n$ natural: $n! = 1 \cdot 2 \cdot 3 \cdot 4 \cdot \dots \cdot n$
* **Teoremas**: (Se enunciarán y preguntarán) Ej: Teorema de Pitágoras.
* **Corolario**: (Consecuencias de un teorema) Ej: En un triángulo rectángulo de catetos $b$ y $c$ e hipotenusa $a$:
  $$a^2 = b^2 + c^2$$
* **Escolio**: (Nota breve para explicar un teorema)

---

### Identidades Elementales
* $(A+B)^2 = A^2 + 2AB + B^2$
* $(A-B)^2 = A^2 - 2AB + B^2$
* $(A+B)(A-B) = A^2 - B^2$

### Tipos de Igualdades
* **Identidades**: Se verifican siempre (para cualquier valor).
* **Ecuaciones**: Se verifican para un valor (o conjunto de valores) concreto.

---

## Conjuntos Numéricos

### 1. Naturales ($\mathbb{N}$)
$$\mathbb{N} = \{0, 1, 2, 3, 4, \dots\}$$

Se pueden sumar y multiplicar, por lo que forman un **semigrupo**.

#### Propiedades
* **Asociativa**: 
  $$a + (b + c) = (a + b) + c$$
* **Elemento Neutro**: 
  $$a + 0 = a \quad ; \quad a \cdot 1 = a$$
* **Conmutativa**: 
  $$a + b = b + a$$
* **Distributiva**: 
  $$a \cdot (b + c) = a \cdot b + a \cdot c$$

> **Nota**: No siempre es posible realizar la resta en $\mathbb{N}$, por lo que se amplía el conjunto.

---

### 2. Enteros ($\mathbb{Z}$)
$$\mathbb{Z} = \{0, 1, -1, 2, -2, \dots\}$$

Se pueden sumar, restar y multiplicar, por lo que forman un **grupo**.

> **Grupo Abeliano**: Grupo conmutativo.

#### Propiedades
* **Asociativa**
* **Elemento Neutro**: $[0, 1]$ (0 para la suma, 1 para el producto)
* **Elemento Opuesto**: $[a \ ; \ -a]$
* **Conmutativa**

> **Nota**: La multiplicación no tiene inversa en $\mathbb{Z}$. Se amplía el conjunto:

---

### 3. Racionales ($\mathbb{Q}$)
$$\mathbb{Q} = \left\{ \frac{a}{b} \quad \text{donde} \quad a \in \mathbb{Z}, \ b \in \mathbb{Z}^*, \ \mathbb{Z}^* = \mathbb{Z} \setminus \{0\} \right\}$$

#### Propiedades de la Suma
* **Asociativa**
* **Elemento Neutro**: $\left[\frac{0}{1}\right]$
* **Elemento Opuesto**: $\left[\frac{a}{b} \ ; \ -\frac{a}{b}\right]$
* **Conmutativa**

#### Propiedades del Producto
* **Asociativa**
* **Elemento Neutro**: $\left[\frac{1}{1}\right]$
* **Elemento Recíproco**: $\left[\frac{a}{b} \cdot \frac{b}{a} = 1\right]$
* **Conmutativa**

#### Propiedad Distributiva
$$a \cdot (b + c) = a \cdot b + a \cdot c$$

> **Definición (Cuerpo)**: Conjunto en el que se puede sumar y multiplicar, y además se cumplen las propiedades asociativa, conmutativa, distributiva, y existen los elementos neutros y opuestos/inversos (tanto para la suma como para el producto).

A pesar de que $\mathbb{Q}$ es un cuerpo, hay números que no son racionales y no están dentro de este conjunto.

---

### 4. Reales ($\mathbb{R}$)

Se pueden realizar las operaciones $(+, \cdot, \div, a^b, \ln)$ con las siguientes restricciones:
* División por $0$.
* Logaritmos de números negativos.
* Elevación de un número negativo a una potencia fraccionaria irreducible con denominador par, o elevación a una potencia irracional.

---

## Tema 1: Números Reales

$\mathbb{R}$ será un conjunto no vacío. Describiremos las propiedades que lo definen:

### Suma
Tenemos una suma de números reales. Es una operación que dados dos números reales $\{a, b\}$ devuelve otro número real, $a + b \in \mathbb{R}$.

#### Propiedades
* **Asociativa**: 
  $$a + (b + c) = (a + b) + c$$
* **Conmutativa**: 
  $$a + b = b + a$$
* **Elemento Neutro**: Existe un único número $0$ tal que:
  $$x + 0 = x$$
* **Elemento Opuesto**: Dado $x \in \mathbb{R}$, existe un número $-x$ tal que:
  $$x + (-x) = 0$$

> **Notación**: Denotaremos por $x - y = x + (-y)$.

---

### Producto
Dados dos números $a, b \in \mathbb{R}$, nos devuelve otro número real denotado por $a \cdot b$.

#### Propiedades
* **Asociativa**: 
  $$a \cdot (b \cdot c) = (a \cdot b) \cdot c$$
* **Conmutativa**: 
  $$a \cdot b = b \cdot a$$
* **Elemento Neutro**: Existe un único elemento $1$ tal que:
  $$x \cdot 1 = x$$
* **Elemento Inverso**: Dado cualquier $a \in \mathbb{R}$ con $a \neq 0$, $\exists$ un único elemento $a^{-1}$ (o $\frac{1}{a}$) tal que:
  $$a \cdot a^{-1} = 1$$
* **Distributiva**: 
  $$a \cdot (b + c) = a \cdot b + a \cdot c$$

> **Proposición**: 
> $$a \cdot 0 = 0$$
> *Demostración*: 
> $$a \cdot 0 = a \cdot (0 + 0) = a \cdot 0 + a \cdot 0 \implies a \cdot 0 = 0$$
> Como consecuencia, no existe $\frac{1}{0}$ ni $0^{-1}$.

---

## Relación de Orden

Tenemos una relación "$\le$" con las siguientes propiedades:

1. **Reflexiva**: 
   $$a \le a$$
2. **Antisimétrica**: 
   $$\left. \begin{array}{c} a \le b \\ b \le a \end{array} \right\} \implies a = b$$
3. **Transitiva**: 
   $$a \le b, \ b \le c \implies a \le c$$

> **Notación**: Escribiremos $a < b$ si $a \le b$ y $a \neq b$.

4. Si $a \le b$ y $c \in \mathbb{R} \implies a + c \le b + c$
5. Si $a \le b$ y $c \in \mathbb{R}$ con $c \ge 0 \implies a \cdot c \le b \cdot c$

### Propiedades que se deducen:
1. Si $a \le b \implies -b \le -a$
2. Si $a \le b$ y $c < 0 \implies a \cdot c \ge b \cdot c$
3. Dado $a \in \mathbb{R} \implies a \cdot a = a^2 \ge 0$

En particular, $1 > 0$, y en consecuencia, $\mathbb{R}$ tiene "muchos elementos".

> **Axioma (del Supremo / Completitud)**: 
> Dados dos subconjuntos no vacíos $A, B \subseteq \mathbb{R}$ que cumplen que $a \le b$ para todo $a \in A$ y todo $b \in B$. Entonces existe un elemento $c \in \mathbb{R}$ tal que:
> $$a \le c \le b \quad \forall a \in A, \ \forall b \in B$$

---

### Conjuntos destacados en $\mathbb{R}$
* $\mathbb{N} = \{1, 1+1, 1+1+1, 1+1+1+1, \dots\}$
* $\mathbb{Z} = \mathbb{N} \cup \{0\} \cup \{-n : n \in \mathbb{N}\}$
* $\mathbb{Q} = \left\{ \frac{p}{q} : p \in \mathbb{Z}, \ q \in \mathbb{N} \right\}$
* $\mathbb{R} \setminus \mathbb{Q} = \{x \in \mathbb{R} : x \notin \mathbb{Q}\}$ (Irracionales)

---

## Intervalos

Un subconjunto de números reales $I \subseteq \mathbb{R}$, no vacío, es un intervalo si cumple la propiedad:
$$\text{Si } x, y \in I \text{ y } z \in \mathbb{R} \text{ tal que } x \le z \le y \implies z \in I$$

Se demuestra que todo intervalo de $\mathbb{R}$ es de una de las siguientes formas:
1. $\mathbb{R}$
2. $[a, b] = \{x \in \mathbb{R} : a \le x \le b\} \quad a, b \in \mathbb{R}$
3. $[a, b) = \{x \in \mathbb{R} : a \le x < b\} \quad a, b \in \mathbb{R}$
4. $(a, b) = \{x \in \mathbb{R} : a < x < b\} \quad a, b \in \mathbb{R}$
5. $(a, +\infty) = \{x \in \mathbb{R} : a < x\} \quad a \in \mathbb{R}$

---

## Valor Absoluto

Dado $x \in \mathbb{R}$, definimos su **valor absoluto** como:
$$|x| := \begin{cases} x & \text{si } x \ge 0 \\ -x & \text{si } x < 0 \end{cases}$$

Usando el valor absoluto se define la **distancia**:
$$d(x, y) = |x - y| \quad x, y \in \mathbb{R}$$

### Propiedades
1. $|x| \ge 0$. Además, $|0| = 0$
2. $|x| < y \iff -y < x < y$
3. $|x + y| \le |x| + |y|$ (Desigualdad triangular)
4. $||x| - |y|| \le |x - y|$
5. $|x \cdot y| = |x| \cdot |y|$

---

### Ejercicio Resuelto: Inecuación

Resuelve la siguiente inecuación para $x \in \mathbb{R}, \ x \neq 1$:
$$\left| \frac{x+1}{x-1} \right| < 2$$

#### Solución:
Por la propiedad del valor absoluto, la inecuación es equivalente a:
$$-2 < \frac{x+1}{x-1} < 2$$

Debemos estudiar dos casos según el signo del denominador $x-1$:

#### **Caso 1: $x - 1 > 0 \iff x > 1$** (Intervalo $(1, +\infty)$)
Al ser el denominador positivo, podemos multiplicar sin cambiar el sentido de las desigualdades:

1. **Primera desigualdad**:
   $$\frac{x+1}{x-1} < 2 \implies x+1 < 2(x-1) \implies x+1 < 2x-2 \implies 3 < x$$
2. **Segunda desigualdad**:
   $$-2 < \frac{x+1}{x-1} \implies -2(x-1) < x+1 \implies -2x+2 < x+1 \implies 1 < 3x \implies \frac{1}{3} < x$$

Intersecando las condiciones del Caso 1 ($x > 1$, $x > 3$ y $x > \frac{1}{3}$), obtenemos el intervalo:
$$(3, +\infty)$$

---

#### **Caso 2: $x - 1 < 0 \iff x < 1$** (Intervalo $(-\infty, 1)$)
Al ser el denominador negativo, al multiplicar se invierte el sentido de las desigualdades:

1. **Primera desigualdad**:
   $$\frac{x+1}{x-1} < 2 \implies x+1 > 2(x-1) \implies x+1 > 2x-2 \implies 3 > x$$
2. **Segunda desigualdad**:
   $$-2 < \frac{x+1}{x-1} \implies -2(x-1) > x+1 \implies -2x+2 > x+1 \implies 1 > 3x \implies x < \frac{1}{3}$$

Intersecando las condiciones del Caso 2 ($x < 1$, $x < 3$ y $x < \frac{1}{3}$), obtenemos el intervalo:
$$\left(-\infty, \frac{1}{3}\right)$$

#### **Solución Final:**
El conjunto de soluciones es la unión de los dos casos:
$$\left(-\infty, \frac{1}{3}\right) \cup (3, +\infty)$$

---

## Principio de Inducción

> **Teorema**: 
> Sea $A \subseteq \mathbb{R}$ un conjunto que verifica:
> 1. $1 \in A$
> 2. Si $x \in A \implies x + 1 \in A$
> 
> Entonces $\mathbb{N} \subseteq A$.
> 
> En consecuencia, si $A \subseteq \mathbb{N}$ contiene al $1$ y cumple que si $x \in A \implies x+1 \in A$, entonces $A = \mathbb{N}$.

### Pasos para aplicar Inducción:
1. **Comprobar el caso base** ($n=1$).
2. **Hipótesis de inducción**: Suponer que la propiedad se cumple para $n$.
3. **Tesis de inducción**: Comprobar que se cumple para $n+1$.

---

### Ejercicio Resuelto: Demostración por Inducción

Demuestra que para todo $n \in \mathbb{N}$:
$$1^2 + 2^2 + 3^2 + \dots + n^2 = \frac{n(n+1)(2n+1)}{6}$$

#### Solución:

**1. Caso base ($n=1$):**
$$1^2 = \frac{1(1+1)(2\cdot 1+1)}{6} \implies 1 = \frac{1 \cdot 2 \cdot 3}{6} = 1 \quad \text{(Se cumple)}$$

**2. Hipótesis de inducción:**
Suponemos que es cierto para $n$:
$$\sum_{k=1}^{n} k^2 = \frac{n(n+1)(2n+1)}{6}$$

**3. Comprobación para $n+1$:**
Queremos demostrar que:
$$1^2 + 2^2 + 3^2 + \dots + n^2 + (n+1)^2 = \frac{(n+1)(n+2)(2n+3)}{6}$$

Sustituimos la hipótesis de inducción en el primer término de la suma:
$$\frac{n(n+1)(2n+1)}{6} + (n+1)^2$$

Sacamos factor común $(n+1)$:
$$= (n+1) \left[ \frac{n(2n+1)}{6} + (n+1) \right]$$
$$= (n+1) \left[ \frac{2n^2 + n + 6(n+1)}{6} \right]$$
$$= (n+1) \left[ \frac{2n^2 + 7n + 6}{6} \right]$$

Factorizamos el polinomio de segundo grado $2n^2 + 7n + 6$:
$$2n^2 + 7n + 6 = (n+2)(2n+3)$$

Sustituyendo de nuevo:
$$= \frac{(n+1)(n+2)(2n+3)}{6}$$

Queda demostrado que la igualdad se cumple para $n+1$. Por el principio de inducción, la fórmula es válida para todo $n \in \mathbb{N}$.
