# Bloque 2: Teoría de Números, Algoritmo de Euclides Extendido, Inversos Modulares e Inducción Matemática

En este documento se presentan las soluciones detalladas a una selección de ejercicios fundamentales basados en la obra *Discrete Mathematics and Its Applications* de Kenneth H. Rosen, cubriendo temas críticos de la teoría de números, aritmética modular y técnicas de demostración.

---

### Ejercicio 9: Relaciones de Recurrencia
**Referencia:** *Sección 5.2, Ejercicio 13*

**Enunciado:** Suponga que $a_n = a_{n-1} - 5$ para $n = 1, 2, \dots$. Encuentre una fórmula explícita para $a_n$.

**Solución:**
Calculamos los primeros términos:
- $a_1 = a_0 - 5$
- $a_2 = a_1 - 5 = (a_0 - 5) - 5 = a_0 - 10$
- $a_3 = a_2 - 5 = (a_0 - 10) - 5 = a_0 - 15$

La fórmula general propuesta es $a_n = a_0 - 5n$.

**Demostración por Inducción Matemática:**
1. **Caso base ($n=1$):** $a_1 = a_0 - 5(1) = a_0 - 5$. Se cumple.
2. **Paso inductivo:** Suponemos cierto para $n=k$, es decir, $a_k = a_0 - 5k$. Para $n=k+1$:
   $$a_{k+1} = a_k - 5 = (a_0 - 5k) - 5 = a_0 - 5(k+1)$$
La fórmula queda verificada para todo $n \in \mathbb{Z}^+$.

---

### Ejercicio 10: Algoritmo de Euclides Extendido
**Referencia:** *Sección 4.3, Ejercicio 41*

**Enunciado:** Utilice el Algoritmo de Euclides Extendido para expresar $\gcd(26, 91)$ como una combinación lineal de $26$ y $91$.

**Solución:**
1. **Algoritmo de Euclides:**
   - $91 = 3(26) + 13$
   - $26 = 2(13) + 0$
   Por lo tanto, $\gcd(26, 91) = 13$.

2. **Sustitución regresiva (Backward substitution):**
   De la primera ecuación, despejamos el residuo:
   $$13 = 91 - 3(26)$$
   Los coeficientes de Bézout son $x = -3$ y $y = 1$, tal que $13 = 26(-3) + 91(1)$.

---

### Ejercicio 11: Inversos Modulares
**Referencia:** *Sección 4.4, Ejercicio 6c, 6d*

**Enunciado:** Encuentre el inverso de $a \pmod m$ para los pares: c) $a=144, m=233$; d) $a=200, m=1001$.

**Solución (c):**
Aplicamos el algoritmo de Euclides para verificar que $\gcd(144, 233) = 1$:
$233 = 1(144) + 89 \Rightarrow 89 = 233 - 1(144)$
$144 = 1(89) + 55 \Rightarrow 55 = 144 - 1(89)$
... (procediendo hasta llegar al resto 1) ...
Tras la sustitución regresiva, obtenemos la identidad: $1 = 34(144) - 21(233)$.
Por lo tanto, el inverso de $144 \pmod{233}$ es $34$.

**Solución (d):**
$1001 = 5(200) + 1 \Rightarrow 1 = 1001 - 5(200)$.
En $\pmod{1001}$: $200^{-1} \equiv -5 \equiv 996 \pmod{1001}$.

---

### Ejercicio 12: Pequeño Teorema de Fermat
**Referencia:** *Sección 4.4, Ejercicio 15*

**Enunciado:** Evalúe $9^{200} \pmod{19}$.

**Solución:**
Por el Teorema de Fermat, como $19$ es primo y $\gcd(9, 19) = 1$:
$$9^{19-1} \equiv 9^{18} \equiv 1 \pmod{19}$$
Reducimos el exponente $200$ módulo $18$: $200 = 11 \cdot 18 + 2$.
$$9^{200} = (9^{18})^{11} \cdot 9^2 \equiv 1^{11} \cdot 81 \equiv 81 \pmod{19}$$
Como $81 = 4 \cdot 19 + 5$, entonces $9^{200} \equiv 5 \pmod{19}$.

---

### Ejercicio 13: Inducción Matemática
**Referencia:** *Sección 5.1, Ejercicio 15*

**Enunciado:** Demuestre que $1\cdot2 + 2\cdot3 + \dots + n(n+1) = \frac{n(n+1)(n+2)}{3}$.

**Solución:**
1. **Caso base ($n=1$):** $1(2) = 2$. Lado derecho: $\frac{1(2)(3)}{3} = 2$. Se cumple.
2. **Hipótesis inductiva:** Asumimos $\sum_{i=1}^k i(i+1) = \frac{k(k+1)(k+2)}{3}$.
3. **Paso inductivo:** Debemos demostrar para $k+1$:
   $$\frac{k(k+1)(k+2)}{3} + (k+1)(k+2) = \frac{(k+1)(k+2)(k+3)}{3}$$
   Factorizando $(k+1)(k+2)$:
   $$\frac{(k+1)(k+2)}{3} \cdot [k + 3] = \frac{(k+1)(k+2)(k+3)}{3}$$
Queda demostrado.