from modelos.tramites.spacy.clase_base import ModelosSpacy

class Tramite(ModelosSpacy):
    
    @classmethod
    def __init__(cls, url: str, training_data: list) -> None:
        ModelosSpacy.initialize(url, training_data)
    