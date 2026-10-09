# Prácticas de Laboratorio con wxMaxima · Cálculo

**Asignatura:** Cálculo (CAL)  
**Institución:** Universidad de Granada (UGR) · Doble Grado Informática + ADE  
**Autor:** Francisco Javier Checa Casas  
**Herramienta Computacional:** wxMaxima (Computer Algebra System - CAS)  

---

## 1. Introducción al Cálculo Simbólico y Numérico con Maxima

Las prácticas de la asignatura integran el cálculo analítico formal con la computación simbólica y numérica mediante **wxMaxima**, abordando:
1. **Desarrollo en Polinomios de Taylor** en puntos arbitrarios con control de grado.
2. **Implementación de Algoritmos Numéricos:** Método de Newton-Raphson para resolución de ecuaciones no lineales $g(x) = k$ con tolerancias de error relativo $\le 10^{-11}$.
3. **Cálculo Integral y Cuadratura Numérica:** Integración simbólica y numérica de áreas delimitadas por curvas.
4. **Representación Gráfica 2D:** Visualización conjunta de funciones y polinomios aproximantes con `wxdraw2d`.

---

## 2. Examen de Prácticas: Segundo Parcial (Grupo D2)

### Enunciado Oficial (18 de Diciembre de 2023)

#### Problema 1: Taylor y Método de Newton-Raphson (5 Puntos)
Sea $f: \mathbb{R} \to \mathbb{R}$ definida por:
$$f(x) := 6 + \arctan(x) + \frac{e^{x^2 + 5x + 12}}{x}$$
y sea $g(x)$ el polinomio de Taylor centrado en $x_0 = 2$ de grado $n = 8$.

> **Objetivo:** Programar el algoritmo de Newton-Raphson para aproximar la raíz de la ecuación $g(x) = 10$, inicializando en $a = 5.5$, con cota de error relativo $\le 10^{-11}$ y un límite máximo de 1000 iteraciones.

#### Implementación en Maxima:
```maxima
/* Definición de la función analítica */
f(x) := 6 + atan(x) + exp(x^2 + 5*x + 12)/x;

/* Cálculo del Polinomio de Taylor de orden 8 en x = 2 */
g(x) := ''(taylor(f(x), x, 2, 8));

/* Función objetivo y su derivada para Newton-Raphson */
h(x) := g(x) - 10;
dh(x) := ''(diff(h(x), x));

/* Algoritmo de Newton-Raphson */
newton_raphson(x0, tol, max_iter) := block(
  [x_curr: x0, x_next, err: 1.0, k: 0],
  while (err > tol and k < max_iter) do (
    x_next: float(x_curr - h(x_curr) / dh(x_curr)),
    err: abs((x_next - x_curr) / x_next),
    x_curr: x_next,
    k: k + 1
  ),
  print("Convergencia en iteración:", k, "Raíz aproximada:", x_curr, "Error relativo:", err),
  return(x_curr)
);

/* Ejecución */
sol: newton_raphson(5.5, 10^(-11), 1000);
```

---

#### Problema 2: Gráficas y Cálculo de Áreas (5 Puntos)
Considera $f(x) := \arctan(x)$ y $g(x)$ el polinomio de Taylor de $f$ centrado en $x_0 = 1$ de grado $6$.

1. **Representación gráfica conjunta:** Trazar la gráfica de $f'(x)$ y $g(x)$ en el intervalo $[-2, 2]$.
2. **Cálculo de área:** Calcular de forma justificada el área delimitada entre $f'(x)$ y $g(x)$:
$$A = \int_{a}^{b} |f'(x) - g(x)| \, dx$$

#### Implementación en Maxima:
```maxima
f(x) := atan(x);
df(x) := ''(diff(f(x), x));
g(x) := ''(taylor(f(x), x, 1, 6));

/* Gráfica 2D con wxdraw */
wxdraw2d(
  xrange = [-2, 2],
  grid = true,
  key = "f'(x) = 1/(1+x^2)", color = blue, explicit(df(x), x, -2, 2),
  key = "Taylor g(x) grado 6", color = red, explicit(g(x), x, -2, 2)
);

/* Cálculo del área neta mediante integración */
area: romberg(abs(df(x) - g(x)), x, -2, 2);
```

---

## 3. Archivos y Recursos de Laboratorio Disponibles

En la pestaña de descargas se encuentran todos los ficheros `.wxmx` originales y enunciados oficiales en PDF:

* `ChecaCasas-FranciscoJavier-A21.wxmx` · Sesión completa de examen práctico realizada por Javier Checa.
* `ExamenMaxima2.wxmx` · Plantilla de evaluación del segundo parcial.
* `Segundo parcial D2.pdf` & `Segundo parcial E3.pdf` · Enunciados oficiales de examen.
* `Soluciones D2.wxmx` & `Soluciones E3.wxmx` · Cuadernos con la resolución completa de cada grupo.
* `plantila.wxmx` · Plantilla base de trabajo para el laboratorio.
