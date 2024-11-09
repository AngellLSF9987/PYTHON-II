# biblioteca/menus/submenus/submenu_tareas.py

from biblioteca.menus.submenus import submenu_libro
from biblioteca.menus.submenus import submenu_autor
from biblioteca.menus.submenus import submenu_generos

def submenu_tareas(biblioteca):
    
    while True:
        print("\n- Tareas de Biblioteca -\n")
        print("1. Tareas de Libros.")
        print("2. Tareas de Autores.")
        print("3. Tareas de Géneros y Subgéneros Literarios.")
        print("0. Menú Principal.")
        
        opcion = input("\nSelecciona una opción:\n")
        
        if opcion == "1":
           # LLama al submenu de tareas de libros y le pasa la instancia de Biblioteca
           submenu_libro.submenu_libro(biblioteca)
        elif opcion == "2":
            # LLama al submenu de tareas de autores y le pasa la instancia de Biblioteca
           submenu_autor.submenu_autor(biblioteca)
        elif opcion == "3":
            # LLama al submenu de tareas de géneros y subgéneros literarios y le pasa la instancia de Biblioteca
            submenu_generos.submenu_generos(biblioteca)
        elif opcion == "0":
            return # Volver Menú principal
        else:
            print("\nOpción no válida.\n")
            
            
           
        
        
        
        