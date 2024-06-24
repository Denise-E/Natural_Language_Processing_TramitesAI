from sklearn.model_selection import train_test_split, StratifiedKFold
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer
from keras.models import load_model
import tensorflow as tf
import pandas as pd
import numpy as np
import logging
import shutil
import pickle
import os

# Suprime logs de tensorflow
logging.getLogger('tensorflow').setLevel(logging.ERROR)

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
        # Configurar y entrenar el modelo
        cls.configuracion_entrenamiento_modelo(X_train_fold, y_train_fold, X_val_fold, y_val_fold)
            
    @classmethod
    def configuracion_entrenamiento_modelo(cls, X_train, y_train, X_val, y_val):
        # 1. Tokenización de las sentencias y tratamiento de los datos
        """
        Tokenizador:
        
        - No distingue minusculas y mayúsculas, tampoco simbolos. Si reconoce acentos.
        - El parámetro "num_words" determina la cantidad máxima de tokens que se generarán. Por ejemplo, si se le define el valor 100 y en los 
        datos de capacitación hay 200 palabras distintas, tokenizará únicamente las 100 palabras más repetidas.
        - El valor dado al parámetro oov_token es el identificador que se usará para luego para tokenizar palabras que no se encontraban, o no fueron tokenizados, al procesarse los datos de capacitación. 
        El token '0' guardará este valor, en nuetsro caso {0: "<OOV>"}
        """
        cls.tokenizador = Tokenizer(num_words=cls.max_tokens, oov_token=cls.OOV_TOKEN)
        cls.tokenizador.fit_on_texts(X_train)

        X_train_sequences = cls.tokenizador.texts_to_sequences(X_train)
        X_val_sequences = cls.tokenizador.texts_to_sequences(X_val)

        """
        pad_sequences:
        
        - maxlen debe definirse por concordancia con el resto del proceso.
        - Todas las oraciones deben tener la misma cantidad de palabras, se resuelve completando con la cantidad de OOV_TOKEN necesarios en cada oración.
        - Se completará con el OOV_TOKEN al final, dado por el valor 'post' del parámetro padding.
        Por ejemplo, en una oración de 3 palabras que deba llevarse a una longitud de 5 palabras, quedará [1,2,3,<OOV>,<OOV>]
        """
        X_train_padded = pad_sequences(X_train_sequences, maxlen=cls.long_sentencias, padding=cls.RELLENO, truncating=cls.TIPO_TRUNCADO)
        X_val_padded = pad_sequences(X_val_sequences, maxlen=cls.long_sentencias, padding=cls.RELLENO, truncating=cls.TIPO_TRUNCADO)

        # 2. Creación y configuración del modelo de red neuronal
        cls.model = tf.keras.Sequential([
            tf.keras.layers.Embedding(cls.max_tokens, cls.dim_vector, input_length=cls.long_sentencias),
            tf.keras.layers.GlobalAveragePooling1D(),
            tf.keras.layers.Dense(24, activation='relu'),
            tf.keras.layers.Dense(cls.cantidad_categorias, activation='softmax')
        ])

        # Configuración del modelo
        # El valor del parámetro loss es debido a estar trabajndo con múltiples clases
        cls.model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        # A partir de la versión 2 de tf (TensorFlow), el modelo debe recibir datos del tipo de numpy (np) y no tipos de datos nativos de python
        X_train_padded = np.array(X_train_padded)
        y_train = np.array(y_train)
        X_val_padded = np.array(X_val_padded)
        y_val = np.array(y_val)
        
        # Entrenamiento del modelo con los datos de entrenamiento y de prueba
        cls.model.fit(X_train_padded, y_train, epochs=cls.iteraciones, validation_data=(X_val_padded, y_val))

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
    