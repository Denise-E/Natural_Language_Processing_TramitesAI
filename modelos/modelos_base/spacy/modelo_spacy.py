from spacy.util import filter_spans
from spacy.tokens import DocBin
from tqdm import tqdm
import subprocess
import spacy
import sys

class ModelosSpacy():
    pln = None # Avrebiatura de Procesamiento de Lenguaje Natural
    url_modelo = None
    
    @classmethod
    def inicilizacion(cls, url: str, training_data: list) -> None:
        cls.url_modelo = url
        try:
            cls.pln = spacy.load(url+"/modelo_entrenado/model-best")
            print("Modelo pre existente")
        except OSError:
            cls.entrenar(training_data)
    
    @classmethod
    def entrenar(cls, training_data: list) -> None:
        cls.pln = spacy.load("es_core_news_sm")
        cls.preparar_datos(training_data)
        cls.entrenar_modelo()
        cls.pln = spacy.load(cls.url_modelo+"/modelo_entrenado/model-best")
        print("Modelo creado exitosamente")
    
    @classmethod
    def preparar_datos(cls, datos: list) -> None:
        """
        SpaCy requiere que los datos de entrenamiento deben ser del tipo docbin y deben guardarse en un archivo .spacy
        """
        doc_bin = DocBin()

        # Recorremos nuestros datos de entrenamiento
        for dato  in tqdm(datos): 
            # Obtenemos los textos / las sentencias de entrenamiento
            texto = dato['texto']
            # Obtenemos las entidades encontrada en esa sentencia, incluyendo el inicio y final de estos.
            etiquetas = dato['entidades']
            # Crea un documento por cada dato de entrenamiento
            doc = cls.pln.make_doc(texto) 
            entidades = []
            
            # Cada etiqueta contiene un string y dos ints que marcan el inicio y el final del string en la sentencia
            for principio, fin, etiqueta in etiquetas:
                #print("DATA", principio, fin, etiqueta)
                # Le asignamos entidades a nuestro doc
                span = doc.char_span(principio, fin, label=etiqueta, alignment_mode="contract")
                #print("SPAN", span)
                if span is not None:
                    entidades.append(span)
            entidades_filtradas = filter_spans(entidades)
            doc.ents = entidades_filtradas 
            doc_bin.add(doc)

        doc_bin.to_disk(cls.url_modelo+"/train.spacy") # Se pisa cada vez que re corre la línea de código
    
    @classmethod
    def entrenar_modelo(cls) -> None:
        # Para entrenar al modelo se debe ejecutar el comando de entrenamiento
        print("Entrenando el modelo...")
        subprocess.run([
            sys.executable, "-m", "spacy", "train", "./modelos/modelos_base/spacy/spacy_config/config.cfg",
            "--output", cls.url_modelo+"/modelo_entrenado",  # Directorio donde se guardará el modelo entrenado
            "--paths.train", cls.url_modelo+"/train.spacy", "--paths.dev", cls.url_modelo+"/train.spacy"
        ])
    
    @classmethod
    def predecir(cls, sentencias: list) -> list:
        if cls.pln is None:
            raise ValueError("El modelo no está cargado.")
        
        res = []
        for sentencia in sentencias:
            doc = cls.pln(sentencia)
            for ent in doc.ents:
                res.append({ent.label_ : ent.text})
        return res
    