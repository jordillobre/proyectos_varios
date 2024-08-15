// Escribe un programa que reciba un texto y transforme lenguaje natural a lenguaje hacker
// " (conocido realmente como "leet" o "1337"). Este lenguaje se caracteriza por sustituir caracteres alfanuméricos.
// - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) con el alfabeto y los números en 
// "leet".(Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")

namespace hacker{
    public class Hacker{

        private static Dictionary<string, string> simbolos = new Dictionary<string, string>(){
            { "A", "4"}, { "B", "I3"}, { "C", "["},
            { "D", ")"}, { "E", "3"}, { "F", "|="},
            { "G", "&"}, { "H", "#"}, { "I", "1"},
            { "J", ",_|"}, { "K", ">|"}, { "L", "1"},
            { "M", "/\\/\\"}, { "N", "^/"}, { "O", "0"},
            { "P", "|*"}, { "Q", "(_,)"}, { "R", "I2"}, { "S", "5"},
            { "T", "7"}, { "U", "(_)"}, { "V", "\\/"},
            { "W", "\\/\\/"}, { "X", "><"}, { "Y", "j"}, { "Z", "2"},
            { "1", "L"}, { "2", "R"}, { "3", "E"}, { "4", "A"}, { "5", "S"},
            { "6", "b"}, { "7", "T"}, { "8", "B"}, { "9", "g"}, { "0", "o"}, { " ", " "}
        };

        public static void EjecutarHacker(){
            Console.WriteLine("Opciones disponibles");
            Console.WriteLine("0: Terminar la ejecución del código");
            Console.WriteLine("1: Traducir al lenjuage leet");

            bool repetir = true;

            while (repetir){
                Console.WriteLine("¿Qué opción quieres realizar? ");
                string input = Console.ReadLine();

                try{
                    int opcionSel = int.Parse(input);
                    switch (opcionSel){
                        case 0:
                            repetir = false;
                            break;
                        case 1:
                            TraducirLeet();
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

        private static void TraducirLeet(){
            Console.WriteLine("Introduce el texto que quieras traducir a leet: ");
            string textoTraducir = Console.ReadLine();
            string textoMayus = textoTraducir.ToUpper();
            string resultado = "";

            for (int i = 0; i < textoMayus.Length; i++){
                string letra = textoMayus[i].ToString();
                if (simbolos.ContainsKey(letra)){
                    resultado += simbolos[letra];
                }
                else {
                    Console.WriteLine($"El carácter '{textoMayus[i]}' no puede ser traducido.");
                }
            }

            Console.WriteLine($"El texto: '{textoTraducir}' traducido a leet seria: {resultado}");
        }
    }
}