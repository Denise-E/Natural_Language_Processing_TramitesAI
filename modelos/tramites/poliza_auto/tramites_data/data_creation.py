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
            palabra = palabra.lower()
            patron = re.escape(palabra)  # Escapar palabra para caracteres especiales
            coincidencia = re.search(patron, case[0].lower())
            if coincidencia:
                res['entities'].append((coincidencia.start(), coincidencia.end(),label))
          
        print(res)

training_data = [
    ["buenas tardes, quisiera cotizar un seguro para mi auto por favor, envíenme las diferentes opciones que su compañia ofrece los datos de mi vehiculo son  marca chevrolet  modelo spin  año 2023 cod postal 1414  tengo cochera propia adjunto también foto de mi vehiculo para que se vea que está en perfectas condiciones muchas gracias",
    {'MARCA': 'chevrolet', 'MODELO':'spin', 'ANIO': '2023', 'COD_POSTAL':'1414'}]
]

print(len(training_data))
encontrar_posicion_regex(training_data)

"""
Formato 
 TRAIN_DATA = [(
    {"text": "buenas tardes, quisiera cotizar un seguro para mi auto por favor, envíenme las diferentes opciones que su compañia ofrece los datos de mi vehiculo son  marca chevrolet  modelo spin  año 2023 cod postal 1414  tengo cochera propia adjunto también foto de mi vehiculo para que se vea que está en perfectas condiciones muchas gracias", 
        "entities": [(108, 118, "MARCA"), (120, 124, "MODELO"), (126, 130, "AÑO"), (132, 140, "COD_POSTAL")]}
    )],
"""