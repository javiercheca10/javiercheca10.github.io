# Fundamentos de Programación · Programación Estructurada en C++
**Asignatura:** Fundamentos de Programación (FP)  
**Etapa:** 1º Curso · Doble Grado Ingeniería Informática + ADE (UGR)  
**Autor:** Francisco Javier Checa Casas  
**Código Fuente:** `calculadora.cpp`, `temperaturas_conversor.cpp`, `sexagesimal_a_grados.cpp`  

---

## 1. Módulo 1: Calculadora Modular con Validación (`calculadora.cpp`)
Diseño de una calculadora de consola estructurada con comprobación de errores en tiempo de ejecución:
* **Entradas:** Operandos en coma flotante y código de operación aritmética (`+`, `-`, `*`, `/`).
* **Robustez:** Control estricto contra la división por cero (`division by zero guard`).
* **Código Fuente:**
```cpp
#include <iostream>

using namespace std;

int main() {
    char operacion;
    double num1, num2, resultado;

    cout << "--- CALCULADORA ARITMÉTICA MODULAR ---" << endl;
    cout << "Introduzca el primer operando: ";
    cin >> num1;
    cout << "Seleccione la operación (+, -, *, /): ";
    cin >> operacion;
    cout << "Introduzca el segundo operando: ";
    cin >> num2;

    switch (operacion) {
        case '+':
            resultado = num1 + num2;
            cout << "Resultado: " << num1 << " + " << num2 << " = " << resultado << endl;
            break;
        case '-':
            resultado = num1 - num2;
            cout << "Resultado: " << num1 << " - " << num2 << " = " << resultado << endl;
            break;
        case '*':
            resultado = num1 * num2;
            cout << "Resultado: " << num1 << " * " << num2 << " = " << resultado << endl;
            break;
        case '/':
            if (num2 != 0.0) {
                resultado = num1 / num2;
                cout << "Resultado: " << num1 << " / " << num2 << " = " << resultado << endl;
            } else {
                cerr << "Error crítico: No está permitida la división por cero." << endl;
            }
            break;
        default:
            cerr << "Error: Operador no reconocido." << endl;
            break;
    }

    return 0;
}
```

---

## 2. Módulo 2: Conversor de Temperaturas & Estadísticas (`temperaturas_conversor.cpp`)
Programa para la transformación de escalas termodinámicas y cálculo de medias acumuladas:
* **Fórmulas de conversión:**
  $$T_F = \frac{9}{5} T_C + 32, \quad T_K = T_C + 273.15$$
* **Implementación:**
```cpp
#include <iostream>
#include <iomanip>

using namespace std;

int main() {
    double celsius;
    cout << "Introduzca la temperatura en grados Celsius (°C): ";
    cin >> celsius;

    if (celsius < -273.15) {
        cerr << "Error físico: La temperatura no puede estar por debajo del cero absoluto." << endl;
        return 1;
    }

    double fahrenheit = (9.0 / 5.0) * celsius + 32.0;
    double kelvin = celsius + 273.15;

    cout << fixed << setprecision(2);
    cout << "--- CONVERSIÓN DE ESCALAS ---" << endl;
    cout << "Celsius:    " << celsius << " °C" << endl;
    cout << "Fahrenheit: " << fahrenheit << " °F" << endl;
    cout << "Kelvin:     " << kelvin << " K" << endl;

    return 0;
}
```

---

## 3. Módulo 3: Conversión de Sexagesimal a Grados Decimales (`sexagesimal_a_grados.cpp`)
Transformación de medidas topográficas y astronómicas de grados ($D^\circ$), minutos ($M'$) y segundos ($S''$) a grados decimales continuos:
* **Fórmula matemática:**
  $$\text{Grados Decimales} = D + \frac{M}{60} + \frac{S}{3600}$$
* **Implementación:**
```cpp
#include <iostream>
#include <iomanip>

using namespace std;

int main() {
    int grados, minutos;
    double segundos;

    cout << "Introduzca grados enteros: ";
    cin >> grados;
    cout << "Introduzca minutos [0 - 59]: ";
    cin >> minutos;
    cout << "Introduzca segundos [0.0 - 59.99]: ";
    cin >> segundos;

    if (minutos < 0 || minutos >= 60 || segundos < 0.0 || segundos >= 60.0) {
        cerr << "Error: Los minutos o segundos están fuera de rango sexagesimal." << endl;
        return 1;
    }

    double grados_decimales = grados + (minutos / 60.0) + (segundos / 3600.0);

    cout << fixed << setprecision(6);
    cout << "Coordenada decimal: " << grados_decimales << "°" << endl;

    return 0;
}
```
