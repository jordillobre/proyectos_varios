# Crea una función que reciba dos parámetros para crear una cuenta atrás.
#     • El primero, representa el número en el que comienza la cuenta.
#     • El segundo, los segundos que tienen que transcurrir entre cada cuenta.
#     • Sólo se aceptan números enteros positivos.
#     • El programa finaliza al llegar a cero.
#     • Debes imprimir cada número de la cuenta atrás.

# https://github.com/mouredev/retos-programacion-2023/blob/main/Retos/Reto%20%2327%20-%20CUENTA%20ATR%C3%81S%20%5BMedia%5D/ejercicio.md

import time

def cuenta_atras():
    print("Vamos a comenzar la cuenta atrás")

    opcion_valida = True
    while opcion_valida:
        try:
            iteracciones = int(input("¿Número por el que quieres empezar a contar? "))
            opcion_valida = False
        except ValueError:
                print("Error: Debes introducir un número entero válido.")
    
    opcion_valida = True
    while opcion_valida:
        try:
            espera = int(input("¿Cuantos segundos quieres esperar entre interacciones? "))
            opcion_valida = False
        except ValueError:
                print("Error: Debes introducir un número entero válido.")

    for i in reversed(range(0, (iteracciones +1))):
         print(i)
         time.sleep(espera)

cuenta_atras()