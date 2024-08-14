// Crea una función que reciba dos parámetros para crear una cuenta atrás.
//     • El primero, representa el número en el que comienza la cuenta.
//     • El segundo, los segundos que tienen que transcurrir entre cada cuenta.
//     • Sólo se aceptan números enteros positivos.
//     • El programa finaliza al llegar a cero.
//     • Debes imprimir cada número de la cuenta atrás.

// https://github.com/mouredev/retos-programacion-2023/blob/main/Retos/Reto%20%2327%20-%20CUENTA%20ATR%C3%81S%20%5BMedia%5D/ejercicio.md
using System;
using System.Threading;

namespace cuentaAtras;
public class CuentaAtras{
    public static void EjecutarCuentaAtras(){
        Console.WriteLine("Vamos a comenzar la cuenta atrás");
        int interacciones = 0;
        int segundos = 0;
        string input = "";

        bool repetir = true;
        while(repetir){
            Console.WriteLine("¿Número por el que quieres empezar a contar? ");
            input = Console.ReadLine();
            try{
                interacciones = int.Parse(input);  
                repetir = false ;  
            }catch (FormatException){
                Console.WriteLine("Error: Debes introducir un número entero válido.");
            }
        }

        repetir = true;
        while(repetir){
            Console.WriteLine("¿Cuantos segundos quieres esperar entre interacciones? ");
            input = Console.ReadLine();
            try{
                segundos = int.Parse(input);  
                repetir = false ;  
            }catch (FormatException){
                Console.WriteLine("Error: Debes introducir un número entero válido.");
            }
        }

        Console.Clear();

        for(int i = interacciones; i>=0; i--){
            Console.WriteLine(i);
            Thread.Sleep(segundos * 1000);
        }
 
    }
}