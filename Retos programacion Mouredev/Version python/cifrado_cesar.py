# Crea un programa que realize el cifrado César de un texto y lo imprima.
# También debe ser capaz de descifrarlo cuando así se lo indiquemos.

# Te recomiendo que busques información para conocer en profundidad cómo  realizar el cifrado. Esto también forma parte del reto.

# https://github.com/mouredev/retos-programacion-2023/blob/main/Retos/Reto%20%2324%20-%20CIFRADO%20C%C3%89SAR%20%5BF%C3%A1cil%5D/ejercicio.md


def cifrado():
    abecedario = "abcdefghijklmnopqrstuvwxyz"
    valor_correcto = True
    resultado = ""

    frase = input("Dime la frase que quieres cifrar o descifrar: ")

    print("Para desplazar las letras hacia la derecha escribe 1")
    print("Para desplazar las letras hacia la izquierda escribe 2")
    while valor_correcto:
        try:
            sentido = int(input("¿Qué opción quieres realizar? "))
            if sentido == 1 or sentido == 2:
                valor_correcto = False
            else:
                print("Opción no valida, por favor escribe 1 o 2")
        except ValueError:
            print("Error: Debes introducir un número entero válido.")

    valor_correcto = True

    while valor_correcto:
        try:
            desplazamiento = int(input("¿Cuantos espacios quieres que se desplacen tu letras? "))
            valor_correcto = False
        except ValueError:
            print("Error: Debes introducir un número entero válido.")


    frase = frase.lower()

    for letra in frase:
        if letra in abecedario:
            pos_letra = abecedario.index(letra)
            if sentido == 2:
                posicion_cesar = (pos_letra - desplazamiento) %26
            elif sentido == 1:
                posicion_cesar = (pos_letra + desplazamiento) %26
            resultado = resultado + abecedario[posicion_cesar]
        else:
            resultado = resultado + letra

    print(f"La frase {frase}")
    print("Mediante la codificación César marcada seria:")
    print(resultado)


cifrado()