from modelos.servicios.servicio_base.servicio_modelos import ServicioModelos
from abc import abstractmethod

class ServicioTensorFlow(ServicioModelos):
    
    @abstractmethod
    def entrenar(cls) -> None:
        pass
    
    @abstractmethod
    def predecir(cls, sentencias: list) -> list:
        pass
    
    @classmethod
    def tensorflow_config(cls, data: dict, max_tokens: int, dim_vector: int, long_sentencias: int, iteraciones: int) -> None:
        if 'max_tokens' not in data:
            data['max_tokens'] = max_tokens
            
        if 'dim_vector' not in data:
            data['dim_vector'] = dim_vector
        
        if 'long_sentencias' not in data:
            data['long_sentencias'] = long_sentencias
        
        if 'iteraciones' not in data:
            data['iteraciones'] = iteraciones
        #return data
    