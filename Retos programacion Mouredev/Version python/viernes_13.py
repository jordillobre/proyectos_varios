# Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
# · La función recibirá el mes y el año y retornará verdadero o falso.

# https://github.com/mouredev/retos-programacion-2023/blob/main/Retos/Reto%20%2312%20-%20VIERNES%2013%20%5BF%C3%A1cil%5D/ejercicio.md

import calendar
import time

meses = ["Enero", "Febrero", "Marzo", 
         "Abril", "Mayo", "Junio",
         "Julio", "Agosto", "Septiembre", 
         "Octubre", "Noviembre", "Diciembre"]

def comprobar_viernes(mes: int, anyo : int) -> bool:
    return calendar.weekday(anyo, mes, 13) == 4

def main():
    repetir = True

    while repetir:
        try:
            mes = int(input("Indique el numero del més que quieres comprobar "))
            if 1 < mes < 13:
                repetir = False
            else:
                print("Opción no válida. Por favor, elige un número de més valido.(De 1 a 12)")
        except ValueError:
            print("Error: Debes introducir un número entero válido.")

    repetir = True

    while repetir:
        try:
            anyo = int(input("Indique el año que quieres comprobar: "))
            repetir = False
        except ValueError:
            print("Error: Debes introducir un número entero válido.")
    es_viernes = comprobar_viernes(mes, anyo)
    print(f"¿El mes de {meses[mes - 1]} del año {anyo} tiene un viernes 13? {es_viernes}")
    time.sleep(5)

if __name__ == "__main__":
    main()