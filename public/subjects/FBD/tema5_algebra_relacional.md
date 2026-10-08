# Álgebra Relacional: Formulario Maestro de Operaciones y Restricciones

--- PÁGINA: IMG_1115.HEIC ---

# Fundamentos de Bases de Datos - Álgebra Relacional

## 1. Operación de Selección ($\sigma$)
Se utiliza para elegir filas específicas que satisfacen una condición. Es equivalente conceptualmente al operador `WHERE` de SQL.

$$\sigma_{\text{condición}}(R)$$

---

## 2. Operación de Proyección ($\pi$)
Se utiliza para elegir columnas específicas. Es equivalente a la cláusula `SELECT` de SQL.

$$\pi_{\text{columnas}}(R)$$

---

## 3. Operación de Renombrar ($\rho$)
Permite cambiar el nombre de una relación o el de sus atributos.

$$\rho_{\text{nuevo\_nombre}}(R)$$

---

## 4. Producto Cartesiano ($\times$)
Combina todas las filas de dos relaciones, devolviendo todas las combinaciones posibles de tuplas.

$$\text{Estudiantes} \times \text{Grados}$$

---

## 5. Unión ($\cup$)
Combina las filas de dos relaciones compatibles, eliminando las tuplas duplicadas.

$$\text{Estudiantes} \cup \text{Graduados}$$

---

## 6. Intersección ($\cap$)
Encuentra las filas comunes presentes en ambas relaciones.

$$\text{Estudiantes} \cap \text{Graduados}$$

--- PÁGINA: IMG_1116.HEIC ---

## 7. Diferencia ($-$)
Encuentra las filas que están en el primer conjunto y no están en el segundo.

$$\text{Estudiantes} - \text{Graduados}$$

---

## 8. Agrupación ($\gamma$)
Agrupa filas que comparten un valor en común aplicando funciones de agregación.

$$\gamma_{\text{valores\_en\_común, lista\_de\_funciones}}(R)$$

---

### Funciones de Agregación:

* **9. SUM**
  Calcula la suma de un atributo numérico.
  $$\text{SUM}(\text{columna})$$

* **10. AVG**
  Calcula la media aritmética.
  $$\text{AVG}(\text{columna})$$

* **11. MIN**
  Calcula el valor mínimo.
  $$\text{MIN}(\text{columna})$$

* **12. MAX**
  Calcula el valor máximo.
  $$\text{MAX}(\text{columna})$$

* **13. COUNT**
  Cuenta el número de filas o tuplas.
  $$\text{COUNT}(\text{columna})$$

---

## 14. División Relacional ($\div$)
Encuentra todas las tuplas que están asociadas con todas las tuplas de otra relación.

$$R_1 \div R_2$$

--- PÁGINA: IMG_1117.HEIC ---

## 15. Vistas ($\leftarrow$)
Define una consulta almacenada que puede ser reutilizada como si fuera una relación base.

$$\text{Vista} \leftarrow \text{consulta}$$

---

## 16. Restricciones de Integridad (SQL DDL)

* **16.1. PRIMARY KEY**
  ```sql
  PRIMARY KEY (columna)
  ```

* **16.2. FOREIGN KEY**
  ```sql
  FOREIGN KEY (columna) REFERENCES otra_tabla(columna)
  ```

* **16.3. UNIQUE**
  ```sql
  UNIQUE (columna)
  ```

* **16.4. CHECK**
  ```sql
  CHECK (condición)
  ```

* **16.5. NOT NULL**
  ```sql
  nombre_columna TIPO NOT NULL
  ```

---

## 📌 Formulario & Chuletario de Resumen

| Operación / Concepto | Notación Formal (Álgebra Relacional) | Equivalente en SQL / Sintaxis DDL | Descripción Rápida |
| :--- | :--- | :--- | :--- |
| **Selección** | $\sigma_{\text{cond}}(R)$ | `WHERE` | Filtra filas (horizontal). |
| **Proyección** | $\pi_{\text{attr}}(R)$ | `SELECT DISTINCT` | Selecciona columnas (vertical). |
| **Renombrado** | $\rho_{\text{nuevo}}(R)$ | `AS` | Cambia nombres de relación/atributos. |
| **Producto Cartesiano** | $R \times S$ | `CROSS JOIN` | Multiplica tuplas de dos relaciones. |
| **Unión** | $R \cup S$ | `UNION` | Suma conjuntos eliminando duplicados. |
| **Intersección** | $R \cap S$ | `INTERSECT` | Elementos comunes en ambos conjuntos. |
| **Diferencia** | $R - S$ | `EXCEPT` / `MINUS` | Elementos de $R$ que no están en $S$. |
| **Agrupación** | $\gamma_{\text{grupo, func}}(R)$ | `GROUP BY` + Agregados | Agrupa y aplica funciones resumen. |
| **División** | $R_1 \div R_2$ | *Subconsultas anidadas* | Encuentra tuplas relacionadas con *todos* los elementos. |
| **Vista** | $\text{Vista} \leftarrow Q$ | `CREATE VIEW AS` | Consulta reutilizable. |
| **Clave Primaria** | N/A | `PRIMARY KEY (col)` | Identificador único de tupla. |
| **Clave Foránea** | N/A | `FOREIGN KEY ... REFERENCES` | Integridad referencial entre tablas. |