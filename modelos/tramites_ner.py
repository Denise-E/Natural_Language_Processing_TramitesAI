"""
Tengo 2 situaciones:
    1. Saco info de los textos extraidos de documentos
        * (1) Denuncia Siniestro
            -> En la denuncia policial encuentro datos
        * (4) Carga presupuestos
            -> En el presupuesto encuentro datos
    
    2. Saco info de los bodys, que son escritos libremente por quienes envian sus solicitudes 
        * (2) Cotización póliza de auto
            -> En el body encuentro datos
        * (3) Cotización póliza del hogar
            -> En el body encuentro datos

Para esto voy a usar expresiones regulares y técnicas de reconocimiento de entidades nombradas (NER)
El Reconocimiento de Entidades Nombradas puede identificar entidades basadas en el contexto y patrones aprendidos durante el entrenamiento, lo que lo hace más adaptable y robusto.     
"""
import random
import re
import spacy
from spacy.util import minibatch, compounding

class ValidacionTramites:
    nlp = None
    @classmethod
    def __init__(cls):
        cls.train_nep_model()
    
    @classmethod
    def train_nep_model(cls) -> None:
        # Cargar el modelo de spacy para español
        cls.nlp = spacy.load("es_core_news_sm")
        # Agregar un componente de NER al pipeline si aún no está presente
        if 'ner' not in cls.nlp.pipe_names:
            ner = cls.nlp.create_pipe('ner')
            cls.nlp.add_pipe(ner, last=True)
        else:
            ner = cls.nlp.get_pipe('ner')

        # Agregar las etiquetas de entidades deseadas al modelo
        ner.add_label("MARCA")
        ner.add_label("MODELO")
        ner.add_label("AÑO")
        ner.add_label("COD_POSTAL")

        # Preparar los datos de entrenamiento (reemplaza esto con tu propio conjunto de datos etiquetados)
        TRAIN_DATA = [
            ("buenas tardes, quisiera cotizar un seguro para mi auto por favor, envíenme las diferentes opciones que su compañia ofrece los datos de mi vehiculo son  marca chevrolet  modelo spin  año 2023 cod postal 1414  tengo cochera propia adjunto también foto de mi vehiculo para que se vea que está en perfectas condiciones muchas gracias", 
            {"entities": [(28, 38, "MARCA"), (39, 47, "MODELO"), (48, 52, "AÑO"), (53, 61, "COD_POSTAL")]}),
            # Agregar más ejemplos de texto etiquetado aquí
        ]
        cls.train_ner_model(TRAIN_DATA)

    @classmethod
    # Función para entrenar el modelo de NER
    def train_ner_model(cls, train_data, iterations=100):
        # Preparar el optimizador
        optimizer = cls.nlp.begin_training()
        print("PRINT 1")
        # Iterar sobre los datos de entrenamiento durante el número especificado de iteraciones
        for itn in range(iterations):
            print("PRINT 2")
            # Mezclar los datos de entrenamiento
            random.shuffle(train_data)
            losses = {}
            print("PRINT 3")
            # Dividir los datos en lotes (mini-batches) y actualizar el modelo con cada lote
            for batch in minibatch(train_data, size=compounding(4.0, 32.0, 1.001)):
                print("PRINT 4")
                texts, annotations = zip(*batch)
                print("PRINT 5")
                cls.nlp.update(texts, annotations, drop=0.5, losses=losses)
                print("PRINT 6")

            # Imprimir el progreso del entrenamiento
            print("Iteración {} Loss: {:.4f}".format(itn, losses['ner']))
    
    @staticmethod
    def clean_text(text: str) -> str:
        # Convertir a minúsculas y reemplazar caracteres no deseados
        text = text.lower()
        text = text.replace(".", "")
        text = text.replace(":", "")
        text = text.replace("!", "")
        text = text.replace("¡", "")
        text = text.replace("¿", "")
        text = text.replace("?", "")
        text = text.replace("\n", " ")
        return text
    
    @classmethod
    def validate_tramit(cls, tramite: int, body: str) -> dict:
        body = cls.clean_text(body)

        if int(tramite) == 2: #Cotización póliza de auto
            fields = cls.search_car_policy_fields(body)
        if int(tramite) == 3: #Cotización póliza del hogar
            fields = cls.search_home_policy_fields(body)
            
        validation = cls.validate_completed_fields(fields)
        print(validation)
        return validation
    
    @classmethod
    def search_home_policy_fields(cls, text: str) -> dict:
        """
        Campos: tipo inmueble, dirección, código postal, superficie y rejas
        """
        property = None # Casa, departamento, oficina, consultorio
        direction = None
        area = None
        has_bars = None
        postal_code = cls.search_postal_code(text)
        
        res = {"tipo_inmueble": property, "direccion": direction, "superficie": area, "tiene_barras": has_bars, "cp": postal_code}
        print(res)
        return res

    @classmethod
    def search_car_policy_fields(cls, text: str) -> dict:
        """
        Campos: marca, modelo, año y código postal.
        """
        # Procesar el texto con spaCy para NER
        print("TEXT", text)
        doc = cls.nlp(text)
        print("DOC", doc)

        # Inicializar variables
        brand = model = year = postal_code = None

        # Recorrer las entidades reconocidas por spaCy
        print("ents", doc.ents)
        for ent in doc.ents:
            print("ENT", ent.label_)
            if ent.label_ == "MISC" and "marca" in ent.text:
                brand = ent.text.split()[-1]  # Asume que la marca está después de la palabra 'marca'
            elif ent.label_ == "MISC" and "modelo" in ent.text:
                model = ent.text.split()[-1]  # Asume que el modelo está después de la palabra 'modelo'
            elif ent.label_ == "DATE" and "año" in ent.text:
                year = ent.text.split()[-1]  # Asume que el año está después de la palabra 'año'
            elif ent.label_ == "MISC" and "cod postal" in ent.text:
                postal_code = ent.text.split()[-1]  # Asume que el código postal está después de la palabra 'cod postal'

        res = {"marca": brand, "modelo": model, "año": year, "cp": postal_code}
        print(res)
        return res
    
    @classmethod
    def search_postal_code(cls, text: str) -> str | None:
        """
        # Patrón para identificar código postal (suponiendo que es un número de 4 a 5 dígitos)
        postal_code_pattern = re.compile(r'\b(\d{4,5})\b')
        
        Evaluar si me sirve, el tema es que con el año del auto se confunde
        """
        # Patrón para identificar código postal
        text = text.replace("codigo", "cod")
        text = text.replace("código", "cod")
        # Para que lo remeplace si "pos" viene sólo y no dentro de otra palabra como "postal"
        text = re.sub(r'\bpos\b', 'postal', text)
        text = text.replace("cp", "cod postal")

        postal_code_pattern = re.compile(r'cod postal\s*(\d+)', re.IGNORECASE)
        postal_code = postal_code_pattern.search(text)
        postal_code = postal_code.group(1) if postal_code else None
        return postal_code

    @classmethod
    def validate_completed_fields(cls, fields: dict) -> dict:
        res = {
            "success": True,
            "fields_missing": []
        }
        for key, value in fields.items():
            if not value:
                res['success'] = False
                res["fields_missing"].append(key)
        return res
        
