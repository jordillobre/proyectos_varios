// Los primeros dispositivos móviles tenían un teclado llamado T9 con el que se podía escribir 
// texto utilizando únicamente su teclado numérico (del 0 al 9).

// Crea una función que transforme las pulsaciones del T9 a su representación con letras.
// - Debes buscar cuál era su correspondencia original.
// - Cada bloque de pulsaciones va separado por un guión.
// - Si un bloque tiene más de un número, debe ser siempre el mismo.
// - Ejemplo:
//     Entrada: 6-666-88-777-33-3-33-888
//     Salida: MOUREDEV


namespace tecladoT9{
    public class TecladoT9{

        private static Dictionary<string, string> t9ALetras = new Dictionary<string, string>(){
            { "1", ","}, { "11", "."}, { "111", "?"}, { "1111", "!"},
            { "2", "A"}, { "22", "B"}, { "222", "C"},
            { "3", "D"}, { "33", "E"}, { "333", "F"},
            { "4", "G"}, { "44", "H"}, { "444", "I"},
            { "5", "J"}, { "55", "K"}, { "555", "L"},
            { "6", "M"}, { "66", "N"}, { "666", "O"},
            { "7", "P"}, { "77", "Q"}, { "777", "R"}, { "7777", "S"},
            { "8", "T"}, { "88", "U"}, { "888", "V"},
            { "9", "W"}, { "99", "X"}, { "999", "Y"}, { "9999", "Z"},
            { "0", " " }
        };

        private static Dictionary<string, string> letrasAT9 = new Dictionary<string, string>()
        {
            { ",","1" }, { ".", "11"}, { "?","111"}, { "!", "1111"},
            { "A", "2"}, { "B", "22"}, { "C", "222"},
            { "D", "3"}, { "E", "33"}, { "F", "333"},
            { "G", "4"}, { "H", "44"}, { "I", "444"},
            { "J", "5"}, { "K", "55"}, { "L", "555"},
            { "M", "6"}, { "N", "66"}, { "O", "666"},
            { "P", "7"}, { "Q", "77"}, { "R", "777"}, { "S", "7777"},
            { "T", "8"}, { "U", "88"}, { "V", "888"},
            { "W", "9"}, { "X", "99"}, { "Y", "999"}, { "Z", "9999"},
            { " ", "0" }
        };

        public static void EjecutarTecladoT9(){
            Console.WriteLine("Opciones disponibles");
            Console.WriteLine("0: Terminar la ejecución del código");
            Console.WriteLine("1: Traducir a teclado T9");
            Console.WriteLine("2: Traducir de T9 a español");

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
                            TraducirAT9();
                            break;
                        case 2:
                            TraducirDeT9();
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

        private static void TraducirAT9(){
            Console.WriteLine("Introduce el texto que quieras traducir a T9: ");
            string textoTraducir = Console.ReadLine();
            string textoMayus = textoTraducir.ToUpper();
            string resultado = "";

            for (int i = 0; i < textoMayus.Length; i++){
                string letra = textoMayus[i].ToString();
                if (letrasAT9.ContainsKey(letra)){
                    if (i == (textoMayus.Length - 1)){
                        resultado += letrasAT9[letra];
                    }else{
                        resultado += letrasAT9[letra] + "-";
                    }
                }
                else {
                    Console.WriteLine($"El carácter '{textoMayus[i]}' no puede ser traducido.");
                }
            }

            Console.WriteLine($"El texto: '{textoTraducir}' traducido a T9 seria: {resultado}");
        }

        private static void TraducirDeT9(){
            Console.WriteLine("Introduce el texto que quieras traducir de T9: ");
            string textoTraducir = Console.ReadLine();
            string resultado = "";

            // Separar los caracteres por espacios
            string[] secuencias = textoTraducir.Split('-');

            for (int i = 0; i < secuencias.Length; i++){
                string secuencia = secuencias[i];
                if (t9ALetras.ContainsKey(secuencia)){
                    resultado += t9ALetras[secuencia];
                }
                else{
                    Console.WriteLine($"La secuencia '{secuencia}' no puede ser traducida.");
                }
            }

            Console.WriteLine($"El texto '{textoTraducir}' traducido de T9 a español seria: {resultado}");
        }
    }
}