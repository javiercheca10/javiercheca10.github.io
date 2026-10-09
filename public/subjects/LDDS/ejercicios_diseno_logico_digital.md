# Ejercicios de Diseño Lógico Digital · Contadores & Mapas de Karnaugh
**Asignatura:** Logic Design of Digital Systems (LDDS)  
**Institución:** University of Piraeus (Atenas) · Erasmus+  
**Autor:** Francisco Javier Checa Casas  
**Documentos Fuente:** `EXERCISE_1.pdf`, `EXERCISE_2.pdf`  

---

## 1. Ejercicio 1: Análisis de Contador Binario Síncrono de 4 Bits

### Pregunta 1: Activación de la Salida de Acarreo ($C_{out}$)
* **Cuestión:** *When is the $C_{out}$ output of the binary counter turned on (logic 1)?*
* **Respuesta y Justificación:**
  * La salida de acarreo final (*Carry Out*, $C_{out}$) de un contador binario ascendente se activa (pasa a nivel lógico alto '1') exclusivamente cuando el contador alcanza su capacidad máxima de conteo antes del ciclo de desbordamiento (*overflow*).
  * Dado que se trata de un contador síncrono de 4 bits ($n = 4$), el valor máximo representable en binario es:
    $$1111_2 = 2^3 + 2^2 + 2^1 + 2^0 = 15_{10}$$
  * Por tanto, $C_{out} = 1$ en el estado 15, sirviendo como señal de habilitación en cascada para alimentar la entrada de acarreo de entrada ($C_{in}$) del siguiente contador de orden superior en diseños modulares de 8 o 16 bits.

### Pregunta 2: Entrada de Control de Reset
* **Cuestión:** *Drive the reset control input of the counter to 1. What do you observe?*
* **Respuesta y Justificación:**
  * Al forzar la entrada de inicialización `Reset = 1`, todas las salidas del contador ($Q_0, Q_1, Q_2, Q_3$) se reinician inmediatamente a nivel lógico '0' ($0000_2$).
  * En el circuito implementado, el reset actúa como una señal de prioridad dominante, forzando las salidas a cero con independencia de los pulsos del reloj (`Clk`) o del estado de la señal de habilitación (`Enable`).

### Pregunta 3: Entrada de Control de Habilitación (Enable)
* **Cuestión:** *Drive the enable control input of the counter to 0, while the reset is set to 0. What do you observe?*
* **Respuesta y Justificación:**
  * Al fijar `Enable = 0` con `Reset = 0`, el contador se congela en su estado actual.
  * El circuito ignora los flancos de subida del reloj de sistema, preservando el valor almacenado en los biestables internos ($Q_3 Q_2 Q_1 Q_0$) de forma estática hasta que la señal `Enable` vuelva a ponerse a '1'.

---

## 2. Ejercicio 2: Minimización con Mapas de Karnaugh de 4 Variables

### Definición del Problema
Minimizar la función lógica booleana $F(a, b, c, d)$ especificada mediante la sumatoria canónica de minitérminos:
$$F(a, b, c, d) = \sum m(0, 1, 2, 3, 4, 7, 11, 15)$$

### Estructura del Mapa de Karnaugh (4x4)
Las variables se organizan con código Gray en filas ($a, b$) y columnas ($c, d$):

| $ab \backslash cd$ | **00** | **01** | **11** | **10** |
| :---: | :---: | :---: | :---: | :---: |
| **00** | **1** ($m_0$) | **1** ($m_1$) | **1** ($m_3$) | **1** ($m_2$) |
| **01** | **1** ($m_4$) | 0 ($m_5$) | **1** ($m_7$) | 0 ($m_6$) |
| **11** | 0 ($m_{12}$) | 0 ($m_{13}$) | **1** ($m_{15}$) | 0 ($m_{14}$) |
| **10** | 0 ($m_8$) | 0 ($m_9$) | **1** ($m_{11}$) | 0 ($m_{10}$) |

### Agrupación de Minitérminos en Implicantes Primos
1. **Grupo 1 (Fila completa $ab = 00$):**
   * Agrupa los minitérminos $\{m_0, m_1, m_3, m_2\}$.
   * Al recorrer todas las columnas, las variables $c$ y $d$ se cancelan.
   * Término resultante: **$\overline{a} \cdot \overline{b}$** (o $a'b'$).
2. **Grupo 2 (Columna completa $cd = 11$):**
   * Agrupa los minitérminos $\{m_3, m_7, m_{15}, m_{11}\}$.
   * Al recorrer todas las filas, las variables $a$ y $b$ se cancelan.
   * Término resultante: **$c \cdot d$** (o $cd$).
3. **Grupo 3 (Adyacencia de tamaño 2 para cubrir $m_4$):**
   * El minitérmino $m_4$ ($ab cd = 0100$) se agrupa con el minitérmino $m_0$ ($0000$) aprovechando la adyacencia toroidal entre filas adyacentes con $c=0, d=0$.
   * Término resultante: **$\overline{a} \cdot \overline{c} \cdot \overline{d}$** (o $a'c'd'$).

### Expresión Booleana Mínima Final
$$F(a, b, c, d) = \overline{a} \cdot \overline{b} + c \cdot d + \overline{a} \cdot \overline{c} \cdot \overline{d}$$

Esta expresión mínima requiere únicamente tres puertas AND (dos de 2 entradas y una de 3 entradas) conectadas a una puerta OR final de 3 entradas, optimizando el área de silicio y la velocidad de propagación.
