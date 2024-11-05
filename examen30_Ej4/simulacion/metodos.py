# examen30_Ej4/simulacion/metodos.py

from ..modelos.lima import Lima
from ..modelos.pincel import Pincel
from ..modelos.esmalte import Esmalte
from ..modelos.uña import Uña 

def aplicar_manicura_basica(uñas, esmaltes):
    
    lima = Lima()
    
    print("\n- Limando las uñas -\n")
    
    for uña in uñas:
        lima.usar()
        uña.estado_uña()
        
        print("\n- Aplicando esmlates en las uñas -\n")
        
        for i, uña in enumerate(uñas):
            esmalte = esmaltes[i % len(esmaltes)]
            uña.aplicar_esmalte(esmalte)
            
    pincel = Pincel()
    
    print("\n- Usando el pincel -\n")
    
    pincel.usar()
        