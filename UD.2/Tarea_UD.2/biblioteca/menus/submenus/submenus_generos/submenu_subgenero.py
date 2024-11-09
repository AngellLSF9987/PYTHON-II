# biblioteca/menus/submenus/submenus_generos/submenu_genero.py

from biblioteca.crud import crud_subgenero

def submenu_subgenero(biblioteca):

    while True:
        print("\n- Tareas de Subgéneros Literarios -\n")
        print("1. Mostrar Subgéneros.")
        print("2. Añadir Subgénero.")
        print("3. Modificar Datos Subgénero.")
        print("4. Eliminar Subgénero.")
        print("0. Menú Tareas de Géneros y Subgéneros Literarios.")


        opcion = input("\nSelecciona una opción:\n")
        
        if opcion == "1":
            crud_subgenero.leer_subgenero(biblioteca)
        elif opcion == "2":
            crud_subgenero.crear_subgenero(biblioteca)
        elif opcion == "3":
            crud_subgenero.actualizar_subgenero(biblioteca)
        elif opcion == "4":
            crud_subgenero.eliminar_subgenero(biblioteca)
        elif opcion == "0":
            return          # Volver SubMenú Tareas de Géneros y Subgéneros Literarios
        else:
            print("\nOpción no válida.\n")