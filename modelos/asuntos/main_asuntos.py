from datetime import datetime
import math
from modelos.asuntos.asuntos_multi_clases import ModeloAsuntosMultiClases

inicio = datetime.now()
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
    ["descuento en la membresia del gimnasio, ¡No te la pierdas!", 0 ],
    ["notificación membresía", 0 ],
    ["cotizar vehículo", 2],
    ["presupuestar por favor", 4],
    ["presupuestación", 4],
    ["¡Participá y obtené un premio!", 0 ],
    ["inscribite al seminario web", 0 ],
    ["¿Conocés los servicios de AWS?", 0 ] 
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
tiempo_proceso_mins = math.trunc(tiempo_proceso_segs.total_seconds() / 60)
print(f"El proceso completo demora {tiempo_proceso_mins} minutos.") 
# 23 a 41 mins 4000 iteraciones (en mi máquina)
# 16 a 30 mins 3000 iteraciones (en mi máquina)