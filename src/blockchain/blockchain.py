from blockchain.block import Block
import json
from flask import jsonify
class Blockchain:
    def __init__(self,client):
        self.chain = []
        self.mongoClient = client
        self.generate_genesis_block()

    def generate_genesis_block(self):
        #check if the blockchain is empty
        result = self.mongoClient.get_data('blockchain', {
            'previous_block_hash': '0'
        })
        for item in result:
            print(item)
            #if result is not empty return 
            if item:
                return
        self.chain.append(Block("0", 'Genesis Block', self.mongoClient))
    
    def create_block_from_data(self, data):
        previous_block_hash = self.last_block.block_hash
        self.chain.append(Block(previous_block_hash, data, self.mongoClient))

    def display_chain(self):
        #get the chain from the database
        chain = self.mongoClient.get_data('blockchain', {})
        #format the data for the JSON response
        if chain:
            data = []
            for item in chain:
                item['_id'] = str(item['_id'])
                data.append(item)
            return data
        else:
            return {'message': 'No data found'}, 404
    

    @property
    def last_block(self):
        return self.chain[-1]