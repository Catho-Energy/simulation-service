from blockchain.blockchain import Blockchain
from mongoClient import MongoDBClient
from flask import Flask, request, jsonify
from flask_cors import CORS

# Setup the MongoDB client and the blockchain
myClient = MongoDBClient()
myClient.connect()
blockchain = Blockchain(myClient)

# Now I want a flask integration
app = Flask(__name__)
CORS(app, origins=["http://localhost:3005"])


def validate_data(data):
    required_keys = ["from", "to", "amount","price", "type","timestamp"]
    for key in required_keys:
        if key not in data:
            return False
        if key in ["from", "to","timestamp"]:
            if not isinstance(data[key], int):
                return False
        elif key in ["amount", "price",]:
            if not isinstance(data[key], (int, float)):
                return False
        elif key == "type":
            if not isinstance(data[key], str):
                return False
    return True

@app.route('/block', methods=['POST'])
def create_block():
    data = request.get_json()
    if not data or not validate_data(data):
        return jsonify({'message': 'Invalid data'}), 400
    blockchain.create_block_from_data(data)
    return jsonify({'message': 'Block created'}), 201

@app.route('/chain', methods=['GET'])
def display_chain():
    return blockchain.display_chain()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
