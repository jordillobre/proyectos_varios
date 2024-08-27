# Crea un juego interactivo por terminal en el que tendrás que adivinar el resultado de diferentes operaciones
#  matemáticas aleatorias (suma, resta, multiplicación o división de dos números enteros).
#     • Tendrás 3 segundos para responder correctamente.
#     • El juego finaliza si no se logra responder en ese tiempo.
#     • Al finalizar el juego debes mostrar cuántos cálculos has acertado.
#     • Cada 5 aciertos debes aumentar en uno el posible número de cifras de la operación (cada vez en 
#       un operando):
#         ◦ Preguntas 1 a 5: X (entre 0 y 9) operación Y (entre 0 y 9)
#         ◦ Preguntas 6 a 10: XX (entre 0 y 99) operación Y (entre 0 y 9)
#         ◦ Preguntas 11 a 15: XX operación YY
#         ◦ Preguntas 16 a 20: XXX (entre 0 y 999) operación YY
#         ◦ ...

# https://github.com/mouredev/retos-programacion-2023/blob/main/Retos/Reto%20%2344%20-%20ADIVINANZAS%20MATEM%C3%81TICAS%20%5BMedia%5D/ejercicio.md

import random
import threading

def numero_random(digitos):
    return random.randint(0, 10**digitos - 1)

def respuesta_temporizada(num_X, num_Y, operacion):
    def on_timeout():
        print("\n¡El tiempo ha finalizado! Pulsa enter.")
        global jugando
        jugando = False

    tiempo = threading.Timer(5, on_timeout)
    tiempo.start()

    try:
        respuesta = input(f"¿Cuál es el resultado de la siguiente operación? {num_X} {operacion} {num_Y}: ")
    finally:
        tiempo.cancel()
    return respuesta

def adivinanzas_matematicas():
    global jugando
    jugando = True

    operaciones = ["+", "-", "*", "/"]

    input("Vamos a empezar la partida, cuando estés listo presiona enter.")
    ronda = 1
    digitos_X = 1
    digitos_Y = 1

    while jugando:
        operacion = random.choice(operaciones)
        num_X = numero_random(digitos_X)
        num_Y = numero_random(digitos_Y)

        if operacion == "+":
            respuesta_correcta = num_X + num_Y
        elif operacion == "-":
            respuesta_correcta = num_X - num_Y
        elif operacion == "*":
            respuesta_correcta = num_X * num_Y
        elif operacion == "/":
            while num_Y == 0:  # Evitar la división por cero
                num_Y = numero_random(digitos_Y)
            respuesta_correcta = num_X / num_Y
            respuesta_correcta = round(respuesta_correcta, 1)  # Redondear para simplificar

        respuesta = respuesta_temporizada(num_X, num_Y, operacion)

        if not jugando:
            print("Juego terminado.")
            break

        if respuesta == str(respuesta_correcta):
            print("¡Enhorabuena, has acertado!")
            ronda += 1

            if ronda % 5 == 0:
                if ronda % 2 == 0:
                    digitos_Y += 1
                else:
                    digitos_X += 1
        else:
            print(f"Lo siento, has fallado. La respuesta correcta era {respuesta_correcta}.")
            jugando = False

adivinanzas_matematicas()