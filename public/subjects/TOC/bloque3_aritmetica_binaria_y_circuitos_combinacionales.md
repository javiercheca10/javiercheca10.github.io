# Bloque 3: Aritmética con Signo, Mapas de Karnaugh y Circuitos Combinacionales

**Asignatura:** Tecnología y Organización de Computadores (TOC) — 1º Grado en Ingeniería Informática (UGR)  
**Contenido:** Representación con signo (C1, C2, Signo-Magnitud), detección de Overflow, optimización por Mapas de Karnaugh, metodología de diseño combinacional, sumadores/restadores y módulos MSI (comparadores, codificadores, decodificadores y multiplexores).

---

## 1. Aritmética Binaria con Signo y Complementos

Para representar números enteros con signo en palabras de $n$ bits existen tres esquemas fundamentales:

| Formato | Representación de $+N$ | Representación de $-N$ | Rango para $n=4$ bits | Cero |
| :--- | :---: | :---: | :---: | :---: |
| **Signo y Magnitud (SM)** | $0 \dots \text{magnitud}$ | $1 \dots \text{magnitud}$ | $[-7, +7]$ | Doble ($+0$ y $-0$) |
| **Complemento a 1 (C1)** | $0 \dots \text{bits}$ | Invertir todos los bits | $[-7, +7]$ | Doble ($0000$ y $1111$) |
| **Complemento a 2 (C2)** | $0 \dots \text{bits}$ | $C_1(N) + 1$ | $[-8, +7]$ | **Único ($0000$)** |

### 1.1. Propiedades del Complemento a 2 (Signed 2's Complement)
* **Cálculo directo:** Se invierten todos los bits del número positivo (C1) y se suma 1 al bit menos significativo (LSB).
  $$\text{Ejemplo: Representar } -3 \text{ en 4 bits: } +3 = 0011_2 \implies C_1 = 1100 \implies C_2 = 1100 + 1 = 1101_2$$
* **Truco rápido de inspección visual:** De derecha a izquierda, copiar los bits tal cual hasta encontrar el primer 1 (incluido). A partir de ahí, invertir todos los bits restantes.
* **Rango para $n$ bits:**
  $$[-2^{n-1}, +2^{n-1} - 1]$$
  *(Para 4 bits: $[-8, +7]$. El valor $-8$ es $1000_2$, sin contraparte positiva).*

### 1.2. Resta Binaria en Complemento a 2
La resta $X - Y$ se efectúa directamente como la suma de $X$ con el opuesto de $Y$:
$$X - Y = X + (-Y) = X + C_2(Y) = X + C_1(Y) + 1$$

En hardware, se alimenta $X$ a un sumador, se invierten los bits de $Y$ con puertas XOR o inversores, y se introduce un acarreo inicial $C_{in} = 1$:

$$\begin{array}{r@{\quad}l}
  (+4) & 0100 \\
- (+3) & 1100 \quad (\text{invertido } C_1) \\
\text{carry inicial} & +1 \\
\hline
  (+1) & 0001
\end{array}$$

### 1.3. Desbordamiento Aritmético (Overflow)
Ocurre cuando el resultado de una operación aritmética excede el rango representable del número de bits:
* Solo puede suceder al **sumar dos números del mismo signo**:
  * Positivo $+$ Positivo $\to$ Resultado con bit de signo 1 (aparentemente negativo) $\implies$ **Overflow**.
  * Negativo $+$ Negativo $\to$ Resultado con bit de signo 0 (aparentemente positivo) $\implies$ **Overflow**.
* **Detección en hardware mediante acarreos:**
  $$V = C_n \oplus C_{n-1}$$
  *Hay desbordamiento si el acarreo que entra al bit de signo ($C_{n-1}$) es distinto del acarreo que sale del bit de signo ($C_n$).*

---

## 2. Optimización Lógica mediante Mapas de Karnaugh (K-Maps)

Los mapas de Karnaugh son diagramas bidimensionales donde cada celda corresponde a un minterm. Las celdas adyacentes representan términos que difieren en una sola variable gracias a la ordenación en **Código Gray**.

### 2.1. Estructura según Número de Variables
* **2 Variables ($A, B$):** Cuadrícula de $2 \times 2$.
* **3 Variables ($A, BC$):** Cuadrícula de $2 \times 4$ (columnas $BC: 00, 01, 11, 10$).
* **4 Variables ($AB, CD$):** Cuadrícula de $4 \times 4$ (filas y columnas en secuencia $00, 01, 11, 10$).

### 2.2. Reglas de Agrupamiento
1. Los grupos deben ser **rectángulos de tamaño potencia de 2** ($1, 2, 4, 8, 16$).
2. Cada grupo debe contener exclusivamente unos (para SOP) o ceros (para POS).
3. **Adyacencia toroidal:** Los bordes izquierdo y derecho son adyacentes; los bordes superior e inferior son adyacentes. Las 4 esquinas del mapa de 4 variables forman un grupo válido de 4 celdas.
4. **Simplificación:** Para cada grupo, se eliminan todas las variables que cambien de valor (0 y 1) dentro de las celdas agrupadas. Se conservan únicamente las variables constantes.
5. El número total de grupos debe ser el mínimo posible y cada grupo debe ser tan grande como sea posible.

### 2.3. Condiciones de Indiferencia (Don't Care, $d$ o $X$)
Combinaciones de entrada que nunca ocurrirán en la práctica (por ejemplo, los valores $1010 \dots 1111$ en BCD) o cuyas salidas son irrelevantes:
* En el mapa de Karnaugh, un término $X$ puede tomarse como $1$ si permite formar un grupo más grande.
* Si no ayuda a simplificar ningún grupo de 1s, se toma como $0$ y se ignora.

