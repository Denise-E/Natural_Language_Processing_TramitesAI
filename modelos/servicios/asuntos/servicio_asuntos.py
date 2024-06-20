import os
import logging

from modelos.modelos_base.modelo_tensorflow import ModeloTensorFlow
from modelos.servicios.servicio_base.servicio_tensorflow import ServicioModelos


# Suprimir advertencias
logging.getLogger('tensorflow').setLevel(logging.ERROR)

MODELO_RUTA = os.getenv("MODELO_ASUNTO_GUARDADO")

class ServicioAsuntos(ServicioModelos):
    modelo_asuntos = ModeloTensorFlow(vocab_size=10000, embedding=16, max_length=10000, num_epochs=4000, model_path=MODELO_RUTA)
    
    @classmethod
    def entrenar(cls) -> None :
        cls.modelo_asuntos.crear_modelo()
        
    @classmethod
    def predecir(cls, sentencias: list) -> list:
        predicciones = cls.modelo_asuntos.predecir(sentencias)
        return predicciones
    
    '''@classmethod
    def __init__(cls, vocab_size: int = 10000, embedding: int = 16, max_length: int = 10000, num_epochs: int = 4000):
        super().__init__(vocab_size, embedding, max_length, num_epochs, MODELO_RUTA)
        print("Servicio de asuntos inicializado")'''