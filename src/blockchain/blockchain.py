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
            #if result is not empty return 
            if item:
                return
        self.chain.append(Block("0", 'Genesis Block', self.mongoClient))

    def last_block(self):
        # retrieve the last block from the database
        result = self.mongoClient.get_last_block()
    
    def create_block_from_data(self, data):
        previous_block_hash = self.last_block()
        print(previous_block_hash)

        self.chain.append(Block(previous_block_hash, data, self.mongoClient))

    def display_chain(self):
        # Récupérer des données de la base de données
        result = self.mongoClient.get_data('blockchain', {})
        # Formater les données pour la réponse JSON
        if result:
            data = []
            for item in result:
                item['_id'] = str(item['_id'])
                # Vérifier si le champ 'block_data' est une chaîne JSON valide
                try:
                    item['block_data'] = json.loads(item['block_data'])
                except json.JSONDecodeError:
                    pass  # Ignore si la conversion n'est pas possible
                data.append(item)
            return jsonify(data)
        else:
            return jsonify({'message': 'Aucune donnée trouvée'}), 404
    

