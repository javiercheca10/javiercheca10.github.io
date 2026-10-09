# Casos Prácticos de Examen Parcial: Liquidación del IS (Modelos A Gran Empresa y Modelo B ERD) con Registro Contable

---

## 1. Octubre 2023 - Modelo A (No ERD / Gran Empresa)

### 1.1. Análisis y Justificación de los Ajustes Extracontables

#### 1. Inmuebles (Libre Amortización por Mantenimiento de Plantilla)
*   **Fundamento Legal:** Disposición adicional 11ª de la LIS (o normativa aplicable por temporalidad del elemento adquirido en 2009/2010 bajo régimen de fomento del empleo/mantenimiento de plantilla).
*   **Cálculo de la Base de Amortización:**
    $$P_{\text{adq}} = 210.000 - 10.000 \, (\text{Suelo/Terreno}) = 200.000 \text{ €}$$
*   **Análisis Fiscal vs. Contable:**
    *   **Amortización Contable (GC):** $-4.000 \text{ €}$ anuales (vida útil estimada de 50 años).
    *   **Amortización Fiscal (GF):** En el año de adquisición (2010) se aplicó Libre Amortización por valor de $-200.000 \text{ €}$.
    *   **Ajuste en el Ejercicio Actual (2023):** Al estar el inmueble totalmente amortizado fiscalmente ($GF = 0$), la amortización contable del año ($GC = -4.000 \text{ €}$) no es deducible. Se genera un ajuste extracontable positivo por reversión de la diferencia temporaria.
    $$\text{Ajuste } (A_j) = +4.000 \text{ €} \quad \text{(Reversión de Pasivo por Diferencia Temporaria Imponible - Cuenta 479)}$$

#### 2. Equipos para Procesos de Información
*   **Fundamento Legal:** Art. 12 LIS (Tablas oficiales de amortización lineal).
*   **Análisis:**
    *   **Amortización Contable (GC):** $-10.000 \text{ €}$.
    *   **Límite Fiscal Máximo (GF):** $-15.000 \text{ €}$.
    *   **Ajuste:** Dado que el gasto contable se sitúa por debajo del límite fiscal máximo establecido por tablas oficiales, se respeta el criterio contable y **no procede realizar ajuste extracontable**.

#### 3. Terreno (Operación a Plazos - Principio de Caja)
*   **Fundamento Legal:** Art. 11.4 LIS (Criterio temporal de imputación de operaciones a plazos o con precio aplazado).
*   **Análisis:**
    *   **Ejercicio 2022:** Se devengó contablemente un beneficio de $+75.000 \text{ €}$ ($GC$). Fiscalmente, al aplicarse el principio de caja, solo tributó la parte correspondiente al cobro percibido ($GF = +30.000 \text{ €}$), realizándose un ajuste negativo de $-45.000 \text{ €}$.
    *   **Ejercicio 2023 (Actual):** Se percibe el cobro restante. No existe registro contable en la cuenta de pérdidas y ganancias ($GC = 0$), pero fiscalmente debe integrarse el beneficio pendiente ($GF = +45.000 \text{ €}$).
    $$\text{Ajuste } (A_j) = +45.000 \text{ €} \quad \text{(Reversión de Pasivo por Diferencia Temporaria Imponible)}$$

#### 4. Provisiones no Deducibles
*   **Fundamento Legal:** Art. 14 LIS. Las provisiones por gastos que no correspondan a obligaciones explícitas, seguros o garantías no resultan fiscalmente computables en el periodo de su dotación.
*   **Análisis:**
    *   **Ajuste:** El gasto contable por provisión de $+5.000 \text{ €}$ se dota pero no es deducible en el ejercicio actual.
    $$\text{Ajuste } (A_j) = +5.000 \text{ €} \quad \text{(Origen de Activo por Diferencia Temporaria Deducible - Cuenta 4740)}$$

