# Bloque 1: Lógica Proposicional, Tablas de Verdad, Tautologías y Demostraciones por Resolución

---

## Ejercicio 1 (Rosen, Sección 1.1, Ejercicio 39, incisos e y f)

### Enunciado
Construya la tabla de verdad (*truth table*) para cada una de las siguientes proposiciones compuestas:
* **e)** $(p \leftrightarrow q) \lor (\neg q \leftrightarrow r)$
* **f)** $(\neg p \leftrightarrow \neg q) \leftrightarrow (q \leftrightarrow r)$

---

### Resolución y Análisis Formal

Recordemos que la equivalencia lógica o bicondicional ($A \leftrightarrow B$) es verdadera ($T$) si y solo si ambas proposiciones componentes $A$ y $B$ poseen el mismo valor de verdad; en caso contrario, es falsa ($F$).

#### Inciso e) $(p \leftrightarrow q) \lor (\neg q \leftrightarrow r)$
Desglosamos las subexpresiones:
1. $p \leftrightarrow q$: verdadera cuando $p = q$.
2. $\neg q$: negación del valor de verdad de $q$.
3. $\neg q \leftrightarrow r$: verdadera cuando $\neg q$ y $r$ tienen el mismo valor de verdad.
4. $(p \leftrightarrow q) \lor (\neg q \leftrightarrow r)$: disyunción de las dos subexpresiones anteriores (verdadera si al menos una de ellas es verdadera).

#### Inciso f) $(\neg p \leftrightarrow \neg q) \leftrightarrow (q \leftrightarrow r)$
Notemos la propiedad elemental: $\neg p \leftrightarrow \neg q \equiv p \leftrightarrow q$. Por lo tanto, la expresión evalúa si $(p \leftrightarrow q)$ y $(q \leftrightarrow r)$ tienen el mismo valor de verdad.

### Tabla de Verdad Consolidada

| $p$ | $q$ | $r$ | $\neg p$ | $\neg q$ | $p \leftrightarrow q$ | $\neg q \leftrightarrow r$ | **e)** $(p \leftrightarrow q) \lor (\neg q \leftrightarrow r)$ | $\neg p \leftrightarrow \neg q$ | $q \leftrightarrow r$ | **f)** $(\neg p \leftrightarrow \neg q) \leftrightarrow (q \leftrightarrow r)$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $T$ | $T$ | $T$ | $F$ | $F$ | $T$ | $F$ | **$T$** | $T$ | $T$ | **$T$** |
| $T$ | $T$ | $F$ | $F$ | $F$ | $T$ | $T$ | **$T$** | $T$ | $F$ | **$F$** |
| $T$ | $F$ | $T$ | $F$ | $T$ | $F$ | $T$ | **$T$** | $F$ | $F$ | **$T$** |
| $T$ | $F$ | $F$ | $F$ | $T$ | $F$ | $F$ | **$F$** | $F$ | $T$ | **$F$** |
| $F$ | $T$ | $T$ | $T$ | $F$ | $F$ | $F$ | **$F$** | $F$ | $T$ | **$F$** |
| $F$ | $T$ | $F$ | $T$ | $F$ | $F$ | $T$ | **$T$** | $F$ | $F$ | **$T$** |
| $F$ | $F$ | $T$ | $T$ | $T$ | $T$ | $T$ | **$T$** | $T$ | $F$ | **$F$** |
| $F$ | $F$ | $F$ | $T$ | $T$ | $T$ | $F$ | **$T$** | $T$ | $T$ | **$T$** |

---

## Ejercicio 2 (Rosen, Sección 1.3, Ejercicio 5)

### Enunciado
Utilice una tabla de verdad para verificar la ley distributiva (*distributive law*) de la conjunción respecto de la disyunción:
$$p \land (q \lor r) \equiv (p \land q) \lor (p \land r)$$

---

### Demostración mediante Tabla de Verdad

Para demostrar que dos proposiciones compuestas son lógicamente equivalentes ($\equiv$), debemos verificar que sus columnas correspondientes en la tabla de verdad presenten idénticos valores de verdad bajo cualquier asignación posible de las variables proposicionales $p, q, r$.

