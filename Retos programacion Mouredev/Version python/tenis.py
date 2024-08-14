# Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado. El programa 
# recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien gane cada punto del juego.

#     • Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
#     • Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
# 		15 - Love
# 		30 - Love
# 		30 - 15
# 		30 - 30
# 		40 - 30
# 		Deuce
# 		Ventaja P1
# 		Ha ganado el P1
#     • Si quieres, puedes controlar errores en la entrada de datos.
#     • Consulta las reglas del juego si tienes dudas sobre el sistema de puntos. 

# https://github.com/mouredev/retos-programacion-2023/blob/main/Retos/Reto%20%232%20-%20EL%20PARTIDO%20DE%20TENIS%20%5BMedia%5D/ejercicio.md

from random import *
import time  # Necesario para usar sleep

j1_puntos = 0
j2_puntos = 0

j1_juegos = 0
j2_juegos = 0

j1_sets = 0
j2_sets = 0

tipo_normal = True

j1_resultados = []
j2_resultados = []

num_sets = 0

puntos = ["0", "15", "30", "40", "deuce", "Ventaja"]

def gana_punto() -> bool:
    punto_ganado = randint(1, 100)
    return (punto_ganado % 2) == 0

def reiniciar_puntos():
    global j1_puntos, j2_puntos
    j1_puntos = 0
    j2_puntos = 0

def reiniciar_juegos():
    global j1_juegos, j2_juegos
    j1_juegos = 0
    j2_juegos  = 0 

def gana_set():
    global j1_juegos, j2_juegos, j1_resultados, j2_resultados
    j1_resultados.append(j1_juegos)
    j2_resultados.append(j2_juegos)
    reiniciar_juegos()
    reiniciar_puntos()

def tie_break():
    global j1_puntos, j2_puntos, j1_sets, j2_sets
    
    print("¡Tie-break!")
    reiniciar_puntos()  # Reinicia los puntos para el tie-break
    
    while True:
        punto_ganado = gana_punto()
        if punto_ganado:
            j2_puntos += 1
        else:
            j1_puntos += 1
        
        print(f"Tie-break: Jugador 1 {j1_puntos} - Jugador 2 {j2_puntos}")
        
        if j1_puntos >= 7 and (j1_puntos - j2_puntos) >= 2:
            j1_sets += 1
            print(f"El jugador 1 ha ganado el set (tie-break): {j1_sets} sets a {j2_sets}")
            time.sleep(4)
            gana_set()
            break
        elif j2_puntos >= 7 and (j2_puntos - j1_puntos) >= 2:
            j2_sets += 1
            print(f"El jugador 2 ha ganado el set (tie-break): {j1_sets} sets a {j2_sets}")
            time.sleep(4)
            gana_set()
            break

def comprobar_ganador_juego():
    global j1_puntos, j2_puntos, j1_juegos, j2_juegos, tipo_normal, j1_sets, j2_sets, j1_resultados, j2_resultados

    ganador =0
    
    if j1_puntos >= 3 and j2_puntos >= 3:
        if j1_puntos == j2_puntos:
            print("Deuce")
        elif j1_puntos == j2_puntos + 1:
            print("Ventaja Jugador 1")
        elif j2_puntos == j1_puntos + 1:
            print("Ventaja Jugador 2")
        elif j1_puntos >= j2_puntos + 2:
            j1_juegos += 1
            print(f"El jugador 1 ha ganado el juego: {j1_juegos} juegos a {j2_juegos}")
            time.sleep(2)
            reiniciar_puntos()
        elif j2_puntos >= j1_puntos + 2:
            j2_juegos += 1
            print(f"El jugador 2 ha ganado el juego: {j1_juegos} juegos a {j2_juegos}")
            time.sleep(2)
            reiniciar_puntos()
    else:
        if j1_puntos >= 4 and (j1_puntos - j2_puntos) >= 2:
            j1_juegos += 1
            print(f"El jugador 1 ha ganado el juego: {j1_juegos} juegos a {j2_juegos}")
            time.sleep(2)
            reiniciar_puntos()
        elif j2_puntos >= 4 and (j2_puntos - j1_puntos) >= 2:
            j2_juegos += 1
            print(f"El jugador 2 ha ganado el juego: {j1_juegos} juegos a {j2_juegos}")
            time.sleep(2)
            reiniciar_puntos()

    if j1_juegos == 6 and j2_juegos == 6:
        tipo_normal = False  
        tie_break() 
    elif j1_juegos >= 6 and (j1_juegos - j2_juegos) >= 2:
        j1_sets += 1
        print(f"El jugador 1 ha ganado el set: {j1_sets} sets a {j2_sets}")
        time.sleep(4)
        gana_set()
    elif j2_juegos >= 6 and (j2_juegos - j1_juegos) >= 2:
        j2_sets += 1
        print(f"El jugador 2 ha ganado el set: {j1_sets} sets a {j2_sets}")
        time.sleep(4)
        gana_set()

def partido_tenis():

    global puntos, j1_puntos, j2_puntos, j1_sets, j2_sets

    en_juego = True

    ganador = 0

    opcion_valida = True
    while opcion_valida:
        try:
            num_sets = int(input("¿Número de sets que quieres que se jueguen en el partido de tenis? (3 o 5) "))
            if num_sets != 3 and num_sets != 5:
                print("No has elegido una cantidad de sets valida.")
            else:
                opcion_valida = False
        except ValueError:
                print("Error: Debes introducir un número entero válido.")

    while en_juego:
        punto_ganado = gana_punto()
        if tipo_normal:
            if punto_ganado:
                j2_puntos += 1
                ganador = 2
            else:
                j1_puntos += 1
                ganador = 1
            print(f"Jugador {ganador} ha ganado un punto: {puntos[min(j1_puntos, 3)]} - {puntos[min(j2_puntos, 3)]}")
            comprobar_ganador_juego()
        else:
            pass
        
        if j1_sets == num_sets // 2 + 1:
            ganador = 1
            en_juego = False
        elif j2_sets == num_sets // 2 + 1:
            ganador = 2
            en_juego = False
            
    print(f"El jugador {ganador} ha ganado el partido")
    print("el resultado de los sets ha sido:")
    print("para el jugador 1 el resultado de los sets ha sido")
    print(j1_resultados)
    print("para el jugador 2 el resultado de los sets ha sido")
    print(j2_resultados)
    time.sleep(10)
    

partido_tenis()
