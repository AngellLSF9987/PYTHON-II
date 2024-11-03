# deportes/menus/submenu_tenis.py

from ..utilidades.utilidades import *

def submenu_tenis(deportistas):
    """Submenú para seleccionar tipo de deporte y realizar acciones."""
    
    while True:
        print("\nSeleccione Acción:")
        print("1. Crear Tenista.")
        print("2. Modificar Datos de un Tenista.")
        print("3. Buscar un Tenista.")
        print("4. Mostrar Todos los Tenistas.")
        print("0. Menú Principal.")
        
        opcion = input("Selecciona una opción:\n")

        if opcion == "1":
            # Crear Tipo Tenista
            deportista = crear_deportista('tenista')
            if deportista:
                # Añadir Tipo Tenista a la lista de Tenista, al diccionario de Deportistas
                deportistas['tenista'].append(deportista)
        elif opcion == "2":
            modificar_datos_tenista(deportistas['tenista'])
        elif opcion == "3":
            # Buscar Tenista por nombre
            buscar_tenista(deportistas['tenista'])
        elif opcion == "4":
            # Mostrar Tenistas
            mostrar_tenistas(deportistas)
        elif opcion == "0":
            return # Menú principal
        else:
            print("Opción no válida.")
            
def modificar_datos_tenista(tenistas):
    """Permite modificar los datos de un tenista registrado."""
    nombre = input("Ingrese el nombre del tenista a modificar:\n")
    
    # Buscar tenista en la lista
    for tenista in tenistas:
        if tenista.get_nombre().lower() == nombre.lower():
            print(f"\nModificando datos de {nombre}.")
            # Modificar atributo ranking
            nuevo_ranking = input(f"Nuevo ranking (actual: {tenista.get_ranking()}):\n")
            if nuevo_ranking:
                tenista.set_ranking(nuevo_ranking)
            
            # Modificar atributo trofeos ganados
            nuevo_trofeos_ganados = input(f"Nuevos Trofeos Ganados (actual: {tenista.get_trofeos_ganados()}):\n")
            if nuevo_trofeos_ganados:
                tenista.set_trofeos_ganados(nuevo_trofeos_ganados)

            # Puedes añadir más atributos aquí según la estructura de tenista
            print(f"{nombre} ha sido actualizado correctamente.")
            return  # Finaliza una vez que ha encontrado y modificado el tenista
    
    print("Tenista no encontrado.")
    
def buscar_tenista(tenistas):
    """Busca un deportista por nombre y muestra sus datos."""
    nombre = input(f"Ingrese el nombre del tenista que desea buscar:\n")

    # Buscar en la lista correspondiente al tipo de deportista
    for tenista in tenistas:
        if tenista.get_nombre().lower() == nombre.lower():
            # Mostrar datos del registro buscado
            print("\nResumen del futbolista:")
            print(tenista.mostrar_datos())
        else:
            print("Tenista no encontrado en los registros.")
        