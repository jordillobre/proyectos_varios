import time

def calc_area(base, altura):
    area = base * altura
    return area

def main():
    base = float(input("Ingrese el valor de la base: "))
    altura = float(input("Ingrese el valor de la altura: "))

    area = calc_area(base, altura)

    print("el area del cuadrado es", area)
    time.sleep(10)

if __name__ == "__main__":
    main()