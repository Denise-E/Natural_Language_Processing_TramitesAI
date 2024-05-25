"""
https://www.tensorflow.org/text/guide/word_embeddings?hl=es-419

Tengo 2 situaciones:

1. Saco info de los textos extraidos de documentos
    * (1) Denuncia Siniestro
        -> En la denuncia policial encuentro datos
    * (4) Carga presupuestos
        -> En el presupuesto encuentro datos
    

2. Saco info de los bodys, que son escritos libremente por quienes envian sus solicitudes - EMPIEZO POR ACÁ
    * (2) Cotización póliza de auto
        -> En el body encuentro datos
    * (3) Cotización póliza del hogar
        -> En el body encuentro datos

    Para esto voy a usar expresiones regulares y técnicas de reconocimiento de entidades nombradas (NER)
        
"""
import re

class ValidacionTramites:
    
    @classmethod
    def validate_tramit(cls, tramite: int, body: str) -> dict:
        body = body.lower()
        # Elimino puntos, signos de excalación y de interrogación
        body = re.sub(r'[.:!¡¿?]', '', body)

        if int(tramite) == 2: #Cotización póliza de auto
            fields = cls.search_car_policy_fields(body)
        if int(tramite) == 3:
            fields = cls.search_home_policy_fields(body)
            
        validation = cls.validate_completed_fields(fields)
        print(validation)
        return validation
    
    @classmethod
    def search_home_policy_fields(cls, text: str):
        """
        Campos: tipo inmueble, dirección, código postal, superficie y rejas
        """
        brand = None
        model = None
        year = None
        postal_code = cls.search_postal_code(text)
        res = {"marca": brand, "modelo": model, "año": year, "cp": postal_code}
        print(res)
        return res

    @classmethod
    def search_car_policy_fields(cls, text: str):
        """
        Campos: marca, modelo, año y código postal.
        """
        # Patrón para identificar marca
        brand_pattern = re.compile(r'marca\s*(\w+)', re.IGNORECASE)
        brand = brand_pattern.search(text)
        brand = brand.group(1) if brand else None

        # Patrón para identificar modelo
        model_pattern = re.compile(r'modelo\s*(\w+)', re.IGNORECASE)
        model = model_pattern.search(text)
        model = model.group(1) if model else None

        # Patrón para identificar año
        year_pattern = re.compile(r'año\s*(\d+)', re.IGNORECASE)
        year = year_pattern.search(text)
        year = year.group(1) if year else None

        postal_code = cls.search_postal_code(text)

        res = {"marca": brand, "modelo": model, "año": year, "cp": postal_code}
        print(res)
        return res
    
    @classmethod
    def search_postal_code(cls, text: str):
        # Patrón para identificar código postal
        text = text.replace("codigo", "cod")
        text = text.replace("código", "cod")
        # Para que lo remeplace si "pos" viene sólo y no dentro de otra palabra como "postal"
        text = re.sub(r'\bpos\b', 'postal', text)
        text = text.replace("cp", "cod postal")

        postal_code_pattern = re.compile(r'cod postal\s*(\d+)', re.IGNORECASE)
        postal_code = postal_code_pattern.search(text)
        postal_code = postal_code.group(1) if postal_code else None
        return postal_code

    @classmethod
    def validate_completed_fields(cls, fields: dict):
        res = {
            "success": True,
            "fields_missing": []
        }
        for key, value in fields.items():
            if not value:
                res['success'] = False
                res["fields_missing"].append(key)
        
        return res
        
val = ValidacionTramites()


print()
print("********** Ejemplos póliza para el auto *************** ")
print()
print("CASE 1")
input1 = "Buenas tardes, quisiera cotizar un seguro para mi auto. Por favor, envíenme las diferentes opciones que su compañia ofrece. Los datos de mi vehiculo son: \nMarca: Chevrolet \nModelo: Spin \nAño: 2023\nCod Postal: 1414 \nTengo cochera propia. Adjunto también foto de mi vehiculo para que se vea que está en perfectas condiciones.\nMuchas gracias"
val.validate_tramit(2, input1)
print()
print("CASE 2")
input2 = "Buenas tardes, quisiera cotizar un seguro para mi auto. Por favor, envíenme las diferentes opciones que su compañia ofrece. Los datos de mi vehiculo son: \nMarca Chevrolet \nModelo Spin \nAño 2023\nCod. Postal. 1414 \nTengo cochera propia. Adjunto también foto de mi vehiculo para que se vea que está en perfectas condiciones.\nMuchas gracias"
val.validate_tramit(2, input2)
print()
print("CASE 3")
input3 = "Buenas!! ¿Como estan? Los datos de mi vehiculo son: \nMarca Chevrolet \nModelo Spin \nAño: 2023\n cp. 1414 \nTengo cochera propia. Adjunto también foto de mi vehiculo para que se vea que está en perfectas condiciones.\nMuchas gracias"
val.validate_tramit(2, input3)

print()
print("********** Ejemplos póliza del hogar *************** ")
print()
print("CASE 4")
input4 = "Buenas tardes, quisiera cotizar un seguro para mi hogar. Por favor, envíenme las diferentes opciones que su compañía ofrece. Los datos de mi inmueble son: \nTipo de inmueble: Casa \nDirección: Calle Falsa 123, Ciudad \nCod Postal: 1414 \nSuperficie: 150 m² \nPoseo rejas en todas las ventanas y puertas. Adjunto también fotos del inmueble para que se vea su estado actual.\nMuchas gracias"
val.validate_tramit(3, input4)