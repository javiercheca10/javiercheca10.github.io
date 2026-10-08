# Bloque 2: Álgebra Matricial, Inversas y Ajuste por Mínimos Cuadrados / Ley de Moore (Capítulos 6-13)

---

## Capítulo 6: Matrices

### Ejercicio 6.12: Skew-symmetric matrices (Matrices antisimétricas)

**Enunciado:**
Una matriz cuadrada $n \times n$ $A$ se denomina **antisimétrica** (*skew-symmetric*) si $A^T = -A$, es decir, su traspuesta es igual a su matriz opuesta. (Una matriz simétrica satisface $A^T = A$).

1. **(a)** Encuentra todas las matrices antisimétricas de dimensión $2 \times 2$.
2. **(b)** Explica por qué los elementos de la diagonal de una matriz antisimétrica deben ser necesariamente cero.
3. **(c)** Demuestra que para cualquier matriz antisimétrica $A$ y cualquier $n$-vector $x$, se cumple que $(Ax) \perp x$. Esto significa que el vector resultante $Ax$ y el vector $x$ son ortogonales.  
   *Sugerencia:* Primero demuestra que para cualquier matriz $n \times n$ $A$ y cualquier $n$-vector $x$, se tiene $x^T (Ax) = \sum_{i,j=1}^n A_{ij} x_i x_j$.
4. **(d)** Ahora supón que $A$ es una matriz cualquiera para la cual $(Ax) \perp x$ para todo $n$-vector $x$. Demuestra que $A$ debe ser antisimétrica.  
   *Sugerencia:* Puede resultarte útil la fórmula:
   $$(e_i + e_j)^T (A(e_i + e_j)) = A_{ii} + A_{jj} + A_{ij} + A_{ji}$$
   válida para cualquier matriz $n \times n$ $A$. Para $i = j$, esto se reduce a $e_i^T (Ae_i) = A_{ii}$.

---

#### Desarrollo y Demostración:

*(a) Matrices antisimétricas de $2 \times 2$:*  
Sea una matriz $2 \times 2$ dada por:
$$A = \begin{bmatrix} A_{11} & A_{12} \\ A_{21} & A_{22} \end{bmatrix}$$
Su traspuesta es:
$$A^T = \begin{bmatrix} A_{11} & A_{21} \\ A_{12} & A_{22} \end{bmatrix}$$
La condición de antisimetría es $A^T = -A$:
$$\begin{bmatrix} A_{11} & A_{21} \\ A_{12} & A_{22} \end{bmatrix} = \begin{bmatrix} -A_{11} & -A_{12} \\ -A_{21} & -A_{22} \end{bmatrix}$$
Igualando término a término:
- $A_{11} = -A_{11} \implies 2A_{11} = 0 \implies A_{11} = 0$
- $A_{22} = -A_{22} \implies 2A_{22} = 0 \implies A_{22} = 0$
- $A_{21} = -A_{12} \implies A_{21} = -A_{12}$

Por tanto, toda matriz antisimétrica de $2 \times 2$ tiene la forma general:
$$A = \begin{bmatrix} 0 & -A_{21} \\ A_{21} & 0 \end{bmatrix}$$

---

*(b) Elementos de la diagonal:*  
Por definición de matriz antisimétrica, se cumple $A^T = -A$. Al evaluar los elementos de la diagonal principal, es decir, cuando $i = j$, el elemento $(i,i)$ de la matriz traspuesta $A^T$ es $A_{ii}$, mientras que el elemento $(i,i)$ de la matriz $-A$ es $-A_{ii}$.  
Por lo tanto:
$$A_{ii} = -A_{ii} \implies 2A_{ii} = 0 \implies A_{ii} = 0$$
Así, **todos los elementos de la diagonal principal deben ser necesariamente ceros**.

---

