from modelos.servicios.servicio_base.servicio_modelos import ServicioModelos
from modelos.modelos_base.modelo_tensorflow import ModeloTensorFlow
import logging
import shutil
import os

# Suprime logs de tensorflow
logging.getLogger('tensorflow').setLevel(logging.ERROR)

MODELO_RUTA = os.getenv("MODELO_ASUNTO_GUARDADO")

class ServicioAsuntos(ServicioModelos):    
    modelo_asuntos = ModeloTensorFlow(vocab_size=10000, embedding=16, max_length=10000, num_epochs=4000, model_path=MODELO_RUTA)
    
    @classmethod
    def entrenar(cls, data: dict) -> None :
        ruta_carpeta = MODELO_RUTA+"/modelo_entrenado"
        shutil.rmtree(ruta_carpeta)         
            
        vocab_size = data.get("vocab_size") if 'vocab_size' in data else 10000
        embedding = data.get("embedding") if 'embedding' in data else 16
        max_length = data.get("max_length") if 'max_length' in data else 10000
        num_epochs = data.get("num_epochs") if 'num_epochs' in data else 4000
            
        cls.modelo_asuntos = ModeloTensorFlow(vocab_size=vocab_size, embedding=embedding, max_length=max_length, num_epochs=num_epochs, model_path=MODELO_RUTA)
        
    @classmethod
    def predecir(cls, sentencias: list) -> list:
        predicciones = cls.modelo_asuntos.predecir(sentencias)
        return predicciones
    