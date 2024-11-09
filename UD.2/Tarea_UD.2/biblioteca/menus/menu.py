# biblioteca/menus/menu.py

from ..crud.crud_libro import leer_libro
from ..modelos.biblioteca import Biblioteca
from menus.submenus import submenu_tareas

def menu():
    
    # Inicializa de manera Global la Biblioteca
    biblioteca = Biblioteca()
    
    while True:

        print("\n- Bienvenid@ a Biblioteca AVANZA! -\n")
        print("1. Menú Tareas de Biblioteca.")
        print("2. Buscar libro por nombre.")
        print("3. Mostrar libros por autor.")
        print("4. Mostrar todos libros.")
        print("0. Salir")

        opcion = input("\nElija una de las opciones:\n")

        if opcion == "1":
           # LLama al submenu y le pasa la instancia de Biblioteca
           submenu_tareas.submenu_tareas(biblioteca)
        elif opcion == "2":
            leer_libro(biblioteca)
        elif opcion == "3":
            autor = input("\nIntroduzca el nombre del autor deseado:\n")
            libros = biblioteca.mostrar_libros_por_autor(autor)

            if libros:
                print(f"\n- Libros de {autor} -\n")
                for libro in libros:
                    print(libro.mostrar_datos())
            else:
                print(f"\nNo se encontraron registros de {autor}.\n")

        elif opcion == "4":
            libros = biblioteca.mostrar_libros()

            if libros:
                print("\n- Registro Completo de Libros existentes en la Biblioteca -\n")
                for libro in libros:
                    print(libro)
            else:
                print("\nNo existe ningún registro aún en la Biblioteca.\n")
                return
        elif opcion == "0":
            print("\nHasta luego!\n")
            break

        else:
            print("\nOJO! Opción no válida.\n")
