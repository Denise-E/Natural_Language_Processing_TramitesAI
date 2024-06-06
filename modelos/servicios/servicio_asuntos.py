from modelos.servicios.servicio_base.servicio_modelos import ServicioModelos
from modelos.asuntos.modelo_asuntos import ModeloAsuntos

class ServicioAsuntos(ServicioModelos):
    modelo_suntos = ModeloAsuntos(vocab_size=10000,embedding=16,max_length=10000, num_epochs=4000)   
    
    @classmethod
    def predecir(cls, sentencias: list) -> list:
        """
        Retorna una lista de diccionarios, cada diccionario contiene el un asunto y el resultado de su clasificación,
        es decir la clase que fue determinada para él por el modelo (valor de 0 a 4)
        """
        predicciones = cls.modelo_suntos.predict(sentencias)
        predicciones_int = []
        for prediccion in predicciones:
            predicciones_int.append(int(prediccion))
        return predicciones_int
 
    