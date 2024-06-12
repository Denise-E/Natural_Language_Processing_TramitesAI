import re
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
                        regex_method = getattr(cls, regex_method_name)
                        # Llamar al método y asignar el resultado
                        prediccion['campos'][etiqueta] = regex_method(prediccion['texto']) 
    
    @classmethod
    def regex_marca(cls, texto: str) -> str | None:
        marca_regex = r'(Alfa Romeo|Audi|BMW|Chevrolet|Chery|Chrysler|Citroën|Dacia|Dodge|DS|Ferrari|Fiat|Ford|Geely|Great Wall|Haval|Honda|Hyundai|Iveco|Jaguar|Jeep|Kia|Lamborghini|Land Rover|Lexus|Lifan|Mercedes-Benz|Mini|Mitsubishi|Nissan|Peugeot|Porsche|RAM|Renault|Seat|Subaru|Suzuki|Toyota|Volkswagen|Volvo|alfa romeo|audi|bmw|chevrolet|chery|chrysler|citroën|dacia|dodge|ds|ferrari|fiat|ford|geely|great wall|haval|honda|hyundai|iveco|jaguar|jeep|kia|lamborghini|land rover|lexus|lifan|mercedes-benz|mini|mitsubishi|nissan|peugeot|porsche|ram|renault|seat|subaru|suzuki|toyota|volkswagen|volvo)'
        marca_match = re.search(marca_regex, texto, re.IGNORECASE)
        return marca_match.group(0) if marca_match else None
    
    @classmethod
    def regex_modelo(cls, texto: str) -> str | None:
        #print("REGEX modelo") 
        return None
   
    @classmethod
    def regex_anio(cls, texto: str) -> str | None:
        #print("REGEX anio") 
        return None
    
    @classmethod
    def regex_cod_postal(cls, texto: str) -> str | None:
        # Patrón para normalizar código postal
        texto = texto.lower()
        texto = texto.replace("codigo", "cod")
        texto = texto.replace("código", "cod")
        # Para que lo remeplace si "pos" viene sólo y no dentro de otra palabra como "postal"
        texto = re.sub(r'\bpos\b', 'postal', texto)
        texto = texto.replace("cp", "cod postal")
        cod_postal_regex = r'cod postal(?:[:\s,=]| es[:\s]*)*([0-9]{4,5})'
        cod_postal_match = re.search(cod_postal_regex, texto)
        return cod_postal_match.group(1) if cod_postal_match else None

    """
    El modelo funcionaría bien si tendríamos las marcas y modelos empezando en mayúsculas, pero no queremos dar eso por
    obvio ya que la infromación va a salir del cuerpo de un mail o formulario, por lo que sumamos expresiones regulares
    para disminuir la cantidad de casos donde algunso datos no fueron encontrados.
    
    Esta idea tiene dos partes: 
    
    1. Aplicar expresiones regulares previo a realizar las predicciones, pero ene ste caso para
    que la primera letra de las marcas o modelos se encuentren en mayúscula y así el modelo NER pueda reconocerlas con
    mayor facilidad.
    
    2. Aplicar expresiones regulares en aquellos casos donde no se encontró el campo:
    
    # Expresiones regulares para encontrar marcas, modelos y años. Faltaría CP
    import re

    modelo_regex = r'(Corolla|Camry|Accord|Civic|Focus|Fiesta)'
    anio_regex = r'(\d{4})'

    # Buscar coincidencias en el texto
    modelo_match = re.search(modelo_regex, texto, re.IGNORECASE)
    anio_match = re.search(anio_regex, texto)

    # Obtener los resultados
    modelo = modelo_match.group(0) if modelo_match else None
    anio = anio_match.group(0) if anio_match else None
    
    """