import time
import hashlib


class Block():

    def __init__(self, timestamp=None, data=None):
        self.timestamp = timestamp or time.time()
        self.transactions = [] if data is None else data
        self.prev_hash = None # Hash of preverious block
        self.hash = self.getHash()

    def getHash(self):
        # Set up hash for block
        hash = hashlib.new('sha256')
        hash.update(str(self.prev_hash).encode('UTF-8'))
        hash.update(str(self.timestamp).encode('UTF-8'))
        hash.update(str(self.transactions).encode('UTF-8'))
        return hash.hexdigest()

a = Block()
print(a.hash)