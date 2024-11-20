# biblioteca/crud/crud_subgenero.py

import json
import shutil  # Para respaldar datos antes de guardar

class CRUDEspecifico:

    def __init__(self, ruta_json):
        self.ruta_json = ruta_json
        self.datos = self.cargar_datos()
        self.autor_id_actual = self.obtener_max_id() + 1  # Inicializar ID autoincremental

    def cargar_datos(self):
        """Carga los datos desde el archivo JSON."""
        try:
            with open(self.ruta_json, 'r', encoding='utf-8') as archivo:
                return json.load(archivo)
        except FileNotFoundError:
            print("Archivo JSON no encontrado. Se creará un nuevo archivo.")
            return {"autores": []}  # Inicializa con lista vacía si no existe
        except json.JSONDecodeError:
            print("Error al leer el archivo JSON. Archivo vacío o malformado.")
            return {"autores": []}

    def guardar_datos(self):
        """Guarda los datos en el archivo JSON y realiza un respaldo previo."""
        try:
            # Crear respaldo del archivo
            shutil.copy(self.ruta_json, self.ruta_json + ".bak")
            with open(self.ruta_json, 'w', encoding='utf-8') as archivo:
                json.dump(self.datos, archivo, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Error al guardar los datos: {e}")

    def obtener_max_id(self):
        """Obtiene el máximo ID existente en los especificos."""
        if not self.datos["especificos"]:
            return 0  # Si no hay especificos, inicia en 0
        return max(int(especifico["especifico_id"]) for especifico in self.datos["especificos"])
    
    # def crear_especifico(biblioteca):
    #     """Crear un nuevo subgénero literario y lo añade a la Biblioteca."""

    #     try:
    #         print("\n- Nuevo Registro de SubGénero Literario -\n")
    #         # Obtener el género del usuario
    #         genero = input("Introduce el nombre del género literario:\n").strip()

    #         # Validar que el género no esté vacío
    #         if not genero:
    #             raise ValueError("El nombre del género no puede estar vacío.")

    #         # Validar si el género existe en la biblioteca
    #         if genero.lower() not in biblioteca.diccionario_generos:
    #             raise ValueError(f"El género '{genero}' no existe en la biblioteca. Por favor, asegúrese de que el género esté registrado.")

    #         # Obtener el nombre y tipo del subgénero
    #         nombre_especifico = input("Introduce el nombre subgénero específico:\n").strip()
    #         tipo = input("Introduzca el tipo de subgénero específico:\n").strip()

    #         # Validar que los campos no estén vacíos
    #         if not nombre_especifico or not tipo:
    #             raise ValueError("El nombre del subgénero y el tipo no pueden estar vacíos.")

    #         # Creación y registro del nuevo objeto subgénero
    #         especifico = Especifico(genero, nombre_especifico, tipo)

    #         # Agregar el subgénero a la biblioteca
    #         biblioteca.agregar_especifico(especifico)  # Usar la instancia de biblioteca

    #         print("\nSubgénero Literario registrado correctamente.\n")

    #     except ValueError as e:  # Valores incorrectos al ingresar datos
    #         print(f"\nError: Entrada inválida. {e}\n")
    #     except Exception as e2:  # Errores imprevistos
    #         print(f"\nSe produjo un error inesperado: {e2}\n")



    # def leer_especifico(biblioteca):
    #     """Busca y muestra la información de un subgenero por nombre."""

    #     try:
    #         print("\n- Información del Registro deseado -\n")
    #         nombre_especifico = input("Introduzca el nombre del subgénero literario a buscar:\n")
    #         especifico = biblioteca.buscar_especifico_nombre(nombre_especifico)

    #         if especifico:
    #             print("\nRegistro encontrado.\n")
    #             print(especifico.mostrar_datos_especifico())
    #         else:
    #             print("\nSubgénero Literario no encontrado. Revise la información proporcionada e inténtelo de nuevo.\n")

    #     except Exception as e:                                         # Errores imprevistos
    #         print(f"Se produjo un error al buscar el libro: {e}")


    # def mostrar_especificos(biblioteca):
    #     """Devuelve una lista completa de todos los géneros literarios existentes en la Biblioteca."""
    #     if not biblioteca.especificos:
    #         print("\nNo hay subgéneros literarios registrados en la biblioteca")
    #         return 
    #     print(f"\n- Lista de Subgéneros Literarios -\n")
    #     for especifico in biblioteca.especificos:
    #         print(especifico.mostrar_datos_especifico())
    #         print()

    # def mostrar_especificos_crud(biblioteca):
    #     """Devuelve una lista completa de todos los géneros literarios existentes en la Biblioteca."""
    #     if not biblioteca.especificos:
    #         print("\nNo hay subgéneros literarios registrados en la biblioteca")
    #         return 
    #     print(f"\n- Lista de Subgéneros Literarios -\n")
    #     for especifico in biblioteca.especificos:
    #         print(especifico.mostrar_datos_especifico_crud())
    #         print()


    # def actualizar_especifico(biblioteca):
    #         """Permite actualizar un subgénero literario existente."""

    #         try:
    #             print("\n- Actualizar Subgénero Literario -\n")

    #             genero = input("Introduce el nombre del género literario:\n").strip()
    #             nombre_especifico = input("Introduce el nombre del subgénero literario a actualizar:\n").strip()
    #             tipo = input("Introduce el tipo de subgénero literario:\n").strip()

    #             # Verificación de existencia del subgénero
    #             clave = (genero.lower(), nombre_especifico.lower(), tipo.lower())
    #             if clave not in biblioteca.diccionario_especificos:
    #                 raise ValueError("El subgénero no existe en la biblioteca con ese género y tipo.")

    #             # Obtener el subgénero desde el diccionario
    #             especifico = biblioteca.diccionario_especificos[clave]

    #             # Solo se permiten modificaciones en subgénero y tipo, no en género
    #             nuevo_nombre_genero = input(f"Introduce el nuevo nombre del género [{especifico.get_nombre_genero()}] o presione ENTER si no lo deseas modificar:\n").strip() or especifico.get_nombre_genero()
    #             if nuevo_nombre_genero:
    #                 especifico.set_nombre_genero(nuevo_nombre_genero)

    #             nuevo_nombre_especifico = input(f"Introduce el nuevo nombre del subgénero [{especifico.get_nombre_especifico()}] o presione ENTER si no lo deseas modificar:\n").strip() or especifico.get_nombre_especifico()
    #             if nuevo_nombre_especifico:
    #                 especifico.set_nombre_especifico(nuevo_nombre_especifico)

    #             nuevo_tipo = input(f"Introduce el nuevo tipo del subgénero [{especifico.get_tipo()}] o presione ENTER si no lo deseas modificar:\n").strip() or especifico.get_tipo()
    #             if nuevo_tipo:
    #                 especifico.set_tipo(nuevo_tipo)

    #             print("\nSubgénero actualizado correctamente.")

    #         except ValueError as e:
    #             print(f"\nError: {e}\n")
    #         except Exception as e2:
    #             print(f"\nSe produjo un error inesperado: {e2}\n")

    # def eliminar_especifico(biblioteca):
    #     """Elimina un subgénero literario de la biblioteca búscado por nombre."""

    #     try:
    #         print("\n- Borrado de Registro -\n")
    #         nombre_especifico = input("Introduce el nombre del subgénero literario que deseas borrar:\n")
            
    #         especifico_eliminado = None
    #         for especifico in biblioteca.especificos:
    #             if especifico.get_nombre_especifico().lower() == nombre_especifico.lower():
    #                 especifico_eliminado = especifico
    #                 break # Sale del bucle una vez encontrado el titulo.

    #         if especifico_eliminado:
    #             biblioteca.especificos.remove(especifico_eliminado)  # Elimina el subgénero literario de la lista
    #             print("El registro ha sido eliminado correctamente.")
    #             #return True   ->   # True si se elimina con éxito
    #             biblioteca.reestructurar_ids_especificos()  # Reestructura los ids del resto de registros después de eliminar
    #         else:
    #             print("No se encontró ningún registro con ese nombre.\nCompruebe búsqueda e inténtelo de nuevo.")
    #             #return False  ->  # False si no se encuentra el subgénero.
    #     except Exception as e:                                                     # Errores imprevistos
    #         print(f"\nSe produjo un error al intentar eliminar el subgénero literario: {e}\n")