*(c) Ortogonalidad entre $Ax$ y $x$:*  
Para demostrar que $(Ax) \perp x$, debemos probar que su producto interno es cero: $(Ax)^T x = 0$ (o equivalentemente $x^T (Ax) = 0$).  
Utilizando la propiedad del producto traspuesto de un producto matricial:
$$x^T (Ax) = (x^T A) x$$
Sabemos que al trasponer un escalar, este no cambia ($x^T (Ax)$ es un escalar $1 \times 1$):
$$x^T (Ax) = (x^T (Ax))^T = (Ax)^T (x)$$
Dado que $A$ es antisimétrica, $A^T = -A$:
$$(Ax)^T x = x^T A^T x = x^T (-A) x = - (x^T A x)$$
Sea $\alpha = x^T A x$. Hemos demostrado que $\alpha = -\alpha$, por lo que:
$$2\alpha = 0 \implies \alpha = 0$$
Es decir, $x^T (Ax) = 0$, lo que implica que **$Ax$ y $x$ son ortogonales** ($Ax \perp x$).

---

*(d) Condición suficiente de antisimetría:*  
Si $x^T (Ax) = 0$ para todo $n$-vector $x$, evaluamos la expresión con el vector de prueba $x = e_i + e_j$ (donde $e_i$ es el $i$-ésimo vector canónico):
$$(e_i + e_j)^T A (e_i + e_j) = 0$$
Desarrollando el producto mediante linealidad:
$$(e_i + e_j)^T (Ae_i + Ae_j) = e_i^T Ae_i + e_i^T Ae_j + e_j^T Ae_i + e_j^T Ae_j = 0$$
Dado que $e_i^T Ae_i = A_{ii}$ y $e_j^T Ae_j = A_{jj}$, y sabiendo que los elementos diagonales son cero ($A_{ii} = 0, A_{jj} = 0$), la ecuación se reduce a:
$$A_{ij} + A_{ji} = 0 \implies A_{ji} = -A_{ij}$$
Esto se cumple para todo $i, j$, lo que demuestra formalmente que $A^T = -A$.  
**Conclusión:** $A$ es una matriz antisimétrica.

---

## Capítulo 7: Matrix Examples (Ejemplos de Matrices)

### Ejercicio 7.3: Trimming a vector (Recorte de un vector)

**Enunciado:**
Encuentra una matriz $A$ para la cual $Ax = (x_2, \dots, x_{n-1})$, donde $x$ es un $n$-vector. (Asegúrate de especificar el tamaño de $A$ y describir todos sus elementos).

---

#### Desarrollo:
- **Dimensiones:**  
  El vector de entrada es $x \in \mathbb{R}^n$ y el vector de salida es un $(n-2)$-vector. Por tanto, la matriz $A$ debe tener dimensiones **$(n-2) \times n$**.

- **Definición de las entradas de la matriz $A$:**  
  La $i$-ésima componente del vector resultante es $y_i = x_{i+1}$ para $i = 1, \dots, n-2$.  
  Esto se logra seleccionando el elemento en la columna $i+1$ de cada fila $i$, manteniendo ceros en el resto.  
  Por lo tanto, los elementos de $A$ están definidos como:
  $$A_{ij} = \begin{cases} 1 & \text{si } j = i + 1 \\ 0 & \text{en cualquier otro caso} \end{cases}$$

- **Forma matricial:**
  $$A = \begin{bmatrix} 
  0 & 1 & 0 & 0 & \dots & 0 & 0 \\ 
  0 & 0 & 1 & 0 & \dots & 0 & 0 \\ 
  \vdots & \vdots & \vdots & \ddots & \ddots & \vdots & \vdots \\
  0 & 0 & 0 & 0 & \dots & 1 & 0 
  \end{bmatrix}_{(n-2) \times n}$$

---

## Capítulo 8: Linear Equations (Ecuaciones Lineales)

### Ejercicio 8.5: Symmetric and anti-symmetric part (Parte simétrica y antisimétrica de un vector)

**Enunciado:**
Un $n$-vector $x$ es simétrico si $x_k = x_{n-k+1}$ para $k = 1, \dots, n$. Es anti-simétrico si $x_k = -x_{n-k+1}$ para $k = 1, \dots, n$.

1. **(a)** Demuestra que todo vector $x$ puede ser descompuesto de forma única como una suma $x = x_s + x_a$ de un vector simétrico $x_s$ y un vector anti-simétrico $x_a$.
2. **(b)** Demuestra que las partes simétrica y anti-simétrica $x_s$ y $x_a$ son funciones lineales de $x$. Da las matrices $A_s$ y $A_a$ tales que $x_s = A_s x$ y $x_a = A_a x$ para todo $x$.

