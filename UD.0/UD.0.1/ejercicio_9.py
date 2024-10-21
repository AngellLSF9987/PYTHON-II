contraseña = input("Introduce tu contraseña: \n")

while True:

    if 10 >= len(contraseña) and len(contraseña) <= 20:
        print("La contraseña no es válida. Debe tener entre 10 y 20 caracteres.")
        break
    else:
        print("La contraseña es válida.")
        break
        