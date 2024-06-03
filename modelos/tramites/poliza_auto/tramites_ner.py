"""    
Para cada dato de entrenamiento se definen los textos (Doc) y se les agregan las entidades como una lista de objetos 
(Span) para predecir.
    
Info para mi (temporal):
    sm = small
    lg = large y es más preciso
"""
from datetime import datetime
import math
import subprocess
import sys
from tramites_data.data import TRAIN_DATA
from spacy.util import filter_spans
from spacy.tokens import DocBin
from tqdm import tqdm
import spacy
import sys
import os

class TramitePolizaAuto:
    nlp = None
    
    @classmethod
    def __init__(cls, training_data):
        # Intentar cargar un modelo entrenado si es que existe
        try:
            cls.nlp = spacy.load("modelo_entrenado/model-best")
        except OSError:
            # Si el modelo no existe, inicializa un modelo base y lo entrena
            cls.nlp = spacy.blank("es")
            cls.prepare_model_data(training_data)
            cls.train_model()
            cls.nlp = spacy.load("modelo_entrenado/model-best")
        

    @classmethod
    def prepare_model_data(cls, training_data):
        training_data = training_data

        print(training_data[0]['entities'])
        print(training_data[0]['text'])

        """
        SpaCy requiere que lso datos de entrenamiento deben ser del tipo docbin y deben guardarse en un archivo .spacy
        """
        doc_bin = DocBin()

        # Recorremos nuestros datos de entrenamiento
        for training_example  in tqdm(training_data): 
            # Obtenemos los textos / las sentencias de entrenamiento
            text = training_example['text']
            # Obtenemos las entidades encontrada en esa sentencia, incluyendo el inicio y final de estos.
            labels = training_example['entities']
            # Crea un documento por cada dato de entrenamiento
            doc = cls.nlp.make_doc(text) 
            ents = []
            
            # Cada laabel contiene un string y dos ints que marcan el inicio y el final del string en la sentencia
            for start, end, label in labels:
                #print("DATA", start, end, label)
                # Le asignamos entidades a nuestro doc
                span = doc.char_span(start, end, label=label, alignment_mode="contract")
                #print("SPAN", span)
                if span is None:
                    print("Skipping entity")
                else:
                    ents.append(span)
            filtered_ents = filter_spans(ents)
            doc.ents = filtered_ents 
            doc_bin.add(doc)

        doc_bin.to_disk("train.spacy") # Se pisa cada vez que re corre la línea de código

    @classmethod
    def train_model(cls):
        # Para entrenar al modelo se debe ejecutar el comando de entrenamiento
        print("Entrenando el modelo...")
        subprocess.run([
            sys.executable, "-m", "spacy", "train", "../spacy_config/config.cfg",
            "--output", "./modelo_entrenado",  # Directorio donde se guardará el modelo entrenado
            "--paths.train", "./train.spacy", "--paths.dev", "./train.spacy"
        ])
    
    @classmethod
    def predict(cls, sentences: list) -> list:
        if cls.nlp is None:
            raise ValueError("El modelo no está cargado.")
        
        res = []
        for text in sentences:
            text = text.lower()
            doc = cls.nlp(text)
            for ent in doc.ents:
                res.append({ent.label_ : ent.text})
        return res
        

inicio = datetime.now()
val = TramitePolizaAuto(TRAIN_DATA)


val.train_model()

fin = datetime.now()
tiempo_proceso_segs = fin - inicio
# Obtener la diferencia en minutos
tiempo_proceso_mins = math.trunc(tiempo_proceso_segs.total_seconds() / 60)
print(f"El proceso completo demora {tiempo_proceso_mins} minutos.") 

sentencias = [
    "Busco información para asegurar un peugeot 2008 del 2016, mi código postal es 1420",
    "buenas noches, quisiera información para asegurar un kia rio del 2014, código postal 33445",
    "hola, necesito cotizar un seguro para mi coche marca hyundai modelo elantra del año 2022, vivo en el código postal 77889",
    "quiero un seguro para mi coche. Marca: Renault, Modelo: Kwid, Año: 2019. Código Postal: 67890.",
    "necesito un seguro para mi automóvil. marca mazda, modelo cx-5, año 2018, cp 11011",
    "hola, busco un seguro para un coche de marca suzuki modelo swift año 2016, código postal 12349",
    "cotización de seguro para automóvil marca mitsubishi, modelo lancer, año 2014, código postal 55555",
    "quiero cotizar seguro para mi auto marca fiat, modelo cronos, año 2021, mi código postal es 22334",
    "buenas, me interesa un seguro para mi auto fiat cronos 2020, vivo en el código postal 1414",
    "hola, quiero asegurar mi coche, que es un ford fiesta del 2018. código postal 5000.",
    "buenos días, quisiera cotizar un seguro para mi volkswagen gol 2017. mi código postal es 98765."
]

for sentencia in sentencias:
    print(sentencia)
    prediction = val.predict([sentencia])
    print(prediction)
    print(" *************************************** ")

