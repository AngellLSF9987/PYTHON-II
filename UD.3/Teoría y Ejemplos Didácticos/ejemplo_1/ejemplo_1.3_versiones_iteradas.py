# Versión 1
print()
fichero = open(r"C:\Users\tarde\Desktop\PYTHON-II\UD.3/ejemplo_1/mensajes.txt", 'r', encoding="utf-8")
fichero.seek(0)        # # Indica que empezará a leer desde el comienzo del fichero hasta el final.

print(fichero.read(26))
fichero.close()

# Versión 2
with open(r"C:\Users\tarde\Desktop\PYTHON-II\UD.3\ejemplo_1/mensajes.txt", "r", encoding="utf-8") as adios:
    adios.seek(29)                       # Indica que empezará a leer desde el comienzo del fichero hasta el final.
    contenido = adios.read()

    print(contenido)
print()