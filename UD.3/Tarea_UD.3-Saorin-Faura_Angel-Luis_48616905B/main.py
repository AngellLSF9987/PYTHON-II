# biblioteca/main.py

# from biblioteca.utilidades.ruta_datos_json import RUTA_DATOS_BIBLIOTECA
# from biblioteca.utilidades.lector_json import cargar_datos_json
from biblioteca.menus.menu import menu
import os

def main():
    
    # # Comprobar la ruta absoluta
    # print(f"Ruta calculada: {RUTA_DATOS_BIBLIOTECA}")
    
    # # Verificar si el archivo existe
    # if not os.path.exists(RUTA_DATOS_BIBLIOTECA):
    #     print("El archivo JSON no existe en la ruta especificada.")
    #     return

    # # Cargar los datos y mostrar un resumen
    # datos = cargar_datos_json()
    # if datos:
    #     print("Datos cargados exitosamente.")
    # else:
    #     print("No se pudieron cargar los datos del archivo JSON.")
    #     return

    # Llamar a la función menu después de las comprobaciones
    menu()

# Ejecutar el programa principal
if __name__ == "__main__":
    main()
