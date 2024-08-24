using fizzBuzz;
using multiplicar;
using tecladoT9;
using hacker;
using cuentaAtras;
using cifrado;
using recursividad;

class Program{
    static void Main(string[] args){

        string[] listRetos ={"Reto 01: El famoso fizz buzz",
                            "Reto 02: El lenguaje hacker",
                            "Reto 03: El teclado T9",
                            "Reto 04: Tabla de multiplicar",
                            "Reto 05: Cuenta atras",
                            "Reto 06: Cifrado César",
                            "Reto 07: Recursividad"};

        for (int i=0; i< listRetos.Length; i++){
            Console.WriteLine(listRetos[i]);
        }

        Console.WriteLine("¿Que reto quieres que se ejecute? ");
        string input = Console.ReadLine();

        try{
            int opcionSel = int.Parse(input);

            switch (opcionSel){
                case 01:
                    Console.Clear();
                    FizzBuzz.EjecutarFizzBuzz();
                    break;
                case 02:
                    Console.Clear();
                    Hacker.EjecutarHacker();
                    break;
                case 03:
                    Console.Clear();
                    TecladoT9.EjecutarTecladoT9();
                    break;
                case 04:
                    Console.Clear();
                    Multiplicar.EjecutarMultiplicar();
                    break;
                case 05:
                    Console.Clear();
                    CuentaAtras.EjecutarCuentaAtras();
                    break;
                case 06:
                    Console.Clear();
                    cifradoCesar.ejecutarCifrado();
                    break;
                case 07:
                    Console.Clear();
                    Recursividad.EjecutarRecursividad();
                    break;
                default:
                    Console.WriteLine("Opción no válida. Por favor, elige un número mostrado en la lista.");
                    break;
            }
        }catch(FormatException){
            Console.WriteLine("Error: Debes introducir un número entero válido.");
        }
   
    }
}