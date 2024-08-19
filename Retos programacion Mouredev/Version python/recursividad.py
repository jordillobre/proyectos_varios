# EJERCICIO:
# Entiende el concepto de recursividad creando una función recursiva que imprima números del 100 al 0.


# DIFICULTAD EXTRA (opcional):
# Utiliza el concepto de recursividad para:
# Calcular el factorial de un número concreto (la función recibe ese número).
# Calcular el valor de un elemento concreto (según su posición) en la sucesión de Fibonacci (la función recibe la posición).


# https://github.com/mouredev/roadmap-retos-programacion/blob/main/Roadmap/06%20-%20RECURSIVIDAD/ejercicio.md

import os
import platform

def calcular_fibonacci(num : int) -> int:
    if num <3:
        return num -1
    else:
        return (calcular_fibonacci(num -1) + (calcular_fibonacci(num-2)))


def calc_factorial(num : int) -> int:
    if num == 1:
        return 1
    else:
        return num * calc_factorial(num - 1)
    

def limpiar_consola():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def imprime_numeros(num :  int):
    print(num)
    if (num >0):
        imprime_numeros(num -1)

def main():
    opcion_valida = True

    print("Para ejecutar la cuenta atras desde 100 pulse 0")
    print("Para calcular el factorial pulse 1")
    print("Para calcular el valor de un elemento en la sucesioón de Fibonacci pulse 2")

    while opcion_valida:
        try:
            opcion = int(input("¿Qué opción quieres realizar? "))
            if 0 <= opcion < 3:
                opcion_valida = False
            else:
                print("Opción no valida, seleccione una opción del 0 al 2")
        except ValueError:
            print("Error: Debes introducir un número entero válido.")
    if opcion == 0:
        limpiar_consola()
        imprime_numeros(100)
    
    elif opcion == 1:
        opcion_valida = True
        
        try:
            num_factorial = int(input("Introduce el numero del que quieres que se calcule el factorial: "))
            if num_factorial > 0:
                factorial = num_factorial
                opcion_valida = False
            else:
                print("Debes indicar un numero positivo mayor que 0")
        except ValueError:
            print("Error: Debes introducir un número entero válido.")
        
        limpiar_consola()
        print(calc_factorial(factorial))
    
    elif opcion == 2:
        opcion_valida = True
        try:
            num_fibonacci = int(input("Introduce la posición para calcular el resultado de este dentro de la sucesioón de Fibonacci: "))
            if num_fibonacci > 0:
                fibonacci = num_fibonacci
                opcion_valida = False
            else:
                print("Debes indicar una posición valida, es decir un numero mayor que 1")
        except ValueError:
            print("Error: Debes introducir un número entero válido.")
        limpiar_consola()
        print(calcular_fibonacci(fibonacci))

if __name__ == "__main__":
    main()