from modelos.bebida import Bebida

class Maquina:

    def __init__(self):
        """ - Se inicializan las bebidas disponibles creando un diccionario:
                - KEY : '1'
                - VALUE : El propio objeto Bebida y sus propiedades.

                    self.bebidas = {
                            "1": Bebida("Agua", 0.50),
                            "2": Bebida("Coca-Cola", 1.20),
                            "3": Bebida("Fanta", 1.00)       
                        }        
        """
        # Se inicializan las bebidas disponibles creando un diccionario.
        self.bebidas = {
                "1": Bebida("Agua", 0.50),
                "2": Bebida("Coca-Cola", 1.20),
                "3": Bebida("Fanta", 1.00)
            }

    def mostrar_menu(self):
        # Mostrar las opciones de bebida disponibles
        """ - Mostrar las opciones de bebida disponibles
        Propiedad o Argumento [.2f]:
            - Se emplea para el corte al segundo número en la parte de decimal de un valor numérico."""
        print("\n- Menú de Bebidas -")
        for key, bebida in self.bebidas.items():
            print(f"Opción {key}. {bebida.nombre} - {bebida.precio:.2f}€")
        print("0. Salir")

    def seleccionar_bebida(self):
        # Solicitar al usuario que seleccione una bebida
        opcion = input("\nSeleccione opción de bebida [1,2,3]..[0] Salir:\n")
        return opcion

    def calculos_pago(self, bebida):
        #  Pedir dinero al usuario y calcular la diferencia.

        dinero_total = 0

        while dinero_total < bebida.precio:
            dinero_str = input(f"Introduce pago (faltan {bebida.precio - dinero_total:.2f}€): ")
            
            # Reemplazar coma por punto para aceptar decimales con coma
            dinero_str = dinero_str.replace(",",".")

            dinero = float(dinero_str)
            
            dinero_total += dinero

            if dinero_total < bebida.precio:
                print(f"Falta dinero. Has introducido {dinero_total:.2f}€")
                
            elif dinero_total == bebida.precio:
                print(f"Dinero exacto. Entregando.. {bebida.nombre}")
                break
            else:
                print(f"Te sobran {dinero_total - bebida.precio:.2f}€. Entregando.. {bebida.nombre}")
                break
