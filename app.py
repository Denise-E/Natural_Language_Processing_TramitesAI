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
        return {"msg": "pong"}, 200
    except Exception as e:
        msg = f"Error on ping pong route: {e}"
        return jsonify({"msg": msg}), 400


if __name__ == '__main__':
    app.run(port=5000)