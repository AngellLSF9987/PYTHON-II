# biblioteca/menu/submenus/submenu_libro.py

from biblioteca.crud.crud_libro import CRUDLibro

def submenu_libro(biblioteca):
    crud_libro = CRUDLibro(biblioteca.repositorio_libro.ruta_json)
    while True:
        print("\n- Tareas de Libros -\n")
        print("1. Mostrar Libros.")
        print("2. Añadir Libro.")
        print("3. Buscar Libro por Título.")
        print("4. Modificar Datos Libro.")
        print("5. Eliminar Libro.")
        print("0. Menú Tareas de Biblioteca.")


        opcion = input("\nSelecciona una opción:\n")
        
        if opcion == "1":
            crud_libro.mostrar_libros_crud(biblioteca)
        elif opcion == "2":
            crud_libro.crear_libro(biblioteca)
        elif opcion == "3":
            crud_libro.leer_libro(biblioteca)
        elif opcion == "4":
            crud_libro.actualizar_libro(biblioteca)
        elif opcion == "5":
            crud_libro.eliminar_libro(biblioteca)
        elif opcion == "0":
            return            # Volver SubMenú Tareas de Biblioteca
        else:
            print("\nOpción no válida.\n")