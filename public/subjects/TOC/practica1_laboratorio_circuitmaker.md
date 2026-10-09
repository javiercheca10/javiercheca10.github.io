# Práctica 1 de Laboratorio · Simulación Digital con CircuitMaker
**Asignatura:** Tecnología y Organización de Computadores (TOC)  
**Etapa:** 1º Curso · Doble Grado Ingeniería Informática + ADE (UGR)  
**Autor:** Francisco Javier Checa Casas  
**Archivos de Circuito:** `Circuit1.cct`, `Circuit2.cct`  
**Capturas de Simulación:** `ejercicio1_circuitmaker.png`, `ejercicio2_circuitmaker.png`  

---

## 1. Objetivos del Laboratorio
El objetivo de la sesión práctica de laboratorio consiste en familiarizarse con el entorno CAD de simulación de circuitos digitales **CircuitMaker (Student Edition)**:
* Diseñar esquemas circuitales a nivel de puertas lógicas básicas (AND, OR, NOT, XOR, NAND).
* Conectar generadores de pulsos, interruptores biestables (*Logic Switches*) e instrumentos virtuales de visualización lógica (*Logic Displays* / osciloscopio).
* Verificar experimentalmente las tablas de verdad de funciones booleanas combinacionales.

---

## 2. Circuito 1: Implementación de Función Combinacional (`Circuit1.cct`)
* **Esquema:** Circuito con entradas binarias $A, B, C$ alimentando una red de puertas AND y OR para materializar la expresión lógica simplificada.
* **Verificación:** Se inyectan las 8 combinaciones de entrada posibles ($000_2$ a $111_2$) monitorizando que el estado de salida concuerde exactamente con la tabla de verdad teórica.
* **Captura del esquema:** `ejercicio1_circuitmaker.png`.

---

## 3. Circuito 2: Red Universal con Puertas NAND (`Circuit2.cct`)
* **Esquema:** Transformación de la función canónica utilizando exclusivamente la familia universal **NAND** mediante la aplicación del teorema de De Morgan y doble negación.
* **Ventaja física:** Demostrar cómo una única familia de circuitos integrados TTL (e.g., 74LS00 con cuatro puertas NAND de 2 entradas) reduce el número de encapsulados físicos en la placa de prototipado (*protoboard*).
* **Captura del esquema:** `ejercicio2_circuitmaker.png`.
