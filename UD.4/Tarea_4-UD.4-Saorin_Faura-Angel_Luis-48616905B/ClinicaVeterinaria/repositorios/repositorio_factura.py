import sqlite3
from ClinicaVeterinaria.database.db_connection import ConexionDB

class RepositorioFactura:
    def __init__(self, conexion: ConexionDB, repo_mascota=None):
        """
        Constructor de RepositorioFactura.
        :param conexion: Objeto de conexión a la base de datos.
        :param repo_mascota: Objeto del repositorio de mascotas.
        """
        self.conexion = conexion
        self.repo_mascota = repo_mascota

    def agregar_factura(self, fecha, importe, visita_id, mascota_id, propietario_dni):
        """
        Agrega una nueva factura a la base de datos.
        """
        query = """
        INSERT INTO T_Facturas (Fecha, Importe, Visita_Id, Mascota_Id, Propietario_DNI)
        VALUES (?, ?, ?, ?, ?);
        """
        try:
            with self.conexion as conn:
                cursor = conn.cursor()
                cursor.execute(query, (fecha, importe, visita_id, mascota_id, propietario_dni))
                conn.commit()
                print(f"✅ Factura agregada con éxito. ID generado: {cursor.lastrowid}")
                return cursor.lastrowid
        except sqlite3.IntegrityError:
            print("⚠️ La visita asociada no existe o los datos son inválidos.")
        except sqlite3.Error as e:
            print(f"❌ Error al agregar factura: {e}")
        return None

    def buscar_facturas_por_dni_propietario(self, dni_propietario):
        """
        Busca las facturas de las mascotas asociadas a un propietario por su DNI.
        """
        query_mascotas = """
            SELECT m.IdMascota, m.Nombre
            FROM T_Mascotas m
            JOIN T_Propietarios p ON m.Propietario_DNI = p.DNI
            WHERE p.DNI = ?;
        """
        query_facturas = """
            SELECT f.IdFactura, f.Fecha, f.Importe, f.Visita_Id, f.Mascota_Id, f.Propietario_DNI
            FROM T_Facturas f
            WHERE f.Mascota_Id = ?;
        """
        
        try:
            with self.conexion as conn:
                cursor = conn.cursor()
                cursor.execute(query_mascotas, (dni_propietario,))
                mascotas = cursor.fetchall()

                if not mascotas:
                    print(f"⚠️ No se encontraron mascotas asociadas al DNI de propietario {dni_propietario}.")
                    return []
                
                facturas = []
                for mascota in mascotas:
                    cursor.execute(query_facturas, (mascota[0],))
                    facturas_mascota = cursor.fetchall()
                    for factura in facturas_mascota:
                        facturas.append({
                            "id_factura": factura[0],
                            "fecha": factura[1],
                            "importe": factura[2],
                            "visita_id": factura[3],
                            "mascota_id": factura[4],
                            "propietario_dni": factura[5],
                            "mascota_nombre": mascota[1]
                        })
                return facturas
        except sqlite3.Error as e:
            print(f"❌ Error al buscar facturas: {e}")
            return []

    def generar_factura(self, fecha, importe, visita_id, mascota_id, propietario_dni):
        query = """
        INSERT INTO T_Facturas (Fecha, Importe, Visita_Id, Mascota_Id, Propietario_DNI)
        VALUES (?, ?, ?, ?, ?);
        """
        try:
            with self.conexion as conn:
                cursor = conn.cursor()
                cursor.execute(query, (fecha, importe, visita_id, mascota_id, propietario_dni))
                conn.commit()
                return cursor.lastrowid
        except sqlite3.Error as e:
            print(f"❌ Error al generar la factura: {e}")
            return None

    def modificar_factura(self, factura_modificada):
        """
        Modifica los datos de una factura en la base de datos.
        :param factura_modificada: Diccionario con los datos actualizados de la factura
        """
        query = """
        UPDATE T_Facturas
        SET Fecha = ?, Importe = ?
        WHERE IdFactura = ?;
        """
        try:
            with self.conexion as conn:
                cursor = conn.cursor()
                cursor.execute(query, (
                    factura_modificada['fecha'],
                    factura_modificada['importe'],
                    factura_modificada['id_factura']
                ))
                conn.commit()
        except sqlite3.Error as e:
            print(f"❌ Error al modificar la factura: {e}")

    def eliminar_factura(self, factura_id):
        """
        Elimina una factura de la base de datos.
        """
        query = """
        DELETE FROM T_Facturas
        WHERE IdFactura = ?;
        """
        try:
            with self.conexion as conn:
                cursor = conn.cursor()
                cursor.execute(query, (factura_id,))
                conn.commit()
                
                if cursor.rowcount > 0:
                    print(f"✅ Factura con ID {factura_id} eliminada con éxito.")
                else:
                    print(f"⚠️ No se encontró factura con ID {factura_id}.")
        except sqlite3.Error as e:
            print(f"❌ Error al eliminar la factura: {e}")

    def mostrar_facturas(self):
        """
        Muestra todas las facturas en la base de datos.
        """
        query = "SELECT * FROM T_Facturas;"
        try:
            with self.conexion as conn:
                cursor = conn.cursor()
                cursor.execute(query)
                facturas = cursor.fetchall()
                if facturas:
                    print("\n=== Lista de Facturas ===")
                    for factura in facturas:
                        print(f"ID: {factura[0]} | Fecha de Emisión: {factura[1]} | Importe: {factura[2]} | Visita: {factura[3]} | Mascota: {factura[4]} | Propietario: {factura[5]}")
                else:
                    print("⚠️ No hay facturas registradas.")
        except sqlite3.Error as e:
            print(f"❌ Error al mostrar facturas: {e}")

    def obtener_facturas(self, id_factura=None):
        """
        Obtiene una factura específica o todas las facturas si no se proporciona un ID.
        """
        try:
            cursor = self.conexion.cursor()
            if id_factura:
                query = "SELECT * FROM T_Facturas WHERE id_factura = ?"
                cursor.execute(query, (id_factura,))
            else:
                query = "SELECT * FROM T_Facturas"
                cursor.execute(query)
            facturas = cursor.fetchall()
            return facturas
        except Exception as e:
            print(f"Error al obtener facturas: {e}")
            return None