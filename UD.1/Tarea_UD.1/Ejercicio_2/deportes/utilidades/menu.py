# deportes/utilidades/menu.py

from .utilidades import *


def menu():
    deportistas = {
        'futbolista': [],
        'tenista': [],
        'runner': []
    }
    
    inicializar_deportistas(deportistas)

    while True:
        print("\n1. Crear Futbolista.")
        print("2. Crear Tenista.")
        print("3. Crear Runner.")
        print("4. Mostrar todos los Futbolistas.")
        print("5. Mostrar todos los Tenistas.")
        print("6. Mostrar todos los Runners.")
        print("7. Mostrar todos los Deportistas.")
        print("8. Modificar datos de un Deportista.")
        print("0. Salir.")

        opcion = input("Selecciona una opción:\n")

        if opcion == "1":
            # Crear Tipo Futbolista
            deportista = crear_deportista('futbolista')
            if deportista:
                # Añadir Tipo Futbolista a la lista de Futbolista, al diccionario de Deportistas
                deportistas['futbolista'].append(deportista)
        elif opcion == "2":
            deportista = crear_deportista('tenista')
            if deportista:
                # Añadir Tipo Tenista a la lista de Tenista, al diccionario de Deportistas
                deportistas['tenista'].append(deportista)
        elif opcion == "3":
            deportista = crear_deportista('runner')
            if deportista:
                # Añadir Tipo Runner a la lista de Runner, al diccionario de Deportistas
                deportistas['runner'].append(deportista)
        elif opcion == "4":
            # Mostrar Futbolistas
            mostrar_futbolistas(deportistas)
        elif opcion == "5":
            # Mostrar Tenistas
            mostrar_tenistas(deportistas)
        elif opcion == "6":
            # Mostrar Runners
            mostrar_runners(deportistas)
        elif opcion == "7":
            # Mostrar Todos
            mostrar_deportistas(deportistas)
        elif opcion == "8":
            # Modifcar datos de un Deportista
            modificar_datos(deportistas)
        elif opcion == "0":
            print("Hasta luego!")
            break
        else:
            print("Opción no válida.")
