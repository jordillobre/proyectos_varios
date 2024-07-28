import time

def main():
    grados = float(input("Ingrese la temperatura: "))

    tip_grados = ["celsius", "fahrenheit", "kelvin"]

    while True:
        tipo = input("Ingrese en qué tipo de grados está esta temperatura (Celsius, Fahrenheit, Kelvin): ")
        if tipo.lower() in tip_grados:
            break
        else:
            print("No ha introducido un valor válido.")

    if tipo.lower() == "celsius":
        fahrenheit = (grados * 9/5) + 32
        kelvin = grados + 273.15
        print("{} grados Celsius equivalen a {} grados Fahrenheit y {} Kelvin.".format(grados, fahrenheit, kelvin))
    elif tipo.lower() == "fahrenheit":
        celsius = (grados - 32) * 5/9
        kelvin = (grados - 32) * 5/9 + 273.15
        print("{} grados Fahrenheit equivalen a {} grados Celsius y {} Kelvin.".format(grados, celsius, kelvin))
    elif tipo.lower() == "kelvin":
        celsius = grados - 273.15
        fahrenheit = (grados - 273.15) * 9/5 + 32
        print("{} grados Kelvin equivalen a {} grados Celsius y {} grados Fahrenheit.".format(grados, celsius, fahrenheit))
    
    time.sleep(10)

if __name__ == "__main__":
    main()
