# cocina\database\db_setup.py

from db_connection import ConexionDB
import sqlite3

# class DBSetup:
#     def __init__(self, ruta_bd="database/cocina.db"):
#         """
#         Inicializa la configuración de la base de datos.
#         :param ruta_bd: Ruta al archivo de la base de datos SQLite.
#         """
#         self.ruta_bd = ruta_bd

def crear_tablas(conexion):
        """
        Crea las tablas necesarias para la base de datos de ModaNova.
        """
        with ConexionDB(ruta_bd="database/cocina.db") as conexion:
            cursor = conexion.cursor()
            try:
                # Tabla Roles
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS Rol (
                        id_rol INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre_rol TEXT NOT NULL UNIQUE
                    );
                """)

                # Tabla Usuarios
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS Usuario (
                        id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
                        email TEXT NOT NULL UNIQUE,
                        contrasena TEXT NOT NULL,
                        id_rol INTEGER NOT NULL,
                        id_cliente INTEGER,
                        id_trabajador INTEGER,
                        FOREIGN KEY (id_rol) REFERENCES Rol(id_rol),
                        FOREIGN KEY (id_cliente) REFERENCES Cliente(id_cliente),
                        FOREIGN KEY (id_trabajador) REFERENCES Trabajador(id_trabajador)
                    );
                """)

                # Tabla Cliente
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS Cliente (
                        id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre_cliente TEXT NOT NULL,
                        telefono TEXT,
                        direccion TEXT,
                        fecha_registro DATE DEFAULT CURRENT_DATE
                    );
                """)

                # Tabla Trabajador
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS Trabajador (
                        id_trabajador INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre_trabajador TEXT NOT NULL,
                        telefono TEXT,
                        email TEXT UNIQUE NOT NULL,
                        puesto TEXT NOT NULL,
                        salario REAL
                    );
                """)

                # Tabla Proveedor
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS Proveedor (
                        id_proveedor INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre_proveedor TEXT NOT NULL,
                        contacto TEXT,
                        telefono TEXT NOT NULL,
                        correo TEXT UNIQUE NOT NULL
                    );
                """)
                
                # Tabla Categorias
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS Categoria (
                        id_categoria INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre_categoria TEXT NOT NULL,
                        descripcion TEXT
                    );
                """)
                
                # Tabla Producto
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS Productos (
                        id_producto INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre_producto TEXT NOT NULL,
                        descripcion TEXT,
                        precio REAL NOT NULL,
                        stock INTEGER NOT NULL,
                        id_proveedor INTEGER,
                        id_categoria INTEGER,
                        FOREIGN KEY (id_proveedor) REFERENCES Proveedor(id_proveedor),
                        FOREIGN KEY (id_categoria) REFERENCES Categoria(id_categoria)
                    );
                """)

                # Tabla Venta
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS Ventas (
                        id_venta INTEGER PRIMARY KEY AUTOINCREMENT,
                        fecha DATE DEFAULT CURRENT_DATE,
                        id_cliente INTEGER NOT NULL,
                        total REAL NOT NULL,
                        FOREIGN KEY (id_cliente) REFERENCES Cliente(id_cliente)
                    );
                """)

                # Tabla intermedia Carrito
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS Carrito (
                        id_carrito INTEGER PRIMARY KEY AUTOINCREMENT,
                        id_venta INTEGER NOT NULL,
                        id_producto INTEGER NOT NULL,
                        cantidad INTEGER NOT NULL,
                        precio_unitario REAL NOT NULL,
                        FOREIGN KEY (id_venta) REFERENCES Venta(id_venta),
                        FOREIGN KEY (id_producto) REFERENCES Producto(id_producto)
                    );
                """)


                # Datos iniciales para Roles
                cursor.execute("INSERT OR IGNORE INTO Rol (id_rol, nombre) VALUES (1, 'cliente');")
                cursor.execute("INSERT OR IGNORE INTO Rol (id_rol, nombre) VALUES (2, 'trabajador');")

                conexion.commit()
                print("Tablas creadas exitosamente y datos iniciales añadidos.")
            except sqlite3.Error as e:
                print(f"Error al crear las tablas: {e}")
                conexion.rollback()


def insertar_datos_ejemplo(conexion):
        """
        Inserta datos de ejemplo en las tablas para pruebas iniciales,
        verificando que no haya duplicados.
        """
        with ConexionDB(ruta_bd="database/cocina.db") as conexion:
            cursor = conexion.cursor()
        
            try:
                datos_propietarios = [
                    ("Ana", "Pérez", "Pérez", "12345678A", "600123456", "Calle Luna, 6", "ana@perez.com"),
                    ("Carlos", "López", "López", "87654321B", "610654321", "Calle Sol, 8", "carlos@lopez.com"),
                ]
                datos_mascotas = [
                    ("Firulais", "Perro", "Golden Retriever", "2022-10-10", 40.00, "12345678A"),
                    ("Michi", "Gato", "Siames", "2019-12-12", 8.00, "87654321B"),
                ]
                datos_visitas = [
                    ("2024-12-05", "Vacunación", "Vacunación", 1, "12345678A"),  # 1 es el ID de Firulais
                    ("2024-12-06", "Consulta general", "Consulta general", 2, "87654321B"),  # 2 es el ID de Michi
                ]
                datos_facturas = [
                    ("2024-12-05", 50.00, 1, 1, "12345678A"),  
                    ("2024-12-06", 30.00, 2, 2, "87654321B"),
                ]
            except sqlite3.Error as e:
                print(f"❌ Error al insertar datos de ejemplo: {e}")
                conexion.rollback()
            try:
                
                cursor = conexion.cursor()

                # Verificar si los propietarios ya existen antes de insertarlos
                for propietario in datos_propietarios:
                    query = "SELECT 1 FROM T_Propietarios WHERE DNI = ?"
                    cursor.execute(query, (propietario[3],))  # Usamos el DNI para verificar existencia
                    if not cursor.fetchone():  # Si no existe, insertamos
                        cursor.execute(""" 
                            INSERT INTO T_Propietarios (Nombre, Apellido1, Apellido2, DNI, Telefono, Direccion, Email)
                            VALUES (?, ?, ?, ?, ?, ?, ?);
                        """, propietario)
                        print(f"✔️ Propietario {propietario[0]} {propietario[1]} insertado.")
                    else:
                        print(f"⚠️ Propietario con DNI {propietario[3]} ya existe, no se insertó.")

                # Verificar si las mascotas ya existen antes de insertarlas
                for mascota in datos_mascotas:
                    query = "SELECT 1 FROM T_Mascotas WHERE Nombre = ? AND Propietario_DNI = ?"
                    cursor.execute(query, (mascota[0], mascota[5]))  # Usamos el nombre y DNI del propietario para verificar existencia
                    if not cursor.fetchone():  # Si no existe, insertamos
                        cursor.execute(""" 
                            INSERT INTO T_Mascotas (Nombre, Especie, Raza, FecNac, Peso, Propietario_DNI)
                            VALUES (?, ?, ?, ?, ?, ?);
                        """, mascota)
                        print(f"✔️ Mascota {mascota[0]} insertada.")
                    else:
                        print(f"⚠️ Mascota {mascota[0]} con DNI de propietario {mascota[5]} ya existe, no se insertó.")

                # Verificar si las visitas ya existen antes de insertarlas
                for visita in datos_visitas:
                    query = "SELECT 1 FROM T_Visitas WHERE Fecha = ? AND Mascota_Id = ?"
                    cursor.execute(query, (visita[0], visita[3]))  # Usamos la fecha y el ID de mascota para verificar existencia
                    if not cursor.fetchone():  # Si no existe, insertamos
                        cursor.execute(""" 
                            INSERT INTO T_Visitas (Fecha, Motivo, Tratamiento, Mascota_Id, Propietario_DNI)
                            VALUES (?, ?, ?, ?, ?);
                        """, visita)
                        print(f"✔️ Visita para mascota ID {visita[3]} insertada.")
                    else:
                        print(f"⚠️ Visita para mascota ID {visita[3]} en la fecha {visita[0]} ya existe, no se insertó.")

                # Verificar si las facturas ya existen antes de insertarlas
                for factura in datos_facturas:
                    query = "SELECT 1 FROM T_Facturas WHERE Fecha = ? AND Mascota_Id = ?"
                    cursor.execute(query, (factura[0], factura[3]))  # Usamos la fecha y el ID de mascota para verificar existencia
                    if not cursor.fetchone():  # Si no existe, insertamos
                        cursor.execute(""" 
                            INSERT INTO T_Facturas (Fecha, Importe, Visita_Id, Mascota_Id, Propietario_DNI)
                            VALUES (?, ?, ?, ?, ?);
                        """, factura)
                        print(f"✔️ Factura para mascota ID {factura[3]} insertada.")
                    else:
                        print(f"⚠️ Factura para mascota ID {factura[3]} en la fecha {factura[0]} ya existe, no se insertó.")

                conexion.commit()

            except sqlite3.Error as e:
                print(f"❌ Error al insertar datos de ejemplo: {e}")
                conexion.rollback()

def inicializar_base_datos(ruta_bd="database/cocina.db"):
        """
        Inicializa la base de datos creando tablas e insertando datos de ejemplo.
        """
        with ConexionDB(ruta_bd) as conexion:
            crear_tablas(conexion)
            insertar_datos_ejemplo(conexion)
