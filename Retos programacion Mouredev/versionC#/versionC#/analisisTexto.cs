// Crea un programa que analice texto y obtenga:
// · Número total de palabras.
// · Longitud media de las palabras.
// · Número de oraciones del texto (cada vez que aparecen un punto).
// · Encuentre la palabra más larga.

// Todo esto utilizando un único bucle.

// https://github.com/mouredev/retos-programacion-2023/blob/main/

namespace analisisTexto;

public class AnalisisTexto(){
    public static void ejecutarAnalisisTexto(){

        string frase;
        int oraciones = 0;
        string[] palabrasMaxima, palabras;


        Console.WriteLine("Pasame el texto que quieres analizar:");
        frase = Console.ReadLine();

        if (frase.Length == 0){
             Console.WriteLine("El texto está vacío. Por favor, introduce un texto válido.");
             return;
        }

        palabras = frase.Split(' ');

        foreach(string palabra in palabras){
            
        }


    }
}
