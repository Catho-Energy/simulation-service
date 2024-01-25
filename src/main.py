from blockchain.blockchain import Blockchain
from mongoClient import MongoDBClient
from model.transaction import Transaction
from flask import Flask, request, jsonify

# Setup the MongoDB client and the blockchain
myClient = MongoDBClient()
myClient.connect()
myblockchain = Blockchain(myClient)

# create a transaction
t1 = Transaction(1, 2, 10, 100, 'solar')
t1 = t1.to_dict()
myblockchain.create_block_from_data(t1)


chain = myblockchain.display_chain()
for block in chain:
    print(block)

# # Now I want a flask integration 
# app = Flask(__name__)
# @app.route('/block', methods=['POST'])
# def create_block():
#     data = request.get_json()
#     myblockchain.create_block_from_data(data)
#     return jsonify({'message': 'Block created'}), 201

# @app.route('/chain', methods=['GET'])
# def display_chain():
#     chain = myblockchain.display_chain()
#     print(chain)
#     return jsonify({'chain': chain}), 200

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)