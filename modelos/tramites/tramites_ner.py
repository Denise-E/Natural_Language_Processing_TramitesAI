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
from tramites_data.data import TRAIN_DATA
from spacy.util import filter_spans
from spacy.tokens import DocBin
from tqdm import tqdm
import spacy

class ValidacionTramites:
    nlp = None
    
    @classmethod
    def __init__(cls):
        nlp = spacy.load("es_core_news_sm")
        cls.train_ner_model()

    @classmethod
    def train_ner_model(cls):
        training_data = TRAIN_DATA

        print(training_data[0]['entities'])
        print(training_data[0]['text'])

        """
        SpaCy requiere que lso datos de entrenamiento deben ser del tipo docbin y deben guardarse en un archivo .spacy
        """
        nlp = spacy.blank("es") # Se crea un nuevo modelo de SpaCy en español
        doc_bin = DocBin()

        # Recorremos nuestros datos de entrenamiento
        for training_example  in tqdm(training_data): 
            # Obtenemos los textos / las sentencias de entrenamiento
            text = training_example['text']
            # Obtenemos las entidades encontrada en esa sentencia, incluyendo el inicio y final de estos.
            labels = training_example['entities']
            # Crea un documento por cada dato de entrenamiento
            doc = nlp.make_doc(text) 
            ents = []
            
            # Cada laabel contiene un string y dos ints que marcan el inicio y el final del string en la sentencia
            for start, end, label in labels:
                print("DATA", start, end, label)
                # Le asignamos entidades a nuestro doc
                span = doc.char_span(start, end, label=label, alignment_mode="contract")
                print("SPAN", span)
                if span is None:
                    print("Skipping entity")
                else:
                    ents.append(span)
            filtered_ents = filter_spans(ents)
            doc.ents = filtered_ents 
            doc_bin.add(doc)

        doc_bin.to_disk("train.spacy") # Se pisa cada vez que re corre la línea de código

        """
        Para entrenar al modelo se debe correr el siguiente comando:

        python -m spacy train config.cfg --paths.train ./train.spacy --paths.dev ./train.spacy
        """
        

val = ValidacionTramites()


'''print()
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
val.validate_tramit(3, input4)'''