# Biblioteca/utilidades/menu.py

from ..crud.crud import leer_libro, inicializar_biblioteca
from ..modelos.biblioteca import Biblioteca
from .submenu_libro import submenu_libro

# Instancia de la Biblioteca

biblioteca = Biblioteca()

def menu():

    # Inicializa la biblioteca con libros por defecto
    inicializar_biblioteca()

    print("- Bienvenid@ a Biblioteca AVANZA! -")
    print("1. Menú Tareas de Biblioteca.")
    print("2. Buscar libro por nombre.")
    print("3. Mostrar libros por autor.")
    print("4. Mostrar todos libros.")
    print("0. Salir")

    opcion = input("Introduce una opción")

    while True:
        if opcion == 1:
           # Redirige al submenú de Tareas CRUD de la Biblioteca
           submenu_libro()
        elif opcion == 2:
            leer_libro()
        elif opcion == 3:
            autor = input("Introduzca el nombre del autor deseado:\n")
            libros = biblioteca.mostrar_libros_por_autor()

            if libros:
                print(f"- Libros de {autor} -")
                for libro in libros:
                    print(libro.mostrar_datos())
            else:
                print(f"No se encontraron registros de {autor}.")
        elif opcion == "4":
            libros = biblioteca.listar_libros()

            if libros:
                print("Registro Completo de Libros existentes en la Biblioteca.")
                for libro in libros:
                    print(libro)
            else:
                print("No existe ningún registro aún en la Biblioteca.")
        elif opcion == "0":
            print("Hasta luego!")
            break
        else:
            print("OJO! Opción no válida.")
