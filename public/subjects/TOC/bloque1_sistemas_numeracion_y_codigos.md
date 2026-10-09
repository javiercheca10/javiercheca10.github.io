# Bloque 1: Sistemas de Numeración, Códigos Binarios y Nivel RTL

**Asignatura:** Tecnología y Organización de Computadores (TOC) — 1º Grado en Ingeniería Informática (UGR)  
**Contenido:** Bases de numeración, aritmética binaria elemental, conversiones, códigos BCD, Gray y ASCII, y arquitectura a nivel de transferencia de registros (RTL).

---

## 1. Sistemas de Numeración Posicionales

Un sistema de numeración posicional representa cualquier cantidad numérica mediante una cadena de dígitos donde el peso de cada posición viene determinado por una potencia entera de la base $r$:

$$N = (d_{n-1} d_{n-2} \dots d_1 d_0 . d_{-1} d_{-2} \dots d_{-m})_r = \sum_{i=-m}^{n-1} d_i \cdot r^i$$

### 1.1. Base 2 (Sistema Binario)
* **Alfabeto de dígitos:** $\Sigma = \{0, 1\}$.
* **Capacidad de representación:** Con $n$ bits se pueden representar exactamente $2^n$ combinaciones distintas (rango sin signo: $[0, 2^n - 1]$).
* **Ejemplo de descomposición polinómica:**
  $$(11001)_2 = 1 \cdot 2^4 + 1 \cdot 2^3 + 0 \cdot 2^2 + 0 \cdot 2^1 + 1 \cdot 2^0 = 16 + 8 + 0 + 0 + 1 = 25_{10}$$

### 1.2. Base 16 (Sistema Hexadecimal)
* **Alfabeto de dígitos:** $\Sigma = \{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, \text{A}, \text{B}, \text{C}, \text{D}, \text{E}, \text{F}\}$.
* **Equivalencias decimales:** $\text{A}=10, \text{B}=11, \text{C}=12, \text{D}=13, \text{E}=14, \text{F}=15$.
* **Ejemplo de descomposición polinómica:**
  $$(1\text{AF})_{16} = 1 \cdot 16^2 + 10 \cdot 16^1 + 15 \cdot 16^0 = 256 + 160 + 15 = 431_{10}$$

### 1.3. Base 8 (Sistema Octal)
* **Alfabeto de dígitos:** $\Sigma = \{0, 1, 2, 3, 4, 5, 6, 7\}$.
* Cada dígito octal equivale de forma directa a una terna de 3 bits binarios ($2^3 = 8$).

---

## 2. Métodos de Conversión entre Bases

### 2.1. Conversión de Decimal a Binario (Parte Entera)
Se aplica el método de las **divisiones sucesivas entre 2**. El cociente se vuelve a dividir hasta llegar a 0. Los restos obtenidos conforman el número binario leídos desde el último al primero:
* El **primer resto** obtenido es el bit menos significativo (**LSB**, *Least Significant Bit*).
* El **último resto** obtenido es el bit más significativo (**MSB**, *Most Significant Bit*).

**Ejemplo: Convertir $41_{10}$ a binario:**
1. $41 / 2 = 20$, resto $= 1$ $\rightarrow$ (LSB)
2. $20 / 2 = 10$, resto $= 0$
3. $10 / 2 = 5$, resto $= 0$
4. $5 / 2 = 2$, resto $= 1$
5. $2 / 2 = 1$, resto $= 0$
6. $1 / 2 = 0$, resto $= 1$ $\rightarrow$ (MSB)

Lectura de abajo hacia arriba:
$$41_{10} = 101001_2$$

### 2.2. Conversión de Decimal a Binario / Octal (Parte Fraccionaria)
Para la parte decimal tras la coma, se realizan **multiplicaciones sucesivas por la base**:
1. Se multiplica la parte fraccionaria por la base (2 u 8).
2. La parte entera del resultado (0 o 1 en binario) pasa a ser el dígito tras la coma.
3. Se repite el proceso con la parte decimal sobrante hasta alcanzar la precisión deseada o hasta que el resto sea cero.

### 2.3. Conversión Rápida Binario $\leftrightarrow$ Hexadecimal y Binario $\leftrightarrow$ Octal
Debido a que $16 = 2^4$ y $8 = 2^3$:
* **Binario a Hexadecimal:** Agrupar en bloques de **4 bits** de derecha a izquierda (añadiendo ceros a la izquierda si es necesario) y sustituir cada bloque por su dígito hexadecimal.
  $$\underbrace{0001}_{1} \quad \underbrace{1011}_{\text{B}} \quad \underbrace{1111}_{\text{F}} \quad \underbrace{1010}_{\text{A}} \implies 1\text{BFA}_{16}$$
* **Hexadecimal a Binario:** Expandir cada dígito hexadecimal a su cuarteto de 4 bits.
  $$\text{F4E2}_{16} = \underbrace{1111}_{\text{F}} \quad \underbrace{0100}_{4} \quad \underbrace{1110}_{\text{E}} \quad \underbrace{0010}_{2} = 1111010011100010_2$$
* **Binario a Octal:** Agrupar en bloques de **3 bits** de derecha a izquierda.

---

## 3. Tabla Comparativa de Sistemas de Numeración (0 a 15)

