# Colección de Ejercicios Resueltos de Examen (Recurrencias, Grafos y Davis-Putnam)

---

## Tema 1: Función Booleana $f$

Dada una función booleana $f$, se plantean los siguientes apartados típicos de examen:

*   **a)** Expresión minimal de $f$ a condición de ser suma de productos (FND - Forma Normal Disyuntiva / SOP).
*   **b)** Expresión minimal de $f$ a condición de ser producto de sumas (FNC - Forma Normal Conjuntiva / POS).
*   **c)** Calcule los costes de las expresiones encontradas.
*   **d)** Diga si $f$ es una función autodual.

### Procedimiento de Resolución:

#### a) Expresión minimal como suma de productos (SOP):
1. Transformar minterms en binario.
2. Aplicar el método de **Quine-McCluskey**.
3. Aplicar el método de **Petrick** para la cobertura mínima.

#### b) Expresión minimal como producto de sumas (POS):
1. Trabajar con los maxterms.
2. Aplicar **Quine-McCluskey** (considerando los negados al revés).
3. Aplicar el método de **Petrick**.

#### d) Autodualidad:
Una función $f$ es autodual si la pareja que la describe es neutra. Por ejemplo, en $2^n$ siendo $n=4$:
$$2^n - 1 = 2^4 - 1 = 15$$
Las parejas complementarias cumplen $\{0, 15\}$, $\{1, 14\}$, $\dots$

---

## Tema 5: Recurrencias Homogéneas

Resolver la siguiente relación de recurrencia lineal homogénea:
$$\begin{cases} a_n + a_{n-1} - 6a_{n-2} = 0 & \forall n \ge 2 \\ a_0 = 1, & a_1 = 2 \end{cases}$$

### 1) Polinomio característico y Ecuación característica
*   Polinomio característico: $\lambda^2 + \lambda - 6$
*   Ecuación característica: 
    $$\lambda^2 + \lambda - 6 = 0$$

### 2) Resolución de la ecuación característica
$$\lambda = \frac{-1 \pm \sqrt{1^2 - 4(1)(-6)}}{2} = \frac{-1 \pm \sqrt{25}}{2} = \frac{-1 \pm 5}{2} \implies \begin{cases} \lambda_1 = 2 \\ \lambda_2 = -3 \end{cases}$$

> **Nota:** Si una raíz $\alpha$ estuviese repetida con multiplicidad $m$, la solución general incluiría términos de la forma:
> $$S_n = (A_0 + A_1 n + \dots + A_{m-1}n^{m-1})\alpha^n$$

### 3) Solución general
Por cada raíz simple se introduce un parámetro en la combinación lineal:
$$S_n = A \cdot (2)^n + B \cdot (-3)^n$$

### 4) Aplicación de las condiciones iniciales ($a_0 = 1, a_1 = 2$)
Evaluamos el sistema:
$$\begin{cases} a_0 = 1 \implies 2^0 \cdot A + (-3)^0 \cdot B = 1 \\ a_1 = 2 \implies 2^1 \cdot A + (-3)^1 \cdot B = 2 \end{cases}$$
$$\implies \begin{cases} A + B = 1 \\ 2A - 3B = 2 \end{cases} \implies A = 1, \quad B = 0$$

### 5) Sustitución para la solución particular
$$a_n = 2^n \cdot 1 + (-3)^n \cdot 0 = 2^n$$

### 6) Comprobación
Como se cumple para $\forall n \ge 2$, comprobamos sustituyendo $a_2$ en la ecuación original:
*   $a_2 = 2^2 = 4$
*   $a_1 = 2$
*   $a_0 = 1$

Sustituyendo en $a_n + a_{n-1} - 6a_{n-2} = 0$:
$$4 + 2 - 6(1) = 0 \implies 0 = 0 \quad (\text{Comprobado})$$

---

## Tema 5 (Continuación): Recurrencias No Homogéneas

Resolver la recurrencia:
$$\begin{cases} x_n - 2x_{n-1} = n + 2^n & \forall n \ge 2 \\ x_0 = 0 \end{cases}$$

### 1) Polinomio característico de la parte homogénea
$$x_n - 2x_{n-1} \implies x - 2$$

### 2) Parte no homogénea
El término independiente es $f(n) \cdot b^n = n + 2^n$.
Los sumandos se dividen en dos partes y se analiza cada caso:
1.  $(f_1(n) \cdot b_1^n = n \implies f_1(n) = n, \, b_1 = 1) \implies g_1(f_1) = 1$
2.  $(f_2(n) \cdot b_2^n = 2^n \implies f_2(n) = 1, \, b_2 = 2) \implies g_2(f_2) = 0$

### 3) Factores del polinomio característico asociado
*   Para $b=1$ con grado $g(f_1)=1$: $(x - 1)^{1 + 1} = (x - 1)^2$
*   Para $b=2$ con grado $g(f_2)=0$: $(x - 2)^{0 + 1} = (x - 2)^1$

