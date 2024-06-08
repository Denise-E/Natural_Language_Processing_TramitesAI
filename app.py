from modelos.servicios.servicio_poliza_auto import ServicioPolizasAuto
from modelos.servicios.servicio_asuntos import ServicioAsuntos
from flask_swagger_ui import get_swaggerui_blueprint
from flask import Flask, jsonify, request
from utils.swagger import swagger_data
from flask_cors import cross_origin

app = Flask(__name__) 

# Swagger documentation
@app.route('/swagger.json')
def swagger():
    return jsonify(swagger_data)

SWAGGER_URL = '/swagger'
API_URL = '/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Tramites AI"
    }
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
    
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
        servicio_asuntos = ServicioAsuntos()
        textos = request.json.get('textos')
        res = servicio_asuntos.predecir(textos)
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
        return jsonify({"msg": "ruta no implementada"}), 501
    except Exception as e:
        print("Error: ", e)
        return jsonify({"msg": "Error al evualuar póliza del hogar"}), 400


@app.route("/denuncia_siniestro", methods=['POST']) 
@cross_origin()
def denuncia_siniestro():
    try:
        return jsonify({"msg": "ruta no implementada"}), 501
    except Exception as e:
        print("Error: ", e)
        return jsonify({"msg": "Error al evualuar la denuncia de siniestro"}), 400


@app.route("/carga_presupuesto", methods=['POST']) 
@cross_origin()
def carga_presupuesto():
    try:
        return jsonify({"msg": "ruta no implementada"}), 501
    except Exception as e:
        print("Error: ", e)
        return jsonify({"msg": "Error al evualuar el presupuesto"}), 400


if __name__ == '__main__':
    app.run(port=5000)
    