val = ValidacionTramites()


print()
print("********** Ejemplos póliza para el auto *************** ")
print()
print("CASE 1")
input1 = "Buenas tardes, quisiera cotizar un seguro para mi auto. Por favor, envíenme las diferentes opciones que su compañia ofrece. Los datos de mi vehiculo son: \nMarca: Chevrolet \nModelo: Spin \nAño: 2023\nCod Postal: 1414 \nTengo cochera propia. Adjunto también foto de mi vehiculo para que se vea que está en perfectas condiciones.\nMuchas gracias"
val.validate_tramit(2, input1)
print()
print("CASE 2")
input2 = "Buenas tardes, quisiera cotizar un seguro para mi auto. Por favor, envíenme las diferentes opciones que su compañia ofrece. Los datos de mi vehiculo son: \nMarca Chevrolet \nModelo Spin \nAño 2023\nCod. Postal. 1414 \nTengo cochera propia. Adjunto también foto de mi vehiculo para que se vea que está en perfectas condiciones.\nMuchas gracias"
val.validate_tramit(2, input2)
print()
print("CASE 3")
input3 = "Buenas!! ¿Como estan? Los datos de mi vehiculo son: \nMarca Chevrolet \nModelo Spin \nAño: 2023\n cp. 1414 \nTengo cochera propia. Adjunto también foto de mi vehiculo para que se vea que está en perfectas condiciones.\nMuchas gracias"
val.validate_tramit(2, input3)

print()
print("********** Ejemplos póliza del hogar *************** ")
print()
print("CASE 4")
input4 = "Buenas tardes, quisiera cotizar un seguro para mi hogar. Por favor, envíenme las diferentes opciones que su compañía ofrece. Los datos de mi inmueble son: \nTipo de inmueble: Casa \nDirección: Calle Falsa 123, Ciudad \nCod Postal: 1414 \nSuperficie: 150 m² \nPoseo rejas en todas las ventanas y puertas. Adjunto también fotos del inmueble para que se vea su estado actual.\nMuchas gracias"
val.validate_tramit(3, input4)