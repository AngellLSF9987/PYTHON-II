#Ejercicios Repaso
#Ejercicio 1
num1=int(input("Ingrese primer valor:"))
num2=int(input("Ingrese segundo valor:"))
num3=int(input("Ingrese tercer valor:"))
if num1<10 and num2<10 and num3<10:
    print("Todos los números son menores a diez")

#Ejercicio 2
if num1<10 or num2<10 or num3<10:
    print("Alguno de los números es menor a diez")

#Ejercicio 3

"""Se cargan por teclado tres números distintos. Mostrar por pantalla el mayor de ellos."""
num1=int(input("Ingrese primer valor:"))
num2=int(input("Ingrese segunda valor:"))
num3=int(input("Ingrese tercer valor:"))
if num1>num2:
    if num1>num3:
        print(num1)
    else:
        print(num3)
else:
    if num2>num3:
        print(num2)
    else:
        print(num3)

#Ejercicio 4
"""Escribir un programa que pida ingresar la coordenada de un punto en el plano, es decir dos valores enteros x e y,
Decir de que cuadrante son o si son eje de coordenadas"""

#Version 1
x=int(input("Ingrese coordenada x:"))
y=int(input("Ingrese coordenada y:"))
if x==0 or y==0:
    print("No son valores correctos")
elif x>0 and y>0:
    print("Se encuentra en el primer cuadrante")
else:
    if x<0 and y>0:
        print("Se encuentra en el segundo cuadrante")
    else:
        if x<0 and y<0:
            print("Se encuentra en el tercer cuadrante")
        else:
            print("Se encuentra en el cuarto cuadrante")

#Version 2
x=int(input("Ingrese coordenada x:"))
y=int(input("Ingrese coordenada y:"))
if x>0 and y>0:
    print("Se encuentra en el primer cuadrante")
elif x<0 and y>0:
    print("Se encuentra en el segundo cuadrante")
elif x<0 and y<0:
    print("Se encuentra en el tercer cuadrante")
elif x<0 and y<0:
    print("Se encuentra en el cuarto cuadrante")
else:
    print("No has introducido valores correctos")

#Ejercicio 5
#Imprimir los numeros de 1 al 100 con while 
x=1
while x<=100:
    if(x==100):
        print(x)
        break
    else:
        print(x, end=", ")
        x=x+1

for i in range(1,101):
    if(i==100):
        print(i)
    else:
        print(i, end=", ")

##Ejercicio 6

"""Realizar la carga de enteros por teclado. Preguntar después que ingresa el valor si desea cargar otro valor debiendo el operador ingresar la cadena 'si' o 'no' por teclado.
Mostrar la suma de los valores ingresados."""
opcion="si"
suma=0
while opcion=="si":
    valor=int(input("Ingrese un valor:"))
    suma=suma+valor
    opcion=input("Desea cargar otro numero (si/no):")
print("La suma de valores ingresados es")
print(suma)

##Ejercicio 7. Gestion de un banco
saldo = 1000  # Saldo inicial
while True:
    print("\nBienvenido al cajero automático")
    print("1. Consultar saldo")
    print("2. Retirar dinero")
    print("3. Ingresar dinero")
    print("4. Salir")
    
    opcion = int(input("Ingrese una opción: "))

    if opcion == 1:
        print("Su saldo actual es:", saldo)
    elif opcion == 2:
        cantidad = int(input("Ingrese cantidad a retirar: "))
        if cantidad > saldo:
            print("Fondos insuficientes.")
        else:
            saldo -= cantidad
            print("Se ha ingresado:", cantidad)
            print("Su nuevo saldo es:", saldo)
    elif opcion == 3:
        saldo += cantidad
        print("Se ha retirado:", cantidad)
        print("Su nuevo saldo es:", saldo)
        
    elif opcion == 4:
        print("¡Gracias por usar el cajero automático!")
        break
    else:
        print("Opción inválida. Intente nuevamente.")


"""Escribir un programa que solicite por teclado 10 notas de alumnos y
 nos informe cuántos suspensos hay y cuantos con nota mayor a 7"""
#Ejercicio 8
notables=0
suspensos=0
for f in range(10):
    nota=int(input("Ingrese la nota:"))
    if nota>=7:
        notables=notables+1
    elif nota < 5:
        suspensos = suspensos+1
    else:
        continue
print("Cantidad de notables")
print(notables)
print("Cantidad de suspensos")
print(suspensos)

#Ejercicio 9
contra=input("Ingrese una contraseña que tenga entre 10 y 20 caracteres:")
if len(contra)>=10 and len(contra)<=20:
    print("Largo correcto")
else:
    print("Largo incorrecto")