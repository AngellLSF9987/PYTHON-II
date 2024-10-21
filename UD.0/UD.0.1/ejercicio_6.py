suma = 0
print("Introduzca tantos números como desee hasta que escriba [no].\n Obtendrá la suma de todos los números que haya introducido.")

while True:
    
    num = int(input("Ingrese un número:\n"))
    suma += num
    
    continuar = input("¿Desea añadir más números? [si] / [no]\n")
    
    if continuar == "no":
        break





