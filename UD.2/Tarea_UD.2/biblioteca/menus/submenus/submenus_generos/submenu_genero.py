# biblioteca/menus/submenus/submenus_generos/submenu_genero.py

from biblioteca.crud import crud_genero

def submenu_genero(biblioteca):

    while True:
        print("\n- Tareas de Géneros Literarios -\n")
        print("1. Añadir Género.")
        print("2. Modificar Datos Género.")
        print("3. Eliminar Género.")
        print("0. Menú Principal.")


        opcion = input("\nSelecciona una opción:\n")

        if opcion == "1":
            crud_genero.crear_genero(biblioteca)
        elif opcion == "2":
            crud_genero.actualizar_genero(biblioteca)
        elif opcion == "3":
            crud_genero.eliminar_genero(biblioteca)
        elif opcion == "0":
            return          # Volver SubMenú Tareas de Géneros y Subgéneros Literarios
        else:
            print("\nOpción no válida.\n")
