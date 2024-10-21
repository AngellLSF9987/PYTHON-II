print("Hola Mundo")

print(4*5)


nombre = "Loreto"
print(nombre)

"""Cometario de
    varias lineas """

#Comentario de una linea

"""Conversion de un punto flotante o float en un entero o int.
 Se pierde información ya que solo coge la parte entera."""
numero = int(8.945) 
print(numero)

#Conversion de un entero en float
numero1 = float(8)
print(numero1)

#Conversion de un numero en una cadena
cadena = str(9876)
print(cadena)




"""Evaluación de la expresion con variables,
valores y operadores"""
valor = 98
(valor + 56)*63

x=0
y=0

x == x #x es igual a x
x != y #x es distinto de y
x > y  #x es mayor que y
x < y  #x es menor que y
x >= y #x es mayor o igual que y
x <= y #x es menor o igual que y

#Ejemplos
"hola" == "HOLA"  #False
"telefono" != "Telefono"  #True
78 > 48 #True
8 <= 8  #True

"""x + y  #Operador suma                      
x - y  #Operador resta                     
x * y  #Operador de multiplicacion       
x / y  #Operador de division exacta
x // y #Operador de division entera
x ** y #Operador de potencia       
x % y  #Operador de modulo (devuelve el resto de una division)

True and False  #True
True and True   #True
False and False #False

not True  #False
not False #True """


numero = -6 #Se le asigna un valor negativo a numero

""" Se va a comprobar que el numero sea positivo, negativo o 0,
en este caso el numero es negativo"""
if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")


nota = 8.9
if(nota == 10):
    print ("Matricula de honor")
else:
    if( nota <5):
        print("Estas Suspenso")
    elif(nota <= 6.9 and  nota >= 5):
        print("Estas aprobado")
    elif(nota <= 7.9 and nota >= 6):
        print("Tienes un bien")
    elif(nota <= 8.9 and nota >= 7 ):
        print("Tienes un notable")
    else:
        print("Sobresaliente")

#Este bucle imprimirá 3 veces "Buenos dias"
for i in range(3):
    print("Buenas dias")

numero = 9
while(numero > 0):
        print(numero)
        numero = numero -1

valor = 5
"""En este caso cuando la variable valor sea igual 
a 5 se saldrá del bucle y se pasará a la siguente 
instruccion del programa si la hubiera"""

while (valor >0):
    if(valor== 5):
        break
    print(valor)
    valor = valor - 1

valor = 5
"""Cuando el valor sea igual a 3 se saltará este paso
Se devuelvo el control al inicio del bucle
Se seguirá ejecutando el bucle"""
for valor in range(7):
    if(valor==3):
        continue
    print(valor)