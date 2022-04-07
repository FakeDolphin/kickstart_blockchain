import time
import hashlib


class Block():

    def __init__(self, timestamp=None, data=None):
        self.timestamp = timestamp or time.time()
        self.transaction = [] if data is None else data
        self.prev_hash = None # Hash of preverious block
        self.nonce = 0
        self.hash = self.get_hash()

    def get_hash(self):
        # Set up hash for block
        hash = hashlib.new('sha256')
        hash.update(str(self.prev_hash).encode('UTF-8'))
        hash.update(str(self.timestamp).encode('UTF-8'))
        hash.update(str(self.transaction).encode('UTF-8'))
        hash.update(str(self.nonce).encode('utf-8'))

        return hash.hexdigest()

    def mine(self, difficulty):
        # Тут запускается цикл, работающий до тех пор, пока хеш не будет начинаться со строки
        # 0...000 длины <difficulty>.
        while self.hash[:difficulty] != '0' * difficulty:
            # Инкрементируем nonce, что позволяет получить совершенно новый хеш.
            self.nonce += 1
            # Пересчитываем хеш блока с учётом нового значения nonce.
            self.hash = self.get_hash()

a = Block()
print(a.hash)