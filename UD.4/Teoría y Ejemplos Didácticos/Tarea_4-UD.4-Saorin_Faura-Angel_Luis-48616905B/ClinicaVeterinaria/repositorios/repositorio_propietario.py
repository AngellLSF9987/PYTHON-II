import sqlite3
from ClinicaVeterinaria.database.db_connection import ConexionDB

class RepositorioPropietario:
    def __init__(self, conexion: ConexionDB):
        self.db = conexion  

    def agregar_propietario(self, nombre, dni, fecha_nacimiento, direccion, correo):
        """
        Agrega un nuevo propietario a la base de datos.
        """
        query = """
        INSERT INTO T_Propietarios (Nombre, DNI, FechaNacimiento, Direccion, CorreoElectronico)
        VALUES (?, ?, ?, ?, ?);
        """
        try:
            with self.db.conectar() as conn:
                cursor = conn.cursor()
                cursor.execute(query, (nombre, dni, fecha_nacimiento, direccion, correo))
                conn.commit()
                print(f"Propietario agregado con éxito. ID generado: {cursor.lastrowid}")
                return cursor.lastrowid
        except sqlite3.IntegrityError:
            print("Error: El DNI ya existe o los datos son inválidos.")
        except sqlite3.Error as e:
            print(f"Error al agregar propietario: {e}")
        return None

    def obtener_propietario(self, id_propietario):
        """
        Obtiene un propietario por su ID.
        """
        query = "SELECT * FROM T_Propietarios WHERE ID = ?;"
        try:
            with self.db.conectar() as conn:
                cursor = conn.cursor()
                cursor.execute(query, (id_propietario,))
                propietario = cursor.fetchone()
                if propietario:
                    return propietario
                print(f"No se encontró un propietario con el ID {id_propietario}.")
        except sqlite3.Error as e:
            print(f"Error al obtener propietario: {e}")
        return None

    def actualizar_propietario(self, id_propietario, nombre, dni, fecha_nacimiento, direccion, correo):
        """
        Actualiza los datos de un propietario en la base de datos.
        """
        query = """
        UPDATE T_Propietarios
        SET Nombre = ?, DNI = ?, FechaNacimiento = ?, Direccion = ?, CorreoElectronico = ?
        WHERE ID = ?;
        """
        try:
            with self.db.conectar() as conn:
                cursor = conn.cursor()
                cursor.execute(query, (nombre, dni, fecha_nacimiento, direccion, correo, id_propietario))
                if cursor.rowcount == 0:
                    print(f"No se encontró un propietario con el ID {id_propietario}.")
                else:
                    conn.commit()
                    print("Propietario actualizado con éxito.")
        except sqlite3.IntegrityError:
            print("Error: El DNI proporcionado ya está en uso por otro propietario.")
        except sqlite3.Error as e:
            print(f"Error al actualizar propietario: {e}")

    def eliminar_propietario(self, id_propietario):
        """
        Elimina un propietario de la base de datos por su ID.
        """
        query = "DELETE FROM T_Propietarios WHERE ID = ?;"
        try:
            with self.db.conectar() as conn:
                cursor = conn.cursor()
                cursor.execute(query, (id_propietario,))
                if cursor.rowcount == 0:
                    print(f"No se encontró un propietario con el ID {id_propietario}.")
                else:
                    conn.commit()
                    print("Propietario eliminado con éxito.")
        except sqlite3.Error as e:
            print(f"Error al eliminar propietario: {e}")

    def mostrar_propietarios(self):
        """
        Muestra todos los propietarios en la base de datos.
        """
        query = "SELECT * FROM T_Propietarios;"
        try:
            with self.db.conectar() as conn:
                cursor = conn.cursor()
                cursor.execute(query)
                propietarios = cursor.fetchall()
                if propietarios:
                    print("\n=== Lista de Propietarios ===")
                    for propietario in propietarios:
                        print(f"ID: {propietario[0]}, Nombre: {propietario[1]}, DNI: {propietario[2]}, Dirección: {propietario[3]}")
                else:
                    print("No hay propietarios registrados.")
        except sqlite3.Error as e:
            print(f"Error al mostrar propietarios: {e}")