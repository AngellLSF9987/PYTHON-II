# biblioteca/repositorios/repositorio_especifico.py

def agregar_especifico(self, especifico):
        """Agrega un subgénero literario nuevo a la lista de específicos de la biblioteca."""

        # Verificar si alguno de los valores es None antes de agregar
        if especifico.get_nombre_genero() is None or especifico.get_nombre_especifico() is None or especifico.get_tipo() is None:
            raise ValueError("El nombre del género, el subgénero o el tipo no pueden ser nulos.")

        # Asegurar de que el género existe antes de agregar el subgénero
        genero = especifico.get_nombre_genero().lower()  # Obtener el género en minúsculas
        if genero not in self.diccionario_generos:
            raise ValueError(f"El género '{genero}' no existe en la biblioteca. Por favor, primero agregue el género.")

        # Pasar verificación, se agrega el subgénero
        self.especificos.append(especifico)

        # Crear la clave compuesta o "clave de tupla" para el diccionario (género, subgénero, tipo)
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


def reestructurar_ids_especificos(self):
        for index, especifico in enumerate(self.especificos):
            especifico.set_id(index + 1) # Actualiza los ids, usando el método set_id de forma que vuelvan a ser consecutivos en el resto registros.

def mostrar_especificos(self):
        """Devuelve una lista completa de todos los géneros literarios existentes en la Biblioteca."""
        return [especifico.__str__() for especifico in self.especificos]