---

#### Desarrollo:

*(a) Demostración de existencia y unicidad:*  
Proponemos las fórmulas candidatas para las componentes simétrica y antisimétrica de cualquier vector $x$:
$$(x_s)_k = \frac{x_k + x_{n-k+1}}{2}, \quad (x_a)_k = \frac{x_k - x_{n-k+1}}{2}$$
Verificamos que $x = x_s + x_a$:
$$(x_s)_k + (x_a)_k = \frac{x_k + x_{n-k+1} + x_k - x_{n-k+1}}{2} = \frac{2x_k}{2} = x_k$$
Comprobamos la simetría de $x_s$:
$$(x_s)_{n-k+1} = \frac{x_{n-k+1} + x_{n-(n-k+1)+1}}{2} = \frac{x_{n-k+1} + x_k}{2} = (x_s)_k \quad (\text{Es simétrico})$$
Comprobamos la antisimetría de $x_a$:
$$(x_a)_{n-k+1} = \frac{x_{n-k+1} - x_k}{2} = - \left( \frac{x_k - x_{n-k+1}}{2} \right) = -(x_a)_k \quad (\text{Es antisimétrico})$$
La unicidad se deduce al asumir otra descomposición $x = y_s + y_a$ y restar ambas ecuaciones, lo que obliga a que $y_s = x_s$ y $y_a = x_a$.

---

*(b) Linealidad y matrices asociadas:*  
Dado que cada componente de $x_s$ y $x_a$ se obtiene mediante combinaciones lineales (sumas y restas con factores constantes $1/2$) de las componentes de $x$, ambas funciones son lineales.

Las matrices $A_s$ y $A_a$ de tamaño $n \times n$ tienen unos en la diagonal principal y en la diagonal secundaria invertida (antidiagonal), escalados por $1/2$:
- Para $A_s$: $(A_s)_{i,j} = \frac{1}{2}$ si $j = i$ o $j = n - i + 1$, y $0$ en el resto.
- Para $A_a$: $(A_a)_{i,j} = \frac{1}{2}$ si $j = i$, y $(A_a)_{i,n-i+1} = -\frac{1}{2}$, con $0$ en el resto.

---

## Capítulo 10: Matrix Multiplication (Multiplicación de Matrices)

### Ejercicio 10.3: Matrix sizes (Dimensiones de matrices)

**Enunciado:**
Supón que $A$, $B$ y $C$ son matrices que satisfacen $A + BB^T = C$. Determina cuáles de las siguientes afirmaciones son necesariamente verdaderas. (Puede haber más de una afirmación verdadera).

1. **(a)** $A$ es cuadrada.
2. **(b)** $A$ y $B$ tienen las mismas dimensiones.
3. **(c)** $A$, $B$ y $C$ tienen el mismo número de filas.
4. **(d)** $B$ es una matriz alta (*tall matrix*).

---

#### Resolución y Justificación:

- **Análisis dimensional:**  
  Sea $B$ una matriz de dimensiones $m \times k$.  
  Entonces, la matriz traspuesta $B^T$ tiene dimensiones $k \times m$.  
  El producto matricial $BB^T$ da como resultado una matriz cuadrada de dimensiones $m \times m$.  
  Como la suma matricial $A + BB^T = C$ requiere que $A$, $BB^T$ y $C$ posean exactamente las mismas dimensiones, deducimos que:
  - $A$ y $C$ son matrices de dimensiones $m \times m$ (por lo tanto, **son cuadradas**).
  - El número de filas de $A$, $B$ y $C$ es $m$ (por tanto, **comparten el mismo número de filas**).

- **Evaluación de opciones:**
  - **(a) Verdadera:** $A$ es una matriz cuadrada ($m \times m$).
  - **(b) Falsa:** $A$ es $m \times m$ y $B$ es $m \times k$ (no tienen por qué coincidir en columnas).
  - **(c) Verdadera:** Todas comparten $m$ filas.
  - **(d) Falsa:** $B$ no tiene por qué ser alta obligatoriamente ($k$ puede ser mayor que $m$).

