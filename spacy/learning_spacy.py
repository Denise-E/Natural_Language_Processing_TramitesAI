"""
https://github.com/explosion/projects/tree/v3/tutorials

https://www.youtube.com/results?search_query=python+spacy+nlp+creating+my+own+model

https://spacy.io/api

sm = small
lg = large y es más preciso

Para cada dato de entrenameinto se definen los textos (Doc) y se les agregan las entidades como una lista de objetos (Span) para predecir

Para el entrenamiento del modelo se requiere de un archivo de configuración

"""
from data.data import TRAIN_DATA
from spacy.util import filter_spans
from spacy.tokens import DocBin
from tqdm import tqdm
import spacy

nlp = spacy.load("es_core_news_sm")

training_data = TRAIN_DATA

print(training_data[0]['entities'])
print(training_data[0]['text'])

"""
SpaCy requiere que lso datos de entrenamiento deben ser del tipo docbin y deben guardarse en un archivo .spacy
"""
nlp = spacy.blank("es") # load a new spacy model
doc_bin = DocBin()

# Chequear si está desactualizado. 
"""
Que hace? 
"""
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


