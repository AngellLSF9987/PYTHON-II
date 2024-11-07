# ejemplo_3/galleta/metodos/metodos.py

from modelos.galleta import Galleta

def leer_galletas(ruta_archivo):
    """
    Leer datos del fichero. 
    Usa una lista vacía como mecanismo de 
    almacenamiento para su posterior lectura por líneas.
    """
    mis_galletitas = []
    
    with open(ruta_archivo, "r", encoding="utf-8") as leer_lista:
        for linea in leer_lista:
            
            linea = linea.strip()                                     # Eliminar espacios en blanco  antes y después
            
            if linea and "," in linea:
                marca, sabor = linea.strip().split(",", 1)                # Dividir en marca y sabor teniendo en cuenta el caracter coma(,) como elemento de separación
                galleta = Galleta(marca.strip(), sabor.strip())           # Crear una instancia de Galleta 

                mis_galletitas.append(galleta)                            # Añadir galletas a la lista
            else:
                print(f"Ojo! La línea no tiene el formato correcto de {linea}")
            
    return mis_galletitas                                                 # Retornar la lista de mis_galletitas


def mas_galletas():
    """
    Añadir nuevas galletas al archivo.
    Asegurarse de que no haya duplicados.
    """
    nuevas_galletas = [
        "Chips Ahoy, Vainilla",
        "Príncipe, Fresa"
    ]
    
    ruta_archivo = r"C:\Users\tarde\Desktop\PYTHON-II\UD.3\ejemplo_3\galleta\datos\datos_galletas.txt"
    galletas_existentes = leer_galletas(ruta_archivo)
    
    galletas_existentes_str = [f"{galleta.get_marca()}, {galleta.get_sabor()}" for galleta in galletas_existentes]  # Convertir el objeto galleta a string, cuando se recorrero el fichero, para su comparación interna de su existencia. 
    
    # Abre el archivo en modo append para añadir nuevas galletas(objeto)
    with open(ruta_archivo, "a", encoding = "utf-8") as añadir:
        for galleta in nuevas_galletas:
            
            # Si el objeto galleta no existe, lo añade
            if galleta not in galletas_existentes_str:
                añadir.write(galleta + "\n")
            else:
                print(f"La galleta {galleta} ya existe en el fichero.")
    
    print("Galletas añadidas.")
            