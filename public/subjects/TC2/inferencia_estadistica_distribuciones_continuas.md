# Técnicas Cuantitativas II · Inferencia Estadística & Distribuciones Continuas
**Asignatura:** Técnicas Cuantitativas II (TC2)  
**Etapa:** 2º Curso · Doble Grado Ingeniería Informática + ADE (UGR)  
**Autor:** Francisco Javier Checa Casas  
**Documento Fuente:** `tc2_tema1_inferencia_estadistica.pdf`, `practica3_modelado_cuantitativo.xlsm`  

---

## 1. Introducción a la Inferencia Estadística
La inferencia estadística aborda los métodos matemáticos para deducir propiedades y parámetros de una población desconocida a partir del análisis de una muestra probabilística observada. Los modelos de probabilidad continuos constituyen el soporte analítico de los contrastes de hipótesis y los intervalos de confianza.

---

## 2. Modelos de Distribuciones Continuas Fundamentales

### 2.1. Distribución Uniforme Continua $U(a, b)$
Modela variables aleatorias que toman valores en un intervalo cerrado $[a, b]$ donde cualquier subintervalo de igual longitud tiene la misma probabilidad.
* **Función de densidad de probabilidad (f.d.p.):**
  $$f(x) = \begin{cases} \frac{1}{b - a}, & a \le x \le b \\ 0, & \text{en otro caso} \end{cases}$$
* **Función de distribución acumulada (f.d.):**
  $$F(x) = \begin{cases} 0, & x < a \\ \frac{x - a}{b - a}, & a \le x \le b \\ 1, & x > b \end{cases}$$
* **Esperanza matemática y Varianza:**
  $$E[X] = \frac{a + b}{2}, \quad \text{Var}(X) = \frac{(b - a)^2}{12}$$

---

### 2.2. Distribución Beta $B(p, q)$
Distribución acotada en el intervalo $(0, 1)$, fundamental en estadística bayesiana para modelar proporciones, probabilidades a priori y porcentajes continuos.
* **Función de densidad:**
  $$f(x) = \frac{1}{B(p, q)} x^{p-1} (1 - x)^{q-1}, \quad 0 < x < 1; \quad p, q > 0$$
* **Función Beta de Euler:**
  $$B(p, q) = \int_0^1 t^{p-1} (1 - t)^{q-1} dt = \frac{\Gamma(p)\Gamma(q)}{\Gamma(p + q)}$$
* **Esperanza y Varianza:**
  $$E[X] = \frac{p}{p + q}, \quad \text{Var}(X) = \frac{pq}{(p + q)^2 (p + q + 1)}$$

---

### 2.3. Distribución Exponencial $\text{Exp}(\lambda)$
Modela el tiempo transcurrido hasta la ocurrencia de un suceso aleatorio en un proceso de Poisson (tiempos de servicio, colas, fiabilidad y vida útil de componentes).
* **Función de densidad:**
  $$f(x) = \lambda e^{-\lambda x}, \quad x \ge 0, \quad \lambda > 0$$
* **Función de distribución acumulada:**
  $$F(x) = 1 - e^{-\lambda x}, \quad x \ge 0$$
* **Propiedad de Carencia de Memoria (*Memoryless*):**
  $$P(X > s + t \mid X > s) = P(X > t), \quad \forall s, t \ge 0$$
* **Esperanza y Varianza:**
  $$E[X] = \frac{1}{\lambda}, \quad \text{Var}(X) = \frac{1}{\lambda^2}$$

---

### 2.4. Distribución Gamma $\Gamma(a, p)$
Generalización de la distribución exponencial, representando la suma de $p$ variables aleatorias exponenciales independientes e idénticamente distribuidas de parámetro $a$.
* **Función de densidad:**
  $$f(x) = \frac{a^p}{\Gamma(p)} x^{p-1} e^{-a x}, \quad x > 0; \quad a, p > 0$$
* **Función Gamma:** $\Gamma(p) = \int_0^\infty t^{p-1} e^{-t} dt$. Para enteros positivos, $\Gamma(n) = (n - 1)!$.
* **Esperanza y Varianza:**
  $$E[X] = \frac{p}{a}, \quad \text{Var}(X) = \frac{p}{a^2}$$

---

### 2.5. Distribución Normal General $N(\mu, \sigma)$
La distribución por antonomasia de la teoría estadística, justificada por el **Teorema Central del Límite**.
* **Función de densidad:**
  $$f(x) = \frac{1}{\sigma \sqrt{2\pi}} \exp\left( -\frac{(x - \mu)^2}{2\sigma^2} \right), \quad x \in \mathbb{R}$$
* **Tipificación a la Normal Estándar $Z \sim N(0, 1)$:**
  $$Z = \frac{X - \mu}{\sigma} \implies P(X \le k) = \Phi\left(\frac{k - \mu}{\sigma}\right)$$
* **Propiedades:** Simétrica respecto a $\mu$, puntos de inflexión en $\mu \pm \sigma$, y regla empírica del 68-95-99,7%:
  $$P(\mu - \sigma \le X \le \mu + \sigma) \approx 0,6826$$
  $$P(\mu - 2\sigma \le X \le \mu + 2\sigma) \approx 0,9544$$
  $$P(\mu - 3\sigma \le X \le \mu + 3\sigma) \approx 0,9973$$
