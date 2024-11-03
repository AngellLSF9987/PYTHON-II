# deportes/menus/submenu_futbol.py

from ..utilidades.utilidades import *

def submenu_futbol(deportistas):
    """Submenú para seleccionar tipo de deporte y realizar acciones."""
    
    while True:
        print("\nSeleccione Acción:")
        print("1. Crear Futbolista.")
        print("2. Modificar Datos de un Futbolista.")
        print("3. Buscar un Futbolista.")
        print("4. Mostrar Todos los Futbolistas.")
        print("0. Menú Principal.")
        
        opcion = input("Selecciona una opción:\n")

        if opcion == "1":
            # Crear Tipo Futbolista
            deportista = crear_deportista('futbolista')
            if deportista:
                # Añadir Tipo Futbolista a la lista de Futbolista, al diccionario de Deportistas
                deportistas['futbolista'].append(deportista)
        elif opcion == "2":
            modificar_datos_futbolista(deportistas['futbolista'])
        elif opcion == "3":
            # Buscar Futbolista por nombre
            #buscar_deportista(deportistas, 'futbolista')
            buscar_futbolista(deportistas['futbolista'])
        elif opcion == "4":
            # Mostrar Futbolistas
            mostrar_futbolistas(deportistas)
        elif opcion == "0":
            return # Menú principal
        else:
            print("Opción no válida.")
            
def modificar_datos_futbolista(futbolistas):
    """Permite modificar los datos de un futbolista registrado."""
    nombre = input("Ingrese el nombre del futbolista a modificar:\n")
    
    # Buscar futbolista en la lista de objetos Futbolista
    for futbolista in futbolistas:
        
        # Comparar el nombre del futbolista, usando el método get, que contiene la propiedad nombre encapsulada, ya que esta privatizada.
        # Se ignoran mayúsculas y/o minúsculas.
        if futbolista.get_nombre().lower() == nombre.lower():
            print(f"\nModificando datos de {nombre}.")
            # Modificar atributo equipo
            nuevo_equipo = input(f"Nuevo equipo (actual: {futbolista.get_equipo()}):\n")
            if nuevo_equipo:
                futbolista.set_equipo(nuevo_equipo)
            
            # Modificar atributo goles
            nuevos_goles = int(input(f"Cantidad de goles (actual: {futbolista.get_goles()}):\n"))
            if nuevos_goles:
                futbolista.set_goles(int(nuevos_goles))
            else:
                print("Error: Los goles deben ser un número entero.")

            # Puedes añadir más atributos aquí según la estructura de futbolista
            print(f"{nombre} ha sido actualizado correctamente.")
            return  # Finaliza una vez que ha encontrado y modificado el futbolista
    
    print("Futbolista no encontrado.")


def buscar_futbolista(futbolistas):
    """Busca un futbolista por nombre y muestra sus datos."""
    nombre = input(f"Ingrese el nombre del futbolista que desea buscar:\n")

    for futbolista in futbolistas:
        if futbolista.get_nombre().lower() == nombre.lower():
            # Mostrar datos del registro buscado
            print("\nResumen del futbolista:")
            print(futbolista.mostrar_datos())
        else:
            print("Futbolista no encontrado en los registros.")