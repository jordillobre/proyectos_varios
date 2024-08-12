//  Crea un programa que sea capaz de solicitarte un número y se encargue de imprimir su tabla de multiplicar entre el 1 y el 10.
//  - Debe visualizarse qué operación se realiza y su resultado.
//      Ej: 1 x 1 = 1
//          1 x 2 = 2
//          1 x 3 = 3
//          ... 

using System;

namespace multiplicar;
public class Multiplicar{
    public static void EjecutarMultiplicar(){
        Console.WriteLine("¿Qué tabla de multiplicar deseas conocer? ");
        string valInput = Console.ReadLine();

        try{
            int num = int.Parse(valInput);
            for(int val=1; val<=10; val++ ){
                Console.WriteLine(num + " * " + val + " = " + (val * num));
            }
        }catch(FormatException){
            Console.WriteLine("Error: Debes de introducir un número entero válido");
        }
    }
}