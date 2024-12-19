import json

# Crear un diccionario

productos = [
    {"Refrescos": 
        {{"Nombre": "Coca-Cola", "Precio": "2.40"},
        {"Nombre": "Fanta Naranja", "Precio": "2.00"},
        {"Nombre": "Fanta Limón", "Precio":"2.00"}}
    },
    {"Conservas": 
        {{"Nombre": "Berberechos", "Precio": "7.49"},
        {"nombre": "Mejillones", "Precio": "6.49"}}
    },
    {"Galleta": 
        {{"Marca": "Fontaneda", "Nombre": "María Tostada", "Precio": "2.50"},
        {"Marca": "Cuétara", "Nombre": "Chiquilín", "Precio": "2.30"}}   
    }
]

print(productos)

# Escribir en fichero compras.json

def escribir():

    try:
        # Leer 
            
        with open (r"UD.3\ejemplos_json\ejemplo_9\compras.json", "w", encoding="utf-16", newline="") as compras:
            json.dump(productos, compras, indent=4) # Indent facilita la lectura. Lo normal se usa con valor 4

    except FileExistsError:
        print("Error1: Fichero no accesible o línea no escrita.")
        
escribir()

# # IMPRIMIR JSON FORMATEADO

# def imp_formateado():
    

#     try:   
#         # Leer
#         with open (r"UD.3\ejemplos_json\ejemplo_9\compras-json", "a", encoding="utf-8") as compras:
#             fichero = json.load(compras)
            
#             for fila in fichero:
#                 print(f"Nombre:{[0]}: {fila[0]} | {encabezado[1]}: {fila[1]} | {encabezado[2]}: {fila[2]} | {encabezado[3]}: {fila[3]} | {encabezado[4]}: {fila[4]} \
#                     {encabezado[5]}: {fila[5]} | {encabezado[6]}: {fila[6]} | {encabezado[7]}: {fila[7]}")
#     except FileNotFoundError:
#         print("Error: No se ha encontrado al archivo.\n")

#     except Exception as e:
#         print(f"Error: {e}")   

# imp_formateado()