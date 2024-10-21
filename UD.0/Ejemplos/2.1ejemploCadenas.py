
#Estas 3 variables son cadenas
nombre = "Alejandro " #Dejamos un espacio al final
apellido1 = "Perez"
apellido2 = "Alvarez"

nombreCompleto = nombre + apellido1 + apellido2

#Al utilizar concatenar las cadenas se unen tal se escriben
#Al no haber espacios los apellidos se concatenan juntos
print(nombreCompleto) 

saludo ="Buenas tardes "
print(saludo * 4)

texto = "Bienvenidos al curso de Python"
texto[:] #Parametros por defecto
"Bienvenidos al curso de Python" #Se muestra la cadena entera

texto[::] #Tambien mostrará la cadena completa
"Bienvenidos al curso de Python"

texto[0] #Primer caracter
"B"

texto[-1] #Ultimo caracter
"n"

print(texto[:6]) #Desde la posicion 0 a la 5
"Bienve"

print(texto[1:8]) #Desde la posicion 1 a la 7
"ienveni" 

print(texto[2::2]) #Desde la posicion 2 hasta el final, saltando de 2 en 2
"evndsa us ePto"

texto[3:1] #Daria error porque no se puede ir de la posicion 3 a la 1

texto[-2::3] #ten en cuenta que el ultimo caracter de la cadena es -1
"o"

"""-10: Indica que empezaremos a contar desde el décimo carácter contando desde el final de la cadena.
-2: Indica que terminaremos justo antes del segundo carácter contando desde el final.
:2: Este número indica el "paso" o incremento que se dará al recorrer la cadena. En este caso, se tomará un carácter sí y otro no"""
texto[-10:-2:2] 
"ePt"

texto1= "Lista de la compra: \n *Leche \n *Azucar \n *Huevos \n *Harina"
print(texto1)

texto2="Esto es \t una tabulación"
print(texto2)

ruta = r"C:\Proyectos\Carpeta\Unidad2\Python"
print(ruta)

texto = "El numero ganador del sorteo es:"
numero = 345982
#print(texto+numero) #Esto producirá un error, porque no son del mismo tipo

print(texto+str(numero))

numero = 345982
print(f'El numero ganador del sorteo es: {numero}')
print(f"El numero es {numero}")

numero = 345982
print("El numero ganador del sorteo es: {}".format(numero))

#Tambien se pueden declarar las variables dentro del .format()
print("Mi hijo tiene {edad} años".format(edad=12)) 

cadena = "HOLA"
print(cadena.lower()) #hola

cadena1 = "hola"
print(cadena1.upper()) #HOLA

cadena2 = "hola caracola"
print(cadena2.title()) #Hola

texto = "El sofa es rojo"
print(texto.count("o")) #3

texto1 = " Ya estamos aquí "
print(texto1.strip()) #Ya estamos aquí

texto2 = "en un lugar de la mancha" 
print(texto2.capitalize()) #En un lugar de la mancha

texto3 = "Tengo una camiseta rosa y unos vaqueros negros"
print(texto3.split("o")) #['Teng', ' una camiseta r', 'sa y un', 's vaquer', 's negr', 's']

print(texto3.replace("a","u")) #Tengo unu cumisetu rosu y unos vuqueros negros

texto = "Acabo de llegar a clase"
print(len(texto)) #23

texto = "El barco es rosa"
for letra in texto:
    print(letra)