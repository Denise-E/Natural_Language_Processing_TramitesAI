import re

def encontrar_posicion_regex(input):#cadena, palabra
    for case in input:
        res = {
            'text': case[0], #.lower()
            "entities": [],
        }
        
        labels = case[1]
        for label, palabra in labels.items():
            #label = label.lower()
            if type(palabra) != str:
                palabra = str(palabra) #.lower()
            patron = re.escape(palabra)  # Escapar palabra para caracteres especiales
            coincidencia = re.search(patron, case[0]) #.lower()
            if coincidencia:
                res['entities'].append((coincidencia.start(), coincidencia.end(),label))
          
        print(res)

training_data = []

encontrar_posicion_regex(training_data)
