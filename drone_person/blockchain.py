from hashlib import sha256
import json
import geocoder


class Block:
    def __init__(self, transaction, timestamp, gps_coords, previous_hash):
        self.transaction = transaction
        self.timestamp = timestamp
        self.gps_coords = gps_coords
        self.previous_hash = previous_hash
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return sha256(block_string.encode()).hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(None, 0, geocoder.ip("me").latlng, None)
        self.chain.append(genesis_block)

    def add_block(self, block, proof):
        last = self.last_block()
        previous_hash = last.compute_hash()

        if previous_hash != block.previous_hash or block.compute_hash() != block.hash:
            return False

        self.chain.append(block)
        return True

    def last_block(self):
        return self.chain[-1]
