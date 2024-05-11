import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences


class ModeloAsuntos:
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
        # 1. Definición de los strings de capacitación 
        sentences = [ 
            "denuncia de Siniestro",
            "denuncia de un siniestro",
            "denuncia siniestro",
            "siniestro",
            "denuncia",
            "presupuestos Solicitados",
            "presupuestos",
            "cotizacion",
            "cotización de pólizas de auto",
            "cotización de polizas de auto",
            "cotizacion de pólizas de auto",
            "cotizacion de polizas de auto",
            "polizas de auto",
            "pólizas de auto",
            "cotización de pólizas del hogar",
            "cotizacion de polizas del hogar",
            "polizas del hogar",
            "pólizas del hogar",
            "cotización pólizas auto",
            "cotización polizas auto",
            "cotizacion pólizas auto",
            "cotizacion polizas auto",
            "polizas auto",
            "pólizas auto",
            "cotización pólizas hogar",
            "cotización polizas hogar",
            "polizas hogar",
            "pólizas hogar",
            "vacaciones!", 
            "descuentos solo para vos",
            "solicitud Denuncia de Siniestro",
            "solicitud Denuncia de un siniestro",
            "solicitud Denuncia siniestro",
            "solicitud siniestro",
            "solicitud denuncia",
            "solicitud Presupuestos Solicitados",
            "solicitud presupuestos",
            "solicitud cotizacion",
            "solicitud Cotización de pólizas de auto",
            "solicitud Cotización de polizas de auto",
            "solicitud Cotizacion de pólizas de auto",
            "solicitud Cotizacion de polizas de auto",
            "solicitud polizas de auto",
            "solicitud pólizas de auto",
            "solicitud Cotización de pólizas del hogar",
            "solicitud Cotizacion de polizas del hogar",
            "solicitud polizas del hogar",
            "solicitud pólizas del hogar",
            "solicitud Cotización pólizas auto",
            "solicitud Cotización polizas auto",
            "solicitud Cotizacion pólizas auto",
            "solicitud Cotizacion polizas auto",
            "solicitud polizas auto",
            "solicitud pólizas auto",
            "solicitud Cotización pólizas hogar",
            "solicitud Cotización polizas hogar",
            "solicitud polizas hogar",
            "solicitud pólizas hogar",
            "pedido Denuncia de Siniestro",
            "pedido Denuncia de un siniestro",
            "pedido Denuncia siniestro",
            "pedido siniestro",
            "pedido denuncia",
            "pedido Presupuestos Solicitados",
            "pedido presupuestos",
            "pedido cotizacion",
            "pedido Cotización de pólizas de auto",
            "pedido Cotización de polizas de auto",
            "pedido Cotizacion de pólizas de auto",
            "pedido Cotizacion de polizas de auto",
            "pedido polizas de auto",
            "pedido pólizas de auto",
            "pedido Cotización de pólizas del hogar",
            "pedido Cotizacion de polizas del hogar",
            "pedido polizas del hogar",
            "pedido pólizas del hogar",
            "pedido Cotización pólizas auto",
            "pedido Cotización polizas auto",
            "pedido Cotizacion pólizas auto",
            "pedido Cotizacion polizas auto",
            "pedido polizas auto",
            "pedido pólizas auto",
            "pedido Cotización pólizas hogar",
            "pedido Cotización polizas hogar",
            "pedido polizas hogar",
            "pedido pólizas hogar",
            "conocé Datadog",
            "conoce Datadog",
            "feliz cumpleaños",
            "conocé nuestras ofertas",
            "conoce nuestros beneficios",
            "nuevo mensaje",
            "descubre todas las novedades",
            "últimos días",
            "nuevo lanzamiento",
            "nuevos lanzamientos",
            "pedido Cotización de polizas del hogar",
            "pedido Cotizacion de pólizas del hogar",
            "pedido Vacaciones en Mardel",
            "pedido Promoción en ropa",
            "pedido Cotizacion pólizas hogar",
            "pedido Cotizacion polizas hogar",
            "pedido Carga de presupuestos",
            "pedido presupuestos a cargar",
            "pedido Por favor cotizar",
            "solicitud Cotización de polizas del hogar",
            "solicitud Cotizacion de pólizas del hogar",
            "solicitud Vacaciones en Mardel",
            "solicitud Promoción en ropa",
            "solicitud Cotizacion pólizas hogar",
            "solicitud Cotizacion polizas hogar",
            "solicitud Carga de presupuestos",
            "solicitud presupuestos a cargar",
            "solicitud Por favor cotizar",
            "solicitud cotización",
            "necesito cotización",
            "necesito póliza",
            "necesito presupuesto",
            "cotización de pólizas de la casa",
            "cotizacion de polizas de la casa",
            "cotización de pólizas casa",
            "cotizacion de polizas casa",
            "cotización de pólizas vivienda",
            "cotizacion de polizas vivienda",
            "cotización de pólizas depto",
            "cotizacion de polizas depto",
            "cotización de pólizas departamento",
            "cotizacion de polizas departamento",
            "cotización de polizas veiculo",
            "cotizacion de pólizas veiculo",
            "cotizacion de polizas veiculo",
            "cotisasión de pólizas veiculo",
            "cotisasión de polizas veiculo",
            "cotisasion de pólizas veiculo",
            "cotisasion de polizas veiculo",
            "cotisasión de pólizas de auto",
            "cotisasión de polizas de auto",
            "cotisasion de pólizas de auto",
            "cotisasion de polizas de auto",
            "cotización de pólizas vehiculo",
            "cotización de polizas vehiculo",
            "cotizacion de pólizas vehiculo",
            "cotizacion de polizas vehiculo",
            "cotisasión de pólizas vehiculo",
            "cotisasión de polizas vehiculo",
            "cotisasion de pólizas vehiculo",
            "cotisasion de polizas vehiculo",
            "polisas de auto",
            "pólisas de auto",
            "¡gana un millón de dólares ahora!",
            "oferta especial: ¡Descuento del 50 porciento de descuento solo por hoy!",
            "aumenta tu puntaje de crédito al instante",
            "¡compra seguidores y likes para tus redes sociales!",
            "conoce a solteros locales cerca de ti",
            "reunión de equipo esta tarde a las 3 p.m.",
            "confirmación de reserva para la conferencia",
            "actualización semanal del proyecto",
            "recuerda enviar el informe antes del viernes",
            "invitación a la presentación del nuevo producto",
            "¡gana un iPhone gratis!",
            "¡oferta exclusiva: descuento del 70% en productos electrónicos!",
            "aumenta tus seguidores en redes sociales al instante",
            "¡deshazte de la deuda en 24 horas!",
            "¡sorteo de vacaciones todo incluido!",
            "¡conoce solteros calientes en tu área!",
            "¡baja de peso rápidamente con esta pastilla milagrosa!",
            "¡dinero fácil y rápido: hazte rico en una semana!",
            "¡prueba gratis nuestro producto y gana una tarjeta de regalo!",
            "¡increíble oportunidad de inversión con altos rendimientos!",
            "¡descubre el secreto para una piel perfecta!",
            "¡aprovecha esta oferta única: préstamos sin intereses!",
            "¡gana un viaje de lujo a las Bahamas!",
            "¡incrementa tus ingresos con este sistema probado!",
            "¡obtén un préstamo sin verificación de crédito!",
            "¡haz crecer tu negocio con nuestro software revolucionario!",
            "¡oferta limitada: suscríbete ahora y recibe un descuento adicional!",
            "¡descubre cómo ganar dinero desde casa!",
            "¡productos de belleza gratis solo por registrarte!",
            "¡tu cuenta ha sido seleccionada para recibir un premio especial!",
        ] #116 casos, 51 tokens
        # Resultados esperados.  1 = se vincula a nuestros tramites, 0 = no se vincula
        training_labels = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 

        # 2. Tokenización de las sentencias
        """
        Tokenizer:
        
        No distingue minusculas y mayúsculas, tampoco simbolos. Si reconoce acentos.
        num_words determina la cantidad máxima de tokens a general. Por ejemplo, si se le define el valor 100 y en los 
        datos de capacitación hay 200 palabras distintas, tokenizará únicamente las 100 palabras más repetidas.
        """
        tokenizer = Tokenizer(num_words=cls.VOCAB_SIZE, oov_token=cls.OOV_TOKEN) 
        tokenizer.fit_on_texts(sentences)
        cls.tokenizer = tokenizer
        word_indexed = tokenizer.word_index # Arma lista de las palabras tokenizadas
        print("Indexed  WORDS", word_indexed)

        training_sentences = tokenizer.texts_to_sequences(sentences) #Crea la secuencia de tokens para cada oración. Lista de listas
        """
        pad_sequences:
        
        Hay que deifnirle MAX_LENGTH por concordancia con resto del proceso
        Todas las sentencias deben tener la misma cantidad de palabras, eso se resuelve completando
        con la cantidad de OOV_TOKEN necesarios en cada sentencia. 
        Se completará con el OOV_TOKEN al final, dado por el valor 'post' del parámetro padding.
        Por ejmplo, en un caso de una sentencia formada por 3 palarbas que deba llevarse a una longitud de 
        5 palabras quedaría luego del este método formado de la siguiente manera: [1,2,3,<OOV>,<OOV>]
        """
        training_padded = pad_sequences(training_sentences,maxlen=cls.MAX_LENGTH, padding='post')  
        print("PADDED", training_padded)
        #print("PADDED SHAPE", training_padded.shape) #Filas x columns - Solo muestra cantidades
        
        # 3. Creación del Modelo
        # TODO Documentar
        model = tf.keras.Sequential([
            tf.keras.layers.Embedding(cls.VOCAB_SIZE, cls.EMBEDDING_DIM, input_length=cls.MAX_LENGTH), 
            tf.keras.layers.GlobalAveragePooling1D(), 
            tf.keras.layers.Dense(24, activation='relu'), 
            tf.keras.layers.Dense(1, activation='sigmoid')
        ])

        # Configuración del modelo
        model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
        model.summary()
        cls.model = model

        # Datos de prueba para el modelo
        testing_sentences = [
            "cotización de polizas del hogar", 
            "cotizacion de pólizas del hogar", 
            "vacaciones en Mardel", 
            "promoción en ropa",
            "cotizacion pólizas hogar",
            "cotizacion polizas hogar",
            "carga de presupuestos",
            "presupuestos a cargar",
            "por favor cotizar",
            "cotización",
            "recordatorio de pago de factura pendiente",
            "confirmación de reserva de hotel",
            "actualización de política de privacidad",
            "información sobre cambios en el horario de atención al cliente",
            "recordatorio de cita médica",
            "confirmación de registro en el evento",
            "notificación de entrega de paquete",
            "resumen mensual de cuenta bancaria",
            "invitación a evento de networking empresarial",
            "actualización sobre el estado de tu solicitud",
            "confirmación de reserva de vuelo",
            "recordatorio de fecha de vencimiento de suscripción",
            "informe de rendimiento trimestral",
            "recordatorio de reunión de equipo",
            "confirmación de compra en línea",
            "invitación a participar en encuesta de satisfacción",
            "notificación de cambio de contraseña de cuenta",
            "resumen de actividad en la cuenta de redes sociales",
            "recordatorio de renovación de membresía",
            "invitación a seminario web sobre desarrollo profesional"
        ] #30
        testing_sentences = tokenizer.texts_to_sequences(testing_sentences)
        testing_padded = pad_sequences(testing_sentences, maxlen=cls.MAX_LENGTH, padding='post') 
        testing_labels = [1,1,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

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
    def model_prediction_tests(cls, sentence: str) -> list[list[int]]:
        # Procesamiento de los datos de entrada. Tokenización strings.
        sequences = cls.tokenizer.texts_to_sequences(sentence)
        padded = pad_sequences(sequences, maxlen=cls.MAX_LENGTH, padding=cls.PADDING_TYPE, truncating=cls.TRUNC_TYPE)
        # Con la sentencia recibida ya tokenizada, le pedimos al modelo que haga la predicción.
        prediction = cls.model.predict(padded)
        return [prediction.tolist() , (prediction > 0.6).astype("int32")] #Valor a ajustar una vez que vaya sumando casos para la capacitación del modelo
