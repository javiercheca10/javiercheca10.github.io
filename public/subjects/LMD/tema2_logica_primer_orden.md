# Tema 2: Lógica de Primer Orden (Estructuras, Modelos, Prenexas y Skolem)

---

## Lenguajes de Primer Orden

### Tipos de sujeto

* **Totalmente determinado por un identificador propio:** Ej. *Nombre*.
  * **Símbolos de constante:** $(a, b, c, \dots)$
* **Genérico no determinado:** Ej. *Todos los hombres*.
  * **Símbolos de variable:** $(x, y, z, \dots)$
* **Identificado mediante otro objeto:** Ej. *El tío de Sócrates*.
  * **Símbolos de función:** $(f, g, h, \dots)$
* **Para los predicados:**
  * **Símbolos de predicado:** $(A, B, C, \dots)$

---

### Fórmula

Sucesión de estos símbolos junto con las conectivas y cuantificadores.

---

### Fórmulas atómicas

Símbolo de predicado aplicado a términos. 

**Ejemplos:**
* $P(a,b)$
* $Q(x, c, f(b))$

---

### Fórmulas del lenguaje

* Toda fórmula atómica es una fórmula.
* Si $\alpha$ y $\beta$ son fórmulas, también lo son:
  $$\alpha \lor \beta, \quad \alpha \to \beta, \quad \dots$$
* Si $\alpha$ es una fórmula y $x$ es un símbolo de variable, entonces son fórmulas:
  $$\forall x \, \alpha \quad \text{y} \quad \exists x \, \alpha$$

---

## Radio de Acción de un Cuantificador

El radio de acción será la subfórmula $\beta$ a la que le afecte el cuantificador.

**Ejemplo:**
Dada la fórmula $\alpha$:
$$\underbrace{\exists y \, (R(g(a,y)) \to (P(g(a,b), x) \land \neg (\underbrace{\forall x \, Q(x,x,x)}_{\text{Radio de } \forall x})))}_{\text{Radio de } \exists y}$$

* El alcance/radio de acción de $\exists y$ es toda la fórmula $\alpha$.
* El alcance/radio de acción de $\forall x$ es la subfórmula $Q(x,x,x)$.

---

## Variables Ligadas y Libres

Una variable es **ligada** si está en el radio de acción de un cuantificador; si no, es **libre**.

---

## Sentencia

Una fórmula $\alpha$ es una **sentencia** (o fórmula cerrada) cuando no contiene ninguna aparición de variable libre.

---

## Estructuras

Tenemos un lenguaje $\mathcal{L}(C, V, F, R)$ compuesto por:
* Constantes: $C = \{a, b\}$
* Variables: $V = \{x, y, z, \dots\}$
* Funciones: $F = \{s^1, m^2\}$ *(donde los superíndices denotan la aridad)*
* Relaciones / Predicados: $R = \{P^1, Pr^1, M^2, Eq^2\}$

### Estructura de Ejemplo ($\mathcal{E}$)

1. **Dominio:** $D = \mathbb{N}$
2. **Constantes:** $a = 0$, $b = 1$
3. **Funciones:**
   * $s(x) = x + 1$
   * $m(x,y) = x \cdot y$
4. **Predicados:**
   * $P(x) \equiv x \text{ es par} \quad \Longrightarrow \quad P(x) = \begin{cases} 1 & \text{si } x \text{ es par} \\ 0 & \text{si } x \text{ es impar} \end{cases}$
   * $M(x,y) = \begin{cases} 1 & \text{si } x > y \\ 0 & \text{si } x \le y \end{cases}$
   * $Pr(x) = \begin{cases} 1 & \text{si } x \text{ es primo} \\ 0 & \text{si } x \text{ no es primo} \end{cases}$
   * $Eq(x,y) = \begin{cases} 1 & \text{si } x = y \\ 0 & \text{si } x \neq y \end{cases}$

---

## Valoraciones

* Si $a \in C$, entonces $v(a) = a^{\mathcal{E}}$ (su interpretación en la estructura).
* Si $x \in V$, entonces $v(x)$ ya está definido dentro del dominio.
* La valoración de una función aplicada a términos se define recursivamente:
  $$v(f(t_1, t_2, \dots, t_n)) = f(v(t_1), v(t_2), \dots, v(t_n))$$

**Ejemplo:**
Tomando la estructura ejemplo anterior, si fijamos las valoraciones $v(x) = 2$ y $v(y) = 5$:

$$m(v(m(s(a), x)), v(s(y))) = m(m(v(s(a)), v(x)), s(v(y)))$$

Sustituyendo los valores:
* $v(s(a)) = s(0) = 1$
* $v(x) = 2$
* $s(v(y)) = s(5) = 6$

$$= m(m(1, 2), 6) = m(2, 6) = 12$$

---

## Interpretación

* Una **interpretación** $I$ es un par $(\mathcal{E}, v)$, donde $\mathcal{E}$ es una estructura y $v$ es una valoración.
* Denotaremos $I_{\mathcal{E}}^v(\alpha)$ (o simplemente $I^v(\alpha)$) al valor de verdad de la fórmula $\alpha$.
* El valor de verdad de una fórmula atómica $\alpha = P(t_1, \dots, t_n)$ bajo la interpretación $I$ es:
  $$I(\alpha) = P(v(t_1), v(t_2), \dots, v(t_n))$$
