import rsa
import json
import time
import random

ORDER_ID = 123


class RFDISensor:
    LENGTH = 64

    def __init__(self, dronePrivateKey: str):
        self.dronePrivateKey = dronePrivateKey

    def orderPlaced(self, orderId, onDone):
        # time.sleep(random.uniform(1, 3))
        self.orderId = orderId
        onDone()

    def read(self) -> str:
        timestamp = str(time.time()).encode("UTF-8")
        sign = rsa.sign(timestamp, self.dronePrivateKey, 'SHA-1')
        return {
            "order_id": self.orderId,
            "timestamp": timestamp,
            "sign": sign
        }
