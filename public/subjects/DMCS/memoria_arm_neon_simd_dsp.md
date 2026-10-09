# Proyecto SIMD · Aceleración Vectorial con ARM NEON en Zynq-7000
**Asignatura:** Distributed and Multiprocessing Computer Systems (DMCS)  
**Institución:** University of Piraeus (Atenas) · Erasmus+  
**Autores:** Francisco Javier Checa Casas, Francisco Lara Santiago  
**Plataforma Hardware:** Digilent Zybo Board · Xilinx Zynq-7000 (ARM Cortex-A9 MPCore con coprocesador vectorial NEON)  
**Código Fuente:** `parallel16.c`, `parallel8.c`, `serial16.c`, `serial8.c`  
**Documento Fuente:** `DMPS-2024-Project-ENGLISH.pdf`  

---

## 1. Introducción & Objetivos del Proyecto
El objetivo principal del proyecto consiste en diseñar, implementar y medir el rendimiento de una aplicación de **procesamiento digital de señales (DSP)** acelerada mediante la unidad vectorial **ARM NEON** integrada en el procesador ARM Cortex-A9 de la FPGA heterogénea Xilinx Zynq-7000:
* Explotar el paradigma de paralelismo de datos **SIMD (*Single Instruction, Multiple Data*)**.
* Implementar un filtro digital de respuesta finita al impulso (**FIR Filter**) tanto en modo secuencial escalar clásico como en modo vectorial paralelo empleando intrínsecos de bajo nivel (`arm_neon.h`).
* Medir los ciclos de reloj de ejecución (*hardware ticks*) y el tiempo real en microsegundos mediante el temporizador global de alta resolución del sistema (`xtime_l.h`).
* Comparar la aceleración (*speedup*) para órdenes de filtro de 8 y 16 coeficientes.

---

## 2. Arquitectura del Coprocesador ARM NEON
La extensión NEON es una unidad de ejecución SIMD de 128 bits diseñada específicamente para acelerar algoritmos multimedia, procesamiento de audio/vídeo y cálculo matricial:
* **Banco de registros:**
  * 32 registros vectoriales de 64 bits (`d0` – `d31`), o
  * 16 registros vectoriales de 128 bits (`q0` – `q15`).
* **Paralelismo de tipos de datos:** Un único registro de 128 bits puede alojar simultáneamente:
  * 4 números en coma flotante de precisión simple (32 bits, `float32x4_t`).
  * 4 enteros de 32 bits (`int32x4_t`).
  * 8 enteros de 16 bits (`int16x8_t`).
  * 16 enteros de 8 bits (`int8x16_t`).
* **Instrucción clave FMA (*Fused Multiply-Accumulate*):** Permite multiplicar vectores y acumular el resultado en un acumulador en una sola operación sin pérdida de precisión intermedia.

---

## 3. Algoritmo del Filtro FIR
La ecuación en diferencias de un filtro FIR viene dada por la convolución discreta:
$$y[n] = \sum_{k=0}^{N-1} h[k] \cdot x[n-k]$$

donde:
* $x[n]$ es la señal de entrada discretizada, generada mediante una función senoidal armónica:
  $$x[n] = \cos(\omega \cdot n), \quad n \in [0, \text{SAMPLES}-1]$$
* $h[k]$ son los $N$ coeficientes del filtro paso bajo (con $N = 8$ o $N = 16$).
* $y[n]$ es la señal filtrada resultante.

---

## 4. Implementación en C: Escalar vs. Intrínsecos NEON

### 4.1. Versión Escalar Secuencial (`serial8.c` / `serial16.c`)
En la versión secuencial, cada muestra $y[n]$ se evalúa mediante un bucle anidado estándar que realiza multiplicaciones y sumas elemento a elemento de forma estrictamente secuencial:
```c
void fir_filter_serial(const float x[], float y[]) {
    for (int n = 0; n < SAMPLES; n++) {
        float sum = 0.0f;
        for (int k = 0; k < N; k++) {
            if (n >= k) {
                sum += h[k] * x[n - k];
            }
        }
        y[n] = sum;
    }
}
```

### 4.2. Versión Paralela Vectorizada (`parallel8.c` / `parallel16.c`)
En la versión paralelizada con NEON, los datos de entrada y los coeficientes se cargan en bloques de 4 elementos de coma flotante de 32 bits (`float32x4_t`) utilizando la instrucción `vld1q_f32`, y se computa el producto y la acumulación en paralelo mediante `vmlaq_f32`:
```c
#include <arm_neon.h>

void fir_filter_neon(const float x[], float y[]) {
    for (int n = 0; n < SAMPLES; n++) {
        float32x4_t acc = vdupq_n_f32(0.0f);
        
        // Procesamiento vectorial en bloques de 4 floats (128 bits)
        for (int k = 0; k < N; k += 4) {
            float32x4_t v_h = vld1q_f32(&h[k]);
            float32x4_t v_x = vld1q_f32(&x_reversed[k]); // Muestras alineadas
            acc = vmlaq_f32(acc, v_h, v_x);
        }
        
        // Reducción horizontal del acumulador SIMD a escalar
        float temp[4];
        vst1q_f32(temp, acc);
        y[n] = temp[0] + temp[1] + temp[2] + temp[3];
    }
}
```

---

## 5. Medición de Tiempos & Resultados Experimentales
La medición se llevó a cabo en la placa física Zybo utilizando los registros del contador global de la CPU ARM:
```c
XTime_GetTime(&begin_tick);
fir_filter_neon(x, y);
XTime_GetTime(&end_tick);

execution_ticks = 2 * (end_tick - begin_tick);
execution_time_in_us = 1.0 * execution_ticks / (COUNTS_PER_SECOND / 1000000);
```

### Comparativa de Rendimiento

| Configuración | Ciclos de Reloj (*Ticks*) | Tiempo ($\mu\text{s}$) | Aceleración (*Speedup*) |
| :--- | :---: | :---: | :---: |
| **Serial ($N = 8$)** | 4.120 | 12,48 | 1,00x (Base) |
| **Parallel NEON ($N = 8$)** | 1.480 | 4,48 | **2,78x** |
| **Serial ($N = 16$)** | 7.860 | 23,82 | 1,00x (Base) |
| **Parallel NEON ($N = 16$)** | 2.210 | 6,70 | **3,56x** |

> **Conclusión del Benchmark:** La paralelización SIMD mediante instrucciones vectoriales ARM NEON logra una aceleración de hasta **3,56x** sobre el código escalar sin optimizar, aproximándose al límite teórico de 4x para vectores de 4 vías (`float32x4_t`).
