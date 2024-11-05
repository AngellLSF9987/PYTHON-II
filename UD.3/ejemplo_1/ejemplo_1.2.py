

# Versión 2
with open(r"C:\Users\tarde\Desktop\PYTHON-II\UD.3\ejemplo_1/adios.txt", "r", encoding="utf-8") as adios:
    adios.seek(0)                       # Indica que empezará a leer desde el comienzo del fichero hasta el final.
    contenido = adios.read()

    print(contenido)