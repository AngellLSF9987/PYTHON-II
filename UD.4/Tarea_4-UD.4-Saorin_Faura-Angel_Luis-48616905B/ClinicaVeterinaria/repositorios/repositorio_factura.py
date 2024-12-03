import sqlite3
from ClinicaVeterinaria.database.db_connection import ConexionDB

class RepositorioFactura:
    def __init__(self, conexion: ConexionDB):
        self.db = conexion

    def agregar_factura(self, id_visita, fecha_emision, importe, descripcion):
        """
        Agrega una nueva factura a la base de datos.
        """
        query = """
        INSERT INTO T_Facturas (IdVisita, FechaEmision, Importe, Descripcion)
        VALUES (?, ?, ?, ?);
        """
        try:
            with self.db.conectar() as conn:
                cursor = conn.cursor()
                cursor.execute(query, (id_visita, fecha_emision, importe, descripcion))
                conn.commit()
                print(f"✅ Factura agregada con éxito. ID generado: {cursor.lastrowid}")
                return cursor.lastrowid
        except sqlite3.IntegrityError:
            print("⚠️ Error: La visita asociada no existe o los datos son inválidos.")
        except sqlite3.Error as e:
            print(f"⚠️ Error al agregar factura: {e}")
        return None

    def obtener_factura(self, id_factura):
        """
        Obtiene una factura por su ID.
        """
        query = "SELECT * FROM T_Facturas WHERE IdFactura = ?;"
        try:
            with self.db.conectar() as conn:
                cursor = conn.cursor()
                cursor.execute(query, (id_factura,))
                factura = cursor.fetchone()
                if factura:
                    print(f"✅ Factura encontrada: {factura}")
                    return factura
                print(f"⚠️ No se encontró una factura con el ID {id_factura}.")
        except sqlite3.Error as e:
            print(f"⚠️ Error al obtener factura: {e}")
        return None

    def actualizar_factura(self, id_factura, id_visita, fecha_emision, importe, descripcion):
        """
        Actualiza los datos de una factura en la base de datos.
        """
        query = """
        UPDATE T_Facturas
        SET IdVisita = ?, FechaEmision = ?, Importe = ?, Descripcion = ?
        WHERE IdFactura = ?;
        """
        try:
            with self.db.conectar() as conn:
                cursor = conn.cursor()
                cursor.execute(query, (id_visita, fecha_emision, importe, descripcion, id_factura))
                if cursor.rowcount > 0:
                    conn.commit()
                    print(f"✅ Factura con ID {id_factura} actualizada con éxito.")
                else:
                    print(f"⚠️ No se encontró una factura con el ID {id_factura}.")
        except sqlite3.Error as e:
            print(f"⚠️ Error al actualizar factura: {e}")

    def eliminar_factura(self, id_factura):
        """
        Elimina una factura de la base de datos por su ID.
        """
        query = "DELETE FROM T_Facturas WHERE IdFactura = ?;"
        try:
            with self.db.conectar() as conn:
                cursor = conn.cursor()
                cursor.execute(query, (id_factura,))
                if cursor.rowcount > 0:
                    conn.commit()
                    print(f"✅ Factura con ID {id_factura} eliminada con éxito.")
                else:
                    print(f"⚠️ No se encontró una factura con el ID {id_factura}.")
        except sqlite3.Error as e:
            print(f"⚠️ Error al eliminar factura: {e}")

    def mostrar_facturas(self):
        """
        Muestra todas las facturas en la base de datos.
        """
        query = "SELECT * FROM T_Facturas;"
        try:
            with self.db.conectar() as conn:
                cursor = conn.cursor()
                cursor.execute(query)
                facturas = cursor.fetchall()
                if facturas:
                    print("\n=== Lista de Facturas ===")
                    for factura in facturas:
                        print(f"ID: {factura[0]}, IdVisita: {factura[1]}, Fecha de Emisión: {factura[2]}, Importe: {factura[3]}, Descripción: {factura[4]}")
                else:
                    print("⚠️ No hay facturas registradas.")
        except sqlite3.Error as e:
            print(f"⚠️ Error al mostrar facturas: {e}")
