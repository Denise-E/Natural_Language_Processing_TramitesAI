from modelos.servicios.servicio_base.servicio_modelos import ServicioModelos

class ServicioAsuntos(ServicioModelos):
    
    @classmethod
    def predecir(cls, sentencias: list) -> list:
        """
        Retorna una lista de diccionarios, cada diccionario contiene el un asunto y el resultado de su clasificación,
        es decir la clase que fue determinada para él por el modelo (valor de 0 a 4)
        """
        return sentencias
    