import sqlite3
from ClinicaVeterinaria.database.db_connection import ConexionDB

class RepositorioMascota:
    def __init__(self, conexion: ConexionDB):
        self.db = conexion

    def agregar_mascota(self, dni_propietario, nombre, especie, raza, fecnac, peso):
        """
        Agrega una nueva mascota a la base de datos.
        Si el propietario con el DNI proporcionado no existe, lo agrega.
        """
        # Paso 1: Verificar si el propietario existe utilizando el DNI
        query_propietario = """
        SELECT DNI FROM T_Propietarios WHERE DNI = ?;
        """
        try:
            with self.db.conectar() as conn:
                cursor = conn.cursor()
                cursor.execute(query_propietario, (dni_propietario,))
                propietario = cursor.fetchone()  # Devuelve el primer resultado encontrado

                # Si no se encuentra el propietario, se solicita agregarlo
                if propietario is None:
                    print(f"⚠️ El propietario con DNI {dni_propietario} no está registrado.")
                    agregar_propietario = input("¿Desea agregarlo? (s/n): ").strip().lower()

                    if agregar_propietario == 's':
                        # Pedir los datos para agregar un nuevo propietario
                        nombre = input("Ingrese el nombre del propietario: ")
                        apellido1 = input("Ingrese el primer apellido: ")
                        apellido2 = input("Ingrese el segundo apellido: ")
                        telefono = input("Ingrese el teléfono de contacto: ")
                        direccion = input("Ingrese la dirección del propietario: ")
                        email = input("Ingrese el email del propietario: ")
                        # Insertar el nuevo propietario en la base de datos
                        query_insertar_propietario = """
                        INSERT INTO T_Propietarios (Nombre, Apellido1, Apellido2, DNI, Telefono, Direccion, Email)
                        VALUES (?, ?, ?, ?, ?, ?, ?);
                        """
                        cursor.execute(query_insertar_propietario, (nombre, apellido1, apellido2, dni_propietario, telefono, direccion, email))
                        conn.commit()
                        print(f"✅ Propietario agregado con éxito. DNI: {dni_propietario}")
                    else:
                        print("❌ No se puede agregar la mascota sin propietario registrado.")
                        return None  # Salir del método si el propietario no desea ser agregado

                # Paso 2: Insertar la nueva mascota en la base de datos
                query_mascota = """
                INSERT INTO T_Mascotas (DNIPropietario, Nombre, Especie, Raza, FecNac, Peso)
                VALUES (?, ?, ?, ?, ?, ?);
                """
                cursor.execute(query_mascota, (dni_propietario, nombre, especie, raza, fecnac, peso))
                conn.commit()

                print(f"✅ Mascota agregada con éxito. ID generado: {cursor.lastrowid}")
                return cursor.lastrowid
        except sqlite3.IntegrityError:
            print("⚠️ Error: Los datos son inválidos o ya existen.")
        except sqlite3.Error as e:
            print(f"⚠️ Error al agregar mascota: {e}")
        return None

    def obtener_mascota(self, id_mascota):
        """
        Obtiene una mascota de la base de datos por su ID.
        """
        query = "SELECT * FROM T_Mascotas WHERE IdMascota = ?;"
        try:
            with self.db.conectar() as conn:
                cursor = conn.cursor()
                cursor.execute(query, (id_mascota,))
                mascota = cursor.fetchone()
                if mascota:
                    print(f"✅ Mascota encontrada: {mascota}")
                    return mascota
                print(f"⚠️ No se encontró una mascota con el ID {id_mascota}.")
        except sqlite3.Error as e:
            print(f"⚠️ Error al obtener mascota: {e}")
        return None

    def actualizar_mascota(self, id_mascota, nombre, especie, raza, fecnac, peso):
        """
        Actualiza la información de una mascota en la base de datos.

        :param id_mascota: ID de la mascota a actualizar.
        :param nombre: Nuevo nombre (o actual si no cambia).
        :param especie: Nueva especie (o actual si no cambia).
        :param raza: Nueva raza (o actual si no cambia).
        :param fecnac: Nueva fecha de nacimiento (o actual si no cambia).
        :param peso: Nuevo peso (o actual si no cambia).
        """
        query = """
        UPDATE T_Mascotas
        SET Nombre = ?, Especie = ?, Raza = ?, FecNac = ?, Peso = ?
        WHERE IdMascota = ?;
        """
        try:
            with self.db.conectar() as conn:
                cursor = conn.cursor()
                cursor.execute(query, (nombre, especie, raza, fecnac, peso, id_mascota))
                if cursor.rowcount > 0:
                    conn.commit()
                    print(f"✅ Mascota con ID {id_mascota} actualizada con éxito.")
                else:
                    print(f"⚠️ No se encontró una mascota con el ID {id_mascota}.")
        except sqlite3.Error as e:
            print(f"⚠️ Error al actualizar la mascota: {e}")

    def eliminar_mascota(self, id_mascota):
        """
        Elimina una mascota de la base de datos por su ID.
        """
        query = "DELETE FROM T_Mascotas WHERE IdMascota = ?;"
        try:
            with self.db.conectar() as conn:
                cursor = conn.cursor()
                cursor.execute(query, (id_mascota,))
                if cursor.rowcount > 0:
                    conn.commit()
                    print(f"✅ Mascota con ID {id_mascota} eliminada con éxito.")
                else:
                    print(f"⚠️ No se encontró una mascota con el ID {id_mascota}.")
        except sqlite3.Error as e:
            print(f"⚠️ Error al eliminar mascota: {e}")

    def eliminar_mascota(conexion, dni_propietario):
        """
        Elimina todas las mascotas asociadas a un propietario dado el DNI.
        """
        cursor = conexion.cursor()
        
        # Buscar todas las mascotas asociadas al DNI
        cursor.execute("""
            SELECT IdMascota FROM T_Mascotas WHERE DNIPropietario = ?
        """, (dni_propietario,))
        
        mascotas = cursor.fetchall()
        
        if mascotas:
            print("\n=== Mascotas del Propietario ===")
            for mascota in mascotas:
                print(f"ID Mascota: {mascota[0]}")
            
            # Eliminar las mascotas
            cursor.execute("""
                DELETE FROM T_Mascotas WHERE DNIPropietario = ?
            """, (dni_propietario,))
            conexion.commit()
            print(f"✅ Mascotas del propietario {dni_propietario} eliminadas correctamente.")
        else:
            print(f"⚠️ No se encontraron mascotas para el propietario con DNI: {dni_propietario}")


    def mostrar_mascotas(self):
        """
        Muestra todas las mascotas junto con el DNI de sus propietarios.
        """
        try:
            conexion = self.db.conectar()
            cursor = conexion.cursor()
            cursor.execute("""
                SELECT 
                    m.IdMascota,
                    m.Nombre AS NombreMascota,
                    m.Especie,
                    m.Raza,
                    m.FecNac,
                    m.Peso,
                    p.DNI AS DNIPropietario
                FROM 
                    T_Mascotas AS m
                INNER JOIN 
                    T_Propietarios AS p
                ON 
                    m.DNIPropietario = p.DNI
                ORDER BY 
                    m.IdMascota;
            """)
            resultados = cursor.fetchall()

            if resultados:
                print("\n=== Listado de Mascotas ===")
                for mascota in resultados:
                    print(f"ID Mascota: {mascota[0]} | Nombre: {mascota[1]} | Especie: {mascota[2]} | Raza: {mascota[3]} | Fecha de Nacimiento: {mascota[4]} | Peso: {mascota[5]} kg | DNI Propietario: {mascota[6]}")
            else:
                print("⚠️ No hay mascotas registradas en la base de datos.")

        except sqlite3.Error as e:
            print(f"⚠️ Error al mostrar las mascotas: {e}")
        finally:
            conexion.close()

    def buscar_por_dni_de_propietario(self, dni):
        """
        Busca las mascotas asociadas a un propietario dado su DNI.
        """
        try:
            conexion = self.db.conectar()  # Conectar a la base de datos
            cursor = conexion.cursor()
            cursor.execute("""
                SELECT 
                    m.IdMascota,
                    m.Nombre AS NombreMascota,
                    m.Especie,
                    m.Raza,
                    m.FecNac,
                    m.Peso
                FROM 
                    T_Mascotas AS m
                INNER JOIN 
                    T_Propietarios AS p
                ON 
                    m.DNIPropietario = p.DNI
                WHERE 
                    p.DNI = ?;
            """, (dni,))
            resultados = cursor.fetchall()

            if resultados:
                print("\n=== Mascotas del Propietario ===")
                for mascota in resultados:
                    print(f"ID Mascota: {mascota[0]} | Nombre: {mascota[1]} | Especie: {mascota[2]} | Raza: {mascota[3]} | Fecha de Nacimiento: {mascota[4]} | Peso: {mascota[5]} kg")
            else:
                print(f"⚠️ No se encontraron mascotas para el propietario con DNI {dni}.")

        except sqlite3.Error as e:
            print(f"⚠️ Error al buscar las mascotas por DNI de propietario: {e}")
        finally:
            conexion.close()