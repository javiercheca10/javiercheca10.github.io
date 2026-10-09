/**
  * @file calculadora.cpp
  * @brief Programa para realizar una operación simple entre dos números (Ej. 2.18)
  *
  * @author Francisco Javier Checa Casas
  * @date 13-Octubre-2021
  *
  * Escriba un programa que haga las funciones de una calculadora básica: suma,
  * resta, multiplicación y división. Para ello, el programa debe leer dos números
  * enteros y un carácter que indique la operacióna realizar (+, -, *, /), mostrando
  * el resultado a continuación. Por ejemplo, ante esta entrada:
  *       34 12 +
  * el programa mostrará esta salida:
  *        46
  */
#include <iostream>
using namespace std;

  int main(){
    char c;
    double a,b;

    cout<<"Introduzca dos numeros seguidos de la operacion que desea realizar entre ellos"<<endl;
    cin>>a>>b>>c;

    if (c=='+')
    {
          cout << a+b;
    }
    else if (c=='-')
    {
          cout << a-b;
    }
    else if (c=='*')
    {
          cout << a*b;
    }
    else if (c=='/')
    {
          cout << a/b;
    }
    else {
        cout << "Formato no valido";
    }
  return(0);
  }
