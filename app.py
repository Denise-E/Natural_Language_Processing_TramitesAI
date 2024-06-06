from modelos.servicios.servicio_poliza_auto import ServicioPolizasAuto
from modelos.servicios.servicio_asuntos import ServicioAsuntos
from flask import Flask, jsonify, request
from flask_cors import cross_origin

"""
Hasta la implementación de las rutas, para correr el modelo de asuntos se deberá correr el archivo main_asuntos.py,
el cuál se encuentra dentro de la carpeta modelos > asuntos.
"""

app = Flask(__name__) 
    
# Routes
@app.route("/ping", methods=['GET']) 
@cross_origin()
def ping_pong():
    try:
        # Respuesta temporal para uso del equipo
        return jsonify({
        "resultados": [
                {
                    "texto": "Hola quiero consultar por la póliza para un ford fiesta 2018, mi código postal es 5000",
                    "campos": {
                        'marca': 'ford',
                        'modelo': 'fiesta',
                        'anio': '2018',
                        'cod_postal': '5000'
                    }, 
                }
            ]
        }), 200
        #return {"msg": "pong"}, 200
    except Exception as e:
        print("Error: ", e)
        return jsonify({"msg": 'Error'}), 400


@app.route("/evaluar_asunto", methods=['POST'])  
@cross_origin()
def evaluar_asunto():
    try:
        textos = request.json.get('textos')
        res = []
        res = ServicioAsuntos.predecir(textos)
        return jsonify({"resultados": res}), 200
    except Exception as e:
        print("Error: ", e)
        return jsonify({"msg": "Error al evualuar el asunto"}), 400
    
    
@app.route("/poliza_auto", methods=['POST']) 
@cross_origin()
def poliza_auto():
    try:
        sentencias = request.json.get("textos")
        res = ServicioPolizasAuto.predecir(sentencias)
        return jsonify({"resultados": res}), 200
    except Exception as e:
        print("Error: ", e)
        return jsonify({"msg": "Error al evualuar póliza de auto"}), 400


@app.route("/poliza_hogar", methods=['POST']) 
@cross_origin()
def poliza_hogar():
    try:
        return jsonify({"msg": "ruta no implementada"}), 200
    except Exception as e:
        print("Error: ", e)
        return jsonify({"msg": "Error al evualuar póliza del hogar"}), 400


@app.route("/denuncia_siniestro", methods=['POST']) 
@cross_origin()
def denuncia_siniestro():
    try:
        return jsonify({"msg": "ruta no implementada"}), 200
    except Exception as e:
        print("Error: ", e)
        return jsonify({"msg": "Error al evualuar la denuncia de siniestro"}), 400


@app.route("/carga_presupuesto", methods=['POST']) 
@cross_origin()
def carga_presupuesto():
    try:
        return jsonify({"msg": "ruta no implementada"}), 200
    except Exception as e:
        print("Error: ", e)
        return jsonify({"msg": "Error al evualuar el presupuesto"}), 400


if __name__ == '__main__':
    app.run(port=5000)
    