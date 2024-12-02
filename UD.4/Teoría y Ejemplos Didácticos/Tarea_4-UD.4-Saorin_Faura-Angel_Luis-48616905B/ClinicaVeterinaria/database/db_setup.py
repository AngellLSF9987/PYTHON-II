from database.db_connection import ConexionDB

def crear_tablas():
    db = ConexionDB()
    conexion = db.conectar()
    cursor = conexion.cursor()

    # Crear tablas
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS T_Propietario (
        IdPropietario INTEGER PRIMARY KEY AUTOINCREMENT,
        Nombre TEXT NOT NULL,
        DNI TEXT UNIQUE NOT NULL,
        FechaNacimiento DATE NOT NULL,
        Direccion TEXT,
        CorreoElectronico TEXT
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS T_Mascotas (
        IdMascota INTEGER PRIMARY KEY AUTOINCREMENT,
        IdPropietario INTEGER NOT NULL,
        Nombre TEXT NOT NULL,
        Tipo TEXT NOT NULL,
        Raza TEXT,
        FechaNacimiento DATE,
        Peso REAL,
        Color TEXT,
        Notas TEXT,
        FOREIGN KEY (IdPropietario) REFERENCES T_Propietario(IdPropietario)
    );
    """)

    conexion.commit()
    conexion.close()

if __name__ == "__main__":
    crear_tablas()
