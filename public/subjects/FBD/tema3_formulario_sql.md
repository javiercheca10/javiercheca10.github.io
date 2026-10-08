# SQL Completo: Formulario y Sintaxis de Creación, Consultas y Modificación

---

## 1. Creación de Tablas

```sql
CREATE TABLE "nombre_tabla" (
    "nombre_columna" "Tipo_dato" "modificador",
    ...
);
```

### Ejemplo:
```sql
CREATE TABLE alumnos (
    DNI CHAR(9) PRIMARY KEY,
    nom_alum VARCHAR2(35)
);
```

### Tipos de Modificadores:
* **`PRIMARY KEY`**: Asigna la columna como clave primaria.
* **`UNIQUE`**: El atributo debe tener un valor único para cada tupla.
* **`NOT NULL`**: El atributo no puede ser nulo.
* **`CHECK (<condición>)`**: Los valores de las tuplas deben cumplir la condición.
* **`FOREIGN KEY "nombre" REFERENCES "id_tabla"`**: Definición de claves externas.
* **`DEFAULT`**: Valor por defecto.

---

## 2. Eliminación de Tablas

```sql
DROP TABLE "id_tabla" CASCADE CONSTRAINTS;
```
> **Nota:** `CASCADE CONSTRAINTS` se usa para forzar el borrado cuando de ella dependen otras tablas.

---

## 3. Modificación de Tablas

```sql
ALTER TABLE "id_tabla" Modificador;
```

### Tipos de Modificadores:
* **`ADD ("declaración normal")`**: Añade un atributo.
* **`ADD CONSTRAINT "nombre_restricción" ["declaración_restricción"]`**: Añade una restricción.
* **`DROP CONSTRAINT "nombre_restricción" [CASCADE]`**: Elimina una restricción.

---

## 4. Consultas

```sql
SELECT [DISTINCT] "columna" 
FROM "tabla" 
WHERE "condición";
```

* **Operadores:** `>`, `<`, `AND`, `OR`, `LIKE`, `BETWEEN`, `IN`, `EXISTS`.

---

## 4.1. Combinación (JOIN)

```sql
SELECT estudiantes.nombre, estudiantes.grado, grados.tutor
FROM estudiantes
TIPO_JOIN grados ON estudiantes.grado = grados.grado;
```

### Tipos de `TIPO_JOIN`:
* **`INNER JOIN`**: Devuelve las filas con coincidencias en ambas tablas.
* **`RIGHT JOIN`**: Devuelve todas las filas de la derecha y las coincidentes de la izquierda. Si no hay, incluirá `NULL` en la de la izquierda.
* **`LEFT JOIN`**: Lo mismo al revés.
* **`FULL OUTER JOIN`**: Combina los dos anteriores; devuelve todas las filas de ambas tablas. Si hay filas en una de las tablas sin coincidencias, incluirá `NULL` en la tabla que no tiene coincidencias.

---

## 4.2. Agrupar

```sql
GROUP BY "nombre_atributo";
```

### Ejemplo: Agrupar estudiantes por grado
```sql
SELECT grado, COUNT(*) AS NumEstudi
FROM estudiantes
GROUP BY grado;
```

---

## 4.3. Ordenar

```sql
ORDER BY "nombre_atributo" "Modificador";
```

### Tipos de Modificador:
* **`ASC`** (ascendente)
* **`DESC`** (descendente)

### Ejemplo: Ordenar por edad
```sql
SELECT grado, COUNT(*) AS NumeroEstudiantes
FROM estudiantes
ORDER BY edad ASC;
```

---

## 5. Inserciones

```sql
INSERT INTO "nombre_tabla" ("campo1", "campo2", ..., "campoN") 
VALUES ("valoro1", "valor2", ..., "valorN");
```

---

## 6. Producto Cartesiano

```sql
SELECT *
FROM tabla1, tabla2
WHERE tabla1.atributo = tabla2.atributo;
```
> **Descripción:** Combina todas las filas de 2 o más tablas, devolviendo todas las combinaciones posibles.

---

## 7. Consultas Múltiples

* **`UNION`**: Combina los resultados eliminando duplicados.
* **`INTERSECT`**: Devuelve las filas comunes.
* **`MINUS`**: Devuelve las filas de la primera que no estén en la segunda.

---

## 8. Modificar Contenido de una Tabla

```sql
UPDATE "nombre_tabla"
SET "nombre_atributo" = "nuevo_valor"
[...]
[WHERE <condición>];
```

---

## 9. Borrado de Tuplas

```sql
DELETE FROM "nombre_tabla" 
WHERE <condición>;
```

---

## 10. División en SQL (Buscar las que tengan un conjunto completo)

```sql
SELECT * FROM "nombre_tabla" 
WHERE NOT EXISTS ("conjunto")
MINUS ("conjunto_en_los_buscados");
```

### Ejemplo: Alumnos matriculados en todas las asignaturas de segundo
```sql
SELECT m1.DNI 
FROM matricula m1 
WHERE NOT EXISTS (
    (SELECT asi# FROM asigna WHERE curso=2)
    MINUS
    (SELECT codasi# FROM matricula m2 WHERE m2.DNI = m1.DNI)
);
```

---

## 11. Views (Atajo)

```sql
CREATE VIEW "nombre_view" AS "consulta";
```

Ahora podemos hacer la consulta como una tabla:
```sql
SELECT * FROM "nombre_view";
```

---

## 📌 Formulario & Chuletario de Resumen

| Operación / Comando | Sintaxis Básica | Equivalente en Álgebra Relacional |
| :--- | :--- | :--- |
| **Selección** | `SELECT ... WHERE <cond>` | $\sigma_{cond}(R)$ |
| **Proyección** | `SELECT DISTINCT attr` | $\pi_{attr}(R)$ |
| **Producto Cartesiano** | `FROM R, S WHERE ...` | $R \times S$ |
| **Reunión (Join)** | `FROM R JOIN S ON ...` | $R \bowtie S$ |
| **Agrupación** | `GROUP BY attr` | $\gamma_{attr, \text{func}}(R)$ |
| **Unión** | `... UNION ...` | $R \cup S$ |
| **Intersección** | `... INTERSECT ...` | $R \cap S$ |
| **Diferencia** | `... MINUS ...` | $R - S$ |
| **División** | `NOT EXISTS (...) MINUS (...)` | $R \div S$ |