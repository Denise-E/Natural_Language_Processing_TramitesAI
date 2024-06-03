from modelos.tramites.poliza_auto.tramites_data.data import TRAIN_DATA as POLIZA_AUTO_DATOS
from modelos.tramites.tramites_clase import Tramite
from flask import Flask, jsonify, request
from flask_cors import cross_origin
import os

app = Flask(__name__)

"""
Hasta la implementación de las rutas, para correr el modelo de asuntos se deberá correr el archivo main_asuntos.py,
el cuál se encuentra dentro de la carpeta modelos > asuntos.

Para correr el modelo de pólizas de autos, se debe correr el archivo tramites_ner.py, el cuál se encuentra dentro de la
carpeta modelos > tramites
"""
# Se ejecutará automáticamente cada vez que se levante el proyectp
POLIZA_AUTO_RUTA = os.getenv("POLIZA_AUTO_GUARDADO")
TRAMITE_POLIZA_AUTO = Tramite(POLIZA_AUTO_RUTA, POLIZA_AUTO_DATOS)

    
# Routes
@app.route("/heath", methods=['GET']) 
@cross_origin()
def health():
    try:
        return {"msj": "ok"}, 200
    except Exception as e:
        return jsonify({"msj": 'Error'}), 400

@app.route("/poliza_auto", methods=['GET']) 
@cross_origin()
def poliza_auto():
    try:
        sentencias = request.get("textos")
        for sentencia in sentencias:
            print(sentencia)
            prediction = TRAMITE_POLIZA_AUTO.predict([sentencia])
            print(prediction)
            print(" *************************************** ")
        return {"msj": "ruta no implementada"}, 200
    except Exception as e:
        return jsonify({"msj": "Error al evualuar póliza de auto"}), 400

@app.route("/poliza_hogar", methods=['GET']) 
@cross_origin()
def poliza_hogar():
    try:
        return {"msj": "ruta no implementada"}, 200
    except Exception as e:
        return jsonify({"msj": "Error al evualuar póliza del hogar"}), 400

@app.route("/denuncia_siniestro", methods=['GET']) 
@cross_origin()
def denuncia_siniestro():
    try:
        return {"msj": "ruta no implementada"}, 200
    except Exception as e:
        return jsonify({"msj": "Error al evualuar la denuncia de siniestro"}), 400

@app.route("/carga_presupuesto", methods=['GET']) 
@cross_origin()
def carga_presupuesto():
    try:
        return {"msj": "ruta no implementada"}, 200
    except Exception as e:
        return jsonify({"msj": "Error al evualuar el presupuesto"}), 400

@app.route("/evaluar_asunto", methods=['GET']) 
@cross_origin()
def evaluar_asunto():
    try:
        return {"msj": "ruta no implementada"}, 200
    except Exception as e:
        return jsonify({"msj": "Error al evualuar el asunto"}), 400

if __name__ == '__main__':
    app.run(port=5000)