# biblioteca/repositorios/repositorio_especifico.py

from biblioteca.utilidades.lector_json import cargar_datos_json
from biblioteca.modelos.generos.especifico import Especifico

class RepositorioEspecifico:
    
    def __init__(self, repositorio_genero):
        # Inicializa las listas y el diccionario donde se almacenarán los géneros específicos
        self.especificos = []
        self.diccionario_especificos = {}
        self.repositorio_genero = repositorio_genero  # Guardamos el repositorio de géneros

    def cargar_especificos(self, datos_biblioteca):
        """
        Carga los géneros específicos desde un archivo JSON utilizando la función cargar_datos_json.
        """
        # Cargar los datos desde el archivo JSON
        datos = cargar_datos_json(datos_biblioteca)
        
        # Si los datos no son válidos (diccionario vacío), termina la función
        if not datos:
            return
        
        # Recorrer la lista de géneros específicos en el JSON
        for especifico_data in datos.get("especificos", []):
            # Crea un nuevo género específico usando los datos del JSON
            nuevo_especifico = Especifico(
                especifico_data["nombre_genero"],  # Nombre del género (heredado de la clase Genero)
                especifico_data["nombre_especifico"],
                especifico_data["tipo"]
            )
            
            # Añadir el nuevo género específico a la lista
            self.especificos.append(nuevo_especifico)
            
            # Crear una clave compuesta con el nombre del género, subgénero y tipo para el diccionario
            clave = (
                nuevo_especifico.get_nombre_genero().lower(),  # Género en minúsculas
                nuevo_especifico.get_nombre_especifico().lower(),  # Subgénero en minúsculas
                nuevo_especifico.get_tipo().lower()  # Tipo en minúsculas
            )
            
            # Añadir el género específico al diccionario usando la clave compuesta
            self.diccionario_especificos[clave] = nuevo_especifico

        print(f"Géneros específicos cargados desde {datos_biblioteca}")
        
    def agregar_especifico(self, especifico):
        """Agrega un subgénero literario nuevo a la lista de específicos de la biblioteca."""
        
        # Verificar si alguno de los valores es None antes de agregar
        if especifico.get_nombre_genero() is None or especifico.get_nombre_especifico() is None or especifico.get_tipo() is None:
            raise ValueError("El nombre del género, el subgénero o el tipo no pueden ser nulos.")
        
        # Asegurar de que el género existe antes de agregar el subgénero
        genero = especifico.get_nombre_genero().lower()  # Obtener el género en minúsculas
        if genero not in self.repositorio_genero.diccionario_generos:  # Asegurarse de que el género existe
            raise ValueError(f"El género '{genero}' no existe en la biblioteca. Por favor, primero agregue el género.")
        
        # Si pasa la validación, se agrega el subgénero
        self.especificos.append(especifico)

        # Crear la clave compuesta para el diccionario (género, subgénero, tipo)
        clave = (
            especifico.get_nombre_genero().lower(),
            especifico.get_nombre_especifico().lower(),
            especifico.get_tipo().lower()
        )
        
        # Almacenar el objeto 'Especifico' en el diccionario usando la clave compuesta
        self.diccionario_especificos[clave] = especifico
        print(f"Subgénero '{especifico.get_nombre_especifico()}' agregado correctamente al género '{especifico.get_nombre_genero()}'.")
    
    def buscar_especifico_nombre(self, nombre_genero, nombre_especifico, tipo):
        """Busca un subgénero literario por su género, nombre específico y tipo en el diccionario."""
        
        # Crear la clave compuesta con los tres parámetros
        clave = (
            nombre_genero.lower(),
            nombre_especifico.lower(),
            tipo.lower()
        )
        
        # Buscar en el diccionario usando la clave
        return self.diccionario_especificos.get(clave, None)
    
    def mostrar_especificos(self):
        """Devuelve una lista completa de todos los géneros literarios específicos existentes en la Biblioteca."""
        return [especifico.__str__() for especifico in self.especificos]

    def reestructurar_ids_especificos(self):
        """Reestructura los IDs de los géneros específicos, haciendo que sean consecutivos."""
        for index, especifico in enumerate(self.especificos):
            especifico.set_id(index + 1)  # Actualiza los ids, haciendo que empiecen desde 1
