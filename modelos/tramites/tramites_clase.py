from modelos.modelos_base.spacy.modelo_spacy import ModeloSpacy

class Tramite(ModeloSpacy):
    
    @classmethod
    def __init__(cls, url: str, training_data: list) -> None:
        ModeloSpacy.inicilizacion(url, training_data)
    