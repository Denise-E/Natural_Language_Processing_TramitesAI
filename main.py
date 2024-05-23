from datetime import datetime
from modelos.asuntos_multi_clases import ModeloAsuntosMultiClases

inicio = datetime.now()
# TODO probar con 3000 iteraciones
MODELO_ASUNTOS = ModeloAsuntosMultiClases(vocab_size=10000,embedding=16,max_length=10000, num_epochs=4000) 

def predecir(sentencia: list):
    return MODELO_ASUNTOS.model_prediction_tests(sentencia)
    
# Sentencias a prdecir, junto al outcome esperado
sentences = [
    ["siniestro a denunciar", 1 ],
    ["denuncia siniestro urgente", 1 ],
    ["auto cotizacion", 2 ],
    ["envio presupuestos", 4],
    ["solicitud cotizacion póliza del hogar",  3 ],
    ["solicitud póliza del hogar",  3],
    ["vacaciones en Mardel", 0],
    ["notificación membresia", 0 ],
    ["notificación membresía", 0 ],
    ["cotizar vehículo", 2],
    ["presupuestar por favor", 4],
    ["presupuestación", 4],
    ["que seas feliz", 0 ],
    ["premio mayor", 0 ], 
    ["participa de este imperdible momento!", 0 ],
    ["inscribite al seminario web", 0 ],
    ["¿Conocés AWS?", 0 ] 
]

print("Información modelo:" )
print("Cantidad de iteraciones al momento de la capacitación del modelo: 3000")
print("Total de datos: 750")
print("Cantidad datos de capacitación: 600 - 80%")
print("Cantidad datos de testeo: 150 - 20%")
print("********************* INICIO PREDICCIÓNES *************************")
for sentence in sentences:
    prediccion = predecir([sentence[0]])
    print("STRING A PREDECIR: ",sentence[0], " RESULTADO ESPERADO: ", sentence[1])
    print("PREDICCIÓN:", prediccion)
print("********************** FIN PREDICCIÓNES **************************")
fin = datetime.now()
tiempo_proceso_segs = fin - inicio
# Obtener la diferencia en minutos
tiempo_proceso_mins = tiempo_proceso_segs.total_seconds() / 60

print(f"Han pasado {tiempo_proceso_mins} minutos.")
