# Tema 1: Lógica Proposicional (Sintaxis, Semántica y Consecuencia)

---

## 1. Conectivas Lógicas

Las conectivas lógicas son operadores que permiten construir fórmulas complejas a partir de fórmulas proposicionales o variables atómicas.

| Conectiva | Nombre | Expresión Formal | Lectura Natural | Condición Semántica (Valores $\{0, 1\}$) |
| :---: | :---: | :---: | :---: | :---: |
| $\lor$ | Disyunción | $\alpha \lor \beta$ | $\alpha \text{ o } \beta$ | $0$ solo si $\alpha = 0$ y $\beta = 0$ |
| $\land$ | Conjunción | $\alpha \land \beta$ | $\alpha \text{ y } \beta$ | $1$ solo si $\alpha = 1$ y $\beta = 1$ |
| $\to$ | Implicación | $\alpha \to \beta$ | $\alpha \text{ implica } \beta$ | Siempre $1$, salvo cuando $1 \to 0$ |
| $\leftrightarrow$ | Equivalencia | $\alpha \leftrightarrow \beta$ | $\alpha \text{ equivale a } \beta$ | $1$ si igual valor, $0$ si diferente |
| $\neg$ | Negación | $\neg \alpha$ | $\text{No } \alpha$ | Invierte el valor de verdad |

---

## 2. Árboles de Formación (Subfórmulas)

Un **árbol de formación** representa la estructura sintáctica abstracta de una fórmula, donde el conector principal actúa como la raíz y los subárboles corresponden a las subfórmulas inmediatas.

### Ejemplo 1: Árbol de la fórmula $\big(r \land (p \lor q)\big) \to (\neg p \lor q)$

$$\begin{array}{c}
\to \\
\swarrow \quad \searrow \\
\land \qquad\qquad \lor \\
\swarrow \ \searrow \qquad \swarrow \ \searrow \\
r \quad \lor \quad \neg \quad q \\
\swarrow \ \searrow \quad \mid \quad \\
p \quad q \quad p \quad
\end{array}$$

Descomposición explícita de subfórmulas:
* **Nivel 0 (Raíz):** $r \land (p \lor q) \to (\neg p \lor q)$
* **Nivel 1:** $r \land (p \lor q)$, $\neg p \lor q$
* **Nivel 2:** $r$, $p \lor q$, $\neg p$, $q$
* **Nivel 3 (Hojas):** $p$, $q$

---

### Ejemplo 2: Árbol de la fórmula $(p \lor \neg q) \to (\neg p \leftrightarrow q)$

$$\begin{array}{c}
\to \\
\swarrow \quad \searrow \\
\lor \qquad\qquad \leftrightarrow \\
\swarrow \ \searrow \qquad \swarrow \ \searrow \\
p \quad \neg \quad \neg \quad q \\
\mid \qquad \mid \\
q \qquad p
\end{array}$$

---

## 3. Interpretaciones y Conectivas (Álgebra sobre $\mathbb{F}_2$ / Polinomio de Gegalkine)

Dado un dominio booleano en el cuerpo finito $\mathbb{F}_2 = (\{0,1\}, +, \cdot)$ (donde la suma $+$ es la operación Módulo-2 / XOR, y el producto $\cdot$ es la conjunción / AND), las interpretaciones $I$ de las conectivas responden a las siguientes expresiones polinómicas:

$$\begin{aligned}
I(\alpha \lor \beta) &= I(\alpha) + I(\beta) + I(\alpha) \cdot I(\beta) \\
I(\alpha \land \beta) &= I(\alpha) \cdot I(\beta) \\
I(\alpha \to \beta) &= 1 + I(\alpha) + I(\alpha) \cdot I(\beta) \\
I(\alpha \leftrightarrow \beta) &= 1 + I(\alpha) + I(\beta) \\
I(\neg \alpha) &= 1 + I(\alpha)
\end{aligned}$$

