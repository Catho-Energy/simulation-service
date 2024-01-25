from blockchain.block import Block

class Blockchain:
    def __init__(self,client):
        self.chain = []
        self.mongoClient = client
        self.generate_genesis_block()

    def generate_genesis_block(self):
        self.chain.append(Block("0", 'Genesis Block', self.mongoClient))
    
    def create_block_from_data(self, data):
        previous_block_hash = self.last_block.block_hash
        self.chain.append(Block(previous_block_hash, data, self.mongoClient))

    def display_chain(self):
        return self.mongoClient.get_data('blockchain',{})

    @property
    def last_block(self):
        return self.chain[-1]