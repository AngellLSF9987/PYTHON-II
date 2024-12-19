
# Versión 1

fichero = open(r"C:\Users\tarde\Desktop\PYTHON-II\UD.3/ejemplo_1/hola.txt", 'r')
fichero.seek(0)        # # Indica que empezará a leer desde el comienzo del fichero hasta el final.

print(fichero.read())
fichero.close()