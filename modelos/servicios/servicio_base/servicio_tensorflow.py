from abc import ABC, abstractmethod

class ServicioModelos(ABC):
    
    @abstractmethod
    def entrenar(cls) -> None:
        pass
    
    @abstractmethod
    def predecir(cls, sentencias: list) -> list:
        pass
    