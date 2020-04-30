from flask import Flask, request, jsonify
from rfidSensor import RFDISensor
import os
import base64
from keyLoader import loadPublic

app = Flask(__name__)

PORT = os.getenv("PORT", 6000)
ORDER_ID = os.getenv("ORDER_ID", "123AA")

publicKey = loadPublic()
print("Public key loaded")

@app.route("/drone/<string:droneId>/key", methods=['GET'])
def getKey(droneId: str):
    return {"public_key": str(publicKey.save_pkcs1(), "UTF-8")}

@app.route("/order/<string:restaurantId>", methods=['POST'])
def placeOrder(restaurantId: str):
    return {
        "drone_public": str(publicKey.save_pkcs1(), "UTF-8"),
        "order_id": "123AA"
    }

if __name__ == '__main__':
    app.run('0.0.0.0', PORT)
