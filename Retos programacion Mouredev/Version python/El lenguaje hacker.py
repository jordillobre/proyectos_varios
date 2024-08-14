# Escribe un programa que reciba un texto y transforme lenguaje natural a "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje se caracteriza por sustituir caracteres alfanuméricos.
#     • Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) con el alfabeto y los números en "leet".
#     • (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")

# https://github.com/mouredev/retos-programacion-2023/blob/main/Retos/Reto%20%231%20-%20EL%20LENGUAJE%20HACKER%20%5BF%C3%A1cil%5D/ejercicio.md

leet ={
    "A": "4" ,      "B": "I3",  "C": "[",    "D": ")" ,     "E": "3",       "F": "|=",
    "G": "&" ,      "H": "#",   "I": "1",    "J": ",_|" ,   "K": ">|",      "L": "1",
    "M": "/\\/\\" , "N": "^/",  "O": "0",    "P": "|*" ,    "Q": "(_,)",    "R": "I2", 
    "S": "5",       "T": "7" ,  "U": "(_)",  "V": "\\/",    "W": "\\/\\/" , "X": "><",  
    "Y": "j",       "Z": "2",   " ": " ",
    "1": "L" ,      "2": "R",   "3": "E",   "4": "A",       "5": "S",
    "6": "b" ,      "7": "T",   "8": "B",   "9": "g",       "0": "o"
}

def traductor_leet():
    print("Opciones disponibles")
    print("0: Terminar la ejecución del código")
    print("1: Traducir al lenjuage leet")

    repetir = True

    while repetir:
        try:
            opcion = int(input("¿Qué opción quieres realizar? "))
            if opcion == 0:
                repetir = False
            elif opcion == 1:
                traducir_a_leet()
            else:
                print("Opción no válida. Por favor, elige un número mostrado en la lista.")
        except ValueError:
            print("Error: Debes introducir un número entero válido.")


def traducir_a_leet():
    texto_traducir = input("Introduce el texto que quieras traducir a leet: ").upper()
    resultado = ""

    for i in range(len(texto_traducir)):
        letra = texto_traducir[i]
        if letra in leet:
            resultado += leet[letra]
        else:
            print(f"El carácter '{letra}' no puede ser traducido.")
    print(f"El texto '{texto_traducir}' traducido a leet sería: {resultado}")


traductor_leet()