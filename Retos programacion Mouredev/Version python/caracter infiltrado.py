# Crea una función que reciba dos cadenas de texto casi iguales, a excepción de uno o varios caracteres.

# La función debe encontrarlos y retornarlos en formato lista/array.
# · Ambas cadenas de texto deben ser iguales en longitud.
# · Las cadenas de texto son iguales elemento a elemento.
# · No se pueden utilizar operaciones propias del lenguaje que lo resuelvan directamente.


# Ejemplos:
# Me llamo mouredev / Me llemo mouredov -> ["e", "o"]
# Me llamo.Brais Moure / Me llamo brais moure -> [" ", "b", "m"]

# https://github.com/mouredev/retos-programacion-2023/blob/main/Retos/Reto%20%2329%20-%20EL%20CAR%C3%81CTER%20INFILTRADO%20%5BF%C3%A1cil%5D/ejercicio.md

def comp_expresiones():
    infiltrados = []

    cad1 = input("Dime la primera cadena que quieres comprobar: ")
    cad2 = input("Dime la segunda cadena que quieres comprobar: ")

    if len(cad1) != len(cad2):
        print("las cadenas que me has pasado no tienen el mismo tamaño")
    else:
        for caracter in range (0, len(cad1)):
            if cad1[caracter] != cad2[caracter]:
                infiltrados.append(cad2[caracter])

    if len(infiltrados) == 0:
        print("No hay caracteres infiltrados en las cadenas que me has pasado")
    else:
        print("Los caracteres infiltrados en las cadenas que me has pasado son:")
        for letras in infiltrados:
            print(letras, end=" ")


comp_expresiones()