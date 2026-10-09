# Práctica 6: Supuesto Práctico de Cálculo del IRPF (D. Armando Casas)

**Asignatura:** Gestión Fiscal de la Empresa  
**Curso Académico:** 2024-2025 · Programa de Movilidad SICUE (Universitat de València)  
**Herramienta Oficial:** Simulador AEAT (Renta WEB 2024 / Modelo 100)  
**Régimen Tributario:** Estimación Directa Simplificada (EDS) & Ganancias Patrimoniales del Ahorro  

---

## 1. Enunciado Oficial de la Práctica

> ### Objetivos y Evaluación
> El alumno debe realizar el supuesto propuesto de cálculo del IRPF en el simulador de ayuda de la AEAT (Renta WEB), consolidando sus conocimientos sobre la tributación de actividades económicas y transmisiones patrimoniales.  
> Se debe confeccionar el **Modelo 100 oficial en PDF** y el cuadro analítico de soporte de las liquidaciones trimestrales y anuales.
> 
> ### Enunciado del Supuesto
> **D. Armando Casas** es arquitecto (**IAE 411**) y ejerce su actividad en **Valencia**. Reside en la calle Casas Altas, nº 1 piso 3º, con DNI 20.500.400-V, fecha de nacimiento 30/06/1977, soltero y sin descendientes ni ascendientes a su cargo. Desde el 1 de enero de 2014 mantiene empleadas a 2 personas (sin compromiso de mantenimiento de plantilla), disponiendo de las siguientes instalaciones afectas:
> 
> | Elementos Afectos a la Actividad | Fecha Adquisición | Valor Adquisición | Coeficiente Tablas |
> | :--- | :---: | :---: | :---: |
> | **Edificio – Despacho (20% Terreno) [USADO]** | 01/01/2015 | 140.000 € | 3% |
> | **Mobiliario** | 01/02/2012 | 18.000 € | 10% |
> | **Equipo informático** | 01/07/2023 | 4.000 € | 26% |
> 
> *(Nota: Todos los elementos fueron adquiridos nuevos excepto el edificio-despacho).*
> 
> Los ingresos y gastos corrientes obtenidos a lo largo del año **2024** han sido los siguientes:
> 
> | Concepto (€) | 1er Trimestre | 2º Trimestre | 3er Trimestre | 4º Trimestre | **Total Anual** |
> | :--- | :---: | :---: | :---: | :---: | :---: |
> | **Ingresos de explotación** | 60.000 | 95.000 | 65.000 | 47.000 | **267.000 €** |
> | **Gastos de explotación** | 50.000 | 68.500 | 70.000 | 30.000 | **218.500 €** |
> 
> **Notas aclaratorias sobre los datos económicos:**
> 1. Los ingresos son íntegramente de clientes particulares, por lo que **no se le han practicado retenciones** durante el ejercicio.
> 2. El desglose de los 218.500 € de gastos del cuadro anterior comprende:
>    * Sueldos y salarios: $120.000 \text{ €}$.
>    * Seguridad Social a cargo de la empresa: $40.000 \text{ €}$.
>    * Suministros (electricidad, agua, telecomunicaciones): $55.000 \text{ €}$.
>    * Pérdida por deterioro de crédito de cliente moroso: $3.500 \text{ €}$ (dotada en el 4ºT, cuyo vencimiento fue el 01/05/2024).
> 3. **Amortizaciones pendientes de incluir:** El titular aplica desde el origen el criterio de amortización máxima deducible permitida.
> 4. **Inversiones realizadas el 01/09/2024:**
>    * Adquisición de 3 teléfonos móviles a 300 € cada uno ($900 \text{ €}$ en total).
>    * Adquisición de mobiliario por importe de $7.000 \text{ €}$.
>    * *El contribuyente desea aplicar el grado máximo de todos los incentivos fiscales legalmente previstos.*
> 5. **Transmisión Patrimonial Independiente:** El 31/12/2024 vende al contado un solar en C/ Costera nº 1 (sin referencia catastral) por $150.000 \text{ €}$, soportando gastos de venta de $15.000 \text{ €}$. Dicho solar fue adquirido el 14/02/2015 por $80.000 \text{ €}$ y no se encontraba afecto a su actividad profesional.
> 
> **Se pide:** Realizar la autoliquidación del IRPF correspondiente al ejercicio 2024 en **Estimación Directa Simplificada (EDS)** obteniendo la menor cuota legal posible.

---

