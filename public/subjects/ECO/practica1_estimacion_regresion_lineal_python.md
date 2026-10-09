# Práctica 1: Estimación e Inferencia en Modelos de Regresión Lineal con Python

**Asignatura:** Econometría (ECO)  
**Institución:** Universidad de Granada (UGR) · Doble Grado Informática + ADE  
**Autor:** Francisco Javier Checa Casas  
**Tecnologías:** Python, NumPy, Statsmodels, SciPy, Matplotlib, Wooldridge Datasets  

---

## 1. El Modelo de Regresión Lineal Clásico (MCO)

El modelo de regresión lineal múltiple en notación matricial se formula como:
$$y = X\beta + u$$
donde:
* $y \in \mathbb{R}^{n \times 1}$ es el vector de la variable endógena o dependiente.
* $X \in \mathbb{R}^{n \times k}$ es la matriz de regresores o variables explicativas (incluyendo el término constante).
* $\beta \in \mathbb{R}^{k \times 1}$ es el vector de coeficientes estructurales desconocidos.
* $u \in \mathbb{R}^{n \times 1}$ es la perturbación aleatoria, con hipótesis clásicas: $E[u|X] = 0$ y $\text{Var}(u|X) = \sigma^2 I_n$ (homocedasticidad y no autocorrelación).

### Estimador de Mínimos Cuadrados Ordinarios (MCO):
$$\hat{\beta} = (X^T X)^{-1} X^T y$$

---

## 2. Implementación Computacional en Python con Statsmodels

```python
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
from scipy import stats
from wooldridge import data as dataWoo

# 1. Carga de dataset 'ceosal1' (Salarios de CEOs vs Rentabilidad ROE)
datos = dataWoo('ceosal1')
y = datos['salary']
X = sm.add_constant(datos['roe'])

# 2. Ajuste MCO y resumen econométrico
modelo_mco = sm.OLS(y, X).fit()
print(modelo_mco.summary())

# 3. Descomposición de la Varianza (ANOVA):
# SCT = SCE + SCR
sct = modelo_mco.centered_tss
sce = modelo_mco.ess
scr = modelo_mco.ssr
r2 = modelo_mco.rsquared
r2_adj = modelo_mco.rsquared_adj

print(f"R²: {r2:.4f} | R² Ajustado: {r2_adj:.4f}")
```

---

## 3. Contraste de Hipótesis e Inferencia Estadística

### 1. Significatividad Individual (Contraste $t$ de Student):
Para contrastar $H_0: \beta_j = 0$ frente a $H_1: \beta_j \neq 0$:
$$t_{\text{exp}} = \frac{\hat{\beta}_j}{\text{SE}(\hat{\beta}_j)} \sim t_{n-k}$$
```python
alpha = 0.05
t_exp = modelo_mco.tvalues
t_teo = stats.t.ppf(1 - alpha/2, df=modelo_mco.df_resid)
p_valores = modelo_mco.pvalues
```

### 2. Significatividad Global del Modelo (Contraste $F$ de Snedecor):
Para contrastar conjuntamente $H_0: \beta_1 = \beta_2 = \dots = \beta_{k-1} = 0$:
$$F_{\text{exp}} = \frac{\text{SCE} / (k-1)}{\text{SCR} / (n-k)} \sim F_{k-1, n-k}$$
```python
f_exp = modelo_mco.fvalue
f_teo = stats.f.ppf(1 - alpha, dfn=modelo_mco.df_model, dfd=modelo_mco.df_resid)
```

### 3. Estimación de la Varianza de la Perturbación:
$$s^2 = \hat{\sigma}^2 = \frac{\sum e_i^2}{n - k} = \frac{\text{SCR}}{n - k}$$

---

## 4. Recursos y Cuadernos Jupyter Disponibles

En la pestaña de descargas se encuentran disponibles los notebooks y datasets oficiales:

* `00_ECO_Intro.ipynb` · Cuaderno interactivo de introducción a Python, Markdown y LaTeX para econometría.
* `01_ECO_Estimacion.ipynb` · Cuaderno completo de estimación MCO, ANOVA, gráficos diagnósticos y predicción.
* `stock.xlsx`, `carbon_nanotubes.csv`, `Theil.csv` · Datasets empíricos de modelado financiero e industrial.
* `environment.yml` · Configuración del entorno reproducible conda/mamba con todas las dependencias.
