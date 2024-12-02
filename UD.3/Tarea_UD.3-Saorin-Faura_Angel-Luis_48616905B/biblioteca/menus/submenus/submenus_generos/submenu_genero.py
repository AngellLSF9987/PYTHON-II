# biblioteca/menus/submenus/submenus_generos/submenu_genero.py

from biblioteca.crud.crud_genero import CRUDGenero

def submenu_genero(biblioteca):
    """
    Submenú para gestionar tareas de géneros literarios.
    """
    crud_genero = CRUDGenero(biblioteca.repositorio_genero.ruta_json)

    while True:
        print("\n- Tareas de Géneros Literarios -\n")
        print("1. Mostrar Géneros.")
        print("2. Añadir Género.")
        print("3. Modificar Datos de un Género.")
        print("4. Eliminar Género.")
        print("0. Volver al Menú de Tareas de Géneros y Subgéneros.")

        opcion = input("\nSelecciona una opción: ").strip()

        if opcion == "1":
            # Mostrar todos los géneros literarios
            crud_genero.mostrar_generos()
        
        elif opcion == "2":
            # Añadir un nuevo género literario
            nombre_genero = input("Introduce el nombre del Género Literario: ").strip()
            if nombre_genero:
                nuevo_genero = {"nombre_genero": nombre_genero}
                if crud_genero.agregar_genero(nuevo_genero):
                    print("\n✅ Género Literario añadido correctamente.")
                else:
                    print("\n⚠️ Error al añadir el Género Literario.")
            else:
                print("\n⚠️ El nombre del Género Literario no puede estar vacío.")

        elif opcion == "3":
                # Actualizar Género Literario
                crud_genero.actualizar_genero()
        elif opcion == "4":
            # Eliminar un Género Literario
                crud_genero.eliminar_genero()
        elif opcion == "0":
            # Volver al menú anterior
            print("\nRegresando al menú principal...")
            break

        else:
            print("\n⚠️ Opción no válida. Por favor, intenta de nuevo.")
