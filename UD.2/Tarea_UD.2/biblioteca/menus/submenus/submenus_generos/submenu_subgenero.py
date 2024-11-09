# biblioteca/menus/submenus_generos/submenu_genero.py

from ....crud import crud_subgenero

def submenu_subgenero(biblioteca):

    while True:
        print("\n- Tareas de Géneros Literarios -\n")
        print("1. Añadir Subgénero.")
        print("2. Modificar Datos Subgénero.")
        print("3. Eliminar Subgénero.")
        print("0. Menú Géneros.")


        opcion = input("\nSelecciona una opción:\n")

        if opcion == "1":
            crud_subgenero.crear_subgenero(biblioteca)
        elif opcion == "2":
            crud_subgenero.actualizar_subgenero(biblioteca)
        elif opcion == "3":
            crud_subgenero.eliminar_subgenero(biblioteca)
        elif opcion == "0":
            return          # Volver SubMenú Géneros
        else:
            print("\nOpción no válida.\n")