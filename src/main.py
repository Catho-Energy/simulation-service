from blockchain.blockchain import Blockchain
from mongoClient import MongoDBClient
from flask import Flask, request, jsonify


t1 = {
    "type":"user",
    "firstName":"Joe",
    "lastName":"Doe",
}

t2 = {
    "type":"info",
    "consommation": "28.0440000000000",
    "price": "34.6500000000000",
    "production": "15.3140700000000",
    "date": "2021-01-01T00:00:00.000Z"
}
myClient = MongoDBClient()
myClient.connect()
myblockchain = Blockchain(myClient)

myblockchain.create_block_from_data(t1)
myblockchain.create_block_from_data(t2)

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