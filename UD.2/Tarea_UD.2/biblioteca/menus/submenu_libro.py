# biblioteca/utilidades/submenu_libro.py

from ..crud import crud_libro

def submenu_libro(biblioteca):

    while True:
        print("\n- Tareas de Libros -\n")
        print("1. Añadir libro.")
        print("2. Buscar libro por título.")
        print("3. Modificar Datos Libro.")
        print("4. Eliminar Libro.")
        print("0. Menú Principal.")


        opcion = input("\nSelecciona una opción:\n")

        if opcion == "1":
            crud_libro.crear_libro(biblioteca)
        elif opcion == "2":
            crud_libro.leer_libro(biblioteca)
        elif opcion == "3":
            crud_libro.actualizar_libro(biblioteca)
        elif opcion == "4":
            crud_libro.eliminar_libro(biblioteca)
        elif opcion == "0":
            return            # Volver SubMenú Tareas
        else:
            print("\nOpción no válida.\n")