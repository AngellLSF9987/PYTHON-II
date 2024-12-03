import os
import sqlite3

class ConexionDB:
    def __init__(self, ruta_bd=None):
        if ruta_bd is None:
            # Obtener la ruta del directorio donde está el script actual (main.py)
            ruta_base = os.path.join(
                os.path.dirname(os.path.abspath(__file__)),  # Obtiene la ruta del archivo main.py
                "database"  # Añadir el subdirectorio 'database'
            )
            # Crear la carpeta `database` si no existe
            if not os.path.exists(ruta_base):
                os.makedirs(ruta_base)
            # Archivo de la base de datos en `database/`
            ruta_bd = os.path.join(ruta_base, "clinica_veterinaria.db")
        self.ruta_bd = ruta_bd

    def conectar(self):
        """
        Establece una conexión a la base de datos SQLite.
        """
        try:
            conn = sqlite3.connect(self.ruta_bd)
            print(f"Conectado a la base de datos en: {self.ruta_bd}")
            return conn
        except sqlite3.Error as e:
            print(f"Error al conectar con la base de datos: {e}")
            return None
