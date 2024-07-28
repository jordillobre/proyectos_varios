import time

def main():
    while True:
        us_name = input("Ingrese tu nombre de usuario (escribe 'salir' para terminar): ")

        if us_name.lower() == "salir":
            print("Cerrando el programa.")
            break
        else:
            user_input = us_name.lower()
            nom = user_input.capitalize()
            long = len(us_name)
            print("Hola {}, tu nombre tiene {} letras.".format(nom, long))
    time.sleep(10)

if __name__ == "__main__":
    main()