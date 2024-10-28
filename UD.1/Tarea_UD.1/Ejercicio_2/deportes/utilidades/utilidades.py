from modelos.futbolista import Futbolista
from modelos.runner import Runner
from modelos.tenista import Tenista

def obtener_datos_comunes():
    
    nombre = input("Introduce el nombre:\n")
    edad = int(input("Introduce la edad:\n"))
    nacionalidad = input("Introduce el sexo (H/M):\n")

    return nombre, edad, nacionalidad

def crear_deportista(tipo):
    
    nombre,edad, nacionalidad = obtener_datos_comunes()
    
    if tipo == "futbolista":
        equipo = input("Introduce el equipo:\n")
        goles = input("Introduce cantidad de goles:\n")
        
        return Futbolista(nombre, edad, nacionalidad, equipo, goles)
    
    elif tipo == "tenista":
        ranking = input("Introduce el ranking:\n")
        trofeos_ganados = input("Introduce la cantidad de torneos ganados:\n")
        
        return Tenista(nombre, edad, nacionalidad, ranking, trofeos_ganados)
    
    elif tipo == "runner":
        especialidad = input("Introduce la especialidad:\n")
        record = input("Introduce el record de este deportista:\n")
    
        return Runner(nombre, edad, nacionalidad, especialidad, record)
    else: 
        print("Tipo de deportista no válido.")
        return None
    
    
    