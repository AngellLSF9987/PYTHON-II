from datetime import datetime
from ClinicaVeterinaria.utilidades.validaciones import opcion_no_valida, salir, validar_fecha, validar_importe
from ClinicaVeterinaria.repositorios.repositorio_propietario import RepositorioPropietario
from ClinicaVeterinaria.repositorios.repositorio_mascota import RepositorioMascota
from ClinicaVeterinaria.repositorios.repositorio_visita import RepositorioVisita
from ClinicaVeterinaria.repositorios.repositorio_factura import RepositorioFactura
from ClinicaVeterinaria.database.db_connection import ConexionDB

def inicializar_repositorios(db_path):
    """
    Inicializa la conexión a la base de datos y los repositorios necesarios.
    """
    db_path = r"UD.4\Tarea_4-UD.4-Saorin_Faura-Angel_Luis-48616905B\ClinicaVeterinaria\database\clinica_veterinaria.db"
    conexion = ConexionDB(db_path)
    return {
        "propietario": RepositorioPropietario(conexion),
        "mascota": RepositorioMascota(conexion),
        "visita": RepositorioVisita(conexion),
        "factura": RepositorioFactura(conexion),
    }


def mostrar_menu_principal(repositorios):
    opciones = {
        "1": lambda: menu_propietarios(repositorios["propietario"]),
        "2": lambda: menu_mascotas(repositorios["mascota"], repositorios["propietario"]),
        "3": lambda: menu_visitas(repositorios["visita"], repositorios["mascota"]),
        "4": lambda: menu_facturas(repositorios["factura"], repositorios["visita"], repositorios["mascota"], repositorios["propietario"]),
        "0": salir
    }

    while True:
        print("\n--- Clínica Veterinaria ---")
        print("1. Gestión de Propietarios")
        print("2. Gestión de Mascotas")
        print("3. Gestión de Visitas")
        print("4. Gestión de Facturas")
        print("0. Salir")

        opcion = input("\nSeleccione una opción:\n").strip()
        accion = opciones.get(opcion, opcion_no_valida)
        accion()

def menu_propietarios(repo_propietario):
    """
    Submenú para la gestión de propietarios.
    """
    while True:
        print("\n--- Gestión de Propietarios ---")
        print("1. Mostrar todos los propietarios")
        print("2. Buscar propietario por DNI")
        print("3. Añadir nuevo propietario")
        print("4. Modificar datos de un propietario")
        print("5. Eliminar un propietario")
        print("0. Volver al menú principal")

        opcion = input("\nSeleccione una opción:\n").strip()
        try:
            if opcion == "1":
                repo_propietario.mostrar_propietarios()
            elif opcion == "2":
                dni = input("Ingrese el DNI del propietario: ").strip()
                propietario = repo_propietario.buscar_por_dni(dni)
            elif opcion == "3":
                nombre = input("Nombre: ").strip()
                apellido1 = input("Primer apellido: ").strip()
                apellido2 = input("Segundo apellido: ").strip()
                dni = input("DNI: ").strip()
                telefono = input("Teléfono: ").strip()
                direccion = input("Dirección: ").strip()
                email = input("Email: ").strip()
                repo_propietario.agregar_propietario(nombre, apellido1, apellido2, dni, telefono, direccion, email)
                print("✅ Propietario agregado con éxito.")
            elif opcion == "4":
                dni = input("Ingrese el DNI del propietario a modificar: ").strip()
                propietario = repo_propietario.buscar_por_dni(dni)
                if not propietario:
                    print(f"⚠️ No se encontró ningún propietario con DNI {dni}.")
                    continue
                print(f"Propietario actual: {propietario}")
                # Lógica donde modificar el propietario
                nuevo_nombre = input(f"Nombre ({propietario['Nombre']}): ") or propietario['Nombre']
                primer_apellido = input(f"Primer apellido ({propietario['Apellido1']}): ") or propietario['Apellido1']
                segundo_apellido = input(f"Segundo apellido ({propietario['Apellido2']}): ") or propietario['Apellido2']
                telefono = input(f"Teléfono ({propietario['Telefono']}): ") or propietario['Telefono']
                direccion = input(f"Dirección ({propietario['Direccion']}): ") or propietario['Direccion']
                email = input(f"Email ({propietario['Email']}): ") or propietario['Email']

                # Crear un diccionario con los nuevos valores
                propietario_actualizado = {
                    'Nombre': nuevo_nombre,
                    'Apellido1': primer_apellido,
                    'Apellido2': segundo_apellido,
                    'Telefono': telefono,
                    'Direccion': direccion,
                    'Email': email,
                    'DNI': propietario['DNI']  # Este valor no cambia
                }
                # Llamar a la función de actualización pasando el diccionario
                repo_propietario.actualizar_propietario(propietario_actualizado)
                print("✅ Propietario actualizado con éxito.")
            elif opcion == "5":
                dni = input("Ingrese el DNI del propietario a eliminar: ").strip()
                repo_propietario.eliminar_propietario(dni)
                print("✅ Propietario eliminado con éxito.")
            elif opcion == "0":
                break
            else:
                opcion_no_valida()
        except Exception as e:
            print(f"❌ Error: {e}")

