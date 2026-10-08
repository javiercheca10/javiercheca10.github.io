# Álgebra Lineal y Estructuras Matemáticas

## Tipos de ejercicios

---

## Tema 1

### Potencia grande

1. **Reducir base**.
2. **Comprobar si el exponente es primo**.
3. **$\text{Exp} - 1 = 1$** *(Aplicar Pequeño Teorema de Fermat / Teorema de Euler)*.
4. **Propiedades de las potencias**.

---

### Inverso

1. $[\text{Num}] \cdot [y] = [1] + [\text{Base}] \cdot [k]$
2. **Ecuación diofántica** $\longrightarrow \text{Base} \cdot k + \text{Num} \cdot y = 1$
3. **Algoritmo Extendido de Euclides (AEE)**

#### Ejemplo: $\operatorname{mcd}(7585, 1342)$

| $i$ | $a$ | $b$ | $r$ | $q$ | $k$ | $y$ | Operaciones de actualización |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **0** | — | — | — | — | $0$ | $1$ | |
| **1** | $7585$ | $1342$ | $625$ | $5$ | $1$ | $-5$ | $0 - 1 \cdot 5 = -5$ |
| **2** | $1342$ | $625$ | $142$ | $2$ | $-2$ | $11$ | $1 - (-5 \cdot 2) = 11$ |
| **3** | $625$ | $142$ | $57$ | $4$ | $9$ | $-49$ | |
| **4** | $142$ | $57$ | $28$ | $2$ | $-20$ | $109$ | |
| **5** | $57$ | $28$ | $1$ | $2$ | $49$ | $-267$ | |

4. **Condición necesaria**: $\operatorname{mcd}(\text{Num}, \text{Base}) = 1$
5. **Resultado**: la $y$

---

### Congruencias

#### Ejemplo: $17x \equiv 45 \pmod{42}$

1. $\operatorname{mcd}(17, 42)$
2. Si el $\operatorname{mcd}$ divide a $45$, hay solución.
3. Cálculo del inverso: $[17]^{-1}$
4. Despejar $x$.

---

### Diofántica: $ax + by = c$

1. **Tiene solución** si $\operatorname{mcd}(a, b) \mid c$.
2. **Calcular solución particular con AEE**:
   - 2.1. Calcular con AEE los coeficientes $k'$ e $y'$ (o $x'$) para el caso $= 1$.
   - 2.2. Multiplicamos la ecuación por el término independiente $c$.
3. **Escribir la solución general**:
   $$
   \left.\begin{aligned}
   x &= x_0 + \frac{b}{\operatorname{mcd}(a, b)} n \\
   y &= y_0 - \frac{a}{\operatorname{mcd}(a, b)} n
   \end{aligned}\right\} \quad n \in \mathbb{Z}
   $$

---

### Diofántica con restricción en $c$

1. Calcular $\operatorname{mcd}(a, b)$.
2. Averiguar los múltiplos del $\operatorname{mcd}$ que están dentro del intervalo dado.

---

### Sistema de congruencias

$$
\begin{cases}
x \equiv a \pmod{m_1} \\
x \equiv b \pmod{m_2}
\end{cases}
$$

1. **TCR (Teorema Chino del Resto)**: Si $\operatorname{mcd}(m_1, m_2) = 1$, tiene solución.
2. **Expresar soluciones de una de las ecuaciones**: 
   $$x = a + m_1 k$$
3. **Sustituir** en la segunda ecuación.
4. **Resolver la congruencia** resultante para $k$.

---

## Tema 3

### Sistemas de ecuaciones

1. Escribir la matriz del sistema y expresarlo en $\mathbb{Z}_n$.
2. Aplicar reducción por **Hermite por columnas**.

---

### Teorema para calcular una matriz $P$

$$
A \sim_F B \iff \exists P \text{ regular tal que } PA = B
$$

$$
\Downarrow
$$

$$
H_A = H_B \longrightarrow P_1 A = P_2 B
$$

---

### Discutir según valores

1. Calcular el rango: $\operatorname{rg}(A)$, $\operatorname{rg}(A|B)$.
2. Clasificación:
   - Si $\operatorname{rg} = n^\circ \text{ incógnitas} \longrightarrow \mathbf{C.D.}$ (Compatible Determinado).
   - Si $\operatorname{rg} < n^\circ \text{ incógnitas} \longrightarrow \mathbf{C.I.}$ (Compatible Indeterminado).

---

## Tema 4

### $N^\circ$ de vectores independientes en un conjunto

1. Formar una matriz colocando los vectores como columnas.
2. El rango ($\operatorname{rg}$) de la matriz es el número de vectores linealmente independientes.