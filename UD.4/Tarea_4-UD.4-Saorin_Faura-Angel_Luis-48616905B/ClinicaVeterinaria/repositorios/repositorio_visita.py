import sqlite3
from ClinicaVeterinaria.database.db_connection import ConexionDB

class RepositorioVisita:
    def __init__(self, conexion: ConexionDB):
        self.conexion = conexion

    def agregar_visita(self, mascota_id, fecha, motivo, tratamiento):
        """
        Agrega una nueva visita a la base de datos.
        """
        query = """
        INSERT INTO T_Visitas (Mascota_Id, Fecha, Motivo, Tratamiento)
        VALUES (?, ?, ?, ?);
        """
        try:
            with self.conexion as conn:
                cursor = conn.cursor()
                cursor.execute(query, (mascota_id, fecha, motivo, tratamiento))
                conn.commit()
                print(f"✅ Visita agregada con éxito. ID generado: {cursor.lastrowid}")
                return cursor.lastrowid
        except sqlite3.Error as e:
            print(f"❌ Error al agregar visita: {e}")
        return None

    def obtener_visita(self, id_visita):
        """
        Obtiene una visita por su ID.
        """
        query = "SELECT * FROM T_Visitas WHERE IdVisita = ?;"
        try:
            with self.conexion as conn:
                cursor = conn.cursor()
                cursor.execute(query, (id_visita,))
                visita = cursor.fetchone()
                if visita:
                    print(f"✅ Visita encontrada")
                    # Formatear la visita como diccionario si es necesario
                    columns = [col[0] for col in cursor.description]
                    return dict(zip(columns, visita))
                print(f"⚠️ No se encontró una visita con el ID {id_visita}.")
        except sqlite3.Error as e:
            print(f"❌ Error al obtener visita: {e}")
        return None
    
    def obtener_visita_completa(self, id_visita):
        """
        Obtiene una visita completa (incluyendo información de la mascota y el propietario) por su ID.
        """
        query = """
        SELECT 
            v.IdVisita, v.Fecha, v.Motivo, v.Tratamiento,
            m.IdMascota, 
            p.DNI
        FROM T_Visitas v
        JOIN T_Mascotas m ON v.Mascota_Id = m.IdMascota
        JOIN T_Propietarios p ON m.Propietario_DNI = p.DNI
        WHERE v.IdVisita = ?;
        """
        try:
            with self.conexion as conn:
                cursor = conn.cursor()
                cursor.execute(query, (id_visita,))
                visita = cursor.fetchone()
                if visita:
                    print(f"✅ Visita completa encontrada")
                    columns = [col[0] for col in cursor.description]
                    return dict(zip(columns, visita))
                print(f"⚠️ No se encontró una visita completa con el ID {id_visita}.")
        except sqlite3.Error as e:
            print(f"❌ Error al obtener visita completa: {e}")
        return None

    def obtener_todas_visitas_completas(self):
        """
        Obtiene todas las visitas con información de mascotas y propietarios.
        """
        query = """
        SELECT 
            v.IdVisita, v.Fecha, v.Motivo, v.Tratamiento, 
            m.IdMascota, 
            p.DNI
        FROM T_Visitas v
        JOIN T_Mascotas m ON v.Mascota_Id = m.IdMascota
        JOIN T_Propietarios p ON m.Propietario_DNI = p.DNI;
        """
        try:
            with self.conexion as conn:
                cursor = conn.cursor()
                cursor.execute(query)
                visitas = cursor.fetchall()
                if visitas:
                    print(f"✅ Todas las visitas obtenidas con éxito")
                    columns = [col[0] for col in cursor.description]
                    return [dict(zip(columns, visita)) for visita in visitas]
                print(f"⚠️ No hay visitas registradas.")
        except sqlite3.Error as e:
            print(f"❌ Error al obtener todas las visitas completas: {e}")
        return []

    def actualizar_visita(self, fecha, motivo, tratamiento, id_visita):
        """
        Actualiza los datos de una visita en la base de datos.
        """
        query = """
        UPDATE T_Visitas
        SET Fecha = ?, Motivo = ?, Tratamiento = ?
        WHERE IdVisita = ?;
        """
        try:
            with self.conexion as conn:
                cursor = conn.cursor()
                cursor.execute(query, (fecha, motivo, tratamiento, id_visita))
                if cursor.rowcount > 0:
                    conn.commit()
                    print(f"✅ Visita con ID {id_visita} actualizada con éxito.")
                else:
                    print(f"⚠️ No se encontró una visita con el ID {id_visita}.")
        except sqlite3.Error as e:
            print(f"❌ Error al actualizar visita: {e}")

    def eliminar_visita(self, id_visita):
        """
        Elimina una visita de la base de datos por su ID.
        """
        query = "DELETE FROM T_Visitas WHERE IdVisita = ?;"
        try:
            with self.conexion as conn:
                cursor = conn.cursor()
                cursor.execute(query, (id_visita,))
                if cursor.rowcount > 0:
                    conn.commit()
                    print(f"✅ Visita con ID {id_visita} eliminada con éxito.")
                else:
                    print(f"⚠️ No se encontró una visita con el ID {id_visita}.")
        except sqlite3.Error as e:
            print(f"❌ Error al eliminar visita: {e}")

    def mostrar_visitas(self):
        """
        Muestra todas las Visitas junto con el DNI del cliente propietario.
        """
        query = "SELECT * FROM T_Visitas;"
        try:
            with self.conexion as conn:
                cursor = conn.cursor()
                cursor.execute(query)
                visitas = cursor.fetchall()
                if visitas:
                    print("\n=== Lista de Visitas ===\n")
                    for visita in visitas:
                        print(f"ID Visita: {visita[0]} | Fecha Visita: {visita[1]} | Motivo Visita: {visita[2]} | Tratamiento: {visita[3]} | Mascota: {visita[4]} | Propietario: {visita[5]}")
                else:
                    print("⚠️ No hay visitas registradas en la base de datos.")
        except sqlite3.Error as e:
                print(f"❌ Error al mostrar las visitas: {e}")

    def buscar_visitas_por_dni_propietario(self, dni_propietario):
        """
        Busca las visitas de las mascotas asociadas a un propietario por su DNI.
        """
        query_mascotas = """
            SELECT m.IdMascota, m.Nombre
            FROM T_Mascotas m
            JOIN T_Propietarios p ON m.Propietario_DNI = p.DNI
            WHERE p.DNI = ?;
        """
        query_visitas = """
            SELECT v.IdVisita, v.Fecha, v.Motivo, v.Tratamiento
            FROM T_Visitas v
            WHERE v.Mascota_Id = ?
        """
        try:
            # 'with' garantiza el manejo adecuado del cursor y la conexión
            with self.conexion as conn:
                cursor = conn.cursor()
                
                # Buscar las mascotas del propietario con el DNI dado
                cursor.execute(query_mascotas, (dni_propietario,))
                mascotas = cursor.fetchall()

                if not mascotas:
                    print(f"⚠️ No se encontraron mascotas asociadas al DNI de propietario {dni_propietario}.")
                    return []

                visitas = []
                # Buscar las visitas de las mascotas obtenidas
                for mascota in mascotas:
                    cursor.execute(query_visitas, (mascota[0],))  # mascota[0] es el IdMascota
                    visitas_mascota = cursor.fetchall()

                    for visita in visitas_mascota:
                        visitas.append({
                            "id_visita": visita[0],
                            "fecha": visita[1],
                            "motivo": visita[2],
                            "tratamiento": visita[3],
                            "mascota_id": mascota[0],
                            "mascota_nombre": mascota[1]
                        })
                
                return visitas

        except sqlite3.Error as e:
            print(f"❌ Error al buscar visitas: {e}")
            return []