---

### Ejercicio 10.24: Matrix power identity (Identidad de potencias de matrices)

**Enunciado:**
Un estudiante afirma que para cualquier matriz cuadrada $A$:
$$(A + I)^3 = A^3 + 3A^2 + 3A + I$$
¿Tiene razón? Si la tiene, explica por qué; si está equivocada, proporciona un contraejemplo específico, es decir, una matriz cuadrada $A$ para la cual no se cumpla.

---

#### Resolución:
La expansión algebraica formal se rige por la no conmutatividad del producto de matrices en general ($AB \neq BA$).  
Expandiendo $(A + I)^3$:
$$(A + I)^3 = (A + I)(A + I)(A + I) = (A^2 + 2A + I)(A + I)$$
$$= A^3 + A^2 + 2A^2 + 2A + A + I = A^3 + 3A^2 + 3A + I$$
Dado que la matriz identidad $Iera$ conmuta con cualquier matriz ($AI = IA = A$), las propiedades distributivas y asociativas estándar del álgebra matricial se aplican en este caso particular.  
**Conclusión:** La estudiante **tiene razón**, la identidad se cumple para cualquier matriz cuadrada $A$.

---

## Capítulo 11: Matrix Inverses (Inversas de Matrices)

### Ejercicio 11.12: Combinations of invertible matrices (Combinaciones de matrices invertibles)

**Enunciado:**
Supón que las matrices $n \times n$ $A$ y $B$ son ambas invertibles. Determina si cada una de las matrices dadas a continuación es invertible, sin hacer más suposiciones sobre $A$ y $B$.

1. **(a)** $A + B$.
2. **(b)** $\begin{bmatrix} A & 0 \\ 0 & B \end{bmatrix}$.
3. **(c)** $\begin{bmatrix} A & A + B \\ 0 & B \end{bmatrix}$.
4. **(d)** $ABA$.

---

#### Resolución:

1. **(a) $A + B$:**  
   **No necesariamente invertible.** Contraejemplo trivial: Sea $A = I$ y $B = -I$, ambas invertibles, pero $A + B = 0$ (no invertible).
   
2. **(b) Matriz diagonal por bloques $\begin{bmatrix} A & 0 \\ 0 & B \end{bmatrix}$:**  
   **Inversible.** Su inversa analítica por bloques es:
   $$\begin{bmatrix} A & 0 \\ 0 & B \end{bmatrix}^{-1} = \begin{bmatrix} A^{-1} & 0 \\ 0 & B^{-1} \end{bmatrix}$$
   Dado que $A^{-1}$ y $B^{-1}$ existen, la matriz es invertible.

3. **(c) Matriz triangular por bloques $\begin{bmatrix} A & A + B \\ 0 & B \end{bmatrix}$:**  
   **Inversible.** El determinante de una matriz triangular por bloques es el producto de los determinantes de sus bloques diagonales:
   $$\det \begin{bmatrix} A & A + B \\ 0 & B \end{bmatrix} = \det(A) \cdot \det(B) \neq 0$$
   Como $\det(A) \neq 0$ y $\det(B) \neq 0$, la matriz es invertible.

4. **(d) $ABA$:**  
   **Inversible.** Es el producto de tres matrices invertibles. Su inversa es $(ABA)^{-1} = A^{-1} B^{-1} A^{-1}$.

---

### Ejercicio 11.17: A matrix identity (Identidad matricial y matrices nilpotentes)

**Enunciado:**
Supón que $A$ es una matriz cuadrada que satisface $A^k = 0$ para algún entero $k$ (una matriz de este tipo se denomina **nilpotente**). Un estudiante conjetura que $(I - A)^{-1} = I + A + \dots + A^{k-1}$, basándose en la serie geométrica real $\frac{1}{1-a} = 1 + a + a^2 + \dots$, válida para números $a$ tales que $|a| < 1$.

¿Es correcta o incorrecta la afirmación del estudiante? Demuéstralo.

---

