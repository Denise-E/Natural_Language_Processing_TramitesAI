import os
import logging

from modelos.servicios.servicio_base.servicio_tensorflow import ServicioTensorFlow


# Suprimir advertencias
logging.getLogger('tensorflow').setLevel(logging.ERROR)

MODELO_RUTA = os.getenv("MODELO_ASUNTO_GUARDADO")

class ServicioAsuntos(ServicioTensorFlow):
    
    @classmethod
    def __init__(cls, vocab_size: int = 10000, embedding: int = 16, max_length: int = 10000, num_epochs: int = 4000):
        super().__init__(vocab_size, embedding, max_length, num_epochs, MODELO_RUTA)
        print("Servicio de asuntos inicializado")