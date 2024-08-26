# La última semana de 2021 comenzamos la actividad de retos de programación, con la intención de resolver un ejercicio cada 
# semana para mejorar nuestra lógica... ¡Hemos llegado al EJERCICIO 100! Gracias 🙌

# Crea un programa que calcule los puntos de una palabra.
# Cada letra tiene un valor asignado. Por 	ejemplo, en el abecedario español de 27 letras, la A vale 1 y la Z 27.
# El programa muestra el valor de los puntos de cada palabra introducida.
# El programa finaliza si logras introducir una palabra de 100 puntos
# Puedes usar la terminal para interactuar con el usuario y solicitarle cada palabra.

# https://github.com/mouredev/retos-programacion-2023/blob/main/Retos/Reto%20%2347%20-%20LA%20PALABRA%20DE%20100%20PUNTOS%20%5BF%C3%A1cil%5D/ejercicio.md

import random
import string

def asignar_valores():
    letras = list(string.ascii_lowercase)
    puntuaciones = list(range(1, 27))  # Corrección de tange a range
    random.shuffle(puntuaciones)
    asignacion = {}

    for i, letra in enumerate(letras):
        asignacion[letra] = puntuaciones[i]

    return asignacion

def cien_puntos():
    puntos_letras = asignar_valores()

    print("Vamos a intentar acertar la palabra de 100 puntos. En caso de no querer continuar, escribe una cadena vacía.")

    repetir = True
    
    while repetir:
        pal = input("Escribe la palabra de los 100 puntos: ").lower()
        resultado = 0

        if pal == "":
            repetir = False
        else:    
            for letra in pal:
                if letra in puntos_letras:
                    resultado += puntos_letras[letra]

            if resultado == 100:
                print(f"¡Enhorabuena! La palabra de 100 puntos ha sido '{pal}'.")
            else:
                print(f"La palabra '{pal}' no es la que buscábamos, ya que solo vale {resultado} puntos.")

cien_puntos()