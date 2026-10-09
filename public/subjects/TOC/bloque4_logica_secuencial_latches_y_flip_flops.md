# Bloque 4: Lógica Secuencial, Latches y Flip-Flops

**Asignatura:** Tecnología y Organización de Computadores (TOC) — 1º Grado en Ingeniería Informática (UGR)  
**Contenido:** Fundamentos de sistemas secuenciales, realimentación, Latch SR asíncrono y síncrono, biestables disparados por flanco (D, JK, T), ecuaciones características y tablas de excitación.

---

## 1. Fundamentos de la Lógica Secuencial

A diferencia de los circuitos combinacionales (donde las salidas dependen exclusivamente de los valores actuales de las entradas), en un **circuito secuencial** las salidas dependen de las entradas actuales y de la **historia previa** del sistema, almacenada en variables de estado interno (*Memoria*):

$$\text{Salida}(t) = f(\text{Entradas}(t), \text{Estado}(t))$$
$$\text{Estado}(t+1) = g(\text{Entradas}(t), \text{Estado}(t))$$

El elemento básico de almacenamiento se logra introduciendo **realimentación** (*feedback*) en un lazo de puertas lógicas.

---

## 2. Latches (Cerrojos Asíncronos)

Los latches son dispositivos biestables sensibles al **nivel** de las señales de entrada.

### 2.1. Latch SR Asíncrono con Puertas NAND
Construido mediante dos puertas NAND cuyas salidas están conectadas de forma cruzada a las entradas opuestas:
* Funciona con lógica negativa en las entradas ($\bar{S}, \bar{R}$ activos a nivel bajo $0$):

| $S$ | $R$ | $Q(t+1)$ | $Q'(t+1)$ | Estado / Operación |
| :---: | :---: | :---: | :---: | :--- |
| 1 | 0 | 0 | 1 | **Reset** (Puesta a cero) |
| 0 | 1 | 1 | 0 | **Set** (Puesta a uno) |
| 1 | 1 | $Q(t)$ | $Q'(t)$ | **Memoria** (Sin cambio) |
| 0 | 0 | 1 | 1 | **Prohibido / Indeterminado** (Salidas contradictorias $Q = Q'$) |

* *Nota de diseño:* Si ambas entradas pasan bruscamente de $00$ a $11$, se produce una condición de carrera (*race condition*) impredecible.

### 2.2. Latch SR Sincronizado (con Señal de Habilitación / Enable)
Se añaden dos puertas NAND a la entrada controladas por la señal de reloj o habilitación $En$:
* Cuando $En = 0$: Las entradas $S$ y $R$ quedan bloqueadas. El latch permanece en estado de **memoria** ($Q(t+1) = Q(t)$).
* Cuando $En = 1$: El latch responde a las entradas $S$ y $R$ con lógica positiva:

| $En$ | $S$ | $R$ | $Q(t+1)$ | Comportamiento |
| :---: | :---: | :---: | :---: | :--- |
| 0 | X | X | $Q(t)$ | Memoria (No change) |
| 1 | 0 | 0 | $Q(t)$ | Memoria (No change) |
| 1 | 0 | 1 | 0 | **Reset** ($Q = 0$) |
| 1 | 1 | 0 | 1 | **Set** ($Q = 1$) |
| 1 | 1 | 1 | Indet. | **Indeterminado / Estado prohibido** |

---

## 3. Biestables / Flip-Flops Disparados por Flanco (Edge-Triggered)

Para evitar la transparencia del nivel alto y prevenir carreras críticas en circuitos complejos, los **Flip-Flops** muestrean las entradas y cambian su estado de salida exclusivamente durante la transición o **flanco** de la señal de reloj (*flanco de subida* $\uparrow$ o *flanco de bajada* $\downarrow$).

### 3.1. Flip-Flop D (Data / Delay)
Almacena directamente el bit presente en la entrada $D$ en el instante del flanco de reloj:
* **Tabla Característica:**

| $D$ | $Q(t+1)$ | Operación |
| :---: | :---: | :--- |
| 0 | 0 | Reset |
| 1 | 1 | Set |

* **Ecuación característica:**
  $$Q(t+1) = D$$
* **Aplicación principal:** Bancos de registros de procesadores, registros de desplazamiento (*shift registers*) y sincronización de señales asíncronas.

### 3.2. Flip-Flop JK (Universal)
Resuelve de forma definitiva el problema del estado prohibido del latch SR. Cuando ambas entradas son 1 ($J=K=1$), el biestable conmuta o **bascula** (*toggle*):
* **Tabla Característica:**

| $J$ | $K$ | $Q(t+1)$ | Operación |
| :---: | :---: | :---: | :--- |
| 0 | 0 | $Q(t)$ | Memoria (No change) |
| 0 | 1 | 0 | Reset ($Q=0$) |
| 1 | 0 | 1 | Set ($Q=1$) |
| 1 | 1 | $Q'(t)$ | **Complemento / Basculación (Toggle)** |

* **Ecuación característica:**
  $$Q(t+1) = J \cdot \bar{Q} + \bar{K} \cdot Q$$

### 3.3. Flip-Flop T (Toggle)
Dispone de una única entrada de control $T$. Se obtiene a partir de un Flip-Flop JK uniendo sus entradas ($J = K = T$) o con un Flip-Flop D mediante $D = T \oplus Q$:
* **Tabla Característica:**

| $T$ | $Q(t+1)$ | Operación |
| :---: | :---: | :--- |
| 0 | $Q(t)$ | Memoria (No pasa nada, retiene estado) |
| 1 | $Q'(t)$ | **Alternando (Invierte el estado anterior)** |

* **Ecuación característica:**
  $$Q(t+1) = T \oplus Q = T \bar{Q} + \bar{T} Q$$
* **Aplicación principal:** Contadores binarios síncronos y asíncronos y divisores de frecuencia por 2.

---

## 4. Tabla Comparativa de Excitación de Biestables

Para el diseño de autómatas finitos (FSM) y contadores, se requiere conocer qué entradas deben aplicarse para forzar una transición de estado $Q(t) \to Q(t+1)$:

| Transición $Q(t) \to Q(t+1)$ | Entrada $D$ | Entradas $J, K$ | Entrada $T$ |
| :---: | :---: | :---: | :---: |
| $0 \to 0$ | $0$ | $J=0, K=\text{X}$ | $0$ |
| $0 \to 1$ | $1$ | $J=1, K=\text{X}$ | $1$ |
| $1 \to 0$ | $0$ | $J=\text{X}, K=1$ | $1$ |
| $1 \to 1$ | $1$ | $J=\text{X}, K=0$ | $0$ |
