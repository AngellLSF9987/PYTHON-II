num1 = int(input("Ingrese el primero número:\n"))
num2 = int(input("Ingrese el primero número:\n"))
num3 = int(input("Ingrese el primero número:\n"))

def comprobar():
    if num1 < 10 and num2 < 10 and num3 < 10:
        print(f"{num1}, {num2}, {num3} son menores que 10")
    else:
        print(f"{num1}, {num2}, {num3} son mayores que 10")

def main():
    comprobar()

if __name__ == "__main__":
    main()