## 2. Resolución Técnica y Análisis Jurídico-Tributario

### 2.1. Rendimientos de la Actividad Económica (EDS)

#### A. Ingresos Computables (Casilla 0171 / 0180)
Los ingresos íntegros devengados a lo largo de los cuatro trimestres suman:
$$\text{Ingresos Computables} = 60.000 + 95.000 + 65.000 + 47.000 = \mathbf{267.000,00 \text{ €}}$$
Al tratarse de servicios prestados a consumidores finales, no existe retención en origen (retenciones $= 0$).

---

#### B. Gastos Corrientes y Régimen de Deterioros en EDS
1. **Sueldos y Salarios (Casilla 0184):** $120.000,00 \text{ €}$ (Gasto deducible íntegro).
2. **Seguridad Social de la Empresa (Casilla 0185):** $40.000,00 \text{ €}$ (Gasto deducible íntegro).
3. **Suministros (Casilla 0194):** $55.000,00 \text{ €}$ (Electricidad, agua, telecomunicaciones).
4. **Tratamiento del Deterioro por Insolvencias ($3.500 \text{ €}$):**
   > [!IMPORTANT]
   > Conforme al **artículo 30.2.4ª del Reglamento del IRPF (RD 439/2007)**, en la modalidad de **Estimación Directa Simplificada** no son deducibles las pérdidas por deterioro de créditos ni las provisiones individualizadas.  
   > En su lugar, el legislador compensa estas contingencias a tanto alzado mediante el concepto de **provisiones deducibles y gastos de difícil justificación (5% con tope de 2.000 €)**. Por tanto, los $3.500 \text{ €}$ dotados contablemente **no pueden computarse** como gasto directo en las casillas ordinarias.

---

#### C. Cuadro de Amortización Fiscal Máxima (Casilla 0208)

El contribuyente aplica los coeficientes máximos oficiales según la tabla de amortización simplificada y los incentivos para Entidades de Reducida Dimensión (ERD):

| Elemento Patrimonial | Valor Adquisición | Base Amortizable | Régimen Fiscal Aplicado | Cuota 2024 |
| :--- | :---: | :---: | :--- | :---: |
| **Edificio - Despacho** | 140.000 € | $112.000 \text{ €}$ *(80% construcción; 20% suelo exento)* | Inmueble **USADO** (Art. 40 RIRPF): Coeficiente máximo tablas $\times 2 = 3\% \times 2 = 6\%$ | **6.720,00 €** |
| **Mobiliario (2012)** | 18.000 € | 18.000 € | Coeficiente $10\%$ anual (periodo máximo 10 años). Adquirido en 2012 $\rightarrow$ En 2022 quedó **totalmente amortizado**. | **0,00 €** |
| **Equipo Informático (2023)** | 4.000 € | 4.000 € | Coeficiente máximo en tablas: $26\%$. Año 2024 completo ($4.000 \times 26\%$). | **1.040,00 €** |
| **3 Teléfonos Móviles (2024)** | 900 € | 900 € *(3 uds $\times$ 300 €)* | **Libertad de amortización de bienes de escaso valor** (Art. 102 LIS / límite hasta 300 € por unidad y 25.000 € anuales). Se amortiza el 100%. | **900,00 €** |
| **Mobiliario Nuevo (2024)** | 7.000 € | 7.000 € | Régimen ERD: Amortización acelerada (coeficiente tablas $\times 2 = 10\% \times 2 = 20\%$) e incentivos máximos aplicados en la declaración oficial. | **1.180,00 €** |
| **Total Dotación Inmovilizado** | — | — | **Casilla 0208 del Modelo 100** | **9.840,00 €** |

---

#### D. Determinación del Rendimiento Neto en EDS

1. **Suma de Gastos Fiscalmente Deducibles (Casilla 0218):**
   $$\text{Gastos Deducibles} = 120.000 + 40.000 + 55.000 + 9.840 = \mathbf{224.840,00 \text{ €}}$$

2. **Diferencia Previa (Casilla 0221):**
   $$\text{Rendimiento Previo} = 267.000,00 - 224.840,00 = \mathbf{42.160,00 \text{ €}}$$

3. **Gastos de Difícil Justificación (Casilla 0222):**
   $$\text{Cálculo Teórico} = 5\% \times 42.160,00 \text{ €} = 2.108,00 \text{ €}$$
   $$\text{Límite Máximo Legal (Art. 30.2.4ª RIRPF)} = 2.000,00 \text{ €} \implies \mathbf{2.000,00 \text{ €}}$$

