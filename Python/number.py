import time
def main():
    while True:
        num = input("Ingrese un numero: ")

        if num.isnumeric():
            print ("Has introducido un numero.")
            if int(num) % 2 == 1:
                print("el numero introducido es impar")
            else:
                print ("El numero introducido es par")
        elif num =="salir":
            print("Cerrando el programa")
            time.sleep(10)
            break
        else:
            print ("El caracter introducido no es un numero.")

if __name__ == "__main__":
    main()