def menu_mascotas(repo_mascota, repo_propietario):
    while True:
        print("\n--- Gestión de Mascotas ---")
        print("1. Mostrar todas las mascotas")
        print("2. Buscar mascota por DNI de propietario")
        print("3. Añadir nueva mascota")
        print("4. Modificar datos de una mascota")
        print("5. Eliminar una mascota")
        print("0. Volver al menú principal")

        opcion = input("\nSeleccione una opción:\n").strip()
        try:
            if opcion == "1":
                repo_mascota.mostrar_mascotas()
            elif opcion == "2":
                propietario_DNI = input("Ingrese el DNI del propietario: ").strip()  # El DNI, no el ID de la mascota
                mascotas = repo_mascota.buscar_por_dni_de_propietario(propietario_DNI)
            
            elif opcion == "3":
                # Recoger los datos de la nueva mascota
                nombre = input("Nombre: ").strip()
                especie = input("Especie: ").strip()
                raza = input("Raza: ").strip()
                fecnac = input("Fecha Nacimiento: ").strip()
                try:
                    peso = float(input(f"Peso ({mascota_actual['peso']}) kg: ").strip() or mascota_actual["peso"])
                except ValueError:
                    print("⚠️ El peso debe ser un número válido.")
                    continue
                propietario_dni = input("DNI del propietario: ").strip()

                # Llamar al método para agregar la mascota (este método ahora se encargará de agregar el propietario si no existe)
                id_mascota = repo_mascota.agregar_mascota(propietario_dni, nombre, especie, raza, fecnac, peso)

                # Si el ID de la mascota no es None, significa que la mascota se agregó correctamente
                if id_mascota:
                    print(f"✅ Mascota agregada con éxito. ID: {id_mascota}")
                else:
                    print("❌ No se pudo agregar la mascota.")
            elif opcion == "4":
                propietario_DNI = input("Ingrese el DNI del propietario de la mascota a modificar: ").strip()
                mascotas = repo_mascota.buscar_por_dni_de_propietario(propietario_DNI)
                if not mascotas:
                    print(f"⚠️ No se encontró ninguna mascota desde el DNI de propietario proporcionado {propietario_DNI}.")
                    continue
                print(f"\n=== Mascotas del Propietario ===\n")
                for mascota in mascotas:
                    print(f"ID Mascota: {mascota['id']} | Nombre: {mascota['nombre']} | Especie: {mascota['especie']} | Raza: {mascota['raza']} | Fecha de Nacimiento: {mascota['fecnac']} | Peso: {mascota['peso']} kg")

                id_mascota = int(input("Ingrese el ID de la mascota a modificar: "))
                mascota_actual = next((m for m in mascotas if m['id'] == id_mascota), None)
                if mascota_actual:
                    nombre = input(f"Nombre ({mascota_actual['nombre']}): ").strip() or mascota_actual["nombre"]
                    especie = input(f"Especie ({mascota_actual['especie']}): ").strip() or mascota_actual["especie"]
                    raza = input(f"Raza ({mascota_actual['raza']}): ").strip() or mascota_actual["raza"]
                    fecnac = input(f"Fecha de nacimiento ({mascota_actual['fecnac']}): ").strip() or mascota_actual["fecnac"]
                    try:
                        peso = float(input(f"Peso ({mascota_actual['peso']}) kg: ").strip() or mascota_actual["peso"])
                    except ValueError:
                        print("⚠️ El peso debe ser un número válido.")
                        continue
                    repo_mascota.actualizar_mascota(mascota_actual['id'], nombre, especie, raza, fecnac, peso)
                    print("✅ Mascota actualizada con éxito.")
                else:
                    print("⚠️ No se encontró una mascota con ese ID.")
            elif opcion == "5":
                propietario_DNI = input("Ingrese el DNI del propietario de la mascota/s a eliminar: ").strip()
                mascotas = repo_mascota.buscar_por_dni_de_propietario(propietario_DNI)
                if not mascotas:
                    print(f"⚠️ No se encontró ninguna mascota desde el DNI de propietario proporcionado {propietario_DNI}.")
                    continue
                print(f"\n=== Mascotas del Propietario ===\n")
                for mascota in mascotas:
                    print(f"ID Mascota: {mascota['id']} | Nombre: {mascota['nombre']} | Especie: {mascota['especie']} | Raza: {mascota['raza']} | Fecha de Nacimiento: {mascota['fecnac']} | Peso: {mascota['peso']} kg")

                id_mascota = int(input("Ingrese el ID de la mascota a modificar: "))
                repo_mascota.eliminar_mascota(id_mascota)
                print("✅ Mascota eliminada con éxito.")
            elif opcion == "0":
                break
            else:
                opcion_no_valida()
        except Exception as e:
            print(f"❌ Error: {e}")


