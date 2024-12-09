# UD.4\Tarea_4-UD.4-Saorin_Faura-Angel_Luis-48616905B\ClinicaVeterinaria\database\db_setup.py
import sqlite3
from ClinicaVeterinaria.database.db_connection import ConexionDB

def crear_tablas(conexion):
    """
    Crea las tablas necesarias en la base de datos si no existen.
    """
    tablas_sql = {
        "T_Propietarios": """
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
        """,
        "T_Mascotas": """
            CREATE TABLE IF NOT EXISTS T_Mascotas (
                IdMascota INTEGER PRIMARY KEY AUTOINCREMENT,
                Nombre TEXT NOT NULL,
                Especie TEXT NOT NULL,
                Raza TEXT,
                FecNac DATE,
                Peso REAL NOT NULL,
                Propietario_DNI TEXT,
                FOREIGN KEY (Propietario_DNI) REFERENCES T_Propietarios(DNI)
            );
        """,
        "T_Visitas": """
            CREATE TABLE IF NOT EXISTS T_Visitas (
                IdVisita INTEGER PRIMARY KEY AUTOINCREMENT,
                Fecha TEXT NOT NULL,
                Motivo TEXT,
                Tratamiento TEXT,
                Mascota_Id INTEGER,
                Propietario_DNI TEXT,
                FOREIGN KEY (Mascota_Id) REFERENCES T_Mascotas(IdMascota),
                FOREIGN KEY (Propietario_DNI) REFERENCES T_Propietarios(DNI)
            );
        """,
        "T_Facturas": """
            CREATE TABLE IF NOT EXISTS T_Facturas (
                IdFactura INTEGER PRIMARY KEY AUTOINCREMENT,
                Fecha TEXT NOT NULL,
                Importe REAL NOT NULL,
                Visita_Id INTEGER,
                Mascota_Id INTEGER,
                Propietario_DNI TEXT,
                FOREIGN KEY (Propietario_DNI) REFERENCES T_Propietarios(DNI),
                FOREIGN KEY (Mascota_Id) REFERENCES T_Mascotas(IdMascota),
                FOREIGN KEY (Visita_Id) REFERENCES T_Visitas(IdVisita)
            );
        """
    }

    cursor = conexion.cursor()
    for nombre, sql in tablas_sql.items():
        cursor.execute(sql)
        print(f"✔️ Tabla '{nombre}' creada o ya existente.")
    conexion.commit()


def insertar_datos_ejemplo(conexion):
    """
    Inserta datos de ejemplo en las tablas para pruebas iniciales,
    verificando que no haya duplicados.
    """
    datos_propietarios = [
        ("Ana", "Pérez", "Pérez", "12345678A", "600123456", "Calle Luna, 6", "ana@perez.com"),
        ("Carlos", "López", "López", "87654321B", "610654321", "Calle Sol, 8", "carlos@lopez.com"),
    ]
    datos_mascotas = [
        ("Firulais", "Perro", "Golden Retriever", "2022-10-10", 40.00, "12345678A"),
        ("Michi", "Gato", "Siames", "2019-12-12", 8.00, "87654321B"),
    ]
    datos_visitas = [
        ("2024-12-05", "Vacunación", "Vacunación", 1, "12345678A"),  # 1 es el ID de Firulais
        ("2024-12-06", "Consulta general", "Consulta general", 2, "87654321B"),  # 2 es el ID de Michi
    ]
    datos_facturas = [
        ("2024-12-05", 50.00, 1, 1, "12345678A"),  
        ("2024-12-06", 30.00, 2, 2, "87654321B"),
    ]

    try:
        cursor = conexion.cursor()

        # Verificar si los propietarios ya existen antes de insertarlos
        for propietario in datos_propietarios:
            query = "SELECT 1 FROM T_Propietarios WHERE DNI = ?"
            cursor.execute(query, (propietario[3],))  # Usamos el DNI para verificar existencia
            if not cursor.fetchone():  # Si no existe, insertamos
                cursor.execute(""" 
                    INSERT INTO T_Propietarios (Nombre, Apellido1, Apellido2, DNI, Telefono, Direccion, Email)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                """, propietario)
                print(f"✔️ Propietario {propietario[0]} {propietario[1]} insertado.")
            else:
                print(f"⚠️ Propietario con DNI {propietario[3]} ya existe, no se insertó.")

        # Verificar si las mascotas ya existen antes de insertarlas
        for mascota in datos_mascotas:
            query = "SELECT 1 FROM T_Mascotas WHERE Nombre = ? AND Propietario_DNI = ?"
            cursor.execute(query, (mascota[0], mascota[5]))  # Usamos el nombre y DNI del propietario para verificar existencia
            if not cursor.fetchone():  # Si no existe, insertamos
                cursor.execute(""" 
                    INSERT INTO T_Mascotas (Nombre, Especie, Raza, FecNac, Peso, Propietario_DNI)
                    VALUES (?, ?, ?, ?, ?, ?);
                """, mascota)
                print(f"✔️ Mascota {mascota[0]} insertada.")
            else:
                print(f"⚠️ Mascota {mascota[0]} con DNI de propietario {mascota[5]} ya existe, no se insertó.")

        # Verificar si las visitas ya existen antes de insertarlas
        for visita in datos_visitas:
            query = "SELECT 1 FROM T_Visitas WHERE Fecha = ? AND Mascota_Id = ?"
            cursor.execute(query, (visita[0], visita[3]))  # Usamos la fecha y el ID de mascota para verificar existencia
            if not cursor.fetchone():  # Si no existe, insertamos
                cursor.execute(""" 
                    INSERT INTO T_Visitas (Fecha, Motivo, Tratamiento, Mascota_Id, Propietario_DNI)
                    VALUES (?, ?, ?, ?, ?);
                """, visita)
                print(f"✔️ Visita para mascota ID {visita[3]} insertada.")
            else:
                print(f"⚠️ Visita para mascota ID {visita[3]} en la fecha {visita[0]} ya existe, no se insertó.")

        # Verificar si las facturas ya existen antes de insertarlas
        for factura in datos_facturas:
            query = "SELECT 1 FROM T_Facturas WHERE Fecha = ? AND Mascota_Id = ?"
            cursor.execute(query, (factura[0], factura[3]))  # Usamos la fecha y el ID de mascota para verificar existencia
            if not cursor.fetchone():  # Si no existe, insertamos
                cursor.execute(""" 
                    INSERT INTO T_Facturas (Fecha, Importe, Visita_Id, Mascota_Id, Propietario_DNI)
                    VALUES (?, ?, ?, ?, ?);
                """, factura)
                print(f"✔️ Factura para mascota ID {factura[3]} insertada.")
            else:
                print(f"⚠️ Factura para mascota ID {factura[3]} en la fecha {factura[0]} ya existe, no se insertó.")

        conexion.commit()

    except sqlite3.Error as e:
        print(f"❌ Error al insertar datos de ejemplo: {e}")
        conexion.rollback()

def inicializar_base_datos(ruta_bd):
    """
    Inicializa la base de datos creando tablas e insertando datos de ejemplo.
    """
    with ConexionDB(ruta_bd) as conexion:
        crear_tablas(conexion)
        insertar_datos_ejemplo(conexion)
