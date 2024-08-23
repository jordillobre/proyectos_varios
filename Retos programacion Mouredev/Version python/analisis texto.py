# Crea un programa que analice texto y obtenga:
# · Número total de palabras.
# · Longitud media de las palabras.
# · Número de oraciones del texto (cada vez que aparecen un punto).
# · Encuentre la palabra más larga.

# Todo esto utilizando un único bucle.

# https://github.com/mouredev/retos-programacion-2023/blob/main/Retos/Reto%20%2319%20-%20AN%C3%81LISIS%20DE%20TEXTO%20%5BMedia%5D/ejercicio.md

import string

def analisis_texto():
    texto = input("Introduce el texto que quieres que analice: ").strip()

    if not texto:
        print("El texto está vacío. Por favor, introduce un texto válido.")
        return

    palabras = texto.split()

    longitud_total = 0
    palabra_maxima = []
    oraciones = 0

    for palabra in palabras:
        palabra_limpia = palabra.rstrip(string.punctuation)

        longitud_total += len(palabra_limpia)

        if len(palabra_maxima) == 0 or len(palabra_limpia) == len(palabra_maxima[0]):
            palabra_maxima.append(palabra_limpia)
        elif len(palabra_limpia) > len(palabra_maxima[0]):
            palabra_maxima = [palabra_limpia]

        if palabra.endswith('.'):
            oraciones += 1

    long_media = longitud_total / len(palabras) if len(palabras) > 0 else 0

    if not texto.endswith('.') and texto:
        oraciones += 1

    print(f"El texto tiene un total de {len(palabras)} palabras.")
    print(f"La longitud media de las palabras es de {long_media:.2f} caracteres.")
    print(f"La(s) palabra(s) más larga(s) es/son: {', '.join(palabra_maxima)} con un total de {len(palabra_maxima[0])} caracteres.")
    print(f"El texto introducido tiene un total de {oraciones} oraciones.")

analisis_texto()