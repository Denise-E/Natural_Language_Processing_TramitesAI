from flask import Flask, jsonify, request
from flask_cors import cross_origin

app = Flask(__name__)

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