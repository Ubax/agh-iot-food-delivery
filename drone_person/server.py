from flask import Flask, request, jsonify
from rfidSensor import RFDISensor
import os
import base64
from keyLoader import loadPublic
import socket
import threading
import json
import requests

PORT = os.getenv("PORT", 6000)
RESTAURANT_PORT = os.getenv("PORT", 7000)
ORDER_ID = os.getenv("ORDER_ID", "123AA")

app = Flask(__name__)

restaurants = {}

publicKey = loadPublic()
print("Public key loaded")

@app.route("/drone/<string:droneId>/key", methods=['GET'])
def getKey(droneId: str):
    return {"public_key": str(publicKey.save_pkcs1(), "UTF-8")}

@app.route("/restaurant", methods=['POST'])
def newRestaurant():
    data = request.get_json()
    restaurants[data["restaurant_id"]]=data["port"]
    return {"status": "added"}

@app.route("/order/<string:restaurantId>", methods=['POST'])
def placeOrder(restaurantId: str):
    data = {
        "drone_public": str(publicKey.save_pkcs1(), "UTF-8"),
        "order_id": "123AA"
    }
    def run():
        print(restaurants[restaurantId])
        requests.post(f"http://localhost:{restaurants[restaurantId]}/order", json=data)
    threading.Thread(target=run).start()
    return data

def runServer():
    app.run('0.0.0.0', PORT)

if __name__ == '__main__':
    runServer()
