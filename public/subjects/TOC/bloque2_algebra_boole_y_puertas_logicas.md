# Bloque 2: Álgebra de Boole, Teoremas, Formas Canónicas y Puertas Lógicas

**Asignatura:** Tecnología y Organización de Computadores (TOC) — 1º Grado en Ingeniería Informática (UGR)  
**Contenido:** Operaciones booleanas básicas, tablas de verdad, axiomas y teoremas, De Morgan, minterms y maxterms, catálogo de puertas digitales y familias universales (NAND y NOR).

---

## 1. Operaciones Lógicas Fundamentales

El álgebra booleana opera sobre el conjunto binario $B = \{0, 1\}$ mediante tres operaciones elementales:

1. **Producto Lógico (AND / Conjunción):** $z = x \cdot y$ (o simplemente $xy$). La salida es 1 únicamente cuando todas las entradas son 1.
2. **Suma Lógica (OR / Disyunción):** $z = x + y$. La salida es 1 cuando al menos una de las entradas es 1.
3. **Inversión (NOT / Negación):** $z = \bar{x} = x'$. Invierte el valor lógico del operando.

### 1.1. Tablas de Verdad

| $x$ | $y$ | AND ($x \cdot y$) | OR ($x + y$) | NOT ($x'$) |
| :---: | :---: | :---: | :---: | :---: |
| 0 | 0 | 0 | 0 | 1 |
| 0 | 1 | 0 | 1 | 1 |
| 1 | 0 | 0 | 1 | 0 |
| 1 | 1 | 1 | 1 | 0 |

---

## 2. Axiomas y Teoremas del Álgebra de Boole

### 2.1. Reglas de Operación con Elementos Neutros y Absorbentes
* **Operación OR:**
  1. $A + 0 = A$ (Elemento neutro para la suma)
  2. $A + 1 = 1$ (Elemento absorbente para la suma)
  3. $A + A = A$ (Idempotencia)
  4. $A + \bar{A} = 1$ (Complementariedad)

* **Operación AND:**
  1. $A \cdot 0 = 0$ (Elemento absorbente para el producto)
  2. $A \cdot 1 = A$ (Elemento neutro para el producto)
  3. $A \cdot A = A$ (Idempotencia)
  4. $A \cdot \bar{A} = 0$ (Complementariedad)

### 2.2. Propiedades Algebraicas
* **Involución (Doble Negación):**
  $$\overline{\overline{A}} = A$$
* **Conmutatividad:**
  $$A + B = B + A \qquad A \cdot B = B \cdot A$$
* **Asociatividad:**
  $$(A + B) + C = A + (B + C) \qquad (A \cdot B) \cdot C = A \cdot (B \cdot C)$$
* **Distributividad:**
  $$A \cdot (B + C) = A \cdot B + A \cdot C$$
  $$A + (B \cdot C) = (A + B) \cdot (A + C) \quad \text{(Distributiva de la suma sobre el producto)}$$
* **Absorción:**
  $$A + A \cdot B = A \qquad A \cdot (A + B) = A$$

### 2.3. Teoremas de De Morgan
Permiten transformar sumas en productos y viceversa mediante la negación:
1. **Primera Ley de De Morgan:**
   $$\overline{A + B} = \bar{A} \cdot \bar{B}$$
   *El complemento de una suma es igual al producto de los complementos.*
2. **Segunda Ley de De Morgan:**
   $$\overline{A \cdot B} = \bar{A} + \bar{B}$$
   *El complemento de un producto es igual a la suma de los complementos.*

---

## 3. Formas Canónicas: Minterms y Maxterms

Cualquier función booleana de $n$ variables puede expresarse de manera única e inequívoca en forma canónica.

### 3.1. Términos Mínimos (Minterms, $m_i$)
Un **minterm** es un producto booleano que contiene todas las $n$ variables de la función, apareciendo afirmadas si en la fila de la tabla de verdad valen 1, o negadas si valen 0:
* Para una función $F(A, B, C)$:
  * Fila 0 ($A=0, B=0, C=0$): $m_0 = \bar{A}\bar{B}\bar{C}$
  * Fila 3 ($A=0, B=1, C=1$): $m_3 = \bar{A}BC$
  * Fila 7 ($A=1, B=1, C=1$): $m_7 = ABC$
* **Forma Canónica en Suma de Productos (SOP / DNF):**
  $$F(A, B, C) = \sum m(i) = \text{Suma de los minterms donde la función vale 1}$$

### 3.2. Términos Máximos (Maxterms, $M_i$)
Un **maxterm** es una suma booleana que contiene todas las $n$ variables de la función, apareciendo afirmadas si en la fila valen 0, o negadas si valen 1:
* Para una función $F(A, B, C)$:
  * Fila 0 ($A=0, B=0, C=0$): $M_0 = A + B + C$
  * Fila 5 ($A=1, B=0, C=1$): $M_5 = \bar{A} + B + \bar{C}$
* **Forma Canónica en Producto de Sumas (POS / CNF):**
  $$F(A, B, C) = \prod M(j) = \text{Producto de los maxterms donde la función vale 0}$$

### 3.3. Relación de Dualidad
$$m_i = \overline{M_i} \iff \overline{F} = \sum m(\text{filas donde } F=0) = \prod M(\text{filas donde } F=1)$$

---

## 4. Catálogo Completo de Puertas Lógicas Digitales

| Nombre de la Puerta | Símbolo Gráfico | Función Algebraica | Tabla de Verdad ($x, y \to F$) |
| :--- | :---: | :--- | :---: |
| **AND** | `D` plano | $F = x \cdot y$ | `00:0, 01:0, 10:0, 11:1` |
| **OR** | `)` curvo | $F = x + y$ | `00:0, 01:1, 10:1, 11:1` |
| **Inversor (NOT)** | Triángulo con círculo | $F = x'$ | `0:1, 1:0` |
| **Buffer** | Triángulo directo | $F = x$ | `0:0, 1:1` |
| **NAND** | AND con círculo de inversión | $F = (x \cdot y)'$ | `00:1, 01:1, 10:1, 11:0` |
| **NOR** | OR con círculo de inversión | $F = (x + y)'$ | `00:1, 01:0, 10:0, 11:0` |
| **XOR (OR Exclusiva)** | OR con doble arco de entrada | $F = x \oplus y = x'y + xy'$ | `00:0, 01:1, 10:1, 11:0` |
| **XNOR (Equivalencia)** | XOR con círculo de inversión | $F = (x \oplus y)' = xy + x'y'$ | `00:1, 01:0, 10:0, 11:1` |

---

## 5. Universalidad de Puertas Lógicas (NAND y NOR)

Las puertas **NAND** y **NOR** son conjuntos completos o funcionales universales: cualquier circuito lógico digital combinacional o secuencial puede ser implementado empleando exclusivamente puertas de un solo tipo.

### 5.1. Implementaciones Universales con NAND
1. **NOT mediante NAND:**
   $$\text{NOT}(A) = \overline{A \cdot A} = \bar{A}$$
   *(Se unen las dos entradas de la puerta NAND a la misma señal $A$).*
2. **AND mediante NAND:**
   $$\text{AND}(A, B) = \overline{\overline{A \cdot B}} = A \cdot B$$
   *(Se pasa la salida de una puerta NAND por un inversor NAND).*
3. **OR mediante NAND (aplicando De Morgan):**
   $$\text{OR}(A, B) = \overline{\bar{A} \cdot \bar{B}} = A + B$$
   *(Se niegan independientemente $A$ y $B$ con inversores NAND y sus salidas se introducen a una tercera puerta NAND).*

### 5.2. Implementaciones Universales con NOR
1. **NOT mediante NOR:**
   $$\text{NOT}(A) = \overline{A + A} = \bar{A}$$
   *(Se unen las dos entradas de la puerta NOR).*
2. **OR mediante NOR:**
   $$\text{OR}(A, B) = \overline{\overline{A + B}} = A + B$$
   *(Se invierte la salida de la puerta NOR con un inversor NOR).*
3. **AND mediante NOR (aplicando De Morgan):**
   $$\text{AND}(A, B) = \overline{\bar{A} + \bar{B}} = A \cdot B$$
   *(Se invierten las entradas con puertas NOR y se alimentan a una puerta NOR final).*
