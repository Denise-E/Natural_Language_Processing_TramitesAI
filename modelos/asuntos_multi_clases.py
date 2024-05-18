import numpy as np
import tensorflow as tf
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from .data.data_asuntos_mc import outcomes, training_sentences as training_sentences_sentences, training_labels as data_training_labels, testing_sentences as data_testing_sentences, testing_labels as data_testing_labels
from keras.utils import to_categorical

class ModeloAsuntosMultiClases:
    VOCAB_SIZE = 10000 #Máx num de palabras que se deben conservar, si se le pasan más va a guardar las 10000 más repetidas.
    EMBEDDING_DIM = 16 
    MAX_LENGTH = 10000 
    TRUNC_TYPE='post'
    PADDING_TYPE='post' 
    OOV_TOKEN = "<OOV>" #Token para todas aquellas palabras no tokenizadas.
    tokenizer = None 
    model = None

    @classmethod
    def __init__(cls):
        cls.model_config_and_training()
        
    @classmethod
    def model_config_and_training(cls):
        # 1. Definición de los strings de capacitación, importados de la carpeta data
        sentences = training_sentences_sentences
        training_labels = data_training_labels
        # Nos guardamos la cantidad de clases con las que vamos a estar trabajando, ya que este valor será utilizado varias veces
        outcomes_quantity = len(outcomes)

        # 2. Tokenización de las sentencias
        """
        Tokenizer:
        
        - No distingue minusculas y mayúsculas, tampoco simbolos. Si reconoce acentos.
        - El parámetro "num_words" determina la cantidad máxima de tokens que se generarán. Por ejemplo, si se le define el valor 100 y en los 
        datos de capacitación hay 200 palabras distintas, tokenizará únicamente las 100 palabras más repetidas.
        - El valor dado al parámetro oov_token es el identificador que se usará para luego para tokenizar palabras que no se encontraban, o no fueron tokenizados, al procesarse los datos de capacitación. 
        El token '0' guardará este valor, en nuetsro caso {0: "<OOV>"}
        """
        tokenizer = Tokenizer(num_words=cls.VOCAB_SIZE, oov_token=cls.OOV_TOKEN) 
        tokenizer.fit_on_texts(sentences)
        cls.tokenizer = tokenizer
        word_indexed = tokenizer.word_index # Arma lista de las palabras tokenizadas
        print("Indexed  WORDS", word_indexed)
        
        training_sentences = tokenizer.texts_to_sequences(sentences) # Crea la secuencia de tokens para cada oración. Lista de listas.
        """
        pad_sequences:
        
        Hay que deifnirle MAX_LENGTH por concordancia con resto del proceso, sino va a romper luego.
        Todas las sentencias deben tener la misma cantidad de palabras, eso se resuelve completando
        con la cantidad de OOV_TOKEN necesarios en cada sentencia. 
        Se completará con el OOV_TOKEN al final, dado por el valor 'post' del parámetro padding.
        Por ejemplo, en un caso de una sentencia formada por 3 palarbas que deba llevarse a una longitud de 
        5 palabras quedaría luego del este método formado de la siguiente manera: [1,2,3,<OOV>,<OOV>]
        """
        training_padded = pad_sequences(training_sentences,maxlen=cls.MAX_LENGTH, padding='post')  
        training_labels = to_categorical(training_labels, num_classes=outcomes_quantity)
        print("PADDED", training_padded)
        #print("PADDED SHAPE", training_padded.shape) #Filas x columns - muestra cantidades
        
        # 3. Creación del Modelo
        # TODO Documentar
        model = tf.keras.Sequential([
            tf.keras.layers.Embedding(cls.VOCAB_SIZE, cls.EMBEDDING_DIM, input_length=cls.MAX_LENGTH),
            tf.keras.layers.GlobalAveragePooling1D(),
            tf.keras.layers.Dense(24, activation='relu'),
            tf.keras.layers.Dense(outcomes_quantity, activation='softmax') # Para trabajar con múltiples clases
        ])

        # Configuración del modelo
        # El valor del parámetro loss es debido a estar trabajndo con múltiples clases
        model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
        model.summary()
        # Guardamos el modelo en la variable de clase, ya que será necesario para luego realizar las predicciones
        cls.model = model

        # Datos de prueba para el modelo
        testing_sentences = data_testing_sentences
        testing_sentences = tokenizer.texts_to_sequences(testing_sentences)
        testing_padded = pad_sequences(testing_sentences, maxlen=cls.MAX_LENGTH, padding='post') 
        testing_labels = data_testing_labels
        testing_labels = to_categorical(testing_labels, num_classes=outcomes_quantity)

        # A partir de la versión 2 de tf (TensorFlow), el modelo debe recibir datos del tipo de numpy (np) y no tipos de datos nativos de python
        training_padded = np.array(training_padded)
        training_labels = np.array(training_labels)
        testing_padded = np.array(testing_padded)
        testing_labels = np.array(testing_labels)

        num_epochs = 3000 # Cantidad de iteraciones que hará el modelo durante el entrenameinto
        print("TEST RESULTS")
        #Se le pasan inputs y outputs de los datos de capacitación y de testeo. Acá es entrenado el motor.
        history = model.fit(training_padded, training_labels, epochs=num_epochs, validation_data=(testing_padded, testing_labels), verbose=2)
        """
        Resultados model.fit:
        
        accuracy = relacionado a los datos de entrenameinto 
        val_accuracy = relacionado a los datos de prueba / testeo 
        """

    @classmethod
    def model_prediction_tests(cls, sentence: str) -> list[int]:
        # Procesamiento de los datos de entrada. Tokenización strings.
        sequences = cls.tokenizer.texts_to_sequences(sentence)
        padded = pad_sequences(sequences, maxlen=cls.MAX_LENGTH, padding=cls.PADDING_TYPE, truncating=cls.TRUNC_TYPE)
        # Con la sentencia recibida ya tokenizada, le pedimos al modelo que haga la predicción.
        prediction = cls.model.predict(padded)
        return [prediction.tolist() , np.argmax(prediction, axis=1)] #Valor a ajustar una vez que vaya sumando casos para la capacitación del modelo
        #return np.argmax(prediction, axis=1)
    