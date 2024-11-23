# biblioteca/menus/submenus/submenu_autor.py

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
                print("\n=== Lista de Autores ===\n")
                for autor in autores:
                    nombre_completo = f"{autor['nombre']} {autor['apellido1']} {autor.get('apellido2', '')}".strip()
                    print(
                        f"> ID: {autor['autor_id']} | Nombre: {nombre_completo} | "
                        f"  Pseudónimo: {autor.get('pseudonimo', 'No disponible')} |\n"
                        f"  Fecha de Nacimiento: {autor.get('nacido', 'No disponible')} | Fecha de Fallecimiento: {autor.get('fallecido', 'No fallecido')} |\n"
                        f"  Nacionalidad: {autor.get('nacionalidad', 'Desconocida')}\n"
                    )
            else:
                print("\n⚠️ No hay autores registrados.")

        elif opcion == "2":
            nuevo_autor = {
                "nombre": input("Nombre: ").strip(),
                "apellido1": input("Primer Apellido: ").strip(),
                "apellido2": input("Segundo Apellido (opcional): ").strip(),
                "pseudonimo": input("Pseudónimo (opcional): ").strip(),
                "nacido": input("Año de Nacimiento: ").strip(),
                "fallecido": input("Año de Fallecimiento (opcional): ").strip(),
                "nacionalidad": input("Nacionalidad: ").strip(),
            }
            if crud_autor.agregar_autor(nuevo_autor):
                print("\n✅ Autor añadido correctamente.")
            else:
                print("\n⚠️ No se pudo añadir al autor. Revisa los datos e inténtalo de nuevo.")

        elif opcion == "3":
            criterio = input("Introduce Nombre Completo o Pseudónimo: \n").strip()
            autor = crud_autor.buscar_autor_por_nombre_o_pseudonimo(criterio)
            if autor:
                print("\n=== Autor Encontrado ===")
                nombre_completo = f"{autor['nombre']} {autor['apellido1']} {autor.get('apellido2', '')}".strip()
                print(
                    f"ID: {autor['autor_id']} | Nombre: {nombre_completo} | "
                    f"Pseudónimo: {autor.get('pseudonimo', 'No disponible')} | "
                    f"Nacionalidad: {autor.get('nacionalidad', 'Desconocida')}"
                )
            else:
                print("\n⚠️ No se encontró ningún autor con ese criterio.")

        elif opcion == "4":
            criterio = input("Introduce Nombre Completo o Pseudónimo del autor a modificar: ").strip()
            autor = crud_autor.buscar_autor_por_nombre_o_pseudonimo(criterio)
            if autor:
                print("\n=== Datos Actuales ===")
                nombre_completo = f"{autor['nombre']} {autor['apellido1']} {autor.get('apellido2', '')}".strip()
                print(
                    f"ID: {autor['autor_id']} | Nombre: {nombre_completo} | "
                    f"Pseudónimo: {autor.get('pseudonimo', 'No disponible')} | "
                    f"Nacionalidad: {autor.get('nacionalidad', 'Desconocida')}"
                )
                print("\nIntroduce los nuevos datos. Deja vacío para mantener los actuales.")
                actualizado = {
                    "nombre": input(f"Nombre [{autor['nombre']}]: ").strip() or autor['nombre'],
                    "apellido1": input(f"Primer Apellido [{autor['apellido1']}]: ").strip() or autor['apellido1'],
                    "apellido2": input(f"Segundo Apellido [{autor.get('apellido2', '')}]: ").strip() or autor.get('apellido2', ''),
                    "pseudonimo": input(f"Pseudónimo [{autor.get('pseudonimo', 'No disponible')}]: ").strip() or autor.get('pseudonimo', ''),
                    "nacido": input(f"Año de Nacimiento [{autor['nacido']}]: ").strip() or autor['nacido'],
                    "fallecido": input(f"Año de Fallecimiento [{autor.get('fallecido', 'No disponible')}]: ").strip() or autor.get('fallecido', ''),
                    "nacionalidad": input(f"Nacionalidad [{autor.get('nacionalidad', 'Desconocida')}]: ").strip() or autor.get('nacionalidad', ''),
                }
                if crud_autor.actualizar_autor(autor['autor_id'], actualizado):
                    print("\n✅ Autor actualizado correctamente.")
                else:
                    print("\n⚠️ No se pudo actualizar al autor.")
            else:
                print("\n⚠️ Autor no encontrado.")

        elif opcion == "5":
            criterio = input("Introduce Nombre Completo o Pseudónimo del autor a eliminar: ").strip()
            autor = crud_autor.buscar_autor_por_nombre_o_pseudonimo(criterio)
            if autor:
                confirmacion = input(f"¿Estás seguro de eliminar al Autor {autor['nombre']} {autor['apellido1']}? (s/n): ").strip().lower()
                if confirmacion == 's':
                    if crud_autor.eliminar_autor(autor['autor_id']):
                        print("\n✅ Autor eliminado correctamente.")
                    else:
                        print("\n⚠️ No se pudo eliminar al autor.")
            else:
                print("\n⚠️ Autor no encontrado.")

        elif opcion == "0":
            break

        else:
            print("\n⚠️ Opción no válida. Inténtalo de nuevo.")
