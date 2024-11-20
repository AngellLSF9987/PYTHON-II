from biblioteca.crud.crud_autor import CRUDAutor

def submenu_autor(crud_autor):
    while True:
        print("\n- Tareas de Autores -\n")
        print("1. Mostrar Autores.")
        print("2. Añadir Autor.")
        print("3. Buscar Autor por Nombre Completo o Pseudónimo.")
        print("4. Modificar Datos de un Autor.")
        print("5. Eliminar Autor.")
        print("0. Volver al Menú Principal.")

        opcion = input("\nSelecciona una opción:\n")

        if opcion == "1":
            crud_autor.mostrar_autores()
        elif opcion == "2":
            nuevo_autor = {
                "nombre": input("Nombre: "),
                "apellido1": input("Primer Apellido: "),
                "apellido2": input("Segundo Apellido (opcional): "),
                "pseudonimo": input("Pseudónimo: "),
                "nacido": input("Año de Nacimiento: "),
                "fallecido": input("Año de Fallecimiento (opcional): "),
                "nacionalidad": input("Nacionalidad: "),
            }
            crud_autor.agregar_autor(nuevo_autor)
            print("Autor añadido correctamente.")
        elif opcion == "3":
            nombre_o_pseudonimo = input("Introduce Nombre Completo o Pseudónimo: ")
            autor = crud_autor.buscar_autor_por_nombre_o_pseudonimo(nombre_o_pseudonimo)
            if autor:
                print(f"Autor encontrado: {autor}")
            else:
                print("No se encontró ningún autor con ese dato.")
        elif opcion == "4":
            id_autor = input("ID del Autor a Modificar: ")
            nuevos_datos = {
                "nombre": input("Nuevo Nombre (opcional): "),
                "apellido1": input("Nuevo Primer Apellido (opcional): "),
                "apellido2": input("Nuevo Segundo Apellido (opcional): "),
                "pseudonimo": input("Nuevo Pseudónimo (opcional): "),
                "nacido": input("Nuevo Año de Nacimiento (opcional): "),
                "fallecido": input("Nuevo Año de Fallecimiento (opcional): "),
                "nacionalidad": input("Nueva Nacionalidad (opcional): "),
            }
            if crud_autor.actualizar_autor(id_autor, nuevos_datos):
                print("Autor actualizado correctamente.")
            else:
                print("No se encontró un autor con ese ID.")
        elif opcion == "5":
            id_autor = input("ID del Autor a Eliminar: ")
            if crud_autor.eliminar_autor(id_autor):
                print("Autor eliminado correctamente.")
            else:
                print("No se encontró un autor con ese ID.")
        elif opcion == "0":
            break
        else:
            print("\nOpción no válida. Intenta nuevamente.")
