from modelos.tramites.poliza_auto.tramites_data.data import TRAIN_DATA as POLIZA_AUTO_DATOS
from modelos.tramites.tramites_clase import Tramite
from flask import Flask, jsonify, request
from flask_cors import cross_origin
import os

"""
Hasta la implementación de las rutas, para correr el modelo de asuntos se deberá correr el archivo main_asuntos.py,
el cuál se encuentra dentro de la carpeta modelos > asuntos.

Para correr el modelo de pólizas de autos, se debe correr el archivo tramites_ner.py, el cuál se encuentra dentro de la
carpeta modelos > tramites
"""

app = Flask(__name__) 
 

# Se ejecutará automáticamente cada vez que se levante el proyectp
POLIZA_AUTO_RUTA = os.getenv("POLIZA_AUTO_GUARDADO")
TRAMITE_POLIZA_AUTO = Tramite(POLIZA_AUTO_RUTA, POLIZA_AUTO_DATOS)

    
# Routes
@app.route("/ping", methods=['GET']) 
@cross_origin()
def ping_pong():
    try:
        return jsonify({
        "resultados": [
                {
                    "texto": "Hola quiero consultar por la póliza para un ford fiesta 2018, mi código posstal es 5000",
                    "campos": {
                        'marca': 'ford',
                        'modelo': 'fiesta',
                        'año': '2018',
                        'cod_postal': '5000'
                    }, 
                }
            ]
        }), 200
        #return {"msg": "pong"}, 200
    except Exception as e:
        return jsonify({"msg": 'Error'}), 400

@app.route("/poliza_auto", methods=['POST']) 
@cross_origin()
def poliza_auto():
    try:
        sentencias = request.json.get("textos")
        prediccion = []
        for sentencia in sentencias:
            prediction = TRAMITE_POLIZA_AUTO.predict([sentencia])
            campos = {}
            
            for predict in prediction:
                for label, value in predict.items():
                    campos[label] = value
            
            prediccion.append(
                {
                    "texto": sentencia,
                    "campos": campos
                }
            )
        return {"resultados": prediccion}, 200
    except Exception as e:
        print(e)
        return jsonify({"msg": "Error al evualuar póliza de auto"}), 400

@app.route("/poliza_hogar", methods=['POST']) 
@cross_origin()
def poliza_hogar():
    try:
        return {"msg": "ruta no implementada"}, 200
    except Exception as e:
        return jsonify({"msg": "Error al evualuar póliza del hogar"}), 400

@app.route("/denuncia_siniestro", methods=['POST']) 
@cross_origin()
def denuncia_siniestro():
    try:
        return {"msg": "ruta no implementada"}, 200
    except Exception as e:
        return jsonify({"msg": "Error al evualuar la denuncia de siniestro"}), 400

@app.route("/carga_presupuesto", methods=['POST']) 
@cross_origin()
def carga_presupuesto():
    try:
        return {"msg": "ruta no implementada"}, 200
    except Exception as e:
        return jsonify({"msg": "Error al evualuar el presupuesto"}), 400

@app.route("/evaluar_asunto", methods=['POST']) 
@cross_origin()
def evaluar_asunto():
    try:
        return {"msg": "ruta no implementada"}, 200
    except Exception as e:
        return jsonify({"msg": "Error al evualuar el asunto"}), 400

if __name__ == '__main__':
    app.run(port=5000)