from abc import ABC, abstractmethod
import re

class ServicioSpacy(ABC):
    
    @classmethod
    def completar_etiquetas(cls, predicciones: list, etiquetas: list) -> list:
        for prediccion in predicciones:
            keys = prediccion['campos'].keys()
            if len(keys) != len(etiquetas):
                for etiqueta in etiquetas:
                    if etiqueta not in prediccion['campos']:
                        # Construir el nombre del método
                        regex_method_name = f"regex_{etiqueta}"
                        # Verifica que existe un método de regex para ese atributo
                        if hasattr(cls, regex_method_name):
                            # Obtener el método usando getattr
                            regex_method = getattr(cls, regex_method_name)
                            prediccion['campos'][etiqueta] = regex_method(prediccion['texto'])
                        else:
                            prediccion['campos'][etiqueta] = None
                            print(f"El método {regex_method_name} no existe en {cls.__name__}")
    
    @classmethod
    def hacer_predecccion(cls, textos: list, model_class, etiquetas:list) -> list:
        """
        Retorna una lista de diccionarios, cada diccionario contiene la sentencia evaluada y las etiquetas
        que fueron encontradas en ella.
        
        params:
        model_class: Clase del modelo de SpaCy a utilizar para predecir
        """
        predicciones = []
        for sentencia in textos:
            resultado_predicciones = model_class.predict([sentencia])
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
        cls.completar_etiquetas(predicciones, etiquetas)
        return predicciones
    
    
    @classmethod
    def regex_marca(cls, texto: str, campos_encontrados: dict = None) -> str | None:
        marca_regex = r'(Alfa Romeo|Audi|BMW|Chevrolet|Chery|Chrysler|Citroën|Dacia|Dodge|DS|Ferrari|Fiat|Ford|Geely|Great Wall|Haval|Honda|Hyundai|Iveco|Jaguar|Jeep|Kia|Lamborghini|Land Rover|Lexus|Lifan|Mercedes-Benz|Mini|Mitsubishi|Nissan|Peugeot|Porsche|RAM|Renault|Seat|Subaru|Suzuki|Toyota|Volkswagen|Volvo|alfa romeo|audi|bmw|chevrolet|chery|chrysler|citroën|dacia|dodge|ds|ferrari|fiat|ford|geely|great wall|haval|honda|hyundai|iveco|jaguar|jeep|kia|lamborghini|land rover|lexus|lifan|mercedes-benz|mini|mitsubishi|nissan|peugeot|porsche|ram|renault|seat|subaru|suzuki|toyota|volkswagen|volvo)'
        marca_match = re.search(marca_regex, texto, re.IGNORECASE)
        return marca_match.group(0) if marca_match else None
    
    @classmethod
    def regex_modelo(cls, texto: str, campos_encontrados: dict = None) -> str | None:
        modelo_regex = r'(?:marca[:\s,=]*|marca es[:\s]*|modelo\s+)([a-zA-Z\s]+)'
        modelo_match = re.search(modelo_regex, texto, re.IGNORECASE)
        if not modelo_match and campos_encontrados is not None and 'marca' in campos_encontrados and campos_encontrados['marca'] is not None:
            palabra_clave = campos_encontrados['marca'] 
            palabras_excluidas = r'\b(de|para|como|por|si|pero|no|posible|posiblemente)\b'
            modelo_regex = rf'{palabra_clave}\s+((?!{palabras_excluidas})[a-zA-Z\s]+)'
            modelo_match = re.search(modelo_regex, texto, re.IGNORECASE)
        return modelo_match.group(1) if modelo_match else None
   
    @classmethod
    def regex_anio(cls, texto: str, campos_encontrados: dict = None) -> str | None:
        texto = texto.lower()
        if campos_encontrados is not None and 'cod_postal' in campos_encontrados and campos_encontrados['cod_postal'] is not None:
            texto = texto.replace(campos_encontrados['cod_postal'], '').strip()
        anio_regex = r'(?:año[:\s,=]*|año es[:\s]*|del[:\s]*)([0-9]{4})'
        anio_match = re.search(anio_regex, texto)
        
        if not anio_match:
            anio_general_regex = r'([0-9]{4})'
            anio_match = re.search(anio_general_regex, texto)
        return anio_match.group(1) if anio_match else None
    
    @classmethod
    def regex_cod_postal(cls, texto: str, campos_encontrados: dict = None) -> str | None:
        # Patrón para normalizar código postal
        texto = texto.lower()
        texto = texto.replace("codigo", "cod")
        texto = texto.replace("código", "cod")
        # Para que lo remplace si "pos" viene sólo y no dentro de otra palabra como "postal"
        texto = re.sub(r'\bpos\b', 'postal', texto)
        texto = texto.replace("cp", "cod postal")
        cod_postal_regex = r'cod postal(?:[:\s,=]| es[:\s]*)*([0-9]{4,5})'
        cod_postal_match = re.search(cod_postal_regex, texto)
        return cod_postal_match.group(1) if cod_postal_match else None