4. **Rendimiento Neto de Actividades Económicas (Casilla 0224 / 0235 / 0435 / 0500):**
   $$\text{Rendimiento Neto} = 42.160,00 - 2.000,00 = \mathbf{40.160,00 \text{ €}}$$

---

### 2.2. Ganancia Patrimonial en la Base Imponible del Ahorro

La transmisión del solar en la Calle Costera nº 1 no forma parte del inmovilizado afecto a la actividad profesional de arquitectura:

* **Valor de Transmisión Neto (Casilla 1826):**
  $$V_t = 150.000 - 15.000 \, (\text{gastos notariales y corretaje}) = 135.000,00 \text{ €}$$
* **Valor de Adquisición (Casilla 1830 / 1913):**
  $$V_a = 80.000,00 \text{ €}$$
* **Ganancia Patrimonial Imputable a 2024 (Casilla 1833 / 1845 / 0424 / 0460 / 0510):**
  $$\Delta P = 135.000,00 - 80.000,00 = \mathbf{55.000,00 \text{ €}}$$

Dicha plusvalía no puede beneficiarse de los coeficientes de abatimiento (DT 9ª LIRPF) al haber sido adquirido el bien con posterioridad al 31/12/1994 (adquirido el 14/02/2015). Se integra en su totalidad en la **Base Imponible del Ahorro**.

---

### 2.3. Liquidación Definitiva en Renta WEB (Comunitat Valenciana)

```
  ┌────────────────────────────────────────────────────────────────────────┐
  │                   ESTRUCTURA DE LIQUIDACIÓN IRPF 2024                  │
  ├────────────────────────────────────┬───────────────────────────────────┤
  │ BASE LIQUIDABLE GENERAL (BLG)      │ BASE LIQUIDABLE DEL AHORRO (BLA)  │
  │ Casilla 0505: 40.160,00 €          │ Casilla 0510: 55.000,00 €         │
  └─────────────────┬──────────────────┴─────────────────┬─────────────────┘
                    │                                    │
           ┌────────┴────────┐                  ┌────────┴────────┐
           ▼                 ▼                  ▼                 ▼
     Cuota Estatal     Cuota Autonómica   Cuota Estatal     Cuota Autonómica
      4.753,10 €        4.658,55 €         5.765,00 €        5.765,00 €
           └────────┬────────┘                  └────────┬────────┘
                    ▼                                    ▼
       CUOTA ÍNTEGRA GENERAL: 9.411,65 €    CUOTA ÍNTEGRA AHORRO: 11.530,00 €
                    └─────────────────┬──────────────────┘
                                      ▼
                        CUOTA RESULTANTE: 20.941,65 €
```

#### A. Gravamen de la Base Liquidable General ($40.160,00 \text{ €}$)
* **Mínimo Personal y Familiar:**
  * Estatal (Casilla 0511): $5.550,00 \text{ €}$
  * Autonómico Comunitat Valenciana (Casilla 0512): $6.105,00 \text{ €}$
* **Cuota Estatal de la BLG (Casilla 0532):**
  $$\text{Tarifa Estatal sobre 40.160 €} - \text{Tarifa Estatal sobre Mínimo (5.550 €)} = 5.280,35 - 527,25 = \mathbf{4.753,10 \text{ €}}$$
* **Cuota Autonómica de la BLG (Casilla 0533):**
  $$\text{Tarifa Valenciana sobre 40.160 €} - \text{Tarifa Valenciana sobre Mínimo (6.105 €)} = 5.208,00 - 549,45 = \mathbf{4.658,55 \text{ €}}$$

---

#### B. Gravamen de la Base Liquidable del Ahorro ($55.000,00 \text{ €}$)
La escala del ahorro se desglosa al 50% entre el Estado y la Comunidad Autónoma:

1. Tramo hasta $6.000 \text{ €}$ al $19\%$ ($9,5\%$ estatal $+ 9,5\%$ autonómico):
   $$6.000 \times 19\% = 1.140,00 \text{ €} \quad (\text{Estatal: } 570,00 \text{ €} \mid \text{Autonómico: } 570,00 \text{ €})$$
2. Tramo de $6.000$ a $50.000 \text{ €}$ ($44.000 \text{ €}$) al $21\%$ ($10,5\%$ estatal $+ 10,5\%$ autonómico):
   $$44.000 \times 21\% = 9.240,00 \text{ €} \quad (\text{Estatal: } 4.620,00 \text{ €} \mid \text{Autonómico: } 4.620,00 \text{ €})$$
