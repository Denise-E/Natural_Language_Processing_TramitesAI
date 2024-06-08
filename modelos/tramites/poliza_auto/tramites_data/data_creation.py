import re

def encontrar_posicion_regex(input):#cadena, palabra
    """
     # Patrón para normalizar código postal
        text = text.replace("codigo", "cod")
        text = text.replace("código", "cod")
        # Para que lo remeplace si "pos" viene sólo y no dentro de otra palabra como "postal"
        text = re.sub(r'\bpos\b', 'postal', text)
        text = text.replace("cp", "cod postal")
    """
    for case in input:
        res = {
            'text': case[0].lower(),
            "entities": [],
        }
        
        labels = case[1]
        for label, palabra in labels.items():
            label = label.lower()
            if type(palabra) != str:
                palabra = str(palabra).lower()
            patron = re.escape(palabra)  # Escapar palabra para caracteres especiales
            coincidencia = re.search(patron, case[0].lower())
            if coincidencia:
                res['entities'].append((coincidencia.start(), coincidencia.end(),label))
          
        print(res)

training_data = []
encontrar_posicion_regex(training_data)
