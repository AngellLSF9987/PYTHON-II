num1 = int(input("Ingrese el primero número:\n"))
num2 = int(input("Ingrese el primero número:\n"))
num3 = int(input("Ingrese el primero número:\n"))

lista_numeros = [num1,num2,num3]

def num_mayor():
    for i in lista_numeros:
        if num1 > num2 and num1 > num3:
            print (f"{num1} es mayor que {num2} y {num3}")
            break
        elif num2 > num1 and num2 > num3:
            print (f"{num2} es mayor que {num1} y {num3}")
            break
        else:
            print (f"{num3} es mayor que {num1} y {num2}")
            break            
def main():
    num_mayor()

if __name__ == "__main__":
    main()