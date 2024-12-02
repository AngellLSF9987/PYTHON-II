# biblioteca/utilidades/ruta_datos_json.py

# Asegurarnos de que el resultado sea una ruta absoluta
RUTA_DATOS_BIBLIOTECA = r"UD.3\Tarea_UD.3-Saorin-Faura_Angel-Luis_48616905B\datos_biblioteca.json"

# Reemplazar las barras invertidas (\) por barras normales (/)
RUTA_DATOS_BIBLIOTECA = RUTA_DATOS_BIBLIOTECA.replace("\\", "/")

print(f"Ruta calculada: {RUTA_DATOS_BIBLIOTECA}")

# import os

# # Calcula la ruta absoluta basada en el archivo actual
# RUTA_DATOS_BIBLIOTECA = os.path.join(
#     os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
#     "datos_biblioteca.json"
# )