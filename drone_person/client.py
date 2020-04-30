from rfidSensor import RFDISensor
import os
import rsa
import base64
import time
import json
from keyLoader import loadPrivate, loadPublic
import requests

DELTA = os.getenv("DELTA", 10)
server_address = os.getenv("SERVER_ADDRESS", "http://127.0.0.1:6000")

privateKey = loadPrivate()
print("Private key loaded")

droneRFID = RFDISensor(privateKey)


def orderCame(publicKey, orderId):
    try:
        data = droneRFID.read()
        if abs(float(data["timestamp"]) - time.time()) < DELTA:
            rsa.verify(data["timestamp"], data["sign"], publicKey)
            if data["order_id"] == orderId:
                print("Yummy :)")
    except Exception as e:
        print("Error happened")
        print(e)


def runOrder(restaurantId: str):
    response = requests.post(server_address+"/order/"+restaurantId)
    data = response.json()
    publicKey = rsa.PublicKey.load_pkcs1(data["drone_public"])
    droneRFID.orderPlaced(data["order_id"], lambda: orderCame(
        publicKey, data["order_id"]))


def run():
    while True:
        if input("> ") == "place":
            runOrder("123")


if __name__ == '__main__':
    run()
