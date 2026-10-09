/**
  * @file temparaturas.cpp
  * @brief Programa para transformar entre escalas de temperatura (Ej. 2.3)
  *
  * @author Francisco Javier Checa Casas
  * @date 13-Octubre-2021
  *
  * Escriba un programa que permita traducir entre grados Celsius (C),
  * Fahrenheit (F), Kelvin (K) y Rankine (R). El programa preguntará en qué unidades damos
  * la temperatura de entrada y a qué escala queremos convertir. Para ello sabemos que:
  *       K = C + 273'15    R = F + 459'67   9 C = 5(F - 32)
  * Tenga en cuenta que el programa pregunta la temperatura y que ésta se introduce como un
  * número seguido de dos letras que indican las unidades. Por ejemplo: 35CF indica que
  * queremos pasar 35 grados Celsius (C) a grados Fahrenheit (F).
  *
  * Importante: no se permite usar operadores lógicos (&&, ||, !). Posiblemente la primera idea
  * que nos viene a la cabeza para resolver este problema es establecer las fórmulas para
  * convertir de todas a todas las escalas. Esto nos da un total de 4x4=16 fórmulas diferentes
  * (si tuviésemos más escalas, la cantidad de fórmulas aumenta rápidamente). Esta
  * solución, además, necesitaría el uso de condiciones compuestas (que usan operadores
  * lógicos). Debe pensar en una solución alternativa.
  *
  */
#include <iostream>
using namespace std;

int main(){

int d;
double a;
char b,c;

cout << "Introduzca la temperatura seguida de la unidad en la que esta y la unidad que desea convertirla ambas en mayusculas"<<endl;
cin >> a >> b >> c;

    if (b=='K')
        { a=a-273.15; }

    else if (b=='F')
        { a=((a-32)*5)/9; }

    else if (b=='R')
        { a=((a-491.67)*5)/9; }
    else
        { a=a; }


    if (c=='K')
        { a=a+273.15; }

    else if (c=='F')
        { a=((a*9)/5)+32; }

    else if (c=='R')
        { a=((a*9)/5)+491.67; }
    else
        { a=a; }


cout<<"La temperatura en la unidad deseada es "<<a;

return(0);
}
