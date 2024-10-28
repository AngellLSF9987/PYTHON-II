# deportes/utils/menu.py

from utilidades.utilidades import crear_deportista

def menu():
    deportistas = {
        'futbolista': [],
        'tenista': [],
        'runner': []
    }

    while True:
        print("\n1. Crear Futbolista.")
        print("2. Crear Tenista.")
        print("3. Crear Runner.")
        print("4. Mostrar todos los Futbolistas.")
        print("5. Mostrar todos los Tenistas.")
        print("6. Mostrar todos los Runners.")
        print("0. Salir.")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            deportista = crear_deportista('futbolista')
            if deportista:
                deportistas['futbolista'].append(deportista)
        elif opcion == "2":
            deportista = crear_deportista('tenista')
            if deportista:
                deportistas['tenista'].append(deportista)
        elif opcion == "3":
            deportista = crear_deportista('runner')
            if deportista:
                deportistas['runner'].append(deportista)
        elif opcion == "4":
            for futbolista in deportistas['futbolista']:
                print(futbolista.mostrar_datos())
        elif opcion == "5":
            for tenista in deportistas['tenista']:
                print(tenista.mostrar_datos())
        elif opcion == "6":
            for runner in deportistas['runner']:
                print(runner.mostrar_datos())
        elif opcion == "0":
            print("Hasta luego!")
            break
        else:
            print("Opción no válida.")
