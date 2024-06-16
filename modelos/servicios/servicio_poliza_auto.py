from modelos.servicios.servicio_base.servicio_spacy import ServicioSpacy
from modelos.tramites.poliza_auto.tramites_data.data import TRAIN_DATA as POLIZA_AUTO_DATOS
from modelos.tramites.tramites_clase import Tramite
import os

POLIZA_AUTO_RUTA = os.getenv("POLIZA_AUTO_GUARDADO")

class ServicioPolizasAuto(ServicioSpacy):
    tramite_poliza_auto = Tramite(POLIZA_AUTO_RUTA, POLIZA_AUTO_DATOS)
    ETIQUETAS = ['marca', 'cod_postal', 'modelo', 'anio']
    
    @classmethod
    def entrenar(cls) -> None :
        cls.tramite_poliza_auto.entrenar(POLIZA_AUTO_DATOS)
        
    @classmethod
    def predecir(cls, sentencias: list) -> list:
        """
        Retorna una lista de diccionarios, cada diccionario contiene la sentencia evaluada y las etiquetas
        que fueron encontradas en ella.
        """
        predicciones = []
        for sentencia in sentencias:
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
                        # Construir el nombre del método
                        regex_method_name = f"regex_{etiqueta}"
                        # Obtener el método usando getattr
                        regex_method = getattr(ServicioSpacy, regex_method_name)
                        prediccion['campos'][etiqueta] = regex_method(prediccion['texto'], prediccion['campos'])

    