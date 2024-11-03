# deportes/menus/submenu_running.py

from ..utilidades.utilidades import *

def submenu_running(deportistas):
    """Submenú para seleccionar tipo de deporte y realizar acciones."""
    
    while True:
        print("\nSeleccione Acción:")
        print("1. Crear Runner.")
        print("2. Modificar Datos de un Runner.")
        print("3. Buscar un Runner.")
        print("4. Mostrar Todos los Runners.")
        print("0. Menú Principal.")
        
        opcion = input("Selecciona una opción:\n")

        if opcion == "1":
            # Crear Tipo Runner
            deportista = crear_deportista('runner')
            if deportista:
                # Añadir Tipo Runner a la lista de Runner, al diccionario de Deportistas
                deportistas['runner'].append(deportista)
        elif opcion == "2":
            modificar_datos_runner(deportistas['runner'])
        elif opcion == "3":
            # Buscar Runner por nombre
            buscar_runner(deportistas['runner'])
        elif opcion == "4":
            # Mostrar Futbolistas
            mostrar_runners(deportistas)
        elif opcion == "0":
            return # Menú principal
        else:
            print("Opción no válida.")
            
def modificar_datos_runner(runners):
    """Permite modificar los datos de un runner registrado."""
    nombre = input("Ingrese el nombre del runner a modificar:\n")
    
    # Buscar runner en la lista
    for runner in runners:
        if runner.get_nombre().lower() == nombre.lower():
            print(f"\nModificando datos de {nombre}.")
            # Modificar atributo especialidad
            nueva_especialidad = input(f"Nuevo especialidad (actual: {runner.get_especialidad()}):\n")
            if nueva_especialidad:
                runner.set_especialidad(nueva_especialidad)
            
            # Modificar atributo record
            nuevo_record = input(f"Nuevo Récord (actual: {runner.get_especialidad()}):\n")
            if nuevo_record:
                runner.set_record(nuevo_record)

            # Puedes añadir más atributos aquí según la estructura de runner
            print(f"{nombre} ha sido actualizado correctamente.")
            return  # Finaliza una vez que ha encontrado y modificado el runner
    
    print("Futbolista no encontrado.")
    
def buscar_runner(runners):
    """Busca un deportista por nombre y muestra sus datos."""
    nombre = input(f"Ingrese el nombre del Runner que desea buscar:\n")

    # Buscar en la lista correspondiente al tipo de deportista
    for runner in runners:
        if runner.get_nombre().lower() == nombre.lower():
            # Mostrar datos del registro buscado
            print("\nResumen del futbolista:")
            print(runner.mostrar_datos())
        else:
            print("Runner no encontrado en los registros.")