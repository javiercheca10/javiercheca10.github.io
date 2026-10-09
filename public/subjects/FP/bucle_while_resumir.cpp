/**
  * @file bucle_while_resumir.cpp
  * @brief Resume una secuencia de valores en franjas de tiempo
  *
  * @author Francisco Javier Checa Casas
  * @date 23-Noviembre-2021
  *
  * Escriba un programa para leer una secuencia de valores obtenidos en
  * intervalos de tiempo constantes para expresarlos en franjas de tiempo
  * simplificando los valores repetidos.
  *
  * Por ejemplo, podemos suponer que se determina el costo de la energía a lo
  * largo de un día y se quiere simplificar la información mostrando las
  * franjas con igual coste.
  *
  * El programa recibe como entrada:
  *   - El tiempo de comienzo de muestreo (horas:minutos:segundos).
  *   - El intervalo de muestreo o tiempo entre muestras (segundos).
  *   - Una secuencia de muestras, valores reales no negativos.
  *
  * La salida consiste en cada una de esas franjas en una línea donde se presenta
  * el tiempo de comienzo de la franja, el final, y el coste asociado.
  *
  * Por ejemplo, la entrada puede ser:
  *    00:00:00
  *    3600
  *    150 150 150 150 150 150 150 175 175 190 190 190
  *    190 190 170 170 180 200 200 200 200 190 190 190
  *    -1
  *
  * Y la salida correpondiente sería:
  *    00:00:00 07:00:00 150
  *    07:00:00 09: 00:00 175
  *    09:00:00 14:00:00 190
  *    14:00:00 16:00:00 170
  *    16:00:00 17:00:00 180
  *    17:00:00 21:00:00 200
  *    21:00:00 00:00:00 190
  *
  * Observe que en la entrada aparece un valor negativo para indicar el final
  * de la secuencia de valores.
  *
  * Note que los tiempos cambian sólo la hora porque el itervalo es de 3600
  * segundos. Si hubiera intervalos de muestreo menores se obtendrían fracciones
  * de hora (pruebe con muestreo cada 1 segundo o 30 segundos para comprobar
  * que su programa funciona correctamente).
  *
  * Tenga en cuenta que los valores de tiempo aparecen siempre con dos dígitos.
  * Por ejemplo, 1 hora y 5 segundos se debe escribir como 01:00:05.
  *
  * El programa también indicará que no hay datos si no hay muestras. Por ejemplo,
  * con la siguiente entrada:
  *    00:00:00
  *    3600
  *    -1
  *
  * Note que si hay algún dato, habrá al menos un intervalo. Con la entrada:
  *    00:00:00
  *    1800
  *    150 -1
  *
  * Obtendrá el intervalo:
  *    00:00:00 00:30:00 150
  *
  * El programa deberá estar resuelto en la función main. No se usarán vectores ni
  * funciones.
  *
  */
#include <iostream>
using namespace std;

int main(){
int h,m,s,t,muestras,b,contador=1,st,hi,si,mi;
char c;

    cout<<"Introduzca el intervalo de tiempo inicial: ";

    cin>>hi>>c>>mi>>c>>si;
    h=hi;
    m=mi;
    s=si;

    cout<<"Introduzca el tiempo entre muestras en segundos: ";

    cin>>t;

    cout<<"Introduzca la secuencia de muestras: ";

    cin>>muestras;
    //diferencio de cuando no hay muestras

        if(muestras>0){
                //bucle hasta que se introduzca un numero negativo

             while (muestras>=0){

                b=muestras;
                cin>>muestras;
                        //condicion para acumular en el contador el numero de numeros consecutivos iguales

                    if(b==muestras){
                        contador++;
                    }
                    else{
                            //cálculo de la hora final del intervalo
                        st=t*contador;
                        h=hi+(st/3600);
                        m=mi+((st%3600)/60);
                        s=si+(st%60);

                        //diferencio si es menor o mayor que 10 para ajustarme al formato

                        if(hi>10){
                            cout << hi << ":";
                        }
                        else{
                            cout << "0" << hi << ":" ;
                        }


                        if(mi>10){
                            cout << mi << ":";
                        }
                        else{
                            cout << "0" << mi << ":";
                        }


                        if(si>10){
                            cout << si << " " ;
                        }
                        else{
                            cout << "0" << si << " ";
                        }


                        if(h>10){
                            cout << h << ":";
                        }
                        else{
                            cout << "0" << h << ":" ;
                        }


                        if(m>10){
                            cout << m << ":";
                        }
                        else{
                            cout << "0" << m << ":";
                        }


                        if(s>10){
                            cout << s << " " << b << endl;
                        }
                        else{
                            cout << "0" << s << " " << b << endl;
                        }
                        //inicializo las variables para otro ciclo
                        contador=1;
                        hi=h;
                        mi=m;
                        si=s;
                    }
                }
            }

        else{
            cout<<"No hay muestras";
        }
return(0);
}