| $p$ | $q$ | $r$ | $q \lor r$ | $p \land (q \lor r)$ | $p \land q$ | $p \land r$ | $(p \land q) \lor (p \land r)$ | ¿Idénticos? |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $T$ | $T$ | $T$ | $T$ | **$T$** | $T$ | $T$ | **$T$** | Sí |
| $T$ | $T$ | $F$ | $T$ | **$T$** | $T$ | $F$ | **$T$** | Sí |
| $T$ | $F$ | $T$ | $T$ | **$T$** | $F$ | $T$ | **$T$** | Sí |
| $T$ | $F$ | $F$ | $F$ | **$F$** | $F$ | $F$ | **$F$** | Sí |
| $F$ | $T$ | $T$ | $T$ | **$F$** | $F$ | $F$ | **$F$** | Sí |
| $F$ | $T$ | $F$ | $T$ | **$F$** | $F$ | $F$ | **$F$** | Sí |
| $F$ | $F$ | $T$ | $T$ | **$F$** | $F$ | $F$ | **$F$** | Sí |
| $F$ | $F$ | $F$ | $F$ | **$F$** | $F$ | $F$ | **$F$** | Sí |

### Conclusión
Las columnas correspondientes a $p \land (q \lor r)$ y $(p \land q) \lor (p \land r)$ coinciden en todas las filas ($2^3 = 8$ interpretaciones). Queda formalmente demostrada la equivalencia lógica.

---

## Ejercicio 3 (Rosen, Sección 1.3, Ejercicio 33)

### Enunciado
Demuestre que la siguiente proposición condicional, correspondiente a la regla de inferencia del **Silogismo Hipotético** (*Hypothetical Syllogism*), es una tautología:
$$((p \rightarrow q) \land (q \rightarrow r)) \rightarrow (p \rightarrow r)$$

---

### Demostración mediante Tabla de Verdad

Una proposición compuesta es una tautología si su valor de verdad es verdadero ($T$) para todas y cada una de las interpretaciones de sus variables.

| $p$ | $q$ | $r$ | $p \rightarrow q$ | $q \rightarrow r$ | $p \rightarrow r$ | $(p \rightarrow q) \land (q \rightarrow r)$ | $[(p \rightarrow q) \land (q \rightarrow r)] \rightarrow (p \rightarrow r)$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $T$ | $T$ | $T$ | $T$ | $T$ | $T$ | $T$ | **$T$** |
| $T$ | $T$ | $F$ | $T$ | $F$ | $F$ | $F$ | **$T$** |
| $T$ | $F$ | $T$ | $F$ | $T$ | $T$ | $F$ | **$T$** |
| $T$ | $F$ | $F$ | $F$ | $T$ | $F$ | $F$ | **$T$** |
| $F$ | $T$ | $T$ | $T$ | $T$ | $T$ | $T$ | **$T$** |
| $F$ | $T$ | $F$ | $T$ | $F$ | $T$ | $F$ | **$T$** |
| $F$ | $F$ | $T$ | $T$ | $T$ | $T$ | $T$ | **$T$** |
| $F$ | $F$ | $F$ | $T$ | $T$ | $T$ | $T$ | **$T$** |

### Conclusión
Dado que la última columna contiene únicamente valores $T$, la proposición es formalmente una **tautología**.

---

## Ejercicio 4 (Rosen, Sección 1.3, Ejercicio 34)

### Enunciado
Demuestre que la proposición condicional correspondiente al **Principio de Resolución** (*Resolution Principle*) es una tautología:
$$((p \lor q) \land (\neg p \lor r)) \rightarrow (q \lor r)$$

---

### Demostración mediante Tabla de Verdad