### 4) Polinomio característico total
$$(x - 2)(x - 1)^2(x - 2) = (x - 1)^2(x - 2)^2$$

### 5) Identificación de raíces
*   $\alpha_1 = 2$, con multiplicidad $2$
*   $\alpha_2 = 1$, con multiplicidad $2$

### 6) Forma de la solución general
$$x_n = (A + Bn)2^n + (C + Dn)1^n = A \cdot 2^n + B \cdot n 2^n + C \cdot 1^n + D \cdot n$$

### 7) Cálculo de condiciones iniciales necesarias
Dado que necesitamos 4 coeficientes ($A, B, C, D$), calculamos los valores iniciales mediante la recurrencia:
*   $x_0 = 0$
*   $x_1 = 1 + 2^1 + 2 \cdot x_0 = 1 + 2 + 0 = 3$
*   $x_2 = 2 + 2^2 + 2 \cdot x_1 = 2 + 4 + 2(3) = 12$
*   $x_3 = 3 + 2^3 + 2 \cdot x_2 = 3 + 8 + 2(12) = 35$

### 8) Sustitución y resolución del sistema
Planteamos el sistema para $n = 0, 1, 2, 3$:
$$\begin{cases}
A \cdot 2^0 + B \cdot 0 \cdot 2^0 + C \cdot 1^0 + D \cdot 0 \cdot 1^0 = 0 \\
A \cdot 2^1 + B \cdot 1 \cdot 2^1 + C \cdot 1^1 + D \cdot 1 \cdot 1^1 = 3 \\
A \cdot 2^2 + B \cdot 2 \cdot 2^2 + C \cdot 1^2 + D \cdot 2 \cdot 1^2 = 12 \\
A \cdot 2^3 + B \cdot 3 \cdot 2^3 + C \cdot 1^3 + D \cdot 3 \cdot 1^3 = 35
\end{cases}$$

Resolviendo el sistema obtenemos los coeficientes:
*   $D = -1$
*   $C = -2$
*   $B = 1$
*   $A = 2$

### 9) Solución particular final
$$x_n = 2 \cdot 2^n + n \cdot 2^n - 2 \cdot 1^n - n \cdot 1^n$$

---

## Tema 6: Grafos

### Algoritmo de Hakimi (Validación de Grafibilidad)

#### Precondiciones:
1. Sucesión de números en orden decreciente.
2. El número de elementos impares debe ser **par** (Lema del apretón de manos).
3. El mayor elemento debe ser estrictamente menor que el número de vértices ($d_{\max} < n$).

#### Procedimiento:
1. Quitas el $n$-ésimo mayor elemento y restas $1$ a los $n$ siguientes términos.
2. Repites el proceso ordenadamente hasta que se acaben los elementos.
3. Reconstruyes el grafo uniendo los vértices correspondientes.

---

### Algoritmo de Kruskal (Árbol de Recubrimiento Mínimo / Máximo)

#### Procedimiento:
1. Dependiendo de si buscamos el **máximo** o **mínimo** coste, ordenamos las aristas de mayor a menor o viceversa.
2. Seleccionamos las aristas en orden de peso, comprobando que **no se cierren ciclos** (habitualmente usando conjuntos disjuntos / Union-Find).

---

### Algoritmo de Prim

#### Procedimiento:
1. Empezamos en un vértice cualquiera.
2. Vamos eligiendo la arista de menor coste incidente hacia un vértice **no visitado**, hasta que todos los vértices estén visitados.

---

### Código de Prüfer (Árboles Etiquetados)

#### Construir el árbol a partir del código:
1. Dado un vector de $n$ elementos (código de Prüfer), se crea otro vector con los números desde $1$ hasta $n+2$.
2. Se toma el primer valor del código y se busca en el segundo vector el elemento de **menor valor** que **ya no esté** en el código.
3. Se unen ambos vértices y se eliminan de sus respectivas listas. Se repite hasta que sobren dos vértices, los cuales se unen entre sí.

#### Sacar el código a partir del árbol:
1. Se localiza la hoja (vértice de grado 1) con la etiqueta **más pequeña**, se anota el vértice al que está conectada y se elimina la hoja.
2. Se repite el proceso recursivamente hasta que queden exactamente $2$ vértices en el árbol.

---

## Tema 2: Lógica Proposicional y Resolución (Davis-Putnam)

### Ejercicio 3: Demostración de Tautología
Sea la fórmula $\alpha$:
$$\alpha \equiv p \lor q \to \big[(p \to i) \to ((i \to q) \to ((q \to p) \to q \land i))\big]$$
Demuestra que $\alpha$ es una tautología (**Muy importante para examen**).

#### Paso 1: Transformación a Insatisfactibilidad
Transformamos el problema de implicación semántica en un problema de insatisfactibilidad aplicando el **Teorema de la Deducción**:
$$\Sigma \cup \{\alpha\} \models \beta \iff \Sigma \models \alpha \to \beta$$
$$\{\alpha\} \models \beta \iff \emptyset \models \alpha \to \beta$$
Y por el teorema de refutación:
$$\{\alpha\} \text{ es tautología} \iff \{\neg \alpha\} \text{ es insatisfactible}$$