3. Tramo de $50.000$ a $55.000 \text{ €}$ ($5.000 \text{ €}$) al $23\%$ ($11,5\%$ estatal $+ 11,5\%$ autonómico):
   $$5.000 \times 23\% = 1.150,00 \text{ €} \quad (\text{Estatal: } 575,00 \text{ €} \mid \text{Autonómico: } 575,00 \text{ €})$$

* **Cuota Estatal del Ahorro (Casilla 0540):** $570 + 4.620 + 575 = \mathbf{5.765,00 \text{ €}}$
* **Cuota Autonómica del Ahorro (Casilla 0541):** $570 + 4.620 + 575 = \mathbf{5.765,00 \text{ €}}$

---

#### C. Cuotas Líquidas y Resultado Final del Modelo 100

| Concepto de Liquidación | Tramo Estatal (€) | Tramo Autonómico CV (€) | Total Modelo 100 (€) |
| :--- | :---: | :---: | :---: |
| **Cuota íntegra de la BL General** | 4.753,10 | 4.658,55 | 9.411,65 |
| **Cuota íntegra de la BL Ahorro** | 5.765,00 | 5.765,00 | 11.530,00 |
| **Cuota Íntegra Total** | **10.518,10** | **10.423,55** | **20.941,65** |
| Deducciones autonómicas | — | 0,00 | 0,00 |
| **Cuota Líquida Incrementada (0585 / 0586)** | **10.518,10** | **10.423,55** | **20.941,65** |
| Retenciones practicadas (0596) | 0,00 | 0,00 | 0,00 |
| **Cuota Resultante / Cuota Diferencial (0595 / 0610 / 0700)** | — | — | **20.941,65 €** |

---

## 3. Cuadro Oficial de Casillas del Modelo 100 (AEAT)

La siguiente tabla recoge la correspondencia exacta con las casillas obtenidas en el **Borrador Oficial Renta WEB 2024**:

| Casilla | Descripción Oficial AEAT | Importe (€) |
| :---: | :--- | :---: |
| **0167** | Epígrafe I.A.E. (Actividad profesional arquitecto) | `411` |
| **0168** | Modalidad de determinación del rendimiento neto | `Simplificada` |
| **0180** | Total ingresos computables de la actividad | `267.000,00` |
| **0184** | Sueldos y salarios | `120.000,00` |
| **0185** | Seguridad Social a cargo de la empresa | `40.000,00` |
| **0194** | Suministros (electricidad, agua, telecomunicaciones) | `55.000,00` |
| **0208** | Dotación del ejercicio para amortización de inmovilizado | `9.840,00` |
| **0218** | Suma de gastos fiscalmente deducibles | `224.840,00` |
| **0221** | Diferencia en modalidad simplificada `[(0180) - (0218)]` | `42.160,00` |
| **0222** | Provisiones deducibles y gastos de difícil justificación (tope legal 2.000 €) | `2.000,00` |
| **0224** | **Rendimiento neto de actividades económicas** | `40.160,00` |
| **1826** | Valor de transmisión del solar (150.000 € - 15.000 €) | `135.000,00` |
| **1830** | Valor de adquisición del solar | `80.000,00` |
| **1833** | **Ganancia patrimonial obtenida (solar C/ Costera)** | `55.000,00` |
| **0435 / 0505** | **Base liquidable general sometida a gravamen** | `40.160,00` |
| **0460 / 0510** | **Base liquidable del ahorro** | `55.000,00` |
| **0511** | Mínimo del contribuyente estatal | `5.550,00` |
| **0512** | Mínimo del contribuyente autonómico (Comunitat Valenciana) | `6.105,00` |
| **0532** | Cuota estatal correspondiente a la BL General | `4.753,10` |
| **0533** | Cuota autonómica correspondiente a la BL General | `4.658,55` |
| **0540** | Cuota estatal correspondiente a la BL del Ahorro | `5.765,00` |
| **0541** | Cuota autonómica correspondiente a la BL del Ahorro | `5.765,00` |
| **0545 / 0570** | Cuota líquida estatal | `10.518,10` |
| **0546 / 0571** | Cuota líquida autonómica | `10.423,55` |
| **0587 / 0700** | **Resultado de la autoliquidación a ingresar** | **`20.941,65`** |
