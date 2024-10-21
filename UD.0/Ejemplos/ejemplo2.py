#CADENAS

nombre = "Loreto"

poblacion = "Murcia"

print(f"Soy {nombre} y vivo en {poblacion}")

print("Soy {} y vivo en {}".format(nombre,poblacion))

print("Soy",nombre,"y vivo en",poblacion)

texto = "En un lugar de Murcia."

texto1 =  texto.upper()
texto = texto.lower()
texto = texto.strip()
texto = texto.capitalize()
fragmentos = texto.split(" ")
texto = "".join("Y se vive muy bien")

email = "rosaura.crepo@carm.es"

valido = email.find("@carm.es")

num_o = texto.count("a")

texto = texto.replace("Murcia","Zarandona")

subtexto = texto[2:8]

texto= texto[::-1]

long = len(texto)


#LISTAS

lista = [1,3,5,"hola","agua"]

primer = lista[0]
ultimo = lista[-1]

lista[2]= "mundo"

#Añadir elementos a la lista. Ultima posicion
lista.append("raton")

#Añadir elementos en posicion deseada. (Posicion,Valor)
lista.insert(3,8)

#Borrar elemento
lista.remove(8)

#Borra elemento por el indice
lista.pop(2)

#Borrar todos los elementos 
lista.clear()

lista1 = [8,2,4,1,8,6,2,9]

lista1.sort(reverse=True)
lista1.sort()
lista1.reverse()

sublista = lista1[1:4]


for elemento in lista1:
    print(elemento)

#Listas anidadas
matriz = [[1,2,3],[4,5,6],[7,["asdasdasd",2],9]]

#Listas de comprension
lista1 = [8,2,4,1,8,6,2,9]
cuadrados = [x**2 for x in lista1]

cuadrados1 = []
for x in range(5):
    cuadrados1.append(x**2)
    
for indice, elemento in enumerate(cuadrados):
    print(indice,elemento)

#TUPLAS

tupla = (1,2,4,5,63,4,9)

tupla[2] 

lista_tupla = list(tupla)

lista_tupla[2]= 9

tupla1 = tuple(lista_tupla)

a,b,c = (1,2,3)

print(a,b,c)

def dividir (dividendo,divisor):
    cociente = dividendo // divisor
    resto = dividendo % divisor
    return (cociente,resto)

c,r = dividir(10,4)
print(c,r)

#DICCIONARIOS

diccionario = {"nombre":"Loreto","edad":32}

print(diccionario["nombre"])