---

## 3. Metodología de Diseño de Circuitos Combinacionales

El flujo sistemático para diseñar un circuito lógico digital consta de 4 etapas:
1. **Especificación:** Definir con precisión las variables de entrada (*Inputs*) y las funciones de salida (*Outputs*).
2. **Tabla de verdad:** Enumerar las $2^n$ combinaciones posibles y asignar los valores de salida correspondientes.
3. **Minimización booleana:** Obtener las funciones algebraicas simplificadas para cada salida mediante Mapas de Karnaugh o álgebra booleana.
4. **Diagrama lógico:** Dibujar el esquema electrónico con puertas lógicas interconectadas.

---

## 4. Sumadores y Restadores Aritméticos

### 4.1. Semisumador (Half Adder)
Suma dos bits independientes $x, y$:
* **Tabla de verdad:**

| $x$ | $y$ | Carry ($C$) | Sum ($S$) |
| :---: | :---: | :---: | :---: |
| 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 0 |

* **Ecuaciones:**
  $$S = x \cdot y' + x' \cdot y = x \oplus y \qquad C = x \cdot y$$

### 4.2. Sumador Completo (Full Adder)
Suma tres bits: $x$, $y$, y el acarreo entrante $z = C_{in}$:
* **Ecuaciones simplificadas por K-Map:**
  $$S = x'y'z + x'yz' + xy'z' + xyz = x \oplus y \oplus z$$
  $$C_{out} = xy + xz + yz$$

### 4.3. Sumador-Restador de 4 Bits con Control de Modo y Overflow
Construido encadenando 4 etapas *Full Adder* (FA) con propagación de acarreo (*Ripple Carry*):
* **Línea de Modo $M$:**
  * Conectada al acarreo inicial $C_0 = M$ y a una entrada de cada puerta XOR en las líneas del operando $B$:
    * Si $M = 0$: $B_i \oplus 0 = B_i$, $C_0 = 0 \implies \text{Operación } A + B$ (Suma).
    * Si $M = 1$: $B_i \oplus 1 = \overline{B_i}$, $C_0 = 1 \implies \text{Operación } A + \bar{B} + 1 = A - B$ (Resta en C2).
* **Detector de Overflow ($V$):**
  $$V = C_4 \oplus C_3$$
  *(Si $C_4 \neq C_3$, la puerta XOR activa $V=1$ señalando error de desbordamiento).*

---

## 5. Módulos Combinacionales MSI Estándar

### 5.1. Comparadores de Magnitud (2 y 4 bits)
Comparan dos números binarios $A$ y $B$ generando tres salidas mutuamente excluyentes: $A > B$, $A = B$ y $A < B$.
* **Condición de igualdad bit a bit ($A_i = B_i$):** Viene dada por la función XNOR:
  $$x_i = A_i B_i + A'_i B'_i = (A_i \oplus B_i)'$$
* Para 4 bits ($A_3 A_2 A_1 A_0$ y $B_3 B_2 B_1 B_0$):
  $$(A = B) = x_3 \cdot x_2 \cdot x_1 \cdot x_0$$
  $$(A > B) = A_3 B'_3 + x_3 A_2 B'_2 + x_3 x_2 A_1 B'_1 + x_3 x_2 x_1 A_0 B'_0$$
  $$(A < B) = A'_3 B_3 + x_3 A'_2 B_2 + x_3 x_2 A'_1 B_1 + x_3 x_2 x_1 A'_0 B_0$$

### 5.2. Codificadores y Decodificadores
* **Decodificador $n$ a $2^n$:** Activa una única línea de salida entre $2^n$ según la combinación binaria presente en sus $n$ entradas. Con entrada de habilitación *Enable* ($En$), funciona como demultiplexor.
* **Codificador sin prioridad (8 a 3):** Asume que solo una línea de entrada $D_0 \dots D_7$ está a 1 en cada instante:
  $$z = D_1 + D_3 + D_5 + D_7 \qquad y = D_2 + D_3 + D_6 + D_7 \qquad x = D_4 + D_5 + D_6 + D_7$$
* **Codificador con Prioridad (4 a 2):** Permite que múltiples entradas estén activas simultáneamente; la salida refleja el índice de mayor prioridad ($D_3 > D_2 > D_1 > D_0$). Incluye una salida de validez $V=1$ si al menos una entrada está activa:

| $D_0$ | $D_1$ | $D_2$ | $D_3$ | $x$ | $y$ | $V$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 0 | 0 | 0 | 0 | X | X | 0 |
| 1 | 0 | 0 | 0 | 0 | 0 | 1 |
| X | 1 | 0 | 0 | 0 | 1 | 1 |
| X | X | 1 | 0 | 1 | 0 | 1 |
| X | X | X | 1 | 1 | 1 | 1 |

### 5.3. Multiplexores (MUX)
Selector multicanal con $2^n$ entradas de datos, $n$ líneas de selección y 1 salida.
* **MUX $4 \times 1$:** Con líneas de selección $S_1, S_0$ y datos $I_0, I_1, I_2, I_3$:
  $$F = S'_1 S'_0 I_0 + S'_1 S_0 I_1 + S_1 S'_0 I_2 + S_1 S_0 I_3$$
* **Síntesis de funciones lógicas arbitrarias con MUX:**
  Cualquier función de $n$ variables puede implementarse directamente con un MUX de $2^{n-1}$ entradas asignando $n-1$ variables a las líneas de selección y conectando a las entradas de datos los valores $0, 1, z$ o $z'$ deducidos de la tabla de verdad.
