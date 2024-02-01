import hashlib
import json
import datetime
class Block:
    
    def __init__(self, previous_block_hash, data, mongoClient):
        self.previous_block_hash = previous_block_hash
        self.data_list = data
        self.block_data = json.dumps(data)
        # exemple de data : {'from': 2, 'to': 10, 'amount': 100, 'type': 'solar', 'timestamp': 1706792996}
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()
        #on veut l'ajouter dans la base de données mongoDB
        mongoClient.add_data('blockchain', {'block_data': self.block_data, 'block_hash': self.block_hash, 'previous_block_hash': self.previous_block_hash})
    