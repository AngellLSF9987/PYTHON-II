from biblioteca.crud.crud_especifico import CRUDEspecifico
from biblioteca.repositorios.repositorio_genero import RepositorioGenero
from biblioteca.utilidades.ruta_datos_json import RUTA_DATOS_BIBLIOTECA

def submenu_especifico(biblioteca):
    """
    Submenú para gestionar tareas de subgéneros literarios específicos.
    """
    ruta_json = RUTA_DATOS_BIBLIOTECA
    repositorio_genero = RepositorioGenero(ruta_json)
    crud_especifico = CRUDEspecifico(ruta_json, repositorio_genero)

    while True:
        print("\n- Tareas de Subgéneros Literarios -\n")
        print("1. Mostrar Subgéneros.")
        print("2. Añadir Subgénero.")
        print("3. Actualizar Subgénero.")
        print("4. Eliminar Subgénero.")
        print("5. Mostrar Subgéneros por Género.")
        print("0. Volver al Menú Principal.")

        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            crud_especifico.mostrar_especificos_crud(biblioteca)
        elif opcion == "2":
            especifico_id = input("Introduce el ID del subgénero: ").strip()
            genero_id = input("Introduce el ID del género asociado: ").strip()
            nombre_especifico = input("Introduce el nombre del subgénero: ").strip()
            tipo = input("Introduce el tipo (opcional): ").strip()

            subgenero = {
                "especifico_id": especifico_id,
                "genero_id": genero_id,
                "nombre_especifico": nombre_especifico,
                "tipo": tipo or "Sin especificar",
            }

            crud_especifico.agregar_especifico(subgenero)
        elif opcion == "3":
            crud_especifico.actualizar_especifico(biblioteca)
        elif opcion == "4":
            crud_especifico.eliminar_especifico(biblioteca)
        elif opcion == "5":
            genero_id = input("Introduce el ID del género: ").strip()
            subgeneros = crud_especifico.obtener_especificos_por_genero(genero_id)

            if subgeneros:
                print("\n=== Subgéneros por Género ===")
                for especifico in subgeneros:
                    print(f"ID: {especifico['especifico_id']} | Subgénero: {especifico['nombre_especifico']} | "
                          f"Tipo: {especifico['tipo']} | Género Asociado: {especifico['nombre_genero']}")
            else:
                print(f"No se encontraron subgéneros específicos para el género con ID {genero_id}.")
        elif opcion == "0":
            print("Regresando al Menú Principal...")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")
