from modelos.asuntos_multi_clases import ModeloAsuntosMultiClases

MODELO_ASUNTOS = ModeloAsuntosMultiClases(vocab_size=10000,embedding=16,max_length=10000)

def predecir(sentencia: list):
    return MODELO_ASUNTOS.model_prediction_tests(sentencia)
    
# Sentencias a prdecir, junto al outcome esperado
sentences = [
    "siniestro a denunciar", #1 
    "auto cotizacion", #2 
    "envio presupuestos", #4
    "solicitud cotizacion póliza del hogar",  #3 
    "solicitud póliza del hogar",  #3
    "que seas feliz", #0 
    "vacaciones en Mardel", #0
    "notificación membresia", #0 
    "notificación membresía", #0 
]

print("Información modelo:" )
print("Cantidad de iteraciones al momento de la capacitación del modelo: 3000")
print("Total de datos: 646")
print("Cantidad datos de capacitación: 507 - 78%")
print("Cantidad datos de testeo: 139 - 22%")
print("********************* INICIO PREDICCIÓNES *************************")
for sentence in sentences:
    prediccion = predecir([sentence])
    print("STRING A PREDECIR:",sentence)
    print("PREDICCIÓN:", prediccion)
print("********************** FIN PREDICCIÓNES **************************")
