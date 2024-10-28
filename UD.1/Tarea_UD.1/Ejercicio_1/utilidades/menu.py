from utilidades.crud import añadir_cliente, buscar_cliente, modificar_cliente, borrar_cliente
from utilidades.herramientas import comprobar_edad, comprobar_imc

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
            dni = input("Introduce el DNI del cliente:\n")
            cliente = buscar_cliente(dni)
            
            if cliente:
                print(cliente.mostrar_datos())
            else:
                print("Cliente no encontrado.")
                
        elif opcion == "3":
            modificar_cliente()
        elif opcion == "4":
            borrar_cliente()
        
        elif opcion == "5":
            
            dni = input("Introduce el DNI del cliente:\n")
            cliente = buscar_cliente(dni)
            
            if cliente:
                print(comprobar_imc(cliente))
            else:
                print("Cliente no encontrado.")
        
        elif opcion == "6":
            
            dni = input("Introduce el DNI del cliente:\n")
            cliente = buscar_cliente(dni)
            
            if cliente:
                if comprobar_edad(cliente):
                    print("El cliente es mayor de edad.")
                else:
                    print("El cliente es menor de edad.")
            else:
                print("Cliente no encontrado.")                                    

        elif opcion == "0":
            print("Hasta luego!")
            break
        else:
            print("OJO! Opción no válida.")