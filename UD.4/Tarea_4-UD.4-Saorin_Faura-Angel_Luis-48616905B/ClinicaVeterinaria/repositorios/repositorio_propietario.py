import sqlite3
from ClinicaVeterinaria.database.db_connection import ConexionDB

class RepositorioPropietario:
    def __init__(self, conexion: ConexionDB):
        self.conexion = conexion

    def agregar_propietario(self, nombre, apellido1, apellido2, dni, telefono, direccion, email):
        """
        Agrega un nuevo propietario a la base de datos.
        """
        query = """
        INSERT INTO T_Propietarios (Nombre, Apellido1, Apellido2, DNI, Telefono, Direccion, Email)
        VALUES (?, ?, ?, ?, ?, ?, ?);
        """
        try:
            with self.conexion as conn:
                cursor = conn.cursor()
                cursor.execute(query, (nombre, apellido1, apellido2, dni, telefono, direccion, email))
                conn.commit()
                print(f"✅ Propietario agregado con éxito. ID generado: {cursor.lastrowid}")
                return cursor.lastrowid
        except sqlite3.IntegrityError:
            print("⚠️ Error: El DNI ya existe o los datos son inválidos.")
        except sqlite3.Error as e:
            print(f"❌ Error al agregar propietario: {e}")
        return None

    def obtener_propietario(self, id_propietario):
        """
        Obtiene un propietario por su ID.
        """
        query = "SELECT * FROM T_Propietarios WHERE IdPropietario = ?;"
        try:
            with self.conexion as conn:
                cursor = conn.cursor()
                cursor.execute(query, (id_propietario,))
                propietario = cursor.fetchone()
                if propietario:
                    print(f"✅ Propietario con ID {id_propietario} encontrado.")
                    return propietario
                print(f"⚠️ No se encontró un propietario con el ID {id_propietario}.")
        except sqlite3.Error as e:
            print(f"❌ Error al obtener propietario: {e}")
        return None

    def actualizar_propietario(self, propietario):
        """
        Actualiza los datos de un propietario en la base de datos.
        """
        query = """
        UPDATE T_Propietarios
        SET Nombre = ?, Apellido1 = ?, Apellido2 = ?, Telefono = ?, Direccion = ?, Email = ?
        WHERE DNI = ?;
        """
        try:
            with self.conexion as conn:
                cursor = conn.cursor()
                cursor.execute(query, (
                    propietario['Nombre'], propietario['Apellido1'], propietario['Apellido2'],
                    propietario['Telefono'], propietario['Direccion'], propietario['Email'], propietario['DNI']
                ))
                conn.commit()
                print("✅ Propietario actualizado correctamente.")
        except sqlite3.Error as e:
            print(f"❌ Error al actualizar el propietario: {e}")

    def eliminar_propietario(self, dni):
        """
        Elimina un propietario de la base de datos por su DNI.
        """
        query = "DELETE FROM T_Propietarios WHERE DNI = ?;"
        try:
            with self.conexion as conn:
                cursor = conn.cursor()
                cursor.execute(query, (dni,))
                if cursor.rowcount > 0:
                    conn.commit()
                    print(f"✅ Propietario con DNI {dni} eliminado correctamente.")
                else:
                    print(f"⚠️ No se encontró propietario con el DNI {dni}.")
        except sqlite3.Error as e:
            print(f"❌ Error al eliminar propietario: {e}")

    def mostrar_propietarios(self):
        """
        Muestra todos los propietarios en la base de datos.
        """
        query = "SELECT * FROM T_Propietarios;"
        try:
            with self.conexion as conn:
                cursor = conn.cursor()
                cursor.execute(query)
                propietarios = cursor.fetchall()
                if propietarios:
                    print("\n=== Lista de Propietarios ===\n")
                    for propietario in propietarios:
                        print(f"ID: {propietario[0]}, Nombre: {propietario[1]} {propietario[2]} {propietario[3]}, DNI: {propietario[4]}, Teléfono: {propietario[5]}, Dirección: {propietario[6]}, Email: {propietario[7]}")
                else:
                    print("⚠️ No hay propietarios registrados.")
        except sqlite3.Error as e:
            print(f"❌ Error al mostrar propietarios: {e}")

    def buscar_por_dni(self, dni):
        """
        Busca un propietario por su DNI.
        """
        query = "SELECT * FROM T_Propietarios WHERE DNI = ?;"
        try:
            with self.conexion as conn:
                cursor = conn.cursor()
                cursor.execute(query, (dni,))
                propietario = cursor.fetchone()
                if propietario:
                    # Mostrar solo los datos de propietario
                    print(f"✅ Propietario encontrado: ID: {propietario['IdPropietario']}, "
                        f"Nombre: {propietario['Nombre']} {propietario['Apellido1']} {propietario['Apellido2']}, "
                        f"DNI: {propietario['DNI']}, Teléfono: {propietario['Telefono']}, "
                        f"Dirección: {propietario['Direccion']}, Email: {propietario['Email']}")
                    return propietario
                print(f"⚠️ No se encontró un propietario con el DNI {dni}.")
        except sqlite3.Error as e:
            print(f"❌ Error al buscar propietario por DNI: {e}")
        return None



