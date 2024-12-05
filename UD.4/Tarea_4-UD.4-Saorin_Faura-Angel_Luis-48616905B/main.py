from ClinicaVeterinaria.utilidades.menu import mostrar_menu_principal
from ClinicaVeterinaria.database.db_setup import crear_tablas, insertar_datos_ejemplo
from ClinicaVeterinaria.database.db_connection import ConexionDB
from ClinicaVeterinaria.utilidades.validaciones import (
    verificar_tablas, 
    listar_tablas, 
    eliminar_duplicados_mascotas, 
    eliminar_duplicados_propietarios, 
    eliminar_duplicados_visitas, 
    eliminar_duplicados_facturas
)

if __name__ == "__main__":
    print("=== Bienvenid@ a la Clínica Veterinaria ===")

    # Ruta a la base de datos
    db_path = r"UD.4\Tarea_4-UD.4-Saorin_Faura-Angel_Luis-48616905B\ClinicaVeterinaria\database\clinica_veterinaria.db"
    
    # Inicializar conexión a la base de datos
    db = ConexionDB(db_path)

    with db.conectar() as conexion:  # Asegura que la conexión se cierre correctamente al final
        # Crear tablas necesarias
        crear_tablas(conexion)

        # Insertar datos de ejemplo
        insertar_datos_ejemplo(conexion)
        
        # Verificar tablas y eliminar duplicados
        listar_tablas(conexion)
        verificar_tablas(conexion)
        eliminar_duplicados_mascotas(conexion, "T_Mascotas", "IdMascota")
        eliminar_duplicados_propietarios(conexion, "T_Propietarios", "DNI")
        eliminar_duplicados_visitas(conexion, "T_Visitas", "IdVisita")
        eliminar_duplicados_facturas(conexion, "T_Facturas", "IdFactura")

    # Ejecutar el menú principal
    while True:
        mostrar_menu_principal()
