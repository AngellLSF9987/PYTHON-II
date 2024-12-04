import os
import sqlite3
from ClinicaVeterinaria.database.db_connection import ConexionDB

# Ruta de la base de datos
db_path = os.path.join(
    os.getcwd(),
    "Tarea_4-UD.4-Saorin_Faura-Angel_Luis-48616905B",
    "clinica_veterinaria.db"
)
print(f"Conectando a la base de datos en: {db_path}")

def crear_tablas(conexion):
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
            Apellido1 TEXT NOT NULL,
            Apellido2 TEXT NOT NULL,
            DNI TEXT UNIQUE NOT NULL,
            Telefono TEXT NOT NULL,
            Direccion TEXT NOT NULL,
            Email TEXT NOT NULL
        );
        """)

        # Crear tabla T_Mascotas
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS T_Mascotas (
            IdMascota INTEGER PRIMARY KEY AUTOINCREMENT,
            DNIPropietario TEXT NOT NULL,
            Nombre TEXT NOT NULL,
            Especie TEXT NOT NULL,
            Raza TEXT NOT NULL,
            Edad INTEGER NOT NULL,
            Peso REAL NOT NULL,
            FOREIGN KEY (DNIPropietario) REFERENCES T_Propietarios(DNI)
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

def insertar_datos_ejemplo(conexion):
    """
    Inserta datos de ejemplo en la base de datos.
    """
    try:
        db = ConexionDB()
        conexion = db.conectar()
        cursor = conexion.cursor()

        # Insertar datos en T_Propietario
        propietarios = [
            ("Juan", "Pérez", "López", "12345678A", "600123456", "Calle Luna, 15", "juan@perezlopez.com"),
            ("Ana", "García", "Fernández", "87654321B", "650987654", "Avenida Sol, 10", "ana@garciafernandez"),
            ("Luis", "Martínez", "Ruiz", "11223344C", "620765432", "Calle Estrella, 8", "luis@martinezruiz.com"),
            ("María", "Martínez", "Soler", "11223556J", "623365432", "Calle Sebastopol, 8", "maria@martinezsoler.com")
        ]
        cursor.executemany("""
        INSERT OR IGNORE INTO T_Propietarios (Nombre, Apellido1, Apellido2, DNI, Telefono, Direccion, Email)
        VALUES (?, ?, ?, ?, ?, ?, ?);
        """, propietarios)

        # Insertar datos en T_Mascotas
        mascotas = [
            ("12345678A", "Rex", "Perro", "Labrador", 5, 40.00),
            ("87654321B", "Miau", "Gato", "Siamés", 3, 8.50),
            ("11223344C", "Bunny", "Conejo", "Angora", 2, 2.10),
            ("11223556J", "Toby", "Perro", "Chihuahua", 1, 2.95)
        ]
        cursor.executemany("""
        INSERT OR IGNORE INTO T_Mascotas (DNIPropietario, Nombre, Especie, Raza, Edad, Peso)
        VALUES (?, ?, ?, ?, ?, ?);
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

def obtener_conexion():
    """
    Devuelve una conexión a la base de datos SQLite.
    """
    return sqlite3.connect("clinica_veterinaria.db")