#### 5. Deterioro de Valor de Créditos por Operaciones Comerciales
*   **Fundamento Legal:** Art. 13.1.a) LIS. No serán deducibles las pérdidas por deterioro de créditos adeudados por entidades de derecho público, salvo que sean objeto de un procedimiento arbitral o judicial.
*   **Análisis:** Al tratarse de un saldo adeudado por una administración pública, el deterioro contabilizado no es deducible.
    $$\text{Ajuste } (A_j) = +4.000 \text{ €} \quad \text{(Diferencia Permanente Positiva)}$$

#### 6. Dividendos Recibidos
*   **Fundamento Legal:** Art. 21 LIS (Exención sobre dividendos y rentas derivadas de la transmisión de valores).
*   **Análisis:** Aunque se cumple el requisito de participación indirecta/directa superior al $5\%$, el periodo de tenencia ininterrumpida de la participación es inferior a un año. Por consiguiente, no se cumple el requisito temporal de permanencia y **no procede ajuste por exención**.

#### 7. Gastos por Atenciones a Clientes
*   **Fundamento Legal:** Art. 15.e) LIS. Los gastos por atenciones a clientes tienen un límite deducible del $1\%$ del Importe Neto de la Cifra de Negocios (INCN).
*   **Cálculo del Límite Deducible:**
    $$\text{Límite} = 1\% \times \text{INCN} = 0,01 \times 7.500.000 \text{ €} = 75.000 \text{ €}$$
*   **Análisis del Ajuste:**
    *   **Gasto Contable (GC):** $-110.000 \text{ €}$.
    *   **Gasto Deducible (GF):** $-75.000 \text{ €}$.
    $$\text{Ajuste } (A_j) = +35.000 \text{ €} \quad \text{(Diferencia Permanente Positiva)}$$

#### 8. Software de I+D (Deducción por Actividades de Investigación y Desarrollo)
*   **Fundamento Legal:** Art. 35 LIS.
*   **Determinación de la Base de la Deducción:**
    $$\text{Gastos totales de la actividad} = 7.000 \text{ €}$$
    $$\text{Exclusiones/No computables} = -1.000 \text{ €}$$
    $$\text{Base de Deducción} = 6.000 \text{ €}$$
*   **Cálculo de la Media de los 2 Años Anteriores:**
    $$\text{Media} = \frac{5.000 + 0}{2} = 2.500 \text{ €}$$
*   **Cálculo del Tramo Incrementado:**
    *   Tramo hasta la media ($25\%$): $2.500 \times 0,25 = 625 \text{ €}$
    *   Exceso sobre la media ($42\%$): $(6.000 - 2.500) \times 0,42 = 3.500 \times 0,42 = 1.470 \text{ €}$
    $$\text{Deducción Total por I+D} = 625 + 1.470 = 2.095 \text{ €}$$

---

### 1.2. Esquema de Liquidación del IS (Modelo A)

| Concepto / Ajuste | Justificación Legal (LIS) | Signo | Importe (€) |
| :--- | :--- | :---: | :---: |
| **Resultado antes de Impuestos (RHI)** | Estado de Cambios en el Patrimonio Neto / PyG | | **24.000** |
| Deterioro de Créditos con Entidad Pública | Art. 13.1.a) LIS | $+$ | 4.000 |
| Exceso de Gastos por Atenciones a Clientes | Art. 15.e) LIS | $+$ | 35.000 |
| **Suma de Diferencias Permanentes (DP)** | | | **+39.000** |
| Amortización Inmuebles (Reversión LA) | DA 11ª LIS | $+$ | 4.000 |
| Reversión Terreno (Venta a plazos) | Art. 11.4 LIS | $+$ | 45.000 |
| Provisión no deducible (Origen) | Art. 14 LIS | $+$ | 5.000 |
| **Suma de Diferencias Temporarias (DT)** | | | **+54.000** |
| **Base Imponible Previa (BI)** | $RHI + DP + DT$ | | **117.000** |
| Compensación de Bases Imponibles Negativas (BINs) | Art. 26 LIS | $-$ | -25.000 |
| **Base Imponible Liquidable** | | | **92.000** |
| Tipo de Gravamen General | Art. 29.1 LIS | $25\%$ | |
| **Cuota Íntegra (CI)** | $92.000 \times 25\%$ | | **23.000** |
| Deducción por Actividades de I+D | Art. 35 LIS | $-$ | -2.095 |
| **Cuota Líquida (CL)** | | | **20.905** |
| Pagos a Cuenta Realizados | Art. 40 LIS | $-$ | -10.700 |
| Retenciones Soportadas | Art. 128 LIS | $-$ | -570 |
| **Cuota Diferencial (A ingresar)** | $CL - \text{Ret} - \text{Pagos}$ | | **9.635** |

