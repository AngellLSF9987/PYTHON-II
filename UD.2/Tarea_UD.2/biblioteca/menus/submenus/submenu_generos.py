# biblioteca/menus/submenus/submenu_generos.py

from biblioteca.menus.submenus.submenus_generos import submenu_genero
from biblioteca.menus.submenus.submenus_generos import submenu_subgenero

def submenu_generos(biblioteca):
    
    while True:
        print("\n- Tareas de Géneros y Subgéneros Literarios -\n")
        print("1. Tareas de Géneros Literarios.")
        print("2. Tareas de Subgéneros Literarios.")
        print("0. Menú Tareas de Biblioteca.")
        
        opcion = input("\nSelecciona una opción:\n")
        
        if opcion == "1":
           # LLama al submenu de tareas de géneros y le pasa la instancia de Biblioteca
           submenu_genero.submenu_genero(biblioteca)
        elif opcion == "2":
            # LLama al submenu de tareas de subgéneros literarios y le pasa la instancia de Biblioteca
           submenu_subgenero.submenu_subgenero(biblioteca)
        elif opcion == "0":
            return # Volver Menú Tareas de Biblioteca
        else:
            print("\nOpción no válida.\n")