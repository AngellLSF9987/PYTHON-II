# biblioteca/menus/submenus/submenus_generos/submenu_genero.py

from biblioteca.crud.crud_genero import CRUDGenero

def submenu_genero(biblioteca):
    crud_genero = CRUDGenero(biblioteca.repositorio_genero.ruta_json)
    
    while True:
        print("\n- Tareas de Géneros Literarios -\n")
        print("1. Mostrar Géneros.")
        print("2. Añadir Género.")
        print("3. Modificar Datos Género.")
        print("4. Eliminar Género.")
        print("0. Menú Tareas de Géneros y Subgéneros Literarios.")


        opcion = input("\nSelecciona una opción:\n")
        if opcion == "1":
            generos = crud_genero.mostrar_generos()
            if generos:
                    print("\n=== Lista de Géneros Literarios ===")
                    for genero in generos:
                        nombre_genero = f"{genero['nombre_genero']}".strip()
                        print(
                            f"ID: {genero['genero_id']} | Género Literario: {nombre_genero} |")
            else:
                print("\n⚠️ No hay géneros literarios registrados.")
        elif opcion == "2":
            nuevo_genero = {
                "nombre_genero": input("Género Literario: ").strip()
            }
            if crud_genero.agregar_genero(nuevo_genero):
                print("\n✅ Género Literario añadido correctamente.")
            else:
                print("\n⚠️ No se pudo añadir al Género Literario. Revisa los datos e inténtalo de nuevo.")
                
        elif opcion == "3":
            criterio = input("Introduce el Género Literario que desea modificar: \n")
            genero = crud_genero.actualizar_genero(criterio)
            if genero:
                print("\n=== Datos Actuales ===")
                print(genero)
                print("\nIntroduce los nuevos datos. Deja vacío para mantener los actuales.")
                actualizado = {
                    "nombre_genero": input(f"Nombre del Género Literario [{genero['nombre_genero']}]: ").strip() or genero['nombre_genero']
                }
                if crud_genero.actualizar_genero(genero['genero_id'], actualizado):
                    print("\n✅ Género Literario actualizado correctamente.")
                else:
                    print("\n⚠️ No se pudo actualizar el Género Literario.")
            else:
                print("\n⚠️ Género Literario no encontrado.")
                
        elif opcion == "4":
            criterio = input("Introduce el Género Literario a eliminar: ").strip()
            genero = crud_genero.buscar_genero_por_nombre_genero(criterio)
            if genero:
                confirmacion = input(f"¿Estás seguro de eliminar el Género Literario {genero['nombre_genero']}? (s/n): ").strip().lower()
                if confirmacion == 's':
                    if crud_genero.eliminar_genero(genero['genero_id']):
                        print("\n✅ Género Literario eliminado correctamente.")
                    else:
                        print("\n⚠️ No se pudo eliminar el Género Literario.")
            else:
                print("\n⚠️ Género Literario no encontrado.")
                
        elif opcion == "0":
            return          # Volver SubMenú Tareas de Géneros y Subgéneros Literarios
        else:
            print("\nOpción no válida.\n")
