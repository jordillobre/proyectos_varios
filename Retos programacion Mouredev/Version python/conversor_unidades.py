#conversión de distancias utilizando recursividad

import time

def calc_incremental(pos1, pos2, cantidad):
    cantidad = cantidad * 10
    pos1 = pos1 + 1
    if pos2 == pos1:
        return cantidad
    else:
        return calc_incremental(pos1, pos2, cantidad)

def calc_decreciente(pos1, pos2, cantidad):
    cantidad = cantidad / 10
    pos1 = pos1 - 1
    if pos2 == pos1:
        return cantidad
    else:
        return calc_decreciente(pos1, pos2, cantidad)

def main():
    unidades = ["kilometros", "hectometros", "decametros", "metros", "decimetros", "centimetros", "milimetros"]

    while True:
        cantidad = input("Introduce la cantidad que quieres convertir: ")
        if cantidad.replace('.', '', 1).isdigit():
            cantidad = float(cantidad)
            break
        else:
            print("Por favor introduzca un valor numérico.")

    while True:
        tipo1 = input("¿En qué unidad se encuentra la cantidad? ")
        if tipo1.lower() in unidades:
            pos1 = unidades.index(tipo1.lower())
            break
        else:
            print("La unidad de medida no es válida, por favor vuelva a intentarlo.")

    while True:
        tipo2 = input("¿A qué tipo de unidad quieres convertirlo? ")
        if tipo2.lower() in unidades:
            pos2 = unidades.index(tipo2.lower())
            if tipo1.lower() == tipo2.lower():
                print("Los tipos introducidos son iguales, por favor ingresa una unidad distinta a la de conversión.")
            else:
                break
        else:
            print("La unidad de medida no es válida, por favor vuelva a intentarlo.")

    if pos1 > pos2:
        resultado = calc_decreciente(pos1, pos2, cantidad)
    else:
        resultado = calc_incremental(pos1, pos2, cantidad)

    print ("{} {} es igual a {} {}".format(cantidad, tipo1, resultado, tipo2))
    time.sleep(10)

if __name__ == "__main__":
    main()