def menu_visitas(repo_visita, repo_mascota):
    while True:
        print("\n--- Gestión de Visitas ---")
        print("1. Mostrar todas las visitas")
        print("2. Buscar visita por DNI de propietario ")
        print("3. Añadir nueva visita")
        print("4. Modificar datos de una visita")
        print("5. Eliminar una visita")
        print("0. Volver al menú principal")

        opcion = input("\nSeleccione una opción:\n").strip()
        try:
            if opcion == "1":
                repo_visita.mostrar_visitas()

            elif opcion == "2":
                propietario_DNI = input("Ingrese el DNI del propietario para obtener la o las mascotas registradas: ").strip()
                mascotas = repo_mascota.buscar_por_dni_de_propietario(propietario_DNI)

                # Verificar si se han encontrado mascotas
                if mascotas:
                    print(f"\n=== Mascotas del Propietario ===")
                    for mascota in mascotas:
                        print(f"ID Mascota: {mascota['id']} | Nombre: {mascota['nombre']} | Especie: {mascota['especie']} | Raza: {mascota['raza']} | Fecha de Nacimiento: {mascota['fecnac']} | Peso: {mascota['peso']} kg")

                    id_mascota = int(input("\nIngrese el ID de la mascota a consultar: "))

                    # Llamar al repositorio para obtener las visitas de la mascota seleccionada
                    visitas = repo_visita.buscar_visitas_por_dni_propietario(propietario_DNI)

                    if visitas:
                        # Filtrar visitas por la mascota seleccionada
                        visitas_mascota = [visita for visita in visitas if visita["mascota_id"] == id_mascota]

                        if visitas_mascota:
                            print(f"\n=== Lista de Visitas de la Mascota ===")
                            for visita in visitas_mascota:
                                print(f"ID Visita: {visita['id_visita']} | Fecha: {visita['fecha']} | Motivo: {visita['motivo']} | Tratamiento: {visita['tratamiento']}")
                        else:
                            print(f"⚠️ No se encontró ninguna visita para la mascota con ID {id_mascota}.")
                    else:
                        print(f"⚠️ No se encontraron visitas para el propietario con DNI {propietario_DNI}.")
                else:
                    print(f"⚠️ No se encontró ninguna mascota asociada al DNI de propietario {propietario_DNI}.")

            elif opcion == "3":
                propietario_DNI = input("Ingrese el DNI del propietario para obtener la o las mascotas registradas: ").strip()
                mascotas = repo_mascota.buscar_por_dni_de_propietario(propietario_DNI)
                
                if not mascotas:
                    print(f"⚠️ No se encontró ninguna mascota asociada al DNI del propietario {propietario_DNI}.")
                    continue
                
                print(f"\n=== Mascotas del Propietario ===")
                for mascota in mascotas:
                    print(f"ID Mascota: {mascota['id']} | Nombre: {mascota['nombre']} | Especie: {mascota['especie']} | Raza: {mascota['raza']} | Fecha de Nacimiento: {mascota['fecnac']} | Peso: {mascota['peso']} kg")

                id_mascota = int(input("\nIngrese el ID de la mascota a la que desea añadir una visita: ").strip())

                # Solicitar detalles de la visita
                fecha = input("Fecha de la visita (YYYY-MM-DD): ").strip()
                motivo = input("Motivo de la visita: ").strip()
                tratamiento = input("Tratamiento realizado: ").strip()

                # Llamar al repositorio para agregar la visita
                id_visita = repo_visita.agregar_visita(id_mascota, fecha, motivo, tratamiento)
                if id_visita:
                    print(f"✅ Visita agregada con éxito. ID de la visita: {id_visita}")
                else:
                    print("❌ Error al agregar la visita.")

            elif opcion == "4":
                propietario_DNI = input("Ingrese el DNI del propietario para obtener la o las mascotas registradas: ").strip()
                mascotas = repo_mascota.buscar_por_dni_de_propietario(propietario_DNI)
                
                if not mascotas:
                    print(f"⚠️ No se encontró ninguna mascota asociada al DNI de propietario {propietario_DNI}.")
                    continue
                
                print(f"\n=== Mascotas del Propietario ===")
                for mascota in mascotas:
                    print(f"ID Mascota: {mascota['id']} | Nombre: {mascota['nombre']} | Especie: {mascota['especie']} | Raza: {mascota['raza']} | Fecha de Nacimiento: {mascota['fecnac']} | Peso: {mascota['peso']} kg")

                id_mascota = int(input("\nIngrese el ID de la mascota a consultar: "))

                # Llamar al repositorio para obtener las visitas de la mascota seleccionada
                visitas = repo_visita.buscar_visitas_por_dni_propietario(propietario_DNI)

                if visitas:
                    print(f"\n=== Lista de Visitas de la Mascota ===")
                    for visita in visitas:
                        if visita["mascota_id"] == id_mascota:
                            print(f"ID Visita: {visita['id_visita']} | Fecha: {visita['fecha']} | Motivo: {visita['motivo']} | Tratamiento: {visita['tratamiento']}")

                id_visita = input("Ingrese el ID de la visita a modificar: ").strip()

                visita_actual = repo_visita.obtener_visita(id_visita)
                if not visita_actual:
                    print(f"⚠️ No se encontró ninguna visita con ID {id_visita}.")
                    continue
                print(f"Visita actual")
                fecha = input(f"Fecha ({visita_actual['fecha']}): ").strip() or visita_actual["fecha"]
                motivo = input(f"Motivo ({visita_actual['motivo']}): ").strip() or visita_actual["motivo"]
                tratamiento = input(f"Tratamiento ({visita_actual['tratamiento']}): ").strip() or visita_actual["tratamiento"]

                repo_visita.actualizar_visita(fecha, motivo, tratamiento, id_visita)

                print("✅ Visita actualizada con éxito.")
            
            elif opcion == "5":
                propietario_DNI = input("Ingrese el DNI del propietario para obtener la o las mascotas registradas: ").strip()
                mascotas = repo_mascota.buscar_por_dni_de_propietario(propietario_DNI)
                
                if not mascotas:
                    print(f"⚠️ No se encontró ninguna mascota asociada al DNI de propietario {propietario_DNI}.")
                    continue
                
                print(f"\n=== Mascotas del Propietario ===")
                for mascota in mascotas:
                    print(f"ID Mascota: {mascota['id']} | Nombre: {mascota['nombre']} | Especie: {mascota['especie']} | Raza: {mascota['raza']} | Fecha de Nacimiento: {mascota['fecnac']} | Peso: {mascota['peso']} kg")

                id_mascota = int(input("\nIngrese el ID de la mascota a consultar: "))

                # Llamar al repositorio para obtener las visitas de la mascota seleccionada
                visitas = repo_visita.buscar_visitas_por_dni_propietario(propietario_DNI)

                if visitas:
                    print(f"\n=== Lista de Visitas de la Mascota ===")
                    for visita in visitas:
                        if visita["mascota_id"] == id_mascota:
                            print(f"ID Visita: {visita['id_visita']} | Fecha: {visita['fecha']} | Motivo: {visita['motivo']}")
                
                id_visita = input("Ingrese el ID de la visita a eliminar: ").strip()
                repo_visita.eliminar_visita(id_visita)
                print("✅ Visita eliminada con éxito.")
            elif opcion == "0":
                break
            else:
                opcion_no_valida()
        except Exception as e:
            print(f"❌ Error: {e}")

