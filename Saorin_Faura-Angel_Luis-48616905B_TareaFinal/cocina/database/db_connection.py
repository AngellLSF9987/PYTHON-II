# cocina\database\db_connection.py
import os
import sqlite3

class ConexionDB:
    def __init__(self, ruta_bd):
        self.ruta_bd = ruta_bd
        directorio = os.path.dirname(self.ruta_bd)
        if not os.path.exists(directorio):
            os.makedirs(directorio)

    def __enter__(self):
        """
        Inicia la conexión al entrar en el contexto `with`.
        """
        try:
            self.conexion = sqlite3.connect(self.ruta_bd)
            self.conexion.row_factory = sqlite3.Row  # Devuelve resultados como diccionarios.
            print(f"Conexión establecida: {self.ruta_bd}")
            return self.conexion
        except sqlite3.Error as e:
            print(f"Error al conectar con la base de datos: {e}")
            raise

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Cierra la conexión al salir del contexto `with`.
        """
        if hasattr(self, 'conexion') and self.conexion:
            self.conexion.close()
            print("Conexión cerrada.")