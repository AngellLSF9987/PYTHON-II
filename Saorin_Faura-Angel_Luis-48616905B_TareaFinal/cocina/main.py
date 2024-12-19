# cocina/main.py
import os
from database.db_connection import inicializar_base_datos, ConexionDB
from database.db_setup import DBSetup

def test_db():
    """
    Realiza pruebas de creación de tablas e inserción de datos de ejemplo.
    """
    db_path = os.path.join(os.getcwd(), "database", "cocina.db")

    with ConexionDB(ruta_bd=db_path) as conexion:
        setup = DBSetup()
        
        # Crear tablas
        setup.crear_tablas(conexion)
        
        # Insertar datos de ejemplo
        setup.insertar_datos_ejemplo(conexion)

        print("\nPruebas de base de datos completadas con éxito.")

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

    # Realizar pruebas de la base de datos (opcional)
    ejecutar_test = input("\u00bfDeseas ejecutar las pruebas de la base de datos? (s/n): ").strip().lower()
    if ejecutar_test == 's':
        test_db()
    
    print("\nPrograma terminado.")