*Nota explicativa sobre Retenciones Soportadas:* $570 \text{ €}$ resultantes de la retención del $19\%$ sobre la base computable de ingresos financieros/arrendamientos devengados:
$$(4.000 - 1.000) \times 19\% = 570 \text{ €}$$

---

### 1.3. Cierre de Ejercicio y Registro Contable (Modelo A)

#### Cálculo del Impuesto Corriente e Impuesto Diferido:
1.  **Resultado Contable Ajustado de Diferencias Permanentes ($RHj$):**
    $$RHj = RHI + DP = 24.000 + 39.000 = 63.000 \text{ €}$$
2.  **Impuesto Bruto Teórico ($IBB$):**
    $$IBB = 63.000 \times 25\% = 15.750 \text{ €}$$
3.  **Impuesto Corriente Teórico ($IB$):**
    $$IB = IBB - \text{Deducciones} = 15.750 - 2.095 = 13.655 \text{ €}$$
4.  **Gasto por Impuesto Corriente ($FC$):**
    $$FC = (BI \text{ Liquidable} \times 25\%) - \text{Deducciones} = (92.000 \times 0,25) - 2.095 = 20.905 \text{ €}$$
5.  **Variación neta de Pasivos/Activos Diferidos ($ID$):**
    $$ID = FC - IB = 20.905 - 13.655 = 7.250 \text{ €}$$

#### Desglose de las Variaciones de Activos y Pasivos por Impuesto Diferido:
*   **Reversión de Pasivo por Diferencia Temporaria (Inmuebles):**
    $$4.000 \times 25\% = 1.000 \text{ € (Disminución de la cuenta 479)}$$
*   **Reversión de Pasivo por Diferencia Temporaria (Terrenos):**
    $$45.000 \times 25\% = 11.250 \text{ € (Disminución de la cuenta 479)}$$
*   **Origen de Activo por Diferencia Temporaria (Provisión):**
    $$5.000 \times 25\% = 1.250 \text{ € (Aumento de la cuenta 4740)}$$
*   **Aplicación de Crédito por Pérdidas a Compensar (BINs):**
    $$25.000 \times 25\% = 6.250 \text{ € (Disminución de la cuenta 4745)}$$

#### Asientos de Cierre en el Libro Diario

**1. Registro del Impuesto Corriente y de las Retenciones/Pagos a Cuenta:**

| Debe (€) | Cuentas del PGC y Concepto | Haber (€) |
| :--- | :--- | :--- |
| 20.905 | **(6300) Impuesto sobre beneficios corriente** | |
| | a **(473) Hacienda Pública, retenciones y pagos a cuenta** | 11.270 |
| | a **(4752) Hacienda Pública, acreedora por Impuesto sobre Sociedades** | 9.635 |

*Nota:* El saldo acreditado en la cuenta (473) corresponde a la suma de pagos fraccionados y retenciones soportadas ($10.700 + 570 = 11.270 \text{ €}$).

**2. Registro del Impuesto Diferido e Imputación de Activos/Pasivos Fiscales:**

