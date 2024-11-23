
from biblioteca.crud.crud_especifico import CRUDEspecifico


def submenu_especifico(biblioteca):
    """
    Submenú para gestionar tareas de subgéneros literarios específicos.
    """

    crud_especifico = CRUDEspecifico(biblioteca.repositorio_especifico.ruta_json)

    while True:
        print("\n- Tareas de Subgéneros Literarios -\n")
        print("1. Mostrar Subgéneros.")
        print("2. Añadir Subgénero.")
        print("3. Actualizar Subgénero.")
        print("4. Eliminar Subgénero.")
        print("0. Volver al Menú Principal.")

        opcion = input("Selecciona una opción:\n").strip()

        if opcion == "1":
            crud_especifico.mostrar_especificos()
        elif opcion == "2":

            # Añadir un nuevo Subgénero Literario y Tipo.
            nombre_especifico = input("Introduce el nombre del Subgénero Literario:\n").strip()
            tipo = input("Introduce el nombre del Tipo de Subgénero Literario:\n").strip()
            especifico = {nombre_especifico,tipo}
            if especifico:
                nuevo_especifico = {"nombre_especifico": nombre_especifico, "tipo": tipo}
                if crud_especifico.agregar_especifico(nuevo_especifico):
                    print("\n✅ Subgénero Literario y Tipo añadido correctamente.")
                else:
                    print("\n⚠️ Error al añadir el Subgénero Literario y Tipo.")
            else:
                print("\n⚠️ El nombre del Subgénero Literario y Tipo no puede estar vacío.")

        elif opcion == "3":
            crud_especifico.actualizar_especifico(biblioteca)
        elif opcion == "4":
            crud_especifico.eliminar_especifico(biblioteca)
        elif opcion == "0":
            print("Regresando al Menú Principal...")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")
