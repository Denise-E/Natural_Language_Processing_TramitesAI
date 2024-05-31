import re

def encontrar_posicion_regex(input):#cadena, palabra
    for case in input:
        res = {
            'text': case[0],
            "entities": [],
        }
        
        labels = case[1]
        for label, palabra in labels.items():
            patron = re.escape(palabra)  # Escapar palabra para caracteres especiales
            coincidencia = re.search(patron, case[0])
            if coincidencia:
                res['entities'].append((coincidencia.start(), coincidencia.end(),label))
          
        print(res)

training_data = [
    ["buenas tardes, quisiera cotizar un seguro para mi auto por favor, envíenme las diferentes opciones que su compañia ofrece los datos de mi vehiculo son  marca chevrolet  modelo spin  año 2023 cod postal 1414  tengo cochera propia adjunto también foto de mi vehiculo para que se vea que está en perfectas condiciones muchas gracias",
    {'MARCA': 'chevrolet', 'MODELO':'spin', 'AÑO': '2023', 'COD_POSTAL':'1414'}],
    ["hola, necesito un seguro para mi auto marca ford modelo fiesta año 2019 código postal 5000 gracias",
    {'MARCA': 'ford', 'MODELO':'fiesta', 'AÑO': '2019','COD_POSTAL': '5000'}]
]

encontrar_posicion_regex(training_data)


'''cadena = "hola, necesito un seguro para mi auto marca ford modelo fiesta año 2019 código postal 5000 gracias"
palabra = 'ford'
posicion = encontrar_posicion_regex(cadena, palabra)
print("MARCA", posicion)

palabra = 'fiesta'
posicion = encontrar_posicion_regex(cadena, palabra)
print("MODELO",posicion)

palabra = '2019'
posicion = encontrar_posicion_regex(cadena, palabra)
print("AÑO", posicion)

palabra = '5000'
posicion = encontrar_posicion_regex(cadena, palabra)
print("COD_POSTAL", posicion)'''