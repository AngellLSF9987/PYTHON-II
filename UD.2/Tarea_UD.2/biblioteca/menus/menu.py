# biblioteca/menus/menu.py

from biblioteca.crud.crud_libro import leer_libro
from biblioteca.crud.crud_autor import leer_autor
from biblioteca.modelos.biblioteca import Biblioteca
from biblioteca.menus.submenus import submenu_tareas

def menu():
    
    # Inicializa de manera Global la Biblioteca
    biblioteca = Biblioteca()
    
    while True:

        print("\n- Bienvenid@ a Biblioteca AVANZA! -\n")
        print("1. Menú Tareas de Biblioteca.")
        print("2. Buscar libro por Título.")
        print("3. Buscar Autor por Nombre Completo o por Pseudónimo Atribuido.")
        print("4. Mostrar todos los Libros.")
        print("5. Mostrar todos los Autores.")
        print("6. Mostrar todos los Géneros Literarios.")
        print("0. Salir")

        opcion = input("\nElija una de las opciones:\n")

        if opcion == "1":
           # LLama al submenu y le pasa la instancia de Biblioteca
           submenu_tareas.submenu_tareas(biblioteca)
        elif opcion == "2":
            leer_libro(biblioteca)
        elif opcion == "3":
            leer_autor(biblioteca)

        elif opcion == "4":
            libros = biblioteca.mostrar_libros()

            if libros:
                print("\n- Registro Completo de Libros existentes en la Biblioteca -\n")
                for libro in libros:
                    print(libro)
            else:
                print("\nNo existe ningún registro aún en la Biblioteca.\n")
                return
        elif opcion == "5":
            autores = biblioteca.mostrar_autores()

            if autores:
                print("\n- Registro Completo de Autores existentes en la Biblioteca -\n")
                for autor in autores:
                    print(autor)
            else:
                print("\nNo existe ningún registro aún en la Biblioteca.\n")
                return
        elif opcion == "6":
            especificos = biblioteca.mostrar_especificos()

            if especificos:
                print("\n- Registro Completo de Subgéneros existentes en la Biblioteca -\n")
                for especifico in especificos:
                    print(especifico)
            else:
                print("\nNo existe ningún registro aún en la Biblioteca.\n")
                return
        elif opcion == "0":
            print("\nHasta luego!\n")
            break

        else:
            print("\nOJO! Opción no válida.\n")
