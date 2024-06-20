from modelos.servicios.tramites.servicio_poliza_auto import ServicioPolizasAuto
from modelos.servicios.asuntos.servicio_asuntos import ServicioAsuntos
from flask_swagger_ui import get_swaggerui_blueprint
from flask import Flask, jsonify, request
from utils.swagger import swagger_data
from flask_cors import cross_origin

app = Flask(__name__) 

# Swagger - documentación
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
        return {"msg": "pong"}, 200
    except Exception as e:
        print("Error: ", e)
        return jsonify({"msg": 'Error'}), 400


@app.route("/evaluar_asunto", methods=['POST'])  
@cross_origin()
def evaluar_asunto():
    try:
        textos = request.json.get('textos')
        res = ServicioAsuntos.predecir(textos)
        return jsonify({"resultados": res}), 200
    except Exception as e:
        print("Error: ", e)
        return jsonify({"msg": "Error al evaluar el asunto"}), 400
    
    
@app.route("/poliza_auto", methods=['POST']) 
@cross_origin()
def poliza_auto():
    try:
        sentencias = request.json.get("textos")
        res = ServicioPolizasAuto.predecir(sentencias)
        return jsonify({"resultados": res}), 200
    except Exception as e:
        print("Error: ", e)
        return jsonify({"msg": "Error al evaluar póliza de auto"}), 400


@app.route("/poliza_hogar", methods=['POST']) 
@cross_origin()
def poliza_hogar():
    try:
        return jsonify({"msg": "Ruta no implementada"}), 501
    except Exception as e:
        print("Error: ", e)
        return jsonify({"msg": "Error al evaluar póliza del hogar"}), 400


@app.route("/denuncia_siniestro", methods=['POST']) 
@cross_origin()
def denuncia_siniestro():
    try:
        return jsonify({"msg": "Ruta no implementada"}), 501
    except Exception as e:
        print("Error: ", e)
        return jsonify({"msg": "Error al evaluar la denuncia de siniestro"}), 400


@app.route("/carga_presupuesto", methods=['POST']) 
@cross_origin()
def carga_presupuesto():
    try:
        return jsonify({"msg": "Ruta no implementada"}), 501
    except Exception as e:
        print("Error: ", e)
        return jsonify({"msg": "Error al evaluar el presupuesto"}), 400

@app.route("/entrenar/evaluar_asunto", methods=['POST'])  
@cross_origin()
def entrenar_modelo_asunto():
    try:
        try:
            data = request.json
            ServicioAsuntos.entrenar(data)
            return jsonify({"msg": True}), 200
        except Exception as e:
            print("Error al entrenar modelo de asuntos: ", e)
            return jsonify({"msg": "Error al entrenar modelo asuntos"}), 400
    except Exception as e:
        print("Error: ", e)
        return jsonify({"msg": "Error al entrenar modelo asuntos"}), 400
    
    
@app.route("/entrenar/poliza_auto", methods=['GET']) 
@cross_origin()
def entrenar_modelo_poliza_auto():
    try:
        try:
            ServicioPolizasAuto.entrenar()
            return jsonify({"msg": True}), 200
        except Exception as e:
            # Sumaría log
            print("Error al entrenar modelo pílizas de auto: ", e)
            return jsonify({"msg": "Error al entrenar el modelo de pólizas de auto"}), 400
    except Exception as e:
        print("Error: ", e)
        return jsonify({"msg": "Error al entrenar el modelo de pólizas de auto"}), 400


if __name__ == '__main__':
    app.run(port=5000)
    