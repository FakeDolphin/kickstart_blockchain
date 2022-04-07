import json
from time import time
from block import Block


class Blockchain():

    def __init__(self):
        self.block_time = 30000
        self.chain = [Block(str(int(time)))]
        self.difficulty = 1

    def __repr__(self):
        resp = []
        for item in self.chain:
            resp.append({
                'data': item.transaction,
                'timestamp': item.timestamp,
                'nonce': item.nonce,
                'hash': item.hash,
                'prevHash': item.prev_hash,
            })
        return json.dumps(resp, indent=4)

    def add_block(self, block):
        # Add block to blockchain
        block.prev_hash = self.get_last_block().hash
        # Recompute hash for new one
        block.hash = block.get_hash()
        block.mine(self.difficulty)
        self.chain.append(block)
        self.difficulty += (-1, 1) \
            [int(time()) - int(self.get_last_block().timestamp) < self.block_time]

    def get_last_block(self) -> object:
        # Take last block
        return self.chain[len(self.chain) - 1]

    def is_valid(self) -> bool:
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            prev_block = self.chain[i-1]

            # Check validation
            if current_block.hash != current_block.get_hash() or \
                prev_block.hash != current_block.prev_hash:
                return False

        return True
