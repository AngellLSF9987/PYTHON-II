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
            buscar_deportista(deportistas, 'futbolista')
        elif opcion == "4":
            # Mostrar Futbolistas
            mostrar_futbolistas(deportistas)
        elif opcion == "0":
            return # Menú principal
        else:
            print("Opción no válida.")
            
def modificar_datos_futbolista(deportistas):
    """Permite modificar los datos de un futbolista registrado."""
    nombre = input("Ingrese el nombre del futbolista a modificar:\n")
    
    # Buscar futbolista en la lista
    futbolistas = deportistas.get('futbolista', [])
    for futbolista in futbolistas:
        if futbolista['nombre'] == nombre:
            print(f"\nModificando datos de {nombre}. Deja el campo en blanco para mantener el valor actual.")
            # Modificar atributos específicos
            nuevo_nombre = input("Nuevo nombre (actual: {}): ".format(futbolista['nombre']))
            if nuevo_nombre:
                futbolista['nombre'] = nuevo_nombre
            
            # Modificar otros atributos
            nueva_posicion = input("Nueva posición (actual: {}): ".format(futbolista.get('posicion', 'Desconocida')))
            if nueva_posicion:
                futbolista['posicion'] = nueva_posicion

            # Puedes añadir más atributos aquí según la estructura de futbolista
            print(f"{nombre} ha sido actualizado correctamente.")
            return  # Finaliza una vez que ha encontrado y modificado el futbolista
    
    print("Futbolista no encontrado.")
    
def buscar_deportista(deportistas, tipo):
    """Busca un deportista por nombre y muestra sus datos."""
    nombre = input(f"Ingrese el nombre del {tipo} que desea buscar:\n")

    # Buscar en la lista correspondiente al tipo de deportista
    for deportista in deportistas.get(tipo, []):
        if deportista['nombre'].lower() == nombre.lower():
            print("\nDatos del Deportista:")
            print(f"Nombre: {deportista['nombre']}")
            print(f"Posición: {deportista.get('posicion', 'Desconocida')}")
            # Puedes añadir más atributos aquí según la estructura del deportista
            return  # Finaliza la búsqueda una vez encontrado

    print(f"{tipo.capitalize()} no encontrado.")