import csv

def leer():

    try:   
        # Leer
        with open (r"UD.3\ejemplo_7_csv\perros.csv", "r", encoding="utf-8") as a_csv:
            lector_csv = csv.reader(a_csv)
            
            # Almacenar los encabezados en una lista
            encabezado = next(lector_csv)
            
            for fila in lector_csv:
                print(f"{encabezado[0]}: {fila[0]} | {encabezado[1]}: {fila[1]} | {encabezado[2]}: {fila[2]} | {encabezado[3]}: {fila[3]} | {encabezado[4]}: {fila[4]} \
                    {encabezado[5]}: {fila[5]} | {encabezado[6]}: {fila[6]} | {encabezado[7]}: {fila[7]}")
    except FileNotFoundError:
        print("Error: No se ha encontrado al archivo.\n")

    except Exception as e:
        print(f"Error: {e}")
    
# Añadir una lista

def escribir():

    try:
        # Leer 
            
        with open (r"UD.3\ejemplo_7_csv\perros.csv", "a", encoding="utf-8", newline="") as a_csv:
            escribrir_csv = csv.writer(a_csv)
            nueva_fila = ["Locky",10,"Golden Retriever",30,"Grande","Blanco Dorado","No","Sí"]
            escribrir_csv.writerow(nueva_fila)
            
    except FileExistsError:
        print("Error: Fichero no accesible o línea no escrita.")

# Modificar

def modificar():
    
    try:
        
        with open (r"UD.3\ejemplo_7_csv\perros.csv", "r", encoding="utf-8") as a_csv:
            lector_csv = csv.reader(a_csv)
            
            filas = list(lector_csv)
            print(filas)
            
        nuevo_peso = 23.7
        filas[12][3] = nuevo_peso
        
        
        # Escribir
        with open (r"UD.3\ejemplo_7_csv\perros.csv", "w", encoding="utf-8", newline="") as a_csv:
            escribrir_csv = csv.writer(a_csv)
            escribrir_csv.writerows(filas)
        
    
    except FileNotFoundError:
        print("Error: El fichero no se ha encontrado.\n")
    except FileExistsError:
        print("Error: Fila no accesible o la información dada es errónea.")

leer()
escribir()
modificar()