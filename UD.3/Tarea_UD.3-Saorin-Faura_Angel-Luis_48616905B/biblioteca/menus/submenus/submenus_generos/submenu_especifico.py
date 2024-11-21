from biblioteca.crud.crud_especifico import CRUDEspecifico
from biblioteca.repositorios.repositorio_genero import RepositorioGenero
from biblioteca.utilidades.ruta_datos_json import RUTA_DATOS_BIBLIOTECA

def submenu_especifico(biblioteca):
    
    ruta_json = RUTA_DATOS_BIBLIOTECA
    # Inicializar el repositorio de géneros
    repositorio_genero = RepositorioGenero(ruta_json)
    
    # Inicializar CRUDEspecifico correctamente
    crud_especifico = CRUDEspecifico(ruta_json, repositorio_genero)

    while True:
        print("\n- Tareas de Subgéneros Literarios -\n")
        print("1. Mostrar Subgéneros.")
        print("2. Añadir Subgénero.")
        print("3. Modificar Datos de Subgénero.")
        print("4. Eliminar Subgénero.")
        print("0. Volver al Menú de Géneros.")

        opcion = input("\nSelecciona una opción: \n").strip()

        if opcion == "1":
            crud_especifico.mostrar_especificos_crud(biblioteca)
        elif opcion == "2":
            crud_especifico.agregar_especifico(biblioteca)
        elif opcion == "3":
            crud_especifico.actualizar_especifico(biblioteca)
        elif opcion == "4":
            crud_especifico.eliminar_especifico(biblioteca)
        elif opcion == "0":
            break
        else:
            print("⚠️ Opción no válida. Intenta de nuevo.")
