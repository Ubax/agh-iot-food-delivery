from flask import Flask, request, jsonify
from rfidSensor import RFDISensor
import os
import base64
import random
import requests
import json
import rsa
import time
from keyLoader import loadPrivate
import threading

privateKey = loadPrivate()
print("Private key loaded")

droneRFID = RFDISensor(privateKey)

app = Flask(__name__)
server_address = os.getenv("SERVER_ADDRESS", "http://127.0.0.1:6000")
DELTA = os.getenv("DELTA", 10)

port = random.randint(10000, 40000)

requests.post(server_address+'/restaurant',
              json={"restaurant_id": "123", "port": port})


def processOrder(publicKey, orderId):
    try:
        time.sleep(2)
        data = droneRFID.read()
        if abs(float(data["timestamp"]) - time.time()) < DELTA:
            rsa.verify(data["timestamp"], data["sign"], publicKey)
            if data["order_id"] == orderId:
                print("Order sent :)")
    except Exception as e:
        print("Error happened")
        print(e)


@app.route("/order", methods=['POST'])
def placeOrder():
    data = request.get_json()

    def run():
        droneRFID.setOrderId(data["order_id"])
        processOrder(rsa.PublicKey.load_pkcs1(
            data["drone_public"]), data["order_id"])
    threading.Thread(target=run).start()
    return {
        "status": "work began"
    }


if __name__ == '__main__':
    app.run('0.0.0.0', port)
