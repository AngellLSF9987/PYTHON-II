import sqlite3
from database.db_connection import ConexionDB

class RepositorioPropietario:
    def __init__(self):
        self.db = ConexionDB()

    def agregar_propietario(self, nombre, dni, fecha_nacimiento, direccion, correo):
        query = """
        INSERT INTO T_Propietario (Nombre, DNI, FechaNacimiento, Direccion, CorreoElectronico)
        VALUES (?, ?, ?, ?, ?);
        """
        conn = self.db.conectar()
        try:
            cursor = conn.cursor()
            cursor.execute(query, (nombre, dni, fecha_nacimiento, direccion, correo))
            conn.commit()
            print("Propietario agregado con éxito.")
        except sqlite3.Error as e:
            print(f"Error al agregar propietario: {e}")
        finally:
            conn.close()