* **Modificación de valoraciones:** Se denota por $v_{x|e}$ a la valoración igual a $v$ salvo para la variable $x$, a la cual se asigna el elemento $e \in D$:
  $$v_{x|e}(y) = \begin{cases} v(y) & \text{si } y \neq x \\ e & \text{si } y = x \end{cases}$$

---

## Interpretaciones y Conectivas

1. $I^v(\alpha \lor \beta) = I^v(\alpha) + I^v(\beta) + I^v(\alpha) \cdot I^v(\beta)$
2. $I^v(\alpha \land \beta) = I^v(\alpha) \cdot I^v(\beta)$
3. $I^v(\alpha \to \beta) = 1 + I^v(\alpha) + I^v(\alpha) \cdot I^v(\beta)$
4. $I^v(\alpha \leftrightarrow \beta) = 1 + I^v(\alpha) + I^v(\beta)$
5. $I^v(\neg \alpha) = 1 + I^v(\alpha)$
6. $I^v(\forall x \, \alpha) = \begin{cases} 1 & \text{si para cualquier elemento } e \in D \text{ se tiene que } I^{v_{x|e}}(\alpha) = 1 \\ 0 & \text{en otro caso} \end{cases}$
7. $I^v(\exists x \, \alpha) = \begin{cases} 1 & \text{si existe algún elemento } e \in D \text{ para el que } I^{v_{x|e}}(\alpha) = 1 \\ 0 & \text{en otro caso} \end{cases}$

---

## Clasificación Semántica de las Fórmulas

* Se dice que $I^v = (\mathcal{E}, v)$ es un **modelo** para la fórmula $\alpha$ si:
  $$I^v(\alpha) = 1$$

Dada una fórmula $\alpha$ y una estructura $\mathcal{E}$:
* $\alpha$ es **válida en $\mathcal{E}$** si para cualquier valoración $v$ se tiene $I^v(\alpha) = 1$.
* $\alpha$ es **satisfacible en $\mathcal{E}$** si hay una valoración $v$ tal que $I^v(\alpha) = 1$.
* $\alpha$ es **refutable en $\mathcal{E}$** si hay una valoración $v$ tal que $I^v(\alpha) = 0$.
* $\alpha$ es **no válida en $\mathcal{E}$** si para cualquier valoración $v$ se tiene $I^v(\alpha) = 0$.

De manera general (considerando la clase de todas las estructuras):
* $\alpha$ es **universalmente válida** (tautología) si es válida para cualquier estructura.
* $\alpha$ es **satisfacible** si hay alguna estructura en la que sea satisfacible.
* $\alpha$ es **refutable** si hay alguna estructura en la que sea refutable.
* $\alpha$ es una **contradicción** (insatisfacible) si es no válida para cualquier estructura.

---

### Satisfacibilidad de Conjuntos de Fórmulas

Un conjunto de fórmulas $\Gamma = \{\gamma_1, \gamma_2, \dots, \gamma_n\}$ es **satisfacible** si existe una interpretación $I^v = (\mathcal{E}, v)$ tal que:
$$I^v(\gamma_1) = I^v(\gamma_2) = \dots = I^v(\gamma_n) = 1$$
En caso contrario, se dice que es **insatisfacible**.

---

## Implicación Semántica (Consecuencia Lógica)

Una fórmula $\alpha$ es **consecuencia lógica** de un conjunto de fórmulas $\Gamma$ si para cualquier interpretación en la que todas las proposiciones de $\Gamma$ sean verdaderas, $\alpha$ también lo es.

Escribiremos:
$$\Gamma \models \alpha$$

---

### Propiedades y Equivalencias

Sea $\Gamma$ un conjunto de fórmulas y $\alpha$ una fórmula. Son equivalentes:
1. $\Gamma \models \alpha$
2. $\Gamma \cup \{\neg \alpha\}$ es **insatisfacible**

---

### Teorema de la Deducción

1. $\Gamma \models \alpha \to \beta$
2. $\Gamma \cup \{\alpha\} \models \beta$

> **Nota:** Cuando el conjunto $\Gamma$ sea vacío ($\emptyset$), la expresión $\models \alpha$ significa que $\alpha$ es **universalmente válida**.

> **Referencia bibliográfica:** *¡ Revisar página 150 del libro de texto !*

---

## Formas Normales

**Objetivo:** Obtener un método algorítmico para determinar si un conjunto de fórmulas es o no satisfacible.

---

### Forma Normal Prenexa

Una fórmula $\alpha$ está en **Forma Normal Prenexa** si es de la forma:
$$Q_1 x_1 \, Q_2 x_2 \, \dots \, Q_n x_n \, \beta$$

donde cada $Q_i$ es un cuantificador ($\forall$ o $\exists$) y $\beta$ es una fórmula **sin cuantificadores** (matriz).

**Ejemplos:**
* $Q(a)$
* $\forall x \, (P(x) \lor Q(x,b))$
* $\forall x \, \exists y \, \forall z \, Q(x,y,z)$

---

### Forma Normal de Skolem

Una fórmula $\alpha$ está en **Forma Normal de Skolem** si está en forma prenexa y **no contiene cuantificadores existenciales** ($\exists$):

$$\alpha = \forall x_1 \, \forall x_2 \, \dots \, \forall x_n \, \beta$$

donde $\beta$ es una fórmula abierta (sin cuantificadores).