| Debe (€) | Cuentas del PGC y Concepto | Haber (€) |
| :--- | :--- | :--- |
| 12.250 | **(479) Pasivos por diferencias temporarias imponibles** <br>*(1.000 Inmuebles + 11.250 Terrenos)* | |
| 1.250 | **(4740) Activos por diferencias temporarias deducibles** <br>*(Dotación Provisión)* | |
| | a **(6301) Impuesto sobre beneficios diferido** | 7.250 |
| | a **(4745) Crédito por pérdidas a compensar del ejercicio...** *(Aplicación BINs)* | 6.250 |

---
---

## 2. Octubre 2023 - Modelo B (Sujeto a Régimen Especial ERD)

### 2.1. Incentivos Fiscales aplicables a ERD (Art. 101 a 105 LIS)
Como entidad de reducida dimensión (cifra de negocios inferior a 10 millones de euros en el periodo impositivo anterior), se aplican las siguientes prerrogativas:
1.  **Libre Amortización de activos vinculados al empleo (I+D / Creación de Empleo):** Límite máximo de $120.000 \text{ €}$ por cada persona/año de incremento de plantilla media.
2.  **Amortización Acelerada:** Multiplicador del coeficiente de amortización lineal máximo de tablas por un factor de $2$.
3.  **Deterioro Global de Deudores (Estimación Global de Insolvencias):** Límite deducible del $1\%$ sobre el saldo de clientes al cierre del ejercicio (excluidos deudores individualizados o no deducibles).
4.  **Reserva de Nivelación (RN):** Reducción de la BI de hasta un $10\%$ con un límite de 1 millón de euros anuales.

---

### 2.2. Análisis de las Modificaciones y Ajustes en el Modelo B

#### 1. Inmuebles
*   **Análisis:** Idéntico tratamiento que en el Modelo A. Se aplica la libre amortización histórica vinculada al mantenimiento de plantilla.
    $$\text{Ajuste } (A_j) = +4.000 \text{ €} \quad \text{(Diferencia Temporaria Positiva - Reversión)}$$

#### 2. Equipos para Procesos de Información (Amortización Acelerada ERD)
*   **Fundamento Legal:** Art. 103 LIS. Duplicación del coeficiente máximo de tablas oficiales ($15\% \times 2 = 30\%$).
*   **Análisis:**
    *   **Gasto Contable (GC):** $-10.000 \text{ €}$.
    *   **Gasto Fiscal Máximo (GF):** $-30.000 \text{ €}$ (aprovechando el incentivo de amortización acelerada $\times 2$ sobre el valor original amortizable).
    $$\text{Ajuste } (A_j) = -20.000 \text{ €} \quad \text{(Diferencia Temporaria Negativa - Origen)}$$

#### 3. Terreno (Operación a Plazos con Pérdida Contable)
*   **Análisis:** El contribuyente aplica el criterio de caja de forma simétrica para una pérdida.
    *   **2022:** Pérdida contable de $-75.000 \text{ €}$ ($GC$), imputando fiscalmente solo $-45.000 \text{ €}$ cobrados/realizados. Generó un ajuste extracontable positivo de $+30.000 \text{ €}$.
    *   **2023:** No hay reflejo contable ($GC = 0$), pero fiscalmente se integra la pérdida restante ($GF = -30.000 \text{ €}$).
    $$\text{Ajuste } (A_j) = -30.000 \text{ €} \quad \text{(Diferencia Temporaria Negativa - Reversión)}$$

#### 4. Provisiones no Deducibles
*   **Análisis:** Igual tratamiento que en el caso general. La dotación contable de la provisión por cuantía de $+5.000 \text{ €}$ es fiscalmente no deducible en este ejercicio, difiriéndose su deducibilidad.
    $$\text{Ajuste } (A_j) = +5.000 \text{ €} \quad \text{(Diferencia Temporaria Positiva)}$$

