# biblioteca/menus/menu.py

#from biblioteca.crud.crud_libro import leer_libro
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
        print("7. Mostrar todos los Géneros y Subgéneros Literarios.")
        print("0. Salir")

        opcion = input("\nElija una de las opciones:\n")

        if opcion == "1":
           # LLama al submenu y le pasa la instancia de Biblioteca
           submenu_tareas.submenu_tareas(biblioteca)
        
        # elif opcion == "2":
        #     #leer_libro(biblioteca)
        
        elif opcion == "3":
            
            datos_libros = biblioteca.obtener_datos_seccion("libros")
            biblioteca.repositorio_libro.cargar_libros(datos_libros)
            
            print("\n- Registro Completo de Libros existentes en la Biblioteca -\n")
            print(biblioteca.repositorio_libro.mostrar_libros())

        elif opcion == "4":

            datos_libros = biblioteca.obtener_datos_seccion("libros")
            biblioteca.repositorio_libro.cargar_libros(datos_libros)
            
            print("\n- Registro Completo de Libros existentes en la Biblioteca -\n")
            print(biblioteca.repositorio_libro.mostrar_libros())

        elif opcion == "5":

            datos_autores = biblioteca.obtener_datos_seccion("autores")
            biblioteca.repositorio_autor.cargar_autores(datos_autores)
            
            print("\n- Registro Completo de Autores existentes en la Biblioteca -\n")
            print(biblioteca.repositorio_autor.mostrar_autores())
            
        elif opcion == "6":

            datos_generos = biblioteca.obtener_datos_seccion("generos")
            biblioteca.repositorio_genero.cargar_generos(datos_generos)
            
            print("\n- Registro Completo de Géneros Literarios existentes en la Biblioteca -\n")
            print(biblioteca.repositorio_genero.mostrar_generos())

        elif opcion == "7":

            datos_especificos = biblioteca.obtener_datos_seccion("especificos")
            biblioteca.repositorio_especifico.cargar_especificos(datos_especificos)

            print("\n- Registro Completo de Géneros y Subgéneros Literarios Específicos existentes en la Biblioteca -\n")
            print(biblioteca.repositorio_especifico.mostrar_especificos())

        elif opcion == "0":
            print("\nHasta luego!\n")
            break

        else:
            print("\nOJO! Opción no válida.\n")
