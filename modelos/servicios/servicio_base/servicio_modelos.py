from abc import ABC, abstractmethod

class ServicioModelos(ABC):
    
    @abstractmethod
    def predecir(cls, textos: list) -> list:
        pass
    
