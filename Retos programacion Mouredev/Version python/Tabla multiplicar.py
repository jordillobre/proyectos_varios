# Crea un programa que sea capaz de solicitarte un número y se encargue de imprimir su tabla de multiplicar entre el 1 y el 10.
#     • Debe visualizarse qué operación se realiza y su resultado.

# Ej: 1 x 1 = 1
# 	1 x 2 = 2
# 	1 x 3 = 3
# 	 ...

# https://github.com/mouredev/retos-programacion-2023/blob/main/Retos/Reto%20%2340%20-%20TABLA%20DE%20MULTIPLICAR%20%5BF%C3%A1cil%5D/ejercicio.md


def tablaMultiplicar():
    try:
        num = int(input("¿Qué tabla de multiplicar deseas conocer? "))

        for val in range(1, 11):
            print ("{} * {} = {}".format(num, val, (num*val)) )
    except:
        print("Error: Debes de introducir un número entero válido")

tablaMultiplicar()