// Crea un programa que realize el cifrado César de un texto y lo imprima.
// También debe ser capaz de descifrarlo cuando así se lo indiquemos.

// Te recomiendo que busques información para conocer en profundidad cómo  realizar el cifrado. Esto también forma parte del reto.

// https://github.com/mouredev/retos-programacion-2023/blob/main/Retos/Reto%20%2324%20-%20CIFRADO%20C%C3%89SAR%20%5BF%C3%A1cil%5D/ejercicio.md
using System;

namespace cifrado;

public class cifradoCesar(){
    public static void ejecutarCifrado(){
        string abecedario = "abcdefghijklmnopqrstuvwxyz";
        string resultado = "";
        string frase = "";
        string input = "";
        int sentido = 0;
        int desplazamiento = 0;

        bool repetir = true;

        Console.WriteLine("Dime la frase que quieres cifrar o descifrar: ");
        frase = Console.ReadLine();
        Console.WriteLine("Para desplazar las letras hacia la derecha escribe 1");
        Console.WriteLine("Para desplazar las letras hacia la izquierda escribe 2");

        while(repetir){
            Console.WriteLine("¿Qué opción quieres realizar?");
            input = Console.ReadLine();
            try{
                sentido = int.Parse(input);  
                if ((sentido == 1) | (sentido == 2)){
                    repetir = false ;  
                }else{
                    Console.WriteLine("Opción no valida, por favor escribe 1 o 2");
                }
                
            }catch (FormatException){
                Console.WriteLine("Error: Debes introducir un número entero válido.");
            }
        }
        repetir = true;
        while(repetir){
            Console.WriteLine("¿Cuantos espacios quieres que se desplacen tu letras?");
            input = Console.ReadLine();
            try{
                desplazamiento = int.Parse(input);  
                repetir = false ;  
            }catch (FormatException){
                Console.WriteLine("Error: Debes introducir un número entero válido.");
            }
        }

        int posCesar = 0;
        int posLetra = 0;

        frase = frase.ToLower();
            foreach (char letra in frase){
                if (abecedario.Contains(letra.ToString())){
                    posLetra = abecedario.IndexOf(letra.ToString());
                    
                    if (sentido == 1){
                        posCesar = (posLetra + desplazamiento) % 26;
                    }
                    else{
                        posCesar = (posLetra - desplazamiento + 26) % 26;
                    }

                    resultado += abecedario[posCesar];
                }
                else{
                    resultado += letra.ToString();
                }
            }

        Console.WriteLine($"La frase '{frase}'");
        Console.WriteLine("Mediante la codificación César marcada seria:");
        Console.WriteLine(resultado);
    }
}