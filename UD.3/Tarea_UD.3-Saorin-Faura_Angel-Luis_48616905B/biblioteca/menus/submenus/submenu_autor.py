# biblioteca/menu/submenus/submenu_autor.py

from biblioteca.crud.crud_autor import CRUDAutor
from biblioteca.utilidades.ruta_datos_json import RUTA_DATOS_BIBLIOTECA

def submenu_autor(biblioteca):
    # Suponiendo que 'biblioteca' tiene un atributo que es una instancia de CRUDAutor
    crud_autor = CRUDAutor(RUTA_DATOS_BIBLIOTECA)  # Crear instancia de CRUDAutor

    while True:
        print("\n- Tareas de Autores -\n")
        print("1. Mostrar Autores.")
        print("2. Añadir Autor.")
        print("3. Buscar Autor por Nombre Completo o por Pseudónimo Atribuido.")
        print("4. Modificar Datos Autor.")
        print("5. Eliminar Autor.")
        print("0. Menú Tareas de Biblioteca.")

        opcion = input("\nSelecciona una opción:\n")

        if opcion == "1":
            crud_autor.mostrar_autores(biblioteca)
        elif opcion == "2":
            crud_autor.agregar_autor(biblioteca)
        elif opcion == "3":
            crud_autor.buscar_autor_por_nombre_o_pseudonimo(biblioteca)
        elif opcion == "4":
            crud_autor.actualizar_autor(biblioteca)
        elif opcion == "5":
            crud_autor.eliminar_autor(biblioteca)
        elif opcion == "0":
            return           # Volver SubMenú Tareas de Biblioteca
        else:
            print("\nOpción no válida.\n")
