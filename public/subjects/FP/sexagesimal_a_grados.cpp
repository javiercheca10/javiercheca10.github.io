/**
  * @file sexagesimal2grados.cpp
  * @brief Programa para pasar de grados/minutos/segundos a grados
  *
  * @author Francisco Javier Checa Casas
  * @date 13-Octubre-2021
  *
  * El programa recibe como entrada un entero (entre 0 y 359) que indica grados, un carácter
  * 'g' que simboliza grados, un entero (entre 0 y 59), un carácter 'm' que simboliza minutos
  * y un real en el intervalo [0,60) seguido de un carácter 's' que simboliza segundos. Como
  * salida obtiene el número de grados correspondiente como número real.
  * Por ejemplo, con la entrada:
  *    34g 34m 1.2s
  * debería obtener la salida:
  *    34.567 grados
  *
  * Además, deberá comprobar que se cumplen las condiciones, es decir, si algún valor no
  * está en el rango correcto o algún carácter simbólico no es el esperado, la salida debe
  * indicar que hay un error de formato.
  */
#include <iostream>
using namespace std;
int main(){
int c;
double a,b;
char g,m,s;

cout<<"Introduzca el numero de grados minutos y segundos que desea convertir a grados"<<endl;
cin>>a>>g>>b>>m>>c>>s;

    if (a<=0){
        cout<<"El numero de grados debe ser mayor que 0";
        return(0);
    }
    else if (a>=359){
        cout<<"El numero de grados debe ser menor de 360";
        return(0);
    }


    if (g!='g'){
        cout<<"Despues de los grados debe escribir una g minuscula";
        return(0);
    }

    if (b<=0){
        cout<<"El numero de minutos debe ser mayor que 0";
        return(0);
    }
    else if (b>=59){
        cout<<"El numero de minutos debe ser menor de 60";
        return(0);
    }

    if (m!='m'){
        cout<<"Despues de los minutos debe escribir una m minuscula";
        return(0);
    }

        if (c<0){
        cout<<"El numero de segundos debe ser mayor que 0";
        return(0);
    }
    else if (c>=60){
        cout<<"El numero de segundos debe ser menor de 60";
        return(0);
    }

    if (s!='s'){
        cout<<"Despues de los segundos debe escribir una s minuscula";
        return(0);
    }

return(0);
}
