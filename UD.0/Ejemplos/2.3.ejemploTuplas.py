#TUPLAS

tupla = (1, 2, 3)
print(tupla) #(1, 2, 3)

tupla = 1, 2, 3
print(type(tupla)) #<class 'tuple'>
print(tupla)       #(1, 2, 3)

tupla = (1, 2, 3)
#tupla[0] = 5 # Error! TypeError

tupla = 1, 2, ('a', 'b'), 3
print(tupla)       #(1, 2, ('a', 'b'), 3)
print(tupla[2][0]) #a

lista = [1, 2, 3]
tupla = tuple(lista)
print(type(tupla)) #<class 'tuple'>
print(tupla)       #(1, 2, 3)

tupla = (1, 2, 3)
for t in tupla:
    print(t) #1, 2, 3

l = (1, 2, 3)
x, y, z = l
print(x, y, z) #1 2 3

l = (7, 7, 7, 3, 5)
print(l.index(5)) #4

l = (7, 7, 7, 3, 5)
#print(l.index(35)) #Error! ValueError

"""El método index() también acepta un segundo parámetro opcional, 
que indica a partir de que índice empezar a buscar el objeto."""
l = (7, 7, 7, 3, 5)
print(l.index(7, 2)) #2

l = (1, 1, 1, 3, 5)
print(l.count(1)) #3

"""Como añadir elementos a una tupla.
Una tupla es inmutable, pero una lista no, por lo tanto, se transformarica la tupla en lista,
se le añadirian los elementos y luego se convierte en tupla otra vez"""

tupla = (1, 2, 3)
lista = list(tupla)
nuevo_elemento = int(input("Ingrese un nuevo elemento: "))
lista.append(nuevo_elemento)
tupla = tuple(lista)
print(tupla)
