from ClinicaVeterinaria.utilidades.validaciones import opcion_no_valida, salir
from ClinicaVeterinaria.repositorios.repositorio_propietario import RepositorioPropietario
from ClinicaVeterinaria.repositorios.repositorio_mascota import RepositorioMascota
from ClinicaVeterinaria.repositorios.repositorio_visita import RepositorioVisita
from ClinicaVeterinaria.repositorios.repositorio_factura import RepositorioFactura
from ClinicaVeterinaria.database.db_connection import ConexionDB

def mostrar_menu_principal():
    """
    Muestra el menú principal de la Clínica Veterinaria y gestiona las opciones.
    """
    # Crear la conexión a la base de datos
    conexion = ConexionDB()

    # Instanciar los repositorios
    repo_propietario = RepositorioPropietario(conexion)
    repo_mascota = RepositorioMascota(conexion)
    repo_visita = RepositorioVisita(conexion)
    repo_factura = RepositorioFactura(conexion)

    # Opciones del menú principal
    opciones = {
        "1": lambda: menu_propietarios(repo_propietario),
        "2": lambda: menu_mascotas(repo_mascota, repo_propietario),
        "3": lambda: menu_visitas(repo_visita, repo_mascota),
        "4": lambda: menu_facturas(repo_factura, repo_visita),
        "0": salir
    }

    while True:
        print("\n- Clínica Veterinaria -\n")
        print("1. Gestión de Propietarios.")
        print("2. Gestión de Mascotas.")
        print("3. Gestión de Visitas.")
        print("4. Gestión de Facturas.")
        print("0. Salir.")

        opcion = input("\nSeleccione una opción:\n")
        accion = opciones.get(opcion, opcion_no_valida)
        accion()

def menu_propietarios(repo_propietario):
    """
    Submenú para la gestión de propietarios.
    """
    while True:
        print("\n- Gestión de Propietarios -\n")
        print("1. Mostrar todos los propietarios.")
        print("2. Buscar propietario por DNI.")
        print("3. Añadir nuevo propietario.")
        print("4. Modificar datos de un propietario.")
        print("5. Eliminar un propietario.")
        print("0. Volver al menú principal.")

        opcion = input("\nSeleccione una opción:\n").strip()
        if opcion == "1":
            repo_propietario.mostrar_propietarios()
        elif opcion == "2":
            dni = input("Ingrese el DNI del propietario:\n").strip()
            repo_propietario.buscar_por_dni(dni)
        elif opcion == "3":
            # Pedir los datos para agregar un nuevo propietario
            nombre = input("Ingrese el nombre del propietario: ")
            apellido1 = input("Ingrese el primer apellido: ")
            apellido2 = input("Ingrese el segundo apellido: ")
            dni = input("Ingrese el DNI del propietario: ")
            telefono = input("Ingrese el teléfono de contacto: ")
            direccion = input("Ingrese la dirección del propietario: ")
            email = input("Ingrese el email del propietario: ")
            repo_propietario.agregar_propietario(nombre, apellido1, apellido2, dni, telefono, direccion, email)
        elif opcion == "4":
            dni = input("Ingrese el DNI del propietario a modificar: ").strip()
            repo_propietario.actualizar_propietario(dni)
        elif opcion == "5":
            dni = input("Ingrese el DNI del propietario a eliminar:\n").strip()
            repo_propietario.eliminar_propietario(dni)
        elif opcion == "0":
            break
        else:
            opcion_no_valida()

