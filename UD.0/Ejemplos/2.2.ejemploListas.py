#Listas

compra = ["huevos","tomates","leche"]
print(compra) #['huevos', 'tomates', 'leche']

#Se introducen entre corchete los datos porque son varios
datos = list(["Andres Rubio",12,True, 6.22]) #['Andres Rubio', 12, True, 6.22]
print(datos)

print(type(datos)) #<class 'list'>

"""Al ser una cadena que es una estructura iterable,
Python los separa automaticamente en elementos individuales
y crea la lista"""
vocales = list("aeiou") 
print(vocales) #['a', 'e', 'i', 'o', 'u']

"""Por el contrario si se declara con numeros enteros
se produce un error, ya que los enteros no son iterables"""
#numeros = list(12345)
#print(numeros)

print(compra)
#['huevos', 'tomates', 'leche']

print(compra[2])
#leche

"""crear sublistas más pequeñas de una más grande. Para ello debemos de usar : entre corchetes, 
indicando a la izquierda el valor de inicio, y a la izquierda el valor final que no está incluido."""
print(compra[1:2]) 
#['tomates']

print(id(compra)) #Se ve la posicion del objeto en memoria
#2079295150336

compra[0] = "Espinacas" #Modificamos datos en la posicion 0
print(id(compra)) #Aunque se ha modificado el id de memoria es el mismo ya que es mutable el objeto 
#2079295150336

print(compra) #Se ha modificado huevos por espinacas
#['Espinacas', 'tomates', 'leche']

print(len(compra))
#3

print(compra *3)
#['Espinacas', 'tomates', 'leche', 'Espinacas', 'tomates', 'leche', 'Espinacas', 'tomates', 'leche']

print(datos + compra)
#['Andres Rubio', 12, True, 6.22, 'Espinacas', 'tomates', 'leche']

coches = ["Mercedes","Audi","BMW","Seat","Opel"] #Creamos la lista

coches.append("Toyota") #Añadimos Toyota a la lista 
print(coches)
#['Mercedes', 'Audi', 'BMW', 'Seat', 'Opel', 'Toyota']

coches.pop() #Se limina el ultimo elemento de la lista (Toyota)
print(coches) 
#['Mercedes', 'Audi', 'BMW', 'Seat', 'Opel']

#Sort Ordena por orden alfabetico y de menor a mayor
coches.sort()
print(coches)
#['Audi', 'BMW', 'Mercedes', 'Opel', 'Seat']

numeros = [1,6,23,88,20,14,7,23, 35]
numeros.sort()
print(numeros)
#[1, 6, 7, 14, 20, 23, 23, 35, 88]

numeros.reverse()
print(numeros)
#[88, 35, 23, 23, 20, 14, 7, 6, 1]

numeros.count(23)
print(numeros)
#2

numeros.remove(23)
print(numeros)
[88, 35, 23, 20, 14, 7, 6, 1]

numeros.extend(range(8))
print(numeros)
#[88, 35, 23, 20, 14, 7, 6, 1, 0, 1, 2, 3, 4, 5, 6, 7]

numeros.insert(4,15)
print(numeros)
#[88, 35, 23, 20, 15, 14, 7, 6, 1, 0, 1, 2, 3, 4, 5, 6, 7]

numeros = [2,5,7,8,15]

for i in numeros:
    print(i + 2)
"""4
7
9
10
17"""

x = [1, 2, 3, ['p', 'q', [5, 6, 7]]]

print(x[3][0])    #p
print(x[3][2][0]) #5
print(x[3][2][2]) #7

print("Iteración lista anidada")
for i in x:
    print(i)
"""
1
2
3
['p', 'q', [5, 6, 7]]
"""

print("Iteración lista anidada")
for i in x[3]:
    print(i)
"""
p
q
[5, 6, 7]
"""


print("Iteración lista anidada")
for i in x [3][2]:
    print(i)
"""
5
6
7
"""

#Crear una lista de letras con la palabra hola
saludo = [letra for letra in "hola"]
print(saludo) #['h', 'o', 'l', 'a']

#Crear una lista de los cuadrados de los pares con rango comprendido entre 1 y 19
numeros_pares =[i*2 for i in range(0,20) if i%2 ==0]
print(numeros_pares) #[0, 4, 8, 12, 16, 20, 24, 28, 32, 36]

