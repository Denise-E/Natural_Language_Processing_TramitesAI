from modelos.modelos_base.modelo_spacy import ModelosSpacy

class Tramite(ModelosSpacy):
    
    @classmethod
    def __init__(cls, url: str, training_data: list) -> None:
        ModelosSpacy.inicilizacion(url, training_data)
    