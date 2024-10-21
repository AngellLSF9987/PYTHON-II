#Ejemplo 1 - Encontrando la primera ocurrencia de una subcadena
texto = "El perro marrón salta sobre la valla"
indice = texto.find("marrón")
print(indice)  # Output: 9 (el índice donde comienza la palabra "marrón")

#Ejemplo 2 - Buscando una subcadena que no existe
texto = "Hola mundo"
indice = texto.find("Python")
print(indice)  # Output: -1 (la subcadena no se encontró)

#Ejemplo 3 - Especificando un rango de búsqueda
texto = "El perro marrón salta sobre la valla"
indice = texto.find("la", 10)  # Buscar "la" a partir del índice 10
print(indice)  # Output: 28 (encuentra la segunda "la")

#Ejemplo 4 - Uso de find() para validar datos
email = "micorreo@ejemplo.com"
arroba = email.find("@")
if arroba != -1:
    print("El correo electrónico es válido.")
else:
    print("El correo electrónico no es válido.")

#Ejemplo 5 - Combinando find() con slicing para extraer subcadenas
texto = "Hola, mundo. Esto es un ejemplo."
indice_coma = texto.find(",")
saludo = texto[:indice_coma]
print(saludo)  # Output: Hola