def menu_mascotas(repo_mascota, repo_propietario):
    """
    Submenú para la gestión de mascotas.
    """
    while True:
        print("\n- Gestión de Mascotas -\n")
        print("1. Mostrar todas las mascotas.")
        print("2. Buscar mascota por DNI propietario.")
        print("3. Añadir nueva mascota.")
        print("4. Modificar datos de una mascota.")
        print("5. Eliminar una mascota.")
        print("0. Volver al menú principal.")

        opcion = input("\nSeleccione una opción:\n").strip()
        if opcion == "1":
            repo_mascota.mostrar_mascotas()
        elif opcion == "2":
            dni = input("Ingrese el DNI del propietario:\n").strip()
            propietario_id = repo_propietario.buscar_por_dni(dni)  # Verifica si el propietario existe
            if propietario_id:  # Solo busca mascotas si el propietario existe
                repo_mascota.buscar_por_dni_de_propietario(dni)
        elif opcion == "3":
            # Pedir los datos para agregar una nueva mascota
            dni_propietario = input("Ingrese el DNI del propietario: ").strip()
            nombre = input("Ingrese el nombre de la mascota: ").strip()
            especie = input("Ingrese la especie de animal: ").strip()
            raza = input("Ingrese la raza: ").strip()
            fecnac = input("Ingrese la fecha de nacimiento: ")
            peso = float(input("Ingrese el peso: "))
            repo_mascota.agregar_mascota(dni_propietario, nombre, especie, raza, fecnac, peso)

        # Opción 4: Actualizar una mascota
        elif opcion == "4":
            dni_propietario = input("Ingrese el DNI del propietario: ").strip()
            
            # Buscar las mascotas del propietario
            mascotas = repo_mascota.buscar_por_dni_propietario(dni_propietario)
            
            if not mascotas:
                print(f"⚠️ No se encontraron mascotas para el propietario con DNI: {dni_propietario}")
                continue  # Volver al menú principal del submenú
            
            print("\n=== Mascotas del Propietario ===")
            for mascota in mascotas:
                print(f"ID Mascota: {mascota[0]} | Nombre: {mascota[1]} | Especie: {mascota[2]} | Raza: {mascota[3]} "
                    f"| Fecha de Nacimiento: {mascota[4]} | Peso: {mascota[5]} kg")

            try:
                id_mascota = int(input("\nSelecciona el ID de la mascota a actualizar: ").strip())
                if id_mascota not in [mascota[0] for mascota in mascotas]:
                    print(f"⚠️ No se encontró una mascota con ID {id_mascota}.")
                    continue

                # Obtener datos actuales de la mascota seleccionada
                mascota_actual = next(m for m in mascotas if m[0] == id_mascota)

                # Solicitar los nuevos datos
                print("\nIntroduce los nuevos datos. Deja vacío y pulsa la tecla 'ENTER' para mantener los actuales.\n")
                nombre = input(f"Nuevo nombre de la mascota ({mascota_actual[1]}): ").strip() or mascota_actual[1]
                especie = input(f"Nueva especie de la mascota ({mascota_actual[2]}): ").strip() or mascota_actual[2]
                raza = input(f"Nueva raza de la mascota ({mascota_actual[3]}): ").strip() or mascota_actual[3]
                fecnac = input(f"Nueva fecha de nacimiento (YYYY-MM-DD) ({mascota_actual[4]}): ").strip() or mascota_actual[4]
                peso = input(f"Nuevo peso de la mascota ({mascota_actual[5]} kg): ").strip() or mascota_actual[5]

                # Llamar al repositorio para realizar la actualización
                repo_mascota.actualizar_mascota(id_mascota, nombre, especie, raza, fecnac, peso)
                print(f"✅ La mascota con ID {id_mascota} ha sido actualizada correctamente.")
            
            except ValueError:
                print("⚠️ Por favor, ingresa un número válido como ID de mascota.")
                continue
                              
        # Opción 5: Eliminar una mascota
        elif opcion == "5":
            dni_propietario = input("Ingrese el DNI del propietario: ").strip()
            # Buscar las mascotas del propietario
            mascotas = repo_mascota.buscar_por_dni_propietario(dni_propietario)
            
            if mascotas:
                print("\n=== Mascotas del Propietario ===")
                for mascota in mascotas:
                    print(f"ID Mascota: {mascota[0]} | Nombre: {mascota[1]} | Especie: {mascota[2]} | Raza: {mascota[3]} | Fecha de Nacimiento: {mascota[4]} | Peso: {mascota[5]}")

                # Preguntar al usuario por el ID de la mascota a eliminar
                try:
                    id_mascota = int(input("\nSelecciona el ID de la mascota a eliminar: "))
                    # Verificar si la mascota existe
                    if id_mascota not in [mascota[0] for mascota in mascotas]:
                        print(f"⚠️ No se encontró una mascota con ID {id_mascota}.")
                        return
                    # Llamar a la función para eliminar la mascota
                    repo_mascota.eliminar_mascota(id_mascota)
                except ValueError:
                    print("⚠️ Por favor, ingresa un número válido como ID de mascota.")
            else:
                print("⚠️ No se encontraron mascotas para el propietario con DNI:", dni_propietario)

        elif opcion == "0":
            break
        else:
            opcion_no_valida()

def menu_visitas(repo_visita, repo_mascota):
    """
    Submenú para la gestión de visitas.
    """
    while True:
        print("\n- Gestión de Visitas -\n")
        print("1. Mostrar todas las visitas.")
        print("2. Buscar visitas por mascota.")
        print("3. Registrar nueva visita.")
        print("4. Modificar datos de una visita.")
        print("5. Eliminar una visita.")
        print("0. Volver al menú principal.")

        opcion = input("\nSeleccione una opción:\n").strip()
        if opcion == "1":
            repo_visita.mostrar_visitas()
        elif opcion == "2":
            id_mascota = input("Ingrese el ID de la mascota:\n").strip()
            repo_visita.buscar_por_mascota(id_mascota)
        elif opcion == "3":
            repo_visita.registrar_visita(repo_mascota)
        elif opcion == "4":
            id_visita = input("Ingrese el ID de la visita a modificar:\n").strip()
            repo_visita.actualizar_visita(id_visita)
        elif opcion == "5":
            id_visita = input("Ingrese el ID de la visita a eliminar:\n").strip()
            repo_visita.eliminar_visita(id_visita)
        elif opcion == "0":
            break
        else:
            opcion_no_valida()

def menu_facturas(repo_factura, repo_visita):
    """
    Submenú para la gestión de facturas.
    """
    while True:
        print("\n- Gestión de Facturas -\n")
        print("1. Mostrar todas las facturas.")
        print("2. Buscar factura por número.")
        print("3. Generar nueva factura.")
        print("4. Modificar datos de una factura.")
        print("5. Eliminar una factura.")
        print("0. Volver al menú principal.")

        opcion = input("\nSeleccione una opción:\n").strip()
        if opcion == "1":
            repo_factura.mostrar_facturas()
        elif opcion == "2":
            numero = input("Ingrese el número de factura:\n").strip()
            repo_factura.buscar_por_numero_de_factura(numero)
        elif opcion == "3":
            repo_factura.generar_factura(repo_visita)
        elif opcion == "4":
            id_factura = input("Ingrese el ID de la factura a modificar:\n").strip()
            repo_factura.actualizar_factura(id_factura)
        elif opcion == "5":
            id_factura = input("Ingrese el ID de la factura a eliminar:\n").strip()
            repo_factura.eliminar_factura(id_factura)
        elif opcion == "0":
            break
        else:
            opcion_no_valida()
