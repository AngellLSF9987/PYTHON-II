from modelos.maquina import Maquina

def main():

    maquina = Maquina()

    while True:
        maquina.mostrar_menu()
        opcion = maquina.seleccionar_bebida()

        if opcion == "0":
            print("Saliendo..")
            break
        
        if opcion in maquina.bebidas:
            bebida = maquina.bebidas[opcion]
            maquina.calculos_pago(bebida)
            break
        else:
            print("Opcion no válida...")
            
if __name__ == "__main__":
    main()