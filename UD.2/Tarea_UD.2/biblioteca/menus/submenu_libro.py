# Biblioteca/utilidades/submenu_libro.py

from ..crud import crud

def submenu_libro(biblioteca):

    while True:
        print("\n- Tareas de Biblioteca -\n")
        print("1. Añadir libro.")
        print("2. Buscar libro por título.")
        print("3. Modificar Datos Libro.")
        print("4. Eliminar Libro.")
        print("0. Menú Principal.")


        opcion = input("\nSelecciona una opción:\n")

        if opcion == "1":
            crud.crear_libro(biblioteca)
        elif opcion == "2":
            crud.leer_libro(biblioteca)
        elif opcion == "3":
            crud.actualizar_libro(biblioteca)
        elif opcion == "4":
            crud.eliminar_libro(biblioteca)
        elif opcion == "0":
            return # Volver Menú principal
        else:
            print("\nOpción no válida.\n")