#### 5. Dividendos Recibidos
*   No procede ajuste por incumplirse el requisito de permanencia de 1 año (mismo análisis que el Modelo A).

#### 6. Deterioro de Créditos por Insolvencias con Entidades Públicas
*   **Fundamento Legal:** Art. 13.1.a) LIS.
*   **Análisis:** No es deducible el deterioro de créditos frente a entes públicos. No computa para el cálculo del incentivo de estimación global de insolvencias del $1\%$ de saldos de clientes para ERD.
    $$\text{Ajuste } (A_j) = +14.000 \text{ €} \quad \text{(Diferencia Permanente Positiva)}$$

#### 7. Atenciones a Clientes
*   **Análisis:** Idéntico límite legal del $1\%$ del INCN ($75.000 \text{ €}$).
    *   **GC:** $-110.000 \text{ €}$ | **GF:** $-75.000 \text{ €}$.
    $$\text{Ajuste } (A_j) = +35.000 \text{ €} \quad \text{(Diferencia Permanente Positiva)}$$

#### 8. Software de I+D (Base de Deducción ERD)
*   **Determinación de la Base:**
    $$\text{Gastos totales de la actividad} = 7.000 \text{ €}$$
    $$\text{Gastos excluidos/no elegibles} = -3.000 \text{ €}$$
    $$\text{Base de Deducción} = 4.000 \text{ €}$$
*   **Cálculo de la Media de los 2 Años Anteriores:**
    $$\text{Media} = \frac{5.000 + 0}{2} = 2.500 \text{ €}$$
*   **Deducción por I+D (Modelo B):**
    *   Tramo hasta la media ($25\%$): $2.500 \times 0,25 = 625 \text{ €}$
    *   Exceso sobre la media ($42\%$): $(4.000 - 2.500) \times 0,42 = 1.500 \times 0,42 = 630 \text{ €}$
    $$\text{Deducción Total por I+D} = 625 + 630 = 1.255 \text{ €}$$

---

### 2.3. Esquema de Liquidación del IS (Modelo B)

| Concepto / Ajuste | Justificación Legal (LIS) | Signo | Importe (€) |
| :--- | :--- | :---: | :---: |
| **Resultado antes de Impuestos (RHI)** | Estado de Cambios en el Patrimonio Neto / PyG | | **24.000** |
| Deterioro de Créditos con Entidad Pública | Art. 13.1.a) LIS | $+$ | 14.000 |
| Exceso de Gastos por Atenciones a Clientes | Art. 15.e) LIS | $+$ | 35.000 |
| **Suma de Diferencias Permanentes (DP)** | | | **+49.000** |
| Amortización Inmuebles (Reversión LA) | DA 11ª LIS | $+$ | 4.000 |
| Amortización Acelerada Equipos Informáticos | Art. 103 LIS | $-$ | -20.000 |
| Reversión Terreno (Operación a Plazos) | Art. 11.4 LIS | $-$ | -30.000 |
| Provisión no deducible (Origen) | Art. 14 LIS | $+$ | 5.000 |
| **Suma de Diferencias Temporarias (DT)** | | | **-41.000** |
| **Base Imponible Previa (BI)** | $RHI + DP + DT$ | | **32.000** |
| Compensación de Bases Imponibles Negativas (BINs) | Art. 26 LIS | $-$ | -25.000 |
| **Base Imponible Liquidable** | | | **7.000** |
| Tipo de Gravamen | Art. 29.1 LIS | $25\%$ | |
| **Cuota Íntegra (CI)** | $7.000 \times 25\%$ | | **1.750** |
| Deducción por Actividades de I+D | Art. 35 LIS | $-$ | -1.255 |
| **Cuota Líquida (CL)** | | | **495** |
| Pagos a Cuenta Realizados | Art. 40 LIS | $-$ | -10.700 |
| Retenciones Soportadas | Art. 128 LIS | $-$ | -570 |
| **Resultado de la Liquidación (A devolver)** | | | **-10.775** |