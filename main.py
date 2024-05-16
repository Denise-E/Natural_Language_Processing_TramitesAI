from modelos.asuntos import ModeloAsuntos
from modelos.asuntos_modelo2 import ModeloAsuntosDos

MODELO_ASUNTOS =  ModeloAsuntos()
#MODELO_ASUNTOS = ModeloAsuntosDos()

def modelo_asuntor_prediccion(sentendes: list):
    return MODELO_ASUNTOS.model_prediction_tests(sentence=sentences)
    
    
sentences = [
    "solicitud cotizacion póliza del hogar", 
    "solicitud póliza del hogar", 
    "que seas feliz", 
    "vacaciones en Mardel", 
    "notificación membresia", 
    "notificación membresía"
]

print("********************* PREDICCIÓN *************************")
print("Información modelo:" )
print("Cantidad de iteraciones al momento de la capacitación del modelo: 3000")
print("Cantidad datos de entrenamiento: 179")
print("Cantidad datos de PRUEBA: 30")

prediccion = modelo_asuntor_prediccion(sentences)
print("SENTENCES:",sentences)
print("PREDICTION:", prediccion)
print("**************************************************************")
