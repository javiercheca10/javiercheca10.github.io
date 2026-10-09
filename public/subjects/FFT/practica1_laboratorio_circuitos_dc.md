# Práctica de Laboratorio 1: Simulación de Circuitos DC y Divisores de Tensión

**Asignatura:** Fundamentos Físicos y Tecnológicos (FFT)  
**Institución:** Universidad de Granada (UGR) · Doble Grado Informática + ADE  
**Autor:** Francisco Javier Checa Casas  
**Herramientas CAD:** CircuitMaker / SPICE / Qucs  

---

## 1. Fundamentos Teóricos del Divisor de Tensión

Un divisor de tensión es una configuración de dos o más impedancias o resistencias en serie conectadas a una fuente de alimentación de tensión continua $V$. 

Para dos resistencias $R_1$ y $R_2$ en serie sometidas a un potencial $V$:
1. **Corriente del circuito en serie:**
   $$I = \frac{V}{R_1 + R_2}$$
2. **Caída de tensión en $R_1$:**
   $$V_1 = I \cdot R_1 = V \cdot \frac{R_1}{R_1 + R_2}$$
3. **Caída de tensión en $R_2$:**
   $$V_2 = I \cdot R_2 = V \cdot \frac{R_2}{R_1 + R_2}$$
4. **Ley de Voltajes de Kirchhoff (LVK):**
   $$V_1 + V_2 = V$$

---

## 2. Metodología Experimental y Simulación DC

En el laboratorio se simulan los esquemas circuitales fijando una fuente DC de $V = 10\text{ V}$ y variando los valores resistivos para analizar el efecto de carga:

* **Medición de Tensión:** Colocación de sondas voltimétricas en paralelo con cada componente ($V_1$, $V_2$).
* **Medición de Intensidad:** Colocación de amperímetros o sondas de corriente en serie ($I_1 = I_2 = I$).
* **Condición de Simetría ($R_1 = R_2$):** La tensión se divide equitativamente a la mitad ($V_1 = V_2 = 5\text{ V}$).
* **Efecto de Carga con Resistencia Desbalanceada:** Cuando $R_2 \gg R_1$, la mayor parte de la caída de potencial se concentra en $R_2$, verificando el comportamiento asintótico $V_2 \to V$.

---

## 3. Archivos y Esquemas de Simulación Disponibles

En la pestaña de descargas se encuentran disponibles los archivos de diseño esquemático y las memorias de laboratorio:

* `laboratoriofft1.pdf` · Memoria oficial cumplimentada de la Práctica 1 de Laboratorio.
* `laboratorioFFT.pdf` · Guía y enunciado completo de los experimentos circuitales.
* `laboratorio1_fft.sch` & `laboratorio2_fft.sch` · Esquemas de simulación circuital (.SCH).
* `Circuit3.cct` · Archivo de simulación CAD CircuitMaker con esquemático activo y sondas virtuales.
* `ejercicio1_fft.png` & `ejercicio2_fft.png` · Capturas de las simulaciones y lecturas de instrumentación.
