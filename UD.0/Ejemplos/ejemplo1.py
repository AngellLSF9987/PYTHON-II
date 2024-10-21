
num = 12
print(type(num))

num = num.__str__()
print(type(num))

num = float(num)
print(type(num))

num1 = int(input("Introduce un numero: "))

num1 = float(input("Introduce un numero: "))

Casa = 2
casa = 1


if (casa <= 3):
    print("Hola")
elif(casa == 1):
    edad = 7
    if edad < 18 and casa == 1: print("Hola")
elif(casa == 6):
    pass 
elif(casa ==9):
    pass
else:
    print("Buenas")

email = "rosaura.crespo@carm.es"

edad = 18

if edad < 18 and casa == 1: print("Hola")

if edad < 18 or casa == 1: print("Hola")

if not(edad<18): print("Hola")

numero= 8
if(numero%2==0):
    print("par")

numero = 9
for i in range(1,numero,2):
    print(i)
    if (i==3):
        break

x=0
while x <=10:
    print(x)
    x +=1
    # x = x+1
    
while True:
    opcion = input("Introduce una opcion")
    
    if(opcion == 1):
        break
    elif(opcion==2):
        continue
    else:
        continue
    
def suma(a,b=6):
    return a+b
    
sum = suma(3,8)

if __name__=="main":
    suma(4,7)

    







