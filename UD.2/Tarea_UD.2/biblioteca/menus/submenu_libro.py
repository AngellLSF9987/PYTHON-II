# Biblioteca/utilidades/submenu_libro.py

from ..crud.crud import crear_libro, leer_libro, actualizar_libro, eliminar_libro

def submenu_libro():

    while True:
        print("- Menú Tareas de Biblioteca -")
        print("1. Añadir libro.")
        print("2. Buscar libro por título.")
        print("3. Modificar Datos Libro.")
        print("4. Eliminar Libro.")
        print("0. Menú Principal.")


        opcion = input("Selecciona una opción:\n")

        if opcion == "1":
            crear_libro()
        elif opcion == "2":
            leer_libro()
        elif opcion == "3":
            actualizar_libro()
        elif opcion == "4":
            eliminar_libro()
        elif opcion == "0":
            return # Volver Menú principal
        else:
            print("Opción no válida.")