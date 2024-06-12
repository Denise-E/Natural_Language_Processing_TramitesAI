from modelos.servicios.servicio_base.servicio_modelos import ServicioModelos
from modelos.tramites.poliza_auto.tramites_data.data import TRAIN_DATA as POLIZA_AUTO_DATOS
from modelos.tramites.tramites_clase import Tramite
import os

POLIZA_AUTO_RUTA = os.getenv("POLIZA_AUTO_GUARDADO")

class ServicioPolizasAuto(ServicioModelos):
    tramite_poliza_auto = Tramite(POLIZA_AUTO_RUTA, POLIZA_AUTO_DATOS)
    ETIQUETAS = ['marca', 'modelo', 'anio', 'cod_postal']
    
    @classmethod
    def entrenar(cls):
        cls.tramite_poliza_auto.entrenar(POLIZA_AUTO_DATOS)
        
    @classmethod
    def predecir(cls, sentencias: list) -> list:
        """
        Retorna una lista de diccionarios, cada diccionario contiene la sentencia evaluada y las etiquetas
        que fueron encontradas en ella.
        """
        predicciones = []
        for sentencia in sentencias:
            sentencia = sentencia.lower()
            resultado_predicciones = cls.tramite_poliza_auto.predict([sentencia])
            campos = {}
            for resultado in resultado_predicciones:
                if resultado:
                    for etiqueta, valor in resultado.items():
                        campos[etiqueta] = valor
            
            predicciones.append(
                {
                    "texto": sentencia,
                    "campos": campos
                }
            )
        
        cls.completar_etiquetas(predicciones)
        return predicciones
    
    @classmethod
    def completar_etiquetas(cls, predicciones: list) -> list:
        
        for prediccion in predicciones:
            keys = prediccion['campos'].keys()
            
            if len(keys) != len(cls.ETIQUETAS):
                for etiqueta in cls.ETIQUETAS:
                    if etiqueta not in prediccion['campos']:
                        prediccion['campos'][etiqueta] = None
    