// EJERCICIO:
// Entiende el concepto de recursividad creando una función recursiva que imprima números del 100 al 0.

// DIFICULTAD EXTRA (opcional):
// Utiliza el concepto de recursividad para:
// · Calcular el factorial de un número concreto (la función recibe ese número).
// · Calcular el valor de un elemento concreto (según su posición) en la sucesión de Fibonacci (la función recibe la posición).

// https://github.com/mouredev/roadmap-retos-programacion/blob/main/Roadmap/06%20-%20RECURSIVIDAD/ejercicio.md

namespace recursividad{
    public class Recursividad{
        public static void EjecutarRecursividad(){
            bool repetir = true;

            Console.WriteLine("Para ejecutar la cuenta atrás desde 100 pulse 0");
            Console.WriteLine("Para calcular el factorial pulse 1");
            Console.WriteLine("Para calcular el valor de un elemento en la sucesión de Fibonacci pulse 2");

            while(repetir){
                Console.WriteLine("¿Qué opción quieres realizar? ");
                string input = Console.ReadLine();

                try{
                    int opcionSel = int.Parse(input);
                    switch (opcionSel){
                        case 0:
                            Console.Clear();
                            contarRecursivo(100);
                            repetir = false;
                            break;
                        case 1:
                            Console.Clear();
                            Console.WriteLine("Introduce el número para calcular el factorial:");
                            int numFactorial = int.Parse(Console.ReadLine());
                            Console.WriteLine($"Factorial de {numFactorial} es {factorial(numFactorial)}");
                            repetir = false;
                            break;
                        case 2:
                            Console.Clear();
                            Console.WriteLine("Introduce el índice para calcular el Fibonacci:");
                            int numFibonacci = int.Parse(Console.ReadLine());
                            Console.WriteLine($"Fibonacci({numFibonacci}) es {fibonacci(numFibonacci)}");
                            repetir = false;
                            break;
                        default:
                            Console.WriteLine("Opción no válida. Por favor, elige un número mostrado en la lista.");
                            break;
                    }
                }
                catch (FormatException){
                    Console.WriteLine("Error: Debes introducir un número entero válido.");
                }
            }
        }

        private static void contarRecursivo(int num){
            Console.WriteLine(num);
            if(num > 0){
                contarRecursivo(num - 1);
            }
        }

        private static int factorial(int n){
            if(n <= 1)
                return 1;
            return n * factorial(n - 1);
        }

        private static int fibonacci(int n){
            if(n <= 1)
                return n;
            return fibonacci(n - 1) + fibonacci(n - 2);
        }
    }
}