import os
import sqlite3

class ConexionDB:
    def __init__(self, ruta_bd):
        self.ruta_bd = ruta_bd
        # Verificar si la carpeta de la base de datos existe; si no, crearla
        directorio = os.path.dirname(self.ruta_bd)
        if not os.path.exists(directorio):
            os.makedirs(directorio)  # Crear el directorio si no existe
    
    def conectar(self):
        try:
            print(f"Conectando a la base de datos en: {self.ruta_bd}")
            conexion = sqlite3.connect(self.ruta_bd)
            return conexion
        except sqlite3.OperationalError as e:
            print(f"Error al conectar con la base de datos: {e}")
            raise
