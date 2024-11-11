# biblioteca/menu/submenus/submenu_autor.py

from biblioteca.crud import crud_autor

def submenu_autor(biblioteca):

    while True:
        print("\n- Tareas de Autores -\n")
        print("1. Mostrar Autores.")
        print("2. Añadir Autor.")
        print("3. Buscar Autor por nombre.")
        print("4. Modificar Datos Autor.")
        print("5. Eliminar Autor.")
        print("0. Menú Tareas de Biblioteca.")


        opcion = input("\nSelecciona una opción:\n")

        if opcion == "1":
            crud_autor.mostrar_autores(biblioteca)
        elif opcion == "2":
            crud_autor.crear_autor(biblioteca)
        elif opcion == "3":
            crud_autor.leer_autor(biblioteca)
        elif opcion == "4":
            crud_autor.actualizar_autor(biblioteca)
        elif opcion == "5":
            crud_autor.eliminar_autor(biblioteca)
        elif opcion == "0":
            return           # Volver SubMenú Tareas de Biblioteca
        else:
            print("\nOpción no válida.\n")