import os
import sqlite3
class ConexionDB:
    def __init__(self, ruta_bd=None):
        if ruta_bd is None:
            ruta_bd = os.path.join(
                os.getcwd(),
                "Tarea_4-UD.4-Saorin_Faura-Angel_Luis-48616905B",
                "clinica_veterinaria.db"
            )
        self.ruta_bd = ruta_bd

    def conectar(self):
        try:
            conn = sqlite3.connect(self.ruta_bd)
            return conn
        except sqlite3.Error as e:
            print(f"Error al conectar con la base de datos: {e}")
            return None