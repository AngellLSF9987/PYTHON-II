from ClinicaVeterinaria.utilidades.menu import mostrar_menu_principal
from ClinicaVeterinaria.database.db_setup import crear_tablas

if __name__ == "__main__":
    print("=== Bienvenid@ a la Clínica Veterinaria ===")
    crear_tablas()  # Garantiza que las tablas existen
    while True:
        mostrar_menu_principal()