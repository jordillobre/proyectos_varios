# Los primeros dispositivos móviles tenían un teclado llamado T9 con el que se podía escribir
# texto utilizando únicamente su teclado numérico (del 0 al 9).

# Crea una función que transforme las pulsaciones del T9 a su representación con letras.
# - Debes buscar cuál era su correspondencia original.
# - Cada bloque de pulsaciones va separado por un guión.
# - Si un bloque tiene más de un número, debe ser siempre el mismo.
# - Ejemplo:
#     Entrada: 6-666-88-777-33-3-33-888
#     Salida: MOUREDEV

t9_a_letras = {
    "1": ",",  "11": ".",  "111": "?", "1111": "!",
    "2": "A",  "22": "B",  "222": "C",
    "3": "D",  "33": "E",  "333": "F",
    "4": "G",  "44": "H",  "444": "I",
    "5": "J",  "55": "K",  "555": "L",
    "6": "M",  "66": "N",  "666": "O",
    "7": "P",  "77": "Q",  "777": "R",  "7777": "S",
    "8": "T",  "88": "U",  "888": "V",
    "9": "W",  "99": "X",  "999": "Y",  "9999": "Z",
    "0": " " 
}

letras_a_T9 = {
    ",":"1",  ".": "11",  "?": "111",  "!": "1111",
    "A": "2",  "B": "22",  "C": "222",
    "D": "3",  "E": "33",  "F": "333",
    "G": "4",  "H": "44",  "I": "444",
    "J": "5",  "K": "55",  "L": "555",
    "M": "6",  "N": "66",  "O": "666",
    "P": "7",  "Q": "77",  "R": "777",  "S": "7777",
    "T": "8",  "U": "88",  "V": "888",
    "W": "9",  "X": "99",  "Y": "999",  "Z": "9999",
    " ": "0"
}

def tecladoT9():
    print("Opciones disponibles")
    print("0: Terminar la ejecución del código")
    print("1: Traducir a teclado T9")
    print("2: Traducir de T9 a español")

    repetir = True

    while repetir:
        try:
            opcion = int(input("¿Qué opción quieres realizar? "))
            if opcion == 0:
                repetir = False
            elif opcion == 1:
                traducir_a_t9()
            elif opcion == 2:   
                traducir_de_t9()
            else:
                print("Opción no válida. Por favor, elige un número mostrado en la lista.")
        except ValueError:
            print("Error: Debes introducir un número entero válido.")

def traducir_a_t9():
    texto_traducir = input("Introduce el texto que quieras traducir a T9: ").upper()
    resultado = ""

    for i in range(len(texto_traducir)):
        letra = texto_traducir[i]
        if letra in letras_a_T9:
            if i == len(texto_traducir) - 1:
                resultado += letras_a_T9[letra]
            else:
                resultado += letras_a_T9[letra] + "-"
        else:
            print(f"El carácter '{letra}' no puede ser traducido.")
    print(f"El texto '{texto_traducir}' traducido a T9 sería: {resultado}")
    
def traducir_de_t9():
    texto = input("Introduce el texto que quieras traducir de T9: ")
    secuencias = texto.split("-")
    resultado = ""

    for secuencia in secuencias:
        if secuencia in t9_a_letras:
            resultado += t9_a_letras[secuencia]
        else:
            print(f"La secuencia '{secuencia}' no puede ser traducida.")
    
    print(f"Texto '{texto}' traducido de T9 a español: {resultado}")

tecladoT9()