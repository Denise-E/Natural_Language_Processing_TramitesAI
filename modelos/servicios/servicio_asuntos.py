import os
import pickle
from modelos.servicios.servicio_base.servicio_modelos import ServicioModelos
import logging
import numpy as np
import pandas as pd
import tensorflow as tf
from keras.utils import to_categorical
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
#from sklearn.model_selection import train_test_split, StratifiedKFold
from keras.models import load_model

# Suprimir advertencias
logging.getLogger('tensorflow').setLevel(logging.ERROR)

MODELO_RUTA = os.getenv("MODELO_ASUNTO_GUARDADO")

class ServicioAsuntos(ServicioModelos):
    # Parámetros para la configuración del modelo
    TRUNC_TYPE='post'  # Tipo de truncado de las secuencias (después de alcanzar max_length).
    PADDING_TYPE='post'  # Tipo de padding (agregado de tokens al final de la secuencia).
    OOV_TOKEN = "<OOV>"  # Token para palabras fuera del vocabulario (Out Of Vocabulary).
    tokenizer = None  # Tokenizer se inicializa como None y se configura posteriormente.
    model = None  # Modelo se inicializa como None y se configura posteriormente.
    vocab_size: int = None  # Máximo número de palabras que se deben conservar, si se le pasan más, guardará las 10000 más repetidas.
    embedding_dim:int = None  # Dimensión del vector de características para cada palabra.
    max_length: int = None  # Longitud máxima de las secuencias de entrada.
    training_sentences: list = None # Sentencias de entrenamiento
    training_labels: list = None # Respuesta esperada para cada sentencia de entrenamiento
    testing_sentences: list = None # Sentencias de prueba
    testing_labels: list = None # Respuesta esperada para cada sentencia de prueba
    categories_quantity: int = None
    num_epochs: int = None # Cantidad de iteraciones que hará el modelo durante el entrenameinto
    model_path = MODELO_RUTA 
    
    @classmethod
    def __init__(cls, vocab_size:int = 10000, embedding:int = 16, max_length: int = 10000, num_epochs:int = 4000):
        cls.vocab_size = vocab_size
        cls.embedding_dim = embedding
        cls.max_length = max_length
        cls.num_epochs = num_epochs

        try:
            if os.path.exists(os.path.join(cls.model_path, 'modelo_entrenado')):
                cls.model = load_model(os.path.join(cls.model_path, 'modelo_entrenado'))
                with open(os.path.join(cls.model_path, 'tokenizer.pkl'), 'rb') as handle:
                    cls.tokenizer = pickle.load(handle)
                with open(os.path.join(cls.model_path, 'training_sentences.pkl'), 'rb') as handle:
                    cls.training_sentences = pickle.load(handle)
                print("Modelo asuntos pre existente")
            else:
                cls.crear_modelo()
        except OSError:
            cls.crear_modelo()
    
    @classmethod
    def crear_modelo(cls):
        # Obtener datos de entrenamiento
        cls.obtener_datos()
        #cls.perform_cross_validation()
        # Configurar y entrenar el modelo
        cls.configuracion_entrenamiento_modelo()
        # Guardar el modelo entrenado y el tokenizer
        cls.model.save(os.path.join(cls.model_path, 'modelo_entrenado'))
        with open(os.path.join(cls.model_path, 'tokenizer.pkl'), 'wb') as handle:
            pickle.dump(cls.tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)
        with open(os.path.join(cls.model_path, 'training_sentences.pkl'), 'wb') as handle:
            pickle.dump(cls.training_sentences, handle, protocol=pickle.HIGHEST_PROTOCOL)
        print("Modelo asuntos creado exitosamente")
            
        '''if os.path.exists(os.path.join(cls.model_path, 'modelo_entrenado')):
            cls.model = load_model(os.path.join(cls.model_path, 'modelo_entrenado'))
            with open(os.path.join(cls.model_path, 'tokenizer.pkl'), 'rb') as handle:
                cls.tokenizer = pickle.load(handle)
            with open(os.path.join(cls.model_path, 'training_sentences.pkl'), 'rb') as handle:
                cls.training_sentences = pickle.load(handle)
            print("Modelo asuntos pre existente")
        else:
            # Obtener datos de entrenamiento
            cls.obtener_datos()
            #cls.perform_cross_validation()
            # Configurar y entrenar el modelo
            cls.configuracion_entrenamiento_modelo()
            # Guardar el modelo entrenado y el tokenizer
            cls.model.save(os.path.join(cls.model_path, 'modelo_entrenado'))
            with open(os.path.join(cls.model_path, 'tokenizer.pkl'), 'wb') as handle:
                pickle.dump(cls.tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)
            with open(os.path.join(cls.model_path, 'training_sentences.pkl'), 'wb') as handle:
                pickle.dump(cls.training_sentences, handle, protocol=pickle.HIGHEST_PROTOCOL)
            print("Modelo asuntos creado exitosamente")'''
    
    '''@classmethod
    def obtener_datos(cls):
        # Este método trabaja con Pandas para la obtención de los datos de entrenamiento y de prueba a partir de archivo csv
        # Crea el dataframe a partir del csv
        df = pd.read_csv('modelos/asuntos/asuntos_data/asuntos.csv')

        # Separa las sentencias y las etiquetas
        sentences = df['Sentencias'].tolist()
        labels = df['Categoria'].tolist()

        # Divide los datos en conjunto de entrenamiento y prueba con una proporción de 80/20
        X_train, X_test, y_train, y_test = train_test_split(sentences, labels, test_size=0.2, stratify=labels)

        # Asigna los datos de entrenamiento y prueba a las variables de clase
        cls.training_sentences = X_train
        cls.training_labels = y_train
        cls.testing_sentences = X_test
        cls.testing_labels = y_test

        # Obtiene la cantidad de valores distintos en la columna 'Categoria'
        cls.categories_quantity = df['Categoria'].nunique()

    @classmethod
    def perform_cross_validation(cls, k=5):
        # Crea el objeto StratifiedKFold
        skf = StratifiedKFold(n_splits=k)

        # Itera sobre los folds generados por StratifiedKFold dentro del conjunto de entrenamiento
        for train_index, val_index in skf.split(cls.training_sentences, cls.training_labels):
            X_train_fold = [cls.training_sentences[i] for i in train_index]
            X_val_fold = [cls.training_sentences[i] for i in val_index]
            y_train_fold = [cls.training_labels[i] for i in train_index]
            y_val_fold = [cls.training_labels[i] for i in val_index]
            
            # Aquí entrenarías y evaluarías tu modelo en cada fold
            # Esto es solo un ejemplo de cómo iterar sobre los folds
            print("Fold entrenamiento:", len(X_train_fold), "Fold validación:", len(X_val_fold))

    '''
    @classmethod
    def obtener_datos(cls):
        # Este metodo trabaja con Pandas para la obtención de los datso de entrenameinto y de prueba a partir de archivo csv
        # Crea el dataframe a partir del csv
        df = pd.read_csv('modelos/asuntos/asuntos_data/asuntos.csv')
        #print(df)
        
        # Es importante que no hayan espacios en lso títulos, para que puedan encontrarse las columnas. Por ejemplo "Uso" y no " Uso "
        # Filtra los datos de capacitación y testeo
        training_data = df[df['Uso'] == 'C']
        testing_data = df[df['Uso'] == 'T']

        # Separa las sentencias de la respuesta esperada
        cls.training_sentences = training_data['Sentencias'].tolist()
        cls.training_labels = training_data['Categoria'].tolist()
        cls.testing_sentences = testing_data['Sentencias'].tolist()
        cls.testing_labels = testing_data['Categoria'].tolist()
        
        # Obtiene la cantidad de valores distintos en la columna 'Categoria'
        cls.categories_quantity = df['Categoria'].nunique()
        
    @classmethod
    def configuracion_entrenamiento_modelo(cls):
        # 1. Tokenización de las sentencias
        """
        Tokenizer:
        
        - No distingue minusculas y mayúsculas, tampoco simbolos. Si reconoce acentos.
        - El parámetro "num_words" determina la cantidad máxima de tokens que se generarán. Por ejemplo, si se le define el valor 100 y en los 
        datos de capacitación hay 200 palabras distintas, tokenizará únicamente las 100 palabras más repetidas.
        - El valor dado al parámetro oov_token es el identificador que se usará para luego para tokenizar palabras que no se encontraban, o no fueron tokenizados, al procesarse los datos de capacitación. 
        El token '0' guardará este valor, en nuetsro caso {0: "<OOV>"}
        """
        tokenizer = Tokenizer(num_words=cls.vocab_size, oov_token=cls.OOV_TOKEN) 
        tokenizer.fit_on_texts(cls.training_sentences)
        cls.tokenizer = tokenizer
        word_indexed = tokenizer.word_index # Genera la lista de las palabras tokenizadas
        print("Indexed  WORDS", word_indexed)
        training_sentences = cls.tokenizer.texts_to_sequences(cls.training_sentences) # Crea la secuencia de tokens para cada oración. Lista de listas.
        
        """
        pad_sequences:
        
        - maxlen debe definirse por concordancia con el resto del proceso.
        - Todas las oraciones deben tener la misma cantidad de palabras, se resuelve completando con la cantidad de OOV_TOKEN necesarios en cada oración.
        - Se completará con el OOV_TOKEN al final, dado por el valor 'post' del parámetro padding.
        Por ejemplo, en una oración de 3 palabras que deba llevarse a una longitud de 5 palabras, quedará [1,2,3,<OOV>,<OOV>]
        """
        training_padded = pad_sequences(training_sentences,maxlen=cls.max_length, padding='post')  
        training_labels = to_categorical(cls.training_labels, num_classes=cls.categories_quantity)
        #print("PADDED SHAPE", training_padded.shape) #Filas x columns - muestra cantidades
        
        # 2. Creación y configuración del modelo de red neuronal
        model = tf.keras.Sequential([
            tf.keras.layers.Embedding(cls.vocab_size, cls.embedding_dim, input_length=cls.max_length),
            tf.keras.layers.GlobalAveragePooling1D(),
            tf.keras.layers.Dense(24, activation='relu'),
            tf.keras.layers.Dense(cls.categories_quantity, activation='softmax') # Para trabajar con múltiples clases
        ])

        # Configuración del modelo
        # El valor del parámetro loss es debido a estar trabajndo con múltiples clases
        model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
        model.summary()
        # Guardamos el modelo en la variable de clase, ya que será necesario para luego realizar las predicciones
        cls.model = model

        # Datos de prueba para el modelo
        testing_sentences = tokenizer.texts_to_sequences(cls.testing_sentences)
        testing_padded = pad_sequences(testing_sentences, maxlen=cls.max_length, padding='post') 
        testing_labels = to_categorical(cls.testing_labels, num_classes=cls.categories_quantity)

        # A partir de la versión 2 de tf (TensorFlow), el modelo debe recibir datos del tipo de numpy (np) y no tipos de datos nativos de python
        training_padded = np.array(training_padded)
        training_labels = np.array(training_labels)
        testing_padded = np.array(testing_padded)
        testing_labels = np.array(testing_labels)

        print("TEST RESULTS")
        # Entrenamiento del modelo con los datos de entrenamiento y de prueba.
        history = model.fit(training_padded, training_labels, epochs=cls.num_epochs, validation_data=(testing_padded, testing_labels), verbose=2)
        """
        Resultados model.fit:
        
        accuracy = relacionado a los datos de entrenameinto 
        val_accuracy = relacionado a los datos de prueba / testeo
        """
        
    @classmethod
    def predecir(cls, sentencias: list) -> list:
        """
        Retorna una lista de diccionarios, cada diccionario contiene el un asunto y el resultado de su clasificación,
        es decir la clase que fue determinada para él por el modelo (valor de 0 a 4)
        """
        if cls.tokenizer is None:
            raise ValueError("El tokenizer no está inicializado.")
        
        # Procesamiento de los datos de entrada. Tokenización strings.
        sequences = cls.tokenizer.texts_to_sequences(sentencias)
        padded = pad_sequences(sequences, maxlen=cls.max_length, padding=cls.PADDING_TYPE, truncating=cls.TRUNC_TYPE)
        
        # Con la sentencia recibida ya tokenizada, le pedimos al modelo que haga la predicción.
        prediction = cls.model.predict(padded)
        res = np.argmax(prediction, axis=1)  # Devuelve la clase predicha con mayor probabilidad.
        predicciones = list(res)
        predicciones_int = [int(prediccion) for prediccion in predicciones]
        
        return predicciones_int
    