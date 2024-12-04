from ClinicaVeterinaria.utilidades.menu import mostrar_menu_principal
from ClinicaVeterinaria.database.db_setup import crear_tablas, insertar_datos_ejemplo, obtener_conexion
from ClinicaVeterinaria.utilidades.validaciones import verificar_tablas, eliminar_duplicados, listar_tablas
if __name__ == "__main__":
    print("=== Bienvenid@ a la Clínica Veterinaria ===")
    
    # Establecer conexión a la base de datos
    conexion = obtener_conexion()
    
    with conexion:  # Asegura que la conexión se cierre correctamente al final
        crear_tablas(conexion)              # Garantiza que las tablas existen
        insertar_datos_ejemplo(conexion)    # Inyección de registros de ejemplo
        
        # Verifica la carga correcta de las tablas
        listar_tablas(conexion)
        verificar_tablas(conexion)
        # mostrar_datos(conexion, "mascotas")
        # mostrar_datos(conexion, "propietarios")
        # mostrar_datos(conexion, "visitas")
        # mostrar_datos(conexion, "facturas")
        
        # Eliminar duplicados en las tablas especificadas
        eliminar_duplicados(conexion, "mascotas", "id")
        eliminar_duplicados(conexion, "propietarios", "dni")
        eliminar_duplicados(conexion, "visitas", "id")
        eliminar_duplicados(conexion, "facturas", "id")
    
    # Ejecutar el menú principal
    while True:
        mostrar_menu_principal()

