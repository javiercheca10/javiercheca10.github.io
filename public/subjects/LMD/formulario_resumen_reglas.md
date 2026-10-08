# Formulario Maestro de Lógica, Álgebra de Boole y Métodos Discretos

---

## 1. Álgebra de Boole

### Funciones Booleanas Básicas
Representación mediante tablas de verdad:

| OR ($+$) | 0 | 1 |
| :--- | :---: | :---: |
| **0** | 0 | 1 |
| **1** | 1 | 1 |

| AND ($\cdot$) | 0 | 1 |
| :--- | :---: | :---: |
| **0** | 0 | 0 |
| **1** | 0 | 1 |

**Propiedades NOT:**
* $\overline{\overline{x}} = x$
* $\overline{x + y} = \overline{x} \cdot \overline{y}$
* $\overline{x \cdot y} = \overline{x} + \overline{y}$

### Optimización de Funciones: Mapas de Karnaugh y Quine-McCluskey
**Ejemplo:** $f(x, y, z, t) = xyzt + \overline{x}y\overline{z}t + x\overline{y}zt + xy\overline{z}t + \overline{x}\overline{y}zt + \overline{x}yzt$

1. **Tabla de Karnaugh:**
   * Agrupación de 1s para obtener términos simplificados.
   * Resultados parciales: $a_1 = yt$, $a_2 = zt$.
   * Función simplificada: $S = yt + zt$.

2. **Algoritmo de Quine-McCluskey:**
   * Se agrupan los minterms por número de unos.
   * Se comparan grupos adyacentes para simplificar variables (solo se permite el cambio de una variable).
   * Proceso iterativo hasta obtener los implicantes primos esenciales.

### Conversión a NAND / NOR
* $x + y = \overline{\overline{x + y}} = \overline{\overline{x} \cdot \overline{y}}$
* $x \cdot y = \overline{\overline{x \cdot y}} = \overline{\overline{x} + \overline{y}}$
* **NAND:** $x \uparrow y = \overline{x \cdot y}$
* **NOR:** $x \downarrow y = \overline{x + y}$

---

## 2. Lógica de Predicados y Forma Clausulada

### Definiciones
* **Literal:** Una variable atómica $p, q$ o su negación $\neg p, \neg q$.
* **Cláusula:** Disyunción de literales que no contenga una variable y su negado simultáneamente. Si no contiene literales, se denomina **cláusula vacía** ($\square$).
* **Forma Clausulada:** Una fórmula escrita como conjunción de cláusulas.

### Teorema de Transformación
Si $\alpha$ no es una tautología, existe una fórmula $\beta$ lógicamente equivalente en forma clausulada. Reglas de transformación:
1. $\alpha_1 \leftrightarrow \alpha_2 \equiv (\alpha_1 \to \alpha_2) \land (\alpha_2 \to \alpha_1)$
2. $\alpha_1 \to \alpha_2 \equiv \neg \alpha_1 \lor \alpha_2$
3. $\neg \neg \alpha \equiv \alpha$
4. $\neg(\alpha_1 \land \alpha_2) \equiv \neg \alpha_1 \lor \neg \alpha_2$
5. $(\alpha_1 \land \alpha_2) \lor \beta \equiv (\alpha_1 \lor \beta) \land (\alpha_2 \lor \beta)$

### Reglas de Simplificación
* Eliminación de $\lambda \lor \lambda^c$
* $\beta \lor \beta \equiv \beta$
* $(\beta \lor \sigma) \land \beta \equiv \beta$
* $(\alpha \lor \beta) \land (\alpha \lor \neg \beta) \equiv \alpha$

### Algoritmo de Davis-Putnam
Para determinar la insatisfacibilidad de un conjunto de cláusulas $T$:
1. **Cláusula unitaria:** Si existe una cláusula con un solo literal, el conjunto es insatisfacible si y solo si la reducción unitaria es insatisfacible.
2. **Literal puro:** Si un literal aparece pero su negado no, el conjunto es insatisfacible si y solo si el conjunto reducido es insatisfacible.
3. **Regla de división:** Si no se aplican 1 o 2, elegir $\lambda$ arbitrario; el conjunto es insatisfacible si y solo si tanto $T \cup \{\lambda\}$ como $T \cup \{\neg \lambda\}$ son insatisfacibles.

> **Nota:** Si la cláusula vacía pertenece a todas las hojas del árbol de decisión, el conjunto original es insatisfacible.

---

## 3. Análisis Matemático y Optimización

### Clasificación de Cuadráticas
Dada una matriz Hessiana $A$:
* **DP (Definida Positiva):** $H_1 > 0, H_2 > 0, H_3 > 0$
* **DN (Definida Negativa):** $H_1 < 0, H_2 > 0, H_3 < 0$
* **S.D.P (Semidefinida Positiva):** $H_1 > 0, H_2 > 0, H_3 = 0$
* **S.D.N (Semidefinida Negativa):** $H_1 < 0, H_2 > 0, H_3 = 0$

### Métodos de Optimización
* **Vector Gradiente:** $\nabla F = \left( \frac{\partial F}{\partial x}, \frac{\partial F}{\partial y} \right)$. En restricciones, se igualan vectores proporcionales.
* **Teorema de Schwarz:** $\frac{\partial^2 f}{\partial x \partial y} = \frac{\partial^2 f}{\partial y \partial x}$.
* **Teorema de Euler:** Para funciones homogéneas de grado $m$: $x \frac{\partial f}{\partial x} + y \frac{\partial f}{\partial y} = m \cdot f(x, y)$.
* **Taylor (Grado 2):** 
$$f(x, y) \approx f(x_0, y_0) + f_x(x-x_0) + f_y(y-y_0) + \frac{1}{2!} [f_{xx}(x-x_0)^2 + 2f_{xy}(x-x_0)(y-y_0) + f_{yy}(y-y_0)^2]$$

### Criterios de Puntos Críticos
| Tipo | Carácter |
| :--- | :--- |
| Definida positiva | Mínimo local |
| Definida negativa | Máximo local |
| Semidefinida positiva | Mínimo local o punto de silla |
| Semidefinida negativa | Máximo local o punto de silla |
| Indefinida | Punto de silla |