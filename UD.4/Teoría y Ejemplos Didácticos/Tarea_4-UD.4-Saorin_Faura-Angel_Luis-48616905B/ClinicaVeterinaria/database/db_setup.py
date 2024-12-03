import os
import sqlite3
from db_connection import ConexionDB

# Ruta de la base de datos
db_path = os.path.join(
    os.getcwd(),
    "Tarea_4-UD.4-Saorin_Faura-Angel_Luis-48616905B",
    "clinica_veterinaria.db"
)

def crear_tablas():
    """
    Crea las tablas necesarias en la base de datos si no existen.
    """
    try:
        db = ConexionDB()
        conexion = db.conectar()
        cursor = conexion.cursor()

        # Crear tabla T_Propietarios
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS T_Propietarios (
            IdPropietario INTEGER PRIMARY KEY AUTOINCREMENT,
            Nombre TEXT NOT NULL,
            Apellido TEXT NOT NULL,
            DNI TEXT UNIQUE NOT NULL,
            Telefono TEXT NOT NULL,
            Direccion TEXT NOT NULL
        );
        """)

        # Crear tabla T_Mascotas
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS T_Mascotas (
            IdMascota INTEGER PRIMARY KEY AUTOINCREMENT,
            IdPropietario INTEGER NOT NULL,
            Nombre TEXT NOT NULL,
            Especie TEXT NOT NULL,
            Raza TEXT,
            Edad INTEGER,
            FOREIGN KEY (IdPropietario) REFERENCES T_Propietario(IdPropietario)
        );
        """)

        # Crear tabla T_Visitas
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS T_Visitas (
            IdVisita INTEGER PRIMARY KEY AUTOINCREMENT,
            IdMascota INTEGER NOT NULL,
            Fecha DATE NOT NULL,
            Motivo TEXT NOT NULL,
            FOREIGN KEY (IdMascota) REFERENCES T_Mascotas(IdMascota)
        );
        """)

        # Crear tabla T_Facturas
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS T_Facturas (
            IdFactura INTEGER PRIMARY KEY AUTOINCREMENT,
            IdVisita INTEGER NOT NULL,
            FechaEmision DATE NOT NULL,
            Total REAL NOT NULL,
            FOREIGN KEY (IdVisita) REFERENCES T_Visitas(IdVisita)
        );
        """)

        conexion.commit()
        print("Tablas creadas correctamente.")
    except sqlite3.Error as e:
        print(f"Error al crear tablas: {e}")
    finally:
        conexion.close()

def insertar_datos_ejemplo():
    """
    Inserta datos de ejemplo en la base de datos.
    """
    try:
        db = ConexionDB()
        conexion = db.conectar()
        cursor = conexion.cursor()

        # Insertar datos en T_Propietario
        propietarios = [
            ("Juan", "Pérez López", "12345678A", "600123456", "Calle Luna, 15"),
            ("Ana", "García Fernández", "87654321B", "650987654", "Avenida Sol, 10"),
            ("Luis", "Martínez Ruiz", "11223344C", "620765432", "Calle Estrella, 8")
        ]
        cursor.executemany("""
        INSERT OR IGNORE INTO T_Propietario (Nombre, Apellido, DNI, Telefono, Direccion)
        VALUES (?, ?, ?, ?, ?);
        """, propietarios)

        # Insertar datos en T_Mascotas
        mascotas = [
            (1, "Rex", "Perro", "Labrador", 5),
            (1, "Miau", "Gato", "Siamés", 3),
            (2, "Bunny", "Conejo", "Angora", 2),
            (3, "Toby", "Perro", "Chihuahua", 4)
        ]
        cursor.executemany("""
        INSERT OR IGNORE INTO T_Mascotas (IdPropietario, Nombre, Especie, Raza, Edad)
        VALUES (?, ?, ?, ?, ?);
        """, mascotas)

        # Insertar datos en T_Visitas
        visitas = [
            (1, "2024-12-01", "Vacunación anual"),
            (2, "2024-12-02", "Chequeo general"),
            (3, "2024-12-03", "Corte de uñas"),
            (4, "2024-12-04", "Desparasitación")
        ]
        cursor.executemany("""
        INSERT OR IGNORE INTO T_Visitas (IdMascota, Fecha, Motivo)
        VALUES (?, ?, ?);
        """, visitas)

        # Insertar datos en T_Facturas
        facturas = [
            (1, "2024-12-01", 50.00),
            (2, "2024-12-02", 40.00),
            (3, "2024-12-03", 20.00),
            (4, "2024-12-04", 30.00)
        ]
        cursor.executemany("""
        INSERT OR IGNORE INTO T_Facturas (IdVisita, FechaEmision, Total)
        VALUES (?, ?, ?);
        """, facturas)

        conexion.commit()
        print("Datos de ejemplo insertados correctamente.")
    except sqlite3.Error as e:
        print(f"Error al insertar datos de ejemplo: {e}")
    finally:
        conexion.close()

if __name__ == "__main__":
    print("Inicializando base de datos...")
    crear_tablas()
    insertar_datos_ejemplo()
    print("Base de datos lista con datos de ejemplo.")
