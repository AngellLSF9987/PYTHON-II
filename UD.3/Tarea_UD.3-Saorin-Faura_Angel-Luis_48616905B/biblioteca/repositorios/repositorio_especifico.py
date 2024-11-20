# biblioteca/repositorios/repositorio_especifico.py

import json
class RepositorioEspecifico:
    def __init__(self, repositorio_genero):
        """
        Constructor del repositorio de específicos.
        :param repositorio_genero: Instancia de RepositorioGenero.
        """
        self.repositorio_genero = repositorio_genero
        self.especificos = []  # Lista para almacenar instancias de Especifico

    def cargar_especificos(self, datos_especificos):
        """Carga los datos de los Subgéneros Literarios específicos desde el JSON en la memoria del repositorio."""

        try:
            self.especificos = []
            for especifico in datos_especificos:
                genero = self.repositorio_genero.obtener_genero_por_id(especifico["genero_id"])
                if genero is None:
                    print(f"Aviso: No se encontró un género con ID {especifico['genero_id']}.")
                    nombre_genero = "Género desconocido"
                else:
                    nombre_genero = genero["nombre_genero"]

                self.especificos.append({
                    "especifico_id": especifico["especifico_id"],
                    "genero_id": especifico["genero_id"],
                    "nombre_genero": nombre_genero,
                    "nombre_especifico": especifico["nombre_especifico"],
                    "tipo": especifico.get("tipo", "Sin especificar"),
                })
            print("Carga de datos de Subgéneros Literarios Específicos correcta.")

        except KeyError as KeyEspecificoError:
            print(f"{KeyEspecificoError}: Falta la clave o no coincide en los datos de un Subgénero Literario Específico.")
        except FileExistsError as DictEspecificoError:
            print(f"{DictEspecificoError}: La sección de datos pertenciente a Subgéneros Literarios Específicos registrados no ha sido cargada correctamente.")
    
    def mostrar_especificos(self):
        """Devuelve la lista de subgéneros específicos en el repositorio."""
        if not self.especificos:
            return "No hay subgéneros específicos cargados en el repositorio."
        
        return "\n".join(
            f"ID: {especifico['especifico_id']}\nNombre del Subgénero: {especifico['nombre_especifico']}\n"
            f"Tipo: {especifico['tipo']}\n"
            f"Género Asociado: {especifico['nombre_genero']}\n"
            for especifico in self.especificos
        )

    def obtener_especifico_por_id(self, especifico_id):
        """
        Busca un subgénero específico por su ID.
        :param id_especifico: ID del subgénero específico.
        :return: Diccionario con los datos del subgénero si se encuentra, None en caso contrario.
        """
        for especifico in self.especificos:
            if especifico["especifico_id"] == especifico_id:
                return especifico
        return None