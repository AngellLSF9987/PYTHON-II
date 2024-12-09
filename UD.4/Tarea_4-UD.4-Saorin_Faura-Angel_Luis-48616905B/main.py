# UD.4\Tarea_4-UD.4-Saorin_Faura-Angel_Luis-48616905B\main.py
import os
from ClinicaVeterinaria.database.db_setup import inicializar_base_datos
from ClinicaVeterinaria.utilidades.menu import inicializar_repositorios, mostrar_menu_principal

if __name__ == "__main__":
    print("\n=== Bienvenid@ a la Clínica Veterinaria ===\n")

    # Ruta a la base de datos
    db_path = os.path.join(
        os.getcwd(),
        "UD.4",
        "Tarea_4-UD.4-Saorin_Faura-Angel_Luis-48616905B",
        "ClinicaVeterinaria",
        "database",
        "clinica_veterinaria.db"
    )

    # Inicializar la base de datos (crear tablas e insertar datos de ejemplo)
    inicializar_base_datos(db_path)

    # Inicializar repositorios
    repositorios = inicializar_repositorios(db_path)

    # Mostrar el menú principal
    mostrar_menu_principal(repositorios)