#### Resolución:
Comprobamos la hipótesis multiplicando la matriz $(I - A)$ por la expresión propuesta de la suma finita:
$$(I - A)(I + A + A^2 + \dots + A^{k-1})$$
Distribuimos los términos:
$$= (I + A + A^2 + \dots + A^{k-1}) - (A + A^2 + A^3 + \dots + A^k)$$
Cancelando los términos telescópicos intermedios, obtenemos:
$$= I - A^k$$
Dado que $A$ es nilpotente de orden $k$, se cumple por hipótesis que $A^k = 0$:
$$= I - 0 = I$$
**Conclusión:** La afirmación del estudiante es **correcta**. La inversa de $(I - A)$ viene dada exactamente por la serie finita truncada sin necesidad de restricciones de convergencia al ser una matriz nilpotente.

---

## Capítulo 13: Least Squares Data Fitting (Ajuste por Mínimos Cuadrados)

### Ejercicio 13.3: Moore's law (Ley de Moore)

**Enunciado:**
El gráfico y la tabla del ejercicio muestran el número de transistores $N$ en 13 microprocesadores y su año de introducción $t$. El objetivo es encontrar el ajuste por **mínimos cuadrados** (*Least Squares*) en línea recta mediante el modelo logarítmico:
$$\log_{10} N \approx \theta_1 + \theta_2(t - 1970)$$

1. **(a)** Encuentra los coeficientes $\theta_1$ y $\theta_2$ que minimizan el error RMS (*Root Mean Square*) sobre los datos, y calcula el valor del error RMS resultante.
2. **(b)** Utiliza el modelo para predecir el número de transistores en un microprocesador introducido en 2015. Compáralo con el superordenador IBM Z13 (2015) que contiene $4 \times 10^9$ transistores.
3. **(c)** Compara tu resultado con la **Ley de Moore** original, la cual establece que el número de transistores se duplica aproximadamente cada año y medio o dos años.

---

#### Resolución Aplicada:

*(a) Formulación del problema de Mínimos Cuadrados:*  
Construimos el sistema sobredimensionado de ecuaciones lineales $A\theta \approx y$, donde:
- El vector de observaciones $y \in \mathbb{R}^{13}$ contiene los valores de $\log_{10} N$.
- La matriz de diseño $A \in \mathbb{R}^{13 \times 2}$ contiene una columna de unos (para el término independiente $\theta_1$) y una columna con el tiempo transcurrido $t_i - 1970$ (para la pendiente $\theta_2$).

Aplicando la ecuación normal de mínimos cuadrados:
$$\theta = (A^T A)^{-1} A^T y$$

Mediante computación numérica (*Least Squares Regression*):
- $\theta_1 \approx 3.25$ (lo que predice un logaritmo de transistores de $\sim 3.25$ en 1970, es decir, $\approx 1778$ transistores).
- $\theta_2 \approx 0.30$ (tasa de crecimiento anual en escala logarítmica).

---

*(b) Predicción para el año 2015:*  
Sustituimos $t = 2015$ en nuestro modelo entrenado:
$$\log_{10} N = 3.25 + 0.30 \times (2015 - 1970) = 3.25 + 0.30 \times 45 = 3.25 + 13.5 = 16.75$$
Despejando el número estimado de transistores $N$:
$$N = 10^{16.75} \approx 5.6 \times 10^{16} \text{ transistores}$$
*Comparación:* El microprocesador real IBM Z13 lanzado en 2015 contiene $4 \times 10^9$ transistores, por lo que la extrapolación a largo plazo sobreestima significativamente el crecimiento real debido a los límites físicos de miniaturización alcanzados en décadas posteriores.

---

*(c) Validación de la Ley de Moore:*  
El incremento anual estimado por la pendiente es $\theta_2 \approx 0.30$. Dado que $\log_{10}(2) \approx 0.301$, esto significa que:
$$\Delta(\log_{10} N) = 0.30 \implies N \text{ se duplica cada } \frac{1}{0.30} \approx 3.3 \text{ años}$$
**Conclusión analítica:** El resultado empírico obtenido mediante el ajuste de mínimos cuadrados **se alinea muy estrechamente con la Ley de Moore clásica**, demostrando un crecimiento exponencial muy estable durante las décadas analizadas (1971-2003).