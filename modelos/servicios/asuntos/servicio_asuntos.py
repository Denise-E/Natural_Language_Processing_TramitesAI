from modelos.servicios.servicio_base.servicio_tensorflow import ServicioTensorFlow
from modelos.modelos_base.modelo_tensorflow import ModeloTensorFlow
import os

MODELO_RUTA = os.getenv("MODELO_ASUNTO_GUARDADO")
LONG_SENTENCIAS = 10000
MAX_TOKENS = 10000
ITERACIONES = 4000
DIM_VECTOR = 16

class ServicioAsuntos(ServicioTensorFlow):    
    modelo_asuntos = ModeloTensorFlow(max_tokens=MAX_TOKENS, dim_vector=DIM_VECTOR, long_sentencias=LONG_SENTENCIAS, iteraciones=ITERACIONES, ruta_modelo=MODELO_RUTA)
    
    @classmethod
    def entrenar(cls, data: dict) -> None :   
        ServicioTensorFlow.tensorflow_config(data,MAX_TOKENS,DIM_VECTOR,LONG_SENTENCIAS,ITERACIONES)
        cls.modelo_asuntos.re_entrenar(data)
        
    @classmethod
    def predecir(cls, sentencias: list) -> list:
        predicciones = cls.modelo_asuntos.predecir(sentencias)
        return predicciones
    