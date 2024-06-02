from flask import Flask, jsonify, request
from flask_cors import cross_origin

app = Flask(__name__)

"""
Hasta la implementación de las rutas, para correr el modelo de asuntos se deberá correr el archivo main_asuntos.py,
el cuál se encuentra dentro de la carpeta modelos > asuntos.

Para correr el modelo de pólizas de autos, se debe correr el archivo tramites_ner.py, el cuál se encuentra dentro de la
carpeta modelos > tramites
"""

# Routes
@app.route("/ping", methods=['GET']) 
@cross_origin()
def ping():
    try:
        return {"msj": "pong"}, 200
    except Exception as e:
        return jsonify({"msj": 'Error'}), 400

@app.route("/poliza_auto", methods=['GET']) 
@cross_origin()
def ping():
    try:
        return {"msj": "ruta no implementada"}, 200
    except Exception as e:
        return jsonify({"msj": "Error al evualuar póliza de auto"}), 400

@app.route("/poliza_hogar", methods=['GET']) 
@cross_origin()
def ping():
    try:
        return {"msj": "ruta no implementada"}, 200
    except Exception as e:
        return jsonify({"msj": "Error al evualuar póliza del hogar"}), 400

@app.route("/denuncia_siniestro", methods=['GET']) 
@cross_origin()
def ping():
    try:
        return {"msj": "ruta no implementada"}, 200
    except Exception as e:
        return jsonify({"msj": "Error al evualuar la denuncia de siniestro"}), 400

@app.route("/carga_presupuesto", methods=['GET']) 
@cross_origin()
def ping():
    try:
        return {"msj": "ruta no implementada"}, 200
    except Exception as e:
        return jsonify({"msj": "Error al evualuar el presupuesto"}), 400

@app.route("/evaluar_asunto", methods=['GET']) 
@cross_origin()
def ping():
    try:
        return {"msj": "ruta no implementada"}, 200
    except Exception as e:
        return jsonify({"msj": "Error al evualuar el asunto"}), 400

if __name__ == '__main__':
    app.run(port=5000)