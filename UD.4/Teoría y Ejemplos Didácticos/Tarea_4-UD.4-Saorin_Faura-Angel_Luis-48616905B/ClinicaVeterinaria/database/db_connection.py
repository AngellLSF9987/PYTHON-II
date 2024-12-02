import sqlite3

class ConexionDB:
    def __init__(self, ruta_bd="clinica_veterinaria.db"):
        self.ruta_bd = ruta_bd

    def conectar(self):
        try:
            conn = sqlite3.connect(self.ruta_bd)
            return conn
        except sqlite3.Error as e:
            print(f"Error al conectar con la base de datos: {e}")
            return None