| $p$ | $q$ | $r$ | $\neg p$ | $p \lor q$ | $\neg p \lor r$ | $q \lor r$ | $(p \lor q) \land (\neg p \lor r)$ | $[(p \lor q) \land (\neg p \lor r)] \rightarrow (q \lor r)$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $T$ | $T$ | $T$ | $F$ | $T$ | $T$ | $T$ | $T$ | **$T$** |
| $T$ | $T$ | $F$ | $F$ | $T$ | $F$ | $T$ | $F$ | **$T$** |
| $T$ | $F$ | $T$ | $F$ | $T$ | $T$ | $T$ | $T$ | **$T$** |
| $T$ | $F$ | $F$ | $F$ | $T$ | $F$ | $F$ | $F$ | **$T$** |
| $F$ | $T$ | $T$ | $T$ | $T$ | $T$ | $T$ | $T$ | **$T$** |
| $F$ | $T$ | $F$ | $T$ | $T$ | $T$ | $T$ | $T$ | **$T$** |
| $F$ | $F$ | $T$ | $T$ | $F$ | $T$ | $T$ | $F$ | **$T$** |
| $F$ | $F$ | $F$ | $T$ | $F$ | $T$ | $F$ | $F$ | **$T$** |

### Conclusión
La columna resultante está compuesta exclusivamente por el valor de verdad $T$, lo cual confirma que el principio de resolución proposicional es una **tautología**.

---

## Ejercicio 5 (Rosen, Sección 1.3, Ejercicio 55)

### Enunciado
Encuentre una proposición compuesta lógicamente equivalente a la implicación $p \rightarrow q$ utilizando **únicamente** el operador lógico $\downarrow$ (operador **NOR** o flecha de Peirce / *Peirce arrow*).

---

### Análisis y Desarrollo Teórico

#### 1. Definición Formal del Operador NOR ($\downarrow$)
El operador binario $\downarrow$ se define como la negación de la disyunción:
$$p \downarrow q \equiv \neg(p \lor q)$$

*(Nota de corrección técnica sobre los apuntes: El símbolo $\downarrow$ denota el operador **NOR**, mientras que la barra de Sheffer $\mid$ denota **NAND**, definido como $\neg(p \land q)$).*

#### 2. Negación mediante NOR
Para cualquier variable $x$:
$$x \downarrow x \equiv \neg(x \lor x) \equiv \neg x$$
Por lo tanto:
$$\neg p \equiv p \downarrow p$$

#### 3. Conjunción mediante NOR
Aplicando las leyes de De Morgan:
$$\neg x \downarrow \neg y \equiv \neg(\neg x \lor \neg y) \equiv \neg\neg x \land \neg\neg y \equiv x \land y$$
Sustituyendo $\neg x$ por $(x \downarrow x)$ e $y$ por $(y \downarrow y)$:
$$x \land y \equiv (x \downarrow x) \downarrow (y \downarrow y)$$

#### 4. Disyunción mediante NOR
La disyunción es la negación de una operación NOR:
$$x \lor y \equiv \neg(x \downarrow y) \equiv (x \downarrow y) \downarrow (x \downarrow y)$$

#### 5. Expresión de la Implicación $p \rightarrow q$ en términos de NOR
Sabemos que:
$$p \rightarrow q \equiv \neg p \lor q$$

Sustituyendo en la fórmula de la disyunción obtenida en el paso 4:
$$A \lor B \equiv (A \downarrow B) \downarrow (A \downarrow B)$$
Haciendo $A = \neg p \equiv (p \downarrow p)$ y $B = q$:
$$p \rightarrow q \equiv [((p \downarrow p) \downarrow q)] \downarrow [((p \downarrow p) \downarrow q)]$$

Alternativamente, simplificando mediante la equivalencia de la implicación:
$$p \rightarrow q \equiv \neg (p \land \neg q) \equiv p \downarrow \neg q \text{... no, } \neg(p \lor \neg q) \text{ no es } p \rightarrow q.$$
Verifiquemos la expresión por tabla de verdad:
Sea $X = (p \downarrow p) \downarrow q = \neg p \downarrow q \equiv \neg(\neg p \lor q) \equiv p \land \neg q$.
Entonces:
$$X \downarrow X \equiv \neg X \equiv \neg(p \land \neg q) \equiv \neg p \lor q \equiv p \rightarrow q$$

Por consiguiente, la expresión canónica mínima usando exclusivamente el operador NOR ($\downarrow$) es:
$$p \rightarrow q \equiv ((p \downarrow p) \downarrow q) \downarrow ((p \downarrow p) \downarrow q)$$

