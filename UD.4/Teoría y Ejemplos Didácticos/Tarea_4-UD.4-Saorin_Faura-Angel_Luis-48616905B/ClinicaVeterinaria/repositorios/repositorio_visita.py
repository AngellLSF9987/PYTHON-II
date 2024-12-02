import sqlite3
from ClinicaVeterinaria.database.db_connection import ConexionDB

class RepositorioVisita:
    def __init__(self, conexion: ConexionDB):
        self.db = conexion  

    def agregar_visita(self, id_mascota, fecha, motivo, observaciones):
        """
        Agrega una nueva visita a la base de datos.
        """
        query = """
        INSERT INTO T_Visitas (MascotaID, Fecha, Motivo, Observaciones)
        VALUES (?, ?, ?, ?);
        """
        try:
            with self.db.conectar() as conn:
                cursor = conn.cursor()
                cursor.execute(query, (id_mascota, fecha, motivo, observaciones))
                conn.commit()
                print(f"Visita agregada con éxito. ID generado: {cursor.lastrowid}")
                return cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error al agregar visita: {e}")
        return None

    def obtener_visita(self, id_visita):
        """
        Obtiene una visita por su ID.
        """
        query = "SELECT * FROM T_Visitas WHERE ID = ?;"
        try:
            with self.db.conectar() as conn:
                cursor = conn.cursor()
                cursor.execute(query, (id_visita,))
                visita = cursor.fetchone()
                if visita:
                    return visita
                print(f"No se encontró una visita con el ID {id_visita}.")
        except sqlite3.Error as e:
            print(f"Error al obtener visita: {e}")
        return None

    def actualizar_visita(self, id_visita, id_mascota, fecha, motivo, observaciones):
        """
        Actualiza los datos de una visita en la base de datos.
        """
        query = """
        UPDATE T_Visitas
        SET IdMascota = ?, Fecha = ?, Motivo = ?, Observaciones = ?
        WHERE ID = ?;
        """
        try:
            with self.db.conectar() as conn:
                cursor = conn.cursor()
                cursor.execute(query, (id_mascota, fecha, motivo, observaciones, id_visita))
                if cursor.rowcount == 0:
                    print(f"No se encontró una visita con el ID {id_visita}.")
                else:
                    conn.commit()
                    print("Visita actualizada con éxito.")
        except sqlite3.Error as e:
            print(f"Error al actualizar visita: {e}")

    def eliminar_visita(self, id_visita):
        """
        Elimina una visita de la base de datos por su ID.
        """
        query = "DELETE FROM T_Visitas WHERE ID = ?;"
        try:
            with self.db.conectar() as conn:
                cursor = conn.cursor()
                cursor.execute(query, (id_visita,))
                if cursor.rowcount == 0:
                    print(f"No se encontró una visita con el ID {id_visita}.")
                else:
                    conn.commit()
                    print("Visita eliminada con éxito.")
        except sqlite3.Error as e:
            print(f"Error al eliminar visita: {e}")
