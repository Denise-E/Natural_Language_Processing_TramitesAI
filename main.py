from modelos.asuntos import ModeloAsuntos

MODELO_ASUNTOS =  ModeloAsuntos()

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

"""
PREDICTION: [[[0.9999709129333496], [0.9994049072265625], [0.17926892638206482], [0.5865851640701294], [0.49521031975746155], [0.49521031975746155]], array([[1],
       [1],
       [0],
       [0],
       [0],
       [0]])]
"""