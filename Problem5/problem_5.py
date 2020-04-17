import hashlib
from datetime import datetime

class Block:
    def __init__(self, timestamp, data, previous_hash=0):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash=previous_hash
        self.hash=self.calc_hash()
        self.next=None

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = str(self.data).encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

    def get_utc_time(self):
        return self.timestamp

    def get_hash(self):
        return self.hash

class BlockChain:
    def __init__(self):
        self.chain_dict=dict()
        self.head = None
        self.tail = None
        self.size = 0

    def add_block(self, data):
        if self.head is None:
            block=Block(datetime.utcnow(), data)
            self.head=block
            self.tail=block
            self.chain_dict[block.get_hash()]=block
            self.size+= 1
            return
        prev_hash=self.chain_dict[self.tail.get_hash()]
        block=Block(datetime.utcnow(), data, prev_hash)
        self.tail.next=block
        self.tail=self.tail.next
        current_hash = block.get_hash()
        self.chain_dict[current_hash]=block
        self.size+= 1
        return

    def print_blockchain(self):
        head=self.head
        while head is not None:
            string='--------------\n'
            string+=" Address of Node: {}\n Hash: {}\n Data: {}\n Timestamp: {}\n Previous Hash: {} \n ".format(head, head.get_hash(), head.data, head.timestamp, head.previous_hash)
            head=head.next
            print(string)
#----------------------------Test Case---------------------------------------
chain=BlockChain()
chain.add_block("Hello, Alok")
chain.add_block("You done well")
chain.add_block("I know you will complete this course")
#----------print BlockChain
chain.print_blockchain()
