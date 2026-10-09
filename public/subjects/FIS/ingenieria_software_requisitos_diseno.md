# Ingeniería del Software · Requisitos, Casos de Uso & Diseño Conceptual
**Asignatura:** Fundamentos de Ingeniería del Software (FIS)  
**Etapa:** 3º Curso · Doble Grado Ingeniería Informática + ADE (UGR)  
**Autor:** Francisco Javier Checa Casas (con Ángel Torres López en ejercicios de equipo)  
**Documentos Fuente:** `ejercicio4_especificacion_requisitos.pdf`, `ejercicio2_modelado_casos_uso.pdf`, `control_modelo_gestion_almacenes.docx`, `modelo_diseno_videoclub.pdf`  

---

## 1. Análisis y Especificación de Requisitos Software

### 1.1. Inconsistencias en Modelos de Dominio
En la especificación de sistemas transaccionales (por ejemplo, gestión hotelera o reservas turísticas), los errores más frecuentes se producen en la asignación de multiplicidades y relaciones estructurales:
* **Relación Habitación–Cliente (Multiplicidad):** Modelar la relación como $1:1$ es un error crítico. La multiplicidad real debe ser $1:N$ o $N:M$ a lo largo del tiempo, ya que un mismo cliente puede realizar múltiples reservas de habitaciones a lo largo de su historial, y una habitación acoge a sucesivos huéspedes en fechas distintas.
* **Separación de Estados:** Es imperativo distinguir entre la entidad conceptual estática (`Habitación`) y la transacción dinámica temporal (`Reserva` o `Estancia`), evitando sobrecargar atributos temporales (fecha de entrada, fecha de salida) en el inventario físico.

---

## 2. Modelado de Casos de Uso (UML)

### 2.1. Jerarquía de Escenarios y Actores
El modelado funcional define las fronteras del sistema mediante casos de uso:
* **Actores Primarios:** Usuarios que inician la interacción para lograr un objetivo de negocio (e.g., *Cliente*, *Cajero*, *Administrador de Almacén*).
* **Actores Secundarios:** Sistemas externos o actores que proporcionan servicios de soporte (e.g., *Pasarela de Pagos*, *Servidor de Notificaciones SMS*).
* **Relaciones Estructurales:**
  * `<<include>>`: Comportamiento obligatorio que se ejecuta siempre como parte del caso de uso base (e.g., `ValidarCredenciales` dentro de `RealizarTransferencia`).
  * `<<extend>>`: Comportamiento opcional o condicional que se ejecuta únicamente si se cumple una condición de extensión (e.g., `SolicitarSeguroAdicional` al reservar un vehículo).

---

## 3. Modelo Conceptual de Clases: Sistema de Gestión de Almacenes (SGA)
Diseño conceptual para el control integral de existencias, pedidos de aprovisionamiento y expediciones:

### 3.1. Entidades Principales y Justificación de Diseño
1. **Producto & Pedido (Relación $N:M$ desagregada):**
   * Un producto puede formar parte de múltiples pedidos, y un pedido contiene múltiples líneas de producto.
   * Se crea la clase intermedia asociativa `LineaPedido` con atributos propios: `cantidadSolicitada`, `precioUnitario` y `descuentoAplicado`.
2. **Almacén & Ubicación Física:**
   * Un `Almacén` se compone de múltiples `Ubicaciones` (pasillo, estantería, altura).
   * La relación es de composición fuerte: una ubicación física no tiene sentido si desaparece el almacén.
3. **Gestión de Stock por Lotes:**
   * Para garantizar trazabilidad (caducidades y números de serie), el stock no se vincula solo al producto general, sino a una entidad `Lote` asociada a una `Ubicación` concreta.

---

## 4. Modelo de Diseño Orientado a Objetos: Sistema de Videoclub
Diseño formal de clases para la gestión de socios, préstamos y tarifas:

### 4.1. Diagrama de Clases
* **`Socio`:** Atributos: `numeroDeSocio`, `DNI`, `datosPersonales`, `fechaDeAlta`, `/saldo`. Operaciones: `consultarHistorial()`, `penalizar()`.
* **`Alquiler`:** Atributos: `fechaAlquiler`, `horaAlquiler`, `fechaDevolucion`, `horaDevolucion`, `devuelto` (booleano).
* **`Ejemplar` & `Pelicula`:** Patrón *Item-Descriptor*. La clase `Pelicula` almacena metadatos compartidos (título, director, género, sinopsis), mientras que `Ejemplar` modela las copias físicas individuales con su código de barras y estado de conservación (nuevo, desgastado, dañado).
* **Cálculo de Recargos:** Al devolver un ejemplar fuera del plazo estipulado, el sistema calcula de forma polimórfica la sanción según la tarifa asociada al tipo de soporte (estreno, catálogo clásico o videojuego).
