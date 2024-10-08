// Crea un juego interactivo por terminal en el que tendrás que adivinar el resultado de diferentes operaciones
//  matemáticas aleatorias (suma, resta, multiplicación o división de dos números enteros).
//     • Tendrás 3 segundos para responder correctamente.
//     • El juego finaliza si no se logra responder en ese tiempo.
//     • Al finalizar el juego debes mostrar cuántos cálculos has acertado.
//     • Cada 5 aciertos debes aumentar en uno el posible número de cifras de la operación (cada vez en 
//       un operando):
//         ◦ Preguntas 1 a 5: X (entre 0 y 9) operación Y (entre 0 y 9)
//         ◦ Preguntas 6 a 10: XX (entre 0 y 99) operación Y (entre 0 y 9)
//         ◦ Preguntas 11 a 15: XX operación YY
//         ◦ Preguntas 16 a 20: XXX (entre 0 y 999) operación YY
//         ◦ ...

// https://github.com/mouredev/retos-programacion-2023/blob/main/Retos/Reto%20%2344%20-%20ADIVINANZAS%20MATEM%C3%81TICAS%20%5BMedia%5D/ejercicio.md

using System;
using System.Threading;
using System.Threading.Tasks;

namespace adivinanzasMatematicas;

public class AdivMatematicas(){
    public static void ejecutarAdivMatematicas(){

    }

    public int numRandom(int digitos){
        Random random = new Random();
        int valorMaximo = (int)Math.Pow(10, digitos);
        return random.Next(0, valorMaximo);
    }
}