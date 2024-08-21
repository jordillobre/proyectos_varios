# Crea una función que reciba una expresión matemática (String) y compruebe si es correcta. Retornará true o false.
# Para que una expresión matemática sea correcta debe poseer un número, una operación y otro número separados por espacios.
# Tantos números y operaciones como queramos.
# Números positivos, negativos, enteros o decimales.
# Operaciones soportadas: + - * / % 	

# Ejemplos:
# "5 + 6 / 7 - 4" -> true
# "5 a 6" -> false


# https://github.com/mouredev/retos-programacion-2023/blob/main/Retos/Reto%20%2328%20-%20EXPRESI%C3%93N%20MATEM%C3%81TICA%20%5BMedia%5D/ejercicio.md


def expresion_matematica():
    operadores = "+-*/%"

    expresion = input("Indicame la expresión matematica que quieres revisar")

    elementos = expresion.split(" ")

    es_valida = True

    for caracter in elementos:
        if (caracter in operadores) or caracter.isnumeric():
            continue
        else:
            es_valida = False
            break
    
    print(f"¿La expresión matematica introducida {expresion} es valida? {'Sí' if es_valida else 'No'}")

expresion_matematica()