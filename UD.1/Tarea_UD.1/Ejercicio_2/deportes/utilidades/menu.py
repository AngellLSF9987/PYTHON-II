# deportes/utilidades/menu.py

from .utilidades import crear_deportista
from ..modelos.futbolista import Futbolista
from ..modelos.tenista import Tenista
from ..modelos.runner import Runner


def inicializar_deportistas(deportistas):
    # Agregar un futbolista predeterminado
    deportistas['futbolista'].append(Futbolista("Lionel Messi", 36, "Argentina", "Inter Miami", 800))
    # Agregar un tenista predeterminado
    deportistas['tenista'].append(Tenista("Rafael Nadal", 37, "España", 2, 22))
    # Agregar un runner predeterminado
    deportistas['runner'].append(Runner("Usain Bolt", 37, "Jamaica", "100m", "9.58"))

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
            for futbolista in deportistas['futbolista']:
                print(futbolista.mostrar_datos())
        elif opcion == "5":
            # Mostrar Tenistas
            for tenista in deportistas['tenista']:
                print(tenista.mostrar_datos())
        elif opcion == "6":
            # Mostrar Runners
            for runner in deportistas['runner']:
                print(runner.mostrar_datos())
        elif opcion =='7':
            # Mostrar Todos
            for tipo, lista_deportistas in deportistas.items():
                print(f"\n{tipo.capitalize()}s:")
                for deportista in  lista_deportistas:
                    print(deportista.mostrar_datos())
                    print()
        elif opcion == "0":
            print("Hasta luego!")
            break
        else:
            print("Opción no válida.")
