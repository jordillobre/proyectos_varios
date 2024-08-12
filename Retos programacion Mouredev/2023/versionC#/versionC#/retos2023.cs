using fizzBuzz;
using multiplicar;
using tecladoT9;

class Program{
    static void Main(string[] args){

        string[] listRetos ={"Reto 00: El famoso fizz buzz",
                            "Reto 30: El teclado T9",
                            "Reto 40: Tabla de multiplicar"};

        for (int i=0; i< listRetos.Length; i++){
            Console.WriteLine(listRetos[i]);
        }


        Console.WriteLine("¿Que reto quieres que se ejecute? ");
        string input = Console.ReadLine();

        try{
            int opcionSel = int.Parse(input);

            switch (opcionSel){
                case 0:
                    FizzBuzz.EjecutarFizzBuzz();
                    break;
                case 30:
                    TecladoT9.EjecutarTecladoT9();
                    break;
                case 40:
                    Multiplicar.EjecutarMultiplicar();
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