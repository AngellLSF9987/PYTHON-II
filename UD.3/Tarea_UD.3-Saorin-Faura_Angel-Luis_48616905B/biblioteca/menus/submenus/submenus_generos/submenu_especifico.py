from biblioteca.crud.crud_especifico import CRUDEspecifico

def submenu_especifico(biblioteca):
    crud_especifico = CRUDEspecifico(biblioteca.repositorio_especifico.ruta_json)

    while True:
        print("\n- Tareas de Subgéneros Literarios -\n")
        print("1. Mostrar Subgéneros.")
        print("2. Añadir Subgénero.")
        print("3. Modificar Datos de Subgénero.")
        print("4. Eliminar Subgénero.")
        print("0. Volver al Menú de Géneros.")

        opcion = input("\nSelecciona una opción: ").strip()

        if opcion == "1":
            crud_especifico.mostrar_especificos_crud(biblioteca)
        elif opcion == "2":
            crud_especifico.crear_especifico(biblioteca)
        elif opcion == "3":
            crud_especifico.actualizar_especifico(biblioteca)
        elif opcion == "4":
            crud_especifico.eliminar_especifico(biblioteca)
        elif opcion == "0":
            break
        else:
            print("⚠️ Opción no válida. Intenta de nuevo.")
