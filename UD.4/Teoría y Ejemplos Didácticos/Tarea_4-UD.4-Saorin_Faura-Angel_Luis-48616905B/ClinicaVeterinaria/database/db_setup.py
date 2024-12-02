import os
import sqlite3
from database.db_connection import ConexionDB

# Ruta de la base de datos
db_path = os.path.join(os.getcwd(), "Tarea_4-UD.4-Saorin_Faura-Angel_Luis-48616905B", "clinica_veterinaria.db")

def crear_tablas():
    # Verificar si la base de datos ya existe
    if not os.path.exists(db_path):
        # Si no existe, la creamos
        db = ConexionDB()
        conexion = db.conectar()
        cursor = conexion.cursor()

        # Crear tabla T_Propietarios
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS T_Propietario (
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

        # Confirmar y cerrar conexión
        conexion.commit()
        conexion.close()
        print("Base de datos y tablas creadas correctamente.")
    else:
        print("La base de datos ya existe.")

if __name__ == "__main__":
    crear_tablas()
