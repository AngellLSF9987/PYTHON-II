# cocina\main.py
import os
from database.db_connection import inicializar_base_datos
from database.db_setup import DBSetup

if __name__ == "__main__":
    print("\n=== Bienvenid@ a la Clínica Veterinaria ===\n")

    # Ruta a la base de datos
    db_path = os.path.join(
        os.getcwd(),
        "database",
        "cocina.db"
    )

    # Inicializar la base de datos (crear tablas e insertar datos de ejemplo)
    inicializar_base_datos(db_path)
