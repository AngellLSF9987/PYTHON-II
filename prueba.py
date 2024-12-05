# Modificar datos de una mascota
if opcion == "4":
    # Solicitar el DNI del propietario para obtener las mascotas
    dni = input("Ingrese el DNI del propietario: ").strip()
    
    # Buscar las mascotas asociadas a ese DNI
    mascotas = self.buscar_mascotas_por_dni(dni)
    
    if mascotas:
        print("\n=== Mascotas del Propietario ===")
        for mascota in mascotas:
            print(f"ID Mascota: {mascota['IdMascota']} | Nombre: {mascota['Nombre']} | "
                  f"Especie: {mascota['Especie']} | Raza: {mascota['Raza']} | "
                  f"Fecha de Nacimiento: {mascota['FechaNacimiento']} | Peso: {mascota['Peso']} kg")
        
        # Seleccionar una mascota para modificar
        id_mascota = input("Seleccione el ID de la mascota que desea modificar: ").strip()
        
        # Buscar la mascota específica
        mascota_seleccionada = self.buscar_mascota_por_id(id_mascota)
        
        if mascota_seleccionada:
            print("\n=== Modificar Mascota ===")
            nombre = input(f"Nombre (actual: {mascota_seleccionada['Nombre']}): ").strip()
            especie = input(f"Especie (actual: {mascota_seleccionada['Especie']}): ").strip()
            raza = input(f"Raza (actual: {mascota_seleccionada['Raza']}): ").strip()
            fecha_nacimiento = input(f"Fecha de Nacimiento (actual: {mascota_seleccionada['FechaNacimiento']}): ").strip()
            peso = input(f"Peso (actual: {mascota_seleccionada['Peso']} kg): ").strip()
            
            # Actualizar la mascota
            self.modificar_mascota(id_mascota, nombre, especie, raza, fecha_nacimiento, peso)
            print(f"✅ Datos de la mascota actualizados con éxito.")
        else:
            print("⚠️ No se encontró la mascota seleccionada.")
    else:
        print(f"⚠️ No se encontraron mascotas para el propietario con DNI: {dni}.")