def menu_facturas(repo_factura, repo_visita, repo_mascota, repo_propietario):
    """
    Submenú para la gestión de facturas, ajustado al modelo de la tabla T_Facturas.
    """
    while True:
        print("\n--- Gestión de Facturas ---")
        print("1. Mostrar todas las facturas")
        print("2. Buscar factura por DNI de propietario")
        print("3. Generar nueva factura")
        print("4. Modificar factura existente")
        print("5. Eliminar una factura")
        print("0. Volver al menú principal")

        opcion = input("\nSeleccione una opción:\n").strip()
        try:
            if opcion == "1":
                print("\n=== Mostrar todas las facturas ===")
                facturas = repo_factura.mostrar_facturas()  # Método para obtener todas las facturas
            elif opcion == "2":
                propietario_DNI = input("Ingrese el DNI del propietario cliente para mostrar las facturas asociadas: ").strip()
                facturas = repo_factura.buscar_facturas_por_dni_propietario(propietario_DNI)

                if not facturas:
                    print(f"⚠️ No se encontró ninguna factura asociada al DNI de propietario {propietario_DNI}.")
                    continue

                print(f"\n=== Facturas Asociadas al Propietario ===\n")

                for factura in facturas:
                    print(f"ID Factura: {factura['id_factura']} | Fecha de Emisión: {factura['fecha']} | Importe P.V.P.: {factura['importe']} | Visita: {factura['visita_id']} | Mascota: {factura['mascota_nombre']} | Propietario: {factura['propietario_dni']}")

            elif opcion == "3":
                print("=== Generar Nueva Factura ===")

                # Intentar obtener todas las visitas
                visitas = repo_visita.obtener_todas_visitas_completas()
                if not visitas:
                    print("⚠️ No hay visitas registradas.")
                    continue

                # Mostrar las visitas disponibles
                print("Seleccione una visita de la siguiente lista:")
                for visita in visitas:
                    print(f"ID Visita: {visita['IdVisita']} | Fecha: {visita['Fecha']} | Mascota ID: {visita['IdMascota']} | Propietario DNI: {visita['DNI']}")

                # Seleccionar una visita
                id_visita = input("Ingrese el ID de la visita para generar la factura: ").strip()
                visita = repo_visita.obtener_visita(id_visita)

                if not visita:
                    print(f"⚠️ No se encontró una visita con el ID {id_visita}.")
                    continue

                # Buscar la mascota asociada a esta visita
                mascota = repo_mascota.obtener_mascota(visita['Mascota_Id'])
                if not mascota:
                    print(f"⚠️ No se encontró una mascota con el ID {visita['Mascota_Id']}.")
                    continue

                # Buscar el propietario asociado a esta visita
                propietario_dni = visita.get('Propietario_DNI')
                if not propietario_dni:
                    print("⚠️ El DNI del propietario está ausente en la visita. Verifique los datos.")
                    continue

                propietario = repo_propietario.buscar_por_dni(propietario_dni)
                if not propietario:
                    print(f"⚠️ No se encontró un propietario con el DNI {propietario_dni}.")
                    continue

                print(f"Detalles de la visita seleccionada: {visita}")
                print(f"Mascota: {mascota['nombre']}, Propietario: {propietario['nombre']}")

                # Validar la fecha de la factura
                while True:
                    fecha_input = input(f"Fecha de la factura (default: {datetime.now().strftime('%d-%m-%Y')}): ").strip()
                    if not fecha_input:
                        fecha = datetime.now().strftime('%d-%m-%Y')
                        break
                    elif validar_fecha(fecha_input):
                        fecha = fecha_input
                        break
                    else:
                        print("⚠️ Fecha inválida. Por favor, ingrese una fecha en formato DD-MM-AAAA.")

                # Validar el importe de la factura
                while True:
                    try:
                        importe = validar_importe(input("Importe (€): ").strip())
                        if importe <= 0:
                            print("⚠️ El importe debe ser mayor a 0.")
                        else:
                            break
                    except ValueError:
                        print("⚠️ Por favor, ingrese un importe válido en formato numérico.")

                # Generar la factura
                nueva_factura = repo_factura.generar_factura(fecha, importe, id_visita, mascota['IdMascota'], propietario['DNI'])
                if nueva_factura:
                    print(f"✅ Factura generada con éxito. ID: {nueva_factura}")
                else:
                    print("❌ Error al generar la factura.")
            
            elif opcion == "4":
                print("\n=== Modificar Factura ===")
                
                dni_propietario = input("Ingrese el DNI del propietario: ").strip()
                facturas = repo_factura.buscar_facturas_por_dni_propietario(dni_propietario)

                if facturas:
                    print("\n=== Facturas Asociadas ===")
                    for factura in facturas:
                        print(f"ID: {factura['id_factura']} | Fecha: {factura['fecha']} | Importe: {factura['importe']}")

                    id_factura = input("\nIngrese el ID de la factura a modificar: ").strip()
                    factura_seleccionada = next((f for f in facturas if f['id_factura'] == int(id_factura)), None)

                    if factura_seleccionada:
                        print(f"\nFactura seleccionada: {factura_seleccionada}")
                        
                        # Validar nuevo importe
                        while True:
                            try:
                                nuevo_importe = input(f"Nuevo importe (actual: {factura_seleccionada['importe']}): ").strip()
                                nuevo_importe = validar_importe(nuevo_importe)  # Validar el importe
                                break
                            except ValueError as e:
                                print(f"❌ Error: {e}")
                        
                        # Validar nueva fecha
                        while True:
                            try:
                                nueva_fecha = input(f"Nueva fecha (actual: {factura_seleccionada['fecha']}): ").strip()
                                nueva_fecha = validar_fecha(nueva_fecha) if nueva_fecha else factura_seleccionada['fecha']
                                break
                            except ValueError as e:
                                print(f"❌ Error: {e}")
                        
                        # Modificar la factura
                        factura_modificada = {
                            "id_factura": factura_seleccionada['id_factura'],
                            "importe": nuevo_importe,
                            "fecha": nueva_fecha,
                        }

                        repo_factura.modificar_factura(factura_modificada)
                        print("✅ Factura modificada con éxito.")
                    else:
                        print("❌ No se encontró la factura seleccionada.")
                else:
                    print(f"❌ No se encontraron facturas asociadas al propietario con DNI {dni_propietario}.")

            elif opcion == "5":
                id_factura = input("Ingrese el ID de la factura a eliminar: ").strip()
                confirmacion = input("¿Está seguro de que desea eliminar esta factura? (s/n): ").strip().lower()
                if confirmacion == "s":
                    repo_factura.eliminar_factura(id_factura)
                    print("✅ Factura eliminada con éxito.")
            elif opcion == "0":
                break
            else:
                opcion_no_valida()
        except Exception as e:
            print(f"❌ Error: {e}")