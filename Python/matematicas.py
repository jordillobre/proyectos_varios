import time
def main():
    num1 = input("Ingrese el primer valor: ")
    num2 = input("Ingrese el segundo valor: ")

    if (num1.isnumeric() and num2.isnumeric()):
        num1 = int(num1)
        num2 = int(num2)
        suma = num1 + num2
        resta = num1 - num2
        multiplicacion = num1 * num2
        division = num1 / num2
        resto = num1 % num2
        potencia = num1 ** num2
        mayor = num1 > num2
        igual = num1 == num2

        if igual:
            print("Los dos numeros introducidos son iguales")
        else:
            print("Los dos numeros introducidos no son iguales")
            if mayor:
                print("El {} es mayor que {}".format(num1, num2))
            else:
                print("El {} es mayor que {}".format(num2, num1))
        print("El resultado de {} + {} es igual a {}".format(num1, num2, suma))
        print("El resultado de {} - {} es igual a {}".format(num1, num2, resta))
        print("El resultado de {} * {} es igual a {}".format(num1, num2, multiplicacion))
        print("El resultado de {} / {} es igual a {}".format(num1, num2, division))
        print("El resto de la división {} / {} es igual a {}".format(num1, num2, resto))
        print("El resultado de la potencia de {} elevado a {} es igual a {}".format(num1, num2, potencia))
        time.sleep(10)
        
    else:
        print("No has introducido dos numeros")
        time.sleep(10)

if __name__ == "__main__":
    main()