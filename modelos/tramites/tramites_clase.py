from spacy.util import filter_spans
from spacy.tokens import DocBin
from tqdm import tqdm
import subprocess
import spacy
import sys

class Tramite():
    nlp = None
    url_modelo = None
    
    @classmethod
    def __init__(cls, url: str, training_data: str) -> None:
        """
        Params
            url : path a donde se guardará la información del modelo entrenado, variará para cada modelo creado
            training_data : set de datos a usar para la capacitación del modelo
        """
        # Intentar cargar un modelo entrenado si es que existe
        cls.url_modelo = url
        try:
            cls.nlp = spacy.load(cls.url_modelo+"/modelo_entrenado/model-best")
            print("Modelo póliza auto pre existente")
        except OSError:
            cls.entrenar(training_data)
    
    @classmethod
    def entrenar(cls, training_data: list) -> None:
        cls.nlp = spacy.load("es_core_news_sm")
        cls.prepare_model_data(training_data)
        cls.train_model()
        cls.nlp = spacy.load(cls.url_modelo+"/modelo_entrenado/model-best")
        print("Modelo póliza auto creado exitosamente")
        
    @classmethod
    def prepare_model_data(cls, training_data) -> None:
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

        doc_bin.to_disk(cls.url_modelo+"/train.spacy") # Se pisa cada vez que re corre la línea de código
    
    @classmethod
    def train_model(cls) -> None:
        # Para entrenar al modelo se debe ejecutar el comando de entrenamiento
        print("Entrenando el modelo...")
        subprocess.run([
            sys.executable, "-m", "spacy", "train", "./modelos/tramites/spacy_config/config.cfg",
            "--output", cls.url_modelo+"/modelo_entrenado",  # Directorio donde se guardará el modelo entrenado
            "--paths.train", cls.url_modelo+"/train.spacy", "--paths.dev", cls.url_modelo+"/train.spacy"
        ])
    
    @classmethod
    def predict(cls, sentences: list) -> list:
        if cls.nlp is None:
            raise ValueError("El modelo no está cargado.")
        
        res = []
        for text in sentences:
            doc = cls.nlp(text)
            for ent in doc.ents:
                res.append({ent.label_ : ent.text})
        return res
    
    
    