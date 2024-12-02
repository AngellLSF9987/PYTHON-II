import sqlite3
from ClinicaVeterinaria.database.db_connection import ConexionDB

class RepositorioMascota:
    def __init__(self, conexion: ConexionDB):
        self.db = conexion  

    def agregar_mascota(self, nombre, especie, raza, fecha_nacimiento, id_propietario):
        """
        Agrega una nueva mascota a la base de datos.
        """
        query = """
        INSERT INTO T_Mascota (Nombre, Especie, Raza, FechaNacimiento, IdPropietario)
        VALUES (?, ?, ?, ?, ?);
        """
        try:
            with self.db.conectar() as conn:
                cursor = conn.cursor()
                cursor.execute(query, (nombre, especie, raza, fecha_nacimiento, id_propietario))
                conn.commit()
                print("Mascota agregada con éxito.")
        except sqlite3.IntegrityError:
            print("Error: El propietario no existe o los datos son inválidos.")
        except sqlite3.Error as e:
            print(f"Error al agregar mascota: {e}")

    def obtener_mascota(self, id_mascota):
        """
        Obtiene una mascota de la base de datos por su ID.
        """
        query = "SELECT * FROM T_Mascota WHERE ID = ?;"
        try:
            with self.db.conectar() as conn:
                cursor = conn.cursor()
                cursor.execute(query, (id_mascota,))
                mascota = cursor.fetchone()
                if mascota:
                    return mascota
                print(f"No se encontró una mascota con el ID {id_mascota}.")
        except sqlite3.Error as e:
            print(f"Error al obtener mascota: {e}")
        return None

    def actualizar_mascota(self, id_mascota, nombre, especie, raza, fecha_nacimiento, id_propietario):
        """
        Actualiza la información de una mascota en la base de datos.
        """
        query = """
        UPDATE T_Mascota
        SET Nombre = ?, Especie = ?, Raza = ?, FechaNacimiento = ?, IdPropietario = ?
        WHERE ID = ?;
        """
        try:
            with self.db.conectar() as conn:
                cursor = conn.cursor()
                cursor.execute(query, (nombre, especie, raza, fecha_nacimiento, id_propietario, id_mascota))
                if cursor.rowcount == 0:
                    print(f"No se encontró una mascota con el ID {id_mascota}.")
                else:
                    conn.commit()
                    print("Mascota actualizada con éxito.")
        except sqlite3.Error as e:
            print(f"Error al actualizar mascota: {e}")

    def eliminar_mascota(self, id_mascota):
        """
        Elimina una mascota de la base de datos por su ID.
        """
        query = "DELETE FROM T_Mascota WHERE ID = ?;"
        try:
            with self.db.conectar() as conn:
                cursor = conn.cursor()
                cursor.execute(query, (id_mascota,))
                if cursor.rowcount == 0:
                    print(f"No se encontró una mascota con el ID {id_mascota}.")
                else:
                    conn.commit()
                    print("Mascota eliminada con éxito.")
        except sqlite3.Error as e:
            print(f"Error al eliminar mascota: {e}")
