from modelos.asuntos_multi_clases import ModeloAsuntosMultiClases

MODELO_ASUNTOS = ModeloAsuntosMultiClases()

def predecir(sentencia: list):
    return MODELO_ASUNTOS.model_prediction_tests(sentencia)
    
# Sentencias a prdecir, junto al outcome esperado
sentences = [
    "siniestro a denunciar", #1 OK
    "auto cotizacion", #2 MAL TIRO 3 (HOGAR)
    "envio presupuestos", #4
    "solicitud cotizacion póliza del hogar",  #3 MAL TIRO 2 (AUTO)
    "solicitud póliza del hogar",  #3
    "que seas feliz", #0 # MAL TIRO 4 (presupuestos)
    "vacaciones en Mardel", #0
    "notificación membresia", #0 # Mal tiro 4 (presupuestos)
    "notificación membresía", #0 # Mal tiro 1 (denuncia siniestros)
]

print("Información modelo:" )
print("Cantidad de iteraciones al momento de la capacitación del modelo: 3000")
print("Cantidad datos de capacitación: 169")
print("Cantidad datos de testeo: 42")
print("********************* INICIO PREDICCIÓNES *************************")
for sentence in sentences:
    prediccion = predecir([sentence])
    print("STRING A PREDECIR:",sentence)
    print("PREDICCIÓN:", prediccion)
print("********************** FIN PREDICCIÓNES **************************")
