# deportes/utilidades/utilidades.py

from ..modelos.futbolista import Futbolista
from ..modelos.runner import Runner
from ..modelos.tenista import Tenista

def obtener_datos_comunes():
    """Datos comunes heredados de clase padre."""
    nombre = input("Introduce el nombre:\n")
    edad = int(input("Introduce la edad:\n"))
    nacionalidad = input("Introduce la nacionalidad del deportista:\n")

    return nombre, edad, nacionalidad

def crear_deportista(tipo):
    """Accede a las propiedades de cada Deportista(clase padre) según el tipo (clase hija)"""
    nombre, edad, nacionalidad = obtener_datos_comunes()
    
    if tipo == "futbolista":
        equipo = input("Introduce el equipo:\n")
        goles = int(input("Introduce cantidad de goles:\n"))
        
        return Futbolista(nombre, edad, nacionalidad, equipo, goles)
    
    elif tipo == "tenista":
        ranking = int(input("Introduce el ranking:\n"))
        trofeos_ganados = int(input("Introduce la cantidad de torneos ganados:\n"))
        
        return Tenista(nombre, edad, nacionalidad, ranking, trofeos_ganados)
    
    elif tipo == "runner":
        especialidad = input("Introduce la especialidad:\n")
        record = float(input("Introduce el record de este deportista:\n"))
    
        return Runner(nombre, edad, nacionalidad, especialidad, record)
    else: 
        print("Tipo de deportista no válido.")
        return None

def inicializar_deportistas(deportistas):
    """Inicializa un Deportista por Defecto para la Pruebas de Funcionamiento."""
    # Agregar un futbolista predeterminado
    deportistas['futbolista'].append(Futbolista("Lionel Messi", 36, "Argentina", "Inter Miami", 800))
    # Agregar un tenista predeterminado
    deportistas['tenista'].append(Tenista("Rafael Nadal", 37, "España", 2, 22))
    # Agregar un runner predeterminado
    deportistas['runner'].append(Runner("Usain Bolt", 37, "Jamaica", "100m", 9.58))
    
def modificar_datos(deportistas):
    """Submenú para Modificar Datos de un Deportista."""
    print("\nSeleccione el tipo de deportista que modificar:")
    print("1. Futbolista.")
    print("2. Tenista.")
    print("3. Runner.")
    print("0. Menú Principal.")
    
    opcion = input("Selecciona una opción:\n")
    
    if opcion == "1":
        mostrar_futbolistas(deportistas)
        num = int(input("Selecciona el número del futbolista a modificar:\n")) -1
        
        if 0 <= num < len(deportistas["futbolista"]):
            nuevo_equipo = input("Introduce nuevo equipo:\n")
            nuevo_goles = int(input("Introduce cantidad de goles:\n"))
            deportistas["futbolista"][num].set_equipo(nuevo_equipo)
            deportistas["futbolista"][num].set_goles(nuevo_goles)
        else:
            print("Id Futbolista no válido.")
            
    elif opcion == "2":
        mostrar_tenistas(deportistas)
        num = int(input("Selecciona el número del tenista a modificar:\n")) -1
        
        if 0 <= num < len(deportistas["tenista"]):
            nuevo_trofeos_ganados = int(input("Introduce Trofeos Ganados:\n"))
            nuevo_ranking = int(input("Introduce Ranking:\n"))
            deportistas["tenista"][num].set_trofeos_ganados(nuevo_trofeos_ganados)
            deportistas["tenista"][num].set_ranking(nuevo_ranking)
        else:
            print("Id Tenista no válido.")
    
    elif opcion == "3":
        mostrar_runners(deportistas)
        num = int(input("Selecciona el número del runner a modificar:\n")) -1
        
        if 0 <= num < len(deportistas["runner"]):
            nuevo_record = input("Introduce Record:\n")
            nuevo_especialidad = input("Introduce Especialidad:\n")
            deportistas["runner"][num].set_record(nuevo_record)
            deportistas["runner"][num].set_especialidad(nuevo_especialidad)
        else:
            print("Id Runner no válido.")
            
    elif opcion == "0":
        return # Menú principal
    
    else:
        print("Opción no válida.")
        
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
        
