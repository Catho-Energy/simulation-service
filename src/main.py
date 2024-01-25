from blockchain.blockchain import Blockchain
from mongoClient import MongoDBClient
from model.transaction import Transaction
from flask import Flask, request, jsonify
import json

# Setup the MongoDB client and the blockchain
myClient = MongoDBClient()
myClient.connect()
myblockchain = Blockchain(myClient)

# create a transaction
#t1 = Transaction(1, 2, 10, 100, 'solar')
##t1 = t1.to_dict()
#myblockchain.create_block_from_data(t1)


chain = myblockchain.display_chain()

# Now I want a flask integration 
app = Flask(__name__)
# @app.route('/block', methods=['POST'])
# def create_block():
#     data = request.get_json()
#     myblockchain.create_block_from_data(data)
#     return jsonify({'message': 'Block created'}), 201

@app.route('/chain', methods=['GET'])
def display_chain():
    # Récupérer des données de la base de données
    result = myClient.get_data('blockchain', {})
    
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)