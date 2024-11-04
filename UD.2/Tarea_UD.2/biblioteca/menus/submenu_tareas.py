# biblioteca/utilidades/submenu_tareas.py

from ..menus import submenu_libro
from ..menus import submenu_genero
from ..menus import submenu_autor

def submenu_tareas(biblioteca):
    
    while True:
        print("\n- Tareas de Biblioteca -\n")
        print("1. Tareas de Libros.")
        print("2. Tareas de Géneros Literarios.")
        print("3. Tareas de Autores.")
        print("0. Menú Principal.")
        
        opcion = input("\nSelecciona una opción:\n")
        
        if opcion == "1":
           # LLama al submenu de tareas de libros y le pasa la instancia de Biblioteca
           submenu_libro.submenu_libro(biblioteca)
        elif opcion == "2":
            # LLama al submenu de tareas de géneros literarios y le pasa la instancia de Biblioteca
           submenu_genero.submenu_genero(biblioteca)
        elif opcion == "3":
            # LLama al submenu de tareas de autores y le pasa la instancia de Biblioteca
            submenu_autor.submenu_autor(biblioteca)
        elif opcion == "0":
            return # Volver Menú principal
        else:
            print("\nOpción no válida.\n")
            
            
           
        
        
        
        