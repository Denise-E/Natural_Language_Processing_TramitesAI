TRAIN_DATA = [
    (
        {"text": "buenas tardes, quisiera cotizar un seguro para mi auto por favor, envíenme las diferentes opciones que su compañia ofrece los datos de mi vehiculo son  marca chevrolet  modelo spin  año 2023 cod postal 1414  tengo cochera propia adjunto también foto de mi vehiculo para que se vea que está en perfectas condiciones muchas gracias", 
        "entities": [(108, 118, "MARCA"), (120, 124, "MODELO"), (126, 130, "AÑO"), (132, 140, "COD_POSTAL")]}
    ),
    (
        {"text": "hola, necesito un seguro para mi auto marca ford modelo fiesta año 2019 código postal 5000 gracias",
        "entities": [(44, 48, "MARCA"), (54, 60, "MODELO"), (65, 69, "AÑO"), (82, 86, "COD_POSTAL")]}
    ),
    (
        {"text": "buen día, quisiera saber cuánto me cuesta un seguro para mi coche marca toyota modelo corolla año 2015 cod. postal 28001 gracias",
        "entities": [(57, 62, "MARCA"), (70, 77, "MODELO"), (82, 86, "AÑO"), (99, 105, "COD_POSTAL")]}
    ),
    (
        {"text": "necesito asegurar mi vehículo, es un honda civic del año 2020, código postal 90210",
        "entities": [(34, 39, "MARCA"), (40, 45, "MODELO"), (54, 58, "AÑO"), (75, 80, "COD_POSTAL")]}
    ),
    (
        {"text": "buenos días, quisiera información sobre seguros para un nissan sentra del 2018, vivo en el código postal 12345",
        "entities": [(54, 60, "MARCA"), (61, 67, "MODELO"), (72, 76, "AÑO"), (95, 100, "COD_POSTAL")]}
    ),
    (
        {"text": "quiero asegurar un auto marca peugeot modelo 208 año 2021, mi código postal es 54321",
        "entities": [(28, 35, "MARCA"), (44, 47, "MODELO"), (53, 57, "AÑO"), (76, 81, "COD_POSTAL")]}
    ),
    (
        {"text": "hola, estoy buscando opciones de seguro para un volkswagen gol del año 2017, código postal 98765",
        "entities": [(42, 51, "MARCA"), (52, 55, "MODELO"), (64, 68, "AÑO"), (83, 88, "COD_POSTAL")]}
    ),
    (
        {"text": "saludos, necesito un seguro para mi automóvil marca bmw modelo serie 3 año 2016 cod postal 11223",
        "entities": [(48, 51, "MARCA"), (59, 66, "MODELO"), (71, 75, "AÑO"), (86, 91, "COD_POSTAL")]}
    ),
    (
        {"text": "buenas noches, quisiera información para asegurar un kia rio del 2014, código postal 33445",
        "entities": [(47, 50, "MARCA"), (51, 54, "MODELO"), (59, 63, "AÑO"), (80, 85, "COD_POSTAL")]}
    ),
    (
        {"text": "hola, necesito cotizar un seguro para mi coche marca hyundai modelo elantra del año 2022, vivo en el código postal 77889",
        "entities": [(38, 44, "MARCA"), (52, 59, "MODELO"), (68, 72, "AÑO"), (91, 96, "COD_POSTAL")]}
    ),
    (
        {"text": "quiero un seguro para mi coche. Marca: Renault, Modelo: Kwid, Año: 2019. Código Postal: 67890.",
        "entities": [(31, 38, "MARCA"), (48, 52, "MODELO"), (59, 63, "AÑO"), (79, 84, "COD_POSTAL")]}
    ),
    (
        {"text": "necesito un seguro para mi automóvil. marca mazda, modelo cx-5, año 2018, cp 11011",
        "entities": [(38, 43, "MARCA"), (52, 55, "MODELO"), (61, 65, "AÑO"), (70, 75, "COD_POSTAL")]}
    ),
    (
        {"text": "hola, busco un seguro para un coche de marca suzuki modelo swift año 2016, código postal 12349",
        "entities": [(39, 45, "MARCA"), (53, 58, "MODELO"), (63, 67, "AÑO"), (84, 89, "COD_POSTAL")]}
    ),
    (
        {"text": "cotización de seguro para automóvil marca mitsubishi, modelo lancer, año 2014, código postal 55555",
        "entities": [(33, 42, "MARCA"), (51, 57, "MODELO"), (63, 67, "AÑO"), (84, 89, "COD_POSTAL")]}
    ),
    (
        {"text": "quiero cotizar seguro para mi auto marca fiat, modelo cronos, año 2021, mi código postal es 22334",
        "entities": [(32, 36, "MARCA"), (45, 51, "MODELO"), (57, 61, "AÑO"), (82, 87, "COD_POSTAL")]}
    ),
    (
        {"text": "buenas, me interesa un seguro para mi auto fiat cronos 2020, vivo en el código postal 1414",
        "entities": [(39, 43, "MARCA"), (44, 50, "MODELO"), (51, 55, "AÑO"), (77, 81, "COD_POSTAL")]}
    ),
    (
        {"text": "hola, quiero asegurar mi coche, que es un ford fiesta del 2018. código postal 5000.",
        "entities": [(34, 38, "MARCA"), (39, 45, "MODELO"), (51, 55, "AÑO"), (72, 76, "COD_POSTAL")]}
    ),
    (
        {"text": "buenos días, quisiera cotizar un seguro para mi volkswagen gol 2017. mi código postal es 98765.",
        "entities": [(42, 51, "MARCA"), (52, 55, "MODELO"), (56, 60, "AÑO"), (79, 84, "COD_POSTAL")]}
    ),
    (
        {"text": "necesito información para asegurar mi bmw serie 3 2016. Vivo en el código postal 11223.",
        "entities": [(36, 39, "MARCA"), (40, 47, "MODELO"), (48, 52, "AÑO"), (72, 77, "COD_POSTAL")]}
    ),
    (
        {"text": "me gustaría cotizar un seguro para mi chevrolet spin del 2023, código postal 1414",
        "entities": [(35, 45, "MARCA"), (46, 50, "MODELO"), (55, 59, "AÑO"), (74, 78, "COD_POSTAL")]}
    ),
    (
        {"text": "hola, busco asegurar mi coche toyota corolla año 2015 cp 28001",
        "entities": [(29, 34, "MARCA"), (35, 42, "MODELO"), (47, 51, "AÑO"), (54, 59, "COD_POSTAL")]}
    ),
    (
        {"text": "saludos, quisiera asegurar mi auto nissan sentra 2018. Vivo en el código postal 12345",
        "entities": [(33, 39, "MARCA"), (40, 46, "MODELO"), (47, 51, "AÑO"), (71, 76, "COD_POSTAL")]}
    ),
    (
        {"text": "buen día, necesito cotizar un seguro para mi auto peugeot 208 año 2021, cp 54321",
        "entities": [(41, 48, "MARCA"), (49, 52, "MODELO"), (57, 61, "AÑO"), (66, 71, "COD_POSTAL")]}
    ),
    (
        {"text": "necesito un seguro para mi coche volkswagen gol 2017, código postal 98765",
        "entities": [(29, 38, "MARCA"), (39, 42, "MODELO"), (43, 47, "AÑO"), (63, 68, "COD_POSTAL")]}
    ),
    (
        {"text": "quiero asegurar mi automóvil bmw serie 3 del 2016. Mi código postal es 11223.",
        "entities": [(26, 29, "MARCA"), (30, 37, "MODELO"), (42, 46, "AÑO"), (66, 71, "COD_POSTAL")]}
    ),
    (
        {"text": "hola, necesito información sobre seguros para mi auto kia rio del 2014, vivo en el código postal 33445",
        "entities": [(52, 55, "MARCA"), (56, 59, "MODELO"), (64, 68, "AÑO"), (85, 90, "COD_POSTAL")]}
    ),
    (
        {"text": "cotización de seguro para automóvil hyundai elantra 2022. Código postal 77889",
        "entities": [(33, 39, "MARCA"), (40, 47, "MODELO"), (48, 52, "AÑO"), (66, 71, "COD_POSTAL")]}
    ),
    (
        {"text": "necesito asegurar mi coche renault kwid del 2019, cp 67890",
        "entities": [(29, 36, "MARCA"), (37, 41, "MODELO"), (46, 50, "AÑO"), (55, 60, "COD_POSTAL")]}
    ),
    (
        {"text": "hola, quiero cotizar un seguro para mi auto fiat cronos 2021. Mi código postal es 22334",
        "entities": [(39, 43, "MARCA"), (44, 50, "MODELO"), (51, 55, "AÑO"), (75, 80, "COD_POSTAL")]}
    ),
    (
        {"text": "necesito un seguro para mi automóvil, marca mazda, modelo cx-5, año 2018, cp 11011",
        "entities": [(38, 43, "MARCA"), (52, 55, "MODELO"), (61, 65, "AÑO"), (70, 75, "COD_POSTAL")]}
    ),
    (
        {"text": "hola, busco un seguro para un coche de marca suzuki modelo swift año 2016, código postal 12349",
        "entities": [(39, 45, "MARCA"), (53, 58, "MODELO"), (63, 67, "AÑO"), (84, 89, "COD_POSTAL")]}
    ),
    (
        {"text": "quiero cotizar seguro para mi auto marca fiat, modelo cronos, año 2021, mi código postal es 22334",
        "entities": [(32, 36, "MARCA"), (45, 51, "MODELO"), (57, 61, "AÑO"), (82, 87, "COD_POSTAL")]}
    )
]