---

## Ejercicio 6 (Rosen, Sección 1.3, Ejercicio 65)

### Enunciado
Determine si cada una de las siguientes proposiciones compuestas es **satisfacible** (*satisfiable*):
* **a)** $(p \lor \neg q) \land (\neg p \lor q) \land (\neg p \lor \neg q)$
* **b)** $(p \rightarrow q) \land (p \rightarrow \neg q) \land (\neg p \rightarrow q) \land (\neg p \rightarrow \neg q)$
* **c)** $(p \leftrightarrow q) \land (\neg p \leftrightarrow q)$

---

### Análisis y Resolución

Una proposición es satisfacible si existe **al menos una** asignación de valores de verdad a sus variables que haga que la proposición sea verdadera ($T$). Si resulta falsa para todas las interpretaciones, es **insatisfacible** (*unsatisfiable* o contradicción).

#### Inciso a) $(p \lor \neg q) \land (\neg p \lor q) \land (\neg p \lor \neg q)$

| $p$ | $q$ | $\neg p$ | $\neg q$ | $p \lor \neg q$ | $\neg p \lor q$ | $\neg p \lor \neg q$ | $(p \lor \neg q) \land (\neg p \lor q) \land (\neg p \lor \neg q)$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $T$ | $T$ | $F$ | $F$ | $T$ | $T$ | $F$ | $F$ |
| $T$ | $F$ | $F$ | $T$ | $T$ | $F$ | $F$ | $F$ |
| $F$ | $T$ | $T$ | $F$ | $F$ | $T$ | $T$ | $F$ |
| $F$ | $F$ | $T$ | $T$ | $T$ | $T$ | $T$ | **$T$** |

* **Conclusión:** Es **satisfacible** (se satisface con la asignación $p = F, q = F$).

---

#### Inciso b) $(p \rightarrow q) \land (p \rightarrow \neg q) \land (\neg p \rightarrow q) \land (\neg p \rightarrow \neg q)$
Recordemos que $A \rightarrow B \equiv \neg A \lor B$. Por lo tanto:
* $p \rightarrow q \equiv \neg p \lor q$
* $p \rightarrow \neg q \equiv \neg p \lor \neg q$
* $\neg p \rightarrow q \equiv p \lor q$
* $\neg p \rightarrow \neg q \equiv p \lor \neg q$

La expresión representa la conjunción de las cuatro cláusulas posibles sobre dos variables:
$$(p \lor q) \land (p \lor \neg q) \land (\neg p \lor q) \land (\neg p \lor \neg q)$$

| $p$ | $q$ | $p \rightarrow q$ | $p \rightarrow \neg q$ | $\neg p \rightarrow q$ | $\neg p \rightarrow \neg q$ | Expresión Completa |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $T$ | $T$ | $T$ | $F$ | $T$ | $T$ | **$F$** |
| $T$ | $F$ | $F$ | $T$ | $T$ | $T$ | **$F$** |
| $F$ | $T$ | $T$ | $T$ | $T$ | $F$ | **$F$** |
| $F$ | $F$ | $T$ | $T$ | $F$ | $T$ | **$F$** |

* **Conclusión:** Es **insatisfacible** (contradicción).

---

#### Inciso c) $(p \leftrightarrow q) \land (\neg p \leftrightarrow q)$

| $p$ | $q$ | $p \leftrightarrow q$ | $\neg p \leftrightarrow q$ | $(p \leftrightarrow q) \land (\neg p \leftrightarrow q)$ |
|:---:|:---:|:---:|:---:|:---:|
| $T$ | $T$ | $T$ | $F$ | **$F$** |
| $T$ | $F$ | $F$ | $T$ | **$F$** |
| $F$ | $T$ | $F$ | $T$ | **$F$** |
| $F$ | $F$ | $T$ | $F$ | **$F$** |

* **Conclusión:** Es **insatisfacible**. Intuitivamente, $\neg p \leftrightarrow q \equiv \neg(p \leftrightarrow q)$, por lo que la fórmula tiene la forma $A \land \neg A \equiv F$.

