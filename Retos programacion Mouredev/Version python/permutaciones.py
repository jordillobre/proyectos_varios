# Crea un programa que sea capaz de generar e imprimir todas las  permutaciones disponibles formadas por las letras de una palabra.
#     • Las palabras generadas no tienen por qué existir.
#     • Deben usarse todas las letras en cada permutación.
#     • Ejemplo: sol, slo, ols, osl, los, lso 

# https://github.com/mouredev/retos-programacion-2023/blob/main/Retos/Reto%20%2336%20-%20PERMUTACIONES%20%5BMedia%5D/ejercicio.md

def per(palabra : str) -> list:
    if len(palabra) <=1:
        return [palabra]
    
    resultado = []

    for pos in range(len (palabra)):
        letra_actual = palabra[pos]
        resto_palabra= palabra[:pos] + palabra [pos+1:]

        for opciones in per(resto_palabra):
            resultado.append(letra_actual + opciones)

    return resultado  

def permutaciones():
    permuta = []
    pal = input("¿De que palabra quieres ver las permutaciones?")
    permuta = per(pal)
    
    for respuesta in permuta:
        print(respuesta)

permutaciones()