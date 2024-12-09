import sqlite3
from ClinicaVeterinaria.database.db_connection import ConexionDB

class RepositorioMascota:
    def __init__(self, conexion: ConexionDB):
        self.conexion = conexion

    def agregar_mascota(self, propietario_dni, nombre, especie, raza, fecnac, peso):
        """
        Agrega una nueva mascota a la base de datos.
        Si el propietario con el DNI proporcionado no existe, lo agrega automáticamente.
        """
        try:
            with self.conexion as conn:
                cursor = conn.cursor()
                
                # Paso 1: Verificar si el propietario existe
                query_propietario = "SELECT DNI FROM T_Propietarios WHERE DNI = ?;"
                cursor.execute(query_propietario, (propietario_dni,))
                propietario = cursor.fetchone()  # Devuelve el primer resultado encontrado

                if propietario is None:
                    # Si no se encuentra el propietario, lo agregamos
                    print(f"⚠️ El propietario con DNI {propietario_dni} no está registrado.")
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
                        cursor.execute(query_insertar_propietario, (nombre, apellido1, apellido2, propietario_dni, telefono, direccion, email))
                        conn.commit()
                        print(f"✅ Propietario agregado con éxito. DNI: {propietario_dni}")
                    else:
                        print("⚠️ No se puede agregar la mascota sin propietario registrado.")
                        return None  # Salir del método si no se desea agregar el propietario

                # Paso 2: Insertar la nueva mascota en la base de datos
                query_mascota = """
                INSERT INTO T_Mascotas (Propietario_DNI, Nombre, Especie, Raza, FecNac, Peso)
                VALUES (?, ?, ?, ?, ?, ?);
                """
                cursor.execute(query_mascota, (propietario_dni, nombre, especie, raza, fecnac, peso))
                conn.commit()

                print(f"✅ Mascota agregada con éxito. ID generado: {cursor.lastrowid}")
                return cursor.lastrowid
        except sqlite3.IntegrityError:
            print("⚠️ Los datos son inválidos o ya existen.")
        except sqlite3.Error as e:
            print(f"❌ Error al agregar mascota: {e}")
        return None

    def obtener_mascota(self, id_mascota):
        """
        Obtiene una mascota de la base de datos por su ID.
        """
        query = "SELECT * FROM T_Mascotas WHERE IdMascota = ?;"
        try:
            with self.conexion as conn:
                cursor = conn.cursor()
                cursor.row_factory = sqlite3.Row  # Configura el cursor para usar diccionarios
                cursor.execute(query, (id_mascota,))
                mascota = cursor.fetchone()
                if mascota:
                    print(f"✅ Mascota encontrada: {mascota['Nombre']}")  # Accede por nombre de columna
                    return mascota
                print(f"⚠️ No se encontró una mascota con el ID {id_mascota}.")
        except sqlite3.Error as e:
            print(f"❌ Error al obtener mascota: {e}")
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
            with self.conexion as conn:
                cursor = conn.cursor()
                cursor.execute(query, (nombre, especie, raza, fecnac, peso, id_mascota))
                if cursor.rowcount > 0:
                    conn.commit()
                    print(f"✅ Mascota con ID {id_mascota} actualizada con éxito.")
                else:
                    print(f"⚠️ No se encontró una mascota con el ID {id_mascota}.")
        except sqlite3.Error as e:
            print(f"❌ Error al actualizar la mascota: {e}")

    def eliminar_mascota(self, id_mascota):
        """
        Elimina una mascota de la base de datos por su ID.
        """
        query = "DELETE FROM T_Mascotas WHERE IdMascota = ?;"
        try:
            with self.conexion as conn:
                cursor = conn.cursor()
                cursor.execute(query, (id_mascota,))
                if cursor.rowcount > 0:
                    conn.commit()
                    print(f"✅ Mascota con ID {id_mascota} eliminada con éxito.")
                else:
                    print(f"⚠️ No se encontró una mascota con el ID {id_mascota}.")
        except sqlite3.Error as e:
            print(f"❌ Error al eliminar mascota: {e}")

    def eliminar_todas_mascotas(conexion, dni_propietario):
        """
        Elimina todas las mascotas asociadas a un propietario dado su DNI.
        """
        cursor = conexion.cursor()
        
        # Buscar todas las mascotas asociadas al DNI
        cursor.execute("""
            SELECT IdMascota FROM T_Mascotas WHERE DNIPropietario = ?
        """, (dni_propietario,))
        
        mascotas = cursor.fetchall()
        
        if mascotas:
            cursor.execute("""
                DELETE FROM T_Mascotas WHERE DNIPropietario = ?
            """, (dni_propietario,))
            conexion.commit()
            print(f"✅ Todas las mascotas del propietario con DNI {dni_propietario} han sido eliminadas.")
        else:
            print(f"⚠️ No se encontraron mascotas asociadas al propietario con DNI {dni_propietario}.")


    def eliminar_mascota_por_id(conexion, id_mascota):
        """
        Elimina una mascota específica según su ID.
        """
        cursor = conexion.cursor()
        
        # Verificar si el ID existe
        cursor.execute("""
            SELECT * FROM T_Mascotas WHERE IdMascota = ?
        """, (id_mascota,))
        mascota = cursor.fetchone()
        
        if mascota:
            cursor.execute("""
                DELETE FROM T_Mascotas WHERE IdMascota = ?
            """, (id_mascota,))
            conexion.commit()
            print(f"✅ La mascota con ID {id_mascota} ha sido eliminada correctamente.")
        else:
            print(f"⚠️ No se encontró una mascota con ID {id_mascota}.")

    def mostrar_mascotas(self):
        """
        Muestra todas las mascotas junto con el DNI de sus propietarios.
        """
        query = "SELECT * FROM T_Mascotas;"
        try:
            with self.conexion as conn:
                cursor = conn.cursor()
                cursor.execute(query)
                mascotas = cursor.fetchall()
                if mascotas:
                    print("\n=== Lista de Mascotas ===\n")
                    for mascota in mascotas:
                        print(f"ID Mascota: {mascota[0]} | Nombre: {mascota[1]} | Especie: {mascota[2]} | Raza: {mascota[3]} | Fecha de Nacimiento: {mascota[4]} | Peso: {mascota[5]} kg | DNI Propietario: {mascota[6]}")
                else:
                    print("⚠️ No hay mascotas registradas en la base de datos.")
        except sqlite3.Error as e:
                print(f"❌ Error al mostrar las mascotas: {e}")

    def buscar_por_dni_de_propietario(self, propietario_DNI):
        query = """
        SELECT * FROM T_Mascotas
        WHERE Propietario_DNI = ?;
        """
        try:
            with self.conexion as conn:
                cursor = conn.cursor()
                cursor.execute(query, (propietario_DNI,))
                mascotas = cursor.fetchall()  # Obtener todas las mascotas del propietario

                if mascotas:
                    print(f"✔️ Mascotas encontradas para el propietario {propietario_DNI}:")
                    for mascota in mascotas:
                        # Acceder a las columnas por nombre
                        id_mascota = mascota["IdMascota"]
                        nombre = mascota["Nombre"]
                        especie = mascota["Especie"]
                        raza = mascota["Raza"]
                        fecnac = mascota["FecNac"]
                        peso = mascota["Peso"]
                        propietario_dni = mascota["Propietario_DNI"]
                        
                        print(f"ID: {id_mascota} | Nombre: {nombre} | Especie: {especie} | Raza: {raza} | Fecha de Nacimiento: {fecnac} | Peso: {peso} | Propietario: {propietario_dni}")
                else:
                    print(f"No se encontraron mascotas para el propietario con DNI {propietario_DNI}.")
        except sqlite3.Error as e:
            print(f"❌ Error al buscar mascotas por DNI de propietario: {e}")

