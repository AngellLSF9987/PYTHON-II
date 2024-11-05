

# Versión 2
with open("../../ejemplo_1/adios.txt", "r") as adios:
    adios.seek(0)
    contenido = adios.read()

    print(contenido)