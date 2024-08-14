# Escribe un programa que muestre por consola (con un print) los números de 1 a 100 (ambos incluidos y con un salto de línea entre cada impresión), sustituyendo los siguientes:
#     • Múltiplos de 3 por la palabra "fizz".
#     • Múltiplos de 5 por la palabra "buzz".
#     • Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".

# https://github.com/mouredev/retos-programacion-2023/blob/main/Retos/Reto%20%230%20-%20EL%20FAMOSO%20FIZZ%20BUZZ%20%5BF%C3%A1cil%5D/ejercicio.md


def fizbuzz():
    for num in range(1,101):
        if num%3 == 0 :
            if num%5 == 0:
                print("fizzbuzz")
            else:
                print("fizz")
        elif num%5==0:
            print("buzz")
        else:
            print(num)

fizbuzz()