Aplicando las deducciones paso a paso sobre las premisas:
1. $\{p \lor q\} \not\models (p \to i) \to ((i \to q) \to ((q \to p) \to q \land i))$
2. $\{p \lor q, \, p \to i\} \not\models (i \to q) \to ((q \to p) \to q \land i)$
3. $\{p \lor q, \, p \to i, \, i \to q\} \not\models (q \to p) \to q \land i$
4. $\{p \lor q, \, p \to i, \, i \to q, \, q \to p\} \not\models q \land i$

Añadiendo la negación de la tesis para buscar la refutación:
$$\{\, p \lor q, \; \neg p \lor i, \; \neg i \lor q, \; \neg q \lor p, \; \neg(q \land i) \,\}$$

#### Paso 2: Cálculo de las Formas Clausuladas
1. $p \lor q$
2. $p \to i \equiv \neg p \lor i$
3. $i \to q \equiv \neg i \lor q$
4. $q \to p \equiv \neg q \lor p$
5. $\neg(q \land i) \equiv \neg q \lor \neg i$

---

### Paso 3: Aplicación del Algoritmo de Davis-Putnam (D-P)

Conjunto de cláusulas inicial:
$$\{\, p \lor q, \; \neg p \lor i, \; \neg i \lor q, \; \neg q \lor p, \; \neg q \lor \neg i \,\}$$

Aplicamos ramificación por **cláusula unitaria** o **literales puros**:

```text
                        { p ∨ q, ¬p ∨ i, ¬i ∨ q, ¬q ∨ p, ¬q ∨ ¬i }
                                       /           \
                     (λ = p)          /             \         (λ = ¬p)
                                     v               v
                   { i, ¬i ∨ q, ¬q ∨ p, ¬q ∨ ¬i }   { q, ¬i ∨ q, ¬q ∨ p, ¬q ∨ ¬i }
                                   |                               |
                     (λ = i)       |                 (λ = q)       |
                                   v                               v
                       { q, ¬q ∨ p, ¬q ∨ ¬i }                  { ¬i, ¬i ∨ p, ¬i }
                                   |                               |
                     (λ = q)       |                 (λ = ¬i)      |
                                   v                               v
                                { p, ¬i }                        { □ }
                                                              (Cláusula vacía)
```

> **Nota:** Como en **todas** las ramas del árbol hemos llegado a la **cláusula vacía ($\Box$)**, el conjunto de cláusulas es **insatisfactible**. Por consiguiente, la fórmula original $\alpha$ es una **tautología**.

---

### Ejercicio 2: Implicación Semántica
Comprueba si el siguiente problema de implicación semántica es cierto:
$$\{p \leftrightarrow \neg q, \; q \to p \lor t, \; r \to q \lor s, \; q \to r \land p, \; \neg t \lor q \to r \lor p, \; \neg t \lor s\} \models s$$

#### Paso 1: Transformación en insatisfactibilidad
Aplicando las equivalencias lógicas y el Teorema de Deducción, negamos la conclusión y añadimos $\neg s$ al conjunto de premisas:
$$\{ p \leftrightarrow \neg q, \; q \to p \lor t, \; r \to q \lor s, \; q \to r \land p, \; \neg(\neg t \lor q) \lor r \lor p, \; \neg t \lor s, \; \neg s \}$$

#### Paso 2: Clausulación de cada fórmula
1. $p \leftrightarrow \neg q \equiv (p \to \neg q) \land (\neg p \to \neg q) \equiv (\neg p \lor \neg q) \land (p \lor q)$
2. $q \to p \lor t \equiv \neg q \lor p \lor t$
3. $r \to q \lor s \equiv \neg r \lor q \lor s$
4. $q \to r \land p \equiv (\neg q \lor r) \land (\neg q \lor p)$
5. $\neg(\neg t \lor q) \lor r \lor p \equiv (t \land \neg q) \lor r \lor p \equiv (t \lor r \lor p) \land (\neg q \lor r \lor p)$
6. $\neg t \lor s$
7. $\neg s$

#### Paso 3: Aplicación de Davis-Putnam
Conjunto de cláusulas resultante:
$$\{\neg p \lor \neg q, \; p \lor q, \; \neg q \lor p \lor t, \; \neg r \lor q \lor s, \; \neg q \lor r, \; \neg q \lor p, \; t \lor r \lor p, \; \neg q \lor r \lor p, \; \neg t \lor s, \; \neg s\}$$

Aplicando resolución con la cláusula unitaria $\lambda = \neg s$:
*   Se propaga $\neg s$ eliminando $s$ de las cláusulas donde aparezca y generando nuevas reducciones hasta alcanzar la contradicción (cláusula vacía $\Box$).