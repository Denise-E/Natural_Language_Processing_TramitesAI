from modelos.tramites.poliza_auto.tramites_data.data import TRAIN_DATA as POLIZA_AUTO_DATOS
from modelos.tramites.tramites_clase import Tramite
import os

POLIZA_AUTO_RUTA = os.getenv("POLIZA_AUTO_GUARDADO")

class ServicioModelos:
    tramite_poliza_auto = Tramite(POLIZA_AUTO_RUTA, POLIZA_AUTO_DATOS)
    
    @classmethod
    def predecir_asunto(cls, asuntos: list) -> list:
        pass
    
    @classmethod
    def predecir_poliza_auto(cls, sentencias: list) -> list:
        
        prediccion = []
        for sentencia in sentencias:
            sentencia = sentencia.lower()
            resultado_predicciones = cls.tramite_poliza_auto.predict([sentencia])
            campos = {}
            
            for resultado in resultado_predicciones:
                for etiqueta, valor in resultado.items():
                    campos[etiqueta] = valor
            
            prediccion.append(
                {
                    "texto": sentencia,
                    "campos": campos
                }
            )
        return prediccion
    
    @classmethod
    def predecir_poliza_hogar(cls, sentencias: list) -> list:
        pass
    
    @classmethod
    def predecir_presupuesto(cls, sentencias: list) -> list:
        pass
    
    @classmethod
    def predecir_denuncia_siniestro(cls, sentencias: list) -> list:
        pass