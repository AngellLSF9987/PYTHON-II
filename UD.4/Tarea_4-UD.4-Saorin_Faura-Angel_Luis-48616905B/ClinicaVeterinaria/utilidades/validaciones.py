import sqlite3
import re
from datetime import datetime
import sys

# Valida fechas en formato DD-MM-AAAA
def validar_fecha(fecha_str):
    try:
        fecha = datetime.strptime(fecha_str, "%d-%m-%Y")
        return fecha.date()
    except ValueError:
        print("Fecha inválida. Introduce la fecha en formato DD-MM-AAAA.")
        return None

# Valida nombres (mascotas, propietarios)
def validar_nombre(nombre):
    if nombre and nombre.isalpha() and len(nombre) <= 50:
        return nombre.capitalize()
    print("Nombre inválido. Asegúrate de usar solo letras y no superar 50 caracteres.")
    return None

# Valida DNI para propietarios
def validar_dni(dni):
    if re.match(r'^\d{8}[A-Z]$', dni):
        return dni
    print("DNI inválido. Asegúrate de usar el formato correcto (8 dígitos seguidos de una letra mayúscula).")
    return None

# Valida direcciones (opcionalmente puedes definir un máximo de caracteres)
def validar_direccion(direccion):
    if direccion and len(direccion) <= 100:
        return direccion
    print("Dirección inválida. Asegúrate de no superar los 100 caracteres.")
    return None

# Valida correos electrónicos
def validar_correo(correo):
    if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', correo):
        return correo
    print("Correo electrónico inválido. Introduce un formato válido.")
    return None

# Valida ID de mascota (números enteros positivos)
def validar_id_mascota(id_mascota):
    if isinstance(id_mascota, int) and id_mascota > 0:
        return id_mascota
    print("ID de mascota inválido. Introduce un número entero positivo.")
    return None

# Valida visitas (motivo y observaciones)
def validar_visita(motivo, observaciones):
    if not motivo or len(motivo) > 100:
        print("Motivo de visita inválido. Asegúrate de no superar 100 caracteres.")
        return None
    if observaciones and len(observaciones) > 250:
        print("Observaciones inválidas. Asegúrate de no superar 250 caracteres.")
        return None
    return motivo, observaciones

# Valida montos de facturas
def validar_monto(monto):
    try:
        monto = float(monto)
        if monto > 0:
            return round(monto, 2)
        else:
            print("El monto debe ser un número positivo.")
    except ValueError:
        print("Monto inválido. Asegúrate de introducir un número.")
    return None

# Validación general para IDs
def validar_id(id_value, entity_name="elemento"):
    if isinstance(id_value, int) and id_value > 0:
        return id_value
    print(f"ID de {entity_name} inválido. Debe ser un número entero positivo.")
    return None

def opcion_no_valida():
    """
    Función que muestra un mensaje indicando que la opción seleccionada no es válida.
    """
    print("Opción no válida. Por favor, intenta de nuevo.")

def salir():
    """
    Función para salir del sistema o cerrar el menú de manera segura.
    """
    print("Saliendo... ¡Hasta luego!")
    sys.exit()  # Finaliza el programa

def listar_tablas(conexion):
    cursor = conexion.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tablas = cursor.fetchall()
    print("Tablas existentes:", tablas)

def verificar_tablas(conexion):
    cursor = conexion.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tablas = cursor.fetchall()
    print("Tablas existentes:", tablas)

# Funciones para eliminar duplicados en tablas

def eliminar_duplicados_mascotas(conexion, tabla, campo):
    """
    Elimina registros duplicados de la tabla 'tabla' basándose en el campo 'campo'.
    Mantiene el registro con el ID más bajo.
    """
    cursor = conexion.cursor()
    
    # Encuentra duplicados en la tabla
    cursor.execute(f"""
        SELECT MIN(IdMascota), Nombre, Especie, Raza, FecNac, Peso, DNIPropietario
        FROM {tabla}
        GROUP BY Nombre, Especie, Raza, FecNac, Peso, DNIPropietario
        HAVING COUNT(*) > 1
    """)
    duplicados = cursor.fetchall()

    for duplicado in duplicados:
        # Obtiene los IDs de los duplicados
        cursor.execute(f"""
            SELECT IdMascota
            FROM {tabla}
            WHERE Nombre = ? AND Especie = ? AND Raza = ? AND FecNac = ? 
            AND Peso = ? AND DNIPropietario = ?
        """, (duplicado[1], duplicado[2], duplicado[3], duplicado[4], duplicado[5], duplicado[6]))
        
        ids = cursor.fetchall()
        
        # Mantén el registro con el ID más bajo y elimina los demás
        ids_a_eliminar = [id[0] for id in ids[1:]]  # Elimina todos menos el primero
        for id_mascota in ids_a_eliminar:
            cursor.execute(f"DELETE FROM {tabla} WHERE IdMascota = ?", (id_mascota,))
            print(f"⚠️ Eliminado duplicado: {id_mascota}")
    
    conexion.commit()

def eliminar_duplicados_propietarios(conexion, tabla, campo):
    try:
        # Establecer el cursor usando la conexión pasada como parámetro
        cursor = conexion.cursor()
        
        # Consulta para eliminar duplicados basado en IdPropietario
        query = f"""
        DELETE FROM {tabla}
        WHERE rowid NOT IN (
            SELECT MIN(rowid)
            FROM {tabla}
            GROUP BY {campo}
        );
        """
        cursor.execute(query)
        conexion.commit()  # Confirmar los cambios

        print(f"🔧 Duplicados eliminados en la tabla '{tabla}' según '{campo}'.")
    except Exception as e:
        print(f"⚠️ Error eliminando duplicados: {e}")

def eliminar_duplicados_visitas(conexion, tabla, campo):
    try:
        # Establecer el cursor usando la conexión pasada como parámetro
        cursor = conexion.cursor()
        
        # Consulta para eliminar duplicados basado en IdVisita
        query = f"""
        DELETE FROM {tabla}
        WHERE rowid NOT IN (
            SELECT MIN(rowid)
            FROM {tabla}
            GROUP BY {campo}
        );
        """
        cursor.execute(query)
        conexion.commit()  # Confirmar los cambios

        print(f"🔧 Duplicados eliminados en la tabla '{tabla}' según '{campo}'.")
    except Exception as e:
        print(f"⚠️ Error eliminando duplicados: {e}")
        
def eliminar_duplicados_facturas(conexion, tabla, campo):
    try:
        # Establecer el cursor usando la conexión pasada como parámetro
        cursor = conexion.cursor()
        
        # Consulta para eliminar duplicados basado en IdFactura
        query = f"""
        DELETE FROM {tabla}
        WHERE rowid NOT IN (
            SELECT MIN(rowid)
            FROM {tabla}
            GROUP BY {campo}
        );
        """
        cursor.execute(query)
        conexion.commit()  # Confirmar los cambios

        print(f"🔧 Duplicados eliminados en la tabla '{tabla}' según '{campo}'.")
    except Exception as e:
        print(f"⚠️ Error eliminando duplicados: {e}")
