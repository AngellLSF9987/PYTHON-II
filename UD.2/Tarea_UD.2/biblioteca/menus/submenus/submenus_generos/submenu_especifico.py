# biblioteca/menus/submenus/submenus_generos/submenu_genero.py

from biblioteca.crud import crud_especifico

def submenu_especifico(biblioteca):

    while True:
        print("\n- Tareas de Subgéneros Literarios -\n")
        print("1. Mostrar Subgéneros.")
        print("2. Añadir Subgénero.")
        print("3. Modificar Datos Subgénero.")
        print("4. Eliminar Subgénero.")
        print("0. Menú Tareas de Géneros y Subgéneros Literarios.")


        opcion = input("\nSelecciona una opción:\n")
        
        if opcion == "1":
            crud_especifico.mostrar_especificos(biblioteca)
        elif opcion == "2":
            crud_especifico.crear_especifico(biblioteca)
        elif opcion == "3":
            crud_especifico.actualizar_especifico(biblioteca)
        elif opcion == "4":
            crud_especifico.eliminar_especifico(biblioteca)
        elif opcion == "0":
            return          # Volver SubMenú Tareas de Géneros y Subgéneros Literarios
        else:
            print("\nOpción no válida.\n")