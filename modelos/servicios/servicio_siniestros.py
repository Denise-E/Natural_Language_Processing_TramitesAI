from modelos.servicios.servicio_base.servicio_spacy import ServicioSpacy

class ServicioSiniestros(ServicioSpacy):
    
    @classmethod
    def predecir(cls, sentencias: list) -> list:
        pass
    
    @classmethod
    def completar_etiquetas(cls, predicciones: list) -> list:
        pass
    