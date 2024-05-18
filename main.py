from modelos.deprecado.asuntos import ModeloAsuntos
from modelos.asuntos_multi_clases import ModeloAsuntosMultiClases

#MODELO_ASUNTOS =  ModeloAsuntos()
MODELO_ASUNTOS = ModeloAsuntosMultiClases()

def modelo_asuntor_prediccion(sentendes: list):
    return MODELO_ASUNTOS.model_prediction_tests(sentence=sentences)
    
# Sentencias a prdecir, junto al outcome esperado
sentences = [
    "siniestro a denunciar", #1
    "auto cotizacion", #2
    "envio presupuestos" #4
    "solicitud cotizacion póliza del hogar",  #3
    "solicitud póliza del hogar",  #3
    "que seas feliz", #0
    "vacaciones en Mardel", #0
    "notificación membresia", #0
    "notificación membresía", #0
]

print("Información modelo:" )
print("Cantidad de iteraciones al momento de la capacitación del modelo: 3000")
print("Cantidad datos de capacitación: 169")
print("Cantidad datos de testeo: 42")
print("********************* INICIO PREDICCIÓNES *************************")
prediccion = modelo_asuntor_prediccion(sentences)
print("SENTENCES:",sentences)
print("PREDICTION:", prediccion)
print("********************** FIN PREDICCIÓNES **************************")
