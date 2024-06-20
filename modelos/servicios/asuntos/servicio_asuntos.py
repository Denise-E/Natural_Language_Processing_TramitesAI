from modelos.servicios.servicio_base.servicio_modelos import ServicioModelos
from modelos.modelos_base.modelo_tensorflow import ModeloTensorFlow
import logging
import shutil
import os

# Suprime logs de tensorflow
logging.getLogger('tensorflow').setLevel(logging.ERROR)

MODELO_RUTA = os.getenv("MODELO_ASUNTO_GUARDADO")

class ServicioAsuntos(ServicioModelos):    
    modelo_asuntos = ModeloTensorFlow(max_tokens=10000, dim_vector=16, long_sentencias=10000, iteraciones=4000, ruta_modelo=MODELO_RUTA)
    
    @classmethod
    def entrenar(cls, data: dict) -> None :
        ruta_carpeta = MODELO_RUTA+"/modelo_entrenado"
        shutil.rmtree(ruta_carpeta)         
            
        max_tokens = data.get("max_tokens") if 'max_tokens' in data else 10000
        dim_vector = data.get("dim_vector") if 'dim_vector' in data else 16
        long_sentencias = data.get("long_sentencias") if 'long_sentencias' in data else 10000
        iteraciones = data.get("iteraciones") if 'iteraciones' in data else 4000
            
        cls.modelo_asuntos = ModeloTensorFlow(max_tokens=max_tokens, dim_vector=dim_vector, long_sentencias=long_sentencias, iteraciones=iteraciones, ruta_modelo=MODELO_RUTA)
        
    @classmethod
    def predecir(cls, sentencias: list) -> list:
        predicciones = cls.modelo_asuntos.predecir(sentencias)
        return predicciones
    