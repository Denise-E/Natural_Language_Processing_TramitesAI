from modelos.tramites.poliza_auto.datos.datos import TRAIN_DATA as POLIZA_AUTO_DATOS
from modelos.servicios.servicio_base.servicio_modelos import ServicioModelos
from modelos.servicios.servicio_base.servicio_spacy import ServicioSpacy
from modelos.tramites.tramites_clase import Tramite
import os

POLIZA_AUTO_RUTA = os.getenv("POLIZA_AUTO_GUARDADO")

class ServicioPolizasAuto(ServicioSpacy):
    modelo_poliza_auto = Tramite(POLIZA_AUTO_RUTA, POLIZA_AUTO_DATOS)
    ETIQUETAS = ['marca', 'cod_postal', 'modelo', 'anio']
    
    @classmethod
    def entrenar(cls) -> None :
        cls.modelo_poliza_auto.entrenar(POLIZA_AUTO_DATOS)
        
    @classmethod
    def predecir(cls, sentencias: list) -> list:
        predicciones = ServicioSpacy.hacer_predecccion(sentencias, cls.modelo_poliza_auto, cls.ETIQUETAS)
        return predicciones
    
    