| Decimal ($r=10$) | Binario ($r=2$) | Octal ($r=8$) | Hexadecimal ($r=16$) |
| :---: | :---: | :---: | :---: |
| 00 | 0000 | 00 | 0 |
| 01 | 0001 | 01 | 1 |
| 02 | 0010 | 02 | 2 |
| 03 | 0011 | 03 | 3 |
| 04 | 0100 | 04 | 4 |
| 05 | 0101 | 05 | 5 |
| 06 | 0110 | 06 | 6 |
| 07 | 0111 | 07 | 7 |
| 08 | 1000 | 10 | 8 |
| 09 | 1001 | 11 | 9 |
| 10 | 1010 | 12 | A |
| 11 | 1011 | 13 | B |
| 12 | 1100 | 14 | C |
| 13 | 1101 | 15 | D |
| 14 | 1110 | 16 | E |
| 15 | 1111 | 17 | F |

---

## 4. Códigos Binarios

### 4.1. Código BCD (Binary Coded Decimal - 8421)
Codifica cada dígito decimal individual (0 al 9) en un cuarteto de 4 bits independientes:

| Dígito Decimal | Código BCD |
| :---: | :---: |
| 0 | 0000 |
| 1 | 0001 |
| 2 | 0010 |
| 3 | 0011 |
| 4 | 0100 |
| 5 | 0101 |
| 6 | 0110 |
| 7 | 0111 |
| 8 | 1000 |
| 9 | 1001 |

* *Combinaciones prohibidas / no válidas en BCD:* Del $1010$ al $1111$ (10 a 15 en decimal).
* **Suma BCD y regla de corrección:**
  Al sumar dos números en BCD cuarteto a cuarteto:
  1. Si la suma binaria da un valor entre $0$ y $9$ y no hay acarreo al siguiente dígito, el resultado es correcto.
  2. Si la suma da un valor mayor que 9 (un cuarteto inválido $1010 \dots 1111$) o genera un acarreo de 4 bits ($C_{out} = 1$), se debe aplicar la **corrección obligatoria sumando 6 ($0110_2$)**. Esto salta los 6 estados inválidos del cuarteto y genera el acarreo decimal correspondiente.

### 4.2. Código Gray (Código Reflejado)
Propiedad esencial: **Dos valores numéricos consecutivos difieren en un único bit** (distancia de Hamming = 1).
* **Aplicación crítica:** Se utiliza para etiquetar las filas y columnas de los **Mapas de Karnaugh**, garantizando que las celdas adyacentes físicamente representen términos con una sola variable complementada. También previene errores de conmutación en encoders ópticos de posición angular.

| Decimal | Binario Natural | Código Gray |
| :---: | :---: | :---: |
| 0 | 0000 | 0000 |
| 1 | 0001 | 0001 |
| 2 | 0010 | 0011 |
| 3 | 0011 | 0010 |
| 4 | 0100 | 0110 |
| 5 | 0101 | 0111 |
| 6 | 0110 | 0101 |
| 7 | 0111 | 0100 |
| 8 | 1000 | 1100 |
| 9 | 1001 | 1101 |
| 10 | 1010 | 1111 |
| 11 | 1011 | 1110 |
| 12 | 1100 | 1010 |
| 13 | 1101 | 1011 |
| 14 | 1110 | 1001 |
| 15 | 1111 | 1000 |

### 4.3. Código Alfanumérico ASCII (7 bits)
El estándar ASCII (*American Standard Code for Information Interchange*) utiliza cadenas de 7 bits ($2^7 = 128$ símbolos):
* **Caracteres de control:** 32 códigos iniciales (0 a 31) para gestión de comunicaciones y formato: `NUL` (0), `SOH` (1), `STX` (2), `ETX` (3), `EOT` (4), `ACK` (6), `BEL` (7), `BS` (8), `HT` (9), `LF` (10), `VT` (11), `FF` (12), `CR` (13), `ESC` (27), `DEL` (127).
* **Caracteres imprimibles:** Dígitos `'0'` a `'9'` (códigos $0110000_2$ a $0111001_2$, es decir $48_{10}$ a $57_{10}$), letras mayúsculas `'A'` a `'Z'` ($65_{10}$ a $90_{10}$) y minúsculas `'a'` a `'z'` ($97_{10}$ a $122_{10}$).

---

## 5. Nivel de Transferencia de Registros (RTL)

### 5.1. Concepto de Registro
* **Célula binaria:** Dispositivo biestable capaz de mantener de manera estable uno de dos estados posibles ($0$ o $1$), almacenando 1 bit de información.
* **Registro:** Agrupación coordinada de $n$ células binarias que almacena una palabra digital de $n$ bits y comparte líneas comunes de reloj y control.

### 5.2. Flujo de Datos y Tratamiento de la Información
En una arquitectura digital básica:
1. **Unidad de Entrada (Input Unit):** Recibe datos del exterior (teclado, interfaz serie) y los deposita en un registro de entrada temporal (*Input Register*).
2. **Unidad de Memoria (Memory Unit):** Almacena instrucciones y operandos organizados en palabras de memoria direccionables.
3. **Unidad de Procesador (Processor Unit / ALU):**
   * Transfiere operandos desde la memoria a registros internos de trabajo ($R_1, R_2$).
   * Circuitos combinacionales lógicos (como sumadores o ALUs) computan la operación ($R_3 = R_1 + R_2$).
   * El resultado en $R_3$ es transferido de vuelta al registro de datos de memoria o enviado a periféricos de salida.
