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

training_data = [
    ["Necesito un seguro para mi auto marca: Land Rover, modelo: Range Rover Sport, Año: 2020, Código Postal: 2100.", {"MARCA": "Land Rover", "MODELO": "Range Rover Sport", "AÑO": 2020, "COD_POSTAL": 2100}],
    ["Necesito un seguro para mi auto marca: Land Rover, modelo: Discovery, Año: 2018, Código Postal: 2101.", {"MARCA": "Land Rover", "MODELO": "Discovery", "AÑO": 2018, "COD_POSTAL": 2101}],
    ["Necesito un seguro para mi auto marca: Land Rover, modelo: Defender, Año: 2021, Código Postal: 2102.", {"MARCA": "Land Rover", "MODELO": "Defender", "AÑO": 2021, "COD_POSTAL": 2102}],
    ["Necesito un seguro para mi auto marca: Land Rover, modelo: Range Rover Evoque, Año: 2019, Código Postal: 2103.", {"MARCA": "Land Rover", "MODELO": "Range Rover Evoque", "AÑO": 2019, "COD_POSTAL": 2103}],
    ["Necesito un seguro para mi auto marca: Land Rover, modelo: Range Rover Velar, Año: 2017, Código Postal: 2104.", {"MARCA": "Land Rover", "MODELO": "Range Rover Velar", "AÑO": 2017, "COD_POSTAL": 2104}],
    ["Necesito un seguro para mi auto marca: Land Rover, modelo: Range Rover Vogue, Año: 2022, Código Postal: 2105.", {"MARCA": "Land Rover", "MODELO": "Range Rover Vogue", "AÑO": 2022, "COD_POSTAL": 2105}],
    ["Necesito un seguro para mi auto marca: Land Rover, modelo: Discovery Sport, Año: 2018, Código Postal: 2106.", {"MARCA": "Land Rover", "MODELO": "Discovery Sport", "AÑO": 2018, "COD_POSTAL": 2106}],
    ["Necesito un seguro para mi auto marca: Land Rover, modelo: Range Rover Classic, Año: 2020, Código Postal: 2107.", {"MARCA": "Land Rover", "MODELO": "Range Rover Classic", "AÑO": 2020, "COD_POSTAL": 2107}],
    ["Necesito un seguro para mi auto marca: Land Rover, modelo: Freelander, Año: 2019, Código Postal: 2108.", {"MARCA": "Land Rover", "MODELO": "Freelander", "AÑO": 2019, "COD_POSTAL": 2108}],
    ["Necesito un seguro para mi auto marca: Land Rover, modelo: Range Rover Sport SVR, Año: 2017, Código Postal: 2109.", {"MARCA": "Land Rover", "MODELO": "Range Rover Sport SVR", "AÑO": 2017, "COD_POSTAL": 2109}],
    ["Necesito un seguro para mi auto marca: Lamborghini, modelo: Aventador, Año: 2020, Código Postal: 2000.", {"MARCA": "Lamborghini", "MODELO": "Aventador", "AÑO": 2020, "COD_POSTAL": 2000}],
    ["Necesito un seguro para mi auto marca: Lamborghini, modelo: Huracan, Año: 2018, Código Postal: 2001.", {"MARCA": "Lamborghini", "MODELO": "Huracan", "AÑO": 2018, "COD_POSTAL": 2001}],
    ["Necesito un seguro para mi auto marca: Lamborghini, modelo: Urus, Año: 2021, Código Postal: 2002.", {"MARCA": "Lamborghini", "MODELO": "Urus", "AÑO": 2021, "COD_POSTAL": 2002}],
    ["Necesito un seguro para mi auto marca: Lamborghini, modelo: Gallardo, Año: 2019, Código Postal: 2003.", {"MARCA": "Lamborghini", "MODELO": "Gallardo", "AÑO": 2019, "COD_POSTAL": 2003}],
    ["Necesito un seguro para mi auto marca: Lamborghini, modelo: Centenario, Año: 2017, Código Postal: 2004.", {"MARCA": "Lamborghini", "MODELO": "Centenario", "AÑO": 2017, "COD_POSTAL": 2004}],
    ["Necesito un seguro para mi auto marca: Lamborghini, modelo: Diablo, Año: 2022, Código Postal: 2005.", {"MARCA": "Lamborghini", "MODELO": "Diablo", "AÑO": 2022, "COD_POSTAL": 2005}],
    ["Necesito un seguro para mi auto marca: Lamborghini, modelo: Murcielago, Año: 2018, Código Postal: 2006.", {"MARCA": "Lamborghini", "MODELO": "Murcielago", "AÑO": 2018, "COD_POSTAL": 2006}],
    ["Necesito un seguro para mi auto marca: Lamborghini, modelo: Veneno, Año: 2020, Código Postal: 2007.", {"MARCA": "Lamborghini", "MODELO": "Veneno", "AÑO": 2020, "COD_POSTAL": 2007}],
    ["Necesito un seguro para mi auto marca: Lamborghini, modelo: Sian, Año: 2021, Código Postal: 2008.", {"MARCA": "Lamborghini", "MODELO": "Sian", "AÑO": 2021, "COD_POSTAL": 2008}],
    ["Necesito un seguro para mi auto marca: Lamborghini, modelo: Countach, Año: 2019, Código Postal: 2009.", {"MARCA": "Lamborghini", "MODELO": "Countach", "AÑO": 2019, "COD_POSTAL": 2009}],
    ["Buenas tardes, me gustaría obtener un seguro para mi Kia Sportage 2021 en el código postal 2200.", {"MARCA": "Kia", "MODELO": "Sportage", "AÑO": 2021, "COD_POSTAL": 2200}],
    ["Hola, estoy interesado en asegurar mi Kia Seltos 2020. Mi código postal es 2201.", {"MARCA": "Kia", "MODELO": "Seltos", "AÑO": 2020, "COD_POSTAL": 2201}],
    ["Buenas tardes, necesito un seguro para mi Kia Rio 2018 en el código postal 2202.", {"MARCA": "Kia", "MODELO": "Rio", "AÑO": 2018, "COD_POSTAL": 2202}],
    ["Hola, me gustaría obtener un seguro para mi Kia Telluride 2021. Mi código postal es 2203.", {"MARCA": "Kia", "MODELO": "Telluride", "AÑO": 2021, "COD_POSTAL": 2203}],
    ["Buenas tardes, estoy interesado en asegurar mi Kia Soul 2019. Mi código postal es 2204.", {"MARCA": "Kia", "MODELO": "Soul", "AÑO": 2019, "COD_POSTAL": 2204}],
    ["Hola, necesito cotizar un seguro para mi Kia Optima 2017 en el código postal 2205.", {"MARCA": "Kia", "MODELO": "Optima", "AÑO": 2017, "COD_POSTAL": 2205}],
    ["Buenas tardes, me gustaría obtener un seguro para mi Kia Carnival 2022 en el código postal 2206.", {"MARCA": "Kia", "MODELO": "Carnival", "AÑO": 2022, "COD_POSTAL": 2206}],
    ["Hola, estoy interesado en asegurar mi Kia Forte 2018. Mi código postal es 2207.", {"MARCA": "Kia", "MODELO": "Forte", "AÑO": 2018, "COD_POSTAL": 2207}],
    ["Buenas tardes, necesito un seguro para mi Kia Stinger 2019 en el código postal 2208.", {"MARCA": "Kia", "MODELO": "Stinger", "AÑO": 2019, "COD_POSTAL": 2208}],
    ["Hola, me gustaría obtener un seguro para mi Kia Niro 2020 en el código postal 2209.", {"MARCA": "Kia", "MODELO": "Niro", "AÑO": 2020, "COD_POSTAL": 2209}],
    ["Buenas tardes, estoy interesado en un seguro para mi Jeep Wrangler 2020 en el código postal 2100.", {"MARCA": "Jeep", "MODELO": "Wrangler", "AÑO": 2020, "COD_POSTAL": 2100}],
    ["Hola, me gustaría obtener un seguro para mi Jeep Grand Cherokee 2019. Mi código postal es 2101.", {"MARCA": "Jeep", "MODELO": "Grand Cherokee", "AÑO": 2019, "COD_POSTAL": 2101}],
    ["Buenas tardes, necesito un seguro para mi Jeep Renegade 2018 en el código postal 2102.", {"MARCA": "Jeep", "MODELO": "Renegade", "AÑO": 2018, "COD_POSTAL": 2102}],
    ["Hola, estoy interesado en asegurar mi Jeep Compass 2021. Mi código postal es 2103.", {"MARCA": "Jeep", "MODELO": "Compass", "AÑO": 2021, "COD_POSTAL": 2103}],
    ["Buenas tardes, me gustaría obtener un seguro para mi Jeep Cherokee 2019 en el código postal 2104.", {"MARCA": "Jeep", "MODELO": "Cherokee", "AÑO": 2019, "COD_POSTAL": 2104}],
    ["Hola, necesito cotizar un seguro para mi Jeep Gladiator 2017 en el código postal 2105.", {"MARCA": "Jeep", "MODELO": "Gladiator", "AÑO": 2017, "COD_POSTAL": 2105}],
    ["Buenas tardes, estoy interesado en asegurar mi Jeep Wrangler Rubicon 2022. Mi código postal es 2106.", {"MARCA": "Jeep", "MODELO": "Wrangler Rubicon", "AÑO": 2022, "COD_POSTAL": 2106}],
    ["Hola, me gustaría obtener un seguro para mi Jeep Patriot 2018 en el código postal 2107.", {"MARCA": "Jeep", "MODELO": "Patriot", "AÑO": 2018, "COD_POSTAL": 2107}],
    ["Buenas tardes, necesito un seguro para mi Jeep Commander 2019. Mi código postal es 2108.", {"MARCA": "Jeep", "MODELO": "Commander", "AÑO": 2019, "COD_POSTAL": 2108}],
    ["Hola, estoy interesado en asegurar mi Jeep Wagoneer 2020 en el código postal 2109.", {"MARCA": "Jeep", "MODELO": "Wagoneer", "AÑO": 2020, "COD_POSTAL": 2109}]
]














encontrar_posicion_regex(training_data)