---

## Ejercicio 7 (Rosen, Sección 1.6, Ejercicio 33)

### Enunciado
Utilice el método de **Resolución** (*Resolution*) para demostrar que la proposición compuesta en Forma Normal Conjuntiva (FNC / CNF) no es satisfacible:
$$(p \lor q) \land (\neg p \lor q) \land (p \lor \neg q) \land (\neg p \lor \neg q)$$

---

### Demostración Formal por Resolución

El método de resolución consiste en derivar repetidamente resolventes a partir de pares de cláusulas que contienen literales complementarios, con el objetivo de deducir la **cláusula vacía** ($\square$ o $\emptyset$), lo cual demuestra la insatisfacibilidad del conjunto.

#### Paso 1: Identificación del conjunto de cláusulas
Sea la base de conocimiento $\mathcal{S} = \{C_1, C_2, C_3, C_4\}$:
* $C_1: p \lor q$
* $C_2: \neg p \lor q$
* $C_3: p \lor \neg q$
* $C_4: \neg p \lor \neg q$

#### Paso 2: Aplicación sistemática de la regla de resolución
1. **Resolución entre $C_1$ y $C_2$ sobre el literal $p$:**
   $$\frac{p \lor q \quad \neg p \lor q}{q} \implies C_5: q$$

2. **Resolución entre $C_3$ y $C_4$ sobre el literal $p$:**
   $$\frac{p \lor \neg q \quad \neg p \lor \neg q}{\neg q} \implies C_6: \neg q$$

3. **Resolución entre $C_5$ y $C_6$ sobre el literal $q$:**
   $$\frac{q \quad \neg q}{\square}$$

### Conclusión
Al derivarse formalmente la cláusula vacía $\square$ (contradicción), queda demostrado que la proposición original es **insatisfacible**.

---

## Ejercicio 8 (Rosen, Sección 2.3, Ejercicio 8)

### Enunciado
* **a)** Defina dominio (*domain*), codominio (*codomain*) y rango o conjunto imagen (*range*) de una función.
* **b)** Sea $f: \mathbb{Z} \to \mathbb{Z}$ la función definida sobre el conjunto de los números enteros tal que $f(n) = n^2 + 1$. ¿Cuáles son el dominio, el codominio y el rango de esta función?

---

### Solución y Rigor Teórico

#### a) Definiciones Fundamentales
Dada una función $f: A \to B$:
* **Dominio (*Domain*):** Es el conjunto de partida $A$, es decir, el conjunto de todos los posibles valores de entrada para los cuales la función está definida.
* **Codominio (*Codomain*):** Es el conjunto de llegada $B$, que contiene todos los posibles valores que potencialmente puede tomar la función según su definición estructural.
* **Rango o Imagen (*Range / Image*):** Es el subconjunto del codominio formado por todas las imágenes efectivas de los elementos del dominio:
  $$\text{Rango}(f) = f(A) = \{ b \in B \mid \exists a \in A \text{ tal que } f(a) = b \} \subseteq B$$

#### b) Aplicación a la función $f(n) = n^2 + 1$
Para la función dada $f: \mathbb{Z} \to \mathbb{Z}$:
* **Dominio:** $\mathbb{Z}$ (el conjunto de los números enteros, dado explícitamente en la definición).
* **Codominio:** $\mathbb{Z}$ (el conjunto de los números enteros especificado como conjunto de llegada).
* **Rango:**
  Analizamos los valores de salida para $n \in \mathbb{Z}$:
  $$n \in \mathbb{Z} \implies n^2 \in \{0, 1, 4, 9, 16, \dots\} = \{ k^2 \mid k \in \mathbb{N}_0 \}$$
  Por ende:
  $$f(n) = n^2 + 1 \in \{1, 2, 5, 10, 17, 26, \dots\}$$
  En notación de conjuntos por comprensión:
  $$\text{Rango}(f) = \{ n^2 + 1 \mid n \in \mathbb{Z} \} = \{ m \in \mathbb{Z}^+ \mid m - 1 \text{ es un cuadrado perfecto} \}$$