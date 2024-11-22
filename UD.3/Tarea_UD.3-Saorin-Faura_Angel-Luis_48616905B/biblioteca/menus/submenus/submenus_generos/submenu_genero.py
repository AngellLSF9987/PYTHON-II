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
            generos = crud_genero.mostrar_generos()
            if generos:
                print("\n=== Lista de Géneros Literarios ===")
                for genero in generos:
                    print(f"ID: {genero['genero_id']} | Género Literario: {genero['nombre_genero']}")
            else:
                print("\n⚠️ No hay géneros literarios registrados.")

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
            # Modificar los datos de un género existente
            try:
                genero_id = int(input("Introduce el ID del Género Literario a modificar: ").strip())
                genero = crud_genero.buscar_genero_por_id(genero_id)
                if genero:
                    print("\n=== Datos Actuales ===")
                    print(f"ID: {genero['genero_id']} | Nombre: {genero['nombre_genero']}")
                    nuevo_nombre = input(f"Introduce el nuevo nombre (o deja vacío para mantener '{genero['nombre_genero']}'): ").strip()
                    if nuevo_nombre:
                        genero_actualizado = {"nombre_genero": nuevo_nombre}
                        if crud_genero.actualizar_genero(genero_id, genero_actualizado):
                            print("\n✅ Género Literario actualizado correctamente.")
                        else:
                            print("\n⚠️ Error al actualizar el Género Literario.")
                    else:
                        print("\n⚠️ No se realizaron cambios.")
                else:
                    print("\n⚠️ Género Literario no encontrado.")
            except ValueError:
                print("\n⚠️ El ID debe ser un número entero.")

        elif opcion == "4":
            # Eliminar un género literario
            try:
                genero_id = int(input("Introduce el ID del Género Literario a eliminar: ").strip())
                genero = crud_genero.buscar_genero_por_id(genero_id)
                if genero:
                    confirmacion = input(f"¿Estás seguro de eliminar el género '{genero['nombre_genero']}'? (s/n): ").strip().lower()
                    if confirmacion == 's':
                        if crud_genero.eliminar_genero(genero_id):
                            print("\n✅ Género Literario eliminado correctamente.")
                        else:
                            print("\n⚠️ Error al eliminar el Género Literario.")
                    else:
                        print("\nOperación cancelada.")
                else:
                    print("\n⚠️ Género Literario no encontrado.")
            except ValueError:
                print("\n⚠️ El ID debe ser un número entero.")

        elif opcion == "0":
            # Volver al menú anterior
            print("\nRegresando al menú principal...")
            break

        else:
            print("\n⚠️ Opción no válida. Por favor, intenta de nuevo.")
