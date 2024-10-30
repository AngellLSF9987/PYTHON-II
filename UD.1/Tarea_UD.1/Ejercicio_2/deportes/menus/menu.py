# deportes/utilidades/menu.py

from ..menus.submenu_futbol import submenu_futbol
from ..menus.submenu_tenis import submenu_tenis
from ..menus.submenu_running import submenu_running
from ..utilidades.utilidades import inicializar_deportistas, mostrar_deportistas

def menu():
   
    deportistas = {
        'futbolista': [],
        'tenista': [],
        'runner': []
    }
    
    inicializar_deportistas(deportistas)    

    while True:
        print("\nBienvenido a Sports Affinity!")
        print("1. Fútbol.")
        print("2. Tenis.")
        print("3. Running.")
        print("4. Mostrar todos los Deportistas.")
        print("0. Salir.")

        opcion = input("Selecciona una opción:\n")

        if opcion == "1":
            # Redirige al submenú de Futbol
            submenu_futbol(deportistas)
        elif opcion == "2":
            # Redirige al submenú de Futbol
            submenu_tenis(deportistas)
        elif opcion == "3":
            # Redirige al submenú de Futbol
            submenu_running(deportistas)
        elif opcion == "4":
            mostrar_deportistas(deportistas)
        elif opcion == "0":
            print("Hasta luego!")
            break
        else:
            print("Opción no válida.")
