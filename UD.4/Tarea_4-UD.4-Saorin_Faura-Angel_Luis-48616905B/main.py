from ClinicaVeterinaria.utilidades.menu import mostrar_menu_principal
from ClinicaVeterinaria.database.db_setup import crear_tablas, insertar_datos_ejemplo

if __name__ == "__main__":
    print("=== Bienvenid@ a la Clínica Veterinaria ===")
    crear_tablas()              # Garantiza que las tablas existen
    insertar_datos_ejemplo()    # Inyección de registros de ejemplo
    while True:
        mostrar_menu_principal()