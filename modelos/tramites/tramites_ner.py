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

Para esto vamos a utilizar modelos NER, modelo de Reconocimiento de Entidades Nombradas, para poder identificar entidades 
basadas en el contexto y patrones aprendidos durante el entrenamiento, lo que lo hace más adaptable y robusto.     

Para esto vamos a utilizar la librería de python SpaCy.

    Documentación Oficial: https://spacy.io/api

    Para cada dato de entrenamiento se definen los textos (Doc) y se les agregan las entidades como una lista de objetos 
    (Span) para predecir.
    
    Para el entrenamiento del modelo se requiere de un archivo de configuración. Dejo el link para poder leer más
    sobre este; https://spacy.io/usage/training#quickstart

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

class ValidacionTramites:
    nlp = None
    
    @classmethod
    def __init__(cls):
        # Intentar cargar un modelo entrenado si es que existe
        try:
            cls.nlp = spacy.load("modelo_entrenado/model-best")
        except OSError:
            # Si el modelo no existe, inicializa un modelo base y lo entrena
            cls.nlp = spacy.blank("es")
            cls.prepare_model_data()
            cls.train_model()
            cls.nlp = spacy.load("modelo_entrenado/model-best")
        

    @classmethod
    def prepare_model_data(cls):
        training_data = TRAIN_DATA

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
            sys.executable, "-m", "spacy", "train", "config.cfg",
            "--output", "./modelo_entrenado",  # Directorio donde se guardará el modelo entrenado
            "--paths.train", "./train.spacy", "--paths.dev", "./train.spacy"
        ])
        
    @classmethod
    def predict(cls, sentences: list):
        if cls.nlp is None:
            raise ValueError("El modelo no está cargado.")
        
        res = []
        for text in sentences:
            text = text.lower()
            doc = cls.nlp(text)
            for ent in doc.ents:
                #print("Text:", ent.text, "Label:", ent.label_)
                res.append({ent.label_ : ent.text})
        return res

inicio = datetime.now()
val = ValidacionTramites()
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


""""
Campos de los Resultados de Entrenamiento
E: Número de época (Epoch). Una época se refiere a una pasada completa a través del conjunto de datos de entrenamiento.
#: Número de iteración dentro de una época.
LOSS TOK2VEC: Pérdida asociada al componente tok2vec de Spacy, que es responsable de convertir los tokens en vectores.
LOSS NER: Pérdida asociada al componente NER. La pérdida (loss) es una medida de lo bien o mal que el modelo está funcionando. Menos pérdida indica un mejor rendimiento.
ENTS_F: F-score de las entidades. El F-score es la media armónica de la precisión (precision) y el recall.
ENTS_P: Precisión (Precision) de las entidades. La precisión es la proporción de entidades predichas correctamente entre todas las entidades predichas.
ENTS_R: Recall (recuperación) de las entidades. El recall es la proporción de entidades predichas correctamente entre todas las entidades verdaderas en los datos.
SCORE: Una puntuación general del modelo en base a sus predicciones. Generalmente, esta es una métrica global que combina diferentes aspectos del rendimiento del modelo.

Época 51, Iteración 600 y Época 77, Iteración 800:

LOSS TOK2VEC: 0.00
LOSS NER: 0.00
ENTS_F, ENTS_P, ENTS_R, SCORE: Todos en 100.00
Las pérdidas se han reducido a cero y las métricas de rendimiento se mantienen en 100%, lo que indica que el modelo ha aprendido muy bien los datos de entrenamiento.
"""
