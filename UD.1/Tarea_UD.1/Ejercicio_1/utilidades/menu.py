from utilidades.crud import *
from utilidades.herramientas import *

def menu():

    while True:
        print("\n1. Crear Nuevo Cliente.")
        print("2. Buscar Cliente.")        
        print("3. Modificar Cliente.")
        print("4. Borrar Cliente.")
        print("5. Comprobar IMC de un Cliente.")
        print("6. Comprobar mayoría de edad de un Cliente.")
        print("0. Salir.")

        opcion = input("Selecciona una opción:\n")

        if opcion == "1":
            añadir_cliente()
        elif opcion == "2":
            buscar_cliente()
        elif opcion == "3":
            modificar_cliente()
        elif opcion == "4":
            borrar_cliente()
        elif opcion == "5":
            comprobar_imc()
        elif opcion == "6":
            comprobar_edad()                                    

        elif opcion == "0":
            print("Hasta luego!")
        
        else:
            print("OJO! Opción no válida.")