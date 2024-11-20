from biblioteca.crud.crud_autor import CRUDAutor

def submenu_autor(biblioteca):
    crud_autor = CRUDAutor(biblioteca.repositorio_autor.ruta_json)

    while True:
        print("\n- Tareas de Autores -\n")
        print("1. Mostrar Autores.")
        print("2. Añadir Autor.")
        print("3. Buscar Autor por Nombre Completo o Pseudónimo.")
        print("4. Modificar Datos de un Autor.")
        print("5. Eliminar Autor.")
        print("0. Volver al Menú Principal.")

        opcion = input("\nSelecciona una opción: ").strip()

        if opcion == "1":
            autores = crud_autor.mostrar_autores()
            if autores:
                print("\n=== Lista de Autores ===")
                for autor in autores:
                    print(
                        f"ID: {autor['autor_id']} | Nombre: {autor['nombre']} | "
                        f"Pseudónimo: {autor['pseudonimo']} | Nacionalidad: {autor.get('nacionalidad', 'Desconocida')}"
                    )
            else:
                print("\n⚠️ No hay autores registrados.")

        elif opcion == "2":
            nuevo_autor = {
                "nombre": input("Nombre: ").strip(),
                "apellido1": input("Primer Apellido: ").strip(),
                "apellido2": input("Segundo Apellido (opcional): ").strip(),
                "pseudonimo": input("Pseudónimo: ").strip(),
                "nacido": input("Año de Nacimiento: ").strip(),
                "fallecido": input("Año de Fallecimiento (opcional): ").strip(),
                "nacionalidad": input("Nacionalidad: ").strip(),
            }
            if crud_autor.agregar_autor(nuevo_autor):
                print("\n✅ Autor añadido correctamente.")
            else:
                print("\n⚠️ No se pudo añadir al autor. Revisa los datos e inténtalo de nuevo.")

        elif opcion == "3":
            criterio = input("Introduce Nombre Completo o Pseudónimo: ").strip()
            autor = crud_autor.buscar_autor_por_nombre_o_pseudonimo(criterio)
            if autor:
                print("\n=== Autor Encontrado ===")
                print(
                    f"ID: {autor['autor_id']} | Nombre: {autor['nombre']} | "
                    f"Pseudónimo: {autor['pseudonimo']} | Nacionalidad: {autor.get('nacionalidad', 'Desconocida')}"
                )
            else:
                print("\n⚠️ No se encontró ningún autor con ese criterio.")

        elif opcion == "4":
            id_autor = input("ID del Autor a Modificar: ").strip()
            nuevos_datos = {
                "nombre": input("Nuevo Nombre (opcional): ").strip(),
                "apellido1": input("Nuevo Primer Apellido (opcional): ").strip(),
                "apellido2": input("Nuevo Segundo Apellido (opcional): ").strip(),
                "pseudonimo": input("Nuevo Pseudónimo (opcional): ").strip(),
                "nacido": input("Nuevo Año de Nacimiento (opcional): ").strip(),
                "fallecido": input("Nuevo Año de Fallecimiento (opcional): ").strip(),
                "nacionalidad": input("Nueva Nacionalidad (opcional): ").strip(),
            }
            if crud_autor.actualizar_autor(id_autor, nuevos_datos):
                print("\n✅ Autor actualizado correctamente.")
            else:
                print("\n⚠️ No se encontró un autor con ese ID o los datos no son válidos.")

        elif opcion == "5":
            id_autor = input("ID del Autor a Eliminar: ").strip()
            if crud_autor.eliminar_autor(id_autor):
                print("\n✅ Autor eliminado correctamente.")
            else:
                print("\n⚠️ No se encontró un autor con ese ID o no se pudo eliminar.")

        elif opcion == "0":
            break

        else:
            print("\n⚠️ Opción no válida. Inténtalo de nuevo.")
