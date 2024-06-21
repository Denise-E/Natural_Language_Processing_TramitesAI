from sklearn.model_selection import train_test_split, StratifiedKFold
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer
from keras.utils import to_categorical
from keras.models import load_model
import tensorflow as tf
import pandas as pd
import numpy as np
import pickle
import shutil
import os

class ModeloTensorFlow():
    # Parámetros para la configuración del modelo
    TIPO_TRUNCADO='post'  # Tipo de truncado de las secuencias (después de alcanzar long_sentencias).
    RELLENO='post'  # Tipo de padding (agregado de tokens al final de la secuencia).
    OOV_TOKEN = "<OOV>"  # Token para palabras fuera del vocabulario (Out Of Vocabulary).
    tokenizador = None  # El Tokenizador se inicializa como None y se configura posteriormente.
    model = None  # Modelo se inicializa como None y se configura posteriormente.
    max_tokens: int = None  # Máximo número de palabras que se deben tokenizar, si se le pasan más, guardará las 10000 más repetidas.
    dim_vector:int = None  # Dimensión del vector de características para cada palabra.
    long_sentencias: int = None  # Longitud máxima de las secuencias de entrada.
    sentencias_entrenameinto: list = None # Sentencias de entrenamiento
    etiquetas_entrenameinto: list = None # Respuesta esperada para cada sentencia de entrenamiento
    sentencias_prueba: list = None # Sentencias de prueba
    etiquetas_prueba: list = None # Respuesta esperada para cada sentencia de prueba
    cantidad_categorias: int = None
    iteraciones: int = None # Cantidad de iteraciones que hará el modelo durante el entrenameinto
    ruta_modelo = None 
    
    @classmethod
    def __init__(cls, max_tokens:int, dim_vector:int, long_sentencias: int, iteraciones:int, ruta_modelo:str):
        cls.max_tokens = max_tokens
        cls.dim_vector = dim_vector
        cls.long_sentencias = long_sentencias
        cls.iteraciones = iteraciones
        cls.ruta_modelo = ruta_modelo

        try:
            if os.path.exists(os.path.join(cls.ruta_modelo, 'modelo_entrenado')):
                cls.model = load_model(os.path.join(cls.ruta_modelo, 'modelo_entrenado'))
                with open(os.path.join(cls.ruta_modelo, 'tokenizer.pkl'), 'rb') as handle:
                    cls.tokenizador = pickle.load(handle)
                with open(os.path.join(cls.ruta_modelo, 'sentencias_entrenameinto.pkl'), 'rb') as handle:
                    cls.sentencias_entrenameinto = pickle.load(handle)
                print("Modelo pre existente")
            else:
                cls.crear_modelo()
        except OSError:
            cls.crear_modelo()
    
    @classmethod
    def crear_modelo(cls):
        # Obtener datos de entrenamiento
        cls.obtener_datos()
        cls.particionar_datos()
        # Configurar y entrenar el modelo
        cls.configuracion_entrenamiento_modelo()
        # Guardar el modelo entrenado y el tokenizador
        cls.model.save(os.path.join(cls.ruta_modelo, 'modelo_entrenado'))
        with open(os.path.join(cls.ruta_modelo, 'tokenizer.pkl'), 'wb') as handle:
            pickle.dump(cls.tokenizador, handle, protocol=pickle.HIGHEST_PROTOCOL)
        with open(os.path.join(cls.ruta_modelo, 'sentencias_entrenameinto.pkl'), 'wb') as handle:
            pickle.dump(cls.sentencias_entrenameinto, handle, protocol=pickle.HIGHEST_PROTOCOL)
        print("Modelo creado exitosamente")
            
    
    @classmethod
    def obtener_datos(cls):
        # Este método trabaja con Pandas para la obtención de los datos de entrenamiento y de prueba a partir de archivo csv
        # Crea el dataframe a partir del csv
        df = pd.read_csv(f'{cls.ruta_modelo}/datos/datos.csv')

        # Separa las sentencias y las etiquetas
        sentences = df['Sentencias'].tolist()
        labels = df['Categoria'].tolist()

        # Divide los datos en conjunto de entrenamiento y prueba con una proporción de 80/20
        X_train, X_test, y_train, y_test = train_test_split(sentences, labels, test_size=0.2, stratify=labels)

        # Asigna los datos de entrenamiento y prueba a las variables de clase
        cls.sentencias_entrenameinto = X_train
        cls.etiquetas_entrenameinto = y_train
        cls.sentencias_prueba = X_test
        cls.etiquetas_prueba = y_test

        # Obtiene la cantidad de valores distintos en la columna 'Categoria'
        cls.cantidad_categorias = df['Categoria'].nunique()

    @classmethod
    def particionar_datos(cls):
        # Crea el objeto StratifiedKFold
        skf = StratifiedKFold(n_splits=cls.cantidad_categorias)

        # Itera sobre los folds generados por StratifiedKFold dentro del conjunto de entrenamiento
        for train_index, val_index in skf.split(cls.sentencias_entrenameinto, cls.etiquetas_entrenameinto):
            X_train_fold = [cls.sentencias_entrenameinto[i] for i in train_index]
            X_val_fold = [cls.sentencias_entrenameinto[i] for i in val_index]
            y_train_fold = [cls.etiquetas_entrenameinto[i] for i in train_index]
            y_val_fold = [cls.etiquetas_entrenameinto[i] for i in val_index]
        
        print("SENTENCIAS ENTRENAMIENTO", len(cls.sentencias_entrenameinto))
        print("SENTENCIAS PRUEBAS", len(cls.sentencias_prueba))
            
 
    @classmethod
    def configuracion_entrenamiento_modelo(cls):
        # 1. Tokenización de las sentencias
        """
        Tokenizador:
        
        - No distingue minusculas y mayúsculas, tampoco simbolos. Si reconoce acentos.
        - El parámetro "num_words" determina la cantidad máxima de tokens que se generarán. Por ejemplo, si se le define el valor 100 y en los 
        datos de capacitación hay 200 palabras distintas, tokenizará únicamente las 100 palabras más repetidas.
        - El valor dado al parámetro oov_token es el identificador que se usará para luego para tokenizar palabras que no se encontraban, o no fueron tokenizados, al procesarse los datos de capacitación. 
        El token '0' guardará este valor, en nuetsro caso {0: "<OOV>"}
        """
        tokenizador = Tokenizer(num_words=cls.max_tokens, oov_token=cls.OOV_TOKEN) 
        tokenizador.fit_on_texts(cls.sentencias_entrenameinto)
        cls.tokenizador = tokenizador
        word_indexed = tokenizador.word_index # Genera la lista de las palabras tokenizadas
        print("Indexed  WORDS", word_indexed)
        sentencias_entrenameinto = cls.tokenizador.texts_to_sequences(cls.sentencias_entrenameinto) # Crea la secuencia de tokens para cada oración. Lista de listas.
        
        """
        pad_sequences:
        
        - maxlen debe definirse por concordancia con el resto del proceso.
        - Todas las oraciones deben tener la misma cantidad de palabras, se resuelve completando con la cantidad de OOV_TOKEN necesarios en cada oración.
        - Se completará con el OOV_TOKEN al final, dado por el valor 'post' del parámetro padding.
        Por ejemplo, en una oración de 3 palabras que deba llevarse a una longitud de 5 palabras, quedará [1,2,3,<OOV>,<OOV>]
        """
        training_padded = pad_sequences(sentencias_entrenameinto,maxlen=cls.long_sentencias, padding='post')  
        etiquetas_entrenameinto = to_categorical(cls.etiquetas_entrenameinto, num_classes=cls.cantidad_categorias)
        #print("PADDED SHAPE", training_padded.shape) #Filas x columns - muestra cantidades
        
        # 2. Creación y configuración del modelo de red neuronal
        model = tf.keras.Sequential([
            tf.keras.layers.Embedding(cls.max_tokens, cls.dim_vector, input_length=cls.long_sentencias),
            tf.keras.layers.GlobalAveragePooling1D(),
            tf.keras.layers.Dense(24, activation='relu'),
            tf.keras.layers.Dense(cls.cantidad_categorias, activation='softmax') # Para trabajar con múltiples clases
        ])

        # Configuración del modelo
        # El valor del parámetro loss es debido a estar trabajndo con múltiples clases
        model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
        model.summary()
        # Guardamos el modelo en la variable de clase, ya que será necesario para luego realizar las predicciones
        cls.model = model

        # Datos de prueba para el modelo
        sentencias_prueba = tokenizador.texts_to_sequences(cls.sentencias_prueba)
        testing_padded = pad_sequences(sentencias_prueba, maxlen=cls.long_sentencias, padding='post') 
        etiquetas_prueba = to_categorical(cls.etiquetas_prueba, num_classes=cls.cantidad_categorias)

        # A partir de la versión 2 de tf (TensorFlow), el modelo debe recibir datos del tipo de numpy (np) y no tipos de datos nativos de python
        training_padded = np.array(training_padded)
        etiquetas_entrenameinto = np.array(etiquetas_entrenameinto)
        testing_padded = np.array(testing_padded)
        etiquetas_prueba = np.array(etiquetas_prueba)

        print("TEST RESULTS")
        # Entrenamiento del modelo con los datos de entrenamiento y de prueba.
        history = model.fit(training_padded, etiquetas_entrenameinto, epochs=cls.iteraciones, validation_data=(testing_padded, etiquetas_prueba), verbose=2)
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
        if cls.tokenizador is None:
            raise ValueError("El tokenizador no está inicializado.")
        
        # Procesamiento de los datos de entrada. Tokenización strings.
        sequences = cls.tokenizador.texts_to_sequences(sentencias)
        padded = pad_sequences(sequences, maxlen=cls.long_sentencias, padding=cls.RELLENO, truncating=cls.TIPO_TRUNCADO)
        
        # Con la sentencia recibida ya tokenizada, le pedimos al modelo que haga la predicción.
        prediction = cls.model.predict(padded)
        res = np.argmax(prediction, axis=1)  # Devuelve la clase predicha con mayor probabilidad.
        predicciones = list(res)
        predicciones_int = [int(prediccion) for prediccion in predicciones]
        
        return predicciones_int
    
    @classmethod
    def re_entrenar(cls, data: dict) -> None:
        # Elimina el modelo ya creado
        ruta_modelo = cls.ruta_modelo+"/modelo_entrenado"
        shutil.rmtree(ruta_modelo) 
        
        # Actualiza las variables de clase según los datos recibidos
        cls.max_tokens = data['max_tokens']
        cls.dim_vector = data['dim_vector']
        cls.long_sentencias = data['long_sentencias']
        cls.iteraciones = data['iteraciones']
        # Vuelve a crear el modelo
        cls.crear_modelo()
    