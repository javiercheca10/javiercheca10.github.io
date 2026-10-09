# Bases de Datos Relacionales · Tráfico Marítimo & Flota de Buques
**Asignatura:** Databases (DB)  
**Institución:** University of Piraeus (Atenas) · Erasmus+  
**Autor:** Francisco Javier Checa Casas  
**Conjunto de Datos:** `Vessels.csv`, `VesselTypes.csv`  

---

## 1. Contexto & Dominio del Problema
En el marco de la asignatura de Bases de Datos en la University of Piraeus (ubicada junto a uno de los puertos mercantes y de pasajeros más importantes del Mediterráneo), se aborda el diseño lógico y físico de un sistema relacional para la **monitorización, clasificación y análisis de buques y tráfico marítimo**:
* **Objetivo:** Normalizar la información de buques mercantes, petroleros, portacontenedores, pesqueros y embarcaciones de pasaje.
* **Modelo relacional:** Descomposición en entidades normalizadas (3FN / BCNF) para evitar anomalías de inserción, modificación y borrado.

---

## 2. Esquema Relacional & Tablas Normalizadas

### 2.1. Tabla `VesselTypes` (Tipos de Buques)
Almacena el catálogo de categorías normalizadas según la clasificación marítima internacional de la OMI (Organización Marítima Internacional):
* `VesselTypeID` (INT, PRIMARY KEY): Identificador numérico del tipo de embarcación.
* `TypeName` (VARCHAR(100), NOT NULL): Denominación estandarizada (e.g., *Cargo*, *Tanker*, *Passenger*, *Tug*, *Fishing*, *Pleasure Craft*).
* `Description` (TEXT): Descripción operativa y requisitos normativos de la categoría.

```sql
CREATE TABLE VesselTypes (
    VesselTypeID INT PRIMARY KEY,
    TypeName VARCHAR(100) NOT NULL UNIQUE,
    Description TEXT
);
```

### 2.2. Tabla `Vessels` (Buques)
Registra las características físicas, técnicas y de registro de cada barco:
* `VesselID` (INT, PRIMARY KEY): Identificador interno o número IMO único.
* `VesselName` (VARCHAR(150), NOT NULL): Nombre del barco.
* `VesselTypeID` (INT, FOREIGN KEY): Referencia foránea a `VesselTypes(VesselTypeID)`.
* `MMSI` (VARCHAR(9)): Número identificativo para el sistema AIS de radio marítima.
* `Flag` (VARCHAR(50)): País de bandera y pabellón nacional.
* `Length` (DECIMAL(6,2)): Eslora total en metros.
* `Width` (DECIMAL(5,2)): Manga en metros.
* `DWT` (INT): Arqueo y peso muerto en toneladas (*Deadweight Tonnage*).

```sql
CREATE TABLE Vessels (
    VesselID INT PRIMARY KEY,
    VesselName VARCHAR(150) NOT NULL,
    VesselTypeID INT NOT NULL,
    MMSI VARCHAR(9) UNIQUE,
    Flag VARCHAR(50),
    Length DECIMAL(6,2),
    Width DECIMAL(5,2),
    DWT INT,
    FOREIGN KEY (VesselTypeID) REFERENCES VesselTypes(VesselTypeID)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);
```

---

## 3. Consultas Analíticas Clave (SQL)

### 3.1. Distribución de Flota por Tipo y Eslora Media
```sql
SELECT 
    vt.TypeName,
    COUNT(v.VesselID) AS TotalVessels,
    ROUND(AVG(v.Length), 2) AS AvgLengthMeters,
    SUM(v.DWT) AS TotalTonnageDWT
FROM VesselTypes vt
LEFT JOIN Vessels v ON vt.VesselTypeID = v.VesselTypeID
GROUP BY vt.VesselTypeID, vt.TypeName
ORDER BY TotalVessels DESC;
```

### 3.2. Búsqueda de Buques de Gran Tonelaje por Pabellón
```sql
SELECT 
    v.VesselName,
    v.Flag,
    vt.TypeName,
    v.DWT
FROM Vessels v
INNER JOIN VesselTypes vt ON v.VesselTypeID = vt.VesselTypeID
WHERE v.DWT > 50000
ORDER BY v.DWT DESC
LIMIT 10;
```
