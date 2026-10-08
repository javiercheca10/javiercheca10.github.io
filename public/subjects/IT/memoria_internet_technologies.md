# Internet Technologies · Memoria Técnica & Guía de Prácticas

---

## 1. Identificación y Objetivos de la Asignatura
* **Asignatura:** Internet Technologies (Tecnologías de Internet)
* **Programa:** Erasmus+ · Atenas (Grecia)
* **Autor:** Javier Checa
* **Repositorio Oficial:** [github.com/javiercheca/Internet-Technologies](https://github.com/javiercheca10/Internet-Technologies)

La asignatura aborda de manera progresiva el ciclo de vida completo del desarrollo de aplicaciones web cliente-servidor:
1. **Frontend y Maquetación:** HTML5 semántico, maquetación CSS3, modelos de caja y diseño responsivo.
2. **Interactividad y DOM:** JavaScript moderno (ES6+), manipulación del árbol DOM, animaciones y validación robusta con expresiones regulares.
3. **Comunicación Asíncrona:** Arquitectura orientada a servicios ligeros con peticiones asíncronas `fetch()` hacia endpoints en backend.
4. **Backend y Persistencia:** Procesamiento dinámico del lado servidor en PHP y diseño/explotación de bases de datos relacionales en MySQL.

---

## 2. Desglose Estructurado de Laboratorios

```
Internet-Technologies/
├── lab1/             # Lab 1: Perfil personal y maquetación semántica
├── lab2/             # Lab 2: Portal comercial MyTelecom (Frontend)
├── lab3/             # Lab 3: Formulario de registro dinámico con Regex
├── lab4/             # Lab 4: Algoritmo de renderizado dinámico en DOM
├── lab5/             # Lab 5: Tarificador telefónico y persistencia fetch()
├── lab6/             # Lab 6: Backend PHP y base de datos relacional MySQL
└── myTelecom/        # PROYECTO FINAL INTEGRADO: Plataforma unificada
```

---

### Lab 1 · Perfil Personal y Fundamentos Web
* **Objetivo:** Construcción de la presencia digital inicial del estudiante en la universidad de intercambio.
* **Componentes clave:**
  * Estructura semántica en HTML5: jerarquía de títulos (`h1`, `h2`), párrafos estilizados, listados de hitos académicos y contenedor flotante de perfil (`profile.jpg`).
  * Saludo y cabecera en griego (`Καλώς ήρθατε στη σελίδα μου`).
  * Redirección por metadatos HTTP (`<meta http-equiv="refresh" content="10;url=about.html">`).

---

### Lab 2 · Portal Comercial "MyTelecom" (Frontend)
* **Objetivo:** Diseño y maquetación del portal comercial para un operador de telecomunicaciones griego.
* **Módulos implementados:**
  * **Catálogo de Servicios (`services.html`):** Planes de conectividad por fibra óptica, paquetes de telefonía móvil y servicios cloud corporativos.
  * **Red de Sucursales (`locations.html`):** Puntos de atención al público en **Atenas**, **Tesalónica** y **Creta**, integrados con mapa cartográfico de Grecia.
  * **Animaciones CSS:** Reglas `@keyframes rotateColors` para interpolación visual del logotipo y banners.
  * **Validación en Cliente (`validation.js`):** Interceptación de eventos de envío (`submit`), validación de número de teléfono con expresión regular `/^[0-9]{8,15}$/` y animación de opacidad progresiva (*fade-in*) del mensaje de confirmación.

---

### Lab 3 · Formulario de Alta y Seguridad de Credenciales
* **Objetivo:** Registro dinámico de clientes con controles de seguridad estricta en tiempo de ejecución.
* **Mecanismos técnicos:**
  * Inyección algorítmica de los selectores de fecha de nacimiento (días 1–31 y meses del año) mediante bucles JavaScript en el DOM.
  * Validación de contraseñas complejas:
    $$\text{Patrón Regex: } \texttt{\textasciicircum(?=.*[A-Z])(?=.*\textbackslash d).\{6,\}\$}$$
    Exige un mínimo de 6 caracteres, al menos un dígito numérico y al menos una letra mayúscula antes de permitir el envío.

---

### Lab 4 · Reto Algorítmico en DOM (Tree Challenge)
* **Objetivo:** Renderizado procedimental mediante manipulación directa del Document Object Model.
* **Algoritmo:**
  * El usuario introduce por teclado un entero $N \ge 1$ (altura del árbol).
  * El script computa para cada nivel $i \in [1, N]$ los espacios de alineación simétrica y genera $2i - 1$ caracteres asterisco (`*`).
  * Aplica un generador pseudoaleatorio de colores hexadecimales sobre cada nodo individualmente.

---

### Lab 5 · Tarificación Telefónica & Almacenamiento Asíncrono
* **Objetivo:** Simulación de consumo telefónico, cálculo de facturación por tramos y almacenamiento en backend sin recargar la página.
* **Lógica tarifaria:**
  $$\text{Tarifa}(t) = \begin{cases} 0{,}06 \cdot \lceil t / 60 \rceil & \text{si } \lceil t / 60 \rceil \le 3 \\ 0{,}18 + 0{,}04 \cdot (\lceil t / 60 \rceil - 3) & \text{si } \lceil t / 60 \rceil > 3 \end{cases}$$
* **Métricas y Parada:** Contador acumulativo de gasto; si el importe supera $10\text{ €}$ o se alcanzan $100$ llamadas, el proceso se interrumpe y calcula el porcentaje de llamadas de alto coste ($\ge 2\text{ €}$).
* **Persistencia:** Envío asíncrono con `fetch('save_call.php', { method: 'POST', body: JSON.stringify(...) })` hacia un script PHP que almacena las entradas en `call_records.txt`.

---

### Lab 6 · Arquitectura Backend & Base de Datos Relacional
* **Objetivo:** Integración cliente-servidor completa con persistencia ACID en MySQL.
* **Diseño del Esquema Relacional (`company_db`):**

```sql
CREATE DATABASE company_db;
USE company_db;

CREATE TABLE registrations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title ENUM('Mr.', 'Mrs.') NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    dob_day INT NOT NULL,
    dob_month INT NOT NULL,
    dob_year INT NOT NULL,
    marital_status ENUM('Married', 'Single') NOT NULL,
    address VARCHAR(255) NOT NULL,
    city VARCHAR(50) NOT NULL,
    region VARCHAR(50) NOT NULL,
    postal_code VARCHAR(10) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL,
    terms_accepted BOOLEAN NOT NULL
);
```

* **Scripts PHP:**
  * `save_registration.php`: Procesa los campos enviados por formulario POST, valida integridad referencial y persiste los registros en la tabla.
  * `search_registration.php`: Permite realizar búsquedas filtradas por nombre, apellidos o correo y presenta los resultados formateados en tablas HTML dinámicas.

---

## 3. Proyecto Maestro Integrado: `myTelecom`

El directorio `myTelecom` aglutina todas las prácticas bajo una arquitectura modular:

1. **Home (`index.html`):** Portada corporativa con banners y tipografía animada.
2. **About (`about/about.html`):** Presentación del estudiante y de la compañía.
3. **Services (`services/services.html`):** Oferta integral de telecomunicaciones.
4. **Locations (`locations/locations.html`):** Mapa interactivo de tiendas en Grecia.
5. **Contact (`contact/contact.html`):** Formulario validado con Regex.
6. **Challenge (`challenge/challenge.html`):** Reto algorítmico del árbol.
7. **Registration (`registration_form/register.html`):** Alta y consulta conectadas a MySQL.
8. **Call Statistics (`call_statistics/call_statistics.html`):** Simulador de facturación y auditoría.
