# deportes/utilidades/utilidades.py

from ..modelos.futbolista import Futbolista
from ..modelos.runner import Runner
from ..modelos.tenista import Tenista

def obtener_datos_comunes():
    """Datos comunes heredados de clase padre."""
    nombre = input("Introduce el nombre:\n")
    apellido = input("Introduce el apellido:\n")    
    edad = int(input("Introduce la edad:\n"))
    nacionalidad = input("Introduce la nacionalidad del deportista:\n")

    return nombre, apellido, edad, nacionalidad

def crear_deportista(tipo):
    """Accede a las propiedades de cada Deportista(clase padre) según el tipo (clase hija)"""
    nombre, apellido, edad, nacionalidad = obtener_datos_comunes()
    
    if tipo == "futbolista":
        equipo = input("Introduce el equipo:\n")
        goles = int(input("Introduce cantidad de goles:\n"))
        
        return Futbolista(nombre, apellido, edad, nacionalidad, equipo, goles)
    
    elif tipo == "tenista":
        ranking = int(input("Introduce el ranking:\n"))
        trofeos_ganados = int(input("Introduce la cantidad de torneos ganados:\n"))
        
        return Tenista(nombre, apellido, edad, nacionalidad, ranking, trofeos_ganados)
    
    elif tipo == "runner":
        especialidad = input("Introduce la especialidad:\n")
        record = float(input("Introduce el record de este deportista:\n"))
    
        return Runner(nombre, apellido, edad, nacionalidad, especialidad, record)
    else: 
        print("Tipo de deportista no válido.")
        return None

def inicializar_deportistas(deportistas):
    """Inicializa un Deportista por Defecto para la Pruebas de Funcionamiento."""
    # Agregar un futbolista predeterminado
    deportistas['futbolista'].append(Futbolista("Lionel", "Messi", 36, "Argentina", "Inter Miami", 800))
    # Agregar un tenista predeterminado
    deportistas['tenista'].append(Tenista("Rafael", "Nadal", 37, "España", 2, 22))
    # Agregar un runner predeterminado
    deportistas['runner'].append(Runner("Usain", "Bolt", 37, "Jamaica", "100m", 9.58))
        
def mostrar_futbolistas(deportistas):
    """Mostrar los Dato de Todos los Futbolistas Registrados."""
    for futbolista in deportistas['futbolista']:
        print(futbolista.mostrar_datos())

def mostrar_tenistas(deportistas):
    """Mostrar los Dato de Todos los Tenistas Registrados."""
    for tenista in deportistas['tenista']:
        print(tenista.mostrar_datos())
        
def mostrar_runners(deportistas):
    """Mostrar los Dato de Todos los Runners Registrados."""
    for runner in deportistas['runner']:
        print(runner.mostrar_datos())
        
def mostrar_deportistas(deportistas):
    """Muestra todos los Deportistas existentes de cada tipo."""
    for tipo, lista_deportistas in deportistas.items():
        print(f"\n{tipo.capitalize()}s:")
        for deportista in  lista_deportistas:
            print(deportista.mostrar_datos())
            print()
        