> **Nota Editorial:** En la representación polinómica de Gegalkine (o Forma Normal de Zhegalkin), todas las operaciones aritméticas se reducen a expresiones multilineales módulo 2, garantizando la unicidad de representación de cualquier función booleana.

---

## 4. Clasificación Semántica de Fórmulas

Dada una fórmula bien formada $\alpha$ y una interpretación $I$:

1. **Tautología:** $\alpha$ es una tautología si para **cualquier** interpretación $I$, se satisface que:
   $$I(\alpha) = 1$$

2. **Satisfacible:** $\alpha$ es satisfacible si **existe al menos una** interpretación $I$ tal que:
   $$I(\alpha) = 1$$

3. **Refutable:** $\alpha$ es refutable si **existe al menos una** interpretación $I$ tal que:
   $$I(\alpha) = 0$$

4. **Contradicción (o Insatisfacible):** $\alpha$ es una contradicción si para **cualquier** interpretación $I$, se satisface que:
   $$I(\alpha) = 0$$

5. **Contingente:** $\alpha$ es contingente si es simultáneamente **satisfacible** y **refutable** (existen interpretaciones que la hacen verdadera y otras que la hacen falsa).

---

## 5. Métodos de Decisión Semántica

### 5.1. Polinomio de Gegalkine
Consiste en reducir la fórmula a su polinomio equivalente sobre $\mathbb{F}_2$ utilizando las propiedades algebráicas de las conectivas. 
* Si el resultado final es idénticamente igual a $1 \implies$ **Tautología**.
* Si el resultado final es idénticamente igual a $0 \implies$ **Contradicción**.

### 5.2. Tablas de Verdad
Para una fórmula compuesta por $n$ variables proposicionales distintas:
* El tamaño del espacio de interpretaciones es de $2^n$ filas.
* Se evalúa la fórmula bajo cada una de las interpretaciones posibles.

---

## 6. Equivalencia Lógica

Dos fórmulas $\alpha$ y $\beta$ son **lógicamente equivalentes** (denotado por $\alpha \equiv \beta$) si y solo si sus interpretaciones son idénticas para toda asignación de verdad:

$$I(\alpha) = I(\beta) \quad \forall I$$

Para verificar la equivalencia de dos fórmulas se puede:
1. Demostrar que sus **Polinomios de Gegalkine** son idénticos.
2. Comprobar que los valores de sus **Tablas de Verdad** coinciden para todas sus filas.

---

### 6.1. Equivalencias Fundamentales (a memorizar)

$$\begin{aligned}
\text{Doble Negación:} \quad & \alpha \equiv \neg \neg \alpha \\
\text{Definición de Doble Implicación:} \quad & \alpha \leftrightarrow \beta \equiv (\alpha \to \beta) \land (\beta \to \alpha) \\
\text{Definición de Implicación:} \quad & \alpha \to \beta \equiv \neg \alpha \lor \beta \\
\text{Leyes de De Morgan:} \quad & \neg (\alpha \land \beta) \equiv \neg \alpha \lor \neg \beta \\
& \neg (\alpha \lor \beta) \equiv \neg \alpha \land \neg \beta
\end{aligned}$$

Además, se aplican las propiedades sintácticas de **Asociatividad**, **Conmutatividad** y **Distributividad** sobre $\land$ y $\lor$.

---

## 7. Consecuencia Lógica e Implicación Semántica

### 7.1. Conjuntos de Fórmulas Satisfacibles e Insatisfacibles

Dado un conjunto de fórmulas $\Gamma = \{\alpha_1, \alpha_2, \dots, \alpha_n\}$:

* **Conjunto Satisfacible:** Un conjunto $\Gamma$ es satisfacible si existe al menos una interpretación $I$ tal que satisface simultáneamente a todas las fórmulas del conjunto:
  $$I(\alpha_1) = I(\alpha_2) = \dots = I(\alpha_n) = 1$$

> **Propiedad fundamental:** El conjunto vacío $\emptyset$ es trivialmente **satisfacible**.

* **Conjunto Insatisfacible:** Un conjunto $\Gamma$ es insatisfacible si no existe ninguna interpretación que haga verdaderas a todas sus fórmulas a la vez.

---

### 7.2. Definición de Consecuencia Lógica

Una fórmula $\alpha$ es **consecuencia lógica** de un conjunto de fórmulas $\Gamma$ (denotado por $\Gamma \models \alpha$) si para toda interpretación $I$ que hace verdaderas a todas las fórmulas de $\Gamma$, la fórmula $\alpha$ también es verdadera under $I$.

* Si $\Gamma = \emptyset$, escribimos $\models \alpha$, lo cual indica que $\alpha$ es una **tautología**.

### Teorema de Reducción a Insatisfacibilidad
La relación de consecuencia lógica $\Gamma \models \alpha$ se reduce a un problema de insatisfacibilidad:

$$\Gamma \models \alpha \iff \Gamma \cup \{\neg \alpha\} \text{ es insatisfacible}$$

---

## 8. Ejemplos Resueltos

### Ejemplo: Probar que $\{ p \lor q \to r, \, \neg r \} \models \neg q$

Por el teorema de reducción a insatisfacibilidad, la afirmación anterior es equivalente a probar que el conjunto:

$$\{ p \lor q \to r, \, \neg r, \, \neg \neg q \} \equiv \{ p \lor q \to r, \, \neg r, \, q \}$$

es **insatisfacible**.

---

#### Método 1: Tabla de Verdad
Se evalúa la conjunción de las premisas junto con la negación de la conclusión:

$$(p \lor q \to r) \land \neg r \land q$$

Al construir la tabla de verdad para las 8 combinaciones de $p, q, r$, se verifica que la fórmula da $0$ bajo toda interpretación. Por lo tanto, es una **contradicción** y el conjunto es insatisfacible.

---

#### Método 2: Análisis de Modelos (Álgebra Semántica)
Buscamos si existe una interpretación $I$ tal que satisfaga todas las fórmulas del conjunto:

$$\begin{cases}
(1) \quad I(p \lor q \to r) = 1 \\
(2) \quad I(\neg r) = 1 \implies I(r) = 0 \\
(3) \quad I(q) = 1
\end{cases}$$

Sustituimos $I(q) = 1$ e $I(r) = 0$ en la ecuación (1):

$$I(p \lor q) = I(p) + I(q) + I(p) \cdot I(q) = I(p) + 1 + I(p) = 1$$

Evaluamos la implicación $I(p \lor q \to r)$:

$$I(p \lor q \to r) = 1 + I(p \lor q) + I(p \lor q) \cdot I(r) = 1 + 1 + 1 \cdot 0 = 0$$

Esto contradice el supuesto de que $I(p \lor q \to r) = 1$.  
Dado que no existe ninguna interpretación posible, el conjunto es **insatisfacible**, y por tanto queda probado que:

$$\{ p \lor q \to r, \, \neg r \} \models \neg q$$

---

## 9. Teorema de la Deducción

El **Teorema de la Deducción** establece que la relación entre la consecuencia lógica con premisas y la implicación en la fórmula formal son equivalentes:

$$\Gamma \models \alpha \to \beta \iff \Gamma \cup \{\alpha\} \models \beta$$

---

### Ejemplo de Aplicación (Demostración de Tautologías)

**Problema Tipo:** Demostrar que la fórmula $(\neg \alpha \to \neg \beta) \to (\beta \to \alpha)$ es una tautología.

1. Aplicar el Teorema de la Deducción para convertir las implicaciones principales en hipótesis:
   $$\models (\neg \alpha \to \neg \beta) \to (\beta \to \alpha) \iff \{\neg \alpha \to \neg \beta, \, \beta\} \models \alpha$$
2. Trasladar la conclusión negada al conjunto de premisas (Reducción al absurdo / Insatisfacibilidad):
   $$\{\neg \alpha \to \neg \beta, \, \beta, \, \neg \alpha\} \text{ debe ser insatisfacible}$$
3. Comprobar la insatisfacibilidad mediante tablas de